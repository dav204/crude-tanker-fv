"""Reconciliation diagnostic — tool↔broker NAV gap + drift surfacing.

Three jobs (METHODOLOGY §9.9 + CLAUDE.md "What this tool is, philosophically"):

  A. SANITY      — gap within ±50%; failing means a bug, not a call.
  B. CALIBRATION — when a new sector ships, ≥70%/±10% of validators clear
                   the v1 lock bar (existing sectors locked at ≥80%/±5%).
  C. DRIFT       — has the gap moved >2pp since the previous reconcile?

The tool produces independent NAV from transaction-validated marks. Broker
consensus (Pareto P/NAV) is a discrimination diagnostic, NOT a calibration
target. Wide spreads documented in METHODOLOGY §6 are intentional calls,
not failures. The sanity bar catches bugs (mis-routed sector, unit error,
miscounted fleet) — not "you don't match Pareto."

Reads `state/last_run.json` (gitignored quarterly snapshot from
pipeline.main()) and `inputs/watchlist.yaml`. Does NOT re-run the pipeline.
Drift baseline is `state/last_reconcile.json`, written on every reconcile.

Exit codes:
  0 — all checked names SANITY=OK
  1 — at least one SANITY=FAIL (a bug exists)
  2 — usage / missing data error (no pipeline run available)
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "state" / "last_run.json"
DRIFT_SNAPSHOT_PATH = ROOT / "state" / "last_reconcile.json"
WATCHLIST_PATH = ROOT / "inputs" / "watchlist.yaml"

# Sector tiering (CLAUDE.md "Reconciliation has three jobs").
EXISTING_SECTORS = {"crude", "product", "lng"}
EXISTING_LOCK_BAR_PCT = 5.0
EXISTING_LOCK_HIT_RATE = 0.80
NEW_LOCK_BAR_PCT = 10.0
NEW_LOCK_HIT_RATE = 0.70

SANITY_BAR_PCT = 50.0          # Wider than this = bug, not a call.
DRIFT_ALERT_PP = 2.0           # Per-quarter gap-pct move that warrants a note.

# Names whose consensus_pnav is APPROX — either Pareto doesn't publish (NAT,
# ASC, CCEC have "—" in the Pareto P/NAV column) or the watchlist explicitly
# flags "treat the broker NAV column as APPROX" (TEN: VIE-stale P/NAV, no
# active Pareto coverage). Reported but excluded from calibration-lock
# hit-rate denominators because the broker anchor itself is uncertain.
#
# v1 design wart: this is hardcoded. The right v2 design is a structured
# `pnav_basis: approx` field on the watchlist row so the loader carries it
# through. Keeping the hardcode for Week 0 to avoid a watchlist-schema
# refactor; promote to a field in Q3.
APPROX_PNAV_TICKERS = {"NAT", "ASC", "CCEC", "TEN", "CMDB", "MPCC", "GSL"}
# CMDB added 2026-06-10: zero Pareto/VIE coverage (name-sweep: 1 incidental
# mention in 280 dailies, as a charterer); its consensus_pnav is a P/BV
# proxy (spinoff fair-value-basis book), so it must not enter the
# calibration-lock denominator as a Pareto-anchored validator.
# MPCC + GSL added 2026-06-12: the ENTIRE containerships sector is APPROX
# (§11.8.2 — Pareto publishes no container NAV, verified in their own liner
# valuation table). MPCC's proxy is a stale company-implied NAV (Jul-2025
# divestment statement); GSL's is P/B on a depreciated-cost book (WEAK).
# The container calibration lock is N/A-by-construction (§11.8.7).


@dataclass
class ReconcileRow:
    ticker: str
    sector: str
    tool_nav: float
    broker_nav: float
    gap_pct: float
    sanity_status: str          # "OK" or "FAIL"
    drift_pp: Optional[float]   # None if no prior snapshot
    drift_status: str           # "stable" / "alert" / "first-run"
    pnav_basis: str             # "pareto" or "approx"
    k_broker: float
    consensus_pnav: float


def _load_state() -> dict:
    if not STATE_PATH.exists():
        sys.stderr.write(
            "state/last_run.json not found. Run "
            "`python -m crude_tanker_fv.pipeline <QUARTER>` first.\n"
        )
        sys.exit(2)
    return json.loads(STATE_PATH.read_text())


def _load_drift_snapshot() -> Optional[dict]:
    if not DRIFT_SNAPSHOT_PATH.exists():
        return None
    return json.loads(DRIFT_SNAPSHOT_PATH.read_text())


def _load_watchlist() -> dict:
    return yaml.safe_load(WATCHLIST_PATH.read_text())


def compute_row(
    ticker: str,
    state: dict,
    prior: Optional[dict],
    watchlist: dict,
) -> Optional[ReconcileRow]:
    """Compute one ticker's reconciliation row, or None if data is missing."""
    t = state.get("tickers", {}).get(ticker)
    if t is None:
        return None
    w = watchlist.get(ticker) or {}
    consensus_pnav = w.get("consensus_pnav")
    if consensus_pnav is None or w.get("current_price") is None:
        return None

    price = w["current_price"]
    broker_nav = price / consensus_pnav
    tool_nav = t["nav_per_share"]
    gap_pct = (tool_nav - broker_nav) / broker_nav * 100.0
    pnav_basis = "approx" if ticker in APPROX_PNAV_TICKERS else "pareto"
    # APPROX-pnav names have a placeholder broker anchor (Pareto doesn't publish);
    # calling SANITY=FAIL against a placeholder is the wrong frame. Mark as n/a.
    if pnav_basis == "approx":
        sanity = "n/a"
    else:
        sanity = "OK" if abs(gap_pct) <= SANITY_BAR_PCT else "FAIL"

    drift_pp: Optional[float] = None
    drift_status = "first-run"
    if prior is not None:
        prior_gap = prior.get("gaps", {}).get(ticker)
        if prior_gap is not None:
            drift_pp = gap_pct - prior_gap
            drift_status = "alert" if abs(drift_pp) > DRIFT_ALERT_PP else "stable"

    return ReconcileRow(
        ticker=ticker,
        sector=t.get("sector", "?"),
        tool_nav=tool_nav,
        broker_nav=broker_nav,
        gap_pct=gap_pct,
        sanity_status=sanity,
        drift_pp=drift_pp,
        drift_status=drift_status,
        pnav_basis=pnav_basis,
        k_broker=t.get("k_broker", float("nan")),
        consensus_pnav=consensus_pnav,
    )


