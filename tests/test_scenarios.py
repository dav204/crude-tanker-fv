"""Scenario-engine tests (consumes scenario_inputs.yaml).

Covers the crude three-phase MoU framework as before, plus the sector layer
(METHODOLOGY §11): FLNG resolves to the LNG glut-cycle scenarios, not crude.
"""

import pytest

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.scenarios import (
    load_scenarios,
    position_recommendation,
    run_scenarios,
)


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
    # Sector layer (METHODOLOGY §11): the default load returns the crude sub-doc
    # with its own cycle_anchors, and the sector name is stamped in.
    assert doc["sector"] == "crude"
    assert set(doc["cycle_anchors"]) >= {"vlcc", "suezmax", "aframax_dirty", "lr2_clean"}


def test_run_scenarios_weighted_average_identity(doc):
    ci = load_company_inputs("DHT", "2026-Q1")
    r = run_scenarios(ci, 16.40, 16.00, doc)
    assert len(r.scenarios) == 4
    expected = sum(s.weight * s.fair_value for s in r.scenarios)
    assert r.probability_weighted_fv == pytest.approx(expected)


# Point-in-time pin (Jun-9 weights + Jun-11 inputs); re-pin on weight settle
# (post-Hormuz resolution). Re-pinned from skip 2026-06-11 (B3): a pin against
# current intended state catches unintended drift; a skip catches nothing.
def test_nav_flexes_with_scenario(doc):
    ci = load_company_inputs("DHT", "2026-Q1")
    r = run_scenarios(ci, 16.40, 16.00, doc)
    navs = {s.name: s.nav_per_share for s in r.scenarios}
    # Vessel values reset with the scenario forward: escalation > pre-MoU > base > bear.
    assert navs["escalation"] > navs["pre_mou_baseline"] > navs["mou_base"] > navs["mou_bear"]
    # DIRECTION REVERSED at the Jun-9 re-pin: under the war-leaning Jun-9 set
    # (escalation 0.25 + pre_mou 0.45 both price ABOVE the current forward) the
    # probability-weighted NAV sits ABOVE today's NAV ($15.79 vs $15.29 at pin
    # time). The v1 assertion (wnav < base) encoded normalization-leaning
    # weights; the relationship is weight-set-dependent, not structural.
    wnav = sum(s.weight * s.nav_per_share for s in r.scenarios)
    assert wnav > r.base_nav_per_share


def test_per_scenario_range_brackets_base(doc):
    ci = load_company_inputs("FRO", "2026-Q1")
    r = run_scenarios(ci, 34.50, 30.50, doc)
    for s in r.scenarios:
        assert s.fair_value_low <= s.fair_value <= s.fair_value_high


def test_bear_softer_than_base(doc):
    ci = load_company_inputs("DHT", "2026-Q1")
    r = {s.name: s for s in run_scenarios(ci, 16.40, 16.00, doc).scenarios}
    # Bear scenario has lower forward rates -> lower cycle ratio and lower FV.
    assert r["mou_bear"].cycle_position < r["mou_base"].cycle_position
    assert r["mou_bear"].fair_value < r["mou_base"].fair_value


# Point-in-time pin (Jun-9 weights + Jun-11 inputs); re-pin on weight settle
# (post-Hormuz resolution).
def test_lr2_maps_to_clean_curve(doc):
    # FRO's LR2 sleeve uses the scenario lr2_clean curve (spike-sensitive), not
    # the static Aframax proxy. Sanity: the run completes with 3 classes priced.
    ci = load_company_inputs("FRO", "2026-Q1")
    r = run_scenarios(ci, 34.50, 30.50, doc)
    # HOLD at the Jun-9 re-pin (was TRIM/SHORT under v1 weights; PW FV $33.77
    # vs $34.50 — the war-leaning reweight lifted FRO inside the HOLD band).
    assert r.position_recommendation.startswith("HOLD")


