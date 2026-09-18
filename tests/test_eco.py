"""ECO tests: all-spot exposure, modern eco fleet, NAV consensus reconciliation."""

import pytest

from crude_tanker_fv.dividend_strip import _class_counts
from crude_tanker_fv.loaders import load_company_inputs, load_watchlist
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.scenarios import load_scenarios, run_scenarios
from crude_tanker_fv.sensitivity import payout_sensitivity


@pytest.fixture
def eco():
    from conftest import BOOK_QUARTER

    return load_company_inputs("ECO", BOOK_QUARTER)


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
    # Re-pinned at the 2026-08-08 Q2 refresh: NAV +9.4% (paired H1 6-K inputs)
    # against the SAME pinned price/consensus vintage recenters the implied
    # multiple 1.22x -> ~1.10x. Sanity intent unchanged (tool NAV within
    # hailing distance of the consensus read); recenters again at the next
    # watchlist vintage rebase.
    assert 1.04 < implied_pnav < 1.16


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
    # Re-pinned 2026-09-11: the 2026-09-10 crude escalation reweight (0.25/0.62/0.00/0.13
    # → 0.28/0.59/0.00/0.13, fork escalation_c3_rearm, decisions/escalation_c3_rearm_2026-09-10.md)
    # lifts the probability-weighted FV to $1.93 below the $48.10 price — inside the
    # fairly-valued band, so HOLD. The lock test in tests/test_scenarios.py was re-pinned with
    # the reweight; this pin was missed and the suite was not fully run before that commit
    # (caught at the next full run).
    assert r.position_recommendation.startswith("HOLD")
    # RE-PINNED 2026-09-18 — WO5/R4 Phases 0-3b (decisions/r4_deck_reexpression_method_2026-09-18.md,
    # Phase-3 freeze row ECO): the de-escalation re-levelling lifts ECO's whole-company FV +4.57%,
    # carrying EV across zero to +0.10. Still HOLD — the band is +/-5%, and the crossing is a
    # magnitude change inside it, not a flip.
    assert -1.0 < r.expected_value_vs_current < 2.0
