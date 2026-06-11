"""CAPT (Capital Tankers) — 17th name, first Oslo/NOK-quoted listing.

Onboarded 2026-06-11 from the Pareto initiation (Apr-19) + Q1 quarterly
review (May-27), both archived in inputs/research_pareto_other/linked/.
Newbuild-dominated (21 of 30 firm vessels undelivered at Mar-31) — the
heaviest user of the §3.1/§9.6 delivered-market-less-commitment
convention. First reconcile: tool NAV $17.74 vs Pareto-implied $18.21
(-2.6% gap, a real Pareto print) — bands below guard that baseline.
"""

import pytest

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.pipeline import value_company


def test_inputs_load():
    ci = load_company_inputs("CAPT", "2026-Q1")
    assert ci is not None


def test_fleet_composition():
    ci = load_company_inputs("CAPT", "2026-Q1")
    by_class = {}
    for v in ci.fleet.vessels:
        key = getattr(v.cls, "value", str(v.cls))
        by_class[key] = by_class.get(key, 0) + getattr(v, "count", 1)
    assert by_class == {"VLCC": 12, "Suezmax": 10, "Aframax": 4, "LR2": 4}


def test_balance_sheet_newbuild_convention():
    """NBs at delivered market => advances 0 and the full $1.88B remaining
    commitment carried as a liability-side line (FRO precedent)."""
    ci = load_company_inputs("CAPT", "2026-Q1")
    bs = ci.balance_sheet
    assert bs.newbuild_advances_paid == 0
    assert bs.newbuild_capex_commitments == 1_880_000_000
    assert bs.governance_discount_pct == 0  # considered + declined, see capt_log


def test_nav_band():
    """Tool NAV within the documented first-reconcile band (vs Pareto
    NAV ~$18.2 implied; gap -2.6% at onboarding). A move outside the band
    means inputs or curves changed — re-run the drift gate."""
    ci = load_company_inputs("CAPT", "2026-Q1")
    nav = compute_nav(ci).nav_per_share
    assert 15.0 < nav < 21.0


def test_position_at_onboarding_price():
    """At the Jun-10 vintage price ($12.20 = NOK 116.2 / 9.5221) CAPT reads
    BUY — the deepest-discount crude name (Pareto pegs 0.67x NAV)."""
    r = value_company("CAPT", "2026-Q1", current_price=12.20, analyst_target=18.90)
    assert r.blended.fair_value_per_share > 12.20
