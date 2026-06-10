"""GNK tests — second Pareto-anchored dry-bulk validator (METHODOLOGY §11.7.2).

Data populated 2026-06-09 from the Q1 2026 10-Q (accession
0001104659-26-056337). See decisions/gnk_log.md for the onboarding entry and
the Diana-tender deal context.
"""

import pytest

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.pipeline import value_company


@pytest.fixture(scope="module")
def gnk_inputs():
    return load_company_inputs("GNK", "2026-Q1")


def test_inputs_load(gnk_inputs):
    """Sanity: company inputs load without schema error."""
    assert gnk_inputs is not None


def test_fleet_shape(gnk_inputs):
    """44 vessels at Mar-31 quarter-end: 19 Cape (2 nmax + 17 capesize),
    25 Supra-Ultra (15 ultramax + 10 supramax incl. held-for-sale Predator).
    No Pana exposure."""
    vessels = gnk_inputs.fleet.vessels
    assert len(vessels) == 44
    by_class = {}
    for v in vessels:
        by_class[v.cls] = by_class.get(v.cls, 0) + 1
    assert by_class == {"Cape": 19, "Supra-Ultra": 25}


def test_gnk_valuation_runs_and_reconciles():
    """NAV computes, and the tool↔broker gap stays inside the ±50% sanity bar
    (broker NAV = $24.00 / 0.87 = $27.59 per Pareto Jun-4 2026)."""
    r = value_company("GNK", "2026-Q1", current_price=24.00, analyst_target=24.80)
    nav = r.nav.nav_per_share
    broker_nav = 24.00 / 0.87
    gap = nav / broker_nav - 1.0
    assert abs(gap) < 0.50, f"GNK gap {gap:+.1%} breaches sanity bar"
