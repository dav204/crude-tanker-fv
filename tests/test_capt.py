"""CAPT (Capital Tankers) — 17th name, first Oslo/NOK-quoted listing.

Onboarded 2026-06-11 from the Pareto initiation (Apr-19) + Q1 quarterly
review (May-27), both archived in inputs/research_pareto_other/linked/.
Newbuild-dominated (21 of 30 firm vessels undelivered at Mar-31) — the
heaviest user of the §3.1/§9.6 delivered-market-less-commitment
convention. First reconcile: tool NAV $17.74 vs Pareto-implied $18.21
(-2.6% gap, a real Pareto print) — bands below guard that baseline.
"""


from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.pipeline import value_company


def test_inputs_load():
    ci = load_company_inputs("CAPT", "2026-Q2")
    assert ci is not None


def test_fleet_composition():
    ci = load_company_inputs("CAPT", "2026-Q2")
    by_class = {}
    for v in ci.fleet.vessels:
        key = getattr(v.cls, "value", str(v.cls))
        by_class[key] = by_class.get(key, 0) + getattr(v, "count", 1)
    assert by_class == {"VLCC": 15, "Suezmax": 10, "Aframax": 4, "LR2": 4}  # Q2 refresh 2026-09-01: +3 acquired Hengli VLCC contracts (Aspidoforos/Armonikos/Aftarkis)


def test_balance_sheet_newbuild_convention():
    """NBs at delivered market => advances 0 and the full remaining commitment
    carried as a liability-side line (FRO precedent). Q2 refresh 2026-09-01:
    $1,806.6M per the 6/30 per-vessel CAPEX schedule (incl. the acquired trio's
    $256.2M)."""
    ci = load_company_inputs("CAPT", "2026-Q2")
    bs = ci.balance_sheet
    assert bs.newbuild_advances_paid == 0
    assert bs.newbuild_capex_commitments == 1_806_600_000
    assert bs.governance_discount_pct == 0  # considered + declined, see capt_log


def test_nav_band():
    """Tool NAV band re-pinned 2026-09-01 at the H1 refresh: $17.32 verified
    against the frozen prereg (hairline +0.1% band breach investigated +
    accepted — the at-contract below-market acquisition leg). A move outside
    means inputs or curves changed — re-run the drift gate."""
    ci = load_company_inputs("CAPT", "2026-Q2")
    nav = compute_nav(ci).nav_per_share
    assert 16.3 < nav < 18.3   # $17.32 ±~5-6%


def test_position_at_onboarding_price():
    """At the 8/28-vintage price ($16.46) the raw surface reads BUY-shaped —
    RECORDED-NOT-ACTIONABLE: the Stage-A void holds (POSITION_UNRELIABLE, R4
    condition 5); this pin guards the FV>price arithmetic only, never a read."""
    r = value_company("CAPT", "2026-Q2", current_price=16.46, analyst_target=16.95)
    assert r.blended.fair_value_per_share > 16.46
