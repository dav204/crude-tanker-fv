"""Crude carve-out for hybrid operators (METHODOLOGY.md section 6; INSW).

Models the CRUDE sleeve (VLCC / Suezmax / Aframax) only, allocating the whole-
company balance sheet and corporate costs to it. Allocation basis = vessel
MARKET VALUE (stable across cycles and the broker-NAV convention), NOT EBITDA
(cycle-distorted: war years skew the segment mix toward crude).

Debt: vessel-secured debt is allocated DIRECTLY to its sleeve
(``crude_specific_debt`` / ``product_specific_debt``); only the remaining
corporate / unsecured debt is pro-rated by crude vessel-value share. If a name's
debt is essentially all corporate, leave the specific-debt fields at 0 and the
whole stack pro-rates.

The returned crude-only ``CompanyInputs`` flows through the normal NAV / strip /
cycle / blend / scenario pipeline unchanged. Compare its outputs to the
crude-allocated price (``price * crude_share``) — see ``carved_price``.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from .schemas import CompanyInputs
from .vessel_values import vessel_market_value

# Default sleeve by class when a vessel isn't explicitly tagged. LR2 defaults to
# crude (FRO's dual-use proxy); a product operator tags its LR2s sleeve: product.
CRUDE_CLASSES = {"VLCC", "Suezmax", "Aframax", "LR2"}
PRODUCT_CLASSES = {"MR", "LR1", "Handysize", "Handymax"}
LNG_CLASSES = {"LNGC", "MGC"}


def _sleeve_for(vessel) -> str:
    """Sleeve assignment for a vessel: 'crude' | 'product' | 'lng'.

    LNG-class vessels always go LNG. Product-class vessels (or any vessel
    explicitly tagged ``sleeve: product``) go product. Anything explicitly
    tagged ``sleeve: lng`` goes LNG. Everything else defaults to crude.
    This preserves the pre-3-sleeve behavior — ``vessel.sleeve`` defaults to
    ``"crude"`` so the class-default wins unless explicitly overridden.
    """
    if vessel.cls in LNG_CLASSES or vessel.sleeve == "lng":
        return "lng"
    if vessel.cls in PRODUCT_CLASSES or vessel.sleeve == "product":
        return "product"
    return "crude"


def _sleeve_fractions(vessel) -> tuple[float, float, float]:
    """Return (crude, product, lng) split for a vessel (sums to 1.0).

    Dual-use LR1 (``crude_fraction`` set) splits between crude and product.
    Other vessels go 100% to the sleeve from ``_sleeve_for``.
    """
    if vessel.crude_fraction is not None:
        cf = float(vessel.crude_fraction)
        return cf, 1.0 - cf, 0.0
    sleeve = _sleeve_for(vessel)
    if sleeve == "crude":
        return 1.0, 0.0, 0.0
    if sleeve == "product":
        return 0.0, 1.0, 0.0
    return 0.0, 0.0, 1.0


def sleeve_values(inputs: CompanyInputs) -> tuple[float, float, float]:
    """Whole-company vessel value split across (crude, product, lng) sleeves.

    Single source of truth for the 3-sleeve denominator. Used by all three
    carve-out functions so the shares sum to 1.0 across the whole company
    (METHODOLOGY §6 v2 / §11.6).
    """
    md = inputs.market_data
    yard_discounts = md.yard_discounts
    crude_v = product_v = lng_v = 0.0
    for v in inputs.fleet.vessels:
        value = vessel_market_value(v, md.vessel_value_curves[v.cls], yard_discounts) * v.count
        cf, pf, lf = _sleeve_fractions(v)
        crude_v += value * cf
        product_v += value * pf
        lng_v += value * lf
    return crude_v, product_v, lng_v


@dataclass
class CarveOut:
    """Result of a crude carve-out."""

    crude_inputs: CompanyInputs   # crude-only fleet + allocated balance sheet/costs
    crude_share: float            # crude vessel value / total vessel value
    crude_value: float
    product_value: float

    def carved_price(self, whole_company_price: float) -> float:
        """The crude sleeve's share of the whole-company price (for comparison)."""
        return whole_company_price * self.crude_share


