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
    assert len(rows) == 25  # 22 + LPG validators (2026-07-10) + 2343 (Stage-3 intake, 2026-07-14)
    assert {r.ticker for r in rows} >= {"DHT", "SB", "BRUT", "TEN", "FLNG", "MPCC", "LPG", "BWLP"}


def test_eleven_resale_uniform_comparable_set(rows):
    uniform = {r.ticker for r in rows if r.nav_basis == "resale-uniform"}
    # the 11 fully-corrected names (Thread 1 + Amendment B) + 2343 (2026-07-14:
    # every class age-0 on the xclusiv Resale basis incl. Handy-Bulk via
    # alias:Handysize; NOTE the basis rollup is age-0 only — 2343's tier is
    # nonetheless capped GOVERNED-WIDE·pending-anchor by UNANCHORED_VALUE_CLASS_CAP,
    # the §11.7.11 un-anchored mid-age cap)
    assert uniform == {"DHT", "ECO", "FRO", "NAT", "TNK", "BRUT", "CAPT",
                       "CMDB", "GNK", "SB", "SBLK", "2343"}


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


def test_handoff_sleeve_blocks_for_hybrids(tmp_path, rows):
    """WO1 V-1: hybrid rows export per-sleeve PW-FV contributions summing to
    the headline fv (the C-3 per-sleeve identity, now visible at the seam) —
    the governance repo watches CMBT's dry-bulk sleeve, not the whole-co proxy.
    Pure-play rows export null."""
    import json

    val = _synthetic_valuation(rows)
    val["CMBT"] = val["CMBT"].__class__(**{**val["CMBT"].__dict__, "fv": 13.34,
                                           "sleeve_fvs": {"crude": 3.64, "dry_bulk": 8.02,
                                                          "containerships": 1.68}})
    write_scorecard(rows, outputs_dir=tmp_path, valuation=val)
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    by = {n["ticker"]: n for n in doc["names"]}
    sleeves = by["CMBT"]["sleeves"]
    assert [s["sector"] for s in sleeves] == ["crude", "dry_bulk", "containerships"]
    assert all(s["sleeve"] == s["sector"] for s in sleeves)
    # The documented reconciliation identity, to the cent (sleeves_note).
    assert sum(s["fv_contribution_per_share"] for s in sleeves) == pytest.approx(
        by["CMBT"]["fv"], abs=0.01)
    assert "sum(sleeves) == fv" in doc["sleeves_note"]
    assert by["DHT"]["sleeves"] is None                      # pure-play


def test_f13_fv_and_position_share_one_basis():
    """F-13 hard-identity guard (2026-07-02): the verdict/JSON fv must equal the
    scenario report's probability-weighted FV to the cent, and the upside must
    be computed from it — never from the blend. The two bases agreed
    incidentally under the Jun-9 war weights; the vintage separated them and
    the scorecard shipped '+28% upside · TRIM/SHORT' rows. Third instance today
    of an incidental identity treated as an invariant — surfaces assumed to
    agree get a test that they agree."""

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
    lag_ticker = rows[0].ticker
    bs_basis = {"quarter": QUARTER, "total": len(rows),
                "lagging": {lag_ticker: "2025-Q4"}, "missing": []}
    write_scorecard(rows, outputs_dir=tmp_path, valuation=_synthetic_valuation(rows),
                    price_basis=pb, quarter=QUARTER, bs_basis=bs_basis)
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    # String "2.1" — the consumer asserts major == 2 (WO1 Task 1); minor bumps
    # are additive, major bumps break. 2.3 (2026-07-09): + mark_wide_nodes.
    # 2.4 (2026-07-15, D-M5 ruled): + fv_low/fv_high (scenario min/max interval).
    # 2.5 (2026-07-15): family-range containment — out-of-range family fields
    # withhold (null) + weight_family_basis.ev_lagging names them.
    # 2.6 (2026-07-31): + price_basis.stale_fallback (freshness-gate subset;
    # the stale-run alert's counting set).
    # 2.7 (2026-08-08): + balance_sheet_basis + names[].balance_sheet_vintage
    # (the Q2-transition disclosure; per-row field derives from the one map).
    assert doc["schema_version"] == "2.7"
    assert doc["schema_version"].split(".")[0] == "2"
    assert doc["quarter"] == QUARTER
    # The per-row vintage and the run-level map are ONE datum on two surfaces
    # (2026-07-02 rule: surfaces assumed to agree get a test that they agree).
    assert doc["balance_sheet_basis"] == bs_basis
    for n in doc["names"]:
        expect = bs_basis["lagging"].get(n["ticker"], QUARTER)
        assert n["balance_sheet_vintage"] == expect, n["ticker"]
    md = (tmp_path / "book_scorecard.md").read_text()
    assert f"Balance-sheet basis: 1 of {len(rows)}" in md
    assert f"{lag_ticker} (2025-Q4)" in md
    # Vintage stamp: ISO-8601 UTC + the HEAD hash ('-dirty' allowed).
    import subprocess
    assert doc["generated_at"].endswith("+00:00") and "T" in doc["generated_at"]
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True,
                          text=True).stdout.strip()
    assert doc["source_commit"] in (head, head + "-dirty")
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
        # Units (WO1 Task 1.2): governance haircut in percentage POINTS like
        # every other _pct field — TEN and CMDB export 30.0-scale, never 0.3.
        assert n["governance_discount_pct"] == pytest.approx(r.governance_discount_pct * 100.0)
        if n["ticker"] in ("TEN", "CMDB") and r.governance_discount_pct > 0:
            assert n["governance_discount_pct"] >= 1.0   # a real haircut reads in points


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
    assert "STALE-PRICE RUN" not in text   # per-name fallbacks stay a disclosure, not a siren


