"""Filings triage ledger (2026-09-11).

    python -m crude_tanker_fv.filings list                      # landed, not yet triaged
    python -m crude_tanker_fv.filings ack <accession> "<disposition>" [--record <path>]

Why: the sentinel flags every arrival for 48 hours and nothing marked one as dealt with, so
a filing triaged on Wednesday paged the owner on Thursday. The owner's rule (2026-09-11): a
page means the owner's action is needed; filings triage is the agent's daily work. This
ledger is the agent's ack — an acked accession drops out of FILING-LANDED, and the daily
triage task records here what it did with each arrival (record-only / calendar / print /
refresh-trigger) and where the record lives.

State lives beside the page-once memory in state/ (gitignored, like the staged filings).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "state" / "filings_triaged.json"
DISPOSITIONS = ("record-only", "calendar", "print", "refresh-trigger", "unreadable", "owner")


def load(path: Path = STATE_PATH) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text()) or {}
    except Exception:
        return {}


def save(data: dict, path: Path = STATE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=1, sort_keys=True))
    tmp.replace(path)


def ack(accession: str, disposition: str, record: str = "", *, by: str = "agent",
        path: Path = STATE_PATH, now: datetime | None = None) -> dict:
    kind = disposition.split(":")[0].strip().lower()
    if kind not in DISPOSITIONS:
        raise SystemExit(f"disposition must start with one of {DISPOSITIONS}; got {disposition!r}")
    data = load(path)
    data[accession] = {"disposition": disposition, "record": record, "by": by,
                       "at": (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")}
    save(data, path)
    return data[accession]


def is_acked(accession: str, path: Path = STATE_PATH) -> bool:
    return accession in load(path)


def unacked(manifest_entries: list, path: Path = STATE_PATH) -> list:
    done = load(path)
    return [e for e in manifest_entries if e.get("accession") and e["accession"] not in done]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="filings triage ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)
    ls = sub.add_parser("list", help="arrivals in the sentinel's 48h window not yet acked")
    ls.add_argument("--all", action="store_true", help="every manifest row, not just the 48h window")
    a = sub.add_parser("ack", help="record a disposition for an accession")
    a.add_argument("accession")
    a.add_argument("disposition", help=f"one of {DISPOSITIONS}, optionally followed by ': detail'")
    a.add_argument("--record", default="", help="path of the decision log / doc that carries the detail")
    a.add_argument("--by", default="agent")
    args = ap.parse_args(argv)

    if args.cmd == "list":
        from .sentinel import _edgar_manifest_entries
        from .loaders import INPUTS_DIR
        rows = unacked(_edgar_manifest_entries(INPUTS_DIR, False)[-80:])
        if not args.all:
            now = datetime.now(timezone.utc)

            def _fresh(e):
                try:
                    return (now - datetime.fromisoformat(str(e.get("ts")))).total_seconds() <= 48 * 3600
                except Exception:
                    return False
            rows = [e for e in rows if _fresh(e)]
        for e in rows:
            print(f"{e.get('filed')}  {e.get('ticker'):5s} {e.get('form'):10s} {e.get('accession')}  "
                  f"{(e.get('title') or e.get('primary_doc') or '')[:60]}")
        print(f"{len(rows)} unacked")
        return 0
    rec = ack(args.accession, args.disposition, args.record, by=args.by, path=STATE_PATH)
    print(f"acked {args.accession}: {rec['disposition']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
