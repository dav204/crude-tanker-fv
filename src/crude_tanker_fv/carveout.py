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
# Dry-bulk + container classes added 2026-06-26 for the first crude+dry_bulk+
# container multi-sleeve hybrid (CMBT, METHODOLOGY §11.9). Before this, every
# dry_bulk/container class fell through to the crude sleeve (a latent bug that
# only mattered once a name carried those classes through a carve-out).
DRY_BULK_CLASSES = {"Cape", "Pana", "Post-Panamax", "Supra-Ultra"}
CONTAINER_CLASSES = {"Ctr-Feeder", "Ctr-Intermediate", "Ctr-Large"}


def _sleeve_for(vessel) -> str:
    """Sleeve/sector assignment for a vessel.

    Sector by vessel class, with an explicit ``vessel.sleeve`` override per
    sector. The crude/product/lng branches are byte-identical to the pre-multi-
    sleeve behaviour (``vessel.sleeve`` defaults to ``"crude"`` so the class
    wins unless explicitly overridden to a non-crude sector); dry_bulk +
    container are added on the same "class OR explicit tag" pattern.
    """
    if vessel.cls in LNG_CLASSES or vessel.sleeve == "lng":
        return "lng"
    if vessel.cls in PRODUCT_CLASSES or vessel.sleeve == "product":
        return "product"
    if vessel.cls in DRY_BULK_CLASSES or vessel.sleeve == "dry_bulk":
        return "dry_bulk"
    if vessel.cls in CONTAINER_CLASSES or vessel.sleeve == "containerships":
        return "containerships"
    return "crude"


def _sleeve_fractions_by_sector(vessel) -> dict[str, float]:
    """Fraction of a vessel's market value by sector (values sum to 1.0).

    Dual-use LR1 (``crude_fraction`` set) splits between crude and product;
    every other vessel goes 100% to the sector from ``_sleeve_for``. The
    N-sector generalisation of ``_sleeve_fractions`` (METHODOLOGY §11.9) — the
    single source of truth both the 3-tuple shim and ``sector_carve_out`` build on.
    """
    if vessel.crude_fraction is not None:
        cf = float(vessel.crude_fraction)
        return {"crude": cf, "product": 1.0 - cf}
    return {_sleeve_for(vessel): 1.0}


def _sleeve_fractions(vessel) -> tuple[float, float, float]:
    """(crude, product, lng) split for a vessel — back-compat 3-tuple shim.

    Derived from ``_sleeve_fractions_by_sector``; a dry_bulk/container vessel
    returns (0, 0, 0) here (it belongs to neither of the three legacy sleeves),
    which is correct for the legacy carve-outs that only see crude/product/lng
    fleets.
    """
    d = _sleeve_fractions_by_sector(vessel)
    return d.get("crude", 0.0), d.get("product", 0.0), d.get("lng", 0.0)


def sleeve_values_by_sector(inputs: CompanyInputs) -> dict[str, float]:
    """Whole-company vessel value split across ALL sectors (METHODOLOGY §11.9).

    The N-sector denominator source of truth for ``sector_carve_out``. Sectors
    with no vessels are simply absent from the dict, so ``sum(...)`` over the
    values is the whole-company on-curve vessel value.
    """
    md = inputs.market_data
    yard_discounts = md.yard_discounts
    out: dict[str, float] = {}
    for v in inputs.fleet.vessels:
        value = vessel_market_value(v, md.vessel_value_curves[v.cls], yard_discounts) * v.count
        for sector, frac in _sleeve_fractions_by_sector(v).items():
            out[sector] = out.get(sector, 0.0) + value * frac
    return out


def sleeve_values(inputs: CompanyInputs) -> tuple[float, float, float]:
    """Whole-company vessel value split across (crude, product, lng) — 3-tuple shim.

    Single source of truth for the 3-sleeve denominator used by the three legacy
    carve-out functions (METHODOLOGY §6 v2 / §11.6). Derived from
    ``sleeve_values_by_sector``; byte-identical for crude/product/lng-only fleets.
    """
    d = sleeve_values_by_sector(inputs)
    return d.get("crude", 0.0), d.get("product", 0.0), d.get("lng", 0.0)


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


