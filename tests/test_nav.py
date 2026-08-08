"""NAV-path tests (METHODOLOGY.md section 3.1).

Covers the vessel value curve, per-vessel adjustments, the NAV aggregation on
a synthetic fleet, and a DHT integration check against the populated inputs.
"""

from dataclasses import replace

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
import pytest

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
from crude_tanker_fv.vessel_values import value_for_age, vessel_market_value

M = 1_000_000


@pytest.fixture
def vlcc_curve():
    # Compass May 2026 VLCC anchors (resale/prompt as age-0).
    return VesselValueCurve(
        cls="VLCC",
        dwt=300_000,
        newbuild=175 * M,
        five_year_benchmark=138 * M,
        ten_year_benchmark=111 * M,
        scrap_25yr=22 * M,
        scrubber_premium=2.5 * M,
        eco_premium_pct=0.05,
    )


def test_curve_hits_anchors(vlcc_curve):
    assert value_for_age(vlcc_curve, 0) == pytest.approx(175 * M)
    assert value_for_age(vlcc_curve, 5) == pytest.approx(138 * M)
    assert value_for_age(vlcc_curve, 10) == pytest.approx(111 * M)
    assert value_for_age(vlcc_curve, 25) == pytest.approx(22 * M)


def test_curve_clamps_past_scrap_age(vlcc_curve):
    assert value_for_age(vlcc_curve, 30) == pytest.approx(22 * M)


def test_curve_monotonic_non_increasing(vlcc_curve):
    prev = float("inf")
    for age in range(0, 31):
        v = value_for_age(vlcc_curve, age)
        assert v <= prev + 1e-6
        prev = v


def test_curve_old_age_depreciates_faster(vlcc_curve):
    # Old-age acceleration falls out of the broker term structure: the 10->25
    # leg should be steeper per year than the 5->10 leg.
    slope_mid = (value_for_age(vlcc_curve, 5) - value_for_age(vlcc_curve, 10)) / 5
    slope_old = (value_for_age(vlcc_curve, 10) - value_for_age(vlcc_curve, 25)) / 15
    assert slope_old > slope_mid


def test_curve_negative_age_rejected(vlcc_curve):
    with pytest.raises(ValueError):
        value_for_age(vlcc_curve, -1)


def test_curve_interpolates_between_anchors(vlcc_curve):
    # age 8 sits 60% of the way from the 5yr (138) to the 10yr (111) anchor.
    expected = 138 * M + (111 * M - 138 * M) * 0.6
    assert value_for_age(vlcc_curve, 8) == pytest.approx(expected)


def test_eco_and_scrubber_adjustments(vlcc_curve):
    base = value_for_age(vlcc_curve, 5)
    eco = Vessel(id="e", cls="VLCC", dwt=300_000, age=5, eco=True)
    scr = Vessel(id="s", cls="VLCC", dwt=300_000, age=5, scrubber=True)
    both = Vessel(id="b", cls="VLCC", dwt=300_000, age=5, eco=True, scrubber=True)
    assert vessel_market_value(eco, vlcc_curve) == pytest.approx(base * 1.05)
    assert vessel_market_value(scr, vlcc_curve) == pytest.approx(base + 2.5 * M)
    assert vessel_market_value(both, vlcc_curve) == pytest.approx(base * 1.05 + 2.5 * M)


def test_compute_nav_synthetic(vlcc_curve):
    fleet = FleetManifest(
        ticker="TST",
        report_date="2026-Q1",
        vessels=[
            Vessel(id="a", cls="VLCC", dwt=300_000, age=5),
            Vessel(id="b", cls="VLCC", dwt=300_000, age=5),
        ],
    )
    bs = BalanceSheet(
        ticker="TST",
        quarter="2026-Q1",
        cash_and_equivalents=50 * M,
        working_capital_net=10 * M,
        total_debt=80 * M,
        lease_liabilities=5 * M,
        newbuild_capex_commitments=20 * M,
        newbuild_advances_paid=15 * M,
        diluted_shares_outstanding=10 * M,
    )
    ci = CompanyInputs(
        fleet=fleet,
        balance_sheet=bs,
        dividend_policy=DividendPolicy(ticker="TST", policy_type="x", payout_ratio=1.0),
        cost_structure=CostStructure(ticker="TST"),
        market_data=MarketData(vessel_value_curves={"VLCC": vlcc_curve}),
    )
    nav = compute_nav(ci)
    # 2 x 138M fleet + 50 + 10 - 80 - 5 - 20 + 15 = 246M; /10M shares = 24.6
    assert nav.fleet_value == pytest.approx(276 * M)
    assert nav.nav_total == pytest.approx(246 * M)
    assert nav.nav_per_share == pytest.approx(24.6)
    assert nav.fleet_value_by_class == {"VLCC": pytest.approx(276 * M)}
    # Preferred equity defaults to 0 when omitted from the balance sheet
    # (back-compat with the 12 current watchlist names; METHODOLOGY §4.2).
    assert nav.preferred_equity == 0.0
    # Shuttle contracted-book sleeve also defaults to 0 (METHODOLOGY §11.6).
    assert nav.shuttle_contracted_book == 0.0


