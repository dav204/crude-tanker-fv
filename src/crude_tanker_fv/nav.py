"""NAV per share (METHODOLOGY.md section 3.1).

    NAV/share = (Sum vessel_market_values
                 + cash_and_equivalents
                 + working_capital_net
                 - total_debt
                 - lease_liabilities
                 - newbuild_capex_commitments
                 + advances_paid_on_newbuilds)
                / diluted_shares_outstanding

Vessel market values come from ``vessel_values``. Vessels still under
construction are NOT valued on the curve; they enter only through the newbuild
capex / advances balance-sheet lines (open decision 9.6).
"""

from __future__ import annotations

from dataclasses import dataclass

from .schemas import CompanyInputs
from .vessel_values import vessel_market_value

# Canonical cost of equity (≈ high-beta cyclical equity discount, METHODOLOGY §3.2/§9.5).
# ONE 0.11 shared by the newbuild time-to-delivery PV discount AND the dividend-strip
# discount (dividend_strip.DEFAULT_DISCOUNT_RATE), so the two cannot silently diverge
# (BUG-7, 2026-06-22).
COST_OF_EQUITY = 0.11

# Time-to-delivery discount for committed-but-undelivered newbuilds (METHODOLOGY §9.6).
# A newbuild arriving in t years is worth its delivered-market value discounted to today
# at the cost of equity. Applied per-vessel via `years_to_delivery` (0 => on the water =>
# factor 1.0, so existing fleets are unaffected). The remaining capex commitment is kept
# at face on the balance sheet (conservative; PV-ing the payment schedule is a refinement).
NEWBUILD_DELIVERY_DISCOUNT_RATE = COST_OF_EQUITY


@dataclass
class NavResult:
    """NAV breakdown for the per-company report (section 7)."""

    fleet_value: float
    cash_and_equivalents: float
    working_capital_net: float
    total_debt: float
    lease_liabilities: float
    newbuild_capex_commitments: float
    newbuild_advances_paid: float
    diluted_shares_outstanding: float
    nav_total: float
    nav_per_share: float
    fleet_value_by_class: dict[str, float]
    # Same NAV but valuing vessels at par (no yard-quality discount), so the
    # report can show the discount's impact transparently.
    fleet_value_ex_yard_discount: float = 0.0
    nav_per_share_ex_yard_discount: float = 0.0
    # Preferred-equity claim subtracted from NAV (creditor-like; ahead of
    # common). Defaults to 0 for current watchlist names; non-zero only when
    # the balance sheet declares it (METHODOLOGY §4.2).
    preferred_equity: float = 0.0
    # Off-curve shuttle / contract-anchored sleeve carried at NPV of contracted
    # cash flows (METHODOLOGY §11.6). Adds to NAV; defaults to 0.
    shuttle_contracted_book: float = 0.0
    # Governance / value-trap discount (METHODOLOGY §15). Exposed here for
    # transparency; the haircut is applied at the blend layer and on the
    # dividend strip's terminal value, NOT inside compute_nav (so the broker
    # NAV sweep and other asset-side diagnostics see undiscounted asset NAV).
    governance_discount_pct: float = 0.0


def compute_nav(inputs: CompanyInputs) -> NavResult:
    """Compute NAV total and NAV/share with a per-class fleet breakdown.

    Vessels are valued with the yard-quality discount applied; the fleet value
    at par (no discount) is also returned for transparency. Each manifest row
    counts ``vessel.count`` identical sisters.
    """
    curves = inputs.market_data.vessel_value_curves
    yard_discounts = inputs.market_data.yard_discounts

    fleet_value = 0.0
    fleet_value_ex = 0.0
    by_class: dict[str, float] = {}
    for vessel in inputs.fleet.vessels:
        curve = curves.get(vessel.cls)
        if curve is None:
            raise ValueError(f"no vessel value curve for class {vessel.cls!r}")
        # PV-discount a not-yet-delivered newbuild's delivered value for the wait
        # to delivery (§9.6). years_to_delivery defaults to 0 (on the water) ->
        # pv 1.0, so on-water fleets are unaffected.
        pv = (
            (1.0 + NEWBUILD_DELIVERY_DISCOUNT_RATE) ** (-vessel.years_to_delivery)
            if vessel.years_to_delivery
            else 1.0
        )
        value = vessel_market_value(vessel, curve, yard_discounts) * vessel.count * pv
        value_ex = vessel_market_value(vessel, curve, None) * vessel.count * pv
        fleet_value += value
        fleet_value_ex += value_ex
        by_class[vessel.cls] = by_class.get(vessel.cls, 0.0) + value

    bs = inputs.balance_sheet
    balance_sheet_net = (
        bs.cash_and_equivalents
        + bs.working_capital_net
        - bs.total_debt
        - bs.lease_liabilities
        - bs.newbuild_capex_commitments
        + bs.newbuild_advances_paid
        - bs.preferred_equity              # preferred claim ahead of common (§4.2)
        + bs.shuttle_contracted_book       # off-curve shuttle NPV (§11.6)
    )
    nav_total = fleet_value + balance_sheet_net
    nav_per_share = nav_total / bs.diluted_shares_outstanding
    nav_per_share_ex = (fleet_value_ex + balance_sheet_net) / bs.diluted_shares_outstanding

    return NavResult(
        fleet_value=fleet_value,
        cash_and_equivalents=bs.cash_and_equivalents,
        working_capital_net=bs.working_capital_net,
        total_debt=bs.total_debt,
        lease_liabilities=bs.lease_liabilities,
        newbuild_capex_commitments=bs.newbuild_capex_commitments,
        newbuild_advances_paid=bs.newbuild_advances_paid,
        diluted_shares_outstanding=bs.diluted_shares_outstanding,
        nav_total=nav_total,
        nav_per_share=nav_per_share,
        fleet_value_by_class=by_class,
        fleet_value_ex_yard_discount=fleet_value_ex,
        nav_per_share_ex_yard_discount=nav_per_share_ex,
        preferred_equity=bs.preferred_equity,
        shuttle_contracted_book=bs.shuttle_contracted_book,
        governance_discount_pct=bs.governance_discount_pct,
    )
