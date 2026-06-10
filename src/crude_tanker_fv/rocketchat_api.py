"""Rocket.Chat REST API helpers — auth, room lookup, history iteration,
attachment classification, and diagnostic profilers.

Used by ``ingest_rocketchat`` and by any future Rocket.Chat-backed scripts.
"""

from __future__ import annotations

import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterator
from urllib.parse import quote

import requests

BATCH_SIZE = 100
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tiff")

RETRY_ATTEMPTS = 5
RETRY_INITIAL_DELAY = 5.0  # doubles each attempt: 5s, 10s, 20s, 40s


def _get(url: str, **kwargs) -> requests.Response:
    """GET with retry/backoff. Long history walks span thousands of requests
    and hit transient connection resets (caught live 2026-06-10: reset 54
    killed the first scheduled backfill ~3.6k messages in). Retries
    connection errors, timeouts, 429s, and 5xx; returns 4xx to the caller."""
    delay = RETRY_INITIAL_DELAY
    last_exc: Exception | None = None
    for attempt in range(RETRY_ATTEMPTS):
        try:
            r = requests.get(url, **kwargs)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            last_exc = e
        else:
            if r.status_code != 429 and r.status_code < 500:
                return r
            last_exc = requests.exceptions.HTTPError(f"HTTP {r.status_code} from {url}")
        if attempt < RETRY_ATTEMPTS - 1:
            time.sleep(delay)
            delay *= 2
    raise last_exc


def auth_headers() -> dict[str, str]:
    user_id = os.environ.get("ROCKETCHAT_USER_ID")
    token = os.environ.get("ROCKETCHAT_TOKEN")
    if not user_id or not token:
        sys.exit(
            "Missing credentials. Set ROCKETCHAT_USER_ID and ROCKETCHAT_TOKEN.\n"
            "Create a personal access token at:\n"
            "  https://rc.seekingalpha.com → avatar → My Account → Personal Access Tokens\n"
            "The response when you create it shows both the userId and the token."
        )
    return {"X-Auth-Token": token, "X-User-Id": user_id}


