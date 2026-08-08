"""Container validator pins (onboarded 2026-06-12, METHODOLOGY §11.8).

Point-in-time pins at the frozen Apr-01-2026 MB marks vintage + Jun-12
inputs; re-pin on the first MB-subscription marks refresh.
"""


from conftest import BOOK_QUARTER  # follows the book across quarter rolls
from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.pipeline import value_company


def test_mpcc_onboarding_baseline():
    r = value_company("MPCC", "2026-Q1", current_price=2.78, analyst_target=2.63,
                      strip_horizon=10)
    # NAV $2.02 (re-pinned 2026-06-22 from $2.27): the §9.6 time-to-delivery
    # discount rolled out to the 15 owned NBs (q1-q13 out) trims ~$0.25/sh.
    # 51 on-water + 15 owned NB rows net of $633.7M commitments.
    assert 1.92 < r.nav.nav_per_share < 2.12
    assert r.nav.preferred_equity == 0
    assert len(r.strip.dps_by_quarter) == 10  # sector horizon, not the default 8


def test_gsl_onboarding_baseline():
    r = value_company("GSL", BOOK_QUARTER, current_price=38.99, analyst_target=52.04,
                      strip_horizon=10)
    # NAV $38.59 at pin: 71 vessels, $109M Series B prefs subtracted.
    # Re-pinned 2026-08-08 (Q2 refresh, band-verified +6.8%: time-deposit basis +
    # first-real WC + NB advances-only — gsl_log): $41.20 ±5%.
    assert 39.1 < r.nav.nav_per_share < 43.3
    assert r.nav.preferred_equity == 109_000_000


def test_gsl_coverage_schedule_decays_with_charter_expiries():
    ci = load_company_inputs("GSL", BOOK_QUARTER)
    cov = ci.fleet.coverage_schedule
    # Front quarters fully covered; intermediate decays hard by q4_2028 while
    # large holds — the staggered-expiry structure §11.8.6 exists to price.
    assert cov["Ctr-Intermediate"][0] == 1.0 and cov["Ctr-Large"][0] == 1.0
    assert cov["Ctr-Intermediate"][9] < 0.2
    assert cov["Ctr-Large"][9] > 0.6
    assert all(a >= b for a, b in zip(cov["Ctr-Large"], cov["Ctr-Large"][1:]))


def test_mpcc_fleet_schedule_ramps_with_owned_newbuilds():
    ci = load_company_inputs("MPCC", "2026-Q1")
    fs = ci.fleet.fleet_schedule
    # Sold trio departs pre-strip (earning fleet < manifest rows at q0);
    # owned NBs ramp the intermediate count by q4_2028.
    assert fs["Ctr-Intermediate"][0] < fs["Ctr-Intermediate"][9]
    rows = sum(v.count for v in ci.fleet.vessels if v.cls == "Ctr-Intermediate")
    assert fs["Ctr-Intermediate"][0] < rows  # NB rows + sold not yet/no longer earning


def test_container_validators_route_all_classes():
    for t in ("MPCC", "GSL"):
        ci = load_company_inputs(t, BOOK_QUARTER)
        classes = {v.cls for v in ci.fleet.vessels}
        assert classes <= {"Ctr-Feeder", "Ctr-Intermediate", "Ctr-Large"}, classes
