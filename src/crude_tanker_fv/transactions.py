"""Transaction-anchored curve recalibration (METHODOLOGY.md sections 3.1, 9.9).

Recalibrates the **mid-age** leg (ages 5 and 10) of a class's vessel value curve
from observed second-hand S&P transactions. Newbuild (age 0) and old-age (15yr+)
anchors are left untouched — newbuilds are publicly priced and the old-age leg
is disposal-validated separately. The scope is *opt-in*: when enabled, only the
classes with a populated transactions file are recalibrated.

Fit:
- Each transaction's price is converted to a **clean-market** price by applying a
  quality uplift (sale-leaseback / financing structures clear 5-10% below clean
  market; distressed sales 10-15% below; treat newbuild_resale as already clean).
- Each transaction gets a **recency weight** with a ~15-month half-life
  (w = 2 ** (-Δmonths / 15)), so a 15-month-old print carries half the weight of
  a fresh one.
- A weighted linear regression on (age, clean_price) is fit within the mid-age
  window [3, 17] years.
- The fitted line is read off at age 5 and age 10 to produce the new anchors.
- The slope MUST be negative (older = cheaper); if not, or if fewer than 2 prints
  fall in the window, fall back to the existing curve unchanged.

The fit also clamps new anchors to a sensible band [scrap × 1.5, newbuild × 0.95]
to keep the piecewise interpolation monotone if the regression mis-fits at the
edges of the window.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import date as _date
from pathlib import Path
from typing import Optional

import yaml

from .schemas import VesselValueCurve

QUALITY_UPLIFT = {
    "standard": 0.0,
    "financing": 0.05,        # sale-leaseback / financing structure
    "distressed": 0.10,
    "newbuild_resale": 0.0,
}
DEFAULT_HALF_LIFE_MONTHS = 15.0
MID_AGE_MIN, MID_AGE_MAX = 3, 17
ANCHOR_AGES = (5, 10)


@dataclass
class TransactionPrint:
    """One S&P data point used in the recalibration fit."""

    date: _date
    age: float
    price_usd_m: float
    quality_flag: str
    source: str = ""
    notes: str = ""
    # Set False for documentation-only rows (en-bloc aggregates with no per-vessel
    # split, out-of-window references) so they are EXCLUDED from the regression even
    # if their age falls in the fit window. Defaults True (BUG-2, 2026-06-22).
    in_fit: bool = True
    # Vessel dwt at sale. Used ONLY by dwt-scaled classes (dry bulk, §11.7.x) to
    # normalize the print to the curve's baseline dwt before fitting; None falls
    # back to the baseline (no normalization). Ignored for flat-per-class fits.
    dwt: Optional[int] = None

    @property
    def clean_price_usd_m(self) -> float:
        return self.price_usd_m * (1.0 + QUALITY_UPLIFT.get(self.quality_flag, 0.0))


@dataclass
class TransactionSet:
    """All transactions for one vessel class."""

    cls: str
    as_of: _date
    prints: list[TransactionPrint] = field(default_factory=list)


@dataclass
class CurveFit:
    """Diagnostic record of a per-class recalibration."""

    cls: str
    n_used: int                       # transactions inside the mid-age window
    intercept: float                  # USD ($, not $M)
    slope_per_year: float             # USD/year
    new_5yr: float                    # USD
    new_10yr: float                   # USD
    old_5yr: float
    old_10yr: float
    fallback: bool = False
    note: str = ""

    @property
    def delta_5yr_pct(self) -> float:
        return (self.new_5yr / self.old_5yr - 1.0) * 100.0 if self.old_5yr else 0.0

    @property
    def delta_10yr_pct(self) -> float:
        return (self.new_10yr / self.old_10yr - 1.0) * 100.0 if self.old_10yr else 0.0


def load_transaction_set(path: Path) -> TransactionSet:
    """Load one transactions/<class>.yaml file into a TransactionSet."""
    with open(path) as fh:
        doc = yaml.safe_load(fh) or {}
    cls = doc.get("class")
    if not cls:
        raise ValueError(f"transactions file {path} missing 'class'")
    as_of_raw = doc.get("as_of")
    if isinstance(as_of_raw, str):
        as_of = _date.fromisoformat(as_of_raw)
    elif isinstance(as_of_raw, _date):
        as_of = as_of_raw
    else:
        raise ValueError(f"transactions file {path} missing 'as_of' date")

    prints: list[TransactionPrint] = []
    for raw in doc.get("prints") or []:
        d = raw["date"]
        if isinstance(d, str):
            d = _date.fromisoformat(d)
        flag = str(raw.get("quality_flag", "standard"))
        if flag not in QUALITY_UPLIFT:
            raise ValueError(f"unknown quality_flag {flag!r} in {path}")
        prints.append(TransactionPrint(
            date=d,
            age=float(raw["vessel_age_at_sale"]),
            price_usd_m=float(raw["sale_price_usd_m"]),
            quality_flag=flag,
            source=str(raw.get("source", "")),
            notes=str(raw.get("notes", "")),
            in_fit=bool(raw.get("in_fit", True)),
            dwt=(int(raw["dwt"]) if raw.get("dwt") is not None else None),
        ))
    return TransactionSet(cls=cls, as_of=as_of, prints=prints)


def load_all_transactions(inputs_dir: Path) -> dict[str, TransactionSet]:
    """Load every transactions/<class>.yaml file (skipping the template)."""
    out: dict[str, TransactionSet] = {}
    tx_dir = inputs_dir / "market_data" / "transactions"
    if not tx_dir.exists():
        return out
    for path in sorted(tx_dir.glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        ts = load_transaction_set(path)
        out[ts.cls] = ts
    return out


def _months_between(earlier: _date, later: _date) -> float:
    return (later.year - earlier.year) * 12.0 + (later.month - earlier.month) + (later.day - earlier.day) / 30.4375


def _wls_linear(points: list[tuple[float, float, float]]) -> tuple[float, float]:
    """Weighted least-squares: y = a + b·x. Returns (a, b). Caller checks sample count."""
    sw = sum(w for _, _, w in points)
    swx = sum(w * x for x, _, w in points)
    swy = sum(w * y for _, y, w in points)
    swxx = sum(w * x * x for x, _, w in points)
    swxy = sum(w * x * y for x, y, w in points)
    denom = sw * swxx - swx * swx
    if denom == 0:
        # All x identical -> slope undefined; return horizontal at weighted mean.
        return swy / sw, 0.0
    b = (sw * swxy - swx * swy) / denom
    a = (swy - b * swx) / sw
    return a, b


def fit_curve_anchors(
    curve: VesselValueCurve,
    txs: TransactionSet,
    half_life_months: float = DEFAULT_HALF_LIFE_MONTHS,
) -> CurveFit:
    """Solve new 5yr / 10yr anchors from transactions. Falls back gracefully."""
    in_window: list[tuple[float, float, float]] = []
    n_missing_dwt = 0
    for p in txs.prints:
        if not p.in_fit:
            continue   # documentation-only row (e.g. en-bloc aggregate, no per-vessel split)
        if not (MID_AGE_MIN <= p.age <= MID_AGE_MAX):
            continue
        dm = _months_between(p.date, txs.as_of)
        if dm < 0:
            dm = 0.0  # transaction dated after as_of: treat as fresh
        w = 2.0 ** (-dm / half_life_months)
        price = p.clean_price_usd_m * 1_000_000
        # dwt-scaled classes (dry bulk, §11.7.x): normalize the print to the
        # curve's baseline dwt so the fitted 5yr/10yr anchors are at the baseline.
        # vessel_market_value then scales each vessel back up by its own dwt — so a
        # 210k Newcastlemax and a 180k Capesize at the same age differ by size only.
        if curve.dwt_scaled and curve.dwt:
            if p.dwt:
                price *= curve.dwt / p.dwt
            else:
                n_missing_dwt += 1   # treat as baseline (no normalization)
        in_window.append((p.age, price, w))

    if len(in_window) < 2:
        return CurveFit(
            cls=curve.cls, n_used=len(in_window), intercept=0.0, slope_per_year=0.0,
            new_5yr=curve.five_year_benchmark, new_10yr=curve.ten_year_benchmark,
            old_5yr=curve.five_year_benchmark, old_10yr=curve.ten_year_benchmark,
            fallback=True, note=f"fewer than 2 prints in age window [{MID_AGE_MIN},{MID_AGE_MAX}]",
        )

    a, b = _wls_linear(in_window)
    if b >= 0:
        return CurveFit(
            cls=curve.cls, n_used=len(in_window), intercept=a, slope_per_year=b,
            new_5yr=curve.five_year_benchmark, new_10yr=curve.ten_year_benchmark,
            old_5yr=curve.five_year_benchmark, old_10yr=curve.ten_year_benchmark,
            fallback=True, note=f"fit slope non-negative ({b:+.0f} $/yr) — bad sample",
        )

    raw_5yr = a + b * ANCHOR_AGES[0]
    raw_10yr = a + b * ANCHOR_AGES[1]
    lo = curve.scrap_25yr * 1.5
    hi = curve.newbuild * 0.95
    new_5yr = max(lo, min(hi, raw_5yr))
    new_10yr = max(lo, min(new_5yr, raw_10yr))   # also enforce monotone within mid-age

    note = ""
    if new_5yr != raw_5yr or new_10yr != raw_10yr:
        note = "raw fit clamped to [scrap×1.5, newbuild×0.95] / monotone"
    if n_missing_dwt:
        note = (note + "; " if note else "") + \
               f"{n_missing_dwt} dwt-scaled print(s) missing dwt — used baseline"

    return CurveFit(
        cls=curve.cls, n_used=len(in_window), intercept=a, slope_per_year=b,
        new_5yr=new_5yr, new_10yr=new_10yr,
        old_5yr=curve.five_year_benchmark, old_10yr=curve.ten_year_benchmark,
        fallback=False, note=note,
    )


def recalibrated_curve(curve: VesselValueCurve, fit: CurveFit) -> VesselValueCurve:
    """Return a copy of ``curve`` with mid-age anchors replaced by the fit."""
    if fit.fallback:
        return curve
    return replace(curve, five_year_benchmark=fit.new_5yr, ten_year_benchmark=fit.new_10yr)


# v1 proxy aliases: classes that share another's transaction sample because the
# model treats them as equivalent (LR2 modeled as Aframax-equivalent crude/dirty
# proxy per METHODOLOGY 9.3). When the source class is recalibrated and the alias
# does not have its own transactions file, the same fit is propagated to the alias.
_PROXY_ALIASES = {"Aframax": ["LR2"]}


def apply_transaction_anchored_curves(
    market_data, transactions: dict[str, TransactionSet]
) -> tuple[object, dict[str, CurveFit]]:
    """Replace 5yr/10yr anchors for every class with a populated transactions set.

    Returns (new_market_data, per-class CurveFit) so the caller can render the
    recalibration diagnostic alongside the valuation.

    v1 LR2-as-Aframax proxy: the Aframax fit propagates to LR2 unless LR2 has
    its own VALID fit (i.e., enough in-window prints to clear the fallback
    guard). An ``lr2.yaml`` file with too few in-window prints still triggers
    proxy propagation — the file is treated as data documentation, not as a
    competing fit, until it has enough prints to stand alone.
    """
    new_curves = dict(market_data.vessel_value_curves)
    fits: dict[str, CurveFit] = {}
    # Phase 1 — own-class fits
    for cls, ts in transactions.items():
        if cls not in new_curves:
            continue
        fit = fit_curve_anchors(new_curves[cls], ts)
        fits[cls] = fit
        if not fit.fallback:
            new_curves[cls] = recalibrated_curve(new_curves[cls], fit)
    # Phase 2 — proxy aliases (fire where the alias has no own valid fit)
    for src_cls, ts in transactions.items():
        src_fit = fits.get(src_cls)
        if src_fit is None or src_fit.fallback:
            continue   # source itself didn't produce a usable fit
        for alias in _PROXY_ALIASES.get(src_cls, []):
            if alias not in new_curves:
                continue
            existing = fits.get(alias)
            if existing is not None and not existing.fallback:
                continue   # alias already has its own valid fit
            alias_fit = fit_curve_anchors(new_curves[alias], ts)
            alias_fit.note = (alias_fit.note + "; " if alias_fit.note else "") + \
                             f"propagated from {src_cls} (v1 proxy alias)"
            fits[alias] = alias_fit   # may overwrite an earlier fallback record
            new_curves[alias] = recalibrated_curve(new_curves[alias], alias_fit)
    return replace(market_data, vessel_value_curves=new_curves), fits