@dataclass
class SectorCarveOut:
    """Result of a single-sector carve-out (METHODOLOGY §11.9 multi-sleeve).

    The N-sector generalisation of ``CarveOut`` / ``ProductCarveOut`` /
    ``LngCarveOut``: one carve per sleeve sector, sharing the full whole-company
    ``all_values`` denominator so every sleeve's ``sleeve_share`` is taken
    against the same base and the shares across a name's sleeves sum to 1.0.
    """

    sector: str
    sleeve_inputs: CompanyInputs    # sector-only fleet + allocated balance sheet/costs
    sleeve_share: float             # this sector's vessel value / whole-company vessel value
    sleeve_value: float
    all_values: dict                # full {sector: vessel_value} split (for the aggregator/banner)

    def carved_price(self, whole_company_price: float) -> float:
        """This sleeve's share of the whole-company price (for comparison)."""
        return whole_company_price * self.sleeve_share


def sector_carve_out(inputs: CompanyInputs, sector: str) -> SectorCarveOut:
    """Carve ONE sleeve sector out of a multi-sleeve operator's whole-company inputs.

    Generalises ``crude_carve_out`` to an arbitrary sector. Vessel value splits
    across ALL sectors via ``sleeve_values_by_sector``; this sector's vessels
    (count × fraction) enter the sleeve fleet. The corporate stack pro-rates by
    this sleeve's vessel-value share against the WHOLE-COMPANY denominator
    (so all of a name's sleeves sum back to the whole company). Vessel-secured
    debt is allocated directly only where a per-sector field exists today
    (crude/product); dry_bulk + container have no specific-debt field, so their
    debt pro-rates as corporate (CMB.TECH finances at the corporate level —
    METHODOLOGY §11.9). The product sleeve gets the clean-rate remap, as in
    ``product_carve_out``.
    """
    values = sleeve_values_by_sector(inputs)
    total = sum(values.values()) or 1.0
    share = values.get(sector, 0.0) / total

    sleeve_vessels = []
    for v in inputs.fleet.vessels:
        frac = _sleeve_fractions_by_sector(v).get(sector, 0.0)
        if frac > 0.0:
            sleeve_vessels.append(replace(v, count=v.count * frac, crude_fraction=None))

    bs = inputs.balance_sheet
    specific = (bs.crude_specific_debt if sector == "crude"
                else bs.product_specific_debt if sector == "product" else 0.0)
    corporate_debt = bs.total_debt - bs.crude_specific_debt - bs.product_specific_debt
    sleeve_debt = specific + corporate_debt * share
    sleeve_bs = replace(
        bs,
        cash_and_equivalents=bs.cash_and_equivalents * share,
        working_capital_net=bs.working_capital_net * share,
        total_debt=sleeve_debt,
        lease_liabilities=bs.lease_liabilities * share,
        newbuild_capex_commitments=bs.newbuild_capex_commitments * share,
        newbuild_advances_paid=bs.newbuild_advances_paid * share,
        preferred_equity=bs.preferred_equity * share,
        shuttle_contracted_book=bs.shuttle_contracted_book * share,
        crude_specific_debt=0.0,
        product_specific_debt=0.0,
    )

    cost = inputs.cost_structure
    sleeve_cost = replace(
        cost,
        annual_G_and_A=cost.annual_G_and_A * share,
        annual_interest_expense=cost.annual_interest_expense * share,
    )

    md = inputs.market_data
    if sector == "product":
        md = _remap_rates_for_product(md)

    sleeve_inputs = replace(
        inputs,
        fleet=replace(inputs.fleet, vessels=sleeve_vessels),
        balance_sheet=sleeve_bs,
        cost_structure=sleeve_cost,
        market_data=md,
    )
    return SectorCarveOut(sector, sleeve_inputs, share, values.get(sector, 0.0), values)


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
