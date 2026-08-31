"""Tier semantics amendment 2026-08-13 — read-corroboration out of the tier.

decisions/tier_semantics_amendment_2026-08-13.md (+ Addendum A). The tier certifies how the NAV is
BUILT; whether the §17 read AGREES across bases is an EDGE fact that caps size on its own channel.

The load-bearing guard here is `test_tier_is_price_invariant`: the regression it names is
SBLK-2026-08-13, where a 62 bp red open would have UPGRADED a tier hours after a data repair
degraded it, with NAV byte-identical through both. It is ALSO the standing guard on future §17
blockers — `read_blocked` IS a tier input, so any price-dependent guard later added to
`justified_pnav.evaluate` moves a tier under the perturbation and reds the suite (Addendum A §5).
"""

import json
from pathlib import Path

import pytest

from conftest import BOOK_QUARTER
import crude_tanker_fv.justified_pnav as jp
import crude_tanker_fv.scorecard as sc
from crude_tanker_fv.justified_pnav import (
    READ_FLAG_HYST_PCT,
    cheap_fair_boundary,
    fair_rich_boundary,
    flip_margin_pct,
    govern_read_flag,
    load_read_flag_state,
    save_read_flag_state,
)
from crude_tanker_fv.provenance import (
    POSITION_UNRELIABLE,
    TIER_SUBREASON,
    confidence_tier,
    tier_subreason,
)

# SBLK at the 2026-08-13 rebase — the worked example the amendment is pinned to (§2).
SBLK_NAV = 32.785
SBLK_J_PAR = 1.11602
SBLK_J_HIST = 0.930
SBLK_BOUNDARY = 27.72      # NAV x J_hist / (1 + FAIR_BAND)
SBLK_TAPE_CLOSE = 27.89    # the 8/13 live close
SBLK_MARGIN_PCT = 0.62     # +0.62% — inside the deadband, the strobe zone that motivated it
SBLK_VINTAGE_PRICE = 28.60  # the watchlist static the row's own §17 numbers price off
SBLK_ROW_MARGIN_PCT = 3.18   # +3.18% — the SAME boundary measured at the vintage; OUTSIDE the band. SYNTHETIC 8/13-era fixture value, paired with SBLK_VINTAGE_PRICE above — does NOT track the live watchlist (the live-surface test carries its own dated literal)


def _scale_prices(monkeypatch, factor: float) -> None:
    """Perturb PRICE only. Every other input — fleet, sheets, marks, scenarios — is untouched,
    so any tier that moves under this moved on price and nothing else."""
    real = jp.load_watchlist

    def _patched(inputs_dir=jp.INPUTS_DIR, live_prices=False):
        wl = real(inputs_dir, live_prices)
        for entry in wl.values():
            entry["current_price"] *= factor
            entry["as_of_price"] *= factor
        return wl

    monkeypatch.setattr(jp, "load_watchlist", _patched)
    monkeypatch.setattr(sc, "load_watchlist", _patched)


def _surface(monkeypatch, factor: float) -> dict:
    _scale_prices(monkeypatch, factor)
    rows = sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})
    return {r.ticker: {"tier": r.confidence_tier, "blocked": r.read_blocked,
                       "robust": r.robust, "read_hist": r.read_hist} for r in rows}


def test_tier_is_price_invariant(monkeypatch):
    """REGRESSION SBLK-2026-08-13. Tiers under a price-only +/-20% perturbation must be
    byte-identical to the unperturbed run, for every name."""
    base = _surface(monkeypatch, 1.0)
    for factor in (0.80, 1.20):
        moved = _surface(monkeypatch, factor)
        assert set(moved) == set(base)
        for ticker in base:
            assert moved[ticker]["tier"] == base[ticker]["tier"], (
                f"{ticker}: tier moved {base[ticker]['tier']} -> {moved[ticker]['tier']} on a "
                f"PRICE-ONLY {factor:g}x perturbation. A price movement may never change a tier.")
            # read_blocked is the tier's only §17 input, so it carries the same invariant. A
            # price-dependent guard added to evaluate() lands here first, naming itself.
            assert moved[ticker]["blocked"] == base[ticker]["blocked"], (
                f"{ticker}: §17 blocker moved {base[ticker]['blocked']!r} -> "
                f"{moved[ticker]['blocked']!r} on price alone — §17 blockers must be "
                f"price-independent or rule 2 leaks price back into the tier.")


