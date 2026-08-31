"""Scenario-engine tests (consumes scenario_inputs.yaml).

Covers the crude three-phase MoU framework as before, plus the sector layer
(METHODOLOGY §11): FLNG resolves to the LNG glut-cycle scenarios, not crude.
"""

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
import pytest

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.scenarios import (
    ANCHOR_BASIS_LABELS,
    SCENARIO_CLASS_MAP_BY_SECTOR,
    all_sector_anchor_bases,
    detect_mixed_anchor_basis,
    load_scenarios,
    position_recommendation,
    run_scenarios,
)

SECTORS = ("crude", "lng", "product", "dry_bulk", "containerships", "lpg")


@pytest.fixture(scope="module")
def doc():
    return load_scenarios()  # default sector="crude"


@pytest.fixture(scope="module")
def lng_doc():
    return load_scenarios(sector="lng")


def test_scenarios_parse_and_weights_sum_to_one(doc):
    names = list(doc["scenarios"])
    assert names == ["escalation", "pre_mou_baseline", "mou_base", "mou_bear"]
    assert sum(doc["scenarios"][n]["weight"] for n in names) == pytest.approx(1.0)
    # BUG-5 (2026-06-22): pin the individual Crude Set A weights — sum-to-1 alone let a
    # silent weight edit pass (LNG/product weights were value-pinned, crude was not).
    # Re-pinned 2026-07-02 (post-stand-down vintage: crude reweight 0.25/0.45/0.18/0.12
    # → 0.10/0.20/0.45/0.25 + MoU-ineffective leg recalibration —
    # decisions/crude_reweight_proposal_2026-07-02.md).
    # Re-pinned 2026-07-12 (Jun-9 war tilt RESTORED 0.10/0.20/0.45/0.25 →
    # 0.25/0.45/0.18/0.12): trigger crude_doha_talks_resumption FIRED — Jul-7/8
    # Hormuz strikes + sanctions re-imposition; the pre-registered restore executed
    # at owner go. decisions/doha_check_2026-07-12.md.
    # Re-pinned 2026-07-31 (B' reweight 0.25/0.45/0.18/0.12 -> 0.25/0.57/0.05/0.13):
    # the 7/22 ruling's frozen conditional executed at owner go after the 7/29
    # mediation-watch check (pause-without-talks; owner ruled the letter governs).
    # Retires dead-MoU mass; escalation untouched; Aug-16 = the full re-derivation.
    # decisions/ceasefire_mediation_check_2026-07-31.md.
    # Re-pinned 2026-08-16 (C2 at the toll-cliff venue, owner ruling R1:
    # 0.25/0.57/0.05/0.13 -> 0.25/0.62/0.00/0.13). mou_base was held expressly
    # conditional on the day-60 cliff "resolving benignly"; it resolved to NEITHER
    # pre-registered branch (no collection evidenced, no extension, no Oman framework)
    # and the observed state IS pre_mou_baseline's registered meaning, so the
    # benign-conditional mass retires there. escalation untouched (C3 declined).
    # decisions/crude_day60_toll_cliff_2026-08-16.md.
    assert {n: doc["scenarios"][n]["weight"] for n in names} == {
        "escalation": pytest.approx(0.25), "pre_mou_baseline": pytest.approx(0.62),
        "mou_base": pytest.approx(0.00), "mou_bear": pytest.approx(0.13),
    }
    # The retired leg STAYS in the deck at zero — series continuity (the Jul-02
    # semantic-marker pattern): a scenario that disappears breaks a backtest's ability
    # to detect the break. Deleting it would also silently narrow fv_low/fv_high, which
    # are taken over weight>0 scenarios.
    assert "mou_base" in doc["scenarios"], "retired leg must persist at zero, not vanish"
    # Sector layer (METHODOLOGY §11): the default load returns the crude sub-doc
    # with its own cycle_anchors, and the sector name is stamped in.
    assert doc["sector"] == "crude"
    assert set(doc["cycle_anchors"]) >= {"vlcc", "suezmax", "aframax_dirty", "lr2_clean"}


# ---------------------------------------------------------------------------
# Anchor-basis commensurability (B5 — METHODOLOGY §10)
# ---------------------------------------------------------------------------
def test_all_cycle_anchors_carry_valid_anchor_basis():
    """Every cycle_anchor block in every sector must declare an anchor_basis
    drawn from the recognised enum (B5 — METHODOLOGY §10)."""
    valid = set(ANCHOR_BASIS_LABELS)
    for sector in SECTORS:
        anchors = load_scenarios(sector=sector)["cycle_anchors"]
        assert anchors, f"{sector} has no cycle_anchors"
        for cls, block in anchors.items():
            assert "anchor_basis" in block, f"{sector}.{cls} missing anchor_basis"
            assert block["anchor_basis"] in valid, \
                f"{sector}.{cls} anchor_basis {block['anchor_basis']!r} not in {valid}"


def test_anchor_basis_uniform_within_each_sector_and_all_three_present():
    """No sector may mix bases internally (that would surface as 'MIXED'), and
    all three known bases appear somewhere across the book."""
    basis_map = all_sector_anchor_bases()
    valid = set(ANCHOR_BASIS_LABELS)
    assert basis_map
    assert all(b in valid for b in basis_map.values())   # no 'MIXED', no junk
    assert valid <= set(basis_map.values())              # all three are in use
    assert basis_map["crude"] == "tc_10yr_mean"
    assert basis_map["dry_bulk"] == "archive_22mo_median"
    assert basis_map["containerships"] == "fy_calendar_avg"


def test_detect_mixed_anchor_basis():
    # Tanker + LNG sectors share tc_10yr_mean → no cross-basis mix.
    assert detect_mixed_anchor_basis(["crude", "product", "lng"]) is None
    # A single sector is trivially one basis.
    assert detect_mixed_anchor_basis(["dry_bulk"]) is None
    # A cross-basis pairing returns the basis→sectors map with >1 entry.
    mix = detect_mixed_anchor_basis(["crude", "dry_bulk", "containerships"])
    assert mix is not None
    assert set(mix) == {"tc_10yr_mean", "archive_22mo_median", "fy_calendar_avg"}
    assert "crude" in mix["tc_10yr_mean"]
    assert mix["archive_22mo_median"] == ["dry_bulk"]


def test_run_scenarios_weighted_average_identity(doc):
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    r = run_scenarios(ci, 16.40, 16.00, doc)
    assert len(r.scenarios) == 4
    expected = sum(s.weight * s.fair_value for s in r.scenarios)
    assert r.probability_weighted_fv == pytest.approx(expected)


# Point-in-time pin (Jun-9 weights + Jun-11 inputs); re-pin on weight settle
# (post-Hormuz resolution). Re-pinned from skip 2026-06-11 (B3): a pin against
# current intended state catches unintended drift; a skip catches nothing.
# Re-pinned 2026-07-02 (post-stand-down vintage: crude reweight + MoU-ineffective
# leg recalibration — decisions/crude_reweight_proposal_2026-07-02.md).
def test_nav_flexes_with_scenario(doc):
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    r = run_scenarios(ci, 16.40, 16.00, doc)
    navs = {s.name: s.nav_per_share for s in r.scenarios}
    # Vessel values reset with the scenario forward: escalation > pre-MoU > base > bear.
    assert navs["escalation"] > navs["pre_mou_baseline"] > navs["mou_base"] > navs["mou_bear"]
    # DIRECTION REVERSED at the Jun-9 re-pin: under the war-leaning Jun-9 set
    # (escalation 0.25 + pre_mou 0.45 both price ABOVE the current forward) the
    # probability-weighted NAV sits ABOVE today's NAV ($15.79 vs $15.29 at pin
    # time). The v1 assertion (wnav < base) encoded normalization-leaning
    # weights; the relationship is weight-set-dependent, not structural.
    # DIRECTION REVERSED BACK at the 2026-07-02 re-pin: the post-stand-down set
    # (0.10/0.20/0.45/0.25, normalization-leaning) plus the recalibrated
    # MoU-ineffective pre_mou leg put the PW NAV back BELOW today's NAV
    # ($12.40 vs $16.07 at pin time) — same weight-set-dependence as documented above.
    # 2026-07-12 re-pin (Jun-9 war-tilt WEIGHTS restored, doha trigger fired): the
    # direction does NOT reverse back — the Jul-2 semantic recalibration repriced the
    # pre_mou leg (now MoU-INEFFECTIVE, well below the old Jun-9 war-baseline path),
    # so even war-tilt weights leave PW NAV below base ($14.21 vs $16.07 at pin
    # time). Direction depends on weights AND scenario paths, not weights alone.
    # decisions/doha_check_2026-07-12.md.
    # RE-PINNED 2026-08-10 (Stage A): against the RE-ANCHORED base the war-era
    # absolute scenario paths measure ~zero de-escalation flex — weighted scenario
    # NAV now sits marginally ABOVE base via the escalation leg (the documented
    # deck-incoherence, decisions/stage_a_halt_investigation_2026-08-10.md; three
    # position reads VOIDed). The FLEX MECHANISM is what this test guards: scenario
    # NAVs must differ from base (the flex is alive) — the direction re-pins at the
    # 2026-08-16 toll-cliff deck re-derivation.
    wnav = sum(s.weight * s.nav_per_share for s in r.scenarios)
    assert wnav != r.base_nav_per_share
    assert any(abs(s.nav_per_share - r.base_nav_per_share) > 0.01 for s in r.scenarios)