def _select_tickers(args, state: dict, watchlist: dict) -> list[str]:
    if args.all or args.calibration_lock or args.sector:
        tickers = list(state.get("tickers", {}).keys())
        if args.sector:
            tickers = [t for t in tickers if state["tickers"][t].get("sector") == args.sector]
        if args.calibration_lock:
            tickers = [t for t in tickers if state["tickers"][t].get("sector") == args.calibration_lock]
        return tickers
    return [args.ticker.upper()]


def _format_drift(row: ReconcileRow) -> str:
    if row.drift_pp is None:
        return "first-run"
    sign = "+" if row.drift_pp >= 0 else ""
    return f"{sign}{row.drift_pp:.1f}pp ({row.drift_status})"


def _print_table(rows: list[ReconcileRow]) -> None:
    if not rows:
        print("(no rows)")
        return
    header = f"{'TICKER':<8}{'SECTOR':<10}{'TOOL_NAV':>10}{'BROKER':>10}{'GAP':>8}  {'SANITY':<7}{'PNAV':<8}{'Δ vs last':<18}"
    print(header)
    print("-" * len(header))
    for r in rows:
        gap_str = f"{r.gap_pct:+.1f}%"
        nav_str = f"${r.tool_nav:.2f}"
        brk_str = f"${r.broker_nav:.2f}"
        print(
            f"{r.ticker:<8}{r.sector:<10}{nav_str:>10}{brk_str:>10}{gap_str:>8}  "
            f"{r.sanity_status:<7}{r.pnav_basis:<8}{_format_drift(r):<18}"
        )


def _print_verbose(row: ReconcileRow) -> None:
    print()
    print(f"  Mark posture:    k_broker {row.k_broker:.2f}")
    if row.pnav_basis == "approx":
        print(f"  Pareto basis:    APPROX (Pareto does not publish P/NAV for {row.ticker})")
    print(f"  Consensus P/NAV: {row.consensus_pnav:.2f}×")
    print()
    if abs(row.gap_pct) > (EXISTING_LOCK_BAR_PCT if row.sector in EXISTING_SECTORS else NEW_LOCK_BAR_PCT):
        print(
            "  Reading: gap exceeds the v1 lock bar for this sector. "
            "If documented in METHODOLOGY §6 (mark-driven / weight-driven / §12 pure-play), "
            "this is the call — not a calibration failure. Otherwise investigate."
        )
    else:
        print("  Reading: gap is within sector v1 lock bar — mark-validated alignment.")


