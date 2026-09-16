"""The fork registry (inputs/forks.yaml) as a tool, not just a file (2026-09-13).

    python -m crude_tanker_fv.forks list [--all]          # executable today (open, execute_after passed)
    python -m crude_tanker_fv.forks mark <id> <status> --note "..."
    python -m crude_tanker_fv.forks open --id X --kind judgment --doc D --recommendation "..." [--days 3]

Why: the 2026-09-10 policy says silence executes the recommendation, and the sentinel pages
FORK-EXECUTABLE when a window closes — but the executing agent was always a chat session. The
daily task crude-fv-fork-executor now executes them, and the land lane registers a fork for a
flip toward BUY instead of freezing forever. Edits are TEXTUAL (the file is full of dated
comments a YAML round-trip would destroy): a status line is rewritten in place, a new fork is
appended as a block.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml

from .loaders import INPUTS_DIR

FORKS_PATH = INPUTS_DIR / "forks.yaml"
STATUSES = ("open", "executed", "halted", "blocked-ask-tier", "closed")


def load(path: Path = FORKS_PATH) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def add_business_days(start: date, n: int) -> date:
    d = start
    while n > 0:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def executable(today: date | None = None, path: Path = FORKS_PATH, *,
               include_needs_code: bool = False) -> list[dict]:
    """Open forks past their window. A fork flagged `needs_code: true` is excluded by default:
    its recommendation includes a src/ or tests/ change the scheduled executor may not make,
    so it is a chat's to land (2026-09-16 — CMBT cost the executor a full run discovering it)."""
    today = today or date.today()
    out = []
    for f in load(path).get("forks") or []:
        if str(f.get("status", "open")) != "open" or not f.get("execute_after"):
            continue
        if f.get("needs_code") and not include_needs_code:
            continue
        if date.fromisoformat(str(f["execute_after"])) <= today:
            out.append(f)
    return out


def needs_chat(today: date | None = None, path: Path = FORKS_PATH) -> list[dict]:
    """Open forks past their window that need a code change — a chat lands them."""
    today = today or date.today()
    return [f for f in load(path).get("forks") or []
            if str(f.get("status", "open")) == "open" and f.get("needs_code") and f.get("execute_after")
            and date.fromisoformat(str(f["execute_after"])) <= today]


def set_needs_code(fork_id: str, *, path: Path = FORKS_PATH, note: str = "") -> None:
    """Flag an existing fork textually (comments survive): a `needs_code: true` line after `doc:`."""
    text = path.read_text()
    m = re.search(rf"^  - id: {re.escape(fork_id)}[ \t]*(?:#[^\n]*)?\n(.*?)(?=^  - id: |\Z)",
                  text, flags=re.S | re.M)
    if not m:
        raise SystemExit(f"fork {fork_id!r} not found in {path}")
    block = m.group(0)
    if re.search(r"^    needs_code:", block, flags=re.M):
        return
    line = "    needs_code: true" + (f"   # {note}" if note else "") + "\n"
    new_block, n = re.subn(r"(^    doc: [^\n]*\n)", lambda mm: mm.group(1) + line, block, count=1, flags=re.M)
    if n == 0:
        new_block = block.rstrip("\n") + "\n" + line
    path.write_text(text.replace(block, new_block, 1))


def find(fork_id: str, path: Path = FORKS_PATH) -> dict | None:
    return next((f for f in load(path).get("forks") or [] if f.get("id") == fork_id), None)


def mark(fork_id: str, status: str, note: str = "", *, path: Path = FORKS_PATH,
         today: date | None = None) -> None:
    if status not in STATUSES:
        raise SystemExit(f"status must be one of {STATUSES}")
    text = path.read_text()
    m = re.search(rf"^  - id: {re.escape(fork_id)}[ \t]*(?:#[^\n]*)?\n(.*?)(?=^  - id: |\Z)",
                  text, flags=re.S | re.M)
    if not m:
        raise SystemExit(f"fork {fork_id!r} not found in {path}")
    block = m.group(0)
    stamp = (today or date.today()).isoformat()
    comment = f"   # {stamp}" + (f" — {note}" if note else "")
    new_block, n = re.subn(r"^    status: .*$", f"    status: {status}{comment}", block, count=1, flags=re.M)
    if n == 0:
        new_block = block.rstrip("\n") + f"\n    status: {status}{comment}\n"
    path.write_text(text.replace(block, new_block, 1))


