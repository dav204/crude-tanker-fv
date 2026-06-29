"""Tests for the justified-P/NAV diagnostic (METHODOLOGY §17)."""

from __future__ import annotations

from pathlib import Path

import pytest

from crude_tanker_fv.justified_pnav import (
    DEFAULT_G,
    JustifiedPnavRow,
    _g_by_sector,
    compute_justified_pnav_rows,
    evaluate,
    justified_pnav,
    justified_pnav_resid,
    normalized_annual_eps,
    ronav_implied,
    run_justified_pnav_xref,
    subsector_median_pnav,
    write_justified_pnav,
)
from crude_tanker_fv.loaders import INPUTS_DIR, load_company_inputs, load_watchlist
from crude_tanker_fv.nav import COST_OF_EQUITY, compute_nav

QUARTER = "2026-Q1"
R = COST_OF_EQUITY  # 0.11


# ---------------------------------------------------------------------------
# Pure formula
# ---------------------------------------------------------------------------
def test_both_forms_agree():
    for ronav in (0.05, 0.08, 0.11, 0.14, 0.20, 0.30):
        for g in (0.0, 0.01, 0.02, 0.03):
            assert justified_pnav(ronav, R, g) == pytest.approx(
                justified_pnav_resid(ronav, R, g)
            )


def test_validator_known_inputs():
    # (0.14 - 0.01) / (0.11 - 0.01) = 0.13 / 0.10 = 1.30
    assert justified_pnav(0.14, 0.11, 0.01) == pytest.approx(1.30)
    nav = 20.0
    assert justified_pnav(0.14, 0.11, 0.01) * nav == pytest.approx(26.0)  # justified FV/sh


def test_round_trip_implied_recovers_market_pnav():
    # Plug RONAV_implied back in as RONAV_norm -> recover P/NAV(mkt) = price/nav.
    for price, nav, g in [(6.39, 10.14, 0.01), (40.0, 28.0, 0.02), (10.0, 25.0, 0.0)]:
        ri = ronav_implied(price, nav, R, g)
        assert justified_pnav(ri, R, g) == pytest.approx(price / nav)


# ---------------------------------------------------------------------------
# Guards (pure evaluate())
# ---------------------------------------------------------------------------
def _ev(**kw):
    base = dict(
        nav=20.0, price=14.0, eps=2.0, missing_anchor=False,
        has_cost=True, newbuild_share=0.0, r=R, g=0.01,
    )
    base.update(kw)
    return evaluate(**base)


def test_guard_non_positive_nav():
    ev = _ev(nav=-1.0)
    assert ev.flag == "non-positive NAV"
    assert ev.justified_pnav is None and ev.pnav_mkt is None


def test_guard_no_cost():
    ev = _ev(has_cost=False)
    assert ev.flag == "no cost data" and ev.justified_pnav is None


def test_guard_r_le_g():
    ev = _ev(g=0.11)  # r - g == 0
    assert ev.flag == "r≤g (invalid)"
    assert ev.justified_pnav is None and ev.ronav_implied is None


def test_guard_missing_anchor():
    ev = _ev(eps=None, missing_anchor=True)
    assert ev.flag == "no anchor" and ev.justified_pnav is None


def test_guard_negative_mid_cycle_eps():
    ev = _ev(eps=-3.0)
    assert ev.flag == "negative mid-cycle EPS"
    assert ev.ronav_norm == pytest.approx(-3.0 / 20.0)  # shown, but no multiple
    assert ev.justified_pnav is None


def test_guard_sub_growth():
    # eps/nav = 0.1/20 = 0.005 < g (0.01)
    ev = _ev(eps=0.1, g=0.01)
    assert ev.flag == "sub-growth returns" and ev.justified_pnav is None


def test_guard_newbuild_heavy_keeps_ronav_drops_multiple():
    ev = _ev(newbuild_share=0.50, eps=2.0)
    assert ev.flag == "newbuild-heavy (unreliable)"
    assert ev.ronav_norm == pytest.approx(0.10)   # 2.0 / 20.0 shown
    assert ev.justified_pnav is None              # but no multiple