def _crude_fraction(vessel) -> float:
    """Fraction of a vessel attributed to the crude sleeve (0..1).

    Thin wrapper around ``_sleeve_fractions`` returning only the crude share —
    kept for backwards compatibility with call sites that only care about crude.
    """
    return _sleeve_fractions(vessel)[0]


def crude_carve_out(inputs: CompanyInputs) -> CarveOut:
    """Carve the crude sleeve out of a hybrid operator's whole-company inputs.

    Each vessel's market value is split across (crude, product, lng) sleeves
    via ``_sleeve_fractions``; a dual-use LR1 contributes its crude portion to
    the crude fleet at a fractional count. Crude share is computed against the
    WHOLE-COMPANY value (crude + product + lng) so the three sleeves' shares
    sum to 1.0 (METHODOLOGY §6 v2 / §11.6).
    """
    md = inputs.market_data
    yard_discounts = md.yard_discounts

    crude_value, product_value, lng_value = sleeve_values(inputs)
    crude_vessels = []
    for v in inputs.fleet.vessels:
        cf = _crude_fraction(v)
        if cf > 0.0:
            crude_vessels.append(replace(v, count=v.count * cf, crude_fraction=None))

    total = crude_value + product_value + lng_value
    crude_share = crude_value / total if total else 1.0

    bs = inputs.balance_sheet
    corporate_debt = bs.total_debt - bs.crude_specific_debt - bs.product_specific_debt
    crude_debt = bs.crude_specific_debt + corporate_debt * crude_share
    crude_bs = replace(
        bs,
        cash_and_equivalents=bs.cash_and_equivalents * crude_share,
        working_capital_net=bs.working_capital_net * crude_share,
        total_debt=crude_debt,
        lease_liabilities=bs.lease_liabilities * crude_share,
        newbuild_capex_commitments=bs.newbuild_capex_commitments * crude_share,
        newbuild_advances_paid=bs.newbuild_advances_paid * crude_share,
        # Preferred equity is a corporate-stack claim (no vessel-secured
        # equivalent); pro-rate by sleeve like corporate/unsecured debt.
        preferred_equity=bs.preferred_equity * crude_share,
        # Shuttle contracted-book is a vessel-specific asset that lives outside
        # the crude/product/lng vessel-class taxonomy. Pro-rate as a corporate-
        # stack item — same treatment as preferred_equity. A future 4th sleeve
        # could allocate it directly to the shuttle sleeve (METHODOLOGY §11.6).
        shuttle_contracted_book=bs.shuttle_contracted_book * crude_share,
        crude_specific_debt=0.0,
        product_specific_debt=0.0,
    )

    cost = inputs.cost_structure
    crude_cost = replace(
        cost,
        annual_G_and_A=cost.annual_G_and_A * crude_share,
        annual_interest_expense=cost.annual_interest_expense * crude_share,
    )

    crude_inputs = replace(
        inputs,
        fleet=replace(inputs.fleet, vessels=crude_vessels),
        balance_sheet=crude_bs,
        cost_structure=crude_cost,
    )
    return CarveOut(crude_inputs, crude_share, crude_value, product_value)


# Per-class rate-data remap for the product sleeve (METHODOLOGY 6 v2). LR1/LR2
# vessels in the product sleeve earn at CLEAN rates (not the dirty/Aframax-equiv
# values used for crude carve-outs). MR is product-only. The remap below points
# each product-fleet vessel-class to the CORRECT rate key in market_data:
#   * MR keeps its own 'MR' entries
#   * LR1 in product trades clean -> map to LR1_clean entries (v1 proxy
#       lr2_clean rates since liquid LR1_clean curves are scarce)
#   * LR2 in product trades clean -> map to LR2_clean entries
_PRODUCT_RATE_REMAP = {
    "MR": "MR",
    "LR1": "LR1_clean",
    "LR2": "LR2_clean",
}


