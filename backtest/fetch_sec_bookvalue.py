"""Fetch historical book value per share from SEC EDGAR XBRL (Amendment 2).

us-gaap:StockholdersEquity (instant, USD) and dei:EntityCommonStockSharesOutstanding
(fallback us-gaap:CommonStockSharesOutstanding). Each fact carries a `filed`
date — we keep it so the backtest can enforce no-look-ahead on the date the
number became public, not the fiscal period-end.

Only the 9 panel names with deep us-gaap XBRL (probed 2026-06-14). Cache to
backtest/data/sec_bv_<TICKER>.csv. Committed for reproducibility.

    PYTHONPATH=. .venv/bin/python -m backtest.fetch_sec_bookvalue
"""

from __future__ import annotations

import csv
import json
import time
import urllib.request
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
UA = {"User-Agent": "crude-tanker-fv-backtest research dav204@gmail.com"}

CIK = {  # only names with deep us-gaap StockholdersEquity XBRL
    "TNK": 1419945, "INSW": 1679049, "SBLK": 1386716, "GNK": 1326200,
    "HSHP": 1959455, "GLNG": 1207179, "FLNG": 1772253, "LPG": 1596993,
    "NVGS": 1581804,
}


def _concept(cik: int, taxonomy: str, tag: str, unit: str) -> list[dict]:
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/{taxonomy}/{tag}.json"
    try:
        d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read())
    except Exception:
        return []
    return d.get("units", {}).get(unit, [])


def _first_by_end(facts: list[dict]) -> dict[str, dict]:
    """One fact per period-end, keeping the EARLIEST-filed (as-first-reported)
    value. Using the latest-filed value would import restatements that were not
    public at the time AND would stamp old periods with recent filed dates,
    breaking the filed<=asof availability guard. Original filing = point-in-time
    truth for a backtest."""
    best: dict[str, dict] = {}
    for f in facts:
        end = f.get("end")
        if not end or "val" not in f or "filed" not in f:
            continue
        if end not in best or f["filed"] < best[end]["filed"]:
            best[end] = f
    return best


def build(ticker: str, cik: int) -> int:
    equity = _first_by_end(_concept(cik, "us-gaap", "StockholdersEquity", "USD"))
    shares = _first_by_end(_concept(cik, "dei", "EntityCommonStockSharesOutstanding", "shares"))
    if not shares:
        shares = _first_by_end(_concept(cik, "us-gaap", "CommonStockSharesOutstanding", "shares"))
    sh_sorted = sorted(shares.values(), key=lambda f: f["end"])

    rows = []
    for end in sorted(equity):
        eq = equity[end]
        # nearest shares fact with end <= equity end (cover-page count for that filing)
        cand = [s for s in sh_sorted if s["end"] <= end]
        s = cand[-1] if cand else (sh_sorted[0] if sh_sorted else None)
        if not s or not s["val"]:
            continue
        bvps = eq["val"] / s["val"]
        filed = max(eq["filed"], s["filed"])      # public only once both are filed
        rows.append({"period_end": end, "filed": filed,
                     "equity": eq["val"], "shares": s["val"], "bvps": round(bvps, 4)})
    rows.sort(key=lambda r: r["period_end"])
    with open(DATA_DIR / f"sec_bv_{ticker}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["period_end", "filed", "equity", "shares", "bvps"])
        w.writeheader()
        w.writerows(rows)
    span = f"{rows[0]['period_end']}..{rows[-1]['period_end']}" if rows else "EMPTY"
    print(f"{ticker}: {len(rows)} quarter-ends [{span}] last bvps={rows[-1]['bvps'] if rows else 'n/a'}")
    return len(rows)


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for t, c in CIK.items():
        build(t, c)
        time.sleep(0.2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
