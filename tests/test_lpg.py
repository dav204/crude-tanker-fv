"""Dorian LPG (LPG) tests — WO3 Phase 4 onboarding, 2026-07-10.

Pins the load-bearing manifest/balance-sheet shape from the FY2026 10-K
(acc 0001596993-26-000025; balance sheet as of 2026-03-31). Re-pin
deliberately at the 2026-Q2 refresh (Cobra leaves the fleet — sold
2026-05-06; the Corsair + 2×2015-built $256M trio goes held-for-sale)."""

from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    """Sanity: company inputs load without schema error."""
    ci = load_company_inputs("LPG", "2026-Q1")
    assert ci is not None


def test_fleet_shape_2026_q1():
    """22 owned/bareboat VLGCs at 3/31/2026 (carrying-value table ties at
    1,855,000 cbm) — incl Cobra (subsequent-event sale) and Areion (age 0,
    delivered 2026-03-20); zero under construction, zero HFS."""
    ci = load_company_inputs("LPG", "2026-Q1")
    vessels = ci.fleet.vessels
    assert len(vessels) == 22
    assert all(v.cls == "VLGC" for v in vessels)
    by_id = {v.id: v for v in vessels}
    assert by_id["Areion"].age == 0
    assert by_id["Cobra"].age == 11
    assert by_id["Captain_John_NP"].age == 19


def test_balance_sheet_pins_2026_q1():
    """Note-10 gross debt (incl the $288.0M Japanese SLB financings — inside
    total_debt, NOT lease_liabilities) + the zero-newbuild state (Note 20)."""
    ci = load_company_inputs("LPG", "2026-Q1")
    bs = ci.balance_sheet
    assert bs.total_debt == 565814195
    assert bs.newbuild_capex_commitments == 0
    assert bs.newbuild_advances_paid == 0
    assert bs.diluted_shares_outstanding == 42782681
