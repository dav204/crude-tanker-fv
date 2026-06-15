"""Fetch full-history daily prices (+ dividends, + adjusted close) for the
crude backtest names from Yahoo, and cache to backtest/data/.

Mirrors the request mechanism in src/crude_tanker_fv/price_refresh.py (urllib,
User-Agent) but parameterized for a multi-year range with dividend events and
adjusted close. Adjusted close embeds dividend + split adjustments, so the
ratio of two adjclose points IS the total return between them — that is the
return series the backtest uses.

This is a one-time cache builder. Re-running overwrites the cache. The cached
CSVs are committed so the backtest reproduces without network.

    .venv/bin/python backtest/fetch_prices.py
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import time
import urllib.request
from pathlib import Path

NAMES = ["DHT", "NAT", "FRO", "ECO", "TNK"]
DATA_DIR = Path(__file__).resolve().parent / "data"
USER_AGENT = "Mozilla/5.0"
# 10y daily history with dividend events + adjusted close.
CHART_URL = (
    "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    "?interval=1d&range=10y&events=div&includeAdjustedClose=true"
)


def _fetch(symbol: str) -> dict:
    req = urllib.request.Request(CHART_URL.format(symbol=symbol),
                                 headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def _parse(payload: dict) -> tuple[list[dict], list[dict]]:
    res = payload["chart"]["result"][0]
    ts = res.get("timestamp", []) or []
    quote = res["indicators"]["quote"][0]
    closes = quote.get("close", [])
    adj = (res["indicators"].get("adjclose", [{}])[0] or {}).get("adjclose", [])
    prices = []
    for i, t in enumerate(ts):
        c = closes[i] if i < len(closes) else None
        a = adj[i] if i < len(adj) else None
        if c is None and a is None:
            continue
        d = dt.datetime.utcfromtimestamp(t).date().isoformat()
        prices.append({"date": d, "close": c, "adjclose": a})
    divs = []
    for ev in (res.get("events", {}).get("dividends", {}) or {}).values():
        d = dt.datetime.utcfromtimestamp(ev["date"]).date().isoformat()
        divs.append({"date": d, "amount": ev.get("amount")})
    divs.sort(key=lambda r: r["date"])
    return prices, divs


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for name in NAMES:
        payload = _fetch(name)
        prices, divs = _parse(payload)
        with open(DATA_DIR / f"yahoo_{name}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["date", "close", "adjclose"])
            w.writeheader()
            w.writerows(prices)
        with open(DATA_DIR / f"dividends_{name}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["date", "amount"])
            w.writeheader()
            w.writerows(divs)
        span = f"{prices[0]['date']}..{prices[-1]['date']}" if prices else "EMPTY"
        print(f"{name}: {len(prices)} bars [{span}], {len(divs)} dividends")
        time.sleep(0.4)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