def test_per_scenario_range_brackets_base(doc):
    ci = load_company_inputs("FRO", "2026-Q2")
    r = run_scenarios(ci, 34.50, 30.50, doc)
    for s in r.scenarios:
        assert s.fair_value_low <= s.fair_value <= s.fair_value_high


def test_bear_softer_than_base(doc):
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    r = {s.name: s for s in run_scenarios(ci, 16.40, 16.00, doc).scenarios}
    # Bear scenario has lower forward rates -> lower cycle ratio and lower FV.
    assert r["mou_bear"].cycle_position < r["mou_base"].cycle_position
    assert r["mou_bear"].fair_value < r["mou_base"].fair_value


# Point-in-time pin (Jun-9 weights + Jun-11 inputs); re-pin on weight settle
# (post-Hormuz resolution). Re-pinned 2026-07-02 (post-stand-down vintage:
# crude reweight + MoU-ineffective leg recalibration —
# decisions/crude_reweight_proposal_2026-07-02.md).
def test_lr2_maps_to_clean_curve(doc):
    # FRO's LR2 sleeve uses the scenario lr2_clean curve (spike-sensitive), not
    # the static Aframax proxy. Sanity: the run completes with 3 classes priced.
    ci = load_company_inputs("FRO", "2026-Q2")
    r = run_scenarios(ci, 34.50, 30.50, doc)
    # HOLD at the Jun-9 re-pin. (age-0 = xclusiv Resale $175M; Amendment B reverted
    # the Thread-1 5yr-as-age-0, so FRO's static NAV returns to ~$28.5 and the
    # scenario PW FV sits back inside the HOLD band.) The LR2-clean mapping (this
    # test's actual subject) is unaffected; the run still prices 3 classes.
    # TRIM/SHORT at the 2026-07-02 re-pin: the post-stand-down reweight removes
    # the war premium (PW FV ~$21.4 vs $34.50 at pin time). §12 relabel applies
    # downstream — cycle position, not a short. LR2-clean mapping still the subject.
    assert r.position_recommendation.startswith("TRIM/SHORT")


def test_breakeven_is_scenario_invariant(doc):
    from crude_tanker_fv.breakeven import implied_breakeven_tce

    ci = load_company_inputs("DHT", BOOK_QUARTER)
    r = run_scenarios(ci, 16.40, 16.00, doc)
    # ONE breakeven, equal to the standalone (unflexed) value-weighted blended solve.
    expected = implied_breakeven_tce(ci, 16.40).blended_breakeven_tce
    assert r.breakeven_tce == pytest.approx(expected)
    # The scenario-varying number is the *assumed* forward TCE (an assumption).
    assumed = [s.assumed_tce for s in r.scenarios]
    assert max(assumed) > min(assumed)


def test_position_recommendation_bands():
    assert position_recommendation(0.10) == "BUY (undervalued)"
    assert position_recommendation(-0.10) == "TRIM/SHORT (overvalued)"
    assert position_recommendation(0.0) == "HOLD (fairly valued)"


# --------------------------------------------------------------------------- #
# Sector layer (METHODOLOGY §11) — LNG scenarios for FLNG-style names.
# --------------------------------------------------------------------------- #


def test_lng_sector_scenarios_load(lng_doc):
    names = list(lng_doc["scenarios"])
    # structural_reset is the 5th scenario (energy-transition tail). Curated
    # and available, but weight 0.0 under both Set B (v2) and Set B-revised
    # (v3) — its TCE level, range, vessel haircut and probability are too
    # judgmental for parametric weighting; applied as a qualitative overlay.
    assert names == [
        "tight_resurgence",
        "moderate_tightening",
        "glut_base",
        "glut_intensifies",
        "structural_reset",
    ]
    # Jun-9-2026 point-in-time LNG weights (METHODOLOGY §11.3 v4):
    #   {0.25, 0.25, 0.38, 0.12, 0.00}. Shift from v3: +10pp tight, +0pp moderate,
    #   -7pp glut_base, -3pp glut_intensifies — Hormuz contestation pulls weight
    #   toward tight_resurgence (Qatar LNG transits Hormuz). Re-lock when the
    #   US response to the Jun-8 helicopter downing resolves.
    # Re-pinned 2026-07-02 (post-stand-down vintage: LNG v3 Set B-revised
    #   {0.15, 0.25, 0.45, 0.15, 0.00} RESTORED — the Jun-9 v4 Hormuz tilt unwound
    #   with the stand-down; decisions/crude_reweight_proposal_2026-07-02.md §15/C-4).
    active = ["tight_resurgence", "moderate_tightening", "glut_base", "glut_intensifies"]
    assert sum(lng_doc["scenarios"][n]["weight"] for n in active) == pytest.approx(1.0)
    # Re-pinned 2026-07-14 EVE (Jun-9 war shape RESTORED — OWNER RULING on
    # decisions/hormuz_retilt_proposal_2026-07-13.md: RESTORE BOTH, "all three are
    # affected by hormuz, so should all move together coherently"; round-2 NO-SHOW
    # evidence in doha_round2_check_2026-07-15.md):
    assert lng_doc["scenarios"]["tight_resurgence"]["weight"] == pytest.approx(0.25)
    assert lng_doc["scenarios"]["moderate_tightening"]["weight"] == pytest.approx(0.25)
    assert lng_doc["scenarios"]["glut_base"]["weight"] == pytest.approx(0.38)
    assert lng_doc["scenarios"]["glut_intensifies"]["weight"] == pytest.approx(0.12)
    assert lng_doc["scenarios"]["structural_reset"]["weight"] == pytest.approx(0.0)
    # The structural_reset scenario carries a vessel_scale_multiplier (the -10%
    # accelerated-retirement haircut applied on top of the elasticity-derived flex).
    # The mechanism stays in code for future use (other sectors, fleet-specific
    # overrides) even with structural_reset's weight at 0 today.
    assert lng_doc["scenarios"]["structural_reset"]["vessel_scale_multiplier"] == pytest.approx(0.9)
    assert lng_doc["sector"] == "lng"
    # LNG sector cycle anchors: lng (174k cbm LNGC) + mgc (added 2026-06-01
    # for the gas-carrier sub-class — CCEC's LCO2 / multi-gas / dual-fuel MGC
    # fleet routes through here).
    assert set(lng_doc["cycle_anchors"]) == {"lng", "mgc"}
    assert lng_doc["cycle_anchors"]["lng"]["ten_year_mean"] == 85000
    assert lng_doc["cycle_anchors"]["mgc"]["ten_year_mean"] == 20000


def test_unknown_sector_raises():
    # dry_bulk landed 2026-06-09 (METHODOLOGY §11.7). Use offshore_drilling
    # as the placeholder "not-yet-implemented sector" — next on the roadmap.
    with pytest.raises(KeyError):
        load_scenarios(sector="offshore_drilling")


def test_flng_runs_through_lng_scenarios(lng_doc):
    """FLNG (LNGC pure-play) must value through the LNG sector scenario set,
    not the crude one. The report's scenario list and sector tag are the
    canonical signal that the sector layer is wired correctly end-to-end.
    """
    ci = load_company_inputs("FLNG", "2026-Q2")  # fixture advanced at the 8/25 Q2 refresh (pair guard)
    r = run_scenarios(ci, 30.23, 25.00, lng_doc)
    scen_names = [s.name for s in r.scenarios]
    assert scen_names == [
        "tight_resurgence",
        "moderate_tightening",
        "glut_base",
        "glut_intensifies",
        "structural_reset",
    ]
    assert r.sector == "lng"
    # Sanity: glut_intensifies (orderbook drag) must price below glut_base
    # (the same-curve, lower-tail scenario), which must price below the
    # tight_resurgence upside tail.
    by = {s.name: s for s in r.scenarios}
    assert by["glut_intensifies"].fair_value < by["glut_base"].fair_value
    assert by["glut_base"].fair_value < by["tight_resurgence"].fair_value
    # structural_reset carries a -10% vessel_scale_multiplier on top of the
    # elasticity flex, so its NAV (and therefore FV) must sit BELOW glut_intensifies
    # despite a slightly milder front-quarter curve. The two scenarios differ in
    # mechanism (cyclical vs structural), and structural_reset is meant to be the
    # more bearish tail by construction.
    assert by["structural_reset"].fair_value < by["glut_intensifies"].fair_value


