"""ECO tests: all-spot exposure, modern eco fleet, NAV consensus reconciliation."""

import pytest

from crude_tanker_fv.dividend_strip import _class_counts
from crude_tanker_fv.loaders import load_company_inputs, load_watchlist
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.scenarios import load_scenarios, run_scenarios
from crude_tanker_fv.sensitivity import payout_sensitivity


@pytest.fixture
def eco():
    return load_company_inputs("ECO", "2026-Q1")


def test_fleet_and_all_spot(eco):
    counts = _class_counts(eco)
    assert counts["VLCC"] == 8
    assert counts["Suezmax"] == 10          # 8 on-water + 2 newbuilds at market
    assert eco.fleet.spot_coverage_pct["Suezmax"] == pytest.approx(1.00)  # fully spot
    assert eco.fleet.spot_coverage_pct["VLCC"] == pytest.approx(0.88)
    assert all(v.eco for v in eco.fleet.vessels)   # all eco-design


def test_nav_reconciles_to_consensus(eco):
    nav = compute_nav(eco)
    implied_pnav = 48.10 / nav.nav_per_share
    assert 1.15 < implied_pnav < 1.27       # Pareto consensus 1.22x


def test_no_yard_discount(eco):
    # All-Korean-built -> with/without discount NAV identical.
    nav = compute_nav(eco)
    assert nav.nav_per_share == pytest.approx(nav.nav_per_share_ex_yard_discount)


def test_watchlist_has_eco_target():
    wl = load_watchlist()
    assert wl["ECO"]["analyst_target"] == pytest.approx(45.00)
    assert wl["INSW"]["analyst_target"] == pytest.approx(79.50)   # now modeled (hybrid carve-out)


def test_payout_sensitivity_monotonic(eco):
    s = payout_sensitivity(eco)
    assert s[0.80] < s[0.95] < s[1.00]


def test_scenarios_overvalued(eco):
    r = run_scenarios(eco, 48.10, 45.00, load_scenarios())
    # All-spot -> wide scenario swing.
    spread = max(s.fair_value for s in r.scenarios) - min(s.fair_value for s in r.scenarios)
    assert spread > 5.0
    # HOLD (EV ~-2%): Amendment B set Suezmax age-0 to xclusiv Resale $114.3M (> the
    # pre-Thread-1 $108M), lifting ECO's young-Suezmax NAV ~+2% and moving it from
    # TRIM/SHORT into the fairly-valued band. Read straight off the xclusiv curve.
    # Re-pinned 2026-07-02 (post-stand-down vintage: crude reweight 0.10/0.20/0.45/0.25
    # + MoU-ineffective leg recalibration — decisions/crude_reweight_proposal_2026-07-02.md):
    # removing the war premium drops PW FV to ~$30.2 vs $48.10 → TRIM/SHORT
    # (§12 relabel applies downstream — cycle position, not a short).
    assert r.position_recommendation.startswith("TRIM/SHORT")
