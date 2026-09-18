"""The deterministic price-attribution annotator (2026-09-15).

It is allowed to say exactly one thing — the tape moved, the valuation did not — and it must
REFUSE everything else. These guards drive the refusals, because a refusal is the safety
property: a wrongly-accepted row would put a false cause into the ratified baseline.
"""


import pytest

from crude_tanker_fv import annotate as an
from crude_tanker_fv import drift_gate, promote

ANCHOR_COMMIT, ANCHOR_STAMP, CUR_STAMP = "1988a4d", "b357696", "075a357"


def _surface(fv, price, **over):
    row = {"ticker": "AAA", "fv": fv, "price": price, "position": "TRIM/SHORT (overvalued)",
           "ev_pct": round((fv / price - 1) * 100, 1), "broker_nav": None, "void": False,
           "sanity": "OK"}
    row.update(over)
    return {"generated_at": "2026-09-16T01:00:00+00:00", "source_commit": ANCHOR_STAMP,
            "names": [row], "price_basis": {}}


def _ctx(anchor_fv=16.32, anchor_px=22.00, now_fv=16.32, now_px=22.30, *, base_ev=None,
         price_basis=None, asof="2026-09-15", **now_over):
    anchor = _surface(anchor_fv, anchor_px)
    current = _surface(now_fv, now_px, **now_over)
    current["source_commit"] = CUR_STAMP
    if price_basis:
        current["price_basis"] = price_basis
    ev_from = base_ev if base_ev is not None else round((anchor_fv / anchor_px - 1) * 100, 1)
    return an.RunContext(
        baseline={"meta": {"ratified_at": "2026-09-11T20:00:00Z", "ratified_commit": ANCHOR_COMMIT},
                  "names": {"AAA": {"ev_pct": ev_from}}},
        state={"run_at": "2026-09-16T01:00:00+00:00",
               "tickers": {"AAA": {"ev_pct": round((now_fv / now_px - 1) * 100, 1)}}},
        current=current, anchor=anchor, prices={"AAA": {"asof": f"{asof}T20:00:00+00:00"}},
        anchor_commit=ANCHOR_COMMIT, anchor_stamp=ANCHOR_STAMP, current_stamp=CUR_STAMP,
        day="2026-09-16", moved=[an.PRICE_LEG_PATH])


def _row(**over):
    kw = {"ticker": "AAA", "pnav_basis": "pareto", "status": "UNEXPLAINED", "breaches": ["EV%"],
          "band_from": None, "band_to": None, "d_ev": -1.0, "d_nav_pct": 0.0, "d_k": None}
    kw.update(over)
    return drift_gate.DriftRow(**kw)


def test_accepts_a_pure_price_row_and_carries_the_numbers():
    ok, reason, f = an.pure_price(_row(), _ctx())
    assert ok, reason
    assert f["fv"] == 16.32 and f["price_anchor"] == 22.00 and f["price_now"] == 22.30
    assert f["asof"] == "2026-09-15"
    assert abs(f["resid_pp"]) <= f["tol_pp"]


def test_refuses_a_fair_value_move():
    """The whole point. A cause is needed and a machine must not invent one."""
    ok, reason, _ = an.pure_price(_row(), _ctx(now_fv=16.40))
    assert not ok and "fair value moved 16.32 -> 16.40" in reason


def test_refuses_a_flip_toward_buy_so_the_buyflip_fork_keeps_it():
    ok, reason, _ = an.pure_price(
        _row(band_from="HOLD (fairly valued)", band_to="BUY (undervalued)", breaches=["EV%"]),
        _ctx(anchor_fv=35.14, anchor_px=35.08, now_fv=35.14, now_px=32.96))
    assert not ok and "buyflip fork's objection window" in reason


