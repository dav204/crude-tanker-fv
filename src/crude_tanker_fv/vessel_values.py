"""Vessel market-value curve construction (METHODOLOGY.md section 3.1).

Builds a per-(class, age) market value from four anchor points taken from the
broker term structure (e.g. Compass weekly report), which quotes a value at
each of these ages for every class:

- age 0:  newbuild / prompt-resale value
- age 5:  5-year secondhand benchmark
- age 10: 10-year secondhand value
- age 25: scrap value (derived from recycling $/LDT)

The curve is **piecewise-linear** between adjacent anchors, and clamped to
scrap beyond age 25.

On the methodology's "accelerating discount after age 15": rather than a free
acceleration parameter (which, with only newbuild/5yr/scrap anchors, perversely
*raised* mid-life values to satisfy the fixed endpoints), the old-age
acceleration now falls out of the data — the 10->25 segment is steeper than the
5->10 segment because the broker term structure says so. This both removes a
hand-tuned knob and fixes the mid-life over-valuation seen in the first cut
(see also METHODOLOGY.md 9.1).

Per-vessel adjustments (section 3.1):
- eco-design:    multiply by (1 + eco_premium_pct), default +5%.
- scrubber:      add a flat per-vessel premium.
- yard discount: multiply by (1 - discount) for lower-tier yards (Chinese,
                 ex-Hanjin-Subic), looked up by yard name in ``yard_discounts``.
- ice-class:     not modelled (no ice-class field).
"""

from __future__ import annotations

from typing import Optional

from .schemas import Vessel, VesselValueCurve

_SCRAP_AGE = 25.0


def value_for_age(curve: VesselValueCurve, age: float) -> float:
    """Base market value for a vessel of this class at ``age`` (pre-adjustments).

    Piecewise-linear through the age 0 / 5 / 10 / 25 broker anchors
    (METHODOLOGY.md section 3.1).
    """
    if age < 0:
        raise ValueError(f"age must be non-negative, got {age}")
    if age >= _SCRAP_AGE:
        return curve.scrap_25yr

    anchors = [
        (0.0, curve.newbuild),
        (5.0, curve.five_year_benchmark),
        (10.0, curve.ten_year_benchmark),
        (_SCRAP_AGE, curve.scrap_25yr),
    ]
    for (a0, v0), (a1, v1) in zip(anchors, anchors[1:]):
        if age <= a1:
            return v0 + (v1 - v0) * ((age - a0) / (a1 - a0))
    return curve.scrap_25yr  # unreachable (age < 25 handled above)


def vessel_market_value(
    vessel: Vessel,
    curve: VesselValueCurve,
    yard_discounts: Optional[dict[str, float]] = None,
) -> float:
    """Per-vessel market value with eco, yard-discount, and scrubber adjustments.

    Pass ``yard_discounts=None`` (the default) to value a vessel at par (no
    yard haircut) — used to report NAV both with and without the discount.
    """
    value = value_for_age(curve, vessel.age)
    # dwt-scaling (dry-bulk collapsed classes, METHODOLOGY §11.7.x): the curve
    # anchors are at curve.dwt (baseline); scale the base hull value by the
    # vessel's actual size. Applied to the hull value BEFORE the multiplicative
    # eco/yard adjustments and the flat scrubber add. Flat-per-class curves
    # (dwt_scaled False) are unaffected.
    if curve.dwt_scaled and curve.dwt and vessel.dwt:
        value *= vessel.dwt / curve.dwt
    if vessel.eco:
        value *= 1.0 + curve.eco_premium_pct
    if yard_discounts and vessel.yard in yard_discounts:
        value *= 1.0 - yard_discounts[vessel.yard]
    if vessel.scrubber:
        value += curve.scrubber_premium
    return value
