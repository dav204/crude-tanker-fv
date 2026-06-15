"""Test 0 driver — naive published P/NAV, no engine.

Computes the PRE-REGISTERED primary metric (mean quarterly Spearman IC of
published P/NAV vs 1q-forward equal-weight-crude-neutral total return, with
t-stat) on the real Pareto P/NAV window, plus the pre-registered exploratory
reads. Prints a structured summary; REPORT.md is authored from these numbers.

Run: PYTHONPATH=. .venv/bin/python -m backtest.run_test0
"""

from __future__ import annotations

from .loaders import (CRUDE_NAMES, NAT_APPROX, build_panel, load_pnav,
                      load_prices, quarter_ends)
from .evaluate import cheap_minus_rich, ic_series


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def main() -> int:
    pnav = load_pnav()
    prices = load_prices()

    # Window = span of real published crude P/NAV.
    all_dates = [d for n in CRUDE_NAMES for d, _ in pnav.get(n, [])]
    first, last_price = min(all_dates), max(d for s in prices.values() for d, _ in s)
    qe = quarter_ends(first, last_price)

    print(f"P/NAV window: {min(all_dates)} .. {max(all_dates)}")
    print(f"price data to: {last_price}")
    print(f"quarter-ends in scope: {[q.isoformat() for q in qe]}\n")

    panel = build_panel(CRUDE_NAMES, pnav, prices, qe)

    print("=== PRIMARY: per-quarter cross-section (published P/NAV) ===")
    print(f"{'asof':12} {'names':28} {'P/NAV':28} {'fwd_ret%':30} {'ewCrude%':>9}")
    for c in panel:
        names = sorted(c.pnav)
        pn = " ".join(f"{n}:{c.pnav[n]:.2f}" for n in names)
        fr = " ".join(f"{n}:{c.fwd_ret[n]*100:+.1f}" for n in names)
        print(f"{c.asof.isoformat():12} {','.join(names):28} {pn:28} {fr:30} {c.ew_crude*100:+8.1f}")

    res = ic_series(panel, min_names=3)
    print("\n=== PRIMARY metric (pre-registered) ===")
    print(f"{'quarter':12} {'n':>2} {'IC':>8}")
    for q in res.quarter_ics:
        print(f"{q.asof:12} {q.n:>2} {q.ic:>+8.3f}")
    print(f"\nmean quarterly IC : {_fmt(res.mean_ic)}   (Nq={res.n_quarters}, min_names={res.min_names})")
    print(f"t-stat            : {_fmt(res.t_stat, 2)}")

    print("\n=== EXPLORATORY (not the verdict) ===")
    spread = cheap_minus_rich(panel)
    print(f"cheap-minus-rich quarterly spread: mean {_fmt(spread.mean_spread)} "
          f"t {_fmt(spread.t_stat, 2)} (Nq={spread.n_quarters})")
    res2 = ic_series(panel, min_names=2)
    print(f"IC incl. degenerate n=2 quarters : mean {_fmt(res2.mean_ic)} "
          f"t {_fmt(res2.t_stat, 2)} (Nq={res2.n_quarters})")
    nat_panel = build_panel(CRUDE_NAMES + [NAT_APPROX], pnav, prices, qe)
    nat_n = sum(1 for c in nat_panel if NAT_APPROX in c.pnav)
    print(f"NAT published-P/NAV quarters available: {nat_n} (APPROX-only; excluded from primary)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
