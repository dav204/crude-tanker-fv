"""Point-in-time book value + prices from factor-portfolio's Sharadar cache.

Amendment 3 (see PRE_REGISTRATION.md) — the powered P/B proxy on the ACTUAL
watchlist. Sharadar standardizes the FPI 20-F/6-K filings that the SEC us-gaap
XBRL pull (Amendment 2) was blind to, so DHT/FRO/ECO and the full product sector
come into the panel for the first time.

We read factor-portfolio's committed cache CSVs **directly** rather than import
its `SharadarProvider`: the cache is a stable, simple format, and reading it
keeps this backtest runnable in the repo's own 3.9 venv without coupling to
factor-portfolio's 3.10+ package deps. The no-look-ahead discipline
(`filed`-date gating, asserted by the reused `loaders.bvps_at` / `price_at`) is
reproduced faithfully.

  cache layout (branch v2-validation-first):
    data/cache/sharadar/sec_<T>.csv     period_end,filed,field,value,dimension (ARY = annual)
    data/cache/sharadar/prices_<T>.csv  date,close,closeunadj,volume,adjclose  (adjclose = total return)

Provenance is pinned in the report at run time (cache git sha + branch).
"""

from __future__ import annotations

import csv
import datetime as dt
import os
from pathlib import Path

# Curated sector labels, held in code and auditable (mirrors panel.py). Sectors
# match the watchlist primary-sector treatment; GSL is a containerships
# singleton (raw-panel secondary only, never the sector-neutral primary).
SHARADAR_PANEL: dict[str, str] = {
    "DHT": "crude", "FRO": "crude", "ECO": "crude", "INSW": "crude",
    "TNK": "crude", "NAT": "crude", "TEN": "crude",
    "STNG": "product", "HAFN": "product", "TRMD": "product", "ASC": "product",
    "SBLK": "dry_bulk", "GNK": "dry_bulk", "CMDB": "dry_bulk",
    "FLNG": "lng", "CCEC": "lng",
    "GSL": "containerships",
}
SECTOR_OF = dict(SHARADAR_PANEL)

EQUITY_FIELD = "StockholdersEquity"
SHARES_FIELD = "EntityCommonStockSharesOutstanding"
DIMENSION = "ARY"                       # annual; the only dimension with BS fields in this cache
DEFAULT_FP_ROOT = Path.home() / "Projects" / "factor-portfolio"


def cache_dir() -> Path:
    root = Path(os.environ.get("FACTOR_PORTFOLIO_ROOT", DEFAULT_FP_ROOT))
    return root / "data" / "cache" / "sharadar"


def cache_available() -> bool:
    d = cache_dir()
    return d.exists() and (d / "sec_DHT.csv").exists()


def _d(s: str) -> dt.date:
    return dt.date.fromisoformat(s)


def _read_field(path: Path, field: str) -> dict[str, tuple[dt.date, float]]:
    """period_end -> (earliest filed, value at that filing) for one ARY field.

    Earliest filing = first public disclosure of the period (point-in-time
    honest). Restatements (rare for annual equity) are not separately tracked —
    a documented simplification, matching the existing loader's grain.
    """
    out: dict[str, tuple[dt.date, float]] = {}
    with open(path) as fh:
        for row in csv.DictReader(fh):
            if row.get("field") != field or row.get("dimension") != DIMENSION:
                continue
            try:
                filed = _d(row["filed"])
                val = float(row["value"])
            except (ValueError, KeyError):
                continue
            pe = row["period_end"]
            if pe not in out or filed < out[pe][0]:
                out[pe] = (filed, val)
    return out


def load_bvps() -> dict[str, list[tuple[dt.date, dt.date, float]]]:
    """ticker -> sorted [(filed, period_end, bvps)] from Sharadar SF1 ARY.

    BVPS = StockholdersEquity / shares for each fiscal period where both legs
    exist; stamped public at `filed = max(equity_filed, shares_filed)` so a
    signal is never used before both numbers were disclosed.
    """
    d = cache_dir()
    out: dict[str, list[tuple[dt.date, dt.date, float]]] = {}
    for ticker in SHARADAR_PANEL:
        sec = d / f"sec_{ticker}.csv"
        if not sec.exists():
            continue
        equity = _read_field(sec, EQUITY_FIELD)
        shares = _read_field(sec, SHARES_FIELD)
        series: list[tuple[dt.date, dt.date, float]] = []
        for pe in equity.keys() & shares.keys():
            (eq_filed, eq_val), (sh_filed, sh_val) = equity[pe], shares[pe]
            if sh_val <= 0:
                continue
            bvps = eq_val / sh_val
            series.append((max(eq_filed, sh_filed), _d(pe), bvps))
        series.sort()
        if series:
            out[ticker] = series
    return out


def load_prices() -> dict[str, list[tuple[dt.date, float]]]:
    """ticker -> sorted [(date, adjclose)] from Sharadar SEP (total-return series)."""
    d = cache_dir()
    out: dict[str, list[tuple[dt.date, float]]] = {}
    for ticker in SHARADAR_PANEL:
        px = d / f"prices_{ticker}.csv"
        if not px.exists():
            continue
        series: list[tuple[dt.date, float]] = []
        with open(px) as fh:
            for row in csv.DictReader(fh):
                a = row.get("adjclose")
                if a in (None, "", "None"):
                    continue
                try:
                    series.append((_d(row["date"]), float(a)))
                except ValueError:
                    continue
        series.sort()
        if series:
            out[ticker] = series
    return out


def cache_provenance() -> str:
    """Short git sha + branch of the factor-portfolio cache, for the report."""
    import subprocess
    root = Path(os.environ.get("FACTOR_PORTFOLIO_ROOT", DEFAULT_FP_ROOT))
    try:
        sha = subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
        branch = subprocess.run(["git", "-C", str(root), "rev-parse", "--abbrev-ref", "HEAD"],
                                capture_output=True, text=True, check=True).stdout.strip()
        return f"{branch}@{sha}"
    except Exception:
        return "unknown"
