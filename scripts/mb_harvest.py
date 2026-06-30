#!/usr/bin/env python3
"""Archive MB Shipbrokers weekly PDFs from their cdn.flxml.eu download links.

The MECHANICAL half of the MB harvest. The Gmail link-extraction is the AGENT half
(an authed Gmail session — see WORKFLOWS.md "Harvest the MB Shipbrokers weeklies").

Reads TSV lines from a file arg or stdin:

    <YYYY-MM-DD>\\t<email subject>\\t<cdn.flxml.eu Download-report url>

derives the feed + week from the subject, fetches via scripts/fetch_pdf.py (cdn.flxml.eu
is allowlisted in data_sources.yaml), validates the %PDF header, and archives under
  inputs/research_mb/<feed>/<YYYY>/<date>_<Feed>_Weekly_<NN>_<YYYY>.pdf
(the research_mb tree is gitignored broker cache — local-for-use, not committed).

Usage:  python scripts/mb_harvest.py links.tsv      (or: ... | python scripts/mb_harvest.py)
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FEEDS = {  # subject keyword -> (archive subdir, filename token)
    "container": ("container_weekly", "Container"),
    "tanker": ("tanker_weekly", "Tanker"),
    "dry bulk": ("dry_bulk_weekly", "Dry_Bulk"),
    "lng": ("lng_weekly", "LNG"),
}


def parse(subject: str) -> tuple[tuple[str, str], str]:
    s = subject.lower()
    feed = next((k for k in FEEDS if k in s), None)
    m = re.search(r"weekly\s+(\d+)", s)
    if not feed or not m:
        raise ValueError(f"cannot parse feed/week from subject: {subject!r}")
    return FEEDS[feed], m.group(1)


def main() -> None:
    src = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    for raw in src:
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        date, subject, url = raw.split("\t", 2)
        (subdir, token), wk = parse(subject)
        year = date[:4]
        out = REPO / "inputs/research_mb" / subdir / year / f"{date}_{token}_Weekly_{wk}_{year}.pdf"
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            print(f"skip (exists) {out.name}")
            continue
        subprocess.run([str(REPO / ".venv/bin/python"), str(REPO / "scripts/fetch_pdf.py"), url],
                       capture_output=True, text=True)
        base = url.rsplit("/", 1)[-1]
        tmp = next((p for p in (Path("/private/tmp") / base, Path("/tmp") / base) if p.exists()), None)
        if tmp is None:
            print(f"FAIL fetch {subject}")
            continue
        if tmp.read_bytes()[:4] != b"%PDF":
            print(f"FAIL not-pdf {subject}")
            continue
        shutil.copy(tmp, out)
        print(f"OK {out.relative_to(REPO)} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
