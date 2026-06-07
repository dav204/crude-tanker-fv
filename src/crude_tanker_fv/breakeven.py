"""Implied breakeven TCE (METHODOLOGY.md section 3.3).

The sanity check: how extreme must rates be to justify the current share price?
We solve for a single uniform **multiplier** ``m`` on the *current forward curve*
(holding cycle weights at base, NAV fixed) such that the tool's blended fair
value equals the price. Scaling the forward — rather than flattening every class
to one number — preserves the natural inter-class rate structure (a VLCC earns
more than a Suezmax in every state of the world), which matters for blended
fleets (INSW, TNK, EURN). The flat-rate-across-all-classes construct used
previously distorted blended breakevens upward and was not comparable between
names with different fleet mixes.

We report, against the 10-yr mean / current spot / 12-month FFA:

- a **value-weighted blended breakeven TCE** = Σ_class value_weight · (m · FFA_12M_class),
  the headline, comparable across names and to the scenario "assumed TCE"
  (also value-weighted), and
- the **per-class** implied rate (m · FFA_12M_class) in each class's own units.

Implied breakeven >> mean ⇒ market pricing extended peak rates. Implied breakeven
< mean ⇒ market pricing distress. For single-class names (DHT) the blended
breakeven is just that class's rate, and ``m`` is the multiple of its forward.

The multiplier scales the *spot* leg of each class (the strip blends
spot/FFA with fixed contracted charter rates); for single-class names it reduces
to the classic "how many times the forward justifies the price".
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

from .blend import blend_fair_value
from .cycle import FFA_12M_QUARTERS, CycleResult, compute_cycle
from .dividend_strip import compute_dividend_strip
from .nav import NavResult, compute_nav
from .schemas import CompanyInputs

_SOLVE_ITERATIONS = 100
_SOLVE_UPPER_MULT = 50.0  # multiple of the current forward; ample upper bound for bisection


@dataclass
class BreakevenResult:
    """Implied breakeven diagnostics for the per-company report (section 7)."""

    multiplier: float                              # uniform scalar on the forward curve
    blended_breakeven_tce: float                   # value-weighted Σ w·(m·FFA_12M) — headline
    implied_breakeven_tce: dict[str, float]        # per class = m · FFA_12M_class
    value_weights: dict[str, float] = field(default_factory=dict)
    historical_mean_tce: dict[str, float] = field(default_factory=dict)
    current_spot_tce: dict[str, float] = field(default_factory=dict)
    ffa_12m: dict[str, float] = field(default_factory=dict)
    blended_mean_tce: float = 0.0                  # value-weighted 10-yr mean
    blended_ffa_12m: float = 0.0                   # value-weighted 12-month forward
    blended_spot_tce: float = 0.0                  # value-weighted current spot


def _fair_value_at_mult(
    inputs: CompanyInputs, nav: NavResult, base_cycle: CycleResult, mult: float
) -> float:
    """Blended FV with every class's forward curve scaled by ``mult`` (ratios preserved)."""
    scaled = {
        cls: [r * mult for r in curve]
        for cls, curve in inputs.market_data.ffa_forward_curve.items()
    }
    shocked = replace(inputs, market_data=replace(inputs.market_data, ffa_forward_curve=scaled))
    strip = compute_dividend_strip(shocked, nav.nav_per_share)
    return blend_fair_value(nav, strip, base_cycle).fair_value_per_share


def implied_breakeven_tce(inputs: CompanyInputs, current_price: float) -> BreakevenResult:
    """Solve for the uniform forward multiplier that makes blended FV == current price."""
    nav = compute_nav(inputs)
    base_cycle = compute_cycle(inputs)
    md = inputs.market_data

    fleet_classes = {v.cls for v in inputs.fleet.vessels}
    priced = [c for c in fleet_classes if c in md.ffa_forward_curve]

    fv_total = nav.fleet_value or 1.0
    value_weights = {c: nav.fleet_value_by_class.get(c, 0.0) / fv_total for c in priced}
    ffa_12m = {
        c: sum(md.ffa_forward_curve[c][:FFA_12M_QUARTERS]) / FFA_12M_QUARTERS for c in priced
    }

    # Blended FV is monotonically increasing in the multiplier -> bisection.
    lo, hi = 0.0, _SOLVE_UPPER_MULT
    for _ in range(_SOLVE_ITERATIONS):
        mid = (lo + hi) / 2.0
        if _fair_value_at_mult(inputs, nav, base_cycle, mid) < current_price:
            lo = mid
        else:
            hi = mid
    multiplier = (lo + hi) / 2.0

    per_class = {c: multiplier * ffa_12m[c] for c in priced}

    def _blended(source: dict[str, float]) -> float:
        return sum(value_weights.get(c, 0.0) * source.get(c, 0.0) for c in priced)

    mean = {c: md.historical_tce_means[c] for c in priced if c in md.historical_tce_means}
    spot = {c: md.spot_tce[c] for c in priced if c in md.spot_tce}
    return BreakevenResult(
        multiplier=multiplier,
        blended_breakeven_tce=_blended(per_class),
        implied_breakeven_tce=per_class,
        value_weights=value_weights,
        historical_mean_tce=mean,
        current_spot_tce=spot,
        ffa_12m=ffa_12m,
        blended_mean_tce=_blended(mean),
        blended_ffa_12m=_blended(ffa_12m),
        blended_spot_tce=_blended(spot),
    )