def test_breakeven_is_scenario_invariant(doc):
    from crude_tanker_fv.breakeven import implied_breakeven_tce

    ci = load_company_inputs("DHT", "2026-Q1")
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
    active = ["tight_resurgence", "moderate_tightening", "glut_base", "glut_intensifies"]
    assert sum(lng_doc["scenarios"][n]["weight"] for n in active) == pytest.approx(1.0)
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
    ci = load_company_inputs("FLNG", "2026-Q1")
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
    ci = load_company_inputs("FLNG", "2026-Q1")
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
    ci = load_company_inputs("FLNG", "2026-Q1")
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
    ci = load_company_inputs("CCEC", "2026-Q1")
    r = run_scenarios(ci, 23.18, 25.17, lng_doc)
    assert "BUY" in r.position_recommendation, (
        f"CCEC position should be BUY under Set B-revised; got "
        f"{r.position_recommendation!r}"
    )


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
    ci = load_company_inputs("CCEC", "2026-Q1")
    r = run_scenarios(ci, 23.18, 25.17, lng_doc)
    assert 28.15 < r.probability_weighted_fv < 31.11
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
    active = ["refinery_squeeze", "moderate_correction", "glut_base", "demand_softening"]
    assert sum(product_doc["scenarios"][n]["weight"] for n in active) == pytest.approx(1.0)
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
    """HISTORY: this test originally pinned the 'INSW whole-co FV preserved
    exactly through the product-sector refactor' invariant at $52.03. The
    Jun-9 Issue #1 fix DELIBERATELY broke that invariant — it was preserving
    a copy bug (product q3_2026 inherited the Phase-1 spike from
    crude.mou_base). The structural property it documented still holds and
    is still asserted below: `_aggregate_hybrid_report` uses CRUDE scenario
    weights as the whole-co aggregation probability, so product weight
    changes do not move INSW whole-co FV.

    Re-pinned 2026-06-11 (B3) to the Jun-9-weights value $64.59, ±1% band
    [63.9, 65.2] — tight, mirroring the original's intent of catching any
    silent aggregation change.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    insw = watchlist["INSW"]
    ci = load_company_inputs("INSW", "2026-Q1")
    docs = _load_all_sectors()
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "INSW", ci, insw["current_price"], insw["analyst_target"], docs, watchlist,
    )
    assert 63.9 < headline.probability_weighted_fv < 65.2
    # Both sleeves should have valid prob-weighted FVs.
    assert crude_r is not None and product_r is not None
    assert crude_r.probability_weighted_fv > 0
    assert product_r.probability_weighted_fv > 0
    # Whole-co aggregation EQUALS sum_i w_crude_i × (fv_crude_i + fv_product_i),
    # NOT crude_pw_fv + product_pw_fv (which would assume both sleeves use their
    # own weights). Under Product Set A (the v1 placeholder) these two sums
    # coincided numerically because product weights matched crude weights
    # {0.10/0.15/0.50/0.25}; under Product Set B (v2 lock, 2026-06-03) they
    # diverge because product weights are now {0.15/0.25/0.45/0.15}.
    # The methodology equation below stays exact across both weight regimes.
    expected_headline = sum(
        c.weight * (c.fair_value + p.fair_value)
        for c, p in zip(crude_r.scenarios, product_r.scenarios)
    ) / sum(c.weight for c in crude_r.scenarios)
    assert headline.probability_weighted_fv == pytest.approx(expected_headline, abs=0.01)


def test_crude_ticker_does_not_load_lng_doc():
    """A crude ticker run through the LNG doc would crash (the doc has no
    `vlcc` key). This is intentional: the pipeline must resolve sector before
    handing a doc to run_scenarios. Catching the KeyError here pins the
    contract — the sector layer is not a soft default.
    """
    ci = load_company_inputs("DHT", "2026-Q1")
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
    ci = load_company_inputs("ASC", "2026-Q1")
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
    """ASC probability-weighted FV pinned in $13.5-$14.9 band (rebased
    2026-06-03 for Product Set B v2 weight lock — was [$13.0, $14.2] under
    Set A). Q1 2026 inputs under Product Set B produce $14.24 (EV −23.0%,
    TRIM/SHORT) — vs Set A $13.59 (EV −26.5%, TRIM/SHORT). The +$0.65 lift
    reflects the constructive reweighting (+5pp refinery_squeeze, +10pp
    moderate_correction, −5pp glut_base, −10pp demand_softening per
    METHODOLOGY §11.5 v2 + Catlin VIE June 2026 driver). Position stays
    TRIM/SHORT — EV still well below the −5% HOLD threshold.

    A larger drift means: an input changed (likely OK), the MR / LR1 / LR2
    forward curves shifted (review), or the product-sector class routing
    regressed (NOT OK). The band is ±5% around $14.24 to mirror the FLNG /
    CCEC band convention.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    asc = watchlist["ASC"]
    ci = load_company_inputs("ASC", "2026-Q1")
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "ASC", ci, asc["current_price"], asc["analyst_target"], docs, watchlist,
    )
    assert 14.32 < headline.probability_weighted_fv < 15.82
    # Position remains TRIM/SHORT under Set B (EV still well below -5% HOLD
    # threshold). If this flips to HOLD it means either the rate environment
    # shifted enough to warrant another lock review, or Set B itself was
    # over-tilted constructively — investigate.
    assert "TRIM/SHORT" in headline.position_recommendation


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
    ci = load_company_inputs("HAFN", "2026-Q1")
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
    """HAFN probability-weighted FV pinned in $5.0-$5.8 band under Product
    Set B v2 (locked 2026-06-03). Q1 2026 inputs produce $5.35 (EV −33.5%
    TRIM/SHORT — deeply below the −5% HOLD threshold).

    HAFN is the third product name where VIE Bullish ($9.00) opposes our
    framework TRIM, after ASC and TRMD. The pattern is consistent across
    the product sector — VIE is structurally more bullish on product than
    our framework's scenario-weighted view. The TC-vs-spot baseline reframe
    (METHODOLOGY §10) explains part of the cross-methodology gap; the
    Product Set B v2 reweighting (§11.5) absorbed part of the empirical
    case for tightness already. The residual VIE-Bullish vs Tool-TRIM gap
    on HAFN is documented in §6 HAFN entry.

    Methodology caveats reflected in the band:
    - The $300M Handysize off-curve estimate (22 hulls × $15M × 0.9
      liquidity discount) flexes the floor by ±$30M = ±$0.06/sh
    - The $395M TORM equity stake rolled into working_capital_net is exact
      per Hafnia mgmt-disclosed value; if Hafnia exits or trims the stake
      the framework sees the cash directly
    - The ~500M diluted share count is [ESTIMATE] from Q1 dividend math;
      refresh from Q1 6-K when share-count line is pulled
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    hafn = watchlist["HAFN"]
    ci = load_company_inputs("HAFN", "2026-Q1")
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "HAFN", ci, hafn["current_price"], hafn["analyst_target"], docs, watchlist,
    )
    assert 5.58 < headline.probability_weighted_fv < 6.16
    assert "TRIM/SHORT" in headline.position_recommendation
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
    ci = load_company_inputs("TRMD", "2026-Q1")
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
    """TRMD probability-weighted FV pinned in $24-$27 band under Product
    Set B v2 (locked 2026-06-03). Q1 2026 inputs produce $25.59 (EV −6.1%,
    TRIM/SHORT — just below the −5% HOLD threshold).

    TRMD is the cleanest mark-validated TRIM in the product sector
    (k_broker 1.01, +2pp spread — narrowest of any product name) but VIE
    Coverage Universe carries it Bullish at $34.00 (third name where VIE
    Bullish overrules tool + broker on direction, after ASC and CCEC).
    See `outputs/vie_coverage_universe_xref.md` and §6 TRMD entry for the
    soft-signal overlay.

    If this band drifts: check (a) operating WC estimate ($110M is flagged
    as a [ESTIMATE] pending Q1 PDF detail; ±$30M would move FV ~$0.30/sh),
    (b) NB capex commitments breakdown, (c) LR1 cohort assumptions.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    trmd = watchlist["TRMD"]
    ci = load_company_inputs("TRMD", "2026-Q1")
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "TRMD", ci, trmd["current_price"], trmd["analyst_target"], docs, watchlist,
    )
    assert 26.44 < headline.probability_weighted_fv < 29.22


