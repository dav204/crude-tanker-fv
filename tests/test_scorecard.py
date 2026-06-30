"""Book-wide validation scorecard (Thread 4)."""

from __future__ import annotations

import pytest

from crude_tanker_fv.scorecard import (
    _nav_basis_composite,
    _parity_band_status,
    compute_scorecard,
    write_scorecard,
)

QUARTER = "2026-Q1"


# --- pure helpers (deterministic, no IO) ----------------------------------- #

def test_nav_basis_resale_uniform_only_if_all_uniform():
    s = {"VLCC": "resale-uniform", "Suezmax": "resale-uniform"}
    assert _nav_basis_composite(["VLCC", "Suezmax"], s) == ("resale-uniform", "")


def test_nav_basis_primary_is_most_salient_and_detail_shows_all():
    # holds resale-uniform + pending + unverified ⇒ primary pending-sourceable (more
    # salient than unverified), detail lists BOTH non-uniform groups.
    s = {"VLCC": "resale-uniform", "LR1": "pending-sourceable",
         "MR": "unverified-no-current-xclusiv-line"}
    primary, detail = _nav_basis_composite(["VLCC", "LR1", "MR"], s)
    assert primary == "pending-sourceable"
    assert "pending-sourceable: LR1" in detail and "unverified-no-current-xclusiv-line: MR" in detail


def test_nav_basis_structural_outranks_pending():
    s = {"LNGC": "structural-unavailable", "LR1": "pending-sourceable"}
    primary, _ = _nav_basis_composite(["LNGC", "LR1"], s)
    assert primary == "structural-unavailable"


def test_parity_band_clears_and_out_and_unvalidated():
    assert _parity_band_status(["VLCC"], {"VLCC": 41_700.0}) == "clears"        # in [41220,42220]
    assert _parity_band_status(["VLCC"], {"VLCC": 50_000.0}) == "OUT:VLCC"
    assert _parity_band_status(["LNGC"], {"LNGC": None}) == "unvalidated"        # no registered band
    assert _parity_band_status(["VLCC", "LNGC"], {"VLCC": 41_700.0, "LNGC": None}) == "clears (+unvalidated)"


# --- end-to-end (one compute, shared) -------------------------------------- #

@pytest.fixture(scope="module")
def rows():
    return compute_scorecard(QUARTER)


def test_scorecard_covers_whole_book(rows):
    assert len(rows) == 22
    assert {r.ticker for r in rows} >= {"DHT", "SB", "BRUT", "TEN", "FLNG", "MPCC"}


def test_eleven_resale_uniform_comparable_set(rows):
    uniform = {r.ticker for r in rows if r.nav_basis == "resale-uniform"}
    # the 11 fully-corrected names (Thread 1 + Amendment B)
    assert uniform == {"DHT", "ECO", "FRO", "NAT", "TNK", "BRUT", "CAPT",
                       "CMDB", "GNK", "SB", "SBLK"}


def test_both_185_gates_pending_book_wide(rows):
    # No Baltic $/day series, no orderbook ratios in-repo ⇒ every name pending.
    assert all(r.gate_5a == "pending" for r in rows)
    assert all(r.gate_5b == "pending" for r in rows)


def test_pending_not_passed_flagged_names_are_not_resale_uniform(rows):
    by = {r.ticker: r for r in rows}
    assert by["INSW"].nav_basis == "pending-sourceable"      # holds LR1
    assert by["TEN"].nav_basis == "structural-unavailable"   # holds LNGC
    assert by["FLNG"].nav_basis == "structural-unavailable"
    # SB (the canary) is on the uniform basis and cheap on both bases.
    assert by["SB"].nav_basis == "resale-uniform" and by["SB"].robust == "robust"


def test_crude_parity_bands_clear(rows):
    for t in ("DHT", "FRO", "NAT"):
        r = next(x for x in rows if x.ticker == t)
        assert r.parity_band.startswith("clears")


def test_write_scorecard_emits_matrix(tmp_path, rows):
    path = write_scorecard(rows, outputs_dir=tmp_path)
    text = path.read_text()
    assert path.name == "book_scorecard.md"
    assert "Book-wide scorecard" in text
    assert "comparability boundary" in text
    assert "registered-PENDING" in text
    assert "| DHT |" in text and "| SB |" in text
    # No valuation passed ⇒ validation-only, no verdict section (backward compatible).
    assert "Verdict — the consolidated read" not in text


def test_valuation_index_uses_whole_company_spine_for_hybrids():
    """Regression: a hybrid (INSW) renders as a single SLEEVE in fv_reports with a sleeve-allocated
    price/NAV. The verdict MUST take price/NAV/position from the scenario spine (whole company),
    matching the delta-report headline — never the sleeve. Caught 2026-06-30."""
    from types import SimpleNamespace as NS

    from crude_tanker_fv.scorecard import valuation_index

    fv = [NS(ticker="INSW", blended=NS(fair_value_per_share=38.63),
             nav=NS(nav_per_share=34.97), current_price=50.91)]            # crude SLEEVE
    sc = [NS(ticker="INSW", current_price=77.81, base_nav_per_share=52.59,  # WHOLE company
             position_recommendation="TRIM/SHORT (overvalued)")]
    bk = [NS(ticker="INSW", consensus_pnav=0.98)]
    v = valuation_index(fv, sc, bk)["INSW"]
    assert v.price == 77.81 and v.nav_ps == 52.59          # whole-company spine, not the sleeve
    assert v.fv == 38.63                                   # single-point FV from the CompanyReport
    assert v.position == "TRIM/SHORT (overvalued)"


