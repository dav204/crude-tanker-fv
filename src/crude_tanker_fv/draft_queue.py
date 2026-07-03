"""Filing packet draft queue (WO2 2.4a) — authorize-a-batch, one keystroke.

Lists staged filings (state/edgar_manifest.jsonl) that have NO packet yet and,
on confirmation, drains the queue by invoking headless Claude once per filing
with the /filing-packet skill. This is the 2.4a stage: a HUMAN presses the
key; the drafter itself writes only packets + .draft YAMLs (the skill's hard
rules). Stage 2.4b (unattended autodraft under a hardened profile) ships only
as a documented, gated option after a clean season — see the commented block
at the bottom; CLAUDE.md carries the category definition.

  python -m crude_tanker_fv.draft_queue           # show the queue
  python -m crude_tanker_fv.draft_queue --run     # confirm + drain it
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "state" / "edgar_manifest.jsonl"
DECISIONS = ROOT / "decisions"

QUARTERLY_FORMS = {"6-K", "6-K/A", "10-Q", "10-Q/A", "20-F", "20-F/A"}


def pending_packets() -> list[dict]:
    """Staged quarterly filings with no reconciliation packet dated on/after
    their arrival. One entry per (ticker) — newest filing wins."""
    if not MANIFEST.exists():
        return []
    newest: dict[str, dict] = {}
    for line in MANIFEST.read_text().splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("form") in QUARTERLY_FORMS and e.get("staged_path"):
            cur = newest.get(e["ticker"])
            if cur is None or str(e.get("filed")) > str(cur.get("filed")):
                newest[e["ticker"]] = e
    out = []
    for ticker, e in sorted(newest.items()):
        packets = sorted(DECISIONS.glob(
            f"{ticker.lower()}_reconciliation_prereg_*.md"))
        have = packets and packets[-1].name.split("_")[-1][:10] >= str(e.get("filed"))
        if not have:
            out.append(e)
    return out


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(description="filing-packet draft queue (2.4a)")
    ap.add_argument("--run", action="store_true",
                    help="drain the queue via headless Claude (one confirm)")
    args = ap.parse_args(argv)

    queue = pending_packets()
    if not queue:
        print("draft_queue: no staged filings awaiting a packet.")
        return 0
    print(f"draft_queue: {len(queue)} filing(s) awaiting a packet:")
    for e in queue:
        print(f"  {e['ticker']:6s} {e['form']:6s} filed {e['filed']}  {e['staged_path']}")
    if not args.run:
        print("\nre-run with --run to draft them (one confirmation, whole batch).")
        return 0

    ans = input(f"\nDraft {len(queue)} packet(s) via headless Claude? [y/N] ").strip().lower()
    if ans != "y":
        print("aborted — nothing drafted.")
        return 1
    failures = 0
    for e in queue:
        prompt = f"/filing-packet {e['ticker']} {e['accession']}"
        print(f"\n=== drafting {e['ticker']} ({e['accession']}) ...")
        rc = subprocess.run(
            ["claude", "-p", prompt, "--allowedTools",
             "Read,Grep,Glob,Write,Edit"],
            cwd=ROOT).returncode
        if rc != 0:
            failures += 1
            print(f"    FAILED (rc {rc}) — draft it interactively", file=sys.stderr)
    print(f"\ndraft_queue: done, {len(queue) - failures}/{len(queue)} drafted "
          f"({date.today()}). Review the packets; promotion stays human.")
    return 1 if failures else 0


# --- 2.4b (GATED, ships disabled) -------------------------------------------
# Unattended autodraft: on FILING-LANDED, a launchd hook runs the same
# headless invocation under a hardened profile — read staging + write packets
# only, no Bash/git/web, turn and wall-clock caps, packet schema validation
# before the "ready" page, per-run cost logging. Category (CLAUDE.md):
# "constrained agent, unattended, zero authority". DO NOT ENABLE before a
# clean 2.4a season + owner sign-off; enabling = uncommenting a wrapper that
# does not exist yet, deliberately.
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    sys.exit(main())