def resolve_room_id(host: str, group: str, headers: dict[str, str]) -> str:
    r = _get(
        f"{host}/api/v1/groups.info",
        params={"roomName": group},
        headers=headers,
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()
    if not data.get("success"):
        raise SystemExit(f"groups.info failed for '{group}': {data}")
    return data["group"]["_id"]


def iter_history(
    host: str,
    room_id: str,
    headers: dict[str, str],
    oldest: str | None,
) -> Iterator[dict]:
    """Yield messages from newest to oldest, paginating until exhausted.

    ``oldest`` is an ISO-8601 string; when set, the server only returns
    messages strictly newer than it (incremental mode).
    """
    latest: str | None = None
    while True:
        params: dict[str, str] = {"roomId": room_id, "count": str(BATCH_SIZE)}
        if latest:
            params["latest"] = latest
        if oldest:
            params["oldest"] = oldest
        r = _get(
            f"{host}/api/v1/groups.history",
            params=params,
            headers=headers,
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        if not data.get("success"):
            raise SystemExit(f"groups.history failed: {data}")
        messages = data.get("messages", [])
        if not messages:
            return
        for msg in messages:
            yield msg
        if len(messages) < BATCH_SIZE:
            return
        latest = messages[-1]["ts"]


def classify_attachment(name: str, mime: str) -> str:
    n = name.lower()
    if mime == "application/pdf" or n.endswith(".pdf"):
        return "pdf"
    if mime.startswith("image/") or any(n.endswith(ext) for ext in IMAGE_EXTS):
        return "image"
    if mime.startswith("video/"):
        return "video"
    return "other"


def message_attachments(msg: dict) -> Iterator[tuple[str, str, str]]:
    """Yield (url_path, filename, kind) for each file on this message.

    Rocket.Chat surfaces uploads in two shapes: a top-level ``file`` for
    single-file messages, and one entry per attachment under ``attachments[]``
    for richer messages. The two overlap, so we prefer ``file`` and only fall
    back to attachments if it's absent.
    """
    f = msg.get("file") or {}
    if f.get("_id"):
        name = f.get("name", "")
        kind = classify_attachment(name, f.get("type", ""))
        yield f"/file-upload/{f['_id']}/{quote(name)}", name, kind
        return

    for att in msg.get("attachments") or []:
        link = att.get("title_link") or ""
        if not link.startswith("/file-upload/"):
            continue
        name = att.get("title") or link.rsplit("/", 1)[-1]
        kind = classify_attachment(name, "")
        yield link, name, kind


def download(host: str, url_path: str, dest: Path, headers: dict[str, str]) -> bool:
    if dest.exists():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    # _get retries the request phase; this loop covers resets mid-body
    # (after headers, during the streamed read).
    for attempt in range(3):
        r = _get(f"{host}{url_path}", headers=headers, timeout=180, stream=True)
        r.raise_for_status()
        try:
            with tmp.open("wb") as out:
                for chunk in r.iter_content(64 * 1024):
                    if chunk:
                        out.write(chunk)
            break
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            if attempt == 2:
                raise
            time.sleep(RETRY_INITIAL_DELAY)
    tmp.rename(dest)
    return True


def _utc_cutoff(days: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)).strftime(
        "%Y-%m-%dT%H:%M:%S.000Z"
    )


def profile_senders(
    host: str,
    room_id: str,
    headers: dict[str, str],
    days: int,
    min_msgs: int = 2,
) -> None:
    """Walk recent messages, group by sender, print what each posts."""
    senders: dict[str, dict] = defaultdict(
        lambda: {
            "display_name": "",
            "msgs": 0,
            "pdf": 0,
            "image": 0,
            "video": 0,
            "other": 0,
            "text_only": 0,
            "samples": [],
            "sample_text": "",
        }
    )
    total = 0
    for msg in iter_history(host, room_id, headers, oldest=_utc_cutoff(days)):
        total += 1
        u = msg.get("u") or {}
        user = u.get("username") or "?"
        s = senders[user]
        s["display_name"] = u.get("name") or s["display_name"]
        s["msgs"] += 1

        attached_kind = None
        attached_name = None
        for _, name, kind in message_attachments(msg):
            attached_kind = kind
            attached_name = name
            break

        if attached_kind:
            s[attached_kind] += 1
            if attached_name and len(s["samples"]) < 3:
                s["samples"].append(attached_name)
        elif msg.get("msg"):
            s["text_only"] += 1
            if not s["sample_text"]:
                s["sample_text"] = msg["msg"][:120].replace("\n", " ")

    rows = sorted(senders.items(), key=lambda x: -x[1]["msgs"])
    print(f"\n=== Last {days}d — {total} messages from {len(rows)} senders ===\n")
    print(
        f"{'username':28s} {'msgs':>5s} {'pdf':>4s} {'img':>4s} "
        f"{'vid':>4s} {'oth':>4s} {'txt':>4s}  display_name / samples"
    )
    print("-" * 110)
    for user, s in rows:
        if s["msgs"] < min_msgs:
            continue
        sample = ""
        if s["samples"]:
            sample = " | " + ", ".join(s["samples"])
        elif s["sample_text"]:
            sample = " | text: " + s["sample_text"]
        print(
            f"{user:28s} {s['msgs']:>5d} {s['pdf']:>4d} {s['image']:>4d} "
            f"{s['video']:>4d} {s['other']:>4d} {s['text_only']:>4d}  "
            f"{s['display_name']}{sample}"
        )


def inspect_sender(
    host: str,
    room_id: str,
    headers: dict[str, str],
    username: str,
    days: int,
) -> None:
    """Print recent messages from one sender — full text + any attached filenames."""
    shown = 0
    for msg in iter_history(host, room_id, headers, oldest=_utc_cutoff(days)):
        if (msg.get("u") or {}).get("username") != username:
            continue
        shown += 1
        ts = msg["ts"]
        text = (msg.get("msg") or "").strip()
        files = [name for _, name, _ in message_attachments(msg)]
        print(f"\n--- {ts} ---")
        if files:
            print(f"  files: {', '.join(files)}")
        if text:
            print(f"  text:  {text[:500]}{'...' if len(text) > 500 else ''}")
    print(f"\n{shown} messages from {username} in last {days}d")