def _remap_rates_for_product(md):
    """Replace LR1 / LR2 / MR entries in rate dicts with the clean variants.

    Leaves other classes' entries intact. For each (rate_dict, src_key, dst_key)
    pair: if dst_key exists, overwrite dst_key with src_key's value, then drop
    src_key when src_key != dst_key. This way the vessel's cls field still
    routes (e.g. an LR1 vessel looks up md.spot_tce['LR1']) but to clean values.
    """
    def _apply(d: dict) -> dict:
        out = dict(d)
        for vessel_key, rate_key in _PRODUCT_RATE_REMAP.items():
            if rate_key in d:
                out[vessel_key] = d[rate_key]
        return out
    return replace(
        md,
        spot_tce=_apply(md.spot_tce),
        twelve_month_tc=_apply(md.twelve_month_tc),
        historical_tce_means=_apply(md.historical_tce_means),
        ffa_forward_curve=_apply(md.ffa_forward_curve),
    )


@dataclass
class ProductCarveOut:
    """Result of the product carve-out — mirror of CarveOut for the product sleeve."""

    product_inputs: CompanyInputs   # product-only fleet + allocated balance sheet/costs
    product_share: float            # product vessel value / total vessel value
    product_value: float
    crude_value: float

    def carved_price(self, whole_company_price: float) -> float:
        """The product sleeve's share of the whole-company price (for comparison)."""
        return whole_company_price * self.product_share


def product_carve_out(inputs: CompanyInputs) -> ProductCarveOut:
    """Carve the PRODUCT sleeve out of a hybrid operator's whole-company inputs.

    Mirror of ``crude_carve_out``. Vessel value splits across the (crude,
    product, lng) sleeves via ``_sleeve_fractions``; the product portion
    (count × pf) enters the product fleet. Balance sheet pro-rated by
    product vessel-value share (against the WHOLE-COMPANY denominator
    crude + product + lng). Market data re-mapped so LR1/LR2/MR rate dict
    entries point at the CLEAN variants (see ``_remap_rates_for_product``),
    so the existing strip / cycle machinery works unchanged via the vessel's
    existing cls field.
    """
    md = inputs.market_data
    yard_discounts = md.yard_discounts

    crude_value, product_value, lng_value = sleeve_values(inputs)
    product_vessels = []
    for v in inputs.fleet.vessels:
        cf, pf, lf = _sleeve_fractions(v)
        if pf > 0.0:
            product_vessels.append(replace(v, count=v.count * pf, crude_fraction=None))

    total = crude_value + product_value + lng_value
    product_share = product_value / total if total else 0.0

    bs = inputs.balance_sheet
    corporate_debt = bs.total_debt - bs.crude_specific_debt - bs.product_specific_debt
    product_debt = bs.product_specific_debt + corporate_debt * product_share
    product_bs = replace(
        bs,
        cash_and_equivalents=bs.cash_and_equivalents * product_share,
        working_capital_net=bs.working_capital_net * product_share,
        total_debt=product_debt,
        lease_liabilities=bs.lease_liabilities * product_share,
        newbuild_capex_commitments=bs.newbuild_capex_commitments * product_share,
        newbuild_advances_paid=bs.newbuild_advances_paid * product_share,
        # Preferred equity pro-rates as a corporate-stack item (mirror crude sleeve).
        preferred_equity=bs.preferred_equity * product_share,
        shuttle_contracted_book=bs.shuttle_contracted_book * product_share,
        crude_specific_debt=0.0,
        product_specific_debt=0.0,
    )

    cost = inputs.cost_structure
    product_cost = replace(
        cost,
        annual_G_and_A=cost.annual_G_and_A * product_share,
        annual_interest_expense=cost.annual_interest_expense * product_share,
    )

    product_inputs = replace(
        inputs,
        fleet=replace(inputs.fleet, vessels=product_vessels),
        balance_sheet=product_bs,
        cost_structure=product_cost,
        market_data=_remap_rates_for_product(md),
    )
    return ProductCarveOut(product_inputs, product_share, product_value, crude_value)