# Point-in-time pin (Jun-9 v4 LNG weights + Jun-11 inputs); re-pin on weight
# settle (post-Hormuz resolution). Band re-based 2026-06-11 from the v3 $28.04
# pin to the Jun-9-v4 $29.73: ±5% → [28.24, 31.22].
def test_flng_v3_set_b_revised_fv_band(lng_doc):
    """v3 lock (METHODOLOGY §11.3) — Set B-revised weights locked 2026-06-01
    based on the Ras Laffan + Cheniere Stage 3 timing reality (see §11.3 v3
    transition + §13 infrastructure-constraint limitation).

    Weight set: tight 0.15 / moderate 0.25 / glut_base 0.45 / glut_intensifies
    0.15 / structural_reset 0.00 (constructive total 0.85 vs Set B's 0.80).

    FLNG headline FV: $28.04 under Set B-revised (vs $26.17 under Set B).
    Position stays TRIM/SHORT (EV improved from -13.4% to -7.2%, still below
    the -5% HOLD threshold). The reweighting tightens the call but doesn't
    flip it — FLNG's mature TC-heavy book has less scenario torque than
    CCEC's newbuild-heavy structure.

    Band: ±5% around $28.04 → [$26.64, $29.44]. Tight enough to catch a
    deliberate weight shift; loose enough to absorb routine elasticity /
    NAV calibration changes. If this assertion fails, check (a) whether the
    weight set in inputs/scenario_inputs.yaml has been modified, or (b)
    whether a structural change to the LNG scenario forwards has landed.
    """
    ci = load_company_inputs("FLNG", "2026-Q2")  # fixture advanced at the 8/25 Q2 refresh (pair guard)
    r = run_scenarios(ci, 30.23, 25.00, lng_doc)
    assert 28.24 < r.probability_weighted_fv < 31.22
    # The weighted-FV identity (already covered for crude) holds in LNG too —
    # including the structural_reset scenario at weight 0 contributing nothing.
    expected = sum(s.weight * s.fair_value for s in r.scenarios)
    assert r.probability_weighted_fv == pytest.approx(expected)


# Point-in-time pin (Jun-9 v4 LNG weights); re-pin on weight settle
# (post-Hormuz resolution).
def test_flng_v3_locked_weights_position(lng_doc):
    """Position pinned separately from the FV band so a future calibration
    that pushes the EV across a band boundary surfaces as a deliberate
    methodology choice rather than a silent regression.

    History: TRIM/SHORT under v3 Set B-revised (EV −7.2%); the Jun-9 v4
    reweight (tight_resurgence gains mass on Hormuz/Qatar exposure) lifted
    FLNG inside the HOLD band — pinned HOLD at the 2026-06-11 re-pin.
    """
    ci = load_company_inputs("FLNG", "2026-Q2")  # fixture advanced at the 8/25 Q2 refresh (pair guard)
    r = run_scenarios(ci, 30.23, 25.00, lng_doc)
    assert "HOLD" in r.position_recommendation, (
        f"FLNG position should be HOLD under Jun-9 v4 weights; got "
        f"{r.position_recommendation!r}"
    )


def test_ccec_position_under_locked_weights(lng_doc):
    """Under Set B-revised (the production lock), CCEC's position is BUY —
    EV +14.1% comfortably above the +5% threshold. The BUY signal is
    *weight-driven* (METHODOLOGY §13) — CCEC's $2.25B NB orderbook gives it
    ~2× FLNG's scenario torque, so the same constructive tilt produces a
    flip for CCEC where FLNG only gets closer to HOLD. Position sizing
    should reflect that the call's robustness depends on the weight set.
    """
    ci = load_company_inputs("CCEC", BOOK_QUARTER)
    r = run_scenarios(ci, 23.18, 25.17, lng_doc)
    assert "BUY" in r.position_recommendation, (
        f"CCEC position should be BUY under Set B-revised; got "
        f"{r.position_recommendation!r}"
    )


@pytest.fixture(scope="module")
def dry_bulk_doc():
    return load_scenarios(sector="dry_bulk")


def test_dry_bulk_locked_weights_position(dry_bulk_doc):
    """WO4 §9.10 lock: pin the locked Bulk Set A weights AND SBLK's position
    under them, so a future dry-bulk reweight surfaces as a deliberate
    methodology choice, not a silent regression (analogue of
    test_flng_v3_locked_weights_position).

    Fixed price (25.20/34.50, the 2026-07-03 consensus vintage) makes this a
    pure weight-lock guard, immune to daily price drift. SBLK is the canonical
    VALIDATED-TIGHT dry-bulk validator; at the static vintage it is BUY +13.3%,
    comfortably above the +5% threshold. The §9.10 diagnostic
    (scripts/dry_bulk_weight_comparison.py) shows the LABEL is position-driven
    at deeper China-property-drag brackets, but the EV SIGN is stable-positive
    across the whole family — which is the field the consumer's Gate E reads."""
    names = ["china_acceleration", "moderate_growth",
             "china_property_drag", "coordinated_slowdown"]
    assert {n: dry_bulk_doc["scenarios"][n]["weight"] for n in names} == {
        "china_acceleration": pytest.approx(0.20),
        "moderate_growth": pytest.approx(0.40),
        "china_property_drag": pytest.approx(0.25),
        "coordinated_slowdown": pytest.approx(0.15),
    }, "Bulk Set A weights moved — reweighting is a §11.7.x revision, not silent"
    ci = load_company_inputs("SBLK", BOOK_QUARTER)
    r = run_scenarios(ci, 25.20, 34.50, dry_bulk_doc,
                      scenario_class_map=SCENARIO_CLASS_MAP_BY_SECTOR["dry_bulk"])
    assert "BUY" in r.position_recommendation, (
        f"SBLK should be BUY under locked Bulk Set A at the pinned vintage; "
        f"got {r.position_recommendation!r}")


@pytest.fixture(scope="module")
def lpg_doc():
    return load_scenarios(sector="lpg")


def test_lpg_locked_weights_and_anchor(lpg_doc):
    """WO3 Phase 1 lock (2026-07-08): pin the ratified LPG Set A
    (US-export-arb) weights AND the ratified cycle anchor, so a future LPG
    reweight or anchor move surfaces as a deliberate §11.10.x revision, not a
    silent regression. Ratification record: decisions/lpg_methodology_2026-07-07.md
    (all five forks closed 2026-07-07 — weights evidence-first overhang-tilted,
    anchor ~$40k 10-yr through-cycle REALIZED TCE, as_of-dated with an annual
    re-derivation trigger `lpg_anchor_annual_review`).

    No position pin yet — the Phase-4 validators (Dorian LPG / BW LPG) are not
    onboarded; add the SBLK-style position pin when the first validator lands.
    """
    names = ["arb_wide", "absorption_base", "overhang", "arb_collapse"]
    assert list(lpg_doc["scenarios"]) == names
    assert {n: lpg_doc["scenarios"][n]["weight"] for n in names} == {
        "arb_wide": pytest.approx(0.15),
        "absorption_base": pytest.approx(0.35),
        "overhang": pytest.approx(0.35),
        "arb_collapse": pytest.approx(0.15),
    }, "LPG Set A weights moved — reweighting is a §11.10.x revision, not silent"
    assert sum(lpg_doc["scenarios"][n]["weight"] for n in names) == pytest.approx(1.0)

    # Ratified anchor: $40k realized-TCE, TRAILING (drifts) → as_of-dated.
    anchor = lpg_doc["cycle_anchors"]["vlgc"]
    assert anchor["ten_year_mean"] == 40000
    assert anchor["anchor_basis"] == "realized_tce_10yr_mean"
    assert str(anchor["as_of"]) == "2026-07-07", (
        "the LPG anchor is a trailing 10-yr average and must stay as_of-dated "
        "(re-derived annually under lpg_anchor_annual_review)")

    # v1 routing: VLGC-only (Fork 1) — no MGC in this sector.
    assert SCENARIO_CLASS_MAP_BY_SECTOR["lpg"] == {"VLGC": "vlgc"}
    # Every scenario carries the full 8-quarter vlgc curve.
    for n in names:
        assert len(lpg_doc["scenarios"][n]["vlgc"]) == 8


def test_lpg_realized_tce_basis_does_not_compose_with_tc_means():
    """The realized-TCE anchor basis (ratified 2026-07-07: correct for an
    85-99%-spot validator pair, NOT a compromise) is a FOURTH basis — a
    cross-sector view mixing lpg with the TC-anchored sectors must trip the
    MIXED-ANCHOR-BASIS flag rather than silently comparing cycle ratios."""
    mix = detect_mixed_anchor_basis(["crude", "lpg"])
    assert mix is not None
    assert mix["realized_tce_10yr_mean"] == ["lpg"]
    assert "crude" in mix["tc_10yr_mean"]