def test_price_perturbation_actually_moves_the_reads(monkeypatch):
    """The invariance test above is only worth something if the perturbation BITES. +/-20% must
    move the read/robust surface it leaves the tier out of — else the guard passes vacuously."""
    base = _surface(monkeypatch, 1.0)
    moved = _surface(monkeypatch, 1.20)
    assert any(moved[t]["read_hist"] != base[t]["read_hist"] or moved[t]["robust"] != base[t]["robust"]
               for t in base), "a +20% price move changed no read — the perturbation is not live"


def test_confidence_tier_takes_no_read_agreement_argument():
    """The signature itself is the guard: agreement can't reach the tier if it can't be passed."""
    with pytest.raises(TypeError):
        confidence_tier("SBLK", "resale-uniform", "flips (cheap/fair)")


def test_read_flips_never_reenters_tier_subreason():
    """A flipping read no longer widens a tier, so it can never be a tier sub-reason (§5 guard).
    Read state is computed live from §17 every run — registering it is what let a price move
    write itself into the tier record in the first place."""
    assert "read-flips" not in set(TIER_SUBREASON.values())
    for ticker in ("SBLK", "CMDB", "GNK"):
        assert TIER_SUBREASON.get(ticker) is None, f"{ticker} re-registered a tier sub-reason"


def test_flipping_names_are_construction_validated():
    """§7 acceptance: the three read-flips names carry no construction defect, so they are TIGHT —
    and their flip survives on the read channel, where it belongs."""
    rows = {r.ticker: r for r in sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})}
    for ticker in ("SBLK", "CMDB", "GNK"):
        assert rows[ticker].confidence_tier == "VALIDATED-TIGHT", ticker
        assert rows[ticker].robust.startswith("flips"), ticker
        assert rows[ticker].read_flag.startswith("flips"), ticker


def test_read_blocked_names_hold_governed_wide():
    """Addendum A: evaluability is a CONSTRUCTION fact and stays in the tier. BRUT and CAPT have
    no producible §17 multiple, so dropping read AGREEMENT must not promote them."""
    rows = {r.ticker: r for r in sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})}
    for ticker in ("BRUT", "CAPT"):
        assert rows[ticker].read_blocked is not None, ticker
        assert rows[ticker].confidence_tier == "GOVERNED-WIDE", ticker
        assert rows[ticker].read_flag == "n/a", ticker
    # the blocker explains itself in the tier cell; BRUT's registered owner-ruled ground wins
    assert tier_subreason("CAPT", rows["CAPT"].read_blocked) == "newbuild-heavy"
    assert tier_subreason("BRUT", rows["BRUT"].read_blocked) == "going-concern-unfinanced"


def test_edge_cleared_long_set_is_unchanged_by_the_amendment():
    """§7 + Addendum B1: TIGHT ∧ read_flag == "robust" ∧ read_par == "cheap" ∧ BUY. The amendment
    RELOCATES the constraint; it must not enlarge position authorization. Gates on the GOVERNED
    flag, so a now-TIGHT flipping name cannot enter."""
    rows = sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})
    edge_cleared = sorted(r.ticker for r in rows
                          if r.confidence_tier == "VALIDATED-TIGHT"
                          and r.read_flag == "robust" and r.read_par == "cheap")
    assert edge_cleared == ["SB"]


def test_edge_cleared_uses_the_directional_read_not_agreement():
    """Addendum B1's reason for pinning the PARITY read: agreement is symmetric, actionability is
    directional. TNK is robust and raw-BUY but reads rich/rich — §4's literal "TIGHT ∧ robust ∧
    BUY" would have admitted it and enlarged the actionable surface against §7."""
    rows = {r.ticker: r for r in sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})}
    tnk = rows["TNK"]
    assert tnk.confidence_tier == "VALIDATED-TIGHT" and tnk.read_flag == "robust"
    assert tnk.read_par == "rich" and tnk.read_hist == "rich"
    assert "TNK" in POSITION_UNRELIABLE     # B1's docketed second guard, not yet a conjunct


