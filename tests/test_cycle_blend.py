"""Cycle-weighting and blend tests (METHODOLOGY.md sections 2.1-2.3)."""

import pytest

from crude_tanker_fv.blend import blend_fair_value
from crude_tanker_fv.cycle import (
    compute_cycle,
    cycle_position_for_class,
    weights_for_position,
)
from crude_tanker_fv.dividend_strip import DividendStripResult
from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import NavResult


@pytest.mark.parametrize(
    "cp, w_nav, label",
    [
        (2.0, 0.70, "late-cycle/peak"),
        (1.5, 0.60, "elevated"),    # boundary: 1.5 is NOT > 1.5 -> elevated band
        (1.3, 0.60, "elevated"),
        (1.0, 0.50, "mid-cycle"),
        (0.6, 0.40, "below-mid"),
        (0.3, 0.30, "trough"),
    ],
)
def test_weights_for_position_bands(cp, w_nav, label):
    wn, we, lbl = weights_for_position(cp)
    assert wn == pytest.approx(w_nav)
    assert we == pytest.approx(1 - w_nav)
    assert lbl == label


def test_cycle_position_ratio():
    assert cycle_position_for_class(155_000, 40_000) == pytest.approx(3.875)


def test_cycle_position_rejects_nonpositive_mean():
    with pytest.raises(ValueError):
        cycle_position_for_class(100_000, 0)


def test_dht_cycle_uses_12m_tc():
    ci = load_company_inputs("DHT", "2026-Q1")
    cyc = compute_cycle(ci)
    # Cycle uses the Compass 12M TC ($111.5k), NOT the FFA strip: 111500/40000 = 2.7875x.
    assert cyc.cycle_position == pytest.approx(2.7875)
    assert cyc.twelve_month_tc_by_class == {"VLCC": pytest.approx(111_500)}
    assert cyc.band_label == "late-cycle/peak"          # still > 1.5x -> peak band
    assert (cyc.w_nav, cyc.w_earn) == (0.70, 0.30)
    assert cyc.cycle_position_by_class == {"VLCC": pytest.approx(2.7875)}


def test_blend_arithmetic():
    nav = NavResult(
        fleet_value=0, cash_and_equivalents=0, working_capital_net=0, total_debt=0,
        lease_liabilities=0, newbuild_capex_commitments=0, newbuild_advances_paid=0,
        diluted_shares_outstanding=1, nav_total=0, nav_per_share=15.29,
        fleet_value_by_class={},
    )
    strip = DividendStripResult(implied_price=19.46)
    from crude_tanker_fv.cycle import CycleResult

    cyc = CycleResult(
        cycle_position=2.7875, cycle_position_by_class={"VLCC": 2.7875},
        twelve_month_tc_by_class={"VLCC": 111_500},
        w_nav=0.70, w_earn=0.30, band_label="late-cycle/peak",
    )
    fv = blend_fair_value(nav, strip, cyc)
    assert fv.fair_value_per_share == pytest.approx(0.70 * 15.29 + 0.30 * 19.46)
    # Default governance discount is 0; effective NAV equals raw NAV.
    assert fv.governance_discount_pct == 0.0
    assert fv.nav_per_share_effective == pytest.approx(15.29)


def test_blend_applies_governance_discount():
    """A non-zero governance_discount_pct haircuts the NAV term in the blend
    (METHODOLOGY §15). Strip is unchanged at this layer (the terminal-value
    haircut is applied inside compute_dividend_strip and is already reflected
    in strip.implied_price by the time we get here)."""
    nav = NavResult(
        fleet_value=0, cash_and_equivalents=0, working_capital_net=0, total_debt=0,
        lease_liabilities=0, newbuild_capex_commitments=0, newbuild_advances_paid=0,
        diluted_shares_outstanding=1, nav_total=0, nav_per_share=100.0,
        fleet_value_by_class={}, governance_discount_pct=0.30,
    )
    strip = DividendStripResult(implied_price=50.0)
    from crude_tanker_fv.cycle import CycleResult

    cyc = CycleResult(
        cycle_position=2.0, cycle_position_by_class={"VLCC": 2.0},
        twelve_month_tc_by_class={"VLCC": 80_000},
        w_nav=0.70, w_earn=0.30, band_label="late-cycle/peak",
    )
    fv = blend_fair_value(nav, strip, cyc)
    # Effective NAV = 100 * (1 - 0.30) = 70; blend = 0.70 * 70 + 0.30 * 50 = 64.0
    assert fv.nav_per_share_effective == pytest.approx(70.0)
    assert fv.fair_value_per_share == pytest.approx(0.70 * 70.0 + 0.30 * 50.0)
    # The pre-discount FV is also exposed for transparency.
    assert fv.fair_value_per_share_pre_discount == pytest.approx(0.70 * 100.0 + 0.30 * 50.0)
    # nav_per_share remains the raw asset value.
    assert fv.nav_per_share == pytest.approx(100.0)


def test_dht_fair_value_end_to_end():
    from crude_tanker_fv.dividend_strip import compute_dividend_strip
    from crude_tanker_fv.nav import compute_nav

    ci = load_company_inputs("DHT", "2026-Q1")
    nav = compute_nav(ci)
    strip = compute_dividend_strip(ci, nav.nav_per_share)
    cyc = compute_cycle(ci)
    fv = blend_fair_value(nav, strip, cyc)
    # Peak weighting puts 70% on NAV, so FV sits between NAV and the strip price.
    assert nav.nav_per_share < fv.fair_value_per_share < strip.implied_price
    assert 16.0 < fv.fair_value_per_share < 17.0