def open_fork(fork_id: str, *, kind: str, doc: str, recommendation: str, days: int = 3,
              opened: date | None = None, path: Path = FORKS_PATH, needs_code: bool = False) -> dict:
    if find(fork_id, path):
        raise SystemExit(f"fork {fork_id!r} already exists")
    opened = opened or date.today()
    ea = opened if kind == "state-tracking" else add_business_days(opened, days)
    rec = recommendation.replace('"', "'").replace("\n", " ")
    nc = "    needs_code: true   # the recommendation includes a src/ or tests/ change — a chat lands it, not the executor\n" if needs_code else ""
    block = (f"  - id: {fork_id}\n    kind: {kind}\n    doc: {doc}\n{nc}    opened: {opened.isoformat()}\n"
             f"    execute_after: {ea.isoformat()}\n    recommendation: \"{rec}\"\n    status: open\n")
    text = path.read_text()
    path.write_text(text.rstrip("\n") + "\n" + block)
    return {"id": fork_id, "kind": kind, "doc": doc, "opened": opened.isoformat(), "needs_code": needs_code,
            "execute_after": ea.isoformat(), "recommendation": rec, "status": "open"}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="the fork registry")
    sub = ap.add_subparsers(dest="cmd", required=True)
    ls = sub.add_parser("list")
    ls.add_argument("--all", action="store_true", help="every fork, not just the executable ones")
    mk = sub.add_parser("mark")
    mk.add_argument("id")
    mk.add_argument("status", choices=STATUSES)
    mk.add_argument("--note", default="")
    op = sub.add_parser("open")
    op.add_argument("--id", required=True)
    op.add_argument("--kind", default="judgment", choices=["judgment", "state-tracking"])
    op.add_argument("--doc", required=True)
    op.add_argument("--recommendation", required=True)
    op.add_argument("--days", type=int, default=3)
    op.add_argument("--needs-code", action="store_true",
                    help="the recommendation includes a src/ or tests/ change: a chat lands it, the executor skips it")
    nc = sub.add_parser("needs-code", help="flag an existing fork as needing a code change")
    nc.add_argument("id")
    nc.add_argument("--note", default="")
    args = ap.parse_args(argv)

    if args.cmd == "list":
        rows = (load().get("forks") or []) if args.all else executable()
        for f in rows:
            tag = "   NEEDS A CHAT (code change)" if f.get("needs_code") else ""
            print(f"{f.get('id'):40s} {str(f.get('status','open')):18s} execute_after {f.get('execute_after')}  "
                  f"kind {f.get('kind','judgment')}  doc {f.get('doc')}{tag}")
            print(f"    {str(f.get('recommendation'))[:300]}")
        print(f"{len(rows)} fork(s)" + ("" if args.all else " executable today"))
        chat = [] if args.all else needs_chat()
        if chat:
            print(f"{len(chat)} fork(s) past their window NEED A CHAT (code change) — not the executor's: "
                  + ", ".join(f.get("id") for f in chat))
        return 0
    if args.cmd == "mark":
        mark(args.id, args.status, args.note)
        print(f"marked {args.id}: {args.status}")
        return 0
    if args.cmd == "needs-code":
        set_needs_code(args.id, note=args.note)
        print(f"flagged {args.id}: needs_code")
        return 0
    f = open_fork(args.id, kind=args.kind, doc=args.doc, recommendation=args.recommendation,
                  days=args.days, needs_code=args.needs_code)
    print(f"opened {f['id']}: executes after {f['execute_after']}" + (" — NEEDS A CHAT" if args.needs_code else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
