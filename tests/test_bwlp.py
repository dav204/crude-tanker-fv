"""BW LPG (BWLP) tests — WO3 Phase 4 onboarding, 2026-07-10.

Pins the load-bearing shape from the Q1-2026 interim report (acc
0001213900-26-064314; balance sheet 31-Mar-2026) + FY2025 20-F fleet
tables (acc 0001104659-26-037215). Re-pin at the 2026-Q2 refresh (the
30-May-2026 8-hull $940M Panamax-VLGC order enters §9.6 on-curve then).
The NCI-via-preferred_equity convention is the owner-review item #1 in
decisions/bwlp_log.md — its derivation is marks-dependent (re-derive on
VLGC curve re-fits)."""

from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    """Sanity: company inputs load without schema error."""
    ci = load_company_inputs("BWLP", "2026-Q1")
    assert ci is not None


def test_fleet_shape_2026_q1():
    """39 economically-owned VLGCs at 3/31/2026: 28 parent-owned + 3
    lease-financed bareboat (Capella/Polaris/Kyoto — financing inside
    borrowings) + 8 BW LPG India (consolidated, 52%-owned). Chartered-in
    book excluded (CMDB/SBLK convention)."""
    ci = load_company_inputs("BWLP", "2026-Q1")
    vessels = ci.fleet.vessels
    assert len(vessels) == 39
    assert all(v.cls == "VLGC" for v in vessels)
    india = [v for v in vessels if v.id in {
        "BW_Chinook", "BW_Pampero", "BW_Pine", "BW_Loyalty",
        "BW_Oak", "BW_Tyr", "BW_Birch", "BW_Elm"}]
    assert len(india) == 8
    assert all(v.charter_status == "time_charter" for v in india)


def test_balance_sheet_pins_2026_q1():
    """Balance-sheet captions at 31-Mar-2026 + the zero-newbuild state (the
    $940M order is a 30-May subsequent event) + the NCI deduction carried in
    preferred_equity (the only preferred-like claim BWLP has)."""
    ci = load_company_inputs("BWLP", "2026-Q1")
    bs = ci.balance_sheet
    assert bs.total_debt == 763923000
    assert bs.lease_liabilities == 133908000
    assert bs.newbuild_capex_commitments == 0
    assert bs.newbuild_advances_paid == 0
    assert bs.diluted_shares_outstanding == 151814600
    assert bs.preferred_equity == 199000000  # NAV-basis NCI (India 48% + PS 19%)
