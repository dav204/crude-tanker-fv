"""Sensitivity grid (METHODOLOGY.md section 3.4).

For each name, recompute blended fair value across:

- TCE rates:    -30%, -15%, base, +15%, +30%  (scales the FFA forward curve)
- Vessel values: -20%, -10%, base, +10%, +20%  (scales the vessel value curves)

Output a 5x5 grid of fair value. The TCE shock moves the dividend strip; the
vessel-value shock moves NAV and the strip's NAV-based terminal value. Cycle
weights are pinned at their base values so the grid isolates the two levers
(for DHT the cycle stays in the peak band across the whole shock range anyway).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

from .blend import blend_fair_value
from .cycle import compute_cycle
from .dividend_strip import compute_dividend_strip
from .nav import compute_nav
from .schemas import CompanyInputs

TCE_SHOCKS = (-0.30, -0.15, 0.0, 0.15, 0.30)
VESSEL_VALUE_SHOCKS = (-0.20, -0.10, 0.0, 0.10, 0.20)
PAYOUT_SCENARIOS = (0.80, 0.95, 1.00)  # stated floor / base / peak-persists


@dataclass
class SensitivityGrid:
    """5x5 sensitivity grid for the per-company report (section 7)."""

    tce_shocks: tuple[float, ...] = TCE_SHOCKS
    vessel_value_shocks: tuple[float, ...] = VESSEL_VALUE_SHOCKS
    # grid[i][j] = fair value at tce_shocks[i], vessel_value_shocks[j]
    grid: list[list[float]] = field(default_factory=list)
    current_price: float = 0.0


def _shock_inputs(inputs: CompanyInputs, tce_shock: float, vessel_shock: float) -> CompanyInputs:
    md = inputs.market_data
    ffa = {
        cls: [v * (1 + tce_shock) for v in curve]
        for cls, curve in md.ffa_forward_curve.items()
    }
    curves = {
        cls: replace(
            c,
            newbuild=c.newbuild * (1 + vessel_shock),
            five_year_benchmark=c.five_year_benchmark * (1 + vessel_shock),
            ten_year_benchmark=c.ten_year_benchmark * (1 + vessel_shock),
            scrap_25yr=c.scrap_25yr * (1 + vessel_shock),
            scrubber_premium=c.scrubber_premium * (1 + vessel_shock),
        )
        for cls, c in md.vessel_value_curves.items()
    }
    return replace(
        inputs, market_data=replace(md, ffa_forward_curve=ffa, vessel_value_curves=curves)
    )


def compute_sensitivity(inputs: CompanyInputs, current_price: float) -> SensitivityGrid:
    """Recompute blended fair value across the TCE x vessel-value shock grid."""
    base_cycle = compute_cycle(inputs)  # weights pinned at base across the grid
    grid: list[list[float]] = []
    for tce_shock in TCE_SHOCKS:
        row: list[float] = []
        for vessel_shock in VESSEL_VALUE_SHOCKS:
            shocked = _shock_inputs(inputs, tce_shock, vessel_shock)
            nav = compute_nav(shocked)
            strip = compute_dividend_strip(
                shocked, nav.nav_per_share, terminal_multiple=base_cycle.terminal_multiple
            )
            row.append(blend_fair_value(nav, strip, base_cycle).fair_value_per_share)
        grid.append(row)
    return SensitivityGrid(grid=grid, current_price=current_price)


def payout_sensitivity(
    inputs: CompanyInputs, payouts: tuple[float, ...] = PAYOUT_SCENARIOS
) -> dict[float, float]:
    """Blended fair value at each dividend payout-ratio scenario.

    Tanker boards pay near 100% at peaks and revert toward the stated floor as
    the cycle softens, so payout is a structural lever, not a rounding choice
    (METHODOLOGY.md 3.2). Only the dividend strip moves; NAV and cycle are fixed.
    """
    nav = compute_nav(inputs)
    cycle = compute_cycle(inputs)
    out: dict[float, float] = {}
    for payout in payouts:
        shocked = replace(
            inputs, dividend_policy=replace(inputs.dividend_policy, payout_ratio=payout)
        )
        strip = compute_dividend_strip(
            shocked, nav.nav_per_share, terminal_multiple=cycle.terminal_multiple
        )
        out[payout] = blend_fair_value(nav, strip, cycle).fair_value_per_share
    return out
