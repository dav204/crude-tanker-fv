"""Broker-NAV mark-premium sweep tests (METHODOLOGY.md sections 3.1, 9)."""

import pytest

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.marks import (TXN_PURE_PLAY_K_BAND,
                                   TXN_PURE_PLAY_K_UNIFORMITY,
                                   scale_vessel_marks, solve_broker_premium)
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.pipeline import run_broker_sweep


def test_scale_marks_identity_and_monotone():
    ci = load_company_inputs("DHT", "2026-Q1")
    base = compute_nav(ci).nav_per_share
    assert compute_nav(scale_vessel_marks(ci, 1.0)).nav_per_share == pytest.approx(base)
    up = compute_nav(scale_vessel_marks(ci, 1.20)).nav_per_share
    down = compute_nav(scale_vessel_marks(ci, 0.80)).nav_per_share
    assert down < base < up


def test_solve_broker_premium_round_trips():
    ci = load_company_inputs("INSW", "2026-Q1")
    target = 79.18  # INSW broker NAV (76.80 / 0.97)
    k = solve_broker_premium(ci, target)
    assert compute_nav(scale_vessel_marks(ci, k)).nav_per_share == pytest.approx(target, abs=0.05)
    assert k > 1.3  # INSW tool NAV sits well below broker -> large premium


def test_broker_sweep_discriminates_hybrid(tmp_path):
    rows = run_broker_sweep("2026-Q1", outputs_dir=tmp_path)
    by = {r.ticker: r for r in rows}
    # Since 2026-06-09 tool marks = transaction-anchored marks (default-on), so
    # k_broker measures the broker premium over transaction-validated levels.
    # Validated crude pure-plays carry a tight, UNIFORM premium (~1.12-1.14 at
    # the Jun-2026 fit) — the discrimination signal is consistency across them,
    # not a zero premium.
    pure_ks = [by[t].k_broker for t in ("DHT", "FRO", "ECO")]
    lo, hi = TXN_PURE_PLAY_K_BAND
    for k in pure_ks:
        assert lo < k < hi
    assert max(pure_ks) - min(pure_ks) < TXN_PURE_PLAY_K_UNIFORMITY
    # INSW: marks uncertain (hybrid carve-out) -> premium far above the
    # pure-play band ceiling (1.25; INSW 1.52 at the Jun-2026 static),
    # wide spread, EV materially better at broker marks.
    assert by["INSW"].k_broker > 1.4
    assert by["INSW"].spread > 25
    assert by["INSW"].ev_broker > by["INSW"].ev_tool
    assert (tmp_path / "broker_nav_sweep.md").exists()
    assert (tmp_path / "broker_nav_sweep.xlsx").exists()
    # B4 (2026-06-12): the rendered sweep must carry the two-regime band
    # language and must NOT claim the retired pre-flip "k ≈ 1.0 = validated"
    # reading as current semantics.
    md = (tmp_path / "broker_nav_sweep.md").read_text()
    assert f"{lo:.2f}-{hi:.2f}" in md
    assert "two-regime" in md
    assert "k_broker ≈ 1.0 ⇒ tool marks already reconcile to broker" not in md
    assert "| mark-driven |" not in md          # Read column is mechanical now
    assert "wide-spread" in md or "narrow-spread" in md
