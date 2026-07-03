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
    price/NAV. The verdict MUST take price/NAV/FV/position from the scenario spine (whole company),
    matching the delta-report headline — never the sleeve. Caught 2026-06-30.
    RE-BASED 2026-07-02 (F-13): fv is now the SCENARIO-weighted FV (same basis as position);
    the single-point blend moves to the labeled secondary blend_fv."""
    from types import SimpleNamespace as NS

    from crude_tanker_fv.scorecard import valuation_index

    fv = [NS(ticker="INSW", blended=NS(fair_value_per_share=38.63),
             nav=NS(nav_per_share=34.97), current_price=50.91)]            # crude SLEEVE
    sc = [NS(ticker="INSW", current_price=77.81, base_nav_per_share=52.59,  # WHOLE company
             probability_weighted_fv=51.76,
             position_recommendation="TRIM/SHORT (overvalued)")]
    bk = [NS(ticker="INSW", consensus_pnav=0.98)]
    v = valuation_index(fv, sc, bk)["INSW"]
    assert v.price == 77.81 and v.nav_ps == 52.59          # whole-company spine, not the sleeve
    assert v.fv == 51.76                                   # SCENARIO-weighted FV (F-13 headline basis)
    assert v.blend_fv == 38.63                             # blend demoted to the secondary column
    assert v.position == "TRIM/SHORT (overvalued)"


def test_f13_fv_and_position_share_one_basis():
    """F-13 hard-identity guard (2026-07-02): the verdict/JSON fv must equal the
    scenario report's probability-weighted FV to the cent, and the upside must
    be computed from it — never from the blend. The two bases agreed
    incidentally under the Jun-9 war weights; the vintage separated them and
    the scorecard shipped '+28% upside · TRIM/SHORT' rows. Third instance today
    of an incidental identity treated as an invariant — surfaces assumed to
    agree get a test that they agree."""
    import json

    from types import SimpleNamespace as NS

    from crude_tanker_fv.scorecard import valuation_index

    fv = [NS(ticker="CAPT", blended=NS(fair_value_per_share=16.03),
             nav=NS(nav_per_share=15.49), current_price=12.49)]
    sc = [NS(ticker="CAPT", current_price=12.49, base_nav_per_share=15.49,
             probability_weighted_fv=10.07,
             position_recommendation="TRIM/SHORT (overvalued)")]
    bk = [NS(ticker="CAPT", consensus_pnav=0.67)]
    v = valuation_index(fv, sc, bk)["CAPT"]
    assert v.fv == pytest.approx(10.07, abs=0.005)                 # to the cent
    assert v.upside_pct == pytest.approx((10.07 / 12.49 - 1) * 100, abs=0.01)
    assert v.upside_pct < 0 and v.position.startswith("TRIM/SHORT")  # coherent sign
    assert v.blend_fv == pytest.approx(16.03)


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


def test_verdict_applies_owner_label_corrections(tmp_path, rows, monkeypatch):
    """The owner label corrections render: (1) cycle-rich positions are relabeled away from TRIM/SHORT
    (DHT, and NAT — the §12 archetype, de-voided 2026-06-30); (2) the tier cell carries a sub-reason /
    resolution path, incl. NAT's `newbuild-indeterminate`; (3) the void-rendering path strikes all
    derived numbers for any name in NAV_DERIVED_VOID — exercised here with a stand-in, since NAT
    de-voided and the live set is now empty (kept as coverage for the next contradicted-figure name)."""
    import crude_tanker_fv.scorecard as sc_mod
    from crude_tanker_fv.scorecard import _Valuation

    # give the relabel candidates their real (overvalued) position so the relabel is visible
    val = {
        r.ticker: _Valuation(
            price=10.0, fv=8.0, upside_pct=-20.0, position="TRIM/SHORT (overvalued)",
            nav_ps=9.0, broker_nav=12.0, gap_pct=-25.0, sanity="OK", approx=False,
        )
        for r in rows
    }
    verdict = write_scorecard(rows, outputs_dir=tmp_path, valuation=val).read_text().split("## Validation matrix")[0]

    # (1) cycle-position relabel: DHT and NAT say cycle position, never TRIM/SHORT
    for t in ("DHT", "NAT"):
        ln = next(x for x in verdict.splitlines() if x.startswith(f"| {t} |"))
        assert "cycle position" in ln and "TRIM/SHORT" not in ln
    mpcc = next(ln for ln in verdict.splitlines() if ln.startswith("| MPCC |"))
    assert "unreliable read" in mpcc and "TRIM/SHORT" not in mpcc
    # (2) tier sub-reasons present, incl. NAT's newbuild-indeterminate (de-voided -> GOVERNED-WIDE, real numbers)
    assert "GOVERNED-WIDE · structural-class" in verdict
    assert "GOVERNED-WIDE · newbuild-heavy" in verdict            # CAPT
    assert "GOVERNED-WIDE · newbuild-indeterminate" in verdict    # NAT
    nat = next(ln for ln in verdict.splitlines() if ln.startswith("| NAT |"))
    assert "$9.00" in nat                                         # NAT now prints REAL numbers (de-voided)

    # (3) the void-rendering path strikes all derived numbers for a name in NAV_DERIVED_VOID (mechanism
    # coverage via a stand-in — the live set is empty after NAT de-voided).
    monkeypatch.setattr(sc_mod, "NAV_DERIVED_VOID", {"GSL"})
    v2 = write_scorecard(rows, outputs_dir=tmp_path, valuation=val).read_text().split("## Validation matrix")[0]
    gsl = next(ln for ln in v2.splitlines() if ln.startswith("| GSL |"))
    assert "void" in gsl and "$9.00" not in gsl


def _synthetic_valuation(rows, position="BUY (undervalued)", fv=12.0, upside=20.0):
    from crude_tanker_fv.scorecard import _Valuation

    return {
        r.ticker: _Valuation(
            price=10.0, fv=fv, upside_pct=upside, position=position,
            nav_ps=11.0, broker_nav=11.5, gap_pct=-4.3, sanity="OK", approx=False,
        )
        for r in rows
    }


def test_handoff_json_is_a_versioned_contract(tmp_path, rows):
    """The machine-readable handoff (audit F-4): schema-versioned, same objects
    as the Verdict table — tier, sub-reason, handoff-ready, position — so the
    governance repo ingests a contract, not a rendered table."""
    import json

    import crude_tanker_fv.provenance as prov
    from crude_tanker_fv.scorecard import is_handoff_ready

    pb = {"total": len(rows), "static_fallback": {}, "oldest_static_as_of": None,
          "market_event_review": {}}
    write_scorecard(rows, outputs_dir=tmp_path, valuation=_synthetic_valuation(rows),
                    price_basis=pb, quarter=QUARTER)
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    assert doc["schema_version"] == 2   # v2 = F-13 re-basing (fv/ev_pct scenario-weighted)
    assert doc["quarter"] == QUARTER
    assert doc["price_basis"]["total"] == len(rows)
    assert len(doc["names"]) == len(rows)
    by_row = {r.ticker: r for r in rows}
    for n in doc["names"]:
        r = by_row[n["ticker"]]
        assert n["confidence_tier"] == r.confidence_tier
        assert n["tier_subreason"] == prov.TIER_SUBREASON.get(r.ticker)
        assert n["handoff_ready"] == is_handoff_ready(r.confidence_tier)
        assert n["nav_basis"] == r.nav_basis
        assert n["fv"] == 12.0 and n["price"] == 10.0
        # relabeled positions carry through to the JSON exactly as displayed
        if r.ticker in prov.POSITION_CYCLE_RELABEL:
            assert n["position"] == "rich · cycle position (not a short)"


def test_handoff_json_voids_derived_numbers_and_rejects_nan(tmp_path, rows, monkeypatch):
    import json

    import crude_tanker_fv.scorecard as sc_mod

    monkeypatch.setattr(sc_mod, "NAV_DERIVED_VOID", {"GSL"})
    val = _synthetic_valuation(rows)
    val["DHT"] = val["DHT"].__class__(**{**val["DHT"].__dict__, "fv": float("nan"),
                                         "upside_pct": float("nan")})
    write_scorecard(rows, outputs_dir=tmp_path, valuation=val)
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    gsl = next(n for n in doc["names"] if n["ticker"] == "GSL")
    assert gsl["void"] and gsl["fv"] is None and gsl["ev_pct"] is None
    assert gsl["handoff_ready"] is False
    assert gsl["position"] == "void — pending reconciliation"
    dht = next(n for n in doc["names"] if n["ticker"] == "DHT")
    assert dht["fv"] is None                       # NaN -> null, never bare NaN in the file
    assert "NaN" not in (tmp_path / "book_scorecard.json").read_text()


def test_price_basis_header_announces_static_fallbacks(tmp_path, rows):
    """A stale-price scorecard must say so in its header (audit F-1: five names
    silently valued on June-4 statics on decision day)."""
    pb = {"total": 22,
          "static_fallback": {"ASC": {"as_of": "2026-06-04", "reason": "day move -21.7%"},
                              "DHT": {"as_of": "2026-06-04", "reason": "day move -17.2%"}},
          "oldest_static_as_of": "2026-06-04",
          "market_event_review": {"TNK": "day move -15.7% exceeds ±15% band"}}
    text = write_scorecard(rows, outputs_dir=tmp_path, valuation=_synthetic_valuation(rows),
                           price_basis=pb).read_text()
    assert "2 of 22 prices are STATIC-FALLBACK" in text
    assert "oldest as-of 2026-06-04" in text and "ASC, DHT" in text
    assert "Market-event review:" in text and "TNK" in text


def test_verdict_prose_is_derived_not_hardwired(tmp_path, rows):
    """Audit F-8: the opportunity-set narrative must follow the rows. A raw
    TRIM/SHORT outside the relabel/unreliable/void registries is a name-specific
    short and the prose must SAY so — never assert 'not one is a name-specific
    short' from a hand-written literal."""
    val = _synthetic_valuation(rows)
    # GNK: dry-bulk name in no position registry — force a raw short on it.
    val["GNK"] = val["GNK"].__class__(**{**val["GNK"].__dict__,
                                         "position": "TRIM/SHORT (overvalued)"})
    verdict = write_scorecard(rows, outputs_dir=tmp_path, valuation=val)\
        .read_text().split("## Validation matrix")[0]
    assert "Name-specific shorts: GNK" in verdict
    assert "not one is a name-specific short" not in verdict
    # The rich-long sentence is derived from the rows: with this synthetic
    # all-BUY valuation, every VALIDATED-TIGHT name reading rich historically
    # (DHT, ECO, FRO, TNK) is named — nothing hardwired to TNK.
    rich_line = next(ln for ln in verdict.splitlines() if "read *rich*" in ln)
    for t in ("DHT", "ECO", "FRO", "TNK"):
        assert t in rich_line