def test_governed_flag_can_outlive_agreement_so_the_basis_choice_is_material():
    """Why B1 names a specific basis at all, rather than leaving it to whichever reads "cheap".

    `read_flag` is GOVERNED: inside the deadband it HOLDS "robust" while the instantaneous reads
    have already diverged. In that window read_par and read_hist genuinely disagree, so the two
    candidate conjuncts give OPPOSITE answers — the filter must say which basis it means. Built
    from SBLK's real J's at its real price, since no live row currently sits in that window."""
    # the deadband holds the prior flag even though the reads have separated
    held = govern_read_flag("flips (cheap/fair)", READ_FLAG_HYST_PCT / 2, "robust")
    assert held == "robust", "precondition: a sub-deadband move must not move the flag"

    pnav = 28.60 / SBLK_NAV
    read_par = jp._read_from(SBLK_J_PAR, pnav, None)
    read_hist = jp._read_from(SBLK_J_HIST, pnav, None)
    assert read_par == "cheap" and read_hist == "fair", (read_par, read_hist)

    # B1's conjunct admits this row; the read_hist form would have rejected it. Opposite answers
    # from the same state is exactly what makes the ruling load-bearing rather than cosmetic.
    assert (read_par == "cheap") is not (read_hist == "cheap")


# --- §2 boundary prices + flip margin -----------------------------------------------------------
def test_sblk_boundary_and_margin_fixture():
    """The worked example pinned by §2: NAV 32.785, J_hist 0.930 -> $27.72; close $27.89 -> +0.62%.

    Computed from the TAPE close, which is not the watchlist-vintage price the live row prices off
    — the fixture pins the arithmetic, not the row."""
    assert cheap_fair_boundary(SBLK_NAV, SBLK_J_HIST) == pytest.approx(SBLK_BOUNDARY, abs=0.005)
    margin = flip_margin_pct(SBLK_NAV, SBLK_J_PAR, SBLK_J_HIST, SBLK_TAPE_CLOSE)
    assert margin == pytest.approx(SBLK_MARGIN_PCT, abs=0.005)
    assert abs(margin) < READ_FLAG_HYST_PCT, "the fixture is the strobe zone — it must sit inside"


def test_boundaries_invert_the_band_form():
    """The boundary must be the exact price at which the read changes: just inside reads cheap,
    just outside reads fair. Pins the (1 +/- FAIR_BAND) direction against a sign slip."""
    nav, j = 32.785, 0.930
    lo = cheap_fair_boundary(nav, j)
    hi = fair_rich_boundary(nav, j)
    assert lo < nav * j < hi
    assert jp._read_from(j, (lo * 0.999) / nav, None) == "cheap"
    assert jp._read_from(j, (lo * 1.001) / nav, None) == "fair"
    assert jp._read_from(j, (hi * 0.999) / nav, None) == "fair"
    assert jp._read_from(j, (hi * 1.001) / nav, None) == "rich"


def test_flip_margin_measures_a_real_state_change():
    """Only a boundary whose crossing actually changes `robust` may be measured. Stepping the
    margin to zero and through must flip the state; a cosmetic band edge must not be selected."""
    margin = flip_margin_pct(SBLK_NAV, SBLK_J_PAR, SBLK_J_HIST, SBLK_TAPE_CLOSE)
    boundary = SBLK_TAPE_CLOSE / (1 + margin / 100.0)
    before = jp._robust_at_price(SBLK_NAV, SBLK_J_PAR, SBLK_J_HIST, boundary * 0.999)
    after = jp._robust_at_price(SBLK_NAV, SBLK_J_PAR, SBLK_J_HIST, boundary * 1.001)
    assert before != after
    assert before == "robust" and after.startswith("flips")


def test_blocked_name_has_no_margin():
    """No multiple, no boundary, no margin — the row prints the blocker, not a number."""
    assert flip_margin_pct(10.0, None, None, 5.0) is None


