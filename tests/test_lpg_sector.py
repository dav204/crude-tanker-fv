"""LPG/VLGC sector tests (WO3 Phases 1-3 + the 2026-07-09 owner-review hardening).

Owner review findings (pre-Phase-4, 2026-07-09) covered here:
  F-1 the §9.9 age-5 WIDE flag is machine-readable (provenance.MARK_WIDE_NODES
      + scorecard._mark_wide_exposure) — the JSON-seam half lives in
      test_scorecard.test_mark_wide_nodes_reach_the_handoff_json;
  F-2 the synthetic pure-VLGC end-to-end check is a COMMITTED artifact (it was
      only a commit-message claim), plus the two-surfaces identity the Phase-3
      derivation rule asserts (ffa base forward == absorption_base base path);
  F-3 the realized-basis numerator is machine-pinned (rate_basis stamp must
      agree with the sector's cycle-anchor basis — the §10 mixed-basis guard).

Point-in-time pins re-pin on trigger vlgc_realized_tce_refresh (numerator) and
lpg_anchor_annual_review (denominator); the marks-band pins re-pin when new
§9.9 prints land (transactions/vlgc.yaml watch items).
"""

from pathlib import Path

import pytest
import yaml

from crude_tanker_fv.loaders import INPUTS_DIR, load_market_data
from crude_tanker_fv.provenance import MARK_WIDE_NODES
from crude_tanker_fv.scenarios import (
    SCENARIO_CLASS_MAP_BY_SECTOR,
    load_scenarios,
    quarter_keys,
    run_scenarios,
)
from crude_tanker_fv.schemas import (
    BalanceSheet,
    CompanyInputs,
    CostStructure,
    DividendPolicy,
    FleetManifest,
    Vessel,
)
from crude_tanker_fv.scorecard import _mark_wide_exposure

MD_DIR = INPUTS_DIR / "market_data"


@pytest.fixture(scope="module")
def lpg_doc():
    return load_scenarios(sector="lpg")


@pytest.fixture(scope="module")
def anchored_md():
    from crude_tanker_fv.transactions import (
        apply_transaction_anchored_curves,
        load_all_transactions,
    )

    md = load_market_data()
    md, fits = apply_transaction_anchored_curves(md, load_all_transactions(INPUTS_DIR))
    return md, fits


def _synthetic_vlgc_company(md) -> CompanyInputs:
    """A pure-VLGC 4-hull name spanning young/mid/old ages — the Phase-3
    end-to-end verification fleet, committed (F-2)."""
    fleet = FleetManifest(ticker="SYN", report_date="2026-03-31", vessels=[
        Vessel(id=f"VLGC_{a}", cls="VLGC", dwt=54000, age=a) for a in (2, 6, 10, 16)
    ])
    return CompanyInputs(
        fleet=fleet,
        balance_sheet=BalanceSheet(
            ticker="SYN", quarter="2026-Q1", cash_and_equivalents=50e6,
            working_capital_net=0, total_debt=100e6, lease_liabilities=0,
            newbuild_capex_commitments=0, newbuild_advances_paid=0,
            diluted_shares_outstanding=10e6),
        cost_structure=CostStructure(ticker="SYN", opex_per_day={"VLGC": 8500},
                                     annual_G_and_A=10e6, annual_interest_expense=6e6),
        dividend_policy=DividendPolicy(ticker="SYN", policy_type="payout", payout_ratio=0.75),
        market_data=md,
    )


# ---------------------------------------------------------------------------
# F-2b — two-surfaces identity: the Phase-3 derivation rule says the base VLGC
# forward IS the absorption_base base path. Two YAML surfaces assumed to agree
# get a TEST that they agree (2026-07-02 rule).
# ---------------------------------------------------------------------------
def test_ffa_base_forward_equals_absorption_base_path(lpg_doc):
    ffa = yaml.safe_load((MD_DIR / "ffa_forward_curve.yaml").read_text())
    vlgc_forward = [float(x) for x in ffa["ffa_forward_curve"]["VLGC"]]
    base_path = [float(lpg_doc["scenarios"]["absorption_base"]["vlgc"][q][1])
                 for q in quarter_keys(8)]
    assert vlgc_forward == base_path, (
        "ffa_forward_curve.VLGC must equal the sectors.lpg absorption_base base "
        "path (the documented Phase-3 derivation rule; it is also the scenario "
        "engine's vessel-elasticity reference, so absorption_base carries "
        "vessel_scale 1.0). Re-derive BOTH together on refresh.")