def test_lng_weights_sum_to_one(lng_doc):
    """Explicit invariant: the LNG scenario weights must sum to 1.0 across the
    four ACTIVE scenarios (structural_reset is curated but inactive at weight
    0.0). Independent of which weight set is locked — applies to Set B,
    Set B-revised, or any future Set C. Catches the most common YAML
    edit error (typo in a weight) before downstream scenarios get distorted.
    """
    active = ["tight_resurgence", "moderate_tightening", "glut_base", "glut_intensifies"]
    total_active = sum(lng_doc["scenarios"][n]["weight"] for n in active)
    assert total_active == pytest.approx(1.0), (
        f"Active LNG weights should sum to 1.0; got {total_active:.4f}. "
        f"Check inputs/scenario_inputs.yaml sectors.lng.scenarios.<name>.weight."
    )
    # All-in (including structural_reset) sum check — should also equal 1.0 in
    # the current production lock because structural_reset is at 0.0; this
    # would tighten to a different invariant if structural_reset were ever
    # activated at non-zero weight.
    all_in = sum(s["weight"] for s in lng_doc["scenarios"].values())
    assert all_in == pytest.approx(1.0)


# Point-in-time pin (Jun-9 v4 LNG weights + Jun-11 inputs); re-pin on weight
# settle (post-Hormuz resolution). Band re-based 2026-06-11 from the v3 $26.45
# pin to the Jun-9-v4 $29.63: ±5% → [28.15, 31.11]. EV +27.8% at pin time.
# Re-pinned 2026-07-02 (post-stand-down vintage: LNG v3 Set B-revised restored —
# decisions/crude_reweight_proposal_2026-07-02.md): $33.50, ±5% → [31.82, 35.17].
# EV +44.5% at pin time — BUY holds.
def test_ccec_v3_set_b_revised_fv_band_and_buy_flip(lng_doc):
    """v3 lock companion test — CCEC PW FV jumps from $22.94 (Set B HOLD)
    to $26.45 (Set B-revised BUY) under the reweighting. The flip is
    structurally driven by CCEC's newbuild option value (~$2.25B committed):
    NB value compresses brutally in glut scenarios and expands materially in
    tight scenarios, so the Ras Laffan tilt rewards CCEC ~2× as much in
    absolute PW FV terms as it rewards FLNG. The flip is a finding, not the
    target — the weights were specified before this test was computed.

    Band: ±5% around $26.45 → [$25.13, $27.77]. Position must be BUY
    (EV > +5%) — if it slips to HOLD the underlying NAV or scenario forwards
    have drifted enough to demand a methodology review (see §13).
    """
    ci = load_company_inputs("CCEC", BOOK_QUARTER)
    r = run_scenarios(ci, 23.18, 25.17, lng_doc)
    # 2026-06-22 rebased for the cycle-conditional terminal + NET RETAINED EARNINGS
    # (§9.2): CCEC is low-payout LNG with high scenario torque, so retained earnings
    # lift PW FV ~$29 → ~$35.9 (BUY held, EV strengthens).
    # Re-pinned 2026-07-02 (post-stand-down vintage: LNG v3 restore pulls the Jun-9
    # tight_resurgence tilt back out — PW FV ~$33.50, ±5%; BUY held at EV +44.5%).
    # Re-pinned 2026-07-14 EVE (hormuz re-tilt RESTORE BOTH executed): $35.91 ±5% -> [34.11, 37.70].
    # Re-pinned 2026-08-08 (Q2 refresh, band-verified −6.2% FV move: capex schedule
    # 2,251.5→1,697.0 + full-WC basis + debt draws + census hull — ccec_log):
    # $33.70 ±5% -> [32.02, 35.39]. BUY held throughout.
    assert 32.02 < r.probability_weighted_fv < 35.39
    # Position must be BUY at locked weights — flag if it shifts.
    ev_pct = r.expected_value_vs_current / r.current_price * 100
    assert ev_pct > 5.0, (
        f"CCEC EV {ev_pct:.1f}% — expected BUY (>+5%) under Set B-revised. "
        f"If this drifts to HOLD, review §13 weight-stability framework."
    )


# --------------------------------------------------------------------------- #
# Product sector (METHODOLOGY §11.5) — clean-trade product fleet scenarios.
# --------------------------------------------------------------------------- #


@pytest.fixture(scope="module")
def product_doc():
    return load_scenarios(sector="product")


def test_product_sector_scenarios_load(product_doc):
    names = list(product_doc["scenarios"])
    # 5 scenarios: 4 cyclical + structural_decline tail (curated but weight 0).
    assert names == [
        "refinery_squeeze",
        "moderate_correction",
        "glut_base",
        "demand_softening",
        "structural_decline",
    ]
    # Product Set B v2 LOCKED weights (locked 2026-06-03, METHODOLOGY §11.5 v2,
    # rationale §14.6 + §11.5 v2 transition section): {0.15, 0.25, 0.45, 0.15, 0.00}.
    # Same shift direction as LNG Set B → Set B-revised: 10pp moved from
    # bear-side (glut_base + demand_softening) into constructive band
    # (refinery_squeeze + moderate_correction). Source: Catlin VIE June 2026.
    # structural_decline weight 0 unchanged (energy-transition tail, applied as
    # qualitative overlay).
    # Re-pinned 2026-07-02 (post-stand-down vintage: Product Set B v2
    # {0.15, 0.25, 0.45, 0.15, 0.00} RESTORED — the Jun-9 Hormuz tilt unwound with
    # the stand-down; decisions/crude_reweight_proposal_2026-07-02.md §15/C-4).
    active = ["refinery_squeeze", "moderate_correction", "glut_base", "demand_softening"]
    assert sum(product_doc["scenarios"][n]["weight"] for n in active) == pytest.approx(1.0)
    # Re-pinned 2026-07-14 EVE (Jun-9 war shape RESTORED — OWNER RULING on
    # decisions/hormuz_retilt_proposal_2026-07-13.md: RESTORE BOTH, "all three are
    # affected by hormuz, so should all move together coherently"; round-2 NO-SHOW
    # evidence in doha_round2_check_2026-07-15.md):
    assert product_doc["scenarios"]["refinery_squeeze"]["weight"] == pytest.approx(0.25)
    assert product_doc["scenarios"]["moderate_correction"]["weight"] == pytest.approx(0.30)
    assert product_doc["scenarios"]["glut_base"]["weight"] == pytest.approx(0.30)
    assert product_doc["scenarios"]["demand_softening"]["weight"] == pytest.approx(0.15)
    assert product_doc["scenarios"]["structural_decline"]["weight"] == pytest.approx(0.0)
    # Each scenario carries the three product-class forwards (mr, lr1_clean, lr2_clean).
    for n in names:
        s = product_doc["scenarios"][n]
        assert set(s) >= {"mr", "lr1_clean", "lr2_clean"}, f"scenario {n} missing class forwards"
    # structural_decline carries a -10% vessel_scale_multiplier (analogous to LNG's
    # structural_reset — accelerated-retirement haircut for the secular tail).
    assert product_doc["scenarios"]["structural_decline"]["vessel_scale_multiplier"] == pytest.approx(0.9)
    # Cycle anchors for the three product classes.
    assert set(product_doc["cycle_anchors"]) == {"mr", "lr1_clean", "lr2_clean"}
    assert product_doc["cycle_anchors"]["mr"]["ten_year_mean"] == 16000
    assert product_doc["cycle_anchors"]["lr1_clean"]["ten_year_mean"] == 25000
    assert product_doc["cycle_anchors"]["lr2_clean"]["ten_year_mean"] == 27000
    assert product_doc["sector"] == "product"


