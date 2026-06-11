"""Daily watchlist price refresh — Yahoo chart API -> prices_daily.yaml.

Why a side file: ``inputs/watchlist.yaml`` is pipeline-loaded and
judgment-bearing, and the automation-write rule (news-pull spec,
amendment 1) says automation never writes pipeline-loaded YAMLs. Prices
therefore land in ``inputs/market_data/prices_daily.yaml`` (automation-
writable, like the scan cursor), and ``loaders.load_watchlist(...,
live_prices=True)`` prefers them when fresh and unflagged.

Vintage discipline: ``consensus_pnav`` / ``consensus_fwd_pe`` are
Pareto-published ratios tied to the price Pareto saw on the watchlist
``as_of`` date. Broker-NAV (reconcile reads the raw YAML) and the
consensus-EPS xref keep the watchlist-vintage price (``as_of_price``);
only the EV/position layer reads the live price. Caught live on TEN
2026-06-10: the $44 -> $37.14 price fix would have silently moved the
broker-NAV anchor -16% had consensus_pnav not been rebased with it.

Sanity bands: entries are always written, but flagged ones are NOT
applied by the loader — day-over-day move >15%, or divergence from the
watchlist static >30% (a wrong static is what the refresh exists to
correct, so the band is deliberately wide: TEN's -16% clears it).

Run: ``python -m crude_tanker_fv.price_refresh`` (daily via launchd,
``com.crude-tanker-fv.price-refresh``).
"""

from __future__ import annotations

import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

INPUTS_DIR = Path(__file__).resolve().parents[2] / "inputs"
PRICES_RELPATH = Path("market_data") / "prices_daily.yaml"

CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=5d"
USER_AGENT = "Mozilla/5.0 (crude-tanker-fv price refresh)"

DAY_MOVE_FLAG_PCT = 15.0
VS_STATIC_FLAG_PCT = 30.0
PRICE_FRESH_DAYS = 5  # covers weekends + a holiday; beyond this the loader falls back


def _fetch_chart(symbol: str) -> dict:
    req = urllib.request.Request(CHART_URL.format(symbol=symbol),
                                 headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def extract_quote(payload: dict) -> dict:
    """Pull {price, prev_close, asof} out of a Yahoo v8 chart payload."""
    meta = payload["chart"]["result"][0]["meta"]
    price = float(meta["regularMarketPrice"])
    asof = datetime.fromtimestamp(int(meta["regularMarketTime"]), tz=timezone.utc)
    quote = {
        "price": price,
        "asof": asof.isoformat(timespec="seconds"),
        "exchange": meta.get("exchangeName"),
    }
    prev = meta.get("chartPreviousClose") or meta.get("previousClose")
    if prev:
        quote["prev_close"] = float(prev)
        quote["day_change_pct"] = round((price / float(prev) - 1.0) * 100.0, 2)
    return quote


def sanity_flag(quote: dict, static_price: float | None) -> str | None:
    day_move = quote.get("day_change_pct")
    if day_move is not None and abs(day_move) > DAY_MOVE_FLAG_PCT:
        return f"day move {day_move:+.1f}% exceeds ±{DAY_MOVE_FLAG_PCT:.0f}% band"
    if static_price:
        vs_static = (quote["price"] / static_price - 1.0) * 100.0
        if abs(vs_static) > VS_STATIC_FLAG_PCT:
            return (f"{vs_static:+.1f}% vs watchlist static {static_price} "
                    f"exceeds ±{VS_STATIC_FLAG_PCT:.0f}% band")
    return None


def is_fresh(asof_iso: str, now: datetime | None = None) -> bool:
    now = now or datetime.now(timezone.utc)
    asof = datetime.fromisoformat(asof_iso)
    return (now - asof) <= timedelta(days=PRICE_FRESH_DAYS)


def load_daily_prices(inputs_dir: Path = INPUTS_DIR) -> dict[str, dict]:
    """{ticker: quote} from prices_daily.yaml, or {} if no file yet."""
    path = inputs_dir / PRICES_RELPATH
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data.get("prices") or {}


def run_refresh(inputs_dir: Path = INPUTS_DIR) -> tuple[int, int, int]:
    """Fetch every watchlist ticker; returns (fetched, flagged, failed).

    Tickers that fail to fetch keep their previous entry (if any) so a
    transient outage never erases a still-fresh price.
    """
    watchlist = yaml.safe_load((inputs_dir / "watchlist.yaml").read_text()) or {}
    previous = load_daily_prices(inputs_dir)
    prices: dict[str, dict] = {}
    fetched = flagged = failed = 0

    for ticker, entry in watchlist.items():
        if not isinstance(entry, dict):
            continue
        try:
            quote = extract_quote(_fetch_chart(ticker))
        except Exception as exc:
            failed += 1
            print(f"{ticker:6s} FETCH FAILED ({exc}); keeping previous entry", file=sys.stderr)
            if ticker in previous:
                prices[ticker] = previous[ticker]
            continue
        static = entry.get("current_price")
        flag = sanity_flag(quote, float(static) if static else None)
        if flag:
            quote["flag"] = flag
            flagged += 1
        prices[ticker] = quote
        fetched += 1
        print(f"{ticker:6s} ${quote['price']:>8.2f}  {quote.get('day_change_pct', 0):+.2f}%"
              f"  {quote['asof']}" + (f"  ⚑ {flag}" if flag else ""))

    out = {
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "yahoo-chart-v8",
        "prices": prices,
    }
    path = inputs_dir / PRICES_RELPATH
    path.write_text(yaml.safe_dump(out, sort_keys=True))
    print(f"{fetched} fetched, {flagged} flagged, {failed} failed -> {path}")
    return fetched, flagged, failed


def main() -> int:
    fetched, _flagged, failed = run_refresh()
    return 0 if fetched and failed == 0 else (0 if fetched else 1)


if __name__ == "__main__":
    sys.exit(main())