def test_write_scorecard_emits_consolidated_verdict_when_valuation_present(tmp_path, rows):
    """With the valuation join, ONE file carries the verdict (FV-vs-price + position + broker NAV)
    above the validation matrix — the single handoff surface. A PROVISIONAL name is flagged NO."""
    from crude_tanker_fv.scorecard import _Valuation

    val = {
        r.ticker: _Valuation(
            price=10.0, fv=12.0, upside_pct=20.0, position="BUY (undervalued)",
            nav_ps=11.0, broker_nav=11.5, gap_pct=-4.3, sanity="OK",
            approx=(r.ticker in {"SB", "NAT"}),
        )
        for r in rows
    }
    path = write_scorecard(rows, outputs_dir=tmp_path, valuation=val)
    text = path.read_text()
    assert "Verdict — the consolidated read" in text
    assert "single handoff surface" in text
    assert "Validation matrix — per-gate detail" in text          # the detail still ships, same file
    assert "| Ticker | Sector | **Tier · why** | Price | Model FV |" in text
    # every PROVISIONAL name is flagged not-handoff-ready in the verdict
    for r in rows:
        if r.confidence_tier == "PROVISIONAL":
            assert "⛔" in text
    # the opportunity-set finding (BUY positions here ⇒ the 2 cheap TIGHT names qualify as longs)
    assert "validated-and-actionable-long surface is **2 (SB, SBLK" in text


def test_verdict_applies_owner_label_corrections(tmp_path, rows):
    """The three owner corrections (2026-06-30): (1) a cycle-rich position is relabeled away from
    TRIM/SHORT; (2) the tier cell carries a sub-reason / resolution path; (3) a name whose derived
    NAV rests on a contradicted figure (NAT) prints `void`, not numbers."""
    from crude_tanker_fv.scorecard import _Valuation

    # give the relabel/void candidates their real (overvalued) position so the relabel is visible
    val = {
        r.ticker: _Valuation(
            price=10.0, fv=8.0, upside_pct=-20.0, position="TRIM/SHORT (overvalued)",
            nav_ps=9.0, broker_nav=12.0, gap_pct=-25.0, sanity="OK", approx=False,
        )
        for r in rows
    }
    text = write_scorecard(rows, outputs_dir=tmp_path, valuation=val).read_text()
    verdict = text.split("## Validation matrix")[0]   # only the Verdict section

    # (1) cycle-position relabel: DHT's row says cycle position, never TRIM/SHORT
    dht = next(ln for ln in verdict.splitlines() if ln.startswith("| DHT |"))
    assert "cycle position" in dht and "TRIM/SHORT" not in dht
    mpcc = next(ln for ln in verdict.splitlines() if ln.startswith("| MPCC |"))
    assert "unreliable read" in mpcc and "TRIM/SHORT" not in mpcc
    # (2) tier sub-reasons present
    assert "GOVERNED-WIDE · structural-class" in verdict
    assert "GOVERNED-WIDE · newbuild-heavy" in verdict     # CAPT
    assert "PROVISIONAL · void" in verdict                 # NAT
    # (3) NAT's derived numbers are voided, not printed
    nat = next(ln for ln in verdict.splitlines() if ln.startswith("| NAT |"))
    assert "void" in nat and "-25%" not in nat and "$9.00" not in nat


def test_verdict_label_registry_tracks_the_tiers_no_drift():
    """provenance.py is the single source: the tier sub-reason map must cover EXACTLY the
    GOVERNED-WIDE + PROVISIONAL names, and the position-relabel / void sets must sit inside the
    book and stay disjoint — so a new name can't silently miss a label."""
    import crude_tanker_fv.provenance as prov

    rows = compute_scorecard(QUARTER)
    by_tier = {t: {r.ticker for r in rows if r.confidence_tier == t}
               for t in ("VALIDATED-TIGHT", "GOVERNED-WIDE", "PROVISIONAL")}
    book = {r.ticker for r in rows}
    assert set(prov.TIER_SUBREASON) == by_tier["GOVERNED-WIDE"] | by_tier["PROVISIONAL"]
    assert prov.NAV_DERIVED_VOID <= by_tier["PROVISIONAL"]
    assert prov.POSITION_CYCLE_RELABEL <= book and prov.POSITION_UNRELIABLE <= book
    assert not (prov.POSITION_CYCLE_RELABEL & prov.POSITION_UNRELIABLE)
    assert not (prov.POSITION_CYCLE_RELABEL & prov.NAV_DERIVED_VOID)   # void != cycle-relabel