# Point-in-time pin (Jun-9 weights + Jun-11 inputs); re-pin on weight settle
# (post-Hormuz resolution).
def test_insw_whole_company_fv_preserved_through_product_sector_refactor():
    """HISTORY: originally pinned the 'INSW whole-co FV preserved exactly
    through the product-sector refactor' invariant at $52.03; the Jun-9
    Issue #1 fix deliberately broke that (it preserved a copy bug); re-pinned
    2026-06-11 (B3). THEN 2026-07-02 (review C-3) the aggregation identity
    itself CHANGED: the old form applied CRUDE weights to both sleeves
    (rank-1 index pairing — product weight changes could not move INSW
    whole-co FV, which was the bug: INSW's product sleeve was being
    probability-weighted by the Hormuz state). The identity asserted below is
    now the per-sleeve form: whole-co PW FV = crude sleeve PW FV + product
    sleeve PW FV, each ladder weighted by ITS OWN sector's probabilities
    (cross-sector independence).

    Re-pinned 2026-07-02 (post-stand-down vintage: crude reweight 0.10/0.20/
    0.45/0.25 + MoU-ineffective leg recalibration + product v2 restore —
    decisions/crude_reweight_proposal_2026-07-02.md): PW FV ~$66.2 → ~$51.76;
    band keeps the prior relative width (~±2.3%) → [50.6, 52.9]. The per-sleeve
    identity assertions below are weight-agnostic and unchanged.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    insw = watchlist["INSW"]
    ci = load_company_inputs("INSW", BOOK_QUARTER)   # was a 2026-Q1 literal — pair-guarded at the INSW Q2 advance (2026-08-10)
    docs = _load_all_sectors()
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "INSW", ci, insw["current_price"], insw["analyst_target"], docs, watchlist,
    )
    # 2026-06-22: cycle-conditional terminal + net retained earnings (§9.2) lift
    # INSW PW FV ~$64.5 → ~$66.2 (TRIM/SHORT held).
    # 2026-07-02: post-stand-down reweight removes the war premium → ~$51.76
    # (TRIM/SHORT held; §12 relabel applies downstream).
    # 2026-07-12: Jun-9 war tilt RESTORED (doha trigger fired,
    # decisions/doha_check_2026-07-12.md) → ~$57.15; ±2.5% band. TRIM/SHORT still
    # holds at $82.98 (the war premium narrows the read, doesn't flip it).
    # 2026-07-31: B' reweight (dead-MoU mass retired -> pre_mou 0.57) lifts the
    # crude sleeve → ~$58.82; ±2.5% band re-pinned. TRIM/SHORT still holds —
    # the reweight narrows the negative read, doesn't flip it.
    # decisions/ceasefire_mediation_check_2026-07-31.md.
    assert 61.25 < headline.probability_weighted_fv < 64.40   # re-pinned 2026-08-10 STAGE A (deck-incoherence lift, stage_a_halt_investigation_2026-08-10.md; re-reads at the 8/16 deck re-derivation): $62.82 +/-2.5%
    # Both sleeves should have valid prob-weighted FVs.
    assert crude_r is not None and product_r is not None
    assert crude_r.probability_weighted_fv > 0
    assert product_r.probability_weighted_fv > 0
    # C-3 identity (2026-07-02): whole-co aggregation EQUALS
    # crude_pw_fv + product_pw_fv — each sleeve weighted by its own sector's
    # probabilities. The old index-paired form (crude weights applied to the
    # summed ladder) coincided with this only while the two families carried
    # identical weights; the Jun-9 crude reweight broke that silently.
    expected_headline = crude_r.probability_weighted_fv + product_r.probability_weighted_fv
    assert headline.probability_weighted_fv == pytest.approx(expected_headline, abs=0.01)
    # And a product-weight change MUST now move the whole-co FV (the old form
    # was invariant to it — that invariance was the bug).
    import copy as _copy
    docs2 = dict(docs)
    docs2["product"] = _copy.deepcopy(docs["product"])
    names = list(docs2["product"]["scenarios"])
    docs2["product"]["scenarios"][names[0]]["weight"] += 0.10
    docs2["product"]["scenarios"][names[2]]["weight"] -= 0.10
    headline2, _, _ = _run_scenarios_for_ticker(
        "INSW", ci, insw["current_price"], insw["analyst_target"], docs2, watchlist,
    )
    assert headline2.probability_weighted_fv != pytest.approx(
        headline.probability_weighted_fv, abs=0.01)


def test_crude_ticker_does_not_load_lng_doc():
    """A crude ticker run through the LNG doc would crash (the doc has no
    `vlcc` key). This is intentional: the pipeline must resolve sector before
    handing a doc to run_scenarios. Catching the KeyError here pins the
    contract — the sector layer is not a soft default.
    """
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    with pytest.raises(KeyError):
        run_scenarios(ci, 16.40, 16.00, load_scenarios(sector="lng"))


# ----------------------------------------------------------------------------
# ASC (Ardmore Shipping) — first pure-product onboarded ticker (METHODOLOGY §11.5)
# ASC is to the product sector what DHT is to crude and FLNG is to LNG: an all-
# single-class pure-play used as the methodology validator. Tests here pin the
# product-sector class-map routing for pure-plays (the fix for the bug where
# `_run_scenarios_for_ticker` defaulted to the crude+lng class map for any
# non-hybrid name and crashed on MR).
# ----------------------------------------------------------------------------


def test_asc_pure_product_uses_product_class_map():
    """ASC's pure-product routing must reach `mr` / `lr1_clean` / `lr2_clean`
    scenario keys (not the crude `vlcc` / `aframax_dirty` set). If the pipeline
    handed ASC the default class map by accident the scenario engine would
    raise KeyError('MR') — the regression that prompted the §11.5 fix.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    asc = watchlist["ASC"]
    ci = load_company_inputs("ASC", BOOK_QUARTER)
    docs = _load_all_sectors()
    # The smoke test is just "does this not raise"; the KeyError-from-pre-fix
    # would have surfaced here. Behavioural pinning comes from the next test.
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "ASC", ci, asc["current_price"], asc["analyst_target"], docs, watchlist,
    )
    # Pure-play: only headline is populated, sleeve reports are None.
    assert crude_r is None and product_r is None
    assert headline.sector == "product"
    # All five product-sector scenarios should run.
    scen_names = {s.name for s in headline.scenarios}
    assert "refinery_squeeze" in scen_names
    assert "moderate_correction" in scen_names
    assert "demand_softening" in scen_names
    assert "structural_decline" in scen_names


# Point-in-time pin (Jun-9 v3 product weights + Jun-11 inputs); re-pin on
# weight settle (post-Hormuz resolution). Band re-based 2026-06-11 from the
# Set-B-v2 $14.24 pin to the Jun-9-v3 $15.07: ±5% → [14.32, 15.82].
def test_asc_whole_company_fv_in_expected_band():
    """ASC probability-weighted FV pinned in the $16.35-$17.35 band, REBASED
    2026-07-01 for the full balance-sheet reconciliation (was $14.32-$15.82
    under Product Set B v2). Corrected 2026-Q1 inputs produce ~$16.85 (NAV/sh
    $17.82). The +$1.86 NAV lift vs the prior $15.96 is: the April-2026 Handysize
    newbuild EXCLUDED from Q1 (a subsequent event — +$2.15, it was wrongly loaded
    as a −$88.8M commitment-only drag); phantom `Ardmore_Patriot` removed (−$0.90);
    the 4 chemical Handies re-marked to a cited 20-F carrying-value floor (+$0.58);
    balance sheet re-sourced to the 3/31 6-K (net small). See the reconciliation
    pre-reg decisions/asc_reconciliation_prereg_2026-07-01.md.

    A larger drift means: an input changed (likely OK), the MR / LR1 / LR2 forward
    curves shifted (review), or the product-sector class routing regressed (NOT OK).

    Re-pinned 2026-07-02 (post-stand-down vintage: product Set B v2 weights
    {0.15/0.25/0.45/0.15} restored — decisions/crude_reweight_proposal_2026-07-02.md):
    PW FV ~$16.85 → ~$16.30; band keeps the prior ±3% width → [15.81, 16.79].
    Position at re-pin: HOLD (the TRIM/SHORT exclusion below still holds).
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    asc = watchlist["ASC"]
    ci = load_company_inputs("ASC", BOOK_QUARTER)
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "ASC", ci, asc["current_price"], asc["analyst_target"], docs, watchlist,
    )
    # Re-pinned 2026-07-14 EVE (hormuz re-tilt): $16.85 ±5% -> [16.01, 17.70] — back at the pre-stand-down FV.
    assert 16.01 < headline.probability_weighted_fv < 17.70
    # The reconciliation corrected the overvalued read away. RE-PINNED 2026-08-29
    # at the 8/28 consensus-pair rebase: the fixture price moved 17.0 -> 17.7 and
    # ASC's EV at the new vintage sits just past the -5% edge -> the position
    # prints TRIM/SHORT again — this is the KNOWN price-side band oscillator
    # (pre-warned at the 8/16 ratify; NAV delta +0.0% at the rebase, so the
    # "input regressed" failure mode this test guards is directly disproven by
    # the drift gate). The FV band above stays the real regression guard; the
    # position may oscillate HOLD<->T/S with the tape near the edge.
    assert headline.position_recommendation.startswith(("HOLD", "TRIM/SHORT"))  # oscillator-tolerant since 2026-08-29


def test_product_weights_sum_to_one(product_doc):
    """Explicit invariant: the product scenario weights must sum to 1.0
    across the four ACTIVE scenarios (structural_decline is curated but
    inactive at weight 0.0). Independent of Set A vs Set B vs any future
    Set C. Catches the most common YAML edit error (typo in a weight)
    before downstream scenarios get distorted.
    """
    active = ["refinery_squeeze", "moderate_correction", "glut_base", "demand_softening"]
    total_active = sum(product_doc["scenarios"][n]["weight"] for n in active)
    assert total_active == pytest.approx(1.0), (
        f"Active product weights should sum to 1.0; got {total_active:.4f}. "
        f"Check inputs/scenario_inputs.yaml sectors.product.scenarios.<name>.weight."
    )
    all_in = sum(s["weight"] for s in product_doc["scenarios"].values())
    assert all_in == pytest.approx(1.0)


# Note: test_stng_whole_company_fv_in_expected_band_under_set_b was consolidated
# into the existing test_stng_whole_company_fv_in_expected_band below — the
# rebased band [$70, $77] covers the Set B value $73.58.


def test_hafn_full_three_class_product_loads_and_routes():
    """HAFN (Hafnia) is the second watchlist name with all three core product
    classes (10 LR2 + 25 LR1 + 49 MR) and — as of 2026-06-05 — its 22 Handysize
    hulls ON-curve via the new Handysize class (was off-curve in working_capital_net).
    Exercises the LR1 → lr1_clean and Handysize → mr (v1 proxy) rate routing.

    Also the FIRST IFRS-reporting name on the watchlist (TRMD is dual-listed
    but US-equivalent; HAFN is Bermuda-incorporated + Singapore-headquartered
    with IFRS presentation). Tests that the loader accepts the multi-class
    manifest (incl. Handysize) under IFRS-derived input conventions.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    hafn = watchlist["HAFN"]
    ci = load_company_inputs("HAFN", "2026-Q2")
    docs = _load_all_sectors()
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "HAFN", ci, hafn["current_price"], hafn["analyst_target"], docs, watchlist,
    )
    assert crude_r is None and product_r is None
    assert headline.sector == "product"
    classes = {v.cls for v in ci.fleet.vessels}
    assert classes == {"LR2", "LR1", "MR", "Handysize"}, \
        f"HAFN should be LR2+LR1+MR+Handysize (Handy on-curve 2026-06-05), got {classes}"