def test_governance_discount_propagates_to_navresult(vlcc_curve):
    """governance_discount_pct is exposed on NavResult for downstream consumers
    but does NOT modify compute_nav's nav_total (METHODOLOGY §15). The haircut
    is applied at the blend layer and on the strip's terminal — broker-NAV
    sweep / asset-side diagnostics see undiscounted asset NAV.
    """
    fleet = FleetManifest(
        ticker="TST", report_date="2026-Q1",
        vessels=[Vessel(id="a", cls="VLCC", dwt=300_000, age=5)],
    )
    bs_no = BalanceSheet(
        ticker="TST", quarter="2026-Q1",
        cash_and_equivalents=0, working_capital_net=0, total_debt=0,
        lease_liabilities=0, newbuild_capex_commitments=0,
        newbuild_advances_paid=0, diluted_shares_outstanding=10 * M,
    )
    bs_with = replace(bs_no, governance_discount_pct=0.30)
    ci_no = CompanyInputs(
        fleet=fleet, balance_sheet=bs_no,
        dividend_policy=DividendPolicy(ticker="TST", policy_type="x", payout_ratio=1.0),
        cost_structure=CostStructure(ticker="TST"),
        market_data=MarketData(vessel_value_curves={"VLCC": vlcc_curve}),
    )
    ci_with = replace(ci_no, balance_sheet=bs_with)
    nav_no = compute_nav(ci_no)
    nav_with = compute_nav(ci_with)
    # nav_total is unchanged — same asset NAV; haircut applies downstream.
    assert nav_no.nav_total == pytest.approx(nav_with.nav_total)
    # But the discount is exposed on NavResult so blend/strip can apply it.
    assert nav_no.governance_discount_pct == 0.0
    assert nav_with.governance_discount_pct == pytest.approx(0.30)


def test_compute_nav_adds_shuttle_contracted_book(vlcc_curve):
    """shuttle_contracted_book carries DP2-shuttle / contract-anchored sleeves
    at NPV of contracted cash flows (METHODOLOGY §11.6). Adds to NAV. Mirrors
    the synthetic test with $40M contracted-book sleeve added.
    """
    fleet = FleetManifest(
        ticker="TST",
        report_date="2026-Q1",
        vessels=[
            Vessel(id="a", cls="VLCC", dwt=300_000, age=5),
            Vessel(id="b", cls="VLCC", dwt=300_000, age=5),
        ],
    )
    bs = BalanceSheet(
        ticker="TST",
        quarter="2026-Q1",
        cash_and_equivalents=50 * M,
        working_capital_net=10 * M,
        total_debt=80 * M,
        lease_liabilities=5 * M,
        newbuild_capex_commitments=20 * M,
        newbuild_advances_paid=15 * M,
        diluted_shares_outstanding=10 * M,
        shuttle_contracted_book=40 * M,
    )
    ci = CompanyInputs(
        fleet=fleet,
        balance_sheet=bs,
        dividend_policy=DividendPolicy(ticker="TST", policy_type="x", payout_ratio=1.0),
        cost_structure=CostStructure(ticker="TST"),
        market_data=MarketData(vessel_value_curves={"VLCC": vlcc_curve}),
    )
    nav = compute_nav(ci)
    # 2 x 138M fleet + (50 + 10 - 80 - 5 - 20 + 15 + 40) = 246M + 40M = 286M; /10M = 28.6
    assert nav.nav_total == pytest.approx(286 * M)
    assert nav.nav_per_share == pytest.approx(28.6)
    assert nav.shuttle_contracted_book == pytest.approx(40 * M)