def test_refuses_when_cent_rounding_is_coarser_than_the_claim():
    """A sub-$2 name: cent rounding cannot tell a tape move from a curve move, so the machine
    must not claim it did (the 2343 round-trip across the 2026-09-15 dry-FFA promote)."""
    ok, reason, _ = an.pure_price(_row(), _ctx(anchor_fv=0.38, anchor_px=0.54,
                                               now_fv=0.38, now_px=0.53))
    assert not ok and "too\ncoarse".replace("\n", " ") in reason and "pp of EV" in reason


def test_refuses_a_nav_move_and_a_re_read_breach():
    ok, reason, _ = an.pure_price(_row(d_nav_pct=-0.4), _ctx())
    assert not ok and "not exactly 0.0" in reason
    ok, reason, _ = an.pure_price(_row(breaches=["EV%", "nav"]), _ctx())
    assert not ok and "is a re-read" in reason


def test_refuses_a_changed_price_basis_or_a_broken_construction():
    ok, reason, _ = an.pure_price(_row(), _ctx(price_basis={"static_fallback": {"AAA": "x"}}))
    assert not ok and "BASIS changed, not the tape" in reason
    ok, reason, _ = an.pure_price(_row(), _ctx(void=True))
    assert not ok and "construction" in reason


def test_refuses_an_unmoved_price():
    ok, reason, _ = an.pure_price(_row(), _ctx(now_px=22.00))
    assert not ok and "price is unchanged" in reason


def test_a_k_breach_needs_broker_nav_to_track_the_tape():
    """k_broker is AFFINE in price, so the proof is that broker NAV (= price / consensus_pnav)
    moved by the SAME ratio as the price — which is what shows consensus_pnav did not move."""
    ctx = _ctx(now_over={} or {})
    ctx.anchor["names"][0]["broker_nav"] = 20.00
    ctx.current["names"][0]["broker_nav"] = 20.00 * (22.30 / 22.00)
    ok, reason, f = an.pure_price(_row(breaches=["EV%", "k_broker"], d_k=0.06), ctx)
    assert ok, reason
    assert f["broker_nav_now"] == pytest.approx(20.2727, abs=1e-3)
    ctx.current["names"][0]["broker_nav"] = 25.00          # consensus_pnav moved
    ok, reason, _ = an.pure_price(_row(breaches=["EV%", "k_broker"], d_k=0.06), ctx)
    assert not ok and "consensus_pnav moved" in reason


def test_the_written_entry_actually_explains_the_row_to_the_gate(tmp_path):
    """End to end on the real functions: the entry the annotator writes must satisfy
    drift_gate.decision_log_annotated_since, or the whole lane is theatre."""
    ctx = _ctx()
    ok, _, f = an.pure_price(_row(), ctx)
    assert ok
    p = tmp_path / "aaa_log.md"
    p.write_text("# AAA — Decision Log\n\n## 2026-09-01 — Pipeline run (auto)\n\n"
                 "**Decision:** _[pending annotation]_\n")
    an.prepend_entry(p, an.render_entry(ctx, f))
    body = p.read_text()
    assert body.index("## 2026-09-16") < body.index("## 2026-09-01"), "newest-first broken"
    assert "# AAA — Decision Log" in body
    assert drift_gate.decision_log_annotated_since("AAA", "2026-09-11T20:00:00Z", tmp_path)


def test_the_first_sentence_survives_the_cause_composer(tmp_path):
    """promote.compose_cause builds the ratified baseline's cause from the first sentence of
    each explained row, cut at the first '. ' — a decimal must not truncate it mid-number."""
    ctx = _ctx()
    ok, _, f = an.pure_price(_row(), ctx)
    assert ok
    an.prepend_entry(tmp_path / "aaa_log.md", an.render_entry(ctx, f))
    got = promote._first_decision_sentence("AAA", tmp_path)
    assert got.startswith("AAA tape-only: EV") and got.endswith("fv held 16.32.")
    assert "16.32" in got and len(got) < 200