# Week-over-week product-vs-crude TCE moves (VIE, 2026-05-29). Product is
# LEADING the MoU normalization, not lagging it — so a product NAV held at
# current Compass values likely OVERSTATES fair value once a v2 product strip
# is added (the product sleeve carries MORE downside than crude, not less).
PRODUCT_RATE_WOW = {
    "MR (product)": -0.52, "LR2 (product)": -0.28,
    "Aframax (dirty crude)": -0.07, "Suezmax (crude)": -0.07, "VLCC (crude)": -0.08,
}


@dataclass
class LngCarveOut:
    """Result of the LNG carve-out — mirror of CarveOut for the LNG sleeve."""

    lng_inputs: CompanyInputs       # LNG-only fleet + allocated balance sheet/costs
    lng_share: float                # LNG vessel value / whole-company vessel value
    lng_value: float
    crude_value: float
    product_value: float

    def carved_price(self, whole_company_price: float) -> float:
        """The LNG sleeve's share of the whole-company price (for comparison)."""
        return whole_company_price * self.lng_share


def lng_carve_out(inputs: CompanyInputs) -> LngCarveOut:
    """Carve the LNG sleeve out of a 3-sector hybrid's whole-company inputs.

    Mirror of ``crude_carve_out`` / ``product_carve_out`` for LNGC + MGC
    vessels. Pro-rates balance sheet by lng vessel-value share against the
    whole-company (crude + product + lng) denominator. No rate remap needed —
    LNG classes already index their own rate keys (LNGC / MGC) in market_data.

    Currently used by 3-sleeve hybrids (TEN). Returns an LNG sleeve whose
    fleet contains only LNGC / MGC vessels (and any vessel explicitly tagged
    ``sleeve: lng``).
    """
    md = inputs.market_data

    crude_value, product_value, lng_value = sleeve_values(inputs)
    lng_vessels = []
    for v in inputs.fleet.vessels:
        cf, pf, lf = _sleeve_fractions(v)
        if lf > 0.0:
            lng_vessels.append(replace(v, count=v.count * lf, crude_fraction=None))

    total = crude_value + product_value + lng_value
    lng_share = lng_value / total if total else 0.0

    bs = inputs.balance_sheet
    # LNG carriers are typically corporate-financed (no LNG-specific debt
    # tagging convention yet). Pro-rate the full corporate debt stack by share.
    corporate_debt = bs.total_debt - bs.crude_specific_debt - bs.product_specific_debt
    lng_debt = corporate_debt * lng_share
    lng_bs = replace(
        bs,
        cash_and_equivalents=bs.cash_and_equivalents * lng_share,
        working_capital_net=bs.working_capital_net * lng_share,
        total_debt=lng_debt,
        lease_liabilities=bs.lease_liabilities * lng_share,
        newbuild_capex_commitments=bs.newbuild_capex_commitments * lng_share,
        newbuild_advances_paid=bs.newbuild_advances_paid * lng_share,
        preferred_equity=bs.preferred_equity * lng_share,
        shuttle_contracted_book=bs.shuttle_contracted_book * lng_share,
        crude_specific_debt=0.0,
        product_specific_debt=0.0,
    )

    cost = inputs.cost_structure
    lng_cost = replace(
        cost,
        annual_G_and_A=cost.annual_G_and_A * lng_share,
        annual_interest_expense=cost.annual_interest_expense * lng_share,
    )

    lng_inputs = replace(
        inputs,
        fleet=replace(inputs.fleet, vessels=lng_vessels),
        balance_sheet=lng_bs,
        cost_structure=lng_cost,
    )
    return LngCarveOut(lng_inputs, lng_share, lng_value, crude_value, product_value)


def product_read(carve: CarveOut, crude_ev_pct: float) -> str:
    """Qualitative product-sleeve paragraph to accompany the crude carve-out (v1)."""
    product_share = 1.0 - carve.crude_share
    return (
        f"Crude sleeve (this model): {crude_ev_pct:+.0f}% vs the crude-allocated price. "
        f"Product sleeve (qualitative, awaiting v2): ~{product_share:.0%} of vessel value, "
        f"held at current Compass values. Product rates have corrected MORE than crude "
        f"week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product "
        f"is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES "
        f"fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2."
    )
