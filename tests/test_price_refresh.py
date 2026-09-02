"""Daily price refresh: quote extraction, sanity bands, loader override.

No network — Yahoo payloads are canned; loader behavior runs against tmp
fixture dirs. The contract under test (price_refresh.py docstring): live
prices reach current_price ONLY when fresh + unflagged + explicitly
requested; as_of_price always preserves the watchlist-vintage static.
"""

from datetime import datetime, timedelta, timezone

import yaml

from crude_tanker_fv.loaders import load_watchlist, stale_price_fallbacks
from crude_tanker_fv.price_refresh import (
    PRICE_FRESH_DAYS,
    extract_quote,
    is_fresh,
    sanity_flag,
)


def _chart_payload(price, prev_close, epoch, closes=None):
    """Canned Yahoo v8 payload. `closes` (optional) adds a daily-bar series
    ending at `epoch` (one bar per prior day), the way a range=5d response
    carries it; without it extract_quote falls back to chartPreviousClose."""
    result = {"meta": {
        "regularMarketPrice": price,
        "regularMarketTime": epoch,
        "chartPreviousClose": prev_close,
        "exchangeName": "NYQ",
    }}
    if closes is not None:
        result["timestamp"] = [epoch - 86400 * (len(closes) - 1 - i) for i in range(len(closes))]
        result["indicators"] = {"quote": [{"close": closes}]}
    return {"chart": {"result": [result]}}


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


def test_extract_quote_uses_true_prior_day_close():
    """The day-move band must measure vs YESTERDAY's close, not
    meta.chartPreviousClose (= the close before the 5d window). During the
    2026-06-30 repricing the window-edge close overstated the move and held
    five names on June-4 statics for days (audit F-1)."""
    # Steady slide: window-edge close 25.00, yesterday 20.60, today 20.00.
    q = extract_quote(_chart_payload(
        20.0, 25.0, 1781121602, closes=[25.0, 23.5, 22.0, 20.6, 20.0]))
    assert q["prev_close"] == 20.6
    assert q["day_change_pct"] == -2.91          # vs 20.60, NOT -20% vs 25.00
    assert sanity_flag(q, static_price=20.5) is None


def test_extract_quote_prior_session_when_no_bar_today():
    """Fetched before today's session prints a bar: the last bar IS the prior
    close (don't reach one further back)."""
    epoch = 1781121602
    payload = _chart_payload(20.0, 25.0, epoch, closes=[25.0, 23.5, 20.6])
    # Shift all bars back one day: the newest bar is the PRIOR session.
    payload["chart"]["result"][0]["timestamp"] = [epoch - 86400 * i for i in (3, 2, 1)]
    q = extract_quote(payload)
    assert q["prev_close"] == 20.6


def test_extract_quote_falls_back_without_bar_series():
    q = extract_quote(_chart_payload(20.0, 19.8, 1781121602))
    assert q["prev_close"] == 19.8


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
    # The fallback is recorded on the entry so the scorecard can disclose it
    # (stderr-only was audit F-1's silent-static failure).
    assert "day move" in wl["DHT"]["price_fallback"]


def test_loader_applies_market_event_quote(tmp_path):
    """Circuit-breaker pass-through: a market_event quote is APPLIED (fresh
    prices carry the most information during a repricing) and the row carries
    the review marker."""
    _write_fixture(tmp_path, {"price": 13.10, "asof": _now_iso(),
                              "market_event": "day move -20.1% exceeds ±15% band"})
    wl = load_watchlist(tmp_path, live_prices=True)
    assert wl["DHT"]["current_price"] == 13.10
    assert wl["DHT"]["as_of_price"] == 16.40
    assert "day move" in wl["DHT"]["price_review"]


def test_market_event_circuit_breaker(tmp_path, monkeypatch):
    """>=3 names tripping the day band in ONE run = sector repricing: prices
    applied with market_event markers, not rejected. Below the threshold the
    per-name flag behaviour is unchanged (single-name glitch protection)."""
    from crude_tanker_fv import price_refresh

    def _setup(names):
        (tmp_path / "market_data").mkdir(exist_ok=True)
        (tmp_path / "watchlist.yaml").write_text(yaml.safe_dump({
            t: {"current_price": 20.0, "analyst_target": 25.0} for t in names
        }))

    # Every fetch returns a -20% day move (25.0 -> 20.0) with a bar series.
    payload = _chart_payload(20.0, 25.0, 1781121602,
                             closes=[26.0, 25.5, 25.2, 25.0, 20.0])
    monkeypatch.setattr(price_refresh, "_fetch_chart", lambda symbol: payload)

    _setup(["AAA", "BBB", "CCC"])
    fetched, flagged, failed = price_refresh.run_refresh(tmp_path)
    assert (fetched, flagged, failed) == (3, 0, 0)
    prices = yaml.safe_load((tmp_path / "market_data" / "prices_daily.yaml").read_text())["prices"]
    assert all("market_event" in q and "flag" not in q for q in prices.values())

    _setup(["AAA", "BBB"])
    fetched, flagged, failed = price_refresh.run_refresh(tmp_path)
    assert (fetched, flagged, failed) == (2, 2, 0)
    prices = yaml.safe_load((tmp_path / "market_data" / "prices_daily.yaml").read_text())["prices"]
    assert all("flag" in q and "market_event" not in q for q in prices.values())


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


