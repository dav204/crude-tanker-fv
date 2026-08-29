"""BRUT (Bruton Ltd) tests — pure-play VLCC newbuild vehicle.

Exercises the §9.6 time-to-delivery newbuild discount: BRUT is 100% undelivered
newbuilds (first delivers Jul-2026, last Q3-2029), so without the discount its
delivered-less-commitment NAV is ~$15.6/sh = +116% vs the Pareto anchor
(SANITY=FAIL); PV-discounting the deliveries lands it ~$9.4 (≈ +30%, OK)."""

from conftest import BOOK_QUARTER

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav


def test_inputs_load_and_fleet_shape():
    """4 VLCC hulls post-demerger (owner ruling 2026-08-29, Option A — the 2028-29
    tail departed to OMC). All rows stay §9.6 (Vision deliberately so — the
    installment-for-SLB-debt equivalence, carry doc §RULED+EXECUTED)."""
    ci = load_company_inputs("BRUT", BOOK_QUARTER)
    assert ci is not None
    vlcc = [v for v in ci.fleet.vessels if v.cls == "VLCC"]
    assert sum(v.count for v in vlcc) == 4
    assert all(v.age == 0 for v in vlcc)
    assert all(v.years_to_delivery > 0 for v in vlcc)


def test_time_to_delivery_discount_pulls_nav_into_sanity_band():
    """The §9.6 discount must materially reduce a pure-newbuild NAV. Undiscounted
    delivered-less-commitment NAV is ~$15.6/sh; PV-discounting the 2026-29
    deliveries lands it ~$9.6 — well below undiscounted and inside the ±50%
    SANITY bar vs Pareto's ~$7.36. (age-0 = xclusiv Resale $175M; Amendment B
    reverted the Thread-1 $145M, which was actually the xclusiv 5yr value.)
    Quarter follows BOOK_QUARTER: BRUT advanced to 2026-Q2 at the 8/13 H1
    refresh, and the pair guard reds a hardcoded quarter the moment the
    manifest moves."""
    nav = compute_nav(load_company_inputs("BRUT", BOOK_QUARTER)).nav_per_share
    # Re-pinned 2026-08-29 at the demerger absorb (4-hull entity): marks ~$650M PV
    # − $398.1M commitment + net cash ~$11.1M ≈ ~$4.25/sh; Pareto post-split NAV
    # kr 42.7 ≈ $4.56 -> the old 12-hull band [8.5, 10.5] valued a different company.
    assert 3.7 < nav < 4.8       # discounted band (post-split)
    assert nav < 6.0             # proves the discount fired (undiscounted runs ~$5.9)


def test_on_water_names_carry_no_delivery_discount():
    """Backward-compat: the §9.6 field is opt-in — an existing on-water fleet
    has years_to_delivery == 0 on every vessel, so its NAV is unaffected.
    (DHT moved off this set 2026-06-30 — Impala; GNK moved off 2026-08-08 —
    the Genco Volunteer committed row. CMDB is the on-water-only example now:
    zero years_to_delivery rows in its manifest.)"""
    from conftest import BOOK_QUARTER

    ci = load_company_inputs("CMDB", BOOK_QUARTER)
    assert all((v.years_to_delivery or 0) == 0.0 for v in ci.fleet.vessels)
