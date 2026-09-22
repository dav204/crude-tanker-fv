"""Durable accession-based filing triage; only committed dispositions acknowledge work."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "state" / "filings_triaged.json"
DISPOSITIONS = ("record-only", "calendar", "print", "refresh-trigger", "unreadable", "owner")


def load(path=STATE_PATH):
    if not path.exists():
        return {}
    data = json.loads(path.read_text())
    if not isinstance(data, dict) or any(not isinstance(v, dict) for v in data.values()):
        raise ValueError("invalid filings acknowledgment ledger: " + str(path))
    return data


def save(data, path=STATE_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def ack(accession, disposition, record="", *, by="agent", path=STATE_PATH, now=None):
    kind = disposition.split(":")[0].strip().lower()
    if kind not in DISPOSITIONS:
        raise SystemExit(f"disposition must start with one of {DISPOSITIONS}; got {disposition!r}")
    root = path.parent.parent
    rel = Path(record)
    if not record or rel.is_absolute() or ".." in rel.parts or rel.parts[0] != "decisions":
        raise ValueError("ack requires a repository-relative decisions/ record")
    content = subprocess.run(["git", "show", "HEAD:" + rel.as_posix()], cwd=root,
                             capture_output=True, text=True, check=True).stdout
    if accession not in content or disposition not in content:
        raise ValueError("committed record must contain accession and exact disposition")
    data = load(path)
    data[accession] = {"disposition": disposition, "record": record, "by": by,
                      "record_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
                      "at": (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")}
    save(data, path)
    return data[accession]


def is_acked(accession, path=STATE_PATH):
    return accession in load(path)


def unacked(manifest_entries, path=STATE_PATH):
    done = load(path)
    seen = set()
    pending = []
    for entry in manifest_entries:
        accession = entry.get("accession")
        if accession and accession not in done and accession not in seen:
            pending.append(entry)
            seen.add(accession)
    return pending


def parsed_time(value):
    parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("arrival timestamp lacks timezone")
    return parsed


def business_age(start, now):
    days = 0
    cursor = start
    while cursor + timedelta(days=1) <= now:
        cursor += timedelta(days=1)
        days += cursor.weekday() < 5
    return days


def queue(manifest_entries, path=STATE_PATH, now=None):
    now = now or datetime.now(timezone.utc)
    invalid = []
    valid = []
    for i, entry in enumerate(manifest_entries):
        try:
            if not isinstance(entry, dict) or not entry.get("accession"):
                raise ValueError("missing accession")
            parsed_time(entry.get("ts"))
            valid.append(entry)
        except (ValueError, TypeError):
            invalid.append({"row": i + 1, "record": entry})
    pending = unacked(valid, path)
    pending.sort(key=lambda e: (parsed_time(e["ts"]), e["accession"]))
    oldest = pending[0]["ts"] if pending else None
    # Invalid arrivals cannot disappear merely because their timestamp is unreadable.
    for item in invalid:
        entry = item["record"]
        if isinstance(entry, dict) and entry.get("accession") and entry["accession"] not in load(path):
            if not any(e["accession"] == entry["accession"] for e in pending):
                pending.append(entry)
    return {"pending": pending, "pending_total": len(pending), "oldest_arrival": oldest,
            "oldest_business_days": business_age(parsed_time(oldest), now) if oldest else None,
            "invalid": invalid}


def manifest(root=ROOT):
    source = root / "state/edgar_manifest.jsonl"
    if source.exists():
        entries = []
        for index, line in enumerate(source.read_text().splitlines()):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                entry = {"invalid_manifest_line": index + 1}
            entries.append(entry)
        return entries
    snapshot = root / "inputs/filings/_manifest.json"
    if not snapshot.exists():
        return []
    entries = json.loads(snapshot.read_text())
    if not isinstance(entries, list):
        raise ValueError("filing manifest must be an array")
    return entries


def record_dispositions(items, root=ROOT):
    from .runtime import locked, commit_paths
    path = root / "decisions/filings_triage_log.md"
    state = root / "state/filings_triaged.json"
    known = {e.get("accession"): e for e in manifest(root) if isinstance(e, dict)}
    with locked(root / "state/filings.lock"):
        rows = []
        for item in items:
            acc, disposition = item["accession"], item["disposition"]
            if acc not in known or disposition.split(":")[0] not in DISPOSITIONS:
                raise ValueError("unknown accession or disposition")
            if any(c in acc + disposition for c in "\n\r|"):
                raise ValueError("triage cells cannot contain newlines or pipes")
            entry = known[acc]
            rows.append(f"| {datetime.now(timezone.utc).date()} | {entry.get('ticker', '')} | {acc} | {entry.get('filed', '')} | {disposition} | this line |")
        text = path.read_text() if path.exists() else "# Filings triage log\n"
        for row in rows:
            if row not in text:
                text = text.rstrip() + "\n" + row + "\n"
        path.write_text(text)
        commit_paths(root, [str(path.relative_to(root))], "filings triage: committed dispositions")
        for item in items:
            ack(item["accession"], item["disposition"], str(path.relative_to(root)), path=state)
            if item["disposition"].startswith("owner:"):
                from .delivery import enqueue
                enqueue("[crude-fv] PAGE: filing requires owner decision", item["accession"] + "\n" + item["disposition"] +
                        "\nEvidence: decisions/filings_triage_log.md\nACTION: OWNER — resolve the stated filing decision.", root / "state")
    return len(items)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    ls = sub.add_parser("list")
    ls.add_argument("--all", action="store_true", help="compatibility: all pending work is always retained")
    ls.add_argument("--json", action="store_true")
    ls.add_argument("--limit", type=int)
    a = sub.add_parser("ack")
    a.add_argument("accession"); a.add_argument("disposition")
    a.add_argument("--record", required=True); a.add_argument("--by", default="agent")
    sub.add_parser("record", help="commit and acknowledge JSON disposition array from stdin")
    args = ap.parse_args(argv)
    try:
        if args.cmd == "list":
            result = queue(manifest(STATE_PATH.parent.parent), STATE_PATH)
            rows = result["pending"] if args.limit is None else result["pending"][:max(0, args.limit)]
            if args.json:
                print(json.dumps(dict(result, pending=rows), indent=2))
            else:
                for e in rows:
                    print(f"{e.get('filed')} {e.get('ticker', ''):5s} {e.get('form', ''):10s} {e['accession']} {(e.get('title') or e.get('primary_doc') or '')[:60]}")
                print(f"{result['pending_total']} unacked; oldest={result['oldest_arrival']}; invalid={len(result['invalid'])}")
            return 1 if result["invalid"] else 0
        if args.cmd == "record":
            print(f"recorded {record_dispositions(json.load(sys.stdin))} dispositions")
        else:
            rec = ack(args.accession, args.disposition, args.record, by=args.by, path=STATE_PATH)
            print(f"acked {args.accession}: {rec['disposition']}")
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print("FILING-QUEUE-INVALID: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
