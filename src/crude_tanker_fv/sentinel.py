"""Read-only cron sentinel (orchestration WO1 V-2, 2026-07-02).

One command that answers "does anything need the owner's eyes?" without
running the pipeline or writing anything (beyond an optional dated log line):

  python -m crude_tanker_fv.sentinel [--log state/sentinel.log]

Checks, all reusing the canonical implementations (never a second copy —
the F-13 rule):
  1. Trigger register — any §13.3 trigger DUE/overdue/FIRED
     (refresh.check_reweight_triggers; upcoming-warns are the weekly digest's
     job, not a page).
  2. Input staleness — market-data files past their per-type thresholds +
     stale watchlist vintages (refresh.check_market_data / check_watchlist_freshness).
  3. Committed-surface coherence — sign/label contradictions in the shipped
     handoff (scorecard.handoff_coherence_flags) + schema presence.
  4. Price basis — prices_daily.yaml fetch age and band-flagged quote count.

Exit 0 = quiet. Nonzero = one status line per flag on stdout. Designed for
cron via scripts/sentinel_cron.sh (which adds the dirty-tree/PAUSE guard —
V-3: no automation through live surgery).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from .loaders import INPUTS_DIR, load_watchlist
from .refresh import (
    check_market_data,
    check_reweight_triggers,
    check_watchlist_freshness,
)
from .report import OUTPUTS_DIR
from .scorecard import handoff_coherence_flags, weight_family_basis

PRICE_FETCH_STALE_DAYS = 2   # daily cron: a fetch older than this means it missed


_PW_FV_RE = None   # compiled lazily


def _scenario_doc_pw_fv(outputs_dir: Path, ticker: str):
    """Parse the committed scenario doc's headline PW FV for the fv-identity scan."""
    import re

    global _PW_FV_RE
    if _PW_FV_RE is None:
        _PW_FV_RE = re.compile(r"Probability-weighted fair value:\*\* \$([\d,]+\.\d\d)")
    doc = outputs_dir / f"{ticker.lower()}_scenarios.md"
    if not doc.exists():
        return None
    m = _PW_FV_RE.search(doc.read_text())
    return float(m.group(1).replace(",", "")) if m else None


def collect_flags(inputs_dir: Path = INPUTS_DIR, outputs_dir: Path = OUTPUTS_DIR) -> list[str]:
    flags: list[str] = []

    # 1. Trigger register — armed-and-due/overdue, or FIRED (the Jun-17 trigger
    #    sat 15 days because nothing scheduled the check; this is the schedule).
    for it in check_reweight_triggers(inputs_dir):
        if it.status == "missing":
            flags.append(f"TRIGGER-DUE {it.label}: {it.detail}")

    # 2. Input staleness — the per-type thresholds (refresh preflight logic).
    for it in check_market_data(inputs_dir):
        if it.status in ("stale", "missing"):
            flags.append(f"STALE-INPUT {it.label}: {it.detail}")
    try:
        watchlist = load_watchlist(inputs_dir)
    except Exception as exc:
        watchlist = {}
        flags.append(f"STALE-INPUT watchlist unreadable: {exc}")
    for it in check_watchlist_freshness(watchlist):
        if it.status == "stale":
            flags.append(f"STALE-INPUT watchlist {it.label}: {it.detail}")

    # 3. Committed-surface coherence — the F-13 checks against what is SHIPPED:
    #    sign/label (shared implementation) + the fv-identity between the JSON
    #    and each name's committed scenario doc.
    handoff = outputs_dir / "book_scorecard.json"
    doc = None
    if not handoff.exists():
        flags.append("SURFACE-INCOHERENT handoff missing: outputs/book_scorecard.json")
    else:
        doc = json.loads(handoff.read_text())
        if "schema_version" not in doc:
            flags.append("SURFACE-INCOHERENT handoff has no schema_version")
        for f in handoff_coherence_flags(doc):
            flags.append(f"SURFACE-INCOHERENT {f}")
        for n in doc.get("names", []):
            if n.get("void") or n.get("fv") is None:
                continue
            pw = _scenario_doc_pw_fv(outputs_dir, n["ticker"])
            if pw is not None and abs(pw - n["fv"]) > 0.011:
                flags.append(f"SURFACE-INCOHERENT {n['ticker']}: JSON fv {n['fv']} != "
                             f"scenario-doc PW FV {pw}")

    # 3b. Sidecar vintage (WO1-F4) — the §9.10 fragility sidecar must be
    #     computed against the CURRENT scenario_inputs.yaml; a lagging family
    #     means the shipped W-frag/range fields are withheld and the family
    #     scripts owe a re-run.
    fb = weight_family_basis(outputs_dir, inputs_dir)
    if fb["status"] != "current":
        flags.append(f"SIDECAR-STALE weight-family sidecar {fb['status']} vs "
                     f"scenario_inputs {fb['current_sha']} (lagging: "
                     f"{', '.join(fb['lagging']) or 'all'}) — re-run the family diagnostics")

    # 4. Price basis — static fallbacks or pending market-event reviews in the
    #    shipped handoff, plus a missed daily fetch.
    if doc is not None:
        pb = doc.get("price_basis") or {}
        for t, e in (pb.get("static_fallback") or {}).items():
            flags.append(f"PRICE-BASIS {t} on static fallback (as-of {e.get('as_of')}: "
                         f"{e.get('reason')})")
        for t, reason in (pb.get("market_event_review") or {}).items():
            flags.append(f"PRICE-BASIS {t} market-event review pending: {reason}")
    prices = inputs_dir / "market_data" / "prices_daily.yaml"
    if not prices.exists():
        flags.append("PRICE-BASIS prices_daily.yaml missing")
    else:
        import yaml

        pdoc = yaml.safe_load(prices.read_text()) or {}
        fetched = pdoc.get("fetched_at")
        if fetched:
            age = datetime.now(timezone.utc) - datetime.fromisoformat(str(fetched))
            if age.days >= PRICE_FETCH_STALE_DAYS:
                flags.append(f"PRICE-BASIS fetch is {age.days}d old ({fetched}) — cron missed?")
        else:
            flags.append("PRICE-BASIS prices file carries no fetched_at")
    return flags


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="read-only owner-attention sentinel")
    ap.add_argument("--log", type=Path, default=None,
                    help="append one dated status line to this file")
    args = ap.parse_args(argv)

    flags = collect_flags(INPUTS_DIR, OUTPUTS_DIR)   # module-attr lookup at call time (testable)
    for f in flags:
        print(f)
    if args.log:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        with args.log.open("a") as fh:
            if flags:
                fh.write(f"{stamp} FLAG {len(flags)}: " + " | ".join(flags) + "\n")
            else:
                fh.write(f"{stamp} OK\n")
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main())