def test_weight_fragility_flag_renders_and_reaches_the_json(tmp_path, rows):
    """Review 2026-07-02 W-1: EV-sign stability across the §9.10 weight family
    must sit on the verdict row and in the handoff JSON — the mechanical form
    of the BRUT lesson (BUY +98% under one prior, HOLD −5% under another)."""
    import json

    import yaml

    from crude_tanker_fv.scorecard import load_weight_fragility

    (tmp_path / "weight_robustness.yaml").write_text(yaml.safe_dump({
        "weight_sets": {},
        "names": {"BRUT": {"ev_min_pct": -5.0, "ev_max_pct": 98.1, "ev_sign_stable": False},
                  "SB": {"ev_min_pct": 40.0, "ev_max_pct": 55.0, "ev_sign_stable": True}},
    }))
    frag = load_weight_fragility(tmp_path)
    assert frag == {"BRUT": False, "SB": True}

    text = write_scorecard(rows, outputs_dir=tmp_path, valuation=_synthetic_valuation(rows),
                           fragility=frag).read_text()
    brut = next(ln for ln in text.splitlines() if ln.startswith("| BRUT |"))
    assert "⚠ sign flips" in brut
    sb = next(ln for ln in text.splitlines() if ln.startswith("| SB |"))
    assert "stable" in sb
    dht = next(ln for ln in text.splitlines() if ln.startswith("| DHT |"))
    assert dht.rstrip().endswith("| — |")          # not in the diagnostic
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    by = {n["ticker"]: n for n in doc["names"]}
    assert by["BRUT"]["weight_sign_stable"] is False
    assert by["SB"]["weight_sign_stable"] is True
    assert by["DHT"]["weight_sign_stable"] is None


