"""Blended fair value (METHODOLOGY.md sections 2.1-2.2).

    Fair Value per share = w_nav * NAV/share + w_earn * DivStrip_implied_price

Combines the NAV lens (``nav``) and the dividend-strip lens
(``dividend_strip``) using the cycle-position weights (``cycle``).
"""

from __future__ import annotations

from dataclasses import dataclass

from .cycle import CycleResult
from .dividend_strip import DividendStripResult
from .nav import NavResult


@dataclass
class BlendedFairValue:
    """Blended fair value for the per-company report (section 7)."""

    nav_per_share: float                    # raw asset NAV/share
    divstrip_implied_price: float
    w_nav: float
    w_earn: float
    fair_value_per_share: float             # post-governance-haircut blend
    governance_discount_pct: float = 0.0    # METHODOLOGY §15
    nav_per_share_effective: float = 0.0    # NAV/share AFTER haircut
    fair_value_per_share_pre_discount: float = 0.0  # blend without haircut (for transparency)


def blend_fair_value(
    nav: NavResult, strip: DividendStripResult, cycle: CycleResult
) -> BlendedFairValue:
    """Weighted combination of NAV/share and dividend-strip implied price.

    A governance / value-trap haircut (METHODOLOGY §15) is applied to the NAV
    term when ``nav.governance_discount_pct`` > 0. The strip's interim DPS are
    realised cash to common shareholders and are NOT haircut; the strip's
    terminal value IS haircut (it represents a future NAV realisation) — that
    haircut is applied inside ``compute_dividend_strip``, so ``strip.implied_price``
    here already reflects it when relevant.
    """
    gov = nav.governance_discount_pct
    nav_effective = nav.nav_per_share * (1.0 - gov)
    fair_value = cycle.w_nav * nav_effective + cycle.w_earn * strip.implied_price
    fair_value_pre = cycle.w_nav * nav.nav_per_share + cycle.w_earn * strip.implied_price
    return BlendedFairValue(
        nav_per_share=nav.nav_per_share,
        divstrip_implied_price=strip.implied_price,
        w_nav=cycle.w_nav,
        w_earn=cycle.w_earn,
        fair_value_per_share=fair_value,
        governance_discount_pct=gov,
        nav_per_share_effective=nav_effective,
        fair_value_per_share_pre_discount=fair_value_pre,
    )