def _print_calibration_lock(rows: list[ReconcileRow], sector: str) -> int:
    """v1 calibration lock test — does this sector clear the hit-rate bar?"""
    is_existing = sector in EXISTING_SECTORS
    bar_pct = EXISTING_LOCK_BAR_PCT if is_existing else NEW_LOCK_BAR_PCT
    hit_rate_bar = EXISTING_LOCK_HIT_RATE if is_existing else NEW_LOCK_HIT_RATE

    # Exclude APPROX-pnav names from the denominator.
    eligible = [r for r in rows if r.pnav_basis == "pareto" and r.sanity_status == "OK"]
    if not eligible:
        print(f"  No Pareto-anchored names in sector {sector!r}. Cannot evaluate calibration lock.")
        return 0
    hits = [r for r in eligible if abs(r.gap_pct) <= bar_pct]
    hit_rate = len(hits) / len(eligible)
    tier = "existing" if is_existing else "new (v1)"
    status = "PASS" if hit_rate >= hit_rate_bar else "FAIL"
    print()
    print(
        f"Calibration lock ({tier} sector, bar ±{bar_pct:.0f}% / "
        f"hit rate ≥{hit_rate_bar:.0%}):"
    )
    print(f"  {len(hits)}/{len(eligible)} names within ±{bar_pct:.0f}% "
          f"({hit_rate:.0%}) — {status}")
    if rows and any(r.pnav_basis == "approx" for r in rows):
        approx = [r.ticker for r in rows if r.pnav_basis == "approx"]
        print(f"  Excluded (APPROX P/NAV): {', '.join(approx)}")
    if rows and any(r.sanity_status == "FAIL" for r in rows):
        fails = [r.ticker for r in rows if r.sanity_status == "FAIL"]
        print(f"  Excluded (SANITY=FAIL — investigate): {', '.join(fails)}")
    return 0 if status == "PASS" else 1


def _save_drift_snapshot(rows: list[ReconcileRow], state: dict) -> None:
    """Persist current gaps so the NEXT reconcile can compute drift."""
    DRIFT_SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    snapshot = {
        "quarter": state.get("quarter"),
        "run_at": state.get("run_at"),
        "gaps": {r.ticker: r.gap_pct for r in rows},
    }
    DRIFT_SNAPSHOT_PATH.write_text(json.dumps(snapshot, indent=2) + "\n")


def reconcile(args) -> int:
    state = _load_state()
    prior = _load_drift_snapshot()
    watchlist = _load_watchlist()
    tickers = _select_tickers(args, state, watchlist)
    if not tickers:
        sys.stderr.write("No tickers matched the selection.\n")
        return 2

    rows: list[ReconcileRow] = []
    for ticker in tickers:
        row = compute_row(ticker, state, prior, watchlist)
        if row is None:
            sys.stderr.write(
                f"{ticker}: skipped (missing watchlist entry, consensus_pnav, "
                f"or pipeline output)\n"
            )
            continue
        rows.append(row)

    if not rows:
        return 2

    _print_table(rows)

    if args.verbose and len(rows) == 1:
        _print_verbose(rows[0])

    if args.calibration_lock:
        return _print_calibration_lock(rows, args.calibration_lock)

    # Summary footer for --all / --sector
    if len(rows) > 1:
        fails = [r for r in rows if r.sanity_status == "FAIL"]
        alerts = [r for r in rows if r.drift_status == "alert"]
        print()
        print(f"  {len(rows)} names checked. "
              f"SANITY FAIL: {len(fails)}. DRIFT ALERTS (>{DRIFT_ALERT_PP}pp): {len(alerts)}.")
        if fails:
            print(f"  Investigate: {', '.join(r.ticker for r in fails)}")
        if alerts:
            print(f"  Drift alerts: {', '.join(r.ticker for r in alerts)}")

    # Persist drift snapshot for next run (only for --all or full sector — avoids
    # wiping the snapshot when you reconcile a single ticker).
    if args.all or args.sector:
        _save_drift_snapshot(rows, state)

    return 1 if any(r.sanity_status == "FAIL" for r in rows) else 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="crude_tanker_fv.reconcile",
        description="Tool↔broker NAV reconciliation (sanity / calibration / drift).",
    )
    parser.add_argument("ticker", nargs="?", help="ticker to reconcile (e.g. DHT)")
    parser.add_argument("--all", action="store_true", help="reconcile every name in the watchlist")
    parser.add_argument("--sector", help="reconcile every name in a sector (crude/product/lng/...)")
    parser.add_argument("--calibration-lock", dest="calibration_lock",
                        help="v1 calibration-lock test for a sector (use at sector ship)")
    parser.add_argument("--verbose", action="store_true", help="extra diagnostic detail (single ticker)")
    args = parser.parse_args(argv)
    if not (args.ticker or args.all or args.sector or args.calibration_lock):
        parser.print_help(sys.stderr)
        return 2
    return reconcile(args)


if __name__ == "__main__":
    sys.exit(main())
