"""Harness correctness tests — the no-look-ahead property is the load-bearing one.

Run: PYTHONPATH=. .venv/bin/python -m pytest backtest/test_backtest.py -q
"""

import datetime as dt

from backtest.evaluate import spearman, ic_series
from backtest.loaders import (QuarterCross, build_panel, price_at, signal_at,
                              quarter_ends)


def test_spearman_monotone():
    assert spearman([1, 2, 3, 4], [10, 20, 30, 40]) == 1.0
    assert spearman([1, 2, 3, 4], [40, 30, 20, 10]) == -1.0
    assert spearman([1, 1], [1, 1]) is None          # no dispersion -> undefined


def test_signal_never_uses_future_print():
    """The core no-look-ahead guarantee: a print dated after asof is never used."""
    asof = dt.date(2025, 6, 30)
    series = [(dt.date(2025, 6, 20), 1.0),            # the only legitimate signal
              (dt.date(2025, 7, 10), 9.0)]            # FUTURE — must be ignored
    assert signal_at(series, asof) == 1.0
    # and if the only data is in the future, there is no signal (not a leak):
    assert signal_at([(dt.date(2025, 7, 10), 9.0)], asof) is None


def test_signal_staleness_guard():
    asof = dt.date(2025, 6, 30)
    fresh = [(dt.date(2025, 6, 20), 1.0)]             # 10 days old -> ok
    stale = [(dt.date(2025, 4, 1), 1.0)]              # ~90 days old -> dropped
    assert signal_at(fresh, asof, staleness_days=45) == 1.0
    assert signal_at(stale, asof, staleness_days=45) is None


def test_price_no_lookahead():
    asof = dt.date(2025, 6, 30)
    series = [(dt.date(2025, 6, 27), 100.0), (dt.date(2025, 7, 2), 999.0)]
    assert price_at(series, asof) == 100.0


def test_build_panel_signal_predates_asof():
    """Every signal feeding quarter t must be dated <= t (re-derived independently)."""
    pnav = {"A": [(dt.date(2025, 3, 20), 0.8), (dt.date(2025, 6, 20), 1.2)],
            "B": [(dt.date(2025, 3, 20), 1.1), (dt.date(2025, 6, 20), 0.9)],
            "C": [(dt.date(2025, 3, 20), 1.0), (dt.date(2025, 6, 20), 1.0)]}
    prices = {n: [(dt.date(2025, 3, 31), 10.0), (dt.date(2025, 6, 30), 11.0),
                  (dt.date(2025, 9, 30), 12.0)] for n in "ABC"}
    qe = quarter_ends(dt.date(2025, 3, 31), dt.date(2025, 9, 30))
    panel = build_panel(list("ABC"), pnav, prices, qe)
    assert panel, "expected at least one cross-section"
    for cross in panel:
        for name, used in cross.pnav.items():
            prior = [v for d, v in pnav[name] if d <= cross.asof]
            assert used == prior[-1], "panel used a non-latest-or-future P/NAV"


def test_sector_neutral_ic_is_within_sector():
    """Sector-neutral IC must reward within-sector cheapness, and must ignore a
    cross-sector P/NAV-level confound (a uniformly-cheap sector that happens to
    do well should not by itself create signal)."""
    from backtest.evaluate_wide import wide_quarter_ic
    # crude: cheaper name wins; product: cheaper name wins -> IC should be +1
    data = {
        "A": (0.7, 0.20, "crude"), "B": (1.1, -0.05, "crude"),   # A cheap & best
        "C": (0.8, 0.15, "product"), "D": (1.2, -0.02, "product"),  # C cheap & best
    }
    wq = wide_quarter_ic(data)
    assert wq.ic_sector_neutral == 1.0
    # singleton sector contributes nothing (no within-sector rank)
    data2 = dict(data); data2["E"] = (0.5, 0.99, "lng")
    wq2 = wide_quarter_ic(data2)
    assert wq2.ic_sector_neutral == 1.0  # E ignored -> unchanged


def test_ic_sign_convention():
    """Low P/NAV paired with high forward return must yield positive IC."""
    c = QuarterCross(
        asof=dt.date(2025, 6, 30), nxt=dt.date(2025, 9, 30),
        pnav={"A": 0.7, "B": 1.0, "C": 1.3},          # A cheapest
        fwd_ret={"A": 0.20, "B": 0.0, "C": -0.10},     # A best
        rel_ret={"A": 0.167, "B": -0.033, "C": -0.133},
        ew_crude=0.033)
    res = ic_series([c], min_names=3)
    assert res.quarter_ics and res.quarter_ics[0].ic == 1.0
