"""Input validation / data-pipeline sanity checks.

Returns human-readable warnings for inputs that are out of plausible range, so
bad data (wrong units, single-day spikes treated as levels, stale figures) is
surfaced rather than silently flowing into the valuation. Warnings do not stop
a run; they are printed by the pipeline and shown in the report.

The headline check is rate plausibility: no sustained crude-tanker TCE has
historically run more than a few multiples of its 10-year mean, so a spot or
FFA figure far above the mean almost certainly reflects a data problem.
"""

from __future__ import annotations

from .schemas import CompanyInputs

# A sustained TCE this many times the 10-year mean is treated as implausible.
SPOT_HIGH_MULTIPLE = 5.0
FFA_HIGH_MULTIPLE = 5.0


def validate_inputs(inputs: CompanyInputs) -> list[str]:
    """Return a list of warning strings (empty == clean)."""
    warnings: list[str] = []
    md = inputs.market_data
    means = md.historical_tce_means

    for cls, spot in md.spot_tce.items():
        mean = means.get(cls)
        if spot is not None and spot <= 0:
            warnings.append(f"spot TCE {cls}: non-positive ({spot}).")
        elif mean and spot > SPOT_HIGH_MULTIPLE * mean:
            warnings.append(
                f"spot TCE {cls}: ${spot:,.0f}/day is {spot / mean:.1f}x the 10-yr mean "
                f"(${mean:,.0f}) — unsustainable as a level. Confirm it is a genuine cycle "
                f"spike (not a unit/source error) and do not anchor valuation to it."
            )

    for cls, curve in md.ffa_forward_curve.items():
        mean = means.get(cls)
        for q, v in enumerate(curve, 1):
            if v is None:
                continue
            if v <= 0:
                warnings.append(f"FFA {cls} q{q}: non-positive ({v}).")
            elif mean and v > FFA_HIGH_MULTIPLE * mean:
                warnings.append(
                    f"FFA {cls} q{q}: ${v:,.0f}/day is {v / mean:.1f}x the 10-yr mean — verify."
                )

    for cls, tc in md.twelve_month_tc.items():
        mean = means.get(cls)
        if tc is not None and tc <= 0:
            warnings.append(f"12M TC {cls}: non-positive ({tc}).")
        elif mean and tc > SPOT_HIGH_MULTIPLE * mean:
            warnings.append(
                f"12M TC {cls}: ${tc:,.0f}/day is {tc / mean:.1f}x the 10-yr mean — verify."
            )

    for cls, mean in means.items():
        if mean is not None and mean <= 0:
            warnings.append(f"historical mean TCE {cls}: non-positive ({mean}).")

    bs = inputs.balance_sheet
    if bs.diluted_shares_outstanding <= 0:
        warnings.append("diluted shares outstanding must be > 0.")
    if bs.total_debt < 0:
        warnings.append("total debt is negative.")

    return warnings