def test_the_marker_is_stable_for_the_same_run_and_row():
    ctx = _ctx()
    ok, _, f = an.pure_price(_row(), ctx)
    assert ok
    assert an.marker(ctx, f) == an.marker(ctx, f)
    assert "ticker=AAA" in an.marker(ctx, f) and ctx.anchor_commit in an.marker(ctx, f)


def test_the_cause_sentence_names_a_band_flip():
    """The ratify cause is the only place a reader sees what the anchor absorbed. When the owner
    ruled 2026-09-18 that the executor may annotate and land the tape itself, the named cost was
    that an away-from-BUY flip would be absorbed unread — so a flipped row says so in the cause.
    TRMD is the live case: BUY -> TRIM/SHORT on 9/17-9/18 tape, fair value held to the cent."""
    flat = {"ticker": "DHT", "ev_from": -26.8, "ev_to": -29.3, "fv": 16.32, "flipped": False,
            "band_from": "TRIM/SHORT (overvalued)", "band_to": "TRIM/SHORT (overvalued)"}
    flip = {"ticker": "TRMD", "ev_from": 6.6, "ev_to": -6.0, "fv": 35.14, "flipped": True,
            "band_from": "BUY (undervalued)", "band_to": "TRIM/SHORT (overvalued)"}
    assert an.first_sentence(flat) == "DHT tape-only: EV -26.8->-29.3pp, fv held 16.32."
    s = an.first_sentence(flip)
    assert s == "TRMD tape-only: band BUY -> TRIM/SHORT, EV +6.6->-6.0pp, fv held 35.14."
    # promote.compose_cause cuts each row at the first ". " — the band must survive that cut
    assert ". " not in s[:-1]


def test_the_determinant_exclusion_list_has_exactly_one_definition():
    """Two surfaces assumed to agree need a TEST that they agree (2026-07-02). THREE readers
    measure this window — the annotator's price-leg proof, the land lane's (e), and the cron's
    regen trigger — and they must agree, or a morning the promoter calls contaminated is one the
    annotator calls pure (2026-09-18: a shadow build's *.yaml.draft froze (e) for a day while
    the annotator ignored it, because only two of the three shared a definition)."""
    import inspect
    from pathlib import Path as _P

    assert "promote.determinant_paths" in inspect.getsource(an.determinant_changes), \
        "the annotator built its own copy of the list"
    assert "determinant_paths" in inspect.getsource(promote._surface_matches_head)
    cron = (_P(__file__).resolve().parents[1] / "scripts" / "sentinel_cron.sh").read_text()
    assert "crude_tanker_fv.promote determinants" in cron, \
        "the cron's regen trigger hand-copied the list instead of asking promote"
    assert ":(exclude)inputs/filings" not in cron, "a third copy of the exclusion list is back"
    for p in ("inputs/forks.yaml", "inputs/filings", "inputs/earnings_calendar.yaml"):
        assert f":(exclude){p}" in promote.DETERMINANT_EXCLUDES
    for p in ("inputs/market_data/prices_daily.yaml", "inputs/watchlist.yaml", "src"):
        assert f":(exclude){p}" not in promote.DETERMINANT_EXCLUDES


def test_drafts_and_the_scan_cursor_are_not_determinants_for_any_reader():
    """A shadow-build draft and the sp_scan cursor feed no valuation, so neither may freeze (e),
    refuse the annotator, or trigger a regen (2026-09-18)."""
    assert promote.is_non_determinant("inputs/balance_sheets/ten_2026-Q2.yaml.draft")
    assert promote.is_non_determinant("inputs/fleet_manifests/ten.yaml.draft")
    assert promote.is_non_determinant("inputs/market_data/transactions/_scan_state.json")
    assert not promote.is_non_determinant("inputs/balance_sheets/ten_2026-Q2.yaml")
    assert not promote.is_non_determinant("inputs/market_data/prices_daily.yaml")
    assert not promote.is_non_determinant("src/crude_tanker_fv/nav.py")