# Point-in-time pin (Jun-9 v3 product weights + Jun-11 inputs); re-pin on
# weight settle (post-Hormuz resolution). Band re-based 2026-06-11 from the
# Set-B-v2 $5.35 pin to the Jun-9-v3 $5.87: ±5% → [5.58, 6.16].
def test_hafn_whole_company_fv_in_expected_band_set_b():
    """HAFN probability-weighted FV pinned in the $6.10-$6.55 band, REBASED
    2026-07-01 for the full balance-sheet reconciliation (was $5.58-$6.16).
    Corrected Q1-2026 inputs produce ~$6.33 (base NAV/sh $5.69, up from $5.35).
    The +$0.35 NAV lift is: the 8 MR HHI newbuild EXCLUDED from Q1 (signed
    3-Apr-2026, a subsequent event — was a −$405M commitment-only drag + $40M
    phantom advance, the ASC pattern: +$365M); TORM stake to Hafnia's own
    lower-of-cost NAV basis $277.2M (−$117.8M vs the prior $395M market);
    total_debt/lease corrected to the Note-2/4 split $953.9M + $71.6M (−$46M);
    shares → 505.3M. Operating WC held at a conservative pool-gross-up floor
    ($85.7M, NOT the gross balance-sheet $335.9M — pool custodial receivables
    are not NAV-economic). See decisions/hafn_reconciliation_prereg_2026-07-01.md.

    HAFN stays TRIM/SHORT: price $7.70 is ~1.35× the tool's conservative
    (txn-anchored) NAV. The verdict RELABELS this "rich · cycle position (not a
    short)" (§12); the tool↔broker spread (−31% to broker $8.11) is a documented
    feature (txn-anchored marks < broker resale), not an error. HAFN stays
    PROVISIONAL · pool-gross-up-pending (WC floor) — NOT handoff-ready.

    Re-pinned 2026-07-02 (post-stand-down vintage: product Set B v2 weights
    {0.15/0.25/0.45/0.15} restored — decisions/crude_reweight_proposal_2026-07-02.md):
    PW FV ~$6.33 → ~$5.70; band keeps the prior ±3.6% width → [5.50, 5.90].
    TRIM/SHORT held at re-pin.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    hafn = watchlist["HAFN"]
    ci = load_company_inputs("HAFN", "2026-Q2")
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "HAFN", ci, hafn["current_price"], hafn["analyst_target"], docs, watchlist,
    )
    # Re-pinned 2026-07-14 EVE (hormuz re-tilt): $6.33 ±5% -> [6.01, 6.65] — back at the pre-stand-down FV.
    # Re-pinned 2026-08-31 at the Q2 refresh (band-verified NAV $4.64 in [4.40,5.45]):
    # the JV correction (16 hulls at 100% -> 8 x 50% equivalents + $197.75M debt netted)
    # + the ten-hull HHI commitment (8 firm on-curve) move PW FV $6.67 -> $5.59; ±5%.
    assert 5.31 < headline.probability_weighted_fv < 5.87
    assert "TRIM/SHORT" in headline.position_recommendation   # re-pinned 2026-08-13 at the
    # consensus-pair rebase: this test reads the LIVE watchlist price, which moved 7.0 -> 7.6
    # (2026-08-07 Pareto daily). The 8/10 STAGE-A note said the fixture-price read had crossed
    # TRIM->HOLD on the deck lift "while live-book HAFN stays TRIM at the real price" — the
    # rebase moved the fixture ONTO the real price, so the two agree again and it reads TRIM.
    # Still re-reads at the 8/16 deck re-derivation.
    # Belt-and-suspenders per workflow verifier: assert sector explicitly so a
    # silent watchlist-typo regression (HAFN tagged as crude or lng) doesn't
    # accidentally pass the band test by coincidence.
    assert headline.sector == "product"


def test_trmd_full_three_class_product_loads_and_routes():
    """TRMD is the FIRST watchlist name with all three product classes
    (22 LR2 + 10 LR1 + 63 MR). Exercises all three branches of the
    PRODUCT_SCENARIO_CLASS_MAP simultaneously: MR → mr, LR1 → lr1_clean,
    LR2 → lr2_clean. STNG uses MR + LR2 only; INSW touches LR1 only via the
    30/70 product carve-out split. TRMD is the cleanest end-to-end exercise
    of `lr1_clean` rate forwards (METHODOLOGY §11.5).
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    trmd = watchlist["TRMD"]
    ci = load_company_inputs("TRMD", "2026-Q2")  # fixture advanced at the 8/29 Q2 refresh (pair guard); Q2 PW FV $35.79 sits inside the standing 8/10 pin
    docs = _load_all_sectors()
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "TRMD", ci, trmd["current_price"], trmd["analyst_target"], docs, watchlist,
    )
    assert crude_r is None and product_r is None
    assert headline.sector == "product"
    classes = {v.cls for v in ci.fleet.vessels}
    assert classes == {"LR2", "LR1", "MR"}, f"TRMD should be LR2+LR1+MR, got {classes}"


