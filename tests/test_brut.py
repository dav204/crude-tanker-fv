"""BRUT (Bruton Ltd) tests — pure-play VLCC newbuild vehicle.

Exercises the §9.6 time-to-delivery newbuild discount: BRUT is 100% undelivered
newbuilds (first delivers Jul-2026, last Q3-2029), so without the discount its
delivered-less-commitment NAV is ~$15.6/sh = +116% vs the Pareto anchor
(SANITY=FAIL); PV-discounting the deliveries lands it ~$9.4 (≈ +30%, OK)."""

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav


def test_inputs_load_and_fleet_shape():
    """12 firm VLCC newbuilds, none on the water, all future-delivery."""
    ci = load_company_inputs("BRUT", "2026-Q1")
    assert ci is not None
    vlcc = [v for v in ci.fleet.vessels if v.cls == "VLCC"]
    assert sum(v.count for v in vlcc) == 12
    assert all(v.age == 0 for v in vlcc)
    assert all(v.years_to_delivery > 0 for v in vlcc)


def test_time_to_delivery_discount_pulls_nav_into_sanity_band():
    """The §9.6 discount must materially reduce a pure-newbuild NAV. Undiscounted
    delivered-less-commitment NAV is ~$15.6/sh; PV-discounting the 2026-29
    deliveries lands it ~$9.4 — well below undiscounted and inside the ±50%
    SANITY bar vs Pareto's ~$7.20."""
    nav = compute_nav(load_company_inputs("BRUT", "2026-Q1")).nav_per_share
    assert 8.5 < nav < 10.5      # discounted band
    assert nav < 12.0            # proves the discount fired (undiscounted ~$15.6)


def test_on_water_names_carry_no_delivery_discount():
    """Backward-compat: the §9.6 field is opt-in — an existing on-water fleet
    has years_to_delivery == 0 on every vessel, so its NAV is unaffected."""
    ci = load_company_inputs("DHT", "2026-Q1")
    assert all(v.years_to_delivery == 0.0 for v in ci.fleet.vessels)
