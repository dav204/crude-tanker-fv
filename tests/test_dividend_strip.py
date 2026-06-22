"""Dividend-strip tests (METHODOLOGY.md section 3.2)."""

import pytest

from crude_tanker_fv.dividend_strip import compute_dividend_strip
from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.schemas import (
    BalanceSheet,
    CompanyInputs,
    CostStructure,
    DividendPolicy,
    FleetManifest,
    MarketData,
    Vessel,
    VesselValueCurve,
)

M = 1_000_000


def _curve():
    return VesselValueCurve(
        cls="VLCC",
        dwt=300_000,
        newbuild=175 * M,
        five_year_benchmark=138 * M,
        ten_year_benchmark=111 * M,
        scrap_25yr=22 * M,
    )


def _zero_bs(shares):
    return BalanceSheet(
        ticker="TST", quarter="2026-Q1", cash_and_equivalents=0, working_capital_net=0,
        total_debt=0, lease_liabilities=0, newbuild_capex_commitments=0,
        newbuild_advances_paid=0, diluted_shares_outstanding=shares,
    )


def _inputs(*, ffa, spot_pct=1.0, opex=10_000, payout=1.0, base=0.0, floor=0.0,
            gna=0.0, interest=0.0, tax=0.0, shares=1 * M, age=5):
    return CompanyInputs(
        fleet=FleetManifest(
            ticker="TST", report_date="2026-Q1",
            vessels=[Vessel(id="v1", cls="VLCC", dwt=300_000, age=age)],
            spot_coverage_pct={"VLCC": spot_pct},
        ),
        balance_sheet=_zero_bs(shares),
        dividend_policy=DividendPolicy(
            ticker="TST", policy_type="variable", payout_ratio=payout,
            base_dividend_per_share=base, floor=floor,
        ),
        cost_structure=CostStructure(
            ticker="TST", opex_per_day={"VLCC": opex}, annual_G_and_A=gna,
            annual_interest_expense=interest, effective_tax_rate=tax,
        ),
        market_data=MarketData(
            vessel_value_curves={"VLCC": _curve()},
            ffa_forward_curve={"VLCC": ffa},
        ),
    )


def test_strip_arithmetic_flat_curve():
    # 1 VLCC, all spot, flat $50k/day FFA, $10k/day opex, no G&A/interest/tax,
    # r=0, no offhire. Per quarter: 91.25*50k - 91.25*10k = $3.65M; /1M = $3.65.
    ci = _inputs(ffa=[50_000] * 8)
    s = compute_dividend_strip(ci, nav_per_share=138.0, discount_rate=0.0, offhire_rate=0.0)
    assert s.eps_by_quarter == [pytest.approx(3.65)] * 8
    assert s.dps_by_quarter == [pytest.approx(3.65)] * 8
    assert s.discounted_dps == [pytest.approx(3.65)] * 8
    # Terminal NAV/share: vessel aged 5 -> 7.25y = 138 + (111-138)*(2.25/5) =
    # $125.85M, over 1M shares = $125.85/share.
    assert s.terminal_value == pytest.approx(125.85)
    assert s.implied_price == pytest.approx(8 * 3.65 + 125.85)


def test_tce_blends_spot_and_charter():
    # 60% spot at FFA 100k, 40% charter at disclosed 50k -> TCE = 80k.
    ci = _inputs(ffa=[100_000] * 8, spot_pct=0.6)
    ci.fleet.vessels[0] = Vessel(
        id="v1", cls="VLCC", dwt=300_000, age=5,
        charter_status="time_charter", charter_rate=50_000,
    )
    s = compute_dividend_strip(ci, nav_per_share=138.0, discount_rate=0.0, offhire_rate=0.0)
    assert s.blended_tce_by_quarter["VLCC"][0] == pytest.approx(0.6 * 100_000 + 0.4 * 50_000)


def test_dps_floors_at_base_when_eps_negative():
    # FFA 5k/day < 10k/day opex -> negative EPS -> DPS = base dividend only.
    ci = _inputs(ffa=[5_000] * 8, base=0.025)
    s = compute_dividend_strip(ci, nav_per_share=138.0, discount_rate=0.0, offhire_rate=0.0)
    assert all(eps < 0 for eps in s.eps_by_quarter)
    assert s.dps_by_quarter == [pytest.approx(0.025)] * 8


def test_variable_base_is_a_floor_not_additive():
    # 100% payout, positive EPS well above the base -> DPS == EPS (base does NOT
    # stack on top). This is the bug fix: previously DPS = EPS + base.
    ci = _inputs(ffa=[50_000] * 8, payout=1.0, base=0.025)
    s = compute_dividend_strip(ci, nav_per_share=138.0, discount_rate=0.0, offhire_rate=0.0)
    assert all(dps == pytest.approx(eps) for dps, eps in zip(s.dps_by_quarter, s.eps_by_quarter))


def test_base_plus_variable_adds_base_on_top():
    # INSW-style policy: base is paid in addition to the variable part.
    ci = _inputs(ffa=[50_000] * 8, payout=1.0, base=0.12)
    ci.dividend_policy.policy_type = "base_plus_variable"
    s = compute_dividend_strip(ci, nav_per_share=138.0, discount_rate=0.0, offhire_rate=0.0)
    assert all(dps == pytest.approx(eps + 0.12) for dps, eps in zip(s.dps_by_quarter, s.eps_by_quarter))


def test_strip_reports_ffa_front4_mean():
    from crude_tanker_fv.cycle import twelve_month_ffa

    ci = load_company_inputs("DHT", "2026-Q1")
    s = compute_dividend_strip(ci, nav_per_share=compute_nav(ci).nav_per_share)
    # The strip reports the FFA 12M (front-4 mean) for context; it drives the
    # cash flows but NOT the cycle (which now uses the 12M TC).
    expected = twelve_month_ffa(ci.market_data.ffa_forward_curve["VLCC"])
    assert s.ffa_12m_by_class["VLCC"] == pytest.approx(expected)
    assert s.ffa_spot_by_quarter["VLCC"] == ci.market_data.ffa_forward_curve["VLCC"]


def test_terminal_value_below_current_nav():
    # Aging the fleet forward must reduce the terminal NAV vs. today's NAV.
    ci = _inputs(ffa=[50_000] * 8)
    nav_now = compute_nav(ci).nav_per_share
    s = compute_dividend_strip(ci, nav_per_share=nav_now, discount_rate=0.11)
    assert s.terminal_value < nav_now


def test_dht_integration():
    ci = load_company_inputs("DHT", "2026-Q1")
    nav = compute_nav(ci)
    s = compute_dividend_strip(ci, nav.nav_per_share)
    assert len(s.dps_by_quarter) == 8
    # Seasonal FFA with a structural downtrend -> first quarter outranks the last.
    assert s.eps_by_quarter[0] > s.eps_by_quarter[-1]
    # Sanity band around the ~$19.5 implied price (Q3'26-Q2'28 FFA curve).
    assert 18.0 < s.implied_price < 21.0


def test_terminal_nav_multiple_locked_at_1x():
    """§9.2 terminal-value decision LOCKED at 1.0x (owner, 2026-06-21 —
    outputs/terminal_value_options_memo.md). Changing the multiple is a
    methodology decision: update the memo DECISION block and re-pin this test
    deliberately (same discipline as the locked-weights tests)."""
    from crude_tanker_fv import dividend_strip

    assert dividend_strip.TERMINAL_NAV_MULTIPLE == 1.0