# --- §3 hysteresis ------------------------------------------------------------------------------
def test_hysteresis_holds_inside_the_deadband_and_adopts_beyond_it():
    """A margin path crossing the boundary WITHIN +/-HYST must not move read_flag; beyond it must."""
    inside = READ_FLAG_HYST_PCT / 2
    outside = READ_FLAG_HYST_PCT * 1.5
    # walk in from robust territory, crossing the boundary but staying inside the band
    flag = "robust"
    for margin in (-inside, -0.1, 0.1, inside):
        flag = govern_read_flag("flips (cheap/fair)", margin, flag)
        assert flag == "robust", f"read_flag strobed at margin {margin:+.2f}%"
    # clear the band and it adopts
    assert govern_read_flag("flips (cheap/fair)", outside, flag) == "flips (cheap/fair)"
    # and symmetrically on the way back
    held = govern_read_flag("robust", inside, "flips (cheap/fair)")
    assert held == "flips (cheap/fair)"
    assert govern_read_flag("robust", outside, "flips (cheap/fair)") == "robust"


def test_hysteresis_boundary_is_inclusive():
    """`|margin| >= HYST` adopts — exactly at the deadband edge the transition is taken."""
    assert govern_read_flag("flips (cheap/fair)", READ_FLAG_HYST_PCT, "robust") == "flips (cheap/fair)"


def test_hysteresis_bootstraps_and_never_holds_a_blocked_state():
    """state/ is machine-local, so a fresh clone has no prior and must adopt the instantaneous
    read. A blocked name reports n/a regardless of what it used to be."""
    assert govern_read_flag("flips (cheap/fair)", 0.1, None) == "flips (cheap/fair)"
    assert govern_read_flag("n/a", None, "robust") == "n/a"
    # no boundary explains the change => the J's moved (an estimate change), so adopt, don't hold
    assert govern_read_flag("robust", None, "flips (cheap/fair)") == "robust"


def test_read_flag_state_roundtrip_drops_blocked_names(tmp_path: Path):
    """Addendum A §2: no governed state is persisted for a §17-blocked name."""
    path = tmp_path / "read_flag_state.json"
    save_read_flag_state({"SB": "robust", "SBLK": "flips (cheap/fair)", "BRUT": "n/a"}, path=path)
    loaded = load_read_flag_state(path)
    assert loaded == {"SB": "robust", "SBLK": "flips (cheap/fair)"}
    assert json.loads(path.read_text())["hyst_pct"] == READ_FLAG_HYST_PCT
    assert load_read_flag_state(tmp_path / "absent.json") == {}


def test_write_scorecard_does_not_write_machine_state(tmp_path: Path):
    """A test run must never write governed state into the shared tree (2026-07-18 rule). The
    tests drive write_scorecard directly, some with synthetic rows, so persistence lives in the
    production entry (run_scorecard_xref) — not in the writer."""
    before = sc.READ_FLAG_STATE_FILE.read_bytes() if sc.READ_FLAG_STATE_FILE.exists() else None
    rows = sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})
    sc.write_scorecard(rows, outputs_dir=tmp_path)
    after = sc.READ_FLAG_STATE_FILE.read_bytes() if sc.READ_FLAG_STATE_FILE.exists() else None
    assert after == before, "write_scorecard mutated the machine-local read-flag state"


def test_prior_state_cannot_reach_the_tier(tmp_path: Path):
    """The governed flag is stateful BY DESIGN; the tier must not be. A hostile prior state must
    leave every tier untouched — otherwise run order could restate a sizing input."""
    clean = {r.ticker: r.confidence_tier for r in sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})}
    hostile = {t: "flips (cheap/fair)" for t in clean}
    seeded = {r.ticker: r.confidence_tier
              for r in sc.compute_scorecard(BOOK_QUARTER, read_flag_state=hostile)}
    assert seeded == clean


# --- Addendum B2 — the tape-basis strobe, DELTA layer only ---------------------------------------
# B2 ruled the scorecard is a SINGLE-VINTAGE surface and gets no tape column; the forward-looking
# view ships on the monitor layer instead. These guards hold both halves of that: the number exists
# where it was routed, and the surface it was kept OFF of did not move.

