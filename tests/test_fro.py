"""FRO multi-class tests: yard discount, vessel counts, fleet schedule, payout.

Exercises the machinery DHT couldn't (3 classes, Chinese-yard discounts, a
newbuild delivery ramp, and newbuilds valued at market).
"""

import pytest

from crude_tanker_fv.cycle import compute_cycle
from crude_tanker_fv.dividend_strip import _class_counts, compute_dividend_strip
from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.sensitivity import payout_sensitivity


@pytest.fixture
def fro():
    return load_company_inputs("FRO", "2026-Q1")


def test_fleet_counts_match_report(fro):
    counts = _class_counts(fro)
    assert counts["VLCC"] == 42   # 33 on-water + 9 newbuilds in the manifest
    assert counts["Suezmax"] == 21
    assert counts["LR2"] == 18


def test_yard_discount_lowers_nav(fro):
    nav = compute_nav(fro)
    # Chinese / Hanjin-Subic tonnage -> with-discount NAV below par.
    assert nav.nav_per_share < nav.nav_per_share_ex_yard_discount
    impact = nav.nav_per_share_ex_yard_discount - nav.nav_per_share
    assert 0.5 < impact < 2.5   # ~$1.4/share


def test_nav_reconciles_to_consensus_pnav(fro):
    nav = compute_nav(fro)
    # Pareto consensus P/NAV 1.21x at $34.50 -> NAV ~$28.5; newbuilds valued at
    # market are what get us there (cost-based would read ~$23). Thread 1 (VLCC
    # age-0 $175M->$145M dated resale) nudges the un-anchored NAV down to ~$26.9
    # (implied ~1.28). NOTE: on the production transaction-anchored curve the
    # spread widens further (NAV ~$22.7, implied ~1.52) — the intended crude
    # tool-vs-broker divergence (CLAUDE.md "wide spreads are features").
    implied_pnav = 34.50 / nav.nav_per_share
    assert 1.15 < implied_pnav < 1.30


def test_fleet_schedule_ramps_vlcc_in_strip(fro):
    s = compute_dividend_strip(fro, compute_nav(fro).nav_per_share)
    # VLCC earning fleet ramps over the strip (newbuild deliveries); revenue in
    # the same-TCE final quarters reflects more vessels than a static 33.
    sched = fro.fleet.fleet_schedule["VLCC"]
    assert sched[0] < sched[-1]               # ramps up
    assert sched[-1] == pytest.approx(42)


def test_cycle_is_fleet_weighted_peak(fro):
    cyc = compute_cycle(fro)
    # Per-class ratios ~2.79/2.21/2.04; value-weighted blend in the peak band.
    assert set(cyc.cycle_position_by_class) == {"VLCC", "Suezmax", "LR2"}
    assert cyc.cycle_position_by_class["VLCC"] == pytest.approx(2.7875)
    assert 2.0 < cyc.cycle_position < 2.79     # blended, VLCC-weighted
    assert (cyc.w_nav, cyc.w_earn) == (0.70, 0.30)


def test_payout_sensitivity_monotonic(fro):
    sens = payout_sensitivity(fro)
    assert sens[0.80] < sens[0.95] < sens[1.00]


def test_constructed_ffa_warning_surfaces():
    from crude_tanker_fv.pipeline import value_company

    report = value_company("FRO", "2026-Q1", current_price=34.50, analyst_target=30.50)
    assert any("CONSTRUCTED" in w and "LR2" in w for w in report.warnings)
