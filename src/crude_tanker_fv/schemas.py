"""Input data structures (METHODOLOGY.md section 4).

These dataclasses mirror the YAML schemas under ``inputs/`` one-to-one.
They define the *shape* of the inputs only — no valuation logic lives here.
Field names match the YAML keys in section 4 so loaders can map directly.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

# Vessel classes recognised by the model. LR2 is technically a product class;
# its inclusion for FRO is an open decision (METHODOLOGY.md sections 6, 9.3).
VesselClass = str  # one of: "VLCC", "Suezmax", "Aframax", "LR2"
CharterStatus = str  # one of: "spot", "time_charter"


@dataclass
class Vessel:
    """A vessel (or a group of identical sister vessels) in a fleet manifest (section 4.1)."""

    id: str
    cls: VesselClass
    dwt: int
    age: float
    scrubber: bool = False
    eco: bool = False
    charter_status: CharterStatus = "spot"
    charter_rate: Optional[float] = None  # USD/day if time_charter
    charter_end: Optional[str] = None  # ISO date if time_charter
    yard: Optional[str] = None  # building yard (drives the yard-quality discount)
    count: int = 1  # number of identical sister vessels this row represents
    sleeve: str = "crude"  # "crude" | "product" — for hybrid carve-outs (INSW)
    # Fraction of this vessel's value/earnings attributed to the crude sleeve in a
    # carve-out. None => binary by sleeve (1.0 crude / 0.0 product). Set e.g. 0.30
    # for dual-use LR1 (trades dirty ~30% of the time per the historical split).
    crude_fraction: Optional[float] = None
    # Years until a committed-but-undelivered newbuild is delivered. 0.0 => on the
    # water now (no time-to-delivery discount). >0 => compute_nav PV-discounts this
    # vessel's delivered-market value for the wait (METHODOLOGY §9.6). Defaults to
    # 0.0 so existing on-water fleets are unaffected.
    years_to_delivery: float = 0.0


@dataclass
class FleetManifest:
    """Fleet manifest: ``inputs/fleet_manifests/{ticker}.yaml`` (section 4.1)."""

    ticker: str
    report_date: str
    vessels: list[Vessel] = field(default_factory=list)
    spot_coverage_pct: dict[VesselClass, float] = field(default_factory=dict)
    fleet_summary: dict[str, float] = field(default_factory=dict)
    # Optional per-class per-quarter vessel counts for the dividend strip (8 values),
    # used when the earning fleet changes over the horizon (e.g. newbuild deliveries).
    # If absent, the strip uses the static manifest counts.
    fleet_schedule: dict[VesselClass, list[float]] = field(default_factory=dict)
    # Optional per-class per-quarter CHARTER COVERAGE (0..1) for the dividend
    # strip (METHODOLOGY §11.8.6): cov_q earns the disclosed contracted rate,
    # (1 - cov_q) re-fixes at the scenario rate. Built from issuer-disclosed
    # %-days-fixed by calendar year. If absent, the strip uses the static
    # (1 - spot_coverage_pct) — identical to the pre-§11.8 blend.
    coverage_schedule: dict[VesselClass, list[float]] = field(default_factory=dict)


@dataclass
class BalanceSheet:
    """Balance sheet snapshot: ``inputs/balance_sheets/{ticker}_{quarter}.yaml`` (section 4.2)."""

    ticker: str
    quarter: str
    cash_and_equivalents: float
    working_capital_net: float
    total_debt: float
    lease_liabilities: float
    newbuild_capex_commitments: float
    newbuild_advances_paid: float
    diluted_shares_outstanding: float
    # Vessel-secured debt allocated DIRECTLY to a sleeve in a hybrid carve-out
    # (the rest of total_debt is corporate/unsecured and pro-rated by vessel value).
    crude_specific_debt: float = 0.0
    product_specific_debt: float = 0.0
    # Preferred equity at liquidation preference value (sum across all series).
    # A creditor-like claim that subtracts from NAV ahead of common equity.
    # Defaults to 0 (no current watchlist name has preferreds); set for names
    # like TEN (~$287M across multiple series per stale VIE). Pro-rated as a
    # corporate-stack item in hybrid carve-outs (METHODOLOGY §4.2).
    preferred_equity: float = 0.0
    # DP2-shuttle / contract-anchored asset sleeve carried at NPV of contracted
    # cash flows (off-curve-at-contracted-book convention, METHODOLOGY §11.6).
    # Adds to NAV like working_capital_net. Defaults to 0; populated only for
    # names with contracted-book shuttle exposure (TEN). Pro-rates by sleeve
    # in hybrid carve-outs the same way working capital does — but typically
    # belongs to whichever sleeve carries the shuttle vessels in the carveout
    # split (treat as a corporate-stack item if shuttle is its own sleeve).
    shuttle_contracted_book: float = 0.0
    # Governance / structural-NAV-trap discount as a fraction in [0, 1]
    # (METHODOLOGY §15). Captures the persistent P/NAV compression the
    # market applies to controlled-FPI / low-payout / related-party
    # structures where common shareholders are unlikely to capture the full
    # asset NAV. Applied as a haircut to the NAV term of the blended FV
    # (blend.py) and the strip's terminal value (dividend_strip.py) — both
    # are realisation-of-NAV computations. Defaults to 0 (no haircut).
    # Set per-name based on observed multi-year median P/NAV vs peer group;
    # judgmental. Pro-rates as a corporate-stack item in hybrid carve-outs
    # (same scalar applies to each sleeve).
    governance_discount_pct: float = 0.0


@dataclass
class DividendPolicy:
    """Dividend policy: ``inputs/dividend_policies/{ticker}.yaml`` (section 4.3)."""

    ticker: str
    policy_type: str  # e.g. "variable"
    payout_ratio: float
    base_dividend_per_share: float = 0.0
    floor: float = 0.0


@dataclass
class CostStructure:
    """Cost structure: ``inputs/cost_structures/{ticker}.yaml`` (section 4.4)."""

    ticker: str
    opex_per_day: dict[VesselClass, float] = field(default_factory=dict)
    annual_G_and_A: float = 0.0
    annual_interest_expense: float = 0.0
    effective_tax_rate: float = 0.0


@dataclass
class VesselValueCurve:
    """Per-class value anchors used to build the age->value curve (section 3.1).

    Mirrors one class entry in ``inputs/market_data/vessel_value_curves.yaml``.
    Four age anchors (0 / 5 / 10 / 25 years) are taken from the broker term
    structure; the curve is piecewise-linear between them.
    """

    cls: VesselClass
    dwt: int
    newbuild: float            # age 0 (prompt/resale value)
    five_year_benchmark: float  # age 5
    ten_year_benchmark: float   # age 10
    scrap_25yr: float           # age 25
    scrubber_premium: float = 0.0
    eco_premium_pct: float = 0.05


@dataclass
class MarketData:
    """Market data bundle (section 4.5).

    Aggregates the four files under ``inputs/market_data/``.
    """

    vessel_value_curves: dict[VesselClass, VesselValueCurve] = field(default_factory=dict)
    spot_tce: dict[VesselClass, float] = field(default_factory=dict)
    ffa_forward_curve: dict[VesselClass, list[float]] = field(default_factory=dict)  # 8 quarters
    twelve_month_tc: dict[VesselClass, float] = field(default_factory=dict)  # 12M TC, cycle input
    historical_tce_means: dict[VesselClass, float] = field(default_factory=dict)  # 10yr mean
    yard_discounts: dict[str, float] = field(default_factory=dict)  # yard name -> fractional haircut


@dataclass
class CompanyInputs:
    """All per-company inputs bundled for a valuation run."""

    fleet: FleetManifest
    balance_sheet: BalanceSheet
    dividend_policy: DividendPolicy
    cost_structure: CostStructure
    market_data: MarketData
