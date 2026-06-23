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


def test_bvps_filed_date_no_lookahead():
    """Proxy signal must use book value only once FILED (public), not at the
    fiscal period-end — financials aren't knowable before they're filed."""
    from backtest.loaders import bvps_at
    asof = dt.date(2025, 6, 30)
    # period ended Mar-31 but filed May-9 (known by Jun-30) -> usable;
    # period ended Jun-30 filed Aug-7 (NOT yet public at Jun-30) -> must be ignored.
    series = [(dt.date(2025, 5, 9), dt.date(2025, 3, 31), 10.0),
              (dt.date(2025, 8, 7), dt.date(2025, 6, 30), 99.0)]
    assert bvps_at(series, asof) == 10.0


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


# --------------------------------------------------------------------------- #
# Amendment 3 — Sharadar P/B proxy loaders (cache-guarded; skip if absent)
# --------------------------------------------------------------------------- #

import pytest                                                       # noqa: E402
from backtest import loaders_sharadar as ls                        # noqa: E402

_NO_CACHE = pytest.mark.skipif(
    not ls.cache_available(),
    reason="factor-portfolio Sharadar cache absent (set FACTOR_PORTFOLIO_ROOT)",
)


@_NO_CACHE
def test_sharadar_bvps_sane_and_deep():
    bvps = ls.load_bvps()
    for nm in ("DHT", "FRO", "ECO", "INSW", "TNK"):                # crude flagships present
        assert nm in bvps and bvps[nm], f"{nm} missing BVPS"
        assert bvps[nm][-1][2] > 0, f"{nm} latest book value not positive"
        # negative book equity is a real downturn datum (e.g. FRO 2013-14
        # pre-recapitalization); the loader surfaces it, the runner's bv<=0
        # filter drops it — so we assert finiteness, not all-positive.
        import math
        assert all(math.isfinite(v) for _, _, v in bvps[nm]), f"{nm} non-finite BVPS"
    assert min(pe for _, pe, _ in bvps["NAT"]).year <= 1999        # deepest history


@_NO_CACHE
def test_sharadar_prices_total_return_series():
    prices = ls.load_prices()
    for nm, s in prices.items():
        assert all(p > 0 for _, p in s), f"{nm} non-positive adjclose"
        assert s == sorted(s), f"{nm} price series not date-sorted"


def test_engine_test1_ev_cheapness_sign_convention():
    """Test 1's load-bearing convention: HIGH engine EV% must rank as cheap, so
    high EV% predicting high forward return yields POSITIVE sector-neutral IC."""
    from backtest.run_engine_test1 import engine_quarter_ic, sign_hit_rate, verdict
    ev = {"A": 20.0, "B": -10.0, "C": 15.0, "D": -5.0}      # A,C cheap (high EV%)
    sec = {"A": "crude", "B": "crude", "C": "product", "D": "product"}
    ret = {"A": 0.18, "B": -0.06, "C": 0.12, "D": -0.02}    # cheap names outperform
    assert engine_quarter_ic(ev, ret, sec).ic_sector_neutral == 1.0
    hit, n = sign_hit_rate(ev, ret, sec)
    assert hit == 1.0 and n == 4
    # anti-predictive (cheap names underperform) flips the IC negative
    ret_anti = {k: -v for k, v in ret.items()}
    assert engine_quarter_ic(ev, ret_anti, sec).ic_sector_neutral == -1.0
    # decision rule: significant negative = FAIL, significant positive = EDGE
    assert verdict(-0.3, -2.5).startswith("FAIL")
    assert verdict(0.3, 2.5).startswith("EDGE")
    assert verdict(0.04, 0.6).startswith("INCONCLUSIVE")


def test_engine_test1_runs_with_no_vintages(tmp_path):
    """Harness must be runnable now (data pending): empty vintages → clean exit 0."""
    from backtest.run_engine_test1 import discover_vintages, qend_date, next_quarter
    assert discover_vintages(tmp_path) == []
    assert qend_date("2024-Q1") == dt.date(2024, 3, 31)
    assert next_quarter("2024-Q4") == "2025-Q1"
    assert next_quarter("2024-Q1") == "2024-Q2"


@_NO_CACHE
def test_sharadar_bvps_point_in_time():
    """Load-bearing: independently re-derived, the BVPS the proxy would surface
    at every quarter-end is the latest filing dated <= asof (within staleness)
    — never a future filing."""
    from backtest.loaders import bvps_at, quarter_ends
    bvps = ls.load_bvps()
    prices = ls.load_prices()
    last = max(d for s in prices.values() for d, _ in s)
    for asof in quarter_ends(dt.date(2012, 1, 1), last):
        for nm, ser in bvps.items():
            got = bvps_at(ser, asof, 550)
            avail = [(f, pe, v) for f, pe, v in ser if f <= asof]
            if not avail:
                assert got is None
                continue
            f, pe, v = avail[-1]
            assert f <= asof
            assert got is None if (asof - pe).days > 550 else got == v