def _sblk_jrow(price: float = SBLK_VINTAGE_PRICE) -> jp.JustifiedPnavRow:
    """The 8/13 SBLK row from the pinned scalars. Only NAV, the two J's and the price drive any
    §17 boundary or margin — the rest of the row is carried for shape."""
    pnav = price / SBLK_NAV
    return jp.JustifiedPnavRow(
        ticker="SBLK", hybrid=False, sector="dry_bulk", nav_per_share=SBLK_NAV, price=price,
        pnav_mkt=pnav, ronav_implied=None, r=jp.COST_OF_EQUITY, g=0.0,
        ronav_norm=None, justified_pnav=SBLK_J_PAR, justified_fv=None, gap=None, flag=None,
        ronav_norm_hist=None, justified_pnav_hist=SBLK_J_HIST, gap_hist=None, flag_hist=None,
    )


def test_sblk_tape_strobe_pins_the_reference_case():
    """REFERENCE SBLK-2026-08-13. NAV 32.785, J_hist 0.930 -> boundary $27.72; tape close $27.89
    -> +0.62%, INSIDE the ±2.0% deadband. This is the row the ruling cites as the strobe zone and
    that, before this work, reached no surface at all."""
    from crude_tanker_fv.delta import read_flip_strobes

    strobes = read_flip_strobes([_sblk_jrow()], {"SBLK": "flips (cheap/fair)"},
                                {"SBLK": SBLK_TAPE_CLOSE})
    assert len(strobes) == 1
    s = strobes[0]
    assert s.tape_price == SBLK_TAPE_CLOSE
    assert s.boundary_price == pytest.approx(SBLK_BOUNDARY, abs=0.005)
    assert s.tape_margin_pct == pytest.approx(SBLK_MARGIN_PCT, abs=0.005)
    assert s.in_deadband is True, "the reference case IS the deadband case — it must flag"
    # the settling edge names itself: hist is the basis that would come into agreement
    assert "hist" in s.boundary_edge


def test_strobe_does_not_restate_the_rows_own_vintage_margin():
    """The two margins measure the SAME boundary at DIFFERENT prices and must coexist untouched:
    +3.18% governs (it is the price the read is computed on), +0.62% warns. Conflating them is
    exactly the k-vintage mismatch B2 refused to re-create."""
    from crude_tanker_fv.delta import read_flip_strobes

    row = _sblk_jrow()
    assert row.flip_margin_pct == pytest.approx(SBLK_ROW_MARGIN_PCT, abs=0.005)
    assert abs(row.flip_margin_pct) > READ_FLAG_HYST_PCT, "the row sits OUTSIDE the deadband"
    s = read_flip_strobes([row], {"SBLK": "flips (cheap/fair)"}, {"SBLK": SBLK_TAPE_CLOSE})[0]
    assert s.vintage_margin_pct == pytest.approx(SBLK_ROW_MARGIN_PCT, abs=0.005)
    assert s.vintage_price == SBLK_VINTAGE_PRICE
    # and the row is unchanged by having been measured at the tape
    assert row.price == SBLK_VINTAGE_PRICE
    assert row.flip_margin_pct == pytest.approx(SBLK_ROW_MARGIN_PCT, abs=0.005)


def test_strobe_covers_flipping_names_only():
    """§B2 scope: the block answers "would this flip settle?", so a robust name has nothing to
    settle and a §17-blocked name has no read to settle. Neither may produce a row."""
    from crude_tanker_fv.delta import read_flip_strobes

    rows = [_sblk_jrow()]
    tape = {"SBLK": SBLK_TAPE_CLOSE}
    assert read_flip_strobes(rows, {"SBLK": "robust"}, tape) == []
    assert read_flip_strobes(rows, {"SBLK": "n/a"}, tape) == []
    assert len(read_flip_strobes(rows, {"SBLK": "flips (cheap/fair)"}, tape)) == 1


