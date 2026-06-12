#!/usr/bin/env python
"""Domain-validated PDF/document fetcher for the IR-report workflow.

The agent-session replacement for the ad-hoc `curl -sSL <url> -o /tmp/x.pdf`
pattern (CLAUDE.md "WebFetch fails on many IR PDFs"). Raw curl can't be
permission-allowlisted narrowly — it reaches any URL and can POST data out —
so this wrapper IS the allowlist, controlled in code:

  - Hosts are taken from inputs/data_sources.yaml (every URL in the file,
    including _market_data_sources) plus EXTRA_HOSTS below for sources
    documented only in CLAUDE.md (Compass weekly). A host not on the list
    is refused before any connection is made. Add sources to
    data_sources.yaml, not here.
  - https only.
  - The one TLS exception lives here, audited: www.okeanisecotankers.com's
    chain fails verification (CLAUDE.md gotcha) — that host, and only that
    host, is fetched with verification disabled.
  - Output is written under /tmp or inside the repo, nowhere else.

Usage:
    .venv/bin/python scripts/fetch_pdf.py <url> [-o /tmp/out.pdf]

Default output: /tmp/<basename of the URL path>. Prints the saved path on
success so the pypdf step can pick it up directly.
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA_SOURCES = ROOT / "inputs" / "data_sources.yaml"

# Sources documented in CLAUDE.md but not per-ticker in data_sources.yaml.
EXTRA_HOSTS = {
    "compassmar.com",
    "www.compassmar.com",
}

# CLAUDE.md gotcha: ECO's domain TLS chain fails verification — curl-equivalent
# behaviour for this one host only. Keep this set as small as it is.
BROKEN_TLS_HOSTS = {"www.okeanisecotankers.com"}

USER_AGENT = "Mozilla/5.0"


def allowed_hosts() -> set[str]:
    """Every hostname appearing in data_sources.yaml, plus EXTRA_HOSTS."""
    hosts = set(EXTRA_HOSTS)
    for m in re.finditer(r"https?://([a-zA-Z0-9.-]+)", DATA_SOURCES.read_text()):
        hosts.add(m.group(1).lower())
    return hosts


def fetch(url: str, out: Path) -> Path:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https":
        sys.exit(f"refused: {parsed.scheme or 'no'} scheme — https only")
    hosts = allowed_hosts()
    if host not in hosts:
        sys.exit(f"refused: {host} is not in inputs/data_sources.yaml — "
                 "add the source there if it's legitimate")

    out = out.resolve()
    tmp = Path("/tmp").resolve()
    if not (out.is_relative_to(tmp) or out.is_relative_to(ROOT)):
        sys.exit(f"refused: output {out} is outside /tmp and the repo")

    ctx = ssl._create_unverified_context() if host in BROKEN_TLS_HOSTS else None
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
        data = resp.read()

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    kind = "PDF" if data.startswith(b"%PDF") else "non-PDF (check before pypdf)"
    print(f"{out}  [{len(data):,} bytes, {kind}]")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Fetch a document from an allowlisted IR/data source")
    ap.add_argument("url")
    ap.add_argument("-o", "--out", help="output path (default /tmp/<url basename>)")
    args = ap.parse_args(argv)
    name = Path(urlparse(args.url).path).name or "download.pdf"
    fetch(args.url, Path(args.out) if args.out else Path("/tmp") / name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