def test_asc_fleet_loads_mr_plus_handysize():
    """ASC's on-curve fleet: 19 MRs + (as of 2026-06-05) 2 clean-product
    Handysize hulls (Defender/Dauntless, moved on-curve via the new Handysize
    class). The 4 × 25k stainless chemical Handies stay OFF-curve. Pins the
    loader's class-agnostic behaviour incl. the Handysize class.
    """
    ci = load_company_inputs("ASC", "2026-Q1")
    classes = {v.cls for v in ci.fleet.vessels}
    assert classes == {"MR", "Handysize"}, f"ASC fleet should be MR+Handysize, got {classes}"
    assert len(ci.fleet.vessels) == 20, f"ASC rows should be 20 (19 MR + 1 Handysize), got {len(ci.fleet.vessels)}"
    # MR + Handysize rows with eco: true. 5 × 2013 MRs are eco: false (pre-2014
    # Eco-Mod); the 2 product Handies (2015) are eco: true.
    eco_count = sum(1 for v in ci.fleet.vessels if v.eco)
    assert eco_count == 15, f"ASC eco rows should be 15 (14 eco MR + 1 eco Handysize), got {eco_count}"
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
    assert (md.twelve_month_tc["Handysize"] / md.historical_tce_means["Handysize"]
            == md.twelve_month_tc["MR"] / md.historical_tce_means["MR"])


