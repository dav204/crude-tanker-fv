"""Point-in-time signal/price panels for the crude edge backtest.

Source of record: ``inputs/market_data/pareto_share_prices.csv`` — the only
on-disk historical (date, ticker, price, P/NAV) series. It spans
2024-08-22 → 2026-06-08 (weekly Pareto Shipping Daily prints), NOT the
2018–2025 window the test was scoped against. See README for the data gap.

Correctness property (assertion-enforced):
    No observation dated after the as-of cutoff may enter the panel built
    for that cutoff. ``as_of_panel`` raises ``LookAheadError`` on violation.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
PARETO_SHARE_PRICES = REPO_ROOT / "inputs" / "market_data" / "pareto_share_prices.csv"

# The owner's long-listed crude names for Test 0. Maps watchlist symbol ->
# the ticker string used in pareto_share_prices.csv. FRO (Frontline) is NOT
# present in the extract; NAT is present but Pareto publishes no P/NAV for it
# (APPROX in the watchlist) — both surface as data gaps at load time.
CRUDE_PRIMARY = {
    "DHT": "DHT",
    "NAT": "NAT",
    "FRO": "FRO",
    "ECO": "ECO",
    "TNK": "TNK",
}

# Deferred by the owner (too short/complex) — used ONLY for exploratory
# cross-section thickening, never in the primary metric.
CRUDE_EXPLORATORY = {"INSW": "INSW"}


class LookAheadError(AssertionError):
    """Raised when an observation dated after the cutoff enters a panel."""


@dataclass(frozen=True)
class Observation:
    ticker: str
    obs_date: date
    price: Optional[float]
    pnav: Optional[float]


def _parse_float(s: str) -> Optional[float]:
    s = (s or "").strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def load_observations(path: Path = PARETO_SHARE_PRICES) -> list[Observation]:
    """Read all (ticker, date, price, pnav) rows from the Pareto extract."""
    obs: list[Observation] = []
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            d = datetime.strptime(row["report_date"], "%Y-%m-%d").date()
            obs.append(
                Observation(
                    ticker=row["ticker"].strip(),
                    obs_date=d,
                    price=_parse_float(row["price"]),
                    pnav=_parse_float(row["pnav"]),
                )
            )
    return obs


def _series(obs: list[Observation], ticker: str) -> list[Observation]:
    return sorted((o for o in obs if o.ticker == ticker), key=lambda o: o.obs_date)


def obs_on_or_before(
    obs: list[Observation], ticker: str, cutoff: date, max_gap_days: int = 30
) -> Optional[Observation]:
    """Latest observation for ``ticker`` with obs_date <= cutoff.

    Enforces the no-look-ahead property locally. ``max_gap_days`` rejects a
    stale match (no observation within the window before the cutoff).
    """
    best: Optional[Observation] = None
    for o in _series(obs, ticker):
        if o.obs_date <= cutoff:
            best = o
        else:
            break
    if best is None:
        return None
    if best.obs_date > cutoff:  # pragma: no cover - guarded by loop above
        raise LookAheadError(
            f"{ticker} obs {best.obs_date} is after cutoff {cutoff}"
        )
    if (cutoff - best.obs_date).days > max_gap_days:
        return None
    return best


def obs_nearest(
    obs: list[Observation], ticker: str, target: date, max_gap_days: int = 21
) -> Optional[Observation]:
    """Observation for ``ticker`` closest to ``target`` within the window.

    Used for the *realized forward price* (an outcome, not a model input), so
    it is allowed to fall after ``target``. Not subject to no-look-ahead.
    """
    best: Optional[Observation] = None
    best_gap = None
    for o in _series(obs, ticker):
        gap = abs((o.obs_date - target).days)
        if gap <= max_gap_days and (best_gap is None or gap < best_gap):
            best, best_gap = o, gap
    return best


def as_of_panel(
    obs: list[Observation],
    cutoff: date,
    names: dict[str, str],
    require_pnav: bool = True,
    max_gap_days: int = 30,
) -> dict[str, Observation]:
    """Build the point-in-time panel as of ``cutoff``.

    Returns {watchlist_symbol: Observation} for each name with a usable
    (price [+ pnav]) observation dated on or before the cutoff.

    CORRECTNESS PROPERTY: every returned observation is asserted to be dated
    on or before ``cutoff``. A violation raises ``LookAheadError`` — this is
    the single enforced no-look-ahead guarantee for the backtest.
    """
    panel: dict[str, Observation] = {}
    for symbol, pareto_ticker in names.items():
        o = obs_on_or_before(obs, pareto_ticker, cutoff, max_gap_days=max_gap_days)
        if o is None:
            continue
        if o.price is None:
            continue
        if require_pnav and o.pnav is None:
            continue
        # The enforced no-look-ahead assertion:
        if o.obs_date > cutoff:
            raise LookAheadError(
                f"look-ahead: {symbol} obs {o.obs_date} > cutoff {cutoff}"
            )
        panel[symbol] = o
    return panel


def quarter_end_cutoffs(start: date, end: date) -> list[date]:
    """Calendar quarter-end dates within [start, end] (non-overlapping)."""
    ends = []
    for year in range(start.year, end.year + 1):
        for m, d in ((3, 31), (6, 30), (9, 30), (12, 31)):
            qe = date(year, m, d)
            if start <= qe <= end:
                ends.append(qe)
    return ends


def coverage_report(obs: list[Observation]) -> dict[str, dict]:
    """Per-name coverage summary (span + #pnav) for the primary + exploratory
    crude names — what the data actually supports, stated up front."""
    out: dict[str, dict] = {}
    for symbol, pt in {**CRUDE_PRIMARY, **CRUDE_EXPLORATORY}.items():
        s = _series(obs, pt)
        with_pnav = [o for o in s if o.pnav is not None]
        out[symbol] = {
            "pareto_ticker": pt,
            "rows": len(s),
            "rows_with_pnav": len(with_pnav),
            "first": s[0].obs_date.isoformat() if s else None,
            "last": s[-1].obs_date.isoformat() if s else None,
            "pnav_first": with_pnav[0].obs_date.isoformat() if with_pnav else None,
            "pnav_last": with_pnav[-1].obs_date.isoformat() if with_pnav else None,
        }
    return out