# ---------------------------------------------------------------------------
# F-3 — numerator basis is machine-pinned to the denominator basis. A future
# refresh pasting a 1-yr-TC print into twelve_month_tc.VLGC would recreate the
# VOIDED §10 mixed-basis cycle read; now it also has to falsify the rate_basis
# stamp (visible in the diff) to keep the suite green.
# ---------------------------------------------------------------------------
def test_cycle_numerator_basis_agrees_with_anchor_basis():
    tc_doc = yaml.safe_load((MD_DIR / "twelve_month_tc.yaml").read_text())
    rate_basis = tc_doc.get("rate_basis") or {}
    assert rate_basis.get("default") == "tc_assessment", \
        "twelve_month_tc.yaml needs a rate_basis block with default tc_assessment (F-3)"

    scen = yaml.safe_load((INPUTS_DIR / "scenario_inputs.yaml").read_text())
    realized_sectors = {
        s for s, sub in scen["sectors"].items()
        if {a.get("anchor_basis") for a in (sub.get("cycle_anchors") or {}).values()}
        == {"realized_tce_10yr_mean"}
    }
    assert "lpg" in realized_sectors
    realized_classes = set()
    for s in realized_sectors:
        realized_classes |= set(SCENARIO_CLASS_MAP_BY_SECTOR[s])

    stamped = {c for c, b in rate_basis.items() if c != "default" and b == "realized_tce"}
    assert stamped == realized_classes, (
        f"realized_tce numerator stamps {sorted(stamped)} must equal the classes of "
        f"realized-anchored sectors {sorted(realized_classes)} — numerator and "
        f"denominator of a cycle ratio share one basis (§10; ratified 2026-07-07)")
    for cls in realized_classes:
        assert cls in tc_doc["twelve_month_tc"], f"{cls}: stamped but no numerator row"


# ---------------------------------------------------------------------------
# VLGC curve statics lock + fit structural bands (re-pin deliberately when new
# prints land — the bands absorb recency-weight drift, not a sample change).
# ---------------------------------------------------------------------------
def test_vlgc_curve_statics_locked():
    c = load_market_data().vessel_value_curves["VLGC"]
    assert c.newbuild == 117.5e6          # NB-parity age-0 (AGE0_BASIS exception)
    assert c.five_year_benchmark == 92e6  # set AT the §9.9 fit (flagged-wide node)
    assert c.ten_year_benchmark == 80e6   # set AT the §9.9 fit (strong node)
    assert c.scrap_25yr == 42e6           # age-25 VALUE anchor (old prints), not demo
    assert not c.dwt_scaled
    assert c.scrubber_premium == 0 and c.eco_premium_pct == 0.0  # unsourced premiums stay 0


def test_vlgc_fit_fires_and_lands_in_documented_bands(anchored_md):
    _, fits = anchored_md
    f = fits["VLGC"]
    assert not f.fallback and f.n_used >= 5
    assert f.slope_per_year < 0
    assert 78e6 <= f.new_10yr <= 84e6, "age-10 is the STRONG node (fit 80.3, all cuts 80.3-83.0)"
    assert 88e6 <= f.new_5yr <= 97e6, "age-5 is EXTRAPOLATED — the documented wide band 89.7-95.9"


# ---------------------------------------------------------------------------
# F-1 — the wide-node registry + fleet-exposure mapping (the JSON-seam half is
# in test_scorecard).
# ---------------------------------------------------------------------------
def test_sector_v1_lock_caps_tier_at_provisional():
    """WO3 Phase 5 (2026-07-10): the lpg v1 calibration lock read 0/2 within
    ±10% (LPG −20.4% / BWLP −17.2% vs broker) — an unlocked sector's names hold
    at PROVISIONAL (never handoff-ready) regardless of per-name validation
    state, until the OWNER rules on the lock. Leaves with SECTOR_V1_UNLOCKED."""
    from crude_tanker_fv.provenance import (
        SECTOR_V1_UNLOCKED,
        confidence_tier,
        is_handoff_ready,
    )

    assert "lpg" in SECTOR_V1_UNLOCKED  # remove ONLY via the owner's lock ruling
    tier = confidence_tier("LPG", "pending-sourceable", "n/a", sector="lpg")
    assert tier == "PROVISIONAL"
    assert not is_handoff_ready(tier)
    # The cap is the SECTOR lock, not the name: the same state in a locked
    # sector reads GOVERNED-WIDE.
    assert confidence_tier("LPG", "pending-sourceable", "n/a", sector="") == "GOVERNED-WIDE"


