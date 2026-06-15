"""Point-in-time data assembly for the crude backtest.

Two sources, both real:
  - signal: published Pareto P/NAV from inputs/market_data/pareto_share_prices.csv
  - returns: Yahoo adjusted close from backtest/data/yahoo_<TICKER>.csv
             (adjclose embeds dividends+splits, so adjclose ratios = total return)

Correctness property (asserted, not assumed): no input dated after the as-of
quarter-end may enter that quarter's signal. `signal_at` filters to
report_date <= asof and then asserts the chosen row obeys it; `_LookaheadError`
aborts the run otherwise.
"""

from __future__ import annotations

import csv
import datetime as dt
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PNAV_CSV = REPO / "inputs" / "market_data" / "pareto_share_prices.csv"
PRICE_DIR = Path(__file__).resolve().parent / "data"

CRUDE_NAMES = ["DHT", "FRO", "ECO", "TNK"]   # names with real published P/NAV
NAT_APPROX = "NAT"                            # no published P/NAV (exploratory only)
STALENESS_DAYS = 45                           # a signal must be this fresh at asof


class LookaheadError(AssertionError):
    """Raised if any input dated after the as-of quarter-end feeds that quarter."""


def _d(s: str) -> dt.date:
    return dt.date.fromisoformat(s)


def load_pnav() -> dict[str, list[tuple[dt.date, float]]]:
    """ticker -> sorted [(report_date, pnav)] for rows with a published P/NAV."""
    out: dict[str, list[tuple[dt.date, float]]] = {}
    with open(PNAV_CSV) as fh:
        for row in csv.DictReader(fh):
            pnav = row.get("pnav")
            if not pnav:
                continue
            try:
                out.setdefault(row["ticker"], []).append((_d(row["report_date"]), float(pnav)))
            except ValueError:
                continue
    for t in out:
        out[t].sort()
    return out


def load_prices() -> dict[str, list[tuple[dt.date, float]]]:
    """ticker -> sorted [(date, adjclose)] from the cached Yahoo pulls."""
    out: dict[str, list[tuple[dt.date, float]]] = {}
    for path in PRICE_DIR.glob("yahoo_*.csv"):
        ticker = path.stem.split("_", 1)[1]
        series: list[tuple[dt.date, float]] = []
        with open(path) as fh:
            for row in csv.DictReader(fh):
                a = row.get("adjclose")
                if a in (None, "", "None"):
                    continue
                series.append((_d(row["date"]), float(a)))
        series.sort()
        out[ticker] = series
    return out


def quarter_ends(first: dt.date, last: dt.date) -> list[dt.date]:
    ends = []
    for y in range(first.year, last.year + 1):
        for m, d in ((3, 31), (6, 30), (9, 30), (12, 31)):
            qe = dt.date(y, m, d)
            if first <= qe <= last:
                ends.append(qe)
    return ends


def signal_at(series: list[tuple[dt.date, float]], asof: dt.date,
              staleness_days: int = STALENESS_DAYS) -> float | None:
    """Most recent published P/NAV at or before `asof`, if fresh enough.

    Hard no-look-ahead guard: the chosen row's date must be <= asof.
    """
    prior = [(d, v) for d, v in series if d <= asof]
    if not prior:
        return None
    d, v = prior[-1]
    if d > asof:                                  # unreachable by filter; the guard
        raise LookaheadError(f"signal {d} > asof {asof}")
    if (asof - d).days > staleness_days:          # feed went quiet -> not contemporaneous
        return None
    return v


def price_at(series: list[tuple[dt.date, float]], asof: dt.date) -> float | None:
    """Last adjusted close at or before `asof` (no look-ahead by construction)."""
    prior = [(d, p) for d, p in series if d <= asof]
    if not prior:
        return None
    d, p = prior[-1]
    if d > asof:
        raise LookaheadError(f"price {d} > asof {asof}")
    return p


def load_bvps() -> dict[str, list[tuple[dt.date, dt.date, float]]]:
    """ticker -> sorted [(filed_date, period_end, bvps)] from the SEC cache."""
    out: dict[str, list[tuple[dt.date, dt.date, float]]] = {}
    for path in PRICE_DIR.glob("sec_bv_*.csv"):
        ticker = path.stem.split("sec_bv_", 1)[1]
        series = []
        with open(path) as fh:
            for row in csv.DictReader(fh):
                series.append((_d(row["filed"]), _d(row["period_end"]), float(row["bvps"])))
        series.sort()                       # by filed date
        out[ticker] = series
    return out


def bvps_at(series: list[tuple[dt.date, dt.date, float]], asof: dt.date,
            max_period_staleness_days: int = 250) -> float | None:
    """Latest book value PUBLIC at asof (filed <= asof — no look-ahead on the
    date the number became known), if its fiscal period is not too stale."""
    avail = [(f, pe, v) for f, pe, v in series if f <= asof]
    if not avail:
        return None
    f, pe, v = avail[-1]
    if f > asof:
        raise LookaheadError(f"bvps filed {f} > asof {asof}")
    if (asof - pe).days > max_period_staleness_days:
        return None
    return v


@dataclass
class QuarterCross:
    asof: dt.date
    nxt: dt.date
    pnav: dict[str, float]          # name -> published P/NAV at asof
    fwd_ret: dict[str, float]       # name -> total return asof -> nxt
    rel_ret: dict[str, float]       # fwd_ret minus equal-weight-crude mean
    ew_crude: float                 # equal-weight crude forward return (benchmark)


def build_panel(names: list[str],
                pnav: dict[str, list[tuple[dt.date, float]]],
                prices: dict[str, list[tuple[dt.date, float]]],
                qends: list[dt.date],
                staleness_days: int = STALENESS_DAYS) -> list[QuarterCross]:
    """One cross-section per quarter t (signal at t, total return t -> t+1)."""
    crosses: list[QuarterCross] = []
    for i in range(len(qends) - 1):
        t, t1 = qends[i], qends[i + 1]
        sig: dict[str, float] = {}
        ret: dict[str, float] = {}
        for nm in names:
            s = signal_at(pnav.get(nm, []), t, staleness_days)
            p0 = price_at(prices.get(nm, []), t)
            p1 = price_at(prices.get(nm, []), t1)
            if s is None or p0 is None or p1 is None or p0 <= 0:
                continue
            sig[nm] = s
            ret[nm] = p1 / p0 - 1.0
        common = sorted(set(sig) & set(ret))
        if not common:
            continue
        ew = sum(ret[n] for n in common) / len(common)
        rel = {n: ret[n] - ew for n in common}
        crosses.append(QuarterCross(asof=t, nxt=t1,
                                    pnav={n: sig[n] for n in common},
                                    fwd_ret={n: ret[n] for n in common},
                                    rel_ret=rel, ew_crude=ew))
    return crosses
