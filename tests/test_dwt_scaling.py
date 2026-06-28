"""dwt-scaling of dry-bulk value curves (METHODOLOGY §11.7.x)."""

from datetime import date

import pytest

from crude_tanker_fv.schemas import Vessel, VesselValueCurve
from crude_tanker_fv.transactions import TransactionPrint, TransactionSet, fit_curve_anchors
from crude_tanker_fv.vessel_values import vessel_market_value

M = 1_000_000


def _cape_curve(dwt_scaled: bool) -> VesselValueCurve:
    return VesselValueCurve(
        cls="Cape", dwt=180_000, newbuild=74 * M, five_year_benchmark=63 * M,
        ten_year_benchmark=46 * M, scrap_25yr=13 * M, eco_premium_pct=0.0,
        dwt_scaled=dwt_scaled,
    )


def test_dwt_scaling_scales_value_by_size():
    """A 210k Newcastlemax marks 210/180 x a 180k Capesize at the same age."""
    curve = _cape_curve(True)
    v180 = vessel_market_value(Vessel(id="a", cls="Cape", dwt=180_000, age=5), curve)
    v210 = vessel_market_value(Vessel(id="b", cls="Cape", dwt=210_000, age=5), curve)
    assert v180 == pytest.approx(63 * M)                     # at baseline = curve 5yr
    assert v210 / v180 == pytest.approx(210_000 / 180_000)   # pure size
    assert v210 == pytest.approx(63 * M * 210 / 180)


def test_flat_curve_ignores_dwt():
    """A non-dwt_scaled curve (the crude/product/lng/container convention) is flat."""
    curve = _cape_curve(False)
    v180 = vessel_market_value(Vessel(id="a", cls="Cape", dwt=180_000, age=5), curve)
    v210 = vessel_market_value(Vessel(id="b", cls="Cape", dwt=210_000, age=5), curve)
    assert v210 == v180 == pytest.approx(63 * M)


def test_dwt_scaling_composes_with_eco():
    """dwt-scaling applies to the base hull value, then the eco premium multiplies."""
    curve = _cape_curve(True)
    curve = VesselValueCurve(**{**curve.__dict__, "eco_premium_pct": 0.05})
    v = vessel_market_value(Vessel(id="b", cls="Cape", dwt=210_000, age=5, eco=True), curve)
    assert v == pytest.approx(63 * M * (210 / 180) * 1.05)


def _ts(prints):
    return TransactionSet(cls="Cape", as_of=date(2026, 6, 9), prints=prints)


def test_dwt_normalized_fit_lowers_nmax_heavy_sample():
    """The fit normalizes prints to the baseline dwt, so a Newcastlemax-priced
    sample no longer inflates the (180k) Capesize anchor — the engine's
    double-count guard for dwt-scaled classes."""
    # 208k NMax $72.75M and a 207k NMax $55M at ages 5/10 — both >180k. Use a high
    # newbuild anchor so the fit's [scrap*1.5, newbuild*0.95] clamp doesn't bind.
    def _curve(scaled):
        return VesselValueCurve(
            cls="Cape", dwt=180_000, newbuild=90 * M, five_year_benchmark=63 * M,
            ten_year_benchmark=46 * M, scrap_25yr=13 * M, eco_premium_pct=0.0,
            dwt_scaled=scaled,
        )
    prints = [
        TransactionPrint(date=date(2025, 11, 15), age=5, price_usd_m=72.75,
                         quality_flag="standard", dwt=208_000),
        TransactionPrint(date=date(2025, 8, 15), age=10, price_usd_m=55.0,
                         quality_flag="standard", dwt=207_000),
    ]
    scaled = fit_curve_anchors(_curve(True), _ts(prints))
    flat = fit_curve_anchors(_curve(False), _ts(prints))
    assert not scaled.fallback and not flat.fallback
    # Flat fit sits at the raw NMax level; the dwt-scaled fit normalizes to 180k.
    assert flat.new_5yr == pytest.approx(72.75 * M, rel=0.02)
    assert scaled.new_5yr == pytest.approx(72.75 * M * 180 / 208, rel=0.02)   # ~$63M
    assert scaled.new_5yr < flat.new_5yr
