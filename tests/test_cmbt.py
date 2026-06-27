"""CMBT (CMB.TECH) tests — first crude+dry_bulk+containerships MULTI_SLEEVE hybrid (§11.9)."""

import pytest

from crude_tanker_fv.carveout import sector_carve_out
from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.pipeline import (
    MULTI_SLEEVE_TICKERS,
    _load_all_sectors,
    _run_scenarios_for_ticker,
)


def test_inputs_load():
    ci = load_company_inputs("CMBT", "2026-Q1")
    assert ci is not None


def test_cmbt_is_multi_sleeve():
    assert MULTI_SLEEVE_TICKERS.get("CMBT") == ["crude", "dry_bulk", "containerships"]


def test_fleet_counts():
    ci = load_company_inputs("CMBT", "2026-Q1")
    counts: dict[str, int] = {}
    for v in ci.fleet.vessels:
        counts[v.cls] = counts.get(v.cls, 0) + v.count
    assert counts["VLCC"] == 4
    assert counts["Suezmax"] == 16
    assert counts["Cape"] == 75          # 38 Newcastlemax + 37 Capesize
    assert counts["Pana"] == 30          # 26 Kamsarmax + 4 Panamax
    assert counts["Ctr-Large"] == 4
    assert sum(counts.values()) == 129    # on_curve_total cross-foot


def test_sleeve_shares_sum_to_one_and_drybulk_dominates():
    ci = load_company_inputs("CMBT", "2026-Q1")
    shares = {sec: sector_carve_out(ci, sec).sleeve_share
              for sec in ("crude", "dry_bulk", "containerships")}
    assert sum(shares.values()) == pytest.approx(1.0)
    # Post-Golden-Ocean, dry bulk is the dominant sleeve by value.
    assert shares["dry_bulk"] > shares["crude"] > shares["containerships"]
    assert shares["dry_bulk"] > 0.5


def test_each_sleeve_fleet_is_class_clean():
    ci = load_company_inputs("CMBT", "2026-Q1")
    assert {v.cls for v in sector_carve_out(ci, "crude").sleeve_inputs.fleet.vessels} == {"VLCC", "Suezmax"}
    assert {v.cls for v in sector_carve_out(ci, "dry_bulk").sleeve_inputs.fleet.vessels} == {"Cape", "Pana"}
    assert {v.cls for v in sector_carve_out(ci, "containerships").sleeve_inputs.fleet.vessels} == {"Ctr-Large"}


def test_whole_co_nav_aggregation_invariant():
    """Sum of the three sleeve NAV/share ≈ whole-company compute_nav (§11.9)."""
    ci = load_company_inputs("CMBT", "2026-Q1")
    whole = compute_nav(ci).nav_per_share
    parts = sum(compute_nav(sector_carve_out(ci, sec).sleeve_inputs).nav_per_share
                for sec in ("crude", "dry_bulk", "containerships"))
    assert parts == pytest.approx(whole, abs=0.02)


def test_scenario_headline_is_whole_company():
    ci = load_company_inputs("CMBT", "2026-Q1")
    sector_docs = _load_all_sectors()
    watchlist = {"CMBT": {"sector": "crude"}}
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "CMBT", ci, 15.96, 16.59, sector_docs, watchlist,
    )
    assert headline.basis.startswith("WHOLE-COMPANY")
    assert "dry_bulk" in headline.basis and "containerships" in headline.basis
    assert crude_r is not None        # crude sleeve report exposed
    assert product_r is None          # no product sleeve
    assert headline.probability_weighted_fv > 0
