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

import yaml

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


def load_contract_prices(
    inputs_dir: Path = INPUTS_DIR,
) -> tuple[dict[str, float], dict[str, float]]:
    """Registered ``newbuild_contract`` + ``prompt_resale`` per class (Amendment 1).

    Distinct from the NAV curve's resale ``newbuild``. Classes absent from
    ``newbuild_contract`` are UNVALIDATED (no broker contract mark) → parity None.
    """
    doc = yaml.safe_load(open(inputs_dir / "market_data" / "newbuild_contract_prices.yaml"))
    contract = {k: float(v) for k, v in (doc.get("newbuild_contract") or {}).items()}
    resale = {k: float(v) for k, v in (doc.get("prompt_resale") or {}).items()}
    return contract, resale


def validate_contract_resale(contract: dict[str, float], resale: dict[str, float]) -> None:
    """Input-basis halt (Amendment 1 §A1.3): a newbuild CONTRACT price cannot meet or
    exceed the prompt-RESALE ceiling (resale strictly above contract is the hot/normal-
    market norm). A violation means a resale/stale value was fed as contract — the exact
    conflation that put the curve's $175M VLCC resale into the parity formula. Slack
    inequality, not a margin (contract may legitimately approach resale in a soft patch)."""
    for cls, c in contract.items():
        r = resale.get(cls)
        if r is not None and c >= r:
            raise ValueError(
                f"input-basis error: {cls} newbuild_contract {c:,.0f} >= prompt_resale "
                f"{r:,.0f} — a contract price at/above resale is prima facie a resale-as-"
                f"contract conflation (PRE_REGISTRATION_NORMAL_RATES.md §A1.3)"
            )


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
    contract, resale = load_contract_prices(inputs_dir)
    validate_contract_resale(contract, resale)   # input-basis halt before any parity
    out: dict[str, NormalRate] = {}
    for cls in classes:
        c = curves.get(cls)
        nb = contract.get(cls)   # newbuild CONTRACT (NOT the curve's resale newbuild)
        # parity is None for classes with no registered contract mark (UNVALIDATED:
        # Post-Panamax / LNGC / MGC / Ctr-* — Amendment 1 §A1.4).
        par = (
            parity_tce(nb, c.scrap_25yr, opex[cls], wacc)
            if nb is not None and c is not None and cls in opex
            else None
        )
        out[cls] = NormalRate(cls, par, hist.get(cls))
    return out


# ===========================================================================
# §18.5a — mean-reversion gate (Thread 3). DATA-GATED.
# Validates the historical_mean anchor. Needs a REAL $/day Baltic TC series
# (inputs/market_data/baltic_tce_series.yaml). REGISTERED-PENDING until provided —
# see backtest/DATA_CONTRACT_NORMAL_RATES.md. The in-repo baltic_indexes_daily.csv
# is INDEX-POINT (§11.7.2), insufficient; NEVER scale it to $/day. No proxy.
# ===========================================================================

# Registered gate parameters (PRE_REGISTRATION_NORMAL_RATES.md §5a).
MR_GATE_HORIZON_Q = 4        # quarters ahead for the "subsequent realized-rate change"
MR_GATE_MIN_OBS = 12         # <12 quarterly observations ⇒ "insufficient", never a pass/reject
MR_GATE_PASS_RATE = 0.70     # sign-consistency threshold; below ⇒ the anchor is REJECTED
MR_WINSOR_LO, MR_WINSOR_HI = 0.05, 0.95


def winsorize(values: list[float], lo: float = MR_WINSOR_LO, hi: float = MR_WINSOR_HI) -> list[float]:
    """Clamp to the [lo, hi] empirical percentiles (5/95 registered)."""
    if not values:
        return []
    s = sorted(values)
    n = len(s)
    lo_v = s[min(n - 1, int(lo * (n - 1)))]
    hi_v = s[min(n - 1, int(hi * (n - 1)))]
    return [min(max(v, lo_v), hi_v) for v in values]


@dataclass
class MeanReversionVerdict:
    """§18.5a verdict for one class's historical_mean anchor."""

    cls: str
    status: str                       # pass | reject | insufficient | pending
    hit_rate: Optional[float] = None
    n_obs: Optional[int] = None
    anchor: Optional[float] = None


def mean_reversion_gate(
    cls: str,
    series: list[float],
    horizon_q: int = MR_GATE_HORIZON_Q,
    min_obs: int = MR_GATE_MIN_OBS,
    pass_rate: float = MR_GATE_PASS_RATE,
) -> MeanReversionVerdict:
    """Registered §5a gate. ``series``: quarterly REAL (inflation-adjusted) $/day TC,
    oldest-first. Anchor = 5/95-winsorized median of the series. For each quarter t
    with t+horizon in range, the ratio ``series[t] / anchor`` predicts the SIGN of the
    forward realized change (ratio > 1 ⇒ rate falls; < 1 ⇒ rises). Pass = sign-consistent
    in ≥ ``pass_rate`` of ≥ ``min_obs`` observations; below ⇒ the anchor is REJECTED."""
    if len(series) <= horizon_q:
        return MeanReversionVerdict(cls, "insufficient", None, 0, None)
    anchor = median(winsorize(series))
    hits = n = 0
    for t in range(len(series) - horizon_q):
        ratio = series[t] / anchor if anchor else 1.0
        realized = series[t + horizon_q] - series[t]
        if ratio == 1.0 or realized == 0:
            continue                      # no directional prediction / no realized change
        predicted_fall = ratio > 1.0
        hits += 1 if (predicted_fall and realized < 0) or (not predicted_fall and realized > 0) else 0
        n += 1
    if n < min_obs:
        return MeanReversionVerdict(cls, "insufficient", (hits / n if n else None), n, anchor)
    hr = hits / n
    return MeanReversionVerdict(cls, "pass" if hr >= pass_rate else "reject", hr, n, anchor)