def test_evaluate_valid_matches_formula():
    ev = _ev(eps=2.8, nav=20.0, price=14.0, g=0.01)   # ronav 0.14
    assert ev.flag is None
    assert ev.ronav_norm == pytest.approx(0.14)
    assert ev.justified_pnav == pytest.approx(1.30)
    assert ev.justified_fv == pytest.approx(26.0)
    assert ev.pnav_mkt == pytest.approx(0.70)
    assert ev.gap == pytest.approx(0.14 - ronav_implied(14.0, 20.0, R, 0.01))


# ---------------------------------------------------------------------------
# Read label
# ---------------------------------------------------------------------------
def _row(justified, pnav_mkt, flag=None):
    return JustifiedPnavRow(
        ticker="X", hybrid=False, sector="crude", nav_per_share=20.0, price=14.0,
        pnav_mkt=pnav_mkt, ronav_norm=0.1, r=R, g=0.01, justified_pnav=justified,
        justified_fv=None, ronav_implied=0.09, gap=0.01, flag=flag,
    )


def test_read_label_cheap_fair_rich():
    assert _row(1.30, 1.00).read == "cheap"   # justified >> mkt
    assert _row(0.70, 1.00).read == "rich"     # justified << mkt
    assert _row(1.05, 1.00).read == "fair"     # within ±10%
    assert _row(0.92, 1.00).read == "fair"


def test_read_label_flag_short_circuits():
    assert _row(None, 1.00, flag="newbuild-heavy (unreliable)").read == "newbuild-heavy (unreliable)"


# ---------------------------------------------------------------------------
# YAML wiring
# ---------------------------------------------------------------------------
def test_g_loaded_from_yaml():
    g = _g_by_sector(INPUTS_DIR)
    assert g["crude"] == pytest.approx(0.01)
    assert g["product"] == pytest.approx(0.01)
    assert g["dry_bulk"] == pytest.approx(0.01)
    assert g["lng"] == pytest.approx(0.02)
    assert g["containerships"] == pytest.approx(0.015)


def test_rows_use_sector_g():
    rows = {r.ticker: r for r in compute_justified_pnav_rows(QUARTER)}
    assert rows["FLNG"].g == pytest.approx(0.02)   # lng
    assert rows["DHT"].g == pytest.approx(0.01)     # crude
    assert rows["GSL"].g == pytest.approx(0.015)    # containerships


# ---------------------------------------------------------------------------
# Normalized EPS uses anchors, not the FFA front end
# ---------------------------------------------------------------------------
def test_normalized_eps_differs_from_ntm_strip():
    # The normalized (anchor) EPS must NOT equal the FFA-front-end NTM EPS that
    # consensus_eps uses — that's the whole point (anchors, not the hot number).
    from crude_tanker_fv.dividend_strip import compute_dividend_strip
    ci = load_company_inputs("DHT", QUARTER)
    nav = compute_nav(ci).nav_per_share
    eps_norm, missing = normalized_annual_eps(ci, nav)
    assert not missing and eps_norm is not None
    ntm = sum(compute_dividend_strip(ci, nav).eps_by_quarter[:4])
    assert eps_norm != pytest.approx(ntm)  # near a peak the FFA front end runs hotter


def test_normalized_eps_flags_missing_anchor():
    from dataclasses import replace
    ci = load_company_inputs("DHT", QUARTER)
    nav = compute_nav(ci).nav_per_share
    cls = next(iter({v.cls for v in ci.fleet.vessels}))
    stripped = {k: v for k, v in ci.market_data.historical_tce_means.items() if k != cls}
    ci2 = replace(ci, market_data=replace(ci.market_data, historical_tce_means=stripped))
    eps, missing = normalized_annual_eps(ci2, nav)
    assert eps is None and cls in missing


# ---------------------------------------------------------------------------
# Real-watchlist behaviour
# ---------------------------------------------------------------------------
def test_coverage_independence_covers_approx_names():
    rows = compute_justified_pnav_rows(QUARTER)
    tickers = {r.ticker for r in rows}
    valued = {t for t, e in load_watchlist().items()
              if e.get("current_price") and e.get("analyst_target")}
    # Every valued name produces a row that loaded (no consensus_pnav/fwd_pe gate).
    assert tickers.issubset(valued)
    assert len(rows) >= 20
    # APPROX / no-Pareto names — the ones this leg exists to benchmark — are present.
    for t in ("SB", "CMDB", "GSL", "MPCC", "NAT", "CCEC"):
        assert t in tickers


