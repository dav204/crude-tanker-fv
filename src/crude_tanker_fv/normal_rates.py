"""Through-cycle normal-rate layer (P1 — METHODOLOGY §18).

Pre-registered in ``PRE_REGISTRATION_NORMAL_RATES.md`` (frozen 2026-06-29, AHEAD
of results). Produces, per vessel class, two tagged normal-rate bases and their
divergence:

- ``parity`` — replacement economics: the TCE/day that lets a *newbuild* earn its
  cost of capital (the rate that makes justified-P/NAV = 1.0 for a newbuild, so it
  closes the §17 loop). The headline basis for the justified leg's RONAV.
- ``historical_mean`` — realized through-cycle mean (a mean-reversion target). v1
  = the current ``historical_tce_means`` values; the true Baltic $/day route is
  deferred (PRE_REGISTRATION §5a / §7).

The per-class divergence ``historical_mean − parity`` is the under-/over-ordered
signal (negative ⇒ realized below replacement ⇒ under-ordered). This module is the
single computation layer; each consumer picks the basis right for its job. It does
NOT touch ``cycle.py`` (frozen, owner decision D1) — no headline FV moves.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from statistics import median
from typing import Optional

from .loaders import INPUTS_DIR, load_company_inputs, load_market_data, load_watchlist

# ---------------------------------------------------------------------------
# Registered parity inputs (PRE_REGISTRATION_NORMAL_RATES.md §3) — FROZEN.
# ---------------------------------------------------------------------------
WACC_DEFAULT = 0.08
WACC_GRID = (0.07, 0.08, 0.09, 0.10)
ECONOMIC_LIFE_YEARS = 25
OPERATING_DAYS = 360.0           # ~98.6% utilization; reconciled to the strip's
                                 # 2% off-hire as an intentional newbuild-vs-aging
                                 # difference (PRE_REGISTRATION §3c).
OPEX_OUTLIER_FRAC = 0.25         # drop a name's class-opex >25% from the cross-name median


def crf(wacc: float, n: int = ECONOMIC_LIFE_YEARS) -> float:
    """Capital recovery factor: WACC / (1 − (1+WACC)^−N)."""
    return wacc / (1.0 - (1.0 + wacc) ** (-n))


def parity_tce(
    newbuild: float,
    scrap: float,
    opex_per_day: float,
    wacc: float = WACC_DEFAULT,
    n: int = ECONOMIC_LIFE_YEARS,
    operating_days: float = OPERATING_DAYS,
) -> float:
    """Required TCE/day for a newbuild to earn its cost of capital.

    Scrap enters at PRESENT VALUE — ``scrap·(1+wacc)^−n`` — NOT ``(NB − scrap)·CRF``.
    The salvage is a year-N cash inflow; discounting it to year 0 is the NPV=0 form.
    The naive undiscounted credit double-counts the time value, under-charges
    capital, and lands Kamsarmax at $13.1k (outside its registered band); the
    discounted form gives $14.8k (in band). Do NOT "simplify" the discount away
    (PRE_REGISTRATION_NORMAL_RATES.md §2).
    """
    capital_charge = (newbuild - scrap * (1.0 + wacc) ** (-n)) * crf(wacc, n)
    return opex_per_day + capital_charge / operating_days


def class_normalized_opex(
    quarter: str, inputs_dir: Path = INPUTS_DIR
) -> dict[str, float]:
    """Fleet-weighted normalized cash vessel opex per class (PRE_REGISTRATION §3b).

    The repo's ``opex_per_day`` IS the cash-vessel-opex definition (management fees
    live in ``annual_G_and_A``, capitalized special-survey/dry-dock is not in the
    per-day figure) — so the definitional normalization is the convention itself.
    Fleet-weight across every watchlist name carrying the class, then drop any
    name's class-opex >25% from the cross-name median (definitional normalization
    first means the outlier rule fires on errors, not bundling differences).
    """
    by_class: dict[str, list[tuple[float, float, str]]] = {}
    for ticker in load_watchlist(inputs_dir):
        try:
            ci = load_company_inputs(ticker, quarter, inputs_dir)
        except FileNotFoundError:
            continue
        opex = ci.cost_structure.opex_per_day
        counts: dict[str, float] = {}
        for v in ci.fleet.vessels:
            counts[v.cls] = counts.get(v.cls, 0.0) + v.count
        for cls, n in counts.items():
            if cls in opex and opex[cls] > 0:
                by_class.setdefault(cls, []).append((opex[cls], n, ticker))

    out: dict[str, float] = {}
    for cls, entries in by_class.items():
        med = median([o for o, _, _ in entries])
        kept = [(o, w) for o, w, _ in entries if abs(o - med) <= OPEX_OUTLIER_FRAC * med]
        kept = kept or [(o, w) for o, w, _ in entries]   # never empty
        wsum = sum(w for _, w in kept)
        out[cls] = sum(o * w for o, w in kept) / wsum
    return out


@dataclass
class NormalRate:
    """Per-class normal rate under both bases + their divergence."""

    cls: str
    parity: Optional[float]
    historical_mean: Optional[float]

    @property
    def divergence(self) -> Optional[float]:
        """historical_mean − parity. < 0 ⇒ realized below replacement ⇒ under-ordered."""
        if self.parity is None or self.historical_mean is None:
            return None
        return self.historical_mean - self.parity

    @property
    def divergence_pct(self) -> Optional[float]:
        if self.divergence is None or not self.parity:
            return None
        return self.divergence / self.parity


def normal_rate(
    cls: str, basis: str, quarter: str, wacc: float = WACC_DEFAULT,
    inputs_dir: Path = INPUTS_DIR,
) -> Optional[float]:
    """One class's normal rate under ``basis`` in {"parity", "historical_mean"}."""
    t = normal_rate_table(quarter, [cls], wacc, inputs_dir)[cls]
    return t.parity if basis == "parity" else t.historical_mean


def normal_rate_table(
    quarter: str, classes, wacc: float = WACC_DEFAULT, inputs_dir: Path = INPUTS_DIR
) -> dict[str, NormalRate]:
    """Both bases (+ divergence) for each class. Parity is None when the class has
    no value curve or no opex; historical_mean is None when it has no anchor."""
    md = load_market_data(inputs_dir)
    curves = md.vessel_value_curves
    hist = md.historical_tce_means
    opex = class_normalized_opex(quarter, inputs_dir)
    out: dict[str, NormalRate] = {}
    for cls in classes:
        c = curves.get(cls)
        par = (
            parity_tce(c.newbuild, c.scrap_25yr, opex[cls], wacc)
            if c is not None and cls in opex
            else None
        )
        out[cls] = NormalRate(cls, par, hist.get(cls))
    return out
