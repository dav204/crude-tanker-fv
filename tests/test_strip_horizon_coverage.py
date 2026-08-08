"""A1 strip_horizon parameterization + §11.8.6 coverage_schedule blend."""

from dataclasses import replace

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
import pytest

from crude_tanker_fv.dividend_strip import compute_dividend_strip
from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.scenarios import QUARTER_KEYS, quarter_keys


def test_quarter_keys_extends_the_q3_2026_convention():
    assert quarter_keys(8) == QUARTER_KEYS
    assert quarter_keys(10) == QUARTER_KEYS + ["q3_2028", "q4_2028"]
    assert quarter_keys(12)[-1] == "q2_2029"


def test_default_horizon_is_unchanged_8q():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    nav = compute_nav(ci)
    default = compute_dividend_strip(ci, nav.nav_per_share)
    explicit = compute_dividend_strip(ci, nav.nav_per_share, strip_horizon=8)
    assert len(default.dps_by_quarter) == 8
    assert default.implied_price == pytest.approx(explicit.implied_price)


def test_static_coverage_schedule_reproduces_spot_pct_blend():
    # A coverage_schedule pinned at (1 - spot_pct) must be EXACTLY the
    # pre-§11.8 static blend — the generalization's zero-drift property.
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    nav = compute_nav(ci)
    base = compute_dividend_strip(ci, nav.nav_per_share)
    classes = {v.cls for v in ci.fleet.vessels}
    schedule = {
        cls: [1.0 - ci.fleet.spot_coverage_pct.get(cls, 1.0)] * 8 for cls in classes
    }
    ci2 = replace(ci, fleet=replace(ci.fleet, coverage_schedule=schedule))
    withsched = compute_dividend_strip(ci2, nav.nav_per_share)
    assert withsched.implied_price == pytest.approx(base.implied_price)
    assert withsched.dps_by_quarter == pytest.approx(base.dps_by_quarter)


def test_decaying_coverage_blends_each_quarter_independently():
    # FLNG (TC-heavy, disclosed LNGC charter avg above the curve's back end).
    # Covered quarters earn the contracted rate; as cov_q decays, each
    # quarter's blended TCE slides toward that quarter's curve value.
    # (FLNG's DPS is fixed-only, so assert at the TCE level, not NPV.)
    ci = load_company_inputs("FLNG", "2026-Q1")
    nav = compute_nav(ci)
    classes = {v.cls for v in ci.fleet.vessels}
    full = {cls: [1.0] * 8 for cls in classes}
    decaying = {cls: [1.0, 1.0, 0.75, 0.75, 0.5, 0.5, 0.25, 0.0] for cls in classes}
    ci_full = replace(ci, fleet=replace(ci.fleet, coverage_schedule=full))
    ci_dec = replace(ci, fleet=replace(ci.fleet, coverage_schedule=decaying))
    tce_full = compute_dividend_strip(ci_full, nav.nav_per_share).blended_tce_by_quarter
    tce_dec = compute_dividend_strip(ci_dec, nav.nav_per_share).blended_tce_by_quarter
    for cls in classes:
        curve = ci.market_data.ffa_forward_curve[cls]
        contracted = tce_full[cls][0]
        # Fully-covered front quarters match the contracted rate exactly.
        assert tce_dec[cls][0] == pytest.approx(contracted)
        assert tce_dec[cls][1] == pytest.approx(contracted)
        # Zero-coverage final quarter is pure curve.
        assert tce_dec[cls][7] == pytest.approx(curve[7])
        # Half-covered quarter is the exact midpoint.
        assert tce_dec[cls][4] == pytest.approx(0.5 * contracted + 0.5 * curve[4])


def test_longer_horizon_extends_the_strip_and_moves_terminal():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    # Longer horizons require curves of matching length (loud IndexError
    # otherwise — sectors that extend the horizon author longer curves).
    md = ci.market_data
    extended = {cls: list(c) + [c[-1]] * 2 for cls, c in md.ffa_forward_curve.items()}
    ci10 = replace(ci, market_data=replace(md, ffa_forward_curve=extended))
    nav = compute_nav(ci)
    s8 = compute_dividend_strip(ci, nav.nav_per_share, strip_horizon=8)
    s10 = compute_dividend_strip(ci10, nav.nav_per_share, strip_horizon=10)
    assert len(s10.dps_by_quarter) == 10
    # Terminal NAV ages 2 more quarters -> strictly lower terminal.
    assert s10.terminal_value < s8.terminal_value


def test_horizon_beyond_curve_length_fails_loud():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    nav = compute_nav(ci)
    with pytest.raises(IndexError):
        compute_dividend_strip(ci, nav.nav_per_share, strip_horizon=10)
