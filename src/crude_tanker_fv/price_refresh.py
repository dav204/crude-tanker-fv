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
applied by the loader — day-over-day move >15% (vs the TRUE prior-day
close from the daily bars; meta.chartPreviousClose on a range=5d request
is the close before the 5-day WINDOW, which held five names on statics
for days after the 2026-06-30 sector repricing — audit F-1), or
divergence from the watchlist static >30% (a wrong static is what the
refresh exists to correct, so the band is deliberately wide: TEN's -16%
clears it).

Circuit breaker: the day-move band exists for single-name data glitches.
When >= MARKET_EVENT_MIN_NAMES names trip it in the SAME run, that is a
sector-wide repricing, not a glitch — exactly when fresh prices carry
the most information. Those quotes are applied with a ``market_event``
marker (the loader passes them through; the scorecard discloses the rows
for review) instead of silently falling back to stale statics.

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
MARKET_EVENT_MIN_NAMES = 3  # >= this many day-move trips in one run = repricing, not glitches
PRICE_FRESH_DAYS = 5  # covers weekends + a holiday; beyond this the loader falls back


def _fetch_chart(symbol: str) -> dict:
    req = urllib.request.Request(CHART_URL.format(symbol=symbol),
                                 headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def extract_quote(payload: dict) -> dict:
    """Pull {price, prev_close, asof} out of a Yahoo v8 chart payload.

    prev_close is the TRUE prior-day close read from the daily bars.
    meta.chartPreviousClose is the close before the requested range (~5
    sessions back on range=5d), which turns the "day move" band into a
    5-session trailing move — kept only as a fallback when the bar series
    is unavailable.
    """
    result = payload["chart"]["result"][0]
    meta = result["meta"]
    price = float(meta["regularMarketPrice"])
    asof = datetime.fromtimestamp(int(meta["regularMarketTime"]), tz=timezone.utc)
    quote = {
        "price": price,
        "asof": asof.isoformat(timespec="seconds"),
        "exchange": meta.get("exchangeName"),
    }
    closes = (result.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
    bars = [(t, c) for t, c in zip(result.get("timestamp") or [], closes) if c is not None]
    prev = None
    if len(bars) >= 2:
        # If the last bar IS the current session, the prior close is one bar
        # back; if the session hasn't printed a bar yet, it is the last bar.
        last_bar_day = datetime.fromtimestamp(int(bars[-1][0]), tz=timezone.utc).date()
        prev = bars[-2][1] if last_bar_day == asof.date() else bars[-1][1]
    if prev is None:
        prev = meta.get("chartPreviousClose") or meta.get("previousClose")
    if prev:
        quote["prev_close"] = round(float(prev), 4)
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

    fx_cache: dict[str, float] = {}

    def _usd_fx(currency: str) -> float:
        """USD per 1 unit of `currency` is 1/rate for Yahoo's CUR=X (USD->CUR)."""
        if currency not in fx_cache:
            fx_cache[currency] = float(
                _fetch_chart(f"{currency}=X")["chart"]["result"][0]["meta"]
                ["regularMarketPrice"])
        return fx_cache[currency]

    for ticker, entry in watchlist.items():
        if not isinstance(entry, dict):
            continue
        symbol = entry.get("yahoo_symbol") or ticker
        try:
            quote = extract_quote(_fetch_chart(symbol))
            currency = entry.get("quote_currency")
            if currency and currency != "USD":
                fx = _usd_fx(currency)
                quote["native_price"] = quote["price"]
                quote["native_currency"] = currency
                quote["usd_per_unit_fx"] = round(1.0 / fx, 6)
                quote["price"] = round(quote["price"] / fx, 2)
                if "prev_close" in quote:
                    quote["prev_close"] = round(quote["prev_close"] / fx, 2)
        except Exception as exc:
            failed += 1
            print(f"{ticker:6s} FETCH FAILED ({exc}); keeping previous entry", file=sys.stderr)
            if ticker in previous:
                # Mark the carry (WO2 1.2, D-3): a re-served old quote must be
                # distinguishable from a fresh one — the sentinel's stuck-quote
                # check reads this + the asof lag. Cleared on the next success
                # (the whole entry is replaced).
                prices[ticker] = dict(previous[ticker], carried_over=True)
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

    # Circuit breaker (audit 2026-07-02, F-1): many names tripping the day-move
    # band in ONE run is a sector repricing, not a batch of glitches — apply the
    # prices and mark the rows for review instead of rejecting them (only THIS
    # run's day-move flags count; entries carried over from a failed fetch keep
    # their original flag).
    tripped = sorted(t for t, q in prices.items()
                     if (q.get("flag") or "").startswith("day move")
                     and q is not previous.get(t))
    if len(tripped) >= MARKET_EVENT_MIN_NAMES:
        for t in tripped:
            prices[t]["market_event"] = prices[t].pop("flag")
        flagged -= len(tripped)
        print(f"MARKET EVENT: {len(tripped)} names beyond the ±{DAY_MOVE_FLAG_PCT:.0f}% day "
              f"band together ({', '.join(tripped)}) — prices APPLIED, rows marked for review")

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
