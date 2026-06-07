"""Broker-NAV mark-premium sweep tests (METHODOLOGY.md sections 3.1, 9)."""

import pytest

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.marks import scale_vessel_marks, solve_broker_premium
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
    # Pure-plays: tool marks already reconcile to broker -> ~zero spread.
    for t in ("DHT", "FRO", "ECO"):
        assert by[t].k_broker == pytest.approx(1.0, abs=0.05)
        assert abs(by[t].spread) < 5
    # INSW: marks uncertain -> wide spread, EV materially better at broker marks.
    assert by["INSW"].k_broker > 1.3
    assert by["INSW"].spread > 15
    assert by["INSW"].ev_broker > by["INSW"].ev_tool
    assert (tmp_path / "broker_nav_sweep.md").exists()
    assert (tmp_path / "broker_nav_sweep.xlsx").exists()