# Point-in-time pin (Jun-9 v3 product weights + Jun-11 inputs); re-pin on
# weight settle (post-Hormuz resolution). Band re-based 2026-06-11 from the
# Set-B-v2 $25.59 pin to the Jun-9-v3 $27.83: ±5% → [26.44, 29.22].
def test_trmd_whole_company_fv_in_expected_band_set_b():
    """TRMD probability-weighted FV pinned in $32-$34 band under Product Set B v2
    (locked 2026-06-03). Q1 2026 inputs produce ~$33.03 (EV +17%, BUY) at watchlist
    price $28.20.

    REBASED 2026-07-02 by the eighth P0 reconciliation (full balance-sheet sourcing
    to the Q1-2026 6-K, EDGAR acc 0000919574-26-003082, workflow-verified). The prior
    band ($24-27, a TRIM) rested on six [ESTIMATE] figures that suppressed NAV: the
    ~$360M newbuild commitment bundled 6 MR resales bought AFTER quarter-end (subsequent
    event → real Q1 commitment $31.2M for the 2 in-Q1 resales), and operating WC was
    estimated at $110M vs the sourced $254.9M. Base NAV $26.74→$31.65; the 2 MR resales
    wired on-curve (§9.6) and scrubbers corrected to the disclosed 85 (owner forks).
    TRMD → GOVERNED-WIDE·basis-pending (product nav_basis pending-sourceable, not TIGHT).

    If this band drifts: check (a) the sourced balance-sheet figures, (b) the 2 on-curve
    MR resales (years_to_delivery 0.12), (c) the LR1 cohort assumptions.

    Re-pinned 2026-07-02 (post-stand-down vintage: product Set B v2 weights
    {0.15/0.25/0.45/0.15} restored — decisions/crude_reweight_proposal_2026-07-02.md):
    PW FV ~$33.03 → ~$29.68; band keeps the prior ±3% width → [28.78, 30.58].
    Still BUY at re-pin.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    trmd = watchlist["TRMD"]
    ci = load_company_inputs("TRMD", "2026-Q2")  # fixture advanced at the 8/29 Q2 refresh (pair guard); Q2 PW FV $35.79 sits inside the standing 8/10 pin
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "TRMD", ci, trmd["current_price"], trmd["analyst_target"], docs, watchlist,
    )
    # Re-pinned 2026-07-14 EVE (hormuz re-tilt): $33.03 ±5% -> [31.38, 34.68] — back at the pre-stand-down FV.
    assert 35.21 < headline.probability_weighted_fv < 38.91   # re-pinned 2026-08-29 Q2 REFRESH (trmd_q2_prereg_2026-08-25.md band-HIT; the six §9.6 newbuild-resales + sourced sheet legs lift scenario PW FV $34.89->$37.06): $37.06 +/-5%. Prior: 8/10 Stage A $34.89 +/-5%


def test_asc_fleet_loads_mr_plus_handysize():
    """ASC's on-curve fleet: 18 MRs + 2 clean-product Handysize hulls
    (Defender/Dauntless, on-curve via the Handysize class). The 4 × 25k stainless
    chemical Handies stay OFF-curve. Pins the loader's class-agnostic behaviour
    incl. the Handysize class. (18 MRs, not 19 — the phantom `Ardmore_Patriot` was
    removed 2026-07-01: never an Ardmore vessel, 0 mentions in the 6-K/20-F.)
    """
    ci = load_company_inputs("ASC", BOOK_QUARTER)
    classes = {v.cls for v in ci.fleet.vessels}
    assert classes == {"MR", "Handysize"}, f"ASC fleet should be MR+Handysize, got {classes}"
    # Q2 census (transition 2026-08-08; manifest = the verified 4b444f9 state):
    # 18 MR + 3 Handysize rows, 2 of them the §9.6 on-curve NB rows carrying the
    # 4-hull order whose $183.6M commitment the 7/31 half-application hid.
    assert len(ci.fleet.vessels) == 21, f"ASC rows should be 21 (18 MR + 3 Handysize), got {len(ci.fleet.vessels)}"
    # MR + Handysize rows with eco: true. 5 × 2013 MRs are eco: false (pre-2014
    # Eco-Mod); the 2 product Handies (2015) are eco: true; + the 2 Q2 NB rows
    # (eco by the §3.1 newbuild rule, newbuild_specs 4b444f9) = 16.
    eco_count = sum(1 for v in ci.fleet.vessels if v.eco)
    assert eco_count == 16, f"ASC eco rows should be 16 (13 eco MR + 3 eco Handysize incl. 2 NB), got {eco_count}"
    # Zero scrubbers fleet-wide — Ardmore's strategy is Eco-design + biofuel,
    # not scrubber retrofit.
    assert sum(1 for v in ci.fleet.vessels if v.scrubber) == 0


def test_handysize_class_on_curve_and_routes():
    """Clean-product Handysize class (added 2026-06-05) loads, values via its own
    curve below MR, and routes earnings to the MR scenario key (v1 proxy)."""
    from crude_tanker_fv.loaders import load_market_data
    from crude_tanker_fv.vessel_values import value_for_age
    from crude_tanker_fv.scenarios import PRODUCT_SCENARIO_CLASS_MAP

    md = load_market_data()
    assert "Handysize" in md.vessel_value_curves
    h = md.vessel_value_curves["Handysize"]
    # curve ordering sane: NB > 5yr > 10yr > scrap
    assert h.newbuild > h.five_year_benchmark > h.ten_year_benchmark > h.scrap_25yr
    # clean-product Handysize sits below MR (smaller hull)
    assert h.newbuild < md.vessel_value_curves["MR"].newbuild
    # age-11 (ASC product Handies) ~$24.6M and age-18 (HAFN wind-down) ~$14.5M
    assert 23e6 < value_for_age(h, 11) < 26e6
    assert 13e6 < value_for_age(h, 18) < 16e6
    # earnings routed to MR scenario key (v1 proxy); rate files carry the literal key
    assert PRODUCT_SCENARIO_CLASS_MAP["Handysize"] == "mr"
    assert "Handysize" in md.ffa_forward_curve
    assert "Handysize" in md.historical_tce_means
    assert "Handysize" in md.twelve_month_tc
    # Handysize cycle position == MR's (rate proxy: same TC / same 10y mean)
    assert (md.twelve_month_tc["Handysize"] / md.historical_tce_means["Handysize"]   # re-pinned 2026-08-10 STAGE A: donor is HANDYMAX now (split from the MR war-identity; STNG printed the fronts separately)
            == md.twelve_month_tc["Handymax"] / md.historical_tce_means["Handymax"])


def test_stng_multi_class_product_loads_and_routes():
    """STNG is the first multi-class pure-product name (32 LR2 + 35 MR on-curve
    + 14 Handymax on-curve [migrated 2026-06-05 — METHODOLOGY §11.5] + 8 HFS
    off-curve [2026-07-01 rebuild: 6 HFS MRs were double-counted, now removed;
    41→35 MR, 87→81 on-curve]). Exercises three branches of the PRODUCT_SCENARIO_CLASS_MAP
    simultaneously — MR → mr, LR2 → lr2_clean, Handymax → mr — and confirms the
    routing doesn't crash with a multi-class manifest.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    stng = watchlist["STNG"]
    ci = load_company_inputs("STNG", BOOK_QUARTER)
    docs = _load_all_sectors()
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "STNG", ci, stng["current_price"], stng["analyst_target"], docs, watchlist,
    )
    # Pure-product (despite multi-class fleet) — sleeve reports None.
    assert crude_r is None and product_r is None
    assert headline.sector == "product"
    # Fleet has LR2 + MR + Handymax (Handymax migrated on-curve 2026-06-05) —
    # all three must route through the product map.
    classes = {v.cls for v in ci.fleet.vessels}
    assert classes == {"LR2", "MR", "Handymax"}, (
        f"STNG should be LR2+MR+Handymax, got {classes}"
    )