def test_mark_wide_nodes_registry_sane():
    curves = load_market_data().vessel_value_curves
    root = Path(__file__).resolve().parents[1]
    assert "VLGC" in MARK_WIDE_NODES, "the age-5 wide flag must be machine-readable (F-1)"
    for cls, entry in MARK_WIDE_NODES.items():
        assert cls in curves, f"{cls}: registered wide node but no curve"
        lo, hi = entry["age_window"]
        assert 0 <= lo < hi <= 25
        blo, bhi = entry["band_usd_m"]
        assert blo < bhi
        assert (root / entry["record"]).exists(), f"{cls}: record {entry['record']} missing"


def test_mark_wide_exposure_maps_fleet_ages():
    def hull(cls, age):
        return Vessel(id=f"{cls}_{age}", cls=cls, dwt=54000, age=age)

    # A 2019-21-built VLGC (ages ~5-7) sits ON the extrapolated node — flagged.
    assert _mark_wide_exposure([hull("VLGC", 6)]) == ("VLGC@five_year",)
    # Window edges are inclusive (>=50% sensitivity to the 5yr anchor).
    assert _mark_wide_exposure([hull("VLGC", 2.5)]) == ("VLGC@five_year",)
    assert _mark_wide_exposure([hull("VLGC", 7.5)]) == ("VLGC@five_year",)
    # Mid-old VLGC tonnage rests on the STRONG age-10 node — not flagged.
    assert _mark_wide_exposure([hull("VLGC", 10)]) == ()
    assert _mark_wide_exposure([hull("VLGC", 2)]) == ()
    # Unregistered classes never flag; mixed fleets dedup to one marker.
    assert _mark_wide_exposure([hull("VLCC", 6)]) == ()
    assert _mark_wide_exposure([hull("VLGC", 5), hull("VLGC", 6), hull("VLCC", 6)]) == \
        ("VLGC@five_year",)


# ---------------------------------------------------------------------------
# F-2a — the synthetic pure-VLGC END-TO-END, committed. Structural identities
# and orderings only (no FV value pins — the fit legitimately moves when
# prints land); the two value pins (cycle ratio, w_nav) re-pin on the
# vlgc_realized_tce_refresh / lpg_anchor_annual_review triggers.
# ---------------------------------------------------------------------------
def test_synthetic_pure_vlgc_end_to_end(anchored_md, lpg_doc):
    from crude_tanker_fv.cycle import compute_cycle
    from crude_tanker_fv.nav import compute_nav

    md, _ = anchored_md
    ci = _synthetic_vlgc_company(md)

    nav = compute_nav(ci)
    assert nav.fleet_value > 0 and nav.nav_per_share > 0

    cyc = compute_cycle(ci)
    tc = md.twelve_month_tc["VLGC"]
    mean = md.historical_tce_means["VLGC"]
    assert cyc.cycle_position == pytest.approx(tc / mean)
    assert cyc.cycle_position == pytest.approx(63615 / 40000)  # 1.59x — the ratified
    # war-elevated read (realized-vs-realized; re-pin on numerator refresh)
    assert cyc.w_nav == pytest.approx(0.70)  # late-cycle: blend tilts to NAV

    r = run_scenarios(ci, current_price=30.0, analyst_target=30.0, doc=lpg_doc,
                      scenario_class_map=SCENARIO_CLASS_MAP_BY_SECTOR["lpg"])
    assert r.sector == "lpg"
    assert [s.name for s in r.scenarios] == \
        ["arb_wide", "absorption_base", "overhang", "arb_collapse"]

    fv = {s.name: s.fair_value for s in r.scenarios}
    assert fv["arb_collapse"] < fv["overhang"] < fv["absorption_base"] < fv["arb_wide"]

    # The forward_ref identity: the base ffa row IS the absorption_base path,
    # so that scenario's vessel-value elasticity multiplier is exactly 1.0.
    scale = {s.name: s.vessel_scale for s in r.scenarios}
    assert scale["absorption_base"] == pytest.approx(1.0)
    assert scale["arb_wide"] > 1.0 > scale["overhang"] > scale["arb_collapse"]

    weighted = sum(s.weight * s.fair_value for s in r.scenarios)
    assert r.probability_weighted_fv == pytest.approx(weighted)
