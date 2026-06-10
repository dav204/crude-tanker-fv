"""CMDB tests — third dry-bulk validator, APPROX-anchored (METHODOLOGY §11.7.2).

Data populated 2026-06-10 from the Q1 2026 6-K (accession
0001171843-26-003334) + FY2025 20-F (accession 0001140361-26-011994).
See decisions/cmdb_log.md for the onboarding entry, the CBI trading-platform
exclusion, and the §15-candidate flag.
"""

import pytest

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.pipeline import value_company


@pytest.fixture(scope="module")
def cmdb_inputs():
    return load_company_inputs("CMDB", "2026-Q1")


def test_inputs_load(cmdb_inputs):
    """Sanity: company inputs load without schema error."""
    assert cmdb_inputs is not None


def test_fleet_shape(cmdb_inputs):
    """29 owned vessels at Mar-31 quarter-end (Miracle sold in Q1; Astros
    closed Q2): 6 Cape / 7 Pana (Kamsarmax) / 16 Supra-Ultra. The 20-vessel
    CBI chartered-in platform is excluded — not owned."""
    vessels = cmdb_inputs.fleet.vessels
    assert len(vessels) == 29
    by_class = {}
    for v in vessels:
        by_class[v.cls] = by_class.get(v.cls, 0) + 1
    assert by_class == {"Cape": 6, "Pana": 7, "Supra-Ultra": 16}


def test_cmdb_valuation_runs_and_reconciles():
    """NAV computes and the tool↔APPROX-book gap stays inside the ±50% sanity
    bar (APPROX broker NAV = book value $27.98/sh — spinoff fair-value basis)."""
    r = value_company("CMDB", "2026-Q1", current_price=17.25, analyst_target=27.98)
    nav = r.nav.nav_per_share
    approx_broker_nav = 27.98
    gap = nav / approx_broker_nav - 1.0
    assert abs(gap) < 0.50, f"CMDB gap {gap:+.1%} breaches sanity bar"
