"""Vessel-mark premium / broker-NAV sensitivity (METHODOLOGY.md sections 3.1, 9).

The tool's vessel value curves are deliberately conservative independent marks.
Brokers (Compass / VesselsValue / Clarksons) mark the modern and product fleet
higher; disposal data (the only ground truth) validates the *old-age* leg of the
tool curve but not the mid-age / product anchors, where second-hand deal flow is
thin and idiosyncratic.

Rather than pick one number, we expose a uniform **vessel-mark premium** ``k`` on
the value curves and report each name at three points: tool marks (k=1.00), the
broker-equivalent (the k that lifts the tool NAV to the broker NAV implied by the
consensus P/NAV), and the midpoint. The tool-vs-broker spread on the headline /
breakeven shows how much of a name's cheapness or richness is a genuine
price-vs-value signal versus a NAV-mark choice.

NOTE: ``k`` scales the WHOLE curve uniformly (a first-cut uncertainty band). It
therefore also lifts the disposal-validated old-age leg, which is a known
overshoot — leg-specific recalibration (mid-age / product only) is the follow-up
(METHODOLOGY 9). For pinning a name to its broker NAV the uniform proxy is fine;
for absolute old-vessel values keep k=1.00.
"""

from __future__ import annotations

from dataclasses import replace

from .nav import compute_nav
from .schemas import CompanyInputs

_SOLVE_ITERATIONS = 80
_K_LO, _K_HI = 0.3, 4.0

# Post-2026-06-09 k_broker semantics (tool marks = transaction-anchored):
# on txn-anchored sectors k_broker is the broker premium over transaction
# levels, and validated pure-plays carry a tight UNIFORM premium (~1.12-1.14
# at the Jun-2026 fit) — mark-validated means INSIDE this band with
# cross-name uniformity, not k ≈ 1.0 (METHODOLOGY 9 items 9-10, Appendix A
# 2026-06-12 B4). Un-anchored sectors (LNG, containerships) keep the
# original k ≈ 1.0 reading.
TXN_PURE_PLAY_K_BAND = (1.05, 1.25)
TXN_PURE_PLAY_K_UNIFORMITY = 0.05


def scale_vessel_marks(inputs: CompanyInputs, k: float) -> CompanyInputs:
    """Return ``inputs`` with every vessel value curve scaled by ``k`` (ratios kept)."""
    if k == 1.0:
        return inputs
    md = inputs.market_data
    curves = {
        cls: replace(
            vc,
            newbuild=vc.newbuild * k,
            five_year_benchmark=vc.five_year_benchmark * k,
            ten_year_benchmark=vc.ten_year_benchmark * k,
            scrap_25yr=vc.scrap_25yr * k,
            scrubber_premium=vc.scrubber_premium * k,
        )
        for cls, vc in md.vessel_value_curves.items()
    }
    return replace(inputs, market_data=replace(md, vessel_value_curves=curves))


def solve_broker_premium(inputs: CompanyInputs, broker_nav_per_share: float) -> float:
    """Solve the uniform mark premium ``k`` so whole-company NAV/share == broker NAV.

    Monotone in k -> bisection. ``inputs`` is the WHOLE-company bundle (the broker
    P/NAV is a whole-company figure, so hybrids pass un-carved inputs here).
    """
    lo, hi = _K_LO, _K_HI
    for _ in range(_SOLVE_ITERATIONS):
        mid = (lo + hi) / 2.0
        if compute_nav(scale_vessel_marks(inputs, mid)).nav_per_share < broker_nav_per_share:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0