def test_compute_nav_subtracts_preferred_equity(vlcc_curve):
    """preferred_equity is a creditor-like claim ahead of common; NAV subtracts it
    (METHODOLOGY §4.2). Mirrors the synthetic test with $30M preferred added.
    """
    fleet = FleetManifest(
        ticker="TST",
        report_date="2026-Q1",
        vessels=[
            Vessel(id="a", cls="VLCC", dwt=300_000, age=5),
            Vessel(id="b", cls="VLCC", dwt=300_000, age=5),
        ],
    )
    bs = BalanceSheet(
        ticker="TST",
        quarter="2026-Q1",
        cash_and_equivalents=50 * M,
        working_capital_net=10 * M,
        total_debt=80 * M,
        lease_liabilities=5 * M,
        newbuild_capex_commitments=20 * M,
        newbuild_advances_paid=15 * M,
        diluted_shares_outstanding=10 * M,
        preferred_equity=30 * M,
    )
    ci = CompanyInputs(
        fleet=fleet,
        balance_sheet=bs,
        dividend_policy=DividendPolicy(ticker="TST", policy_type="x", payout_ratio=1.0),
        cost_structure=CostStructure(ticker="TST"),
        market_data=MarketData(vessel_value_curves={"VLCC": vlcc_curve}),
    )
    nav = compute_nav(ci)
    # 2 x 138M fleet + (50 + 10 - 80 - 5 - 20 + 15 - 30) = 246M - 30M = 216M; /10M = 21.6
    assert nav.nav_total == pytest.approx(216 * M)
    assert nav.nav_per_share == pytest.approx(21.6)
    assert nav.preferred_equity == pytest.approx(30 * M)


def test_compute_nav_missing_curve_raises(vlcc_curve):
    ci = CompanyInputs(
        fleet=FleetManifest(
            ticker="TST",
            report_date="2026-Q1",
            vessels=[Vessel(id="a", cls="Suezmax", dwt=150_000, age=5)],
        ),
        balance_sheet=BalanceSheet(
            ticker="TST", quarter="2026-Q1", cash_and_equivalents=0, working_capital_net=0,
            total_debt=0, lease_liabilities=0, newbuild_capex_commitments=0,
            newbuild_advances_paid=0, diluted_shares_outstanding=1,
        ),
        dividend_policy=DividendPolicy(ticker="TST", policy_type="x", payout_ratio=1.0),
        cost_structure=CostStructure(ticker="TST"),
        market_data=MarketData(vessel_value_curves={"VLCC": vlcc_curve}),
    )
    with pytest.raises(ValueError, match="Suezmax"):
        compute_nav(ci)


def test_held_for_sale_adds_to_nav(vlcc_curve):
    """A held_for_sale balance (agreed-sold vessels at contracted price) adds to NAV like a
    near-cash current asset — dollar-for-dollar, and is echoed on the NavResult. (NAT, 2026-06-30.)"""
    base = CompanyInputs(
        fleet=FleetManifest(
            ticker="TST", report_date="2026-Q1",
            vessels=[Vessel(id="a", cls="VLCC", dwt=300_000, age=5, count=2)],
        ),
        balance_sheet=BalanceSheet(
            ticker="TST", quarter="2026-Q1", cash_and_equivalents=0, working_capital_net=0,
            total_debt=0, lease_liabilities=0, newbuild_capex_commitments=0,
            newbuild_advances_paid=0, diluted_shares_outstanding=10 * M,
        ),
        dividend_policy=DividendPolicy(ticker="TST", policy_type="x", payout_ratio=1.0),
        cost_structure=CostStructure(ticker="TST"),
        market_data=MarketData(vessel_value_curves={"VLCC": vlcc_curve}),
    )
    r0 = compute_nav(base)
    r1 = compute_nav(replace(base, balance_sheet=replace(base.balance_sheet, held_for_sale=65 * M)))
    assert r1.held_for_sale == 65 * M
    assert r1.nav_total - r0.nav_total == pytest.approx(65 * M)
    assert r1.nav_per_share - r0.nav_per_share == pytest.approx(65 * M / (10 * M))


def test_dht_integration():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    assert len(ci.fleet.vessels) == 23   # 22 operating VLCCs + DHT Impala newbuild on the curve (§9.6, 2026-06-30)
    assert all(v.cls == "VLCC" for v in ci.fleet.vessels)
    assert all(v.scrubber for v in ci.fleet.vessels)  # DHT VLCCs + Impala all scrubber-fitted
    nav = compute_nav(ci)
    # Sanity band: un-anchored ~$16.07/share. DHT Impala (1 VLCC) now ON the curve at age-0
    # delivered PV (§9.6) instead of commitment-net — adds ~$182M PV to fleet_value, advances→0.
    assert 14.0 < nav.nav_per_share < 18.0
    # Re-pinned 2026-08-08 (DHT Q2 refresh): ages -> 2026.5-built basis (+0.5y
    # uniform) eased the fleet marks ~-2.4%; band-verified in dht_log.
    assert nav.fleet_value == pytest.approx(2842.80 * M, rel=1e-3)
