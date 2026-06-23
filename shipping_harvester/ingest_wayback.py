"""Ingest the Wayback-recovered Allied Weekly PDFs (2019-2020) into the marks store.

Separate from the HSN/Capital-Link crawl path: these PDFs were recovered by
wayback_allied.py, dated by their upload-path month. For each quarter we select
the latest issue on/<= quarter-end and only keep it if it is within ~one quarter
(no heavily-stale reuse), parse it with the Allied Weekly parser, and store the
marks under data/marks/allied/<quarter>.json so build_panel picks them up.

Run on .venv310:  PYTHONPATH=. ../.venv310/bin/python ingest_wayback.py
"""
from __future__ import annotations

import datetime as dt
import json
import re
from dataclasses import replace
from pathlib import Path

from shipping_harvester import quarters, store
from shipping_harvester.models import ReportRef
from shipping_harvester.parse.allied import AlliedParser

WB = Path("data/wayback/allied")
STALE_DAYS = 100  # skip a quarter whose newest issue is older than ~one quarter


def _date_of(orig: str) -> dt.date | None:
    m = re.search(r"/uploads/(\d{4})/(\d{2})/", orig)
    if not m:
        return None
    return dt.date(int(m.group(1)), int(m.group(2)), 15)


def main() -> int:
    man = json.loads((WB / "manifest.json").read_text())
    refs = []
    for rec in man:
        d = _date_of(rec["orig"])
        if d:
            refs.append((d, WB / rec["file"], rec["orig"]))
    refs.sort()
    parser = AlliedParser()
    saved = 0
    for label in quarters.quarter_range("2019Q1", "2020Q4"):
        qend = quarters.quarter_end(label)
        # newest-first within the stale window; fall back past truncated/empty captures
        cands = sorted((c for c in refs if c[0] <= qend and (qend - c[0]).days <= STALE_DAYS),
                       key=lambda x: x[0], reverse=True)
        for d, f, o in cands:
            ref = ReportRef(broker_id="allied", source="wayback", title=f.name,
                            post_url=o, pdf_url=o, published=d)
            mm = replace(parser.parse(str(f), ref), quarter=label)
            if mm.marks:
                store.save_marks(mm)
                saved += 1
                print(f"  {label}: {len(mm.marks)} marks from {f.name} (dated {d})")
                break
        else:
            if cands:
                print(f"  {label}: NO marks (all {len(cands)} candidate(s) empty/truncated)")
    print(f"\ningested {saved} Allied 2019-2020 quarter mark sets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