def test_hybrids_flagged_whole_company():
    rows = {r.ticker: r for r in compute_justified_pnav_rows(QUARTER)}
    for t in ("INSW", "TEN", "CMBT"):
        assert rows[t].hybrid is True
    assert rows["DHT"].hybrid is False


def test_newbuild_heavy_flagged():
    rows = {r.ticker: r for r in compute_justified_pnav_rows(QUARTER)}
    for t in ("BRUT", "CAPT", "MPCC"):
        assert rows[t].flag == "newbuild-heavy (unreliable)"
        assert rows[t].justified_pnav is None
    # A flagship with a sub-threshold (~17%) program still computes.
    assert rows["FRO"].flag is None and rows["FRO"].justified_pnav is not None


def test_high_ronav_prints_above_one_low_below_one():
    rows = {r.ticker: r for r in compute_justified_pnav_rows(QUARTER)}
    # FLNG earns well above cost of equity on NAV -> justified P/NAV > 1.
    assert rows["FLNG"].justified_pnav > 1.0
    # ECO earns below cost of equity on its (high) NAV -> justified P/NAV < 1.
    assert rows["ECO"].justified_pnav < 1.0


def test_subsector_medians_present_and_lng_above_crude():
    rows = compute_justified_pnav_rows(QUARTER)
    med = subsector_median_pnav(rows)
    for s in ("crude", "product", "lng", "dry_bulk", "containerships"):
        assert s in med and med[s] > 0
    # LNG (secular demand, higher g + strong RONAV) ranks above crude tankers.
    assert med["lng"] > med["crude"]


def test_sb_worked_example_identity():
    rows = {r.ticker: r for r in compute_justified_pnav_rows(QUARTER)}
    sb = rows["SB"]
    # NAV is the PRODUCTION transaction-anchored mark (§9.9) — the same basis every
    # other surface uses. SB's dry-bulk classes recalibrate UP, landing ~$10.14 (vs
    # the un-anchored $9.48 the prior test wrongly pinned). The row carries it.
    nav = sb.nav_per_share
    assert 9.5 < nav < 11.0                        # ~$10.14, marked above book (~$7.30), §11.7.10
    assert sb.price == pytest.approx(6.39)
    # The market prices SB's fleet to earn RONAV_implied on NAV through cycle.
    assert sb.ronav_implied == pytest.approx(0.01 + (sb.price / nav) * (R - 0.01))
    assert sb.pnav_mkt == pytest.approx(sb.price / nav)
    assert sb.pnav_mkt == pytest.approx(0.630, abs=0.02)   # 6.39 / 10.14
    # At g=0.01 the worked example lands ~7.3% — the brief's number, now reproduced
    # on the anchored NAV (the test pins the identity, not the moving dollar NAV).
    assert sb.ronav_implied == pytest.approx(0.073, abs=0.005)
    # RONAV_norm exceeds implied -> SB is cheap vs justified.
    assert sb.ronav_norm > sb.ronav_implied and sb.read == "cheap"


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def test_writer_emits_md_and_xlsx(tmp_path: Path):
    rows = compute_justified_pnav_rows(QUARTER)
    write_justified_pnav(rows, outputs_dir=tmp_path)
    md = tmp_path / "justified_pnav.md"
    xlsx = tmp_path / "justified_pnav.xlsx"
    assert md.exists() and xlsx.exists()
    text = md.read_text()
    assert "Justified P/NAV diagnostic" in text
    assert "Subsector vector" in text
    assert "Sensitivity grids" in text  # the mandatory hypersensitivity grid


def test_run_returns_rows(tmp_path: Path):
    rows = run_justified_pnav_xref(QUARTER, outputs_dir=tmp_path)
    assert rows
    assert all(isinstance(r, JustifiedPnavRow) for r in rows)
