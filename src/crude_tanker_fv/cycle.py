"""Cycle-position weighting (METHODOLOGY.md section 2.3).

Cycle position = 12-month time-charter (TC) rate / 10-year historical mean TCE,
per vessel class. (Deviation from the literal METHODOLOGY.md 2.3, which names
the 12M FFA strip: the fixed-rate 12M TC is a more conservative cycle read and
is kept distinct from the FFA forward curve, which drives the dividend-strip
cash flows. ``twelve_month_ffa`` remains available for strip reporting.) The
ratio selects the NAV vs. earnings blend weights via a step function:

    > 1.5x       -> w_nav 0.70, w_earn 0.30  (late-cycle / peak)
    1.2x - 1.5x  -> w_nav 0.60, w_earn 0.40  (elevated)
    0.8x - 1.2x  -> w_nav 0.50, w_earn 0.50  (mid-cycle)
    0.5x - 0.8x  -> w_nav 0.40, w_earn 0.60  (below-mid)
    < 0.5x       -> w_nav 0.30, w_earn 0.70  (trough)

For multi-class operators the per-class ratio is combined at the
fleet-weighted-average level, weighted by each class's share of vessel value.

Open decision 9.1 — RULED 2026-07-15 (owner, methodology memo D-M4, "Proceed as
recommended"): **piecewise-linear continuous ramp** between the current band
midpoints (w_nav AND terminal_multiple both interpolate; current values preserved
at midpoints; zero new parameters). NOT yet wired — this module stays frozen (D1)
until the shared adoption round with the D-M3 parity A/B outcome (~late Aug 2026:
one cycle.py change, one regen, one ratify; book-wide small FV deltas eyeballed
under the D-M5 interval rule). Until then the steps above remain the live mechanics.
"""

from __future__ import annotations

from dataclasses import dataclass

from .schemas import CompanyInputs
from .vessel_values import vessel_market_value

FFA_12M_QUARTERS = 4

# (lower_bound_exclusive, w_nav, w_earn, terminal_multiple, label); checked high to low.
# terminal_multiple (METHODOLOGY §9.2, cycle-conditional, owner 2026-06-22): the
# strip's terminal asset-price level mean-reverts with the cycle — peak marks are
# carried DOWN (do not assume peak-forever, §10), trough marks revert UP (ships
# trade below replacement cost). Applied to the terminal's FLEET value only
# (dividend_strip._terminal_nav); cash/debt do not mean-revert.
_BANDS = [
    (1.5, 0.70, 0.30, 0.90, "late-cycle/peak"),
    (1.2, 0.60, 0.40, 0.95, "elevated"),
    (0.8, 0.50, 0.50, 1.00, "mid-cycle"),
    (0.5, 0.40, 0.60, 1.05, "below-mid"),
    (float("-inf"), 0.30, 0.70, 1.10, "trough"),
]


@dataclass
class CycleResult:
    """Cycle-position weighting for the per-company report (section 7)."""

    cycle_position: float  # fleet-weighted 12M TC / 10yr mean
    cycle_position_by_class: dict[str, float]
    twelve_month_tc_by_class: dict[str, float]
    w_nav: float
    w_earn: float
    band_label: str
    terminal_multiple: float = 1.0  # §9.2 cycle-conditional terminal-NAV multiple


def twelve_month_ffa(ffa: list[float]) -> float:
    """The 12-month FFA strip = mean of the first 4 quarters of the FFA curve.

    Single canonical definition of the "12M forward rate", shared by the cycle
    weighting and the dividend-strip reconciliation so there is one source and
    one number (METHODOLOGY.md 2.3).
    """
    if len(ffa) < FFA_12M_QUARTERS:
        raise ValueError(f"FFA curve needs >= {FFA_12M_QUARTERS} quarters, got {len(ffa)}")
    return sum(ffa[:FFA_12M_QUARTERS]) / FFA_12M_QUARTERS


def cycle_position_for_class(ffa_12m: float, historical_mean: float) -> float:
    """Single-class cycle ratio = 12M FFA strip / 10yr mean TCE."""
    if historical_mean <= 0:
        raise ValueError(f"historical mean must be positive, got {historical_mean}")
    return ffa_12m / historical_mean


def weights_for_position(cycle_position: float) -> tuple[float, float, str]:
    """Map a cycle ratio to (w_nav, w_earn, label) via the section 2.3 bands."""
    for lower, w_nav, w_earn, _term_mult, label in _BANDS:
        if cycle_position > lower:
            return w_nav, w_earn, label
    raise AssertionError("unreachable: bands cover all reals")


def terminal_multiple_for_position(cycle_position: float) -> float:
    """Cycle-conditional terminal-NAV multiple (METHODOLOGY §9.2): the strip's
    terminal asset level mean-reverts — 0.90x at a peak (do not carry firm marks
    forward), 1.10x at a trough (ships trade below replacement cost; revert up)."""
    for lower, _w_nav, _w_earn, term_mult, _label in _BANDS:
        if cycle_position > lower:
            return term_mult
    raise AssertionError("unreachable: bands cover all reals")


def _class_value_weights(inputs: CompanyInputs) -> dict[str, float]:
    """Each class's share of total fleet market value (count- and discount-aware)."""
    curves = inputs.market_data.vessel_value_curves
    yard_discounts = inputs.market_data.yard_discounts
    by_class: dict[str, float] = {}
    for v in inputs.fleet.vessels:
        value = vessel_market_value(v, curves[v.cls], yard_discounts) * v.count
        by_class[v.cls] = by_class.get(v.cls, 0.0) + value
    total = sum(by_class.values())
    return {cls: val / total for cls, val in by_class.items()}


def compute_cycle(inputs: CompanyInputs) -> CycleResult:
    """Fleet-weighted cycle position and resulting blend weights."""
    md = inputs.market_data
    value_weights = _class_value_weights(inputs)
    if not value_weights:  # G-1: empty fleet would silently fall to the trough band
        raise ValueError("empty fleet: no vessel classes to weight for cycle position")

    by_class: dict[str, float] = {}
    tc_by_class: dict[str, float] = {}
    for cls in value_weights:
        tc = md.twelve_month_tc.get(cls)
        if tc is None:
            raise ValueError(f"no 12-month TC rate for class {cls!r}")
        mean = md.historical_tce_means.get(cls)
        if mean is None:
            raise ValueError(f"no historical mean TCE for class {cls!r}")
        tc_by_class[cls] = tc
        by_class[cls] = cycle_position_for_class(tc, mean)

    fleet_position = sum(value_weights[cls] * by_class[cls] for cls in by_class)
    w_nav, w_earn, label = weights_for_position(fleet_position)

    return CycleResult(
        cycle_position=fleet_position,
        cycle_position_by_class=by_class,
        twelve_month_tc_by_class=tc_by_class,
        w_nav=w_nav,
        w_earn=w_earn,
        band_label=label,
        terminal_multiple=terminal_multiple_for_position(fleet_position),
    )
