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
from crude_tanker_fv.provenance import TIER_SUBREASON, confidence_tier, tier_subreason

# SBLK at the 2026-08-13 rebase — the worked example the amendment is pinned to (§2).
SBLK_NAV = 32.785
SBLK_J_PAR = 1.11602
SBLK_J_HIST = 0.930
SBLK_BOUNDARY = 27.72      # NAV x J_hist / (1 + FAIR_BAND)
SBLK_TAPE_CLOSE = 27.89    # the 8/13 live close
SBLK_MARGIN_PCT = 0.62     # +0.62% — inside the deadband, the strobe zone that motivated it


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
    """§7: the amendment RELOCATES the constraint; it must not enlarge position authorization.
    The edge-cleared set gates on the GOVERNED flag, so a now-TIGHT flipping name cannot enter."""
    rows = sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})
    edge_cleared = sorted(r.ticker for r in rows
                          if r.confidence_tier == "VALIDATED-TIGHT"
                          and r.read_flag == "robust" and r.read_hist == "cheap")
    assert edge_cleared == ["SB"]


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


def test_prior_state_cannot_reach_the_tier(tmp_path: Path):
    """The governed flag is stateful BY DESIGN; the tier must not be. A hostile prior state must
    leave every tier untouched — otherwise run order could restate a sizing input."""
    clean = {r.ticker: r.confidence_tier for r in sc.compute_scorecard(BOOK_QUARTER, read_flag_state={})}
    hostile = {t: "flips (cheap/fair)" for t in clean}
    seeded = {r.ticker: r.confidence_tier
              for r in sc.compute_scorecard(BOOK_QUARTER, read_flag_state=hostile)}
    assert seeded == clean
