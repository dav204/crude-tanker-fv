"""Regression + gate for the committed drift gate (drift_gate.py / Phase 2).

Three layers:
  1. Deterministic logic — synthetic baseline/state dicts exercise every
     breach path (EV% / NAV / band / k second-difference), the APPROX
     self-consistency carve-out, and the decision-log annotation escape hatch.
  2. Committed-baseline integrity — the tracked
     baselines/reconcile_baseline.yaml parses, covers the live state, and its
     APPROX flags are single-sourced from reconcile.
  3. Live gate — the actual gate the verification loop runs: current outputs vs
     the committed baseline must carry no UNEXPLAINED drift (skips when the
     pipeline snapshot is missing or stale, same as test_reconcile).
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import pytest

from crude_tanker_fv import drift_gate, reconcile

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "state" / "last_run.json"
STALE_AFTER_HOURS = 24

RATIFIED_AT = "2026-03-01T00:00:00+00:00"


# --------------------------------------------------------------------------- #
# synthetic-fixture helpers
# --------------------------------------------------------------------------- #

def _ticker(ev=-10.0, nav=20.0, k=1.20, pos="HOLD (fairly valued)", sector="crude"):
    return {"ev_pct": ev, "nav_per_share": nav, "k_broker": k,
            "position": pos, "sector": sector}


def _state(tickers, run_at=RATIFIED_AT):
    return {"run_at": run_at, "quarter": "2026-Q1", "tickers": tickers}


def _baseline_from(state):
    return drift_gate.build_baseline(state, cause="test", ratified_commit="deadbee")


def _row(rows, ticker):
    return next(r for r in rows if r.ticker == ticker)


# --------------------------------------------------------------------------- #
# 1. deterministic logic
# --------------------------------------------------------------------------- #

def test_build_baseline_shape():
    state = _state({"DHT": _ticker(), "NAT": _ticker(k=2.16)})
    b = drift_gate.build_baseline(state, cause="why", ratified_commit="abc1234")
    assert b["meta"]["ratified_at"] == RATIFIED_AT
    assert b["meta"]["ratified_commit"] == "abc1234"
    assert b["meta"]["cause"] == "why"
    assert b["thresholds"]["ev_pct_pp"] == 2.0
    assert b["names"]["DHT"]["pnav_basis"] == "pareto"
    assert b["names"]["NAT"]["pnav_basis"] == "approx"  # single-sourced from reconcile


def test_stable_run_no_breach(tmp_path):
    state = _state({"DHT": _ticker(), "FRO": _ticker(ev=-29.0, k=1.27)})
    rows = drift_gate.evaluate(_baseline_from(state), state, decisions_dir=tmp_path)
    assert all(r.status == "stable" for r in rows)
    assert not drift_gate.unexplained(rows)


def test_ev_move_is_unexplained_without_annotation(tmp_path):
    base_state = _state({"DHT": _ticker(ev=-21.0)})
    baseline = _baseline_from(base_state)
    moved = _state({"DHT": _ticker(ev=-17.0)})  # +4pp
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "UNEXPLAINED"
    assert "EV%" in r.breaches


def test_sub_threshold_ev_move_is_stable(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(ev=-21.0)}))
    moved = _state({"DHT": _ticker(ev=-19.5)})  # +1.5pp < 2pp
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "stable"


def test_nav_move_breaches(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(nav=20.0)}))
    moved = _state({"DHT": _ticker(nav=21.0)})  # +5%
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "UNEXPLAINED" and "NAV" in r.breaches


def test_band_flip_breaches(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(pos="TRIM/SHORT (overvalued)")}))
    moved = _state({"DHT": _ticker(pos="BUY (undervalued)")})
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "UNEXPLAINED" and "band" in r.breaches


def test_k_broker_second_difference(tmp_path):
    """k is gated on its CHANGE, not its level: a high but stable k stays green;
    only a move beyond the Δk bar trips it (never 'get closer to Pareto')."""
    # High, stable level — green.
    baseline = _baseline_from(_state({"INSW": _ticker(k=1.64)}))
    same = _state({"INSW": _ticker(k=1.64)})
    assert _row(drift_gate.evaluate(baseline, same, decisions_dir=tmp_path), "INSW").status == "stable"
    # Sub-threshold change — green.
    small = _state({"INSW": _ticker(k=1.68)})  # +0.04 < 0.05
    assert _row(drift_gate.evaluate(baseline, small, decisions_dir=tmp_path), "INSW").status == "stable"
    # Over-threshold change — breaches.
    big = _state({"INSW": _ticker(k=1.72)})  # +0.08 > 0.05
    r = _row(drift_gate.evaluate(baseline, big, decisions_dir=tmp_path), "INSW")
    assert r.status == "UNEXPLAINED" and "k_broker" in r.breaches


def test_approx_name_skips_k_gate_but_tracks_self_consistency(tmp_path):
    # NAT is APPROX: a big k swing does NOT breach (no real broker anchor)...
    baseline = _baseline_from(_state({"NAT": _ticker(ev=-52.0, k=2.16)}))
    k_only = _state({"NAT": _ticker(ev=-52.0, k=2.60)})  # huge Δk, ev unchanged
    assert _row(drift_gate.evaluate(baseline, k_only, decisions_dir=tmp_path), "NAT").status == "stable"
    # ...but its own EV% is still tracked.
    ev_moved = _state({"NAT": _ticker(ev=-48.0, k=2.16)})
    r = _row(drift_gate.evaluate(baseline, ev_moved, decisions_dir=tmp_path), "NAT")
    assert r.status == "UNEXPLAINED" and "EV%" in r.breaches and "k_broker" not in r.breaches


def _write_log(decisions_dir: Path, ticker: str, body: str):
    decisions_dir.mkdir(parents=True, exist_ok=True)
    (decisions_dir / f"{ticker.lower()}_log.md").write_text(body)


def test_human_dated_header_after_ratify_clears_breach(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(ev=-21.0)}))
    moved = _state({"DHT": _ticker(ev=-15.0)})
    _write_log(tmp_path, "DHT",
               "## 2026-04-01 — market move: VLCC tape +20% on Hormuz risk\n\nNAV up.\n")
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "explained" and r.annotated


def test_auto_entry_does_not_clear_breach(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(ev=-21.0)}))
    moved = _state({"DHT": _ticker(ev=-15.0)})
    _write_log(tmp_path, "DHT",
               "## 2026-04-01T08:00:00+00:00 — Pipeline run (auto)\n\n"
               "**Decision:** _[pending annotation]_\n")
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "UNEXPLAINED"


def test_filled_decision_line_under_auto_header_clears(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(ev=-21.0)}))
    moved = _state({"DHT": _ticker(ev=-15.0)})
    _write_log(tmp_path, "DHT",
               "## 2026-04-01T08:00:00+00:00 — Pipeline run (auto)\n\n"
               "**Decision:** Q2 refresh — fleet +2 VLCC, NAV rerated; accepted.\n")
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "explained"


def test_annotation_before_ratify_is_ignored(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(ev=-21.0)}))  # ratified 2026-03-01
    moved = _state({"DHT": _ticker(ev=-15.0)})
    _write_log(tmp_path, "DHT",
               "## 2026-01-15 — old note that predates the baseline window\n")
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "UNEXPLAINED"


def test_stale_annotation_under_fresh_auto_entry_does_not_clear(tmp_path):
    """Closed auto-explain hole (X9): a real annotation under an OLDER entry must
    NOT bless a fresh move once the pipeline prepends a new placeholder entry on
    top. Only the most-recent entry counts — the pipeline cannot self-explain."""
    baseline = _baseline_from(_state({"DHT": _ticker(ev=-21.0)}))  # ratified 2026-03-01
    moved = _state({"DHT": _ticker(ev=-15.0)})
    _write_log(tmp_path, "DHT",
               "## 2026-04-02T08:00:00+00:00 — Pipeline run (auto)\n\n"
               "**Decision:** _[pending annotation]_\n\n"
               "---\n\n"
               "## 2026-04-01 — real human note for a PRIOR move\n\n"
               "**Decision:** accepted the prior NAV rerate.\n")
    r = _row(drift_gate.evaluate(baseline, moved, decisions_dir=tmp_path), "DHT")
    assert r.status == "UNEXPLAINED"  # fresh placeholder on top ⇒ not explained


def test_new_and_missing_names_report_not_fail(tmp_path):
    baseline = _baseline_from(_state({"DHT": _ticker(), "FRO": _ticker()}))
    # state drops FRO (missing) and adds GNK (new)
    state = _state({"DHT": _ticker(), "GNK": _ticker(sector="dry_bulk")})
    rows = drift_gate.evaluate(baseline, state, decisions_dir=tmp_path)
    assert _row(rows, "FRO").status == "missing"
    assert _row(rows, "GNK").status == "new"
    assert not drift_gate.unexplained(rows)  # neither fails the gate


# --------------------------------------------------------------------------- #
# 2. committed-baseline integrity
# --------------------------------------------------------------------------- #

def test_committed_baseline_parses_and_well_formed():
    b = drift_gate.load_baseline()
    for key in ("ratified_at", "ratified_commit", "quarter", "cause"):
        assert b["meta"].get(key), f"baseline meta missing {key}"
    for key in ("ev_pct_pp", "nav_pct", "k_broker_delta"):
        assert key in b["thresholds"]
    assert b["names"], "committed baseline has no names"


def test_committed_baseline_approx_flags_single_sourced():
    b = drift_gate.load_baseline()
    for ticker, rec in b["names"].items():
        expected = "approx" if ticker in reconcile.APPROX_PNAV_TICKERS else "pareto"
        assert rec["pnav_basis"] == expected, f"{ticker} basis drifted from reconcile set"


@pytest.mark.skipif(not STATE_PATH.exists(),
                    reason="no pipeline state — baseline-vs-state coverage skipped")
def test_committed_baseline_covers_live_state():
    b = drift_gate.load_baseline()
    state = drift_gate.load_state()
    uncovered = [t for t in state.get("tickers", {}) if t not in b["names"]]
    assert not uncovered, (
        f"names in state but not the baseline: {uncovered}. "
        f"Onboard then re-ratify: scripts/ratify_baseline.sh \"add {uncovered}\"."
    )


# --------------------------------------------------------------------------- #
# 3. live gate
# --------------------------------------------------------------------------- #

def _state_is_fresh() -> bool:
    if not STATE_PATH.exists():
        return False
    raw = json.loads(STATE_PATH.read_text())
    run_at = raw.get("run_at")
    if not run_at:
        return False
    when = dt.datetime.fromisoformat(run_at.replace("Z", "+00:00"))
    return (dt.datetime.now(dt.timezone.utc) - when).total_seconds() <= STALE_AFTER_HOURS * 3600


@pytest.mark.skipif(not _state_is_fresh(),
                    reason=f"state/last_run.json missing or >{STALE_AFTER_HOURS}h old "
                           f"— live drift gate skipped (run the pipeline to enable it).")
def test_live_drift_gate_no_unexplained_drift():
    rows = drift_gate.evaluate(drift_gate.load_baseline(), drift_gate.load_state())
    bad = drift_gate.unexplained(rows)
    assert not bad, (
        "UNEXPLAINED drift vs committed baseline for: "
        + ", ".join(f"{r.ticker}({'/'.join(r.breaches)})" for r in bad)
        + ". Annotate decisions/<ticker>_log.md with the cause, or re-ratify the "
        "baseline if the move is accepted: scripts/ratify_baseline.sh \"<cause>\"."
    )
