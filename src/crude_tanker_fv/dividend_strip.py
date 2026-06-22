"""Forward dividend strip (METHODOLOGY.md section 3.2).

    DivStrip_implied_price = Sum_{q=1..8} DPS_q / (1 + r)^(q/4)
                           + TerminalValue_{q=9} / (1 + r)^(9/4)

with, per quarter q:

    EPS_q = (NetTCE_revenue_q - OPEX_q - G&A_q - interest_q - tax_q) / shares
    NetTCE_revenue_q = Sum_class vessels_class * days * TCE_class_q * (1 - offhire)
    TCE_class_q = spot_pct * FFA_class_q + (1 - spot_pct) * disclosed_charter_rate

DPS depends on the policy type (METHODOLOGY.md 4.3):

- ``variable`` (DHT, FRO, ECO) -- the base is a *minimum floor under* the payout:
      DPS_q = max(base_dividend, payout_ratio * max(0, EPS_q - floor))
  e.g. DHT pays 100% of EPS but never less than its $0.025 nominal base.
- ``base_plus_variable`` (INSW) -- the base is paid *in addition to* the variable:
      DPS_q = base_dividend + payout_ratio * max(0, EPS_q - floor)

(The literal METHODOLOGY.md 3.2 formula is the base_plus_variable form; it
over-pays a floor-type policy by the base every quarter, so we dispatch on type.)

- Discount rate r defaults to 11% (sensitivity +/-2%, METHODOLOGY 3.2 / 9.5).
- OPEX accrues on all operating days (offhire reduces revenue, not opex).
- disclosed_charter_rate is the count-average of disclosed (non-null) charter
  rates among time-chartered vessels of the class in the fleet manifest.
- TerminalValue at q=horizon+1 = cycle-conditional NAV (METHODOLOGY §9.2):
  the fleet aged forward on the depreciation curve, its asset-price level
  mean-reverted by ``terminal_multiple`` (peak 0.9x … trough 1.1x, FLEET value
  only), plus the balance sheet carried forward with RETAINED EARNINGS over the
  strip (terminal cash += sum(EPS - DPS) per share). Callers pass
  ``cycle.terminal_multiple``; default 1.0 (mid-cycle / no cycle supplied).

Strip horizon: per-sector parameter (METHODOLOGY §11.8.6.4). Default 8
quarters (FFA liquidity drops sharply beyond ~18 months); containerships run
longer (contracted backlog, not FFA extrapolation, carries the forward cash).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

from .cycle import twelve_month_ffa
from .nav import COST_OF_EQUITY, NavResult, compute_nav
from .schemas import CompanyInputs, DividendPolicy

DEFAULT_DISCOUNT_RATE = COST_OF_EQUITY   # 11% cost of equity, shared with nav.py (BUG-7)
STRIP_HORIZON_QUARTERS = 8
TERMINAL_NAV_MULTIPLE = 1.0   # DEFAULT terminal multiple (mid-cycle / when no cycle
                              # is supplied). §9.2 is CYCLE-CONDITIONAL since 2026-06-22
                              # (owner — outputs/terminal_value_options_memo.md): callers
                              # pass cycle.terminal_multiple (peak 0.9x … trough 1.1x,
                              # cycle.terminal_multiple_for_position). Changing the band
                              # ramp is a methodology decision: update the memo DECISION
                              # block + re-pin test_terminal_multiple_cycle_conditional.
DEFAULT_OFFHIRE_RATE = 0.02   # ~drydock + unscheduled offhire
DAYS_PER_QUARTER = 365.0 / 4.0


@dataclass
class DividendStripResult:
    """Dividend-strip breakdown for the per-company report (section 7)."""

    dps_by_quarter: list[float] = field(default_factory=list)        # 8 quarters
    eps_by_quarter: list[float] = field(default_factory=list)
    net_tce_revenue_by_quarter: list[float] = field(default_factory=list)
    blended_tce_by_quarter: dict[str, list[float]] = field(default_factory=dict)  # by class
    ffa_spot_by_quarter: dict[str, list[float]] = field(default_factory=dict)     # by class (spot)
    ffa_12m_by_class: dict[str, float] = field(default_factory=dict)              # front-4 mean
    discounted_dps: list[float] = field(default_factory=list)
    terminal_value: float = 0.0               # per share, undiscounted (aged NAV/share)
    discounted_terminal_value: float = 0.0
    implied_price: float = 0.0
    discount_rate: float = DEFAULT_DISCOUNT_RATE


def quarterly_dps(policy: DividendPolicy, eps: float) -> float:
    """DPS for one quarter, dispatched on policy type (METHODOLOGY.md 4.3).

    ``floor`` is the EPS threshold deducted before the payout; ``base`` is either
    a minimum floor under the dividend (``variable``) or an always-paid base on
    top of the variable part (``base_plus_variable``).
    """
    variable = policy.payout_ratio * max(0.0, eps - policy.floor)
    if policy.policy_type == "base_plus_variable":
        return policy.base_dividend_per_share + variable
    return max(policy.base_dividend_per_share, variable)


def _disclosed_charter_rates(inputs: CompanyInputs) -> dict[str, float]:
    """Per-class average of disclosed charter rates among time-chartered vessels."""
    sums: dict[str, float] = {}
    counts: dict[str, float] = {}
    for v in inputs.fleet.vessels:
        if v.charter_status == "time_charter" and v.charter_rate is not None:
            sums[v.cls] = sums.get(v.cls, 0.0) + float(v.charter_rate) * v.count
            counts[v.cls] = counts.get(v.cls, 0.0) + v.count
    return {cls: sums[cls] / counts[cls] for cls in sums}


def _class_counts(inputs: CompanyInputs) -> dict[str, float]:
    """Static earning-fleet counts per class (sums sister-vessel counts)."""
    counts: dict[str, float] = {}
    for v in inputs.fleet.vessels:
        counts[v.cls] = counts.get(v.cls, 0.0) + v.count
    return counts


def _quarter_count(inputs: CompanyInputs, cls: str, q: int, static: float) -> float:
    """Earning-fleet count for class in strip quarter q (0-indexed).

    Uses the manifest's ``fleet_schedule`` if provided (to capture newbuild
    deliveries / sales over the horizon), else the static count.
    """
    schedule = inputs.fleet.fleet_schedule.get(cls)
    if schedule and q < len(schedule):
        return schedule[q]
    return static


def _blended_tce_by_class(inputs: CompanyInputs, q: int) -> dict[str, float]:
    """TCE_class for strip quarter q (0-indexed): scenario/FFA + charter blend.

    Coverage cov_q earns the disclosed contracted rate; (1 - cov_q) earns the
    scenario/FFA rate. cov_q comes from the manifest's per-quarter
    ``coverage_schedule`` when present (METHODOLOGY §11.8.6 — issuer-disclosed
    %-days-fixed, decaying as charters expire); otherwise the static
    (1 - spot_coverage_pct), which is exactly the pre-§11.8 blend.
    """
    md = inputs.market_data
    charter_rates = _disclosed_charter_rates(inputs)
    out: dict[str, float] = {}
    for cls in _class_counts(inputs):
        ffa = md.ffa_forward_curve.get(cls)
        if not ffa:
            raise ValueError(f"no FFA forward curve for class {cls!r}")
        ffa_q = ffa[q]
        schedule = inputs.fleet.coverage_schedule.get(cls)
        if schedule:
            cov = schedule[q] if q < len(schedule) else schedule[-1]
        else:
            cov = 1.0 - inputs.fleet.spot_coverage_pct.get(cls, 1.0)
        charter_rate = charter_rates.get(cls, ffa_q)  # fall back to FFA if none disclosed
        out[cls] = (1.0 - cov) * ffa_q + cov * charter_rate
    return out


def _terminal_nav(inputs: CompanyInputs, quarters_forward: int) -> NavResult:
    """NAV breakdown with the fleet aged forward, balance sheet held constant.

    Returns the full ``NavResult`` so the caller can apply the cycle-conditional
    multiple to the FLEET value only and add retained earnings in per-share space
    (METHODOLOGY §9.2). A newbuild delivered before the terminal date drops its
    time-to-delivery discount (§9.6) and starts aging from delivery; one still
    pending keeps a reduced discount. ``years_to_delivery`` defaults to 0 (on the
    water), so an existing fleet just ages by ``years`` exactly as before."""
    years = quarters_forward / 4.0
    aged_vessels = [
        replace(
            v,
            age=v.age + max(0.0, years - v.years_to_delivery),
            years_to_delivery=max(0.0, v.years_to_delivery - years),
        )
        for v in inputs.fleet.vessels
    ]
    aged = replace(inputs, fleet=replace(inputs.fleet, vessels=aged_vessels))
    return compute_nav(aged)


def compute_dividend_strip(
    inputs: CompanyInputs,
    nav_per_share: float,
    discount_rate: float = DEFAULT_DISCOUNT_RATE,
    offhire_rate: float = DEFAULT_OFFHIRE_RATE,
    strip_horizon: int = STRIP_HORIZON_QUARTERS,
    terminal_multiple: float = TERMINAL_NAV_MULTIPLE,
) -> DividendStripResult:
    """Project ``strip_horizon`` quarters of DPS, discount, and add the
    NAV-based terminal value.

    ``strip_horizon`` is a per-sector parameter (METHODOLOGY §11.8.6.4):
    default 8 (FFA-liquidity argument, crude/lng/product/dry_bulk);
    containerships run longer because their forward cash is contracted
    backlog, not an FFA extrapolation. ``run_scenarios`` passes the sector
    doc's ``strip_horizon``.

    ``nav_per_share`` is the current NAV (for reference); the terminal value is
    recomputed from the aged fleet rather than depreciating this figure.
    """
    pol = inputs.dividend_policy
    cost = inputs.cost_structure
    md = inputs.market_data
    shares = inputs.balance_sheet.diluted_shares_outstanding
    counts = _class_counts(inputs)

    quarterly_gna = cost.annual_G_and_A / 4.0
    quarterly_interest = cost.annual_interest_expense / 4.0

    dps_by_q: list[float] = []
    eps_by_q: list[float] = []
    netrev_by_q: list[float] = []
    tce_by_class: dict[str, list[float]] = {cls: [] for cls in counts}
    ffa_spot_by_class: dict[str, list[float]] = {cls: [] for cls in counts}

    for q in range(strip_horizon):
        tce = _blended_tce_by_class(inputs, q)
        net_tce_revenue = 0.0
        opex = 0.0
        for cls, static_n in counts.items():
            n = _quarter_count(inputs, cls, q, static_n)
            vessel_days = n * DAYS_PER_QUARTER
            net_tce_revenue += vessel_days * tce[cls] * (1.0 - offhire_rate)
            opex += vessel_days * cost.opex_per_day.get(cls, 0.0)
            tce_by_class[cls].append(tce[cls])
            ffa_spot_by_class[cls].append(md.ffa_forward_curve[cls][q])

        pretax = net_tce_revenue - opex - quarterly_gna - quarterly_interest
        tax = cost.effective_tax_rate * max(0.0, pretax)
        eps = (pretax - tax) / shares
        dps = quarterly_dps(pol, eps)

        netrev_by_q.append(net_tce_revenue)
        eps_by_q.append(eps)
        dps_by_q.append(dps)

    ffa_12m_by_class = {cls: twelve_month_ffa(md.ffa_forward_curve[cls]) for cls in counts}

    discounted_dps = [
        dps / (1.0 + discount_rate) ** ((q + 1) / 4.0) for q, dps in enumerate(dps_by_q)
    ]

    # Terminal value (METHODOLOGY §9.2/§10/§12.1, owner 2026-06-22):
    #   (1) the fleet is aged forward and its asset-price level is mean-reverted by
    #       the CYCLE-CONDITIONAL ``terminal_multiple`` (peak 0.9x … trough 1.1x) —
    #       applied to the FLEET value only; cash/debt do not mean-revert;
    #   (2) the balance sheet carries forward RETAINED EARNINGS over the strip
    #       (terminal cash += sum(EPS - DPS) per share) — dividends paid are value
    #       extraction, retained earnings accrete; high-payout names net ~flat,
    #       low-payout retainers rise, names paying out more than they earn fall.
    aged = _terminal_nav(inputs, strip_horizon + 1)
    shares = inputs.balance_sheet.diluted_shares_outstanding
    fleet_per_share = aged.fleet_value / shares
    balance_sheet_per_share = aged.nav_per_share - fleet_per_share
    retained_per_share = sum(eps_by_q) - sum(dps_by_q)
    terminal = (
        terminal_multiple * fleet_per_share + balance_sheet_per_share + retained_per_share
    )
    # Governance / value-trap haircut (METHODOLOGY §15): the strip terminal
    # is a NAV realisation and carries the same discount as the blended NAV
    # term. Interim DPS are NOT haircut (already realised cash). Defaults
    # to 0 (no haircut) for the standard watchlist names.
    terminal *= (1.0 - inputs.balance_sheet.governance_discount_pct)
    discounted_terminal = terminal / (1.0 + discount_rate) ** (
        (strip_horizon + 1) / 4.0
    )

    return DividendStripResult(
        dps_by_quarter=dps_by_q,
        eps_by_quarter=eps_by_q,
        net_tce_revenue_by_quarter=netrev_by_q,
        blended_tce_by_quarter=tce_by_class,
        ffa_spot_by_quarter=ffa_spot_by_class,
        ffa_12m_by_class=ffa_12m_by_class,
        discounted_dps=discounted_dps,
        terminal_value=terminal,
        discounted_terminal_value=discounted_terminal,
        implied_price=sum(discounted_dps) + discounted_terminal,
        discount_rate=discount_rate,
    )