def test_strobe_renders_the_deadband_warning_and_both_bases():
    """The rendered block must carry the three numbers the follow-on names — tape, boundary, signed
    distance — and must say plainly when the distance is inside the deadband, since that is the
    case the hysteresis exists for."""
    from crude_tanker_fv.delta import _render_read_flip_strobe, read_flip_strobes

    text = "\n".join(_render_read_flip_strobe(
        read_flip_strobes([_sblk_jrow()], {"SBLK": "flips (cheap/fair)"},
                          {"SBLK": SBLK_TAPE_CLOSE})))
    assert "STROBE ZONE" in text and "SBLK (+0.62%)" in text
    assert f"±{READ_FLAG_HYST_PCT:.1f}% deadband" in text
    assert "$27.89" in text and "$27.72" in text and "+0.62%" in text
    assert "+3.18% (@ $28.60)" in text, "the vintage margin must print beside it, not instead of it"
    assert "MONITOR layer" in text


def test_strobe_reaches_the_delta_report_and_nowhere_else(tmp_path: Path):
    """Routing: the delta report carries the block, and only when the pipeline hands it the rows."""
    import crude_tanker_fv.delta as dl

    snap = dl.RunSnapshot(run_at="2026-08-14T00:00:00+00:00", quarter=BOOK_QUARTER,
                          tickers={}, input_file_hashes={})
    report = dl.compute_deltas(snap, previous=None)
    strobes = dl.read_flip_strobes([_sblk_jrow()], {"SBLK": "flips (cheap/fair)"},
                                   {"SBLK": SBLK_TAPE_CLOSE})
    with_block = dl.write_delta_report(report, outputs_dir=tmp_path, strobes=strobes).read_text()
    assert "read-flip strobe" in with_block and "STROBE ZONE" in with_block
    # omitted entirely when the caller passes nothing (standalone renders stay byte-compatible)
    assert "read-flip strobe" not in dl.write_delta_report(report, outputs_dir=tmp_path).read_text()
    # and prints as quiet, not absent, when there is simply nothing flipping
    quiet = dl.write_delta_report(report, outputs_dir=tmp_path, strobes=[]).read_text()
    assert "read-flip strobe" in quiet and "STROBE ZONE" not in quiet


def test_scorecard_surface_is_unchanged_by_the_strobe(tmp_path: Path):
    """B2's other half, and the one that can only be broken silently: the tape-basis margin must
    NOT have landed on the scorecard. Both committed artefacts predate this work, so a regenerated
    scorecard that still matches them field-for-field and column-for-column is the proof."""
    import json as _json

    committed_md = (sc.OUTPUTS_DIR / "book_scorecard.md").read_text()
    committed_json = _json.loads((sc.OUTPUTS_DIR / "book_scorecard.json").read_text())

    rows = sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})
    val = {r.ticker: sc._Valuation(price=10.0, fv=12.0, upside_pct=20.0,
                                   position="BUY (undervalued)", nav_ps=11.0, broker_nav=11.5,
                                   gap_pct=-4.3, sanity="OK", approx=False) for r in rows}
    fresh_md = sc.write_scorecard(rows, outputs_dir=tmp_path, valuation=val,
                                  quarter=BOOK_QUARTER).read_text()
    fresh_json = _json.loads((tmp_path / "book_scorecard.json").read_text())

    def _tier_header(text: str) -> str:
        return next(ln for ln in text.splitlines() if ln.startswith("| Ticker | Sector | **Tier**"))

    assert _tier_header(fresh_md) == _tier_header(committed_md), "the tier table gained a column"
    assert fresh_json["schema_version"] == committed_json["schema_version"] == "2.8"
    assert set(fresh_json) == set(committed_json), "the handoff JSON gained a top-level key"
    assert (set(fresh_json["names"][0]) == set(committed_json["names"][0])), \
        "the handoff JSON gained a per-name field — the tape margin belongs to the monitor layer"
    # the row's margin is still the VINTAGE one (nothing swapped a tape number in under the name)
    by = {n["ticker"]: n for n in fresh_json["names"]}
    assert by["SBLK"]["flip_margin_pct"] == pytest.approx(-8.58, abs=0.005)  # LIVE surface value, re-pinned 2026-08-31 with the 24-Aug FFA dry promote (12M leg moved SBLK's FV boundary ~0.02pp; was -8.60 on the 8/28 rebase pin, +3.18 on the 8/07 vintage — moves with each consensus-pair rebase or FV-moving promote)