# ----------------------------------------------------------------------------
# Stale-run alert (2026-07-31): a regen on an aged-out prices_daily vintage
# silently repriced the book on Jun-26/Jul-3 statics — phantom BUY flips.
# >= STALE_PRICE_ALERT_MIN_NAMES freshness-gate fallbacks in one load must be
# detectable (loader helper) and carried to the scorecard's price_basis.
# ----------------------------------------------------------------------------
def _write_book_fixture(tmp_path, n_names, asof):
    (tmp_path / "market_data").mkdir()
    (tmp_path / "watchlist.yaml").write_text(yaml.safe_dump({
        f"T{i}": {"current_price": 10.0 + i, "analyst_target": 15.0,
                  "sector": "crude", "as_of": "2026-06-26"}
        for i in range(n_names)
    }))
    (tmp_path / "market_data" / "prices_daily.yaml").write_text(yaml.safe_dump({
        "prices": {f"T{i}": {"price": 12.0 + i, "asof": asof} for i in range(n_names)},
    }))


def _stale_iso():
    return (datetime.now(timezone.utc)
            - timedelta(days=PRICE_FRESH_DAYS + 2)).isoformat(timespec="seconds")


def test_stale_overlay_multi_name_fallback_is_detected(tmp_path):
    _write_book_fixture(tmp_path, 3, _stale_iso())
    wl = load_watchlist(tmp_path, live_prices=True)
    stale = stale_price_fallbacks(wl)
    assert sorted(stale) == ["T0", "T1", "T2"]
    assert all(reason.startswith("stale quote") for reason in stale.values())
    assert wl["T0"]["current_price"] == 10.0   # overlay dropped, static survived


def test_fresh_overlay_has_no_stale_fallbacks(tmp_path):
    _write_book_fixture(tmp_path, 3, _now_iso())
    wl = load_watchlist(tmp_path, live_prices=True)
    assert stale_price_fallbacks(wl) == {}
    assert wl["T0"]["current_price"] == 12.0   # overlay applied


def test_flagged_and_missing_quotes_do_not_count_as_stale(tmp_path):
    _write_fixture(tmp_path, {"price": 17.25, "asof": _now_iso(),
                              "flag": "day move -21.7% exceeds ±15% band"})
    wl = load_watchlist(tmp_path, live_prices=True)
    assert stale_price_fallbacks(wl) == {}

    (tmp_path / "market_data" / "prices_daily.yaml").unlink()
    wl = load_watchlist(tmp_path, live_prices=True)
    assert stale_price_fallbacks(wl) == {}


def test_price_basis_summary_carries_the_stale_set(tmp_path):
    from crude_tanker_fv.scorecard import price_basis_summary

    _write_book_fixture(tmp_path, 3, _stale_iso())
    pb = price_basis_summary(tmp_path)
    assert sorted(pb["stale_fallback"]) == ["T0", "T1", "T2"]
    assert sorted(pb["static_fallback"]) == ["T0", "T1", "T2"]


def test_bare_run_writes_a_manual_ledger_row_and_wrapper_runs_do_not(tmp_path):
    """2026-09-02 (Stage 0): the seven 8/17-24 outage salvages were invisible to
    state/automation_runs.log — a bare run now ledgers itself as manual:*; under
    the wrapper (CRUDE_FV_CRON_WRAPPER) the wrapper's own row is the record."""
    from crude_tanker_fv.price_refresh import ledger_bare_run
    assert ledger_bare_run(0, root=tmp_path, environ={"USER": "dan"})
    row = (tmp_path / "state" / "automation_runs.log").read_text().strip()
    assert "job=price-refresh initiator=manual:dan@" in row and "outcome=ok rc=0 note=bare-run" in row
    assert not ledger_bare_run(1, root=tmp_path, environ={"USER": "dan", "CRUDE_FV_CRON_WRAPPER": "1"})
    assert (tmp_path / "state" / "automation_runs.log").read_text().count("\n") == 1
