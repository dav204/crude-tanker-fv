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
    ci = load_company_inputs("BWLP", "2026-Q2")
    assert ci is not None


def test_fleet_shape_2026_q1():
    """39 economically-owned VLGCs, unchanged through 6/30/2026 (Q2 refresh
    2026-08-31: vessels cost flat, the -1 VLGC was a chartered-in redelivery):
    28 parent-owned + 3 lease-financed bareboat (Capella/Polaris/Kyoto —
    financing inside borrowings) + 8 BW LPG India (consolidated, 52%-owned;
    Elm/Birch sales are POST-6/30 subsequent events). Chartered-in book
    excluded (CMDB/SBLK convention)."""
    ci = load_company_inputs("BWLP", "2026-Q2")
    vessels = ci.fleet.vessels
    assert len(vessels) == 39
    assert all(v.cls == "VLGC" for v in vessels)
    india = [v for v in vessels if v.id in {
        "BW_Chinook", "BW_Pampero", "BW_Pine", "BW_Loyalty",
        "BW_Oak", "BW_Tyr", "BW_Birch", "BW_Elm"}]
    assert len(india) == 8
    assert all(v.charter_status == "time_charter" for v in india)


def test_balance_sheet_pins_2026_q1():
    """Balance-sheet captions at 30-Jun-2026 (Q2 refresh 2026-08-31) + the
    zero-newbuild state (the 8-hull order HELD OUT pending the owner fork,
    decisions/bwlp_nb_order_fork_2026-08-31.md — the Q2 report is silent and
    advances are $0) + the NCI deduction re-derived on the live curve with
    Q2 Note-10 statics (tests/test_bwlp_nci.py guards the tie)."""
    ci = load_company_inputs("BWLP", "2026-Q2")
    bs = ci.balance_sheet
    assert bs.total_debt == 814248000
    assert bs.lease_liabilities == 118384000
    assert bs.newbuild_capex_commitments == 0
    assert bs.newbuild_advances_paid == 0
    assert bs.diluted_shares_outstanding == 151814600
    assert bs.preferred_equity == 216300000  # NAV-basis NCI (India 48% + PS 19%), 8/31 re-derivation
