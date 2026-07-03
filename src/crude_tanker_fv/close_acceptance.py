"""WO2 acceptance compiler — the two-week close artifact.

Compiles the evidence streams into outputs/acceptance_wo2_<start>_<end>.md.
Every claim is a JOIN against machine records; a failed join renders as a ❌
row — the artifact can record a FAILED acceptance honestly. Owner-side
receipts (the two demonstrated firings, PAGE acks, attestation) live in
decisions/wo2_acceptance_receipts.yaml, owner-edited; null = ❌ pending.

  python -m crude_tanker_fv.close_acceptance 2026-07-28 2026-08-06

Streams:
1. state/automation_runs.log — zero `manual:` fetch initiators inside the
   window. Designed exceptions (each listed + justified, never silently
   passed): initiator `session:mb-batch` (the Saturday MB Gmail step, R-7)
   and runs note-tagged as the drill.
2. state/arrivals.jsonl — every arrival joined to a disposition; quarantine
   residue = files still sitting in any _quarantine/ dir.
3. state/sentinel.log FLAG lines joined to state/notify_sent.log sends
   (same UTC day). Flags on a day with no send = failed join.
4. FILING-LANDED events in the window + the drill record (decisions/*drill*).
5. ctxprobe appendix (~/ctxprobe.log), owner receipts, attestation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "state"
RECEIPTS = ROOT / "decisions" / "wo2_acceptance_receipts.yaml"

FETCH_JOBS = {"price-refresh", "rocketchat-ingest", "news-pull", "harvester",
              "edgar-poll"}
DESIGNED_INITIATORS = {"session:mb-batch"}   # R-7 — listed, not silently passed


def _in_window(ts: str, start: date, end: date) -> bool:
    try:
        return start <= date.fromisoformat(str(ts)[:10]) <= end
    except ValueError:
        return False


def compile_acceptance(start: date, end: date, root: Path = ROOT) -> "tuple[str, bool]":
    state = root / "state"
    lines = [f"# WO2 acceptance — {start} → {end}", ""]
    ok_all = True

    def row(ok: bool, title: str, detail: str):
        nonlocal ok_all
        ok_all &= ok
        lines.append(f"- {'✅' if ok else '❌'} **{title}** — {detail}")

    # 1. No human fetches.
    ledger = state / "automation_runs.log"
    manual, designed = [], []
    if ledger.exists():
        for ln in ledger.read_text().splitlines():
            m = re.match(r"(\S+) job=(\S+) initiator=(\S+)", ln)
            if not m or not _in_window(m.group(1), start, end):
                continue
            if m.group(2) in FETCH_JOBS and m.group(3).startswith("manual:"):
                manual.append(ln)
            elif m.group(3) in DESIGNED_INITIATORS:
                designed.append(ln)
        row(not manual, "Zero manual fetch initiators",
            f"{len(manual)} manual fetch run(s)" + (f": {manual[:3]}" if manual else
            f"; {len(designed)} designed-exception run(s) (session:mb-batch, R-7)"))
    else:
        row(False, "Zero manual fetch initiators", "no run ledger found")

    # 2. Arrivals joined to dispositions + quarantine residue.
    arrivals = state / "arrivals.jsonl"
    if arrivals.exists():
        rows_ = [json.loads(l) for l in arrivals.read_text().splitlines() if l.strip()]
        in_win = [r for r in rows_ if _in_window(r.get("ts", ""), start, end)]
        undisposed = [r for r in in_win if not r.get("disposition")]
        row(not undisposed, "Every arrival has a disposition",
            f"{len(in_win)} arrival(s), {len(undisposed)} undisposed")
    else:
        row(False, "Every arrival has a disposition", "no arrivals ledger found")
    residue = [p for p in (root / "inputs").rglob("_quarantine/*")
               if p.is_file() and not p.name.endswith(".reason")]
    row(not residue, "Zero quarantine residue",
        f"{len(residue)} file(s) still quarantined" + (f": {[str(p) for p in residue[:3]]}" if residue else ""))

    # 3. Flags joined to sends.
    slog, sent = state / "sentinel.log", state / "notify_sent.log"
    flag_days = set()
    if slog.exists():
        for ln in slog.read_text().splitlines():
            if " FLAG " in ln and _in_window(ln, start, end):
                flag_days.add(ln[:10])
    sent_days = set()
    if sent.exists():
        sent_days = {ln[:10] for ln in sent.read_text().splitlines()
                     if _in_window(ln, start, end)}
    orphans = sorted(flag_days - sent_days)
    row(not orphans, "Every flag day joined to a sent email",
        f"{len(flag_days)} flag day(s); orphaned: {orphans or 'none'}")

    # 4. Filings + drill.
    landed = 0
    if slog.exists():
        landed = sum(1 for ln in slog.read_text().splitlines()
                     if "FILING-LANDED" in ln and _in_window(ln, start, end))
    row(landed > 0, "Real FILING-LANDED events crossed the window",
        f"{landed} landed-event day-line(s) in sentinel.log")
    drills = sorted((root / "decisions").glob("*drill*"))
    row(bool(drills), "Drill record committed",
        drills[-1].name if drills else "no decisions/*drill* record")

    # 5. Owner receipts + ctxprobe + attestation.
    rec = yaml.safe_load(RECEIPTS.read_text()) if RECEIPTS.exists() else {}
    rec = rec or {}
    for key, title in [("healthchecks_firing_demonstrated", "Healthchecks firing demonstrated"),
                       ("action_issue_demonstrated", "Action test issue demonstrated"),
                       ("page_ack_demonstrated", "PAGE→owner-ack demonstrated (one-time channel-latency demo, NOT a standing SLA)")]:
        row(bool(rec.get(key)), title, str(rec.get(key) or "pending owner receipt"))
    probe = Path.home() / "ctxprobe.log"
    row(probe.exists(), "ctxprobe appendix",
        f"{len(probe.read_text().splitlines())} probe line(s)" if probe.exists()
        else "~/ctxprobe.log absent")
    row(bool(rec.get("clean_clone_suite")), "Clean-clone pytest transcript",
        str(rec.get("clean_clone_suite") or "pending (run + record in receipts)"))
    row(bool(rec.get("attestation")), "Owner attestation",
        str(rec.get("attestation") or "pending"))

    lines += ["", f"**VERDICT: {'ACCEPTED' if ok_all else 'NOT ACCEPTED'}** "
                  f"(compiled from machine records; ❌ rows are the work list)"]
    return "\n".join(lines) + "\n", ok_all


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(description="WO2 two-week acceptance compiler")
    ap.add_argument("start", type=date.fromisoformat)
    ap.add_argument("end", type=date.fromisoformat)
    args = ap.parse_args(argv)
    text, ok = compile_acceptance(args.start, args.end)
    out = ROOT / "outputs" / f"acceptance_wo2_{args.start}_{args.end}.md"
    out.write_text(text)
    print(text)
    print(f"-> {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