def load_baltic_tce_series(inputs_dir: Path = INPUTS_DIR) -> dict[str, list[float]]:
    """Real $/day Baltic TC series per class (oldest-first), or {} if the file is
    absent — REGISTERED-PENDING. NEVER synthesised from baltic_indexes_daily.csv."""
    path = inputs_dir / "market_data" / "baltic_tce_series.yaml"
    if not path.exists():
        return {}
    doc = yaml.safe_load(open(path)) or {}
    series = doc.get("series") or {}
    return {k: [float(x) for x in v] for k, v in series.items() if v}


def mean_reversion_gate_table(
    quarter: str, classes, inputs_dir: Path = INPUTS_DIR
) -> dict[str, MeanReversionVerdict]:
    """Run §5a per class IF the Baltic $/day series is present; else every class is
    'pending' (no crash, no proxy). When a class REJECTS, its historical_mean is
    unvalidated and consumers should treat that basis as flagged (drop to None)."""
    series_by_class = load_baltic_tce_series(inputs_dir)
    out: dict[str, MeanReversionVerdict] = {}
    for cls in classes:
        s = series_by_class.get(cls)
        out[cls] = mean_reversion_gate(cls, s) if s else MeanReversionVerdict(cls, "pending")
    return out


# ===========================================================================
# §18.5b — orderbook cross-check (Thread 5). DATA-GATED.
# Breaks the parity circularity: "historical < parity ⇒ under-ordered" is only
# validated when an INDEPENDENT orderbook-to-fleet ratio confirms a thin book.
# Needs inputs/market_data/orderbook_ratios.yaml. REGISTERED-PENDING until provided.
# NEVER estimate orderbook ratios from memory. A contradiction flags the parity INPUT.
# ===========================================================================

OB_BALANCED_BAND = 0.20      # ±20% around the neutral (replacement-rate) OB level ⇒ "balanced"
OB_DIVERGENCE_TOL = 0.05     # |divergence / parity| < 5% ⇒ "balanced" divergence


@dataclass
class OrderbookVerdict:
    """§18.5b verdict: does the divergence sign coincide with the orderbook signal?"""

    cls: str
    status: str                       # coincide | contradict | pending
    divergence_signal: Optional[int] = None    # -1 under-ordered / 0 balanced / +1 over-ordered
    orderbook_signal: Optional[int] = None      # -1 thin / 0 balanced / +1 thick
    note: str = ""


def orderbook_crosscheck(
    cls: str,
    divergence_pct: Optional[float],
    orderbook_ratio: Optional[float],
    neutral_ratio: Optional[float],
    band: float = OB_BALANCED_BAND,
    div_tol: float = OB_DIVERGENCE_TOL,
) -> OrderbookVerdict:
    """Registered §5b. ``divergence_pct`` = (historical_mean − parity)/parity (< 0 ⇒
    under-ordered). ``orderbook_ratio`` = orderbook ÷ fleet; ``neutral_ratio`` = the
    balanced (replacement-rate) OB level. The SIGN of the divergence must coincide with
    the orderbook signal (under-ordered ⇒ thin book; over-ordered ⇒ thick). A
    contradiction flags the parity INPUT, not the output."""
    if divergence_pct is None or orderbook_ratio is None or not neutral_ratio:
        return OrderbookVerdict(cls, "pending")
    div_sig = -1 if divergence_pct < -div_tol else (1 if divergence_pct > div_tol else 0)
    ob_sig = (
        -1 if orderbook_ratio < neutral_ratio * (1 - band)
        else 1 if orderbook_ratio > neutral_ratio * (1 + band)
        else 0
    )
    if div_sig == ob_sig:
        return OrderbookVerdict(cls, "coincide", div_sig, ob_sig)
    return OrderbookVerdict(
        cls, "contradict", div_sig, ob_sig,
        note="divergence sign vs orderbook signal disagree — investigate the parity INPUT (§5b)",
    )


def load_orderbook_ratios(inputs_dir: Path = INPUTS_DIR) -> dict[str, dict]:
    """Independent OB-to-fleet ratio + neutral level per class, or {} if absent —
    REGISTERED-PENDING. Each class: {ratio, neutral, date, source}. NEVER estimated."""
    path = inputs_dir / "market_data" / "orderbook_ratios.yaml"
    if not path.exists():
        return {}
    doc = yaml.safe_load(open(path)) or {}
    return doc.get("orderbook") or {}


def orderbook_crosscheck_table(
    quarter: str, classes, wacc: float = WACC_DEFAULT, inputs_dir: Path = INPUTS_DIR
) -> dict[str, OrderbookVerdict]:
    """Run §5b per class IF the orderbook ratios are present; else 'pending'."""
    ratios = load_orderbook_ratios(inputs_dir)
    table = normal_rate_table(quarter, list(classes), wacc, inputs_dir)
    out: dict[str, OrderbookVerdict] = {}
    for cls in classes:
        ob = ratios.get(cls)
        dp = table[cls].divergence_pct
        out[cls] = (
            orderbook_crosscheck(cls, dp, ob.get("ratio"), ob.get("neutral"))
            if ob and dp is not None else OrderbookVerdict(cls, "pending")
        )
    return out
