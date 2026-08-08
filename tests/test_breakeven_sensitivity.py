"""Breakeven and sensitivity tests (METHODOLOGY.md sections 3.3-3.4)."""

from dataclasses import replace

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
import pytest

from crude_tanker_fv.blend import blend_fair_value
from crude_tanker_fv.breakeven import implied_breakeven_tce
from crude_tanker_fv.cycle import compute_cycle
from crude_tanker_fv.dividend_strip import compute_dividend_strip
from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.sensitivity import compute_sensitivity


def _fv_at_mult(ci, mult):
    scaled = {cls: [r * mult for r in c] for cls, c in ci.market_data.ffa_forward_curve.items()}
    shocked = replace(ci, market_data=replace(ci.market_data, ffa_forward_curve=scaled))
    nav = compute_nav(shocked)
    cycle = compute_cycle(ci)
    strip = compute_dividend_strip(
        shocked, nav.nav_per_share, terminal_multiple=cycle.terminal_multiple
    )
    return blend_fair_value(nav, strip, cycle).fair_value_per_share


def test_breakeven_round_trips_to_price():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    price = 16.35
    be = implied_breakeven_tce(ci, price)
    # FV evaluated at the solved forward multiplier must reproduce the price.
    assert _fv_at_mult(ci, be.multiplier) == pytest.approx(price, abs=0.01)
    # Single-class name: blended breakeven == the VLCC per-class breakeven == m × forward.
    assert be.blended_breakeven_tce == pytest.approx(be.implied_breakeven_tce["VLCC"])
    assert be.implied_breakeven_tce["VLCC"] == pytest.approx(be.multiplier * be.ffa_12m["VLCC"])


def test_breakeven_above_mean():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    be = implied_breakeven_tce(ci, 16.35)
    x = be.blended_breakeven_tce
    assert x > be.blended_mean_tce              # pricing extended peak vs the 10-yr mean
    assert be.multiplier < 1.5                  # within ~1.5x of the current forward


def test_breakeven_increases_with_price():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    low = implied_breakeven_tce(ci, 14.00).blended_breakeven_tce
    high = implied_breakeven_tce(ci, 18.00).blended_breakeven_tce
    assert high > low


def test_breakeven_degenerate_is_exact_zero():
    """Price below NAV-alone coverage pins the bisection at the lower bound.

    The result must be an EXACT zero — not the 50/2^101 ≈ 2e-29 residue, which
    rendered as 29-digit Assumed/Breakeven ratios in six committed scenario
    docs and leaked last-ULP float noise into regeneration diffs (external
    audit 2026-07-02, F-3/F-10).
    """
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    be = implied_breakeven_tce(ci, 1.00)
    assert be.multiplier == 0.0
    assert be.blended_breakeven_tce == 0.0
    assert all(v == 0.0 for v in be.implied_breakeven_tce.values())


def test_degenerate_scenario_doc_renders_na_ratio():
    """A NAV-covered name's scenario doc renders 'n/a', never a giant ratio."""
    import re

    from crude_tanker_fv.scenarios import (
        load_scenarios, render_scenario_markdown, run_scenarios,
    )

    ci = load_company_inputs("DHT", BOOK_QUARTER)
    doc = load_scenarios(sector="crude")
    report = run_scenarios(ci, 1.00, 1.00, doc)
    assert report.breakeven_tce == 0.0
    text = render_scenario_markdown(report)
    assert "price justified by NAV alone" in text
    assert "| n/a |" in text
    # No rendered Assumed/Breakeven ratio may exceed 100x (plausibility bound).
    for m in re.finditer(r"([\d,]+\.\d{2})×", text):
        assert float(m.group(1).replace(",", "")) <= 100.0, m.group(0)


def test_sensitivity_grid_shape_and_base():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    grid = compute_sensitivity(ci, 16.35)
    assert len(grid.grid) == 5 and all(len(r) == 5 for r in grid.grid)
    # Base cell (0% TCE, 0% vessel) must equal the unshocked blended FV.
    nav = compute_nav(ci)
    cycle = compute_cycle(ci)
    strip = compute_dividend_strip(
        ci, nav.nav_per_share, terminal_multiple=cycle.terminal_multiple
    )
    base_fv = blend_fair_value(nav, strip, cycle).fair_value_per_share
    assert grid.grid[2][2] == pytest.approx(base_fv)


def test_sensitivity_monotonic_both_axes():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    g = compute_sensitivity(ci, 16.35).grid
    for row in g:                                   # increasing along vessel-value axis
        assert all(row[j] < row[j + 1] for j in range(4))
    for j in range(5):                              # increasing along TCE axis
        col = [g[i][j] for i in range(5)]
        assert all(col[i] < col[i + 1] for i in range(4))


def test_vessel_value_dominates_tce():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    g = compute_sensitivity(ci, 16.35).grid
    vessel_span = g[2][4] - g[2][0]   # +/-20% vessel at base TCE
    tce_span = g[4][2] - g[0][2]      # +/-30% TCE at base vessel
    assert vessel_span > tce_span     # NAV/asset lever dominates at peak weighting
