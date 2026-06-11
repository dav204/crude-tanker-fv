"""Daily price refresh: quote extraction, sanity bands, loader override.

No network — Yahoo payloads are canned; loader behavior runs against tmp
fixture dirs. The contract under test (price_refresh.py docstring): live
prices reach current_price ONLY when fresh + unflagged + explicitly
requested; as_of_price always preserves the watchlist-vintage static.
"""

from datetime import datetime, timedelta, timezone

import yaml

from crude_tanker_fv.loaders import load_watchlist
from crude_tanker_fv.price_refresh import (
    PRICE_FRESH_DAYS,
    extract_quote,
    is_fresh,
    sanity_flag,
)


def _chart_payload(price, prev_close, epoch):
    return {"chart": {"result": [{"meta": {
        "regularMarketPrice": price,
        "regularMarketTime": epoch,
        "chartPreviousClose": prev_close,
        "exchangeName": "NYQ",
    }}]}}


def test_extract_quote():
    q = extract_quote(_chart_payload(37.14, 36.92, 1781121602))
    assert q["price"] == 37.14
    assert q["prev_close"] == 36.92
    assert q["day_change_pct"] == 0.6
    assert q["asof"].startswith("2026-06-10")


def test_sanity_flag_day_move():
    q = extract_quote(_chart_payload(20.0, 25.0, 1781121602))  # -20% day
    assert "day move" in sanity_flag(q, static_price=20.5)


def test_sanity_flag_vs_static():
    q = extract_quote(_chart_payload(20.0, 19.8, 1781121602))
    assert sanity_flag(q, static_price=19.0) is None
    assert "vs watchlist static" in sanity_flag(q, static_price=31.0)


def test_ten_incident_clears_bands():
    """The motivating case: TEN live $37.14 vs erroneous static $44 (-16%)
    must NOT be flagged — correcting a wrong static is the whole point."""
    q = extract_quote(_chart_payload(37.14, 36.92, 1781121602))
    assert sanity_flag(q, static_price=44.0) is None


def test_is_fresh_window():
    now = datetime(2026, 6, 11, tzinfo=timezone.utc)
    fresh = (now - timedelta(days=PRICE_FRESH_DAYS - 1)).isoformat()
    stale = (now - timedelta(days=PRICE_FRESH_DAYS + 1)).isoformat()
    assert is_fresh(fresh, now=now)
    assert not is_fresh(stale, now=now)


def _write_fixture(tmp_path, quote):
    (tmp_path / "market_data").mkdir()
    (tmp_path / "watchlist.yaml").write_text(yaml.safe_dump({
        "DHT": {"current_price": 16.40, "analyst_target": 18.0,
                "consensus_pnav": 1.1, "sector": "crude", "as_of": "2026-06-04"},
    }))
    (tmp_path / "market_data" / "prices_daily.yaml").write_text(yaml.safe_dump({
        "fetched_at": "2026-06-10T22:30:00+00:00",
        "source": "yahoo-chart-v8",
        "prices": {"DHT": quote},
    }))


def _now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def test_loader_default_ignores_daily_prices(tmp_path):
    _write_fixture(tmp_path, {"price": 17.25, "asof": _now_iso()})
    wl = load_watchlist(tmp_path)
    assert wl["DHT"]["current_price"] == 16.40
    assert wl["DHT"]["as_of_price"] == 16.40


def test_loader_live_prices_override(tmp_path):
    _write_fixture(tmp_path, {"price": 17.25, "asof": _now_iso()})
    wl = load_watchlist(tmp_path, live_prices=True)
    assert wl["DHT"]["current_price"] == 17.25
    assert wl["DHT"]["as_of_price"] == 16.40  # vintage price survives
    assert wl["DHT"]["price_as_of"]


def test_loader_skips_flagged_quote(tmp_path):
    _write_fixture(tmp_path, {"price": 17.25, "asof": _now_iso(),
                              "flag": "day move +19.0% exceeds ±15% band"})
    wl = load_watchlist(tmp_path, live_prices=True)
    assert wl["DHT"]["current_price"] == 16.40


def test_loader_skips_stale_quote(tmp_path):
    old = (datetime.now(timezone.utc) - timedelta(days=PRICE_FRESH_DAYS + 2))
    _write_fixture(tmp_path, {"price": 17.25,
                              "asof": old.isoformat(timespec="seconds")})
    wl = load_watchlist(tmp_path, live_prices=True)
    assert wl["DHT"]["current_price"] == 16.40


def test_loader_no_daily_file(tmp_path):
    (tmp_path / "watchlist.yaml").write_text(yaml.safe_dump({
        "DHT": {"current_price": 16.40, "analyst_target": 18.0},
    }))
    wl = load_watchlist(tmp_path, live_prices=True)
    assert wl["DHT"]["current_price"] == 16.40