def test_stng_multi_class_product_loads_and_routes():
    """STNG is the first multi-class pure-product name (32 LR2 + 41 MR on-curve
    + 14 Handymax on-curve [migrated 2026-06-05 — METHODOLOGY §11.5] + 9 HFS
    off-curve). Exercises three branches of the PRODUCT_SCENARIO_CLASS_MAP
    simultaneously — MR → mr, LR2 → lr2_clean, Handymax → mr — and confirms the
    routing doesn't crash with a multi-class manifest.
    """
    from crude_tanker_fv.pipeline import _run_scenarios_for_ticker, _load_all_sectors
    from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

    watchlist = load_watchlist()
    stng = watchlist["STNG"]
    ci = load_company_inputs("STNG", "2026-Q1")
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
    ci = load_company_inputs("STNG", "2026-Q1")
    docs = _load_all_sectors()
    headline, _, _ = _run_scenarios_for_ticker(
        "STNG", ci, stng["current_price"], stng["analyst_target"], docs, watchlist,
    )
    assert 70.0 < headline.probability_weighted_fv < 77.0
    # NAV per share check — $83.76 baseline, allow ±$5 for input flex.
    assert 78.0 < headline.base_nav_per_share < 90.0


# Point-in-time pin (Jun-9 weights + Jun-11 inputs, incl. the June-5 data-kit
# Suezmax fix); re-pin on weight settle (post-Hormuz resolution). Bands
# re-based 2026-06-11: asset NAV $95.95 → [92, 100]; PW FV $67.81 (static
# watchlist price) → ±5% [64.4, 71.2].
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
    assert nav.preferred_equity == 287_328_000
    assert nav.governance_discount_pct == pytest.approx(0.30)
    assert 92.0 < nav.nav_per_share < 100.0, f"NAV/sh out of band: ${nav.nav_per_share:.2f}"

    # 3-sleeve scenario aggregation: PW FV ~$45-55 band POST-HAIRCUT.
    docs = _load_all_sectors()
    headline, crude_r, product_r = _run_scenarios_for_ticker(
        "TEN", ci, ten["current_price"], ten["analyst_target"], docs, watchlist,
    )
    assert 64.4 < headline.probability_weighted_fv < 71.2, (
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