def test_rate_basis_note_reaches_scorecard_and_json(tmp_path, rows):
    """Reviewer condition 2026-07-02: a held rate anchor must announce itself
    in the OUTPUTS (the mtime-based preflight can't see a held VALUE). The
    note is data-driven from ffa_forward_curve.yaml's vintage_notes — no
    hardcoded dates in code (the F-8 lesson)."""
    import json

    import yaml

    from crude_tanker_fv.scorecard import rate_basis_notes

    (tmp_path / "market_data").mkdir()
    (tmp_path / "market_data" / "ffa_forward_curve.yaml").write_text(yaml.safe_dump({
        "vintage_notes": ["Tanker forwards HELD at 2026-06-07 vintage — test note."],
        "ffa_forward_curve": {"VLCC": [1, 2]},
    }))
    notes = rate_basis_notes(tmp_path)
    assert notes == ["Tanker forwards HELD at 2026-06-07 vintage — test note."]

    text = write_scorecard(rows, outputs_dir=tmp_path, valuation=_synthetic_valuation(rows),
                           rate_basis=notes).read_text()
    assert "> **Rate basis:** Tanker forwards HELD at 2026-06-07 vintage" in text
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    assert doc["rate_basis"] == notes
    # The live inputs file must actually carry the note while the hold stands.
    assert any("HELD" in n for n in rate_basis_notes())


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