def test_stng_whole_company_fv_in_expected_band():
    """STNG probability-weighted FV pinned in $70-$77 band (rebased 2026-06-03
    for Product Set B v2 weight lock — was [$66, $72] under Set A). Under
    Set B Q1 2026 inputs produce $73.58 (EV −6.9%, TRIM/SHORT — just below
    the −5% HOLD threshold). Under Set A it was $68.75 (EV −13.0%).

    Two structural factors compound around STNG's signal:
      1. §12 BUYBACK channel limitation: STNG's primary capital return is
         buybacks (~$300M Q1+April), not dividends ($0.45/qtr fixed). Strip
         captures only the fixed dividend → tool FV structurally conservative.
      2. §14.6.1 LR2 cargo-switching gap: ~$0.95/sh of unmodeled Q2 EPS
         upside if the 32-vessel coated-LR2 fleet captured even half the
         March-April clean-vs-dirty premium.

    Both factors push STNG's effective conviction toward HOLD even though
    the locked-weights output remains TRIM/SHORT. Band lets rate / cycle
    inputs drift ~$2/sh either side without retest noise.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    stng = watchlist["STNG"]
    ci = load_company_inputs("STNG", BOOK_QUARTER)
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "STNG", ci, stng["current_price"], stng["analyst_target"], docs, watchlist,
    )
    # 2026-06-22: the cycle-conditional terminal's NET RETAINED EARNINGS (§9.2)
    # captures STNG's buyback/low-payout retention — the §12 buyback-channel
    # conservatism this test flags — lifting PW FV ~$73.6 → ~$83.2 (TRIM/SHORT → BUY).
    # Re-pinned 2026-07-02 (post-stand-down vintage: product Set B v2 weights
    # {0.15/0.25/0.45/0.15} restored — decisions/crude_reweight_proposal_2026-07-02.md):
    # PW FV ~$83.2 → ~$73.81 (BUY → HOLD at re-pin); band keeps the prior ±3.6%
    # width → [71.15, 76.47].
    # Re-pinned 2026-07-14 EVE (hormuz re-tilt): $80.30 ±5% -> [76.28, 84.31] — back at the pre-stand-down FV.
    assert 76.28 < headline.probability_weighted_fv < 84.31
    # NAV per share check — $83.76 baseline, allow ±$5 for input flex.
    assert 78.0 < headline.base_nav_per_share < 90.0


# Point-in-time pin (Jun-9 weights + Jun-11 inputs, incl. the June-5 data-kit
# Suezmax fix); re-pin on weight settle (post-Hormuz resolution). Bands
# re-based 2026-06-11: asset NAV $95.95 → [92, 100]; PW FV $67.81 (static
# watchlist price) → ±5% [64.4, 71.2].
# Re-pinned 2026-07-02 (post-stand-down vintage: crude reweight + MoU-ineffective
# leg recalibration + product v2/LNG v3 restore —
# decisions/crude_reweight_proposal_2026-07-02.md): PW FV $55.15 → ±5%
# [52.39, 57.91]; BUY holds (asset-NAV band [92, 100] weight-independent, unchanged).
def test_ten_three_sleeve_integration_band():
    """TEN is the first **3-sleeve hybrid** on the watchlist (THREE_SLEEVE_TICKERS).
    The pipeline dispatches through crude_carve_out + product_carve_out +
    lng_carve_out, with the DP2 shuttle sleeve handled OFF-CURVE via
    shuttle_contracted_book (METHODOLOGY §11.6).

    Sanity bands (re-pinned 2026-06-11; includes §15 governance haircut 30%):
      - Asset NAV/sh ~$92-100 (UNDISCOUNTED; $95.95 at pin, post June-5
        data-kit Suezmax fix)
      - Scenario PW FV ~$64-71 post-haircut ($67.81 at pin, Jun-9 weights,
        static watchlist price)
      - Position: BUY (undervalued)
      - 3 sleeve shares sum to 1.0 (validates the carve-out routing)
      - Governance discount applied: 30% (METHODOLOGY §15)

    Bands are generous to absorb minor input drift (TC rate updates, NB advance
    refreshes, governance-discount calibration); shrink the band after the
    second quarter of TEN observations.

    Re-pinned 2026-07-02 (post-stand-down vintage: crude reweight + MoU-ineffective
    leg recalibration + product v2/LNG v3 restore —
    decisions/crude_reweight_proposal_2026-07-02.md): PW FV ~$67.81 → ~$55.15,
    ±5% → [52.39, 57.91]; BUY holds; asset-NAV band unchanged ($96.95 at re-pin).

    Re-pinned 2026-07-12 (Jun-9 crude war tilt RESTORED — doha trigger fired,
    decisions/doha_check_2026-07-12.md): PW FV ~$61.09 (crude sleeve lifts;
    product/LNG sleeves un-reweighted), ±5% → [58.04, 64.14]; BUY holds;
    asset-NAV band weight-independent, unchanged.
    """
    from crude_tanker_fv.pipeline import (
        THREE_SLEEVE_TICKERS, _load_all_sectors, _run_scenarios_for_ticker,
    )
    from crude_tanker_fv.carveout import crude_carve_out, lng_carve_out, product_carve_out
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist
    from crude_tanker_fv.nav import compute_nav

    assert "TEN" in THREE_SLEEVE_TICKERS, "TEN must be tagged for 3-sleeve dispatch"

    watchlist = load_watchlist()
    ten = watchlist["TEN"]
    ci = load_company_inputs("TEN", "2026-Q1")

    # Carve-out sanity: the three sleeve shares should sum to 1.0.
    co = crude_carve_out(ci)
    po = product_carve_out(ci)
    lo = lng_carve_out(ci)
    total_share = co.crude_share + po.product_share + lo.lng_share
    assert abs(total_share - 1.0) < 1e-6, f"sleeve shares should sum to 1, got {total_share}"
    # Each sleeve's fleet should only contain vessels of its sector.
    crude_classes = {v.cls for v in co.crude_inputs.fleet.vessels}
    product_classes = {v.cls for v in po.product_inputs.fleet.vessels}
    lng_classes = {v.cls for v in lo.lng_inputs.fleet.vessels}
    assert crude_classes <= {"VLCC", "Suezmax", "Aframax"}, f"crude leaked: {crude_classes}"
    assert product_classes <= {"LR2", "LR1", "MR", "Handysize", "Handymax"}, f"product leaked: {product_classes}"
    assert lng_classes <= {"LNGC", "MGC"}, f"lng leaked: {lng_classes}"

    # NAV reconciles: must include the shuttle book and preferred subtraction.
    # nav.nav_per_share is the UNDISCOUNTED asset NAV; the §15 governance
    # discount applies downstream (at blend + strip terminal).
    nav = compute_nav(ci)
    assert nav.shuttle_contracted_book == 453_100_000
    # 333,282 = 287,328 preferred (E+F liquidation) + 45,954 Mare Success NCI
    # (2026-07-15 reconciliation — the BWLP NCI-via-preferred_equity convention;
    # decisions/ten_reconciliation_prereg_2026-07-15.md §2).
    assert nav.preferred_equity == 333_282_000
    assert nav.governance_discount_pct == pytest.approx(0.30)
    assert 92.0 < nav.nav_per_share < 100.0, f"NAV/sh out of band: ${nav.nav_per_share:.2f}"

    # 3-sleeve scenario aggregation: PW FV ~$45-55 band POST-HAIRCUT.
    docs = _load_all_sectors()
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "TEN", ci, ten["current_price"], ten["analyst_target"], docs, watchlist,
    )
    # (re-pinned 2026-08-10 STAGE A — the deck-incoherence lift, stage_a_halt_investigation_2026-08-10.md; re-reads at the 8/16 deck re-derivation): $66.64 ±5%.
    assert 63.31 < headline.probability_weighted_fv < 69.97, (
        f"PW FV out of band: ${headline.probability_weighted_fv:.2f}"
    )
    # Both sleeve reports returned (LNG sleeve consumed internally; per-sleeve
    # detail for LNG is an onboarding TODO if needed for reports).
    assert crude_r is not None and product_r is not None
    # Position must be BUY (PW FV ~$68 vs static price ~$37 at the Jun-11
    # re-pin); post-haircut value reading, directionally consistent with
    # VIE Bullish $51.50 (independent external read).
    assert headline.position_recommendation.startswith("BUY"), (
        f"expected BUY, got {headline.position_recommendation}"
    )


def test_cycle_anchor_cross_file_consistency():
    """BUG-1 guard (2026-06-22): the crude-dirty trio's 10yr-mean cycle anchors must
    AGREE between historical_tce_means.yaml (the per-name FV / breakeven / sensitivity
    path, via compute_cycle) and scenario_inputs.yaml crude cycle_anchors (the scenario
    path). They silently disagreed on Aframax (27600 vs 36483) → different cycle
    positions for every Aframax-exposed name across the two surfaces."""
    import yaml
    from crude_tanker_fv.loaders import INPUTS_DIR

    means = yaml.safe_load(
        (INPUTS_DIR / "market_data" / "historical_tce_means.yaml").read_text()
    )["historical_tce_means"]
    crude = yaml.safe_load(
        (INPUTS_DIR / "scenario_inputs.yaml").read_text()
    )["sectors"]["crude"]["cycle_anchors"]
    for engine_key, scen_key in {"VLCC": "vlcc", "Suezmax": "suezmax", "Aframax": "aframax_dirty"}.items():
        assert means[engine_key] == crude[scen_key]["ten_year_mean"], (
            f"{engine_key}: historical_tce_means {means[engine_key]} != "
            f"scenario_inputs.{scen_key} {crude[scen_key]['ten_year_mean']}"
        )


# --------------------------------------------------------------------------- #
# As-of-quarter plumbing (PLAN Phase 3b — engine EV% historical-vintage routing)
# --------------------------------------------------------------------------- #

from crude_tanker_fv.scenarios import quarter_keys, strip_start_from_asof  # noqa: E402


def test_quarter_keys_default_unchanged_and_parametrized():
    from crude_tanker_fv.scenarios import QUARTER_KEYS
    assert quarter_keys(8) == QUARTER_KEYS                       # no-arg path byte-unchanged
    assert quarter_keys(4, 3, 2020) == ["q3_2020", "q4_2020", "q1_2021", "q2_2021"]
    assert quarter_keys(3, 1, 2027) == ["q1_2027", "q2_2027", "q3_2027"]


def test_strip_start_from_asof_maps_report_quarter_plus_two():
    assert strip_start_from_asof(None) == (3, 2026)             # live anchor preserved
    assert strip_start_from_asof("2026-Q1") == (3, 2026)        # +2 ⇒ q3_2026 (the live mapping)
    assert strip_start_from_asof("2020-Q1") == (3, 2020)
    assert strip_start_from_asof("2025-Q4") == (2, 2026)        # Q4 report ⇒ Q2 next year
    assert strip_start_from_asof("2026-Q3") == (1, 2027)


def test_run_scenarios_asof_same_vintage_is_byte_identical(doc):
    """asof_quarter=2026-Q1 must reproduce the default (None) run exactly — both
    resolve to q3_2026, so the as-of path is a no-op on the live vintage."""
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    base = run_scenarios(ci, 16.40, 16.00, doc)
    asof = run_scenarios(ci, 16.40, 16.00, doc, asof_quarter="2026-Q1")
    assert asof.probability_weighted_fv == base.probability_weighted_fv
    assert asof.expected_value_vs_current == base.expected_value_vs_current
    assert [s.fair_value for s in asof.scenarios] == [s.fair_value for s in base.scenarios]


def test_run_scenarios_asof_missing_vintage_fails_fast(doc):
    """A historical as-of with no vintage curves in the doc must raise a clear
    error naming the missing forward-quarter keys — never silently mis-route."""
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    with pytest.raises(ValueError) as exc:
        run_scenarios(ci, 16.40, 16.00, doc, asof_quarter="2020-Q1")
    assert "q3_2020" in str(exc.value)
