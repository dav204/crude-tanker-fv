"""Shared, well-behaved HTTP. Per-host throttling, retry/backoff, optional
robots.txt enforcement. Used by both crawl and download so politeness is
applied in exactly one place.
"""
from __future__ import annotations

import time
import urllib.robotparser as robotparser
from urllib.parse import urlparse

import requests

from .config import REQUEST_POLICY, RequestPolicy


class PoliteSession:
    def __init__(self, policy: RequestPolicy = REQUEST_POLICY):
        self.policy = policy
        self.session = requests.Session()
        self.session.headers["User-Agent"] = policy.user_agent
        self._last_hit: dict[str, float] = {}     # host -> monotonic ts
        self._robots: dict[str, robotparser.RobotFileParser | None] = {}

    # -- robots --------------------------------------------------------------
    def _robots_for(self, host_url: str) -> robotparser.RobotFileParser | None:
        host = urlparse(host_url).netloc
        if host not in self._robots:
            rp = robotparser.RobotFileParser()
            robots_url = f"{urlparse(host_url).scheme}://{host}/robots.txt"
            try:
                rp.set_url(robots_url)
                rp.read()
                self._robots[host] = rp
            except Exception:
                self._robots[host] = None  # fail open: can't read robots
        return self._robots[host]

    def allowed(self, url: str) -> bool:
        if not self.policy.respect_robots:
            return True
        rp = self._robots_for(url)
        if rp is None:
            return True
        return rp.can_fetch(self.policy.user_agent, url)

    # -- throttle ------------------------------------------------------------
    def _throttle(self, url: str) -> None:
        host = urlparse(url).netloc
        now = time.monotonic()
        last = self._last_hit.get(host)
        if last is not None:
            wait = self.policy.min_interval_s - (now - last)
            if wait > 0:
                time.sleep(wait)
        self._last_hit[host] = time.monotonic()

    # -- get -----------------------------------------------------------------
    def get(self, url: str, *, expect: str | None = None, **kw) -> requests.Response:
        """GET with throttle + retries. `expect` optionally asserts a substring
        of the Content-Type (e.g. 'pdf', 'json')."""
        if not self.allowed(url):
            raise PermissionError(f"robots.txt disallows: {url}")
        last_exc: Exception | None = None
        for attempt in range(self.policy.max_retries):
            self._throttle(url)
            try:
                resp = self.session.get(url, timeout=self.policy.timeout_s, **kw)
                if resp.status_code in (429, 500, 502, 503, 504):
                    raise requests.HTTPError(f"{resp.status_code} on {url}")
                resp.raise_for_status()
                if expect and expect not in resp.headers.get("Content-Type", ""):
                    # not fatal -- some servers mislabel; caller decides
                    pass
                return resp
            except Exception as e:  # noqa: BLE001 -- we want to retry broadly
                last_exc = e
                time.sleep(self.policy.backoff_base_s * (2 ** attempt))
        raise RuntimeError(f"GET failed after retries: {url}") from last_exc