def test_price_basis_header_goes_loud_when_the_overlay_aged_out(tmp_path, rows):
    """2026-07-31: >= STALE_PRICE_ALERT_MIN_NAMES freshness-gate fallbacks means
    the prices_daily vintage itself aged out — the header must SCREAM (banner
    above the quiet static-fallback line), because the flips it prints are
    presumptively phantom."""
    reason = "stale quote (2026-07-24T20:00:04+00:00)"
    pb = {"total": 22,
          "static_fallback": {t: {"as_of": "2026-06-26", "reason": reason}
                              for t in ("ASC", "STNG", "TNK")},
          "stale_fallback": {t: reason for t in ("ASC", "STNG", "TNK")},
          "oldest_static_as_of": "2026-06-26",
          "market_event_review": {}}
    text = write_scorecard(rows, outputs_dir=tmp_path, valuation=_synthetic_valuation(rows),
                           price_basis=pb).read_text()
    assert "STALE-PRICE RUN" in text and "PHANTOM" in text
    assert "ASC, STNG, TNK" in text
    assert text.index("STALE-PRICE RUN") < text.index("STATIC-FALLBACK")


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
    # The rich-long sentence is derived from the rows: every VALIDATED-TIGHT crude
    # name is named. DERIVED from `rows`, not a literal list — the literal
    # ("DHT", "ECO", "FRO", "TNK") re-red on 2026-07-31 when TNK left TIGHT for
    # GOVERNED-WIDE·read-flips at its Q2 refresh, i.e. the test that asserts
    # "nothing hardwired" was itself hardwired. Deriving it also means a future
    # tier change is caught as a tier change, not as a prose failure.
    rich_line = next(ln for ln in verdict.splitlines() if "read *rich*" in ln)
    tight_crude = {r.ticker for r in rows
                   if r.confidence_tier == "VALIDATED-TIGHT" and r.sector == "crude"}
    assert tight_crude, "no VALIDATED-TIGHT crude names — the assertion below would be vacuous"
    for t in sorted(tight_crude):
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
    assert frag["BRUT"]["ev_sign_stable"] is False and frag["SB"]["ev_sign_stable"] is True

    # upside=45.0 sits inside BOTH synthetic family ranges — the containment
    # guard (2026-07-15) withholds fields whose range excludes the point EV.
    text = write_scorecard(rows, outputs_dir=tmp_path,
                           valuation=_synthetic_valuation(rows, upside=45.0),
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
    # 2.2 (2026-07-03): the family RANGE is the seam datum — the boolean is
    # derived from it, and the consumer derives its own magnitude judgment
    # (CCEC: sign-stable BUY everywhere, sized against family_min, not the
    # point estimate).
    assert by["BRUT"]["ev_pct_family_min"] == -5.0 and by["BRUT"]["ev_pct_family_max"] == 98.1
    assert by["SB"]["ev_pct_family_min"] == 40.0
    assert by["DHT"]["ev_pct_family_min"] is None


def test_family_range_must_contain_point_ev_or_withhold(tmp_path, rows):
    """Containment guard (2026-07-15): the §9.10 family includes the ADOPTED
    weight set, so a printed family range must CONTAIN the printed point EV.
    The WO1-F4 sha stamp scopes only scenario_inputs.yaml — the MR age-0
    re-anchor (5ed418f) moved TEN's point EV +44.9 → +45.0 with the sidecar
    held, and the handoff printed a point OUTSIDE its own family range.
    Out-of-range ⇒ that name's family fields withhold (null), the basis marker
    names it, the banner says why; in-range names keep their fields."""
    import json

    frag = {"TEN": {"ev_sign_stable": True, "ev_min_pct": 26.5, "ev_max_pct": 44.9},
            "SB": {"ev_sign_stable": True, "ev_min_pct": 40.0, "ev_max_pct": 55.0}}
    fb = {"status": "current", "family_shas": {}, "current_sha": "abc123def456",
          "lagging": []}
    text = write_scorecard(rows, outputs_dir=tmp_path,
                           valuation=_synthetic_valuation(rows, upside=45.0),
                           fragility=frag, family_basis=fb).read_text()
    assert "Weight-family EV vintage: LAGGING for TEN" in text
    ten_row = next(ln for ln in text.splitlines() if ln.startswith("| TEN |"))
    assert "stable" not in ten_row                       # withheld renders as "—"
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    by = {n["ticker"]: n for n in doc["names"]}
    assert by["TEN"]["weight_sign_stable"] is None
    assert by["TEN"]["ev_pct_family_min"] is None and by["TEN"]["ev_pct_family_max"] is None
    assert by["SB"]["ev_pct_family_min"] == 40.0         # in-range: kept
    assert doc["weight_family_basis"]["ev_lagging"] == ["TEN"]
    # The emitted surface itself satisfies the invariant — nothing for the
    # coherence check to flag.
    from crude_tanker_fv.scorecard import handoff_coherence_flags

    assert not [f for f in handoff_coherence_flags(doc) if "weight-family" in f]


def test_handoff_coherence_flags_family_containment():
    """The shared checker (test + sentinel callers) flags a handoff doc whose
    point EV escapes a printed family range — exact containment, no tolerance:
    both sides share the 1-dp rounding, so a violation is vintage drift."""
    from crude_tanker_fv.scorecard import handoff_coherence_flags

    row = {"ticker": "TEN", "ev_pct": 45.0, "position": "BUY (undervalued)",
           "ev_pct_family_min": 26.5, "ev_pct_family_max": 44.9}
    flags = handoff_coherence_flags({"names": [row]})
    assert flags == ["TEN: ev_pct +45.0% outside its weight-family range [+26.5%, +44.9%]"]
    # Boundary is inside (the adopted set IS a family member), and null family
    # fields (not in a diagnostic / withheld) have nothing to check.
    assert not handoff_coherence_flags({"names": [{**row, "ev_pct_family_max": 45.0}]})
    assert not handoff_coherence_flags({"names": [{**row, "ev_pct_family_min": None,
                                                   "ev_pct_family_max": None}]})


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


def test_weight_family_basis_and_stale_withholding(tmp_path, rows):
    """WO1-F4: the fragility sidecar is stamped per family with the
    scenario_inputs.yaml content hash it was computed against; a lagging
    family withholds ALL family fields (null, never silently current) and the
    basis marker says why on both surfaces."""
    import json


    from crude_tanker_fv.scorecard import (
        scenario_inputs_sha, update_weight_fragility_sidecar, weight_family_basis,
    )

    inputs = tmp_path / "inputs"
    inputs.mkdir()
    (inputs / "scenario_inputs.yaml").write_text("sectors: {a: 1}\n")
    outputs = tmp_path / "outputs"

    # Per-family stamps: one family re-running must not vouch for the others.
    update_weight_fragility_sidecar(
        "crude", {"SetX": {}}, {"BRUT": {"ev_sign_stable": False,
                                         "ev_min_pct": -61.4, "ev_max_pct": 17.3}},
        outputs_dir=outputs, inputs_dir=inputs)
    sha1 = scenario_inputs_sha(inputs)
    assert weight_family_basis(outputs, inputs)["status"] == "current"

    (inputs / "scenario_inputs.yaml").write_text("sectors: {a: 2}\n")   # weights change
    fb = weight_family_basis(outputs, inputs)
    assert fb["status"] == "stale" and fb["lagging"] == ["crude"]
    assert fb["family_shas"]["crude"] == sha1 != fb["current_sha"]

    # Stale basis at generation: fields withheld + marker on both surfaces.
    text = write_scorecard(rows, outputs_dir=outputs, valuation=_synthetic_valuation(rows),
                           fragility={}, family_basis=fb).read_text()
    assert "Weight-family basis: STALE" in text and "lagging: crude" in text
    doc = json.loads((outputs / "book_scorecard.json").read_text())
    assert doc["weight_family_basis"]["status"] == "stale"
    assert all(n["weight_sign_stable"] is None and n["ev_pct_family_min"] is None
               for n in doc["names"])

    # Re-running the lagging family against the new determinants clears it.
    update_weight_fragility_sidecar(
        "crude", {"SetX": {}}, {"BRUT": {"ev_sign_stable": False,
                                         "ev_min_pct": -60.0, "ev_max_pct": 15.0}},
        outputs_dir=outputs, inputs_dir=inputs)
    assert weight_family_basis(outputs, inputs)["status"] == "current"


def test_mark_wide_nodes_reach_the_handoff_json(tmp_path, rows):
    """F-1 (owner review 2026-07-09), the seam half: a name exposed to a §9.9
    wide node carries mark_wide_nodes in book_scorecard.json (null when clean) —
    the registry/exposure halves live in test_lpg_sector. Since the WO3 Phase-4
    onboarding (2026-07-10) the book carries REAL exposed rows: both VLGC
    validators own hulls on the extrapolated age-5 node (Dorian: Captain Markos
    age 3; BWLP: Avior/Rigel/Capella/Polaris/Yushi/Kizoku ages 3-7)."""
    import json

    pb = {"total": len(rows), "static_fallback": {}, "oldest_static_as_of": None,
          "market_event_review": {}}
    write_scorecard(rows, outputs_dir=tmp_path, valuation=_synthetic_valuation(rows),
                    price_basis=pb, quarter=QUARTER)
    doc = json.loads((tmp_path / "book_scorecard.json").read_text())
    by = {n["ticker"]: n for n in doc["names"]}
    assert by["LPG"]["mark_wide_nodes"] == ["VLGC@five_year"]
    assert by["BWLP"]["mark_wide_nodes"] == ["VLGC@five_year"]
    # 2026-07-18 (PPMX seed): SB joins — its Post-Panamax book sits on the
    # freshly-seeded wide-node fit (ppmx_fit_seed_prereg_2026-07-18.md).
    assert by["SB"]["mark_wide_nodes"] == ["Post-Panamax@five_year+ten_year"]
    assert all(by[r.ticker]["mark_wide_nodes"] is None
               for r in rows if r.ticker not in ("LPG", "BWLP", "SB"))
    # And the markdown surfaces it next to the NAV-basis flags.
    md = (tmp_path / "book_scorecard.md").read_text()
    assert "§9.9 wide-node exposure" in md and "VLGC@five_year" in md


def test_sidecar_merge_preserves_all_other_families(tmp_path):
    """Regression (2026-07-08, caught wiring the lpg family): the merge's
    pre-namespacing guard was a hardcoded {crude, product, lng} whitelist, so
    the FIRST call after a new sector family landed (dry_bulk, WO4) wiped every
    other family's weight_sets — and, because weight_family_basis scopes its
    staleness check to set(weight_sets), silently NARROWED the staleness guard
    to the caller. Shape detection (set-label keys vs family tokens) replaced
    the whitelist; this pins N-family preservation for any future sector."""
    import yaml

    from crude_tanker_fv.scorecard import update_weight_fragility_sidecar, weight_family_basis

    inputs = tmp_path / "inputs"
    inputs.mkdir()
    (inputs / "scenario_inputs.yaml").write_text("sectors: {a: 1}\n")
    outputs = tmp_path / "outputs"

    for fam in ("crude", "product", "lng", "dry_bulk", "lpg"):
        update_weight_fragility_sidecar(
            fam, {f"{fam.title()} Set A": {"s": 1.0}}, {},
            outputs_dir=outputs, inputs_dir=inputs)

    doc = yaml.safe_load((outputs / "weight_robustness.yaml").read_text())
    assert set(doc["weight_sets"]) == {"crude", "product", "lng", "dry_bulk", "lpg"}
    assert set(doc["computed_against"]) == {"crude", "product", "lng", "dry_bulk", "lpg"}
    # The staleness guard covers ALL families, not just the last caller.
    (inputs / "scenario_inputs.yaml").write_text("sectors: {a: 2}\n")
    update_weight_fragility_sidecar("lpg", {"LPG Set A": {"s": 1.0}}, {},
                                    outputs_dir=outputs, inputs_dir=inputs)
    fb = weight_family_basis(outputs, inputs)
    assert fb["status"] == "stale"
    assert fb["lagging"] == ["crude", "dry_bulk", "lng", "product"]

    # The TRUE pre-namespacing shape (set-label keys, no family tokens) is
    # still detected and dropped rather than merged as junk families.
    legacy = outputs / "weight_robustness.yaml"
    legacy.write_text(yaml.safe_dump({
        "weight_sets": {"Crude Set A (locked 2026-06-09)": {"s": 1.0}},
        "names": {},
    }))
    update_weight_fragility_sidecar("crude", {"Crude Set A": {"s": 1.0}}, {},
                                    outputs_dir=outputs, inputs_dir=inputs)
    doc = yaml.safe_load(legacy.read_text())
    assert set(doc["weight_sets"]) == {"crude"}


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
