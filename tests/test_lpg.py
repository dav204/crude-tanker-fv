"""Dorian LPG (LPG) tests — WO3 Phase 4 onboarding, 2026-07-10.

Pins the load-bearing manifest/balance-sheet shape from the FY2026 10-K
(acc 0001596993-26-000025; balance sheet as of 2026-03-31). Re-pin
deliberately at the 2026-Q2 refresh (Cobra leaves the fleet — sold
2026-05-06; the Corsair + 2×2015-built $256M trio goes held-for-sale)."""

from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    """Sanity: company inputs load without schema error."""
    from conftest import BOOK_QUARTER

    ci = load_company_inputs("LPG", BOOK_QUARTER)
    assert ci is not None


def test_fleet_shape():
    """Live-pair pins (re-based at the 2026-08-08 Q2 refresh, 10-Q Note 5/6):
    18 on-curve VLGCs at 6/30 — Cobra SOLD 5/6, the Corsair/Constellation/
    Clermont HFS trio off-curve (balance-sheet held_for_sale at realisable).
    Ages on the 2026.5-built basis."""
    from conftest import BOOK_QUARTER

    ci = load_company_inputs("LPG", BOOK_QUARTER)
    vessels = ci.fleet.vessels
    assert len(vessels) == 18
    assert all(v.cls == "VLGC" for v in vessels)
    by_id = {v.id: v for v in vessels}
    assert by_id["Areion"].age == 0.5
    assert by_id["Captain_John_NP"].age == 19.5
    for gone in ("Cobra", "Corsair", "Constellation", "Clermont"):
        assert gone not in by_id, f"{gone} left the on-curve fleet at the Q2 refresh"


def test_balance_sheet_pins():
    """Note-8 gross debt (Japanese SLB financings INSIDE total_debt, not
    lease_liabilities) + the zero-newbuild state + the Note-5 HFS block at
    realisable. Re-based at the 2026-08-08 Q2 refresh."""
    from conftest import BOOK_QUARTER

    ci = load_company_inputs("LPG", BOOK_QUARTER)
    bs = ci.balance_sheet
    assert bs.total_debt == 512409340
    assert bs.newbuild_capex_commitments == 0
    assert bs.newbuild_advances_paid == 0
    assert bs.diluted_shares_outstanding == 42782681
    assert bs.held_for_sale == 220049076
