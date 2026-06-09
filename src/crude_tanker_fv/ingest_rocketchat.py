"""Multi-source Rocket.Chat ingest, driven by ``inputs/rocketchat_sources.yaml``.

For each source defined in the YAML:
  - kind=file  →  download matching attachments under ``dest_dir/YYYY/MM/<date>_<name>``
  - kind=text  →  parse with a registered parser and upsert into a CSV time-series

State (per-source cursor) lives in ``state/rocketchat_ingest.json`` (gitignored).

Usage::

    # Incremental update of every source (default).
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat

    # Walk full channel history for all sources.
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --backfill

    # Restrict to one source (handy when backfilling).
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --source baltic_indexes --backfill

    # Diagnostics (don't touch state).
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --profile 30
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --inspect-sender John.Pace --days 14
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from crude_tanker_fv import baltic_parser
from crude_tanker_fv.rocketchat_api import (
    auth_headers,
    download,
    inspect_sender,
    iter_history,
    message_attachments,
    profile_senders,
    resolve_room_id,
)

ROOT = Path(__file__).resolve().parents[2]
STATE_FILE = ROOT / "state" / "rocketchat_ingest.json"
CONFIG_FILE = ROOT / "inputs" / "rocketchat_sources.yaml"

# How often to checkpoint text-source CSVs to disk during a walk. Each flush
# writes the accumulated rows so an interrupted backfill keeps its progress.
# State cursor is NOT advanced until the walk completes naturally (otherwise a
# mid-walk crash would mark the cursor at the newest message seen and skip
# everything older on resume).
FLUSH_INTERVAL = 200


def load_config() -> dict:
    return yaml.safe_load(CONFIG_FILE.read_text())


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True))


def _senders_of(source: dict) -> list[str]:
    return source.get("senders") or [source["sender"]]


def _msg_dt(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


# ---------- file-kind ingest ----------

def _handle_file_source(
    source: dict,
    msg: dict,
    when: datetime,
    host: str,
    headers: dict[str, str],
    dry_run: bool,
    counters: dict[str, int],
) -> None:
    accept = set(source.get("accept") or [])
    dest_dir = ROOT / source["dest_dir"]
    for url_path, name, kind in message_attachments(msg):
        if kind not in accept:
            continue
        dest = (
            dest_dir
            / when.strftime("%Y")
            / when.strftime("%m")
            / f"{when.strftime('%Y-%m-%d')}_{name}"
        )
        rel = dest.relative_to(ROOT)
        if dry_run:
            print(f"[{source['name']}] dry-run → {rel}")
            counters["would_download"] += 1
            continue
        if download(host, url_path, dest, headers):
            print(f"[{source['name']}] downloaded → {rel}")
            counters["downloaded"] += 1
        else:
            counters["skipped"] += 1


# ---------- text-kind ingest (in-memory accumulator) ----------

PARSERS = {"baltic_indexes": baltic_parser}


def _baltic_columns() -> list[str]:
    return ["date", *baltic_parser.INDEX_NAMES, "capesize_index", "source_sender"]


def _load_csv(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    out: dict[str, dict] = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            d = row.get("date")
            if d:
                out[d] = row
    return out


def _write_csv(path: Path, rows: dict[str, dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cols = _baltic_columns()
    sorted_rows = sorted(rows.values(), key=lambda r: r["date"])
    tmp = path.with_suffix(path.suffix + ".part")
    with tmp.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted_rows:
            w.writerow({c: r.get(c, "") for c in cols})
    tmp.rename(path)


def _upsert_baltic_row(
    rows: dict[str, dict],
    new: dict,
    sender: str,
    priority: dict[str, int],
) -> bool:
    """Merge a parsed row into the in-memory CSV. Returns True if anything changed."""
    d = new["date"]
    new_pri = priority.get(sender, 0)
    existing = rows.get(d)
    if existing is None:
        rows[d] = {**new, "source_sender": sender}
        return True

    existing_pri = priority.get(existing.get("source_sender", ""), 0)
    changed = False

    # Baltic-5 fields: highest priority sender wins, ties go to the new value.
    for k in baltic_parser.INDEX_NAMES:
        v = new.get(k)
        if v is None:
            continue
        if existing.get(k) in (None, "") or new_pri >= existing_pri:
            if str(existing.get(k, "")) != str(v):
                existing[k] = v
                changed = True

    # Capesize is independent — any contributor's value sticks.
    if new.get("capesize_index") is not None:
        if str(existing.get("capesize_index", "")) != str(new["capesize_index"]):
            existing["capesize_index"] = new["capesize_index"]
            changed = True

    # source_sender tracks the highest-priority Baltic-5 contributor.
    if any(new.get(k) is not None for k in baltic_parser.INDEX_NAMES):
        if new_pri >= existing_pri and existing.get("source_sender") != sender:
            existing["source_sender"] = sender
            changed = True

    return changed


def _handle_text_source(
    source: dict,
    msg: dict,
    when: datetime,
    sender: str,
    text_state: dict,
    counters: dict[str, int],
) -> None:
    parser_name = source.get("parser")
    if parser_name != "baltic_indexes":
        raise SystemExit(f"Unknown text parser '{parser_name}' in source {source['name']}")

    text = msg.get("msg") or ""
    priority: dict[str, int] = source.get("priority") or {}

    rows = text_state["rows"]
    parsed = baltic_parser.parse_baltic_post(text, when)
    if parsed:
        if _upsert_baltic_row(rows, parsed, sender, priority):
            counters["parsed"] += 1
        return

    cap = baltic_parser.parse_capesize_post(text)
    if cap is not None:
        d = when.date().isoformat()
        new_row = {
            "date": d,
            **{n: None for n in baltic_parser.INDEX_NAMES},
            "capesize_index": cap,
        }
        if _upsert_baltic_row(rows, new_row, sender, priority):
            counters["parsed"] += 1


# ---------- main loop ----------

def _select_sources(config: dict, only: str | None) -> list[dict]:
    sources = config.get("sources") or []
    if only:
        sources = [s for s in sources if s["name"] == only]
        if not sources:
            raise SystemExit(f"No source named '{only}' in {CONFIG_FILE.relative_to(ROOT)}")
    return sources


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", help="Process only the named source.")
    ap.add_argument("--backfill", action="store_true", help="Walk full history.")
    ap.add_argument("--since", help="ISO datetime; overrides incremental cursor.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--profile", type=int, metavar="DAYS")
    ap.add_argument("--inspect-sender", metavar="USERNAME")
    ap.add_argument("--days", type=int, default=14, help="With --inspect-sender (default 14).")
    args = ap.parse_args(argv)

    config = load_config()
    host = config.get("host") or os.environ.get("ROCKETCHAT_HOST", "https://rc.seekingalpha.com")
    group = config.get("group") or "value-investor-s-edge"

    headers = auth_headers()
    room_id = resolve_room_id(host, group, headers)

    if args.profile:
        profile_senders(host, room_id, headers, args.profile)
        return 0
    if args.inspect_sender:
        inspect_sender(host, room_id, headers, args.inspect_sender, args.days)
        return 0

    sources = _select_sources(config, args.source)
    state = load_state()

    # Build sender → list of sources lookup
    sender_routes: dict[str, list[dict]] = {}
    for s in sources:
        for sender in _senders_of(s):
            sender_routes.setdefault(sender, []).append(s)

    # Decide the walk cursor: oldest of all involved sources' cursors,
    # or None if any source is fresh / --backfill / --since set.
    cursors = [state.get(s["name"], {}).get("last_seen_ts") for s in sources]
    if args.backfill or None in cursors:
        oldest = None
    elif args.since:
        oldest = args.since
    else:
        oldest = min(cursors)

    # Per-source bookkeeping
    newest_ts: dict[str, str | None] = {
        s["name"]: state.get(s["name"], {}).get("last_seen_ts") for s in sources
    }
    counters: dict[str, dict[str, int]] = {
        s["name"]: {"downloaded": 0, "skipped": 0, "would_download": 0, "parsed": 0}
        for s in sources
    }

    # Lazy-load CSV snapshots for text sources
    text_state: dict[str, dict[str, Any]] = {}
    for s in sources:
        if s["kind"] == "text":
            dest = ROOT / s["dest_file"]
            text_state[s["name"]] = {"path": dest, "rows": _load_csv(dest)}

    def _flush_text_sources() -> None:
        if args.dry_run:
            return
        for s in sources:
            if s["kind"] == "text":
                ts_state = text_state[s["name"]]
                _write_csv(ts_state["path"], ts_state["rows"])

    total_seen = 0
    for msg in iter_history(host, room_id, headers, oldest):
        total_seen += 1
        ts = msg["ts"]
        username = (msg.get("u") or {}).get("username")
        if username and username in sender_routes:
            when = _msg_dt(ts)
            for s in sender_routes[username]:
                cur = newest_ts[s["name"]]
                if cur is None or ts > cur:
                    newest_ts[s["name"]] = ts
                if s["kind"] == "file":
                    _handle_file_source(s, msg, when, host, headers, args.dry_run, counters[s["name"]])
                elif s["kind"] == "text":
                    _handle_text_source(s, msg, when, username, text_state[s["name"]], counters[s["name"]])

        if total_seen % FLUSH_INTERVAL == 0:
            _flush_text_sources()
            print(f"  ... scanned {total_seen} messages so far (last ts {ts})")

    # Final flush after the walk completes naturally.
    _flush_text_sources()

    # Persist cursors
    if not args.dry_run:
        for s in sources:
            if newest_ts[s["name"]]:
                state[s["name"]] = {
                    "last_seen_ts": newest_ts[s["name"]],
                    "last_run_at": datetime.now(timezone.utc).isoformat(),
                }
        save_state(state)

    print(f"\nScanned {total_seen} messages.")
    for s in sources:
        c = counters[s["name"]]
        if s["kind"] == "file":
            print(
                f"  {s['name']:<24} downloaded={c['downloaded']} "
                f"already_present={c['skipped']} dry_run={c['would_download']}"
            )
        else:
            rows = text_state[s["name"]]["rows"]
            print(
                f"  {s['name']:<24} parsed_or_updated={c['parsed']} "
                f"total_rows={len(rows)} → {s['dest_file']}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
