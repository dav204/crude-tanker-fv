"""Multi-source Rocket.Chat ingest, driven by ``inputs/rocketchat_sources.yaml``.

For each source defined in the YAML:
  - kind=file  →  download matching attachments under ``dest_dir/YYYY/MM/<date>_<name>``
(The kind=text lane — Baltic index posts parsed into a CSV — was retired 2026-09-02;
prune ledger rows 4-5.)

State (per-source cursor) lives in ``state/rocketchat_ingest.json`` (gitignored).

Usage::

    # Incremental update of every source (default).
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat

    # Walk full channel history for all sources.
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --backfill

    # Restrict to one source (handy when backfilling).
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --source pareto_research --backfill

    # Diagnostics (don't touch state).
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --profile 30
    .venv/bin/python -m crude_tanker_fv.ingest_rocketchat --inspect-sender John.Pace --days 14
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

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

# Progress-print cadence during a walk. The state cursor is NOT advanced until
# the walk completes naturally (a mid-walk crash would otherwise mark the cursor
# at the newest message seen and skip everything older on resume).
PROGRESS_INTERVAL = 200


def load_config() -> dict:
    return yaml.safe_load(CONFIG_FILE.read_text())


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict) -> None:
    # Atomic (WO2 1.1, invariant 10): a half-written cursor after a crash is a
    # silent-reset seed. Same temp+rename pattern as _write_csv below.
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".json.part")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True))
    tmp.replace(STATE_FILE)


def _senders_of(source: dict) -> list[str]:
    return source.get("senders") or [source["sender"]]


def _decide_oldest(since: str | None, backfill: bool,
                   cursors: list[str | None]) -> str | None:
    """--since BINDS even when a source has no cursor (2026-07-27 fix).

    The old precedence put ``None in cursors`` first, so a cursor-less
    source silently discarded --since and walked unbounded — hit the WO2
    1.1 cap, exited 3 without persisting, and wedged the scheduled runs
    behind the CURSOR-RESET guard for three days (baltic_capesize_table
    bootstrap, 2026-07-24 -> 27). An explicit bound outranks everything;
    --backfill is the only sanctioned unbounded walk.
    """
    if since:
        return since
    if backfill or None in cursors:
        return None
    return min(cursors)


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
            # Arrival validation at staging (WO2 1.5, invariant 6): a PDF that
            # isn't one moves to _quarantine/ + flags via the arrival ledger;
            # identity = RC message id (invariant 4). Images pass through
            # ledger-only (no PDF magic to check).
            from .arrivals import record_arrival, stage_pdf

            identity = f"rc:{msg.get('_id', 'unknown')}"
            if kind == "pdf":
                ok, final = stage_pdf(dest, source["name"], identity,
                                      state_dir=ROOT / "state")
                if not ok:
                    print(f"[{source['name']}] QUARANTINED (not a valid pdf) → "
                          f"{final.relative_to(ROOT)}")
                    counters["quarantined"] = counters.get("quarantined", 0) + 1
                    continue
            else:
                record_arrival(source["name"], identity, "staged", str(rel),
                               state_dir=ROOT / "state")
            print(f"[{source['name']}] downloaded → {rel}")
            counters["downloaded"] += 1
        else:
            counters["skipped"] += 1


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
    ap.add_argument("--max-messages", type=int, default=5000, metavar="N",
                    help="Sanity cap on one walk (WO2 1.1): an incremental run "
                         "hitting this means a blown cursor or a runaway walk — "
                         "stop WITHOUT advancing cursors and exit 3. 0 = uncapped "
                         "(deliberate backfills).")
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
    if not args.backfill and not args.since and state and None in cursors:
        # WO2 1.1 cursor-reset guard: a plain incremental run with a known
        # state file but a missing per-source cursor would silently re-crawl
        # ALL history (oldest=None). A reset is an event, not a default —
        # flag it and make the full walk a deliberate --backfill.
        missing = [s["name"] for s in sources
                   if not state.get(s["name"], {}).get("last_seen_ts")]
        print(f"CURSOR-RESET: no cursor for {', '.join(missing)} in {STATE_FILE} — "
              "refusing the implicit full-history walk. Re-run with --backfill "
              "(deliberate) or --since <ISO> (bounded).", file=sys.stderr)
        return 3
    oldest = _decide_oldest(args.since, args.backfill, cursors)

    # Per-source bookkeeping
    newest_ts: dict[str, str | None] = {
        s["name"]: state.get(s["name"], {}).get("last_seen_ts") for s in sources
    }
    counters: dict[str, dict[str, int]] = {
        s["name"]: {"downloaded": 0, "skipped": 0, "would_download": 0}
        for s in sources
    }

    total_seen = 0
    capped = False
    for msg in iter_history(host, room_id, headers, oldest):
        if args.max_messages and total_seen >= args.max_messages:
            # The walk runs newest→oldest: a capped walk has NOT seen the
            # older tail, so cursors must not advance (they'd skip it forever).
            # Flush what landed, refuse the cursor, exit loud.
            capped = True
            break
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
                else:
                    raise SystemExit(f"unknown source kind {s['kind']!r} for {s['name']} "
                                     "(the text lane was retired 2026-09-02)")

        if total_seen % PROGRESS_INTERVAL == 0:
            print(f"  ... scanned {total_seen} messages so far (last ts {ts})")

    if capped:
        print(f"MAX-MESSAGES: walk capped at {args.max_messages} without finishing — "
              "cursors NOT advanced (downloads/CSV rows kept; idempotent re-run "
              "is safe). Blown cursor, or raise --max-messages for a deliberate "
              "backfill.", file=sys.stderr)
        return 3

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
        print(
            f"  {s['name']:<24} downloaded={c['downloaded']} "
            f"already_present={c['skipped']} dry_run={c['would_download']}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
