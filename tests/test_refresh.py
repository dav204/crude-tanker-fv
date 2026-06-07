"""Tests for the pre-flight refresh checklist (METHODOLOGY §8).

Coverage targets:
  - Target-quarter inference: correct quarter for various input dates,
    including the year-rollover edge case (Q1 today → previous-year Q4).
  - Balance-sheet check correctly identifies missing files for the target
    quarter even when files exist for other quarters.
  - Market-data staleness uses the threshold strictly (> 30 days is stale,
    exactly 30 days is not).
  - APPROX consensus_pnav detection works on the per-ticker block
    (doesn't get confused by APPROX in a different ticker's block).
  - Render doesn't crash on the all-clean / first-run-ever case.
"""

import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest
import yaml

from crude_tanker_fv.refresh import (
    MARKET_DATA_FILES,
    MARKET_DATA_STALE_DAYS,
    build_checklist,
    check_balance_sheets,
    check_market_data,
    check_watchlist_freshness,
    infer_target_quarter,
    write_checklist,
)


# ----------------------------------------------------------------------------
# Target-quarter inference
# ----------------------------------------------------------------------------
@pytest.mark.parametrize("today,expected", [
    (date(2026, 4, 15), "2026-Q1"),    # mid-April — Q1 just closed
    (date(2026, 6, 1),  "2026-Q1"),    # June — Q2 in progress; refresh Q1
    (date(2026, 8, 1),  "2026-Q2"),    # August — Q2 closed end-June
    (date(2026, 11, 15),"2026-Q3"),    # November — Q3 closed end-Sept
    (date(2026, 1, 15), "2025-Q4"),    # January — year rollover, refresh prev Q4
    (date(2026, 3, 31), "2025-Q4"),    # end of Q1 — Q1 not yet closed
    (date(2026, 4, 1),  "2026-Q1"),    # first day of Q2 — Q1 just closed
])
def test_infer_target_quarter(today, expected):
    assert infer_target_quarter(today=today) == expected


# ----------------------------------------------------------------------------
# Balance-sheet check
# ----------------------------------------------------------------------------
def test_check_balance_sheets_detects_missing(tmp_path):
    """Watchlist has 3 tickers; only 2 BSes exist for Q1, 1 exists for Q2."""
    inputs = tmp_path / "inputs"
    (inputs / "balance_sheets").mkdir(parents=True)
    # DHT has Q1 only; ECO has Q1 + Q2; FRO has Q2 only.
    (inputs / "balance_sheets" / "dht_2026-Q1.yaml").write_text("ticker: DHT")
    (inputs / "balance_sheets" / "eco_2026-Q1.yaml").write_text("ticker: ECO")
    (inputs / "balance_sheets" / "eco_2026-Q2.yaml").write_text("ticker: ECO")
    (inputs / "balance_sheets" / "fro_2026-Q2.yaml").write_text("ticker: FRO")

    watchlist = {"DHT": {}, "ECO": {}, "FRO": {}}

    # Asking for Q1 → DHT and ECO present; FRO missing.
    items_q1 = check_balance_sheets("2026-Q1", watchlist, inputs_dir=inputs)
    by_t = {it.label: it.status for it in items_q1}
    assert by_t == {"DHT": "ok", "ECO": "ok", "FRO": "missing"}

    # Asking for Q2 → ECO and FRO present; DHT missing.
    items_q2 = check_balance_sheets("2026-Q2", watchlist, inputs_dir=inputs)
    by_t2 = {it.label: it.status for it in items_q2}
    assert by_t2 == {"DHT": "missing", "ECO": "ok", "FRO": "ok"}


def test_check_balance_sheets_filename_is_lowercase(tmp_path):
    """The watchlist YAML uses uppercase tickers; the BS filename convention
    is lowercase. The check must lowercase the ticker before looking up."""
    inputs = tmp_path / "inputs"
    (inputs / "balance_sheets").mkdir(parents=True)
    (inputs / "balance_sheets" / "stng_2026-Q1.yaml").write_text("ticker: STNG")

    items = check_balance_sheets("2026-Q1", {"STNG": {}}, inputs_dir=inputs)
    assert items[0].status == "ok"


# ----------------------------------------------------------------------------
# Market-data staleness
# ----------------------------------------------------------------------------
def test_check_market_data_threshold_strict(tmp_path):
    """A file modified exactly 30 days ago is NOT stale (strict > threshold);
    31 days IS stale. Backdate the mtime via os.utime."""
    inputs = tmp_path / "inputs"
    (inputs / "market_data").mkdir(parents=True)
    today = date(2026, 6, 1)
    for fname in MARKET_DATA_FILES:
        p = inputs / "market_data" / fname
        p.write_text("dummy")

    # Backdate vessel_value_curves to 30 days ago (boundary — should be ok).
    boundary_ts = (
        datetime(2026, 5, 2, tzinfo=timezone.utc).timestamp()  # 30 days before 6/1
    )
    os.utime(inputs / "market_data" / "vessel_value_curves.yaml",
             (boundary_ts, boundary_ts))
    # Backdate spot_tce to 31 days ago (should be stale).
    stale_ts = (
        datetime(2026, 5, 1, tzinfo=timezone.utc).timestamp()
    )
    os.utime(inputs / "market_data" / "spot_tce.yaml", (stale_ts, stale_ts))

    items = check_market_data(inputs_dir=inputs, today=today)
    by_f = {it.label: it.status for it in items}
    assert by_f["vessel_value_curves.yaml"] == "ok"   # exactly 30 days = ok
    assert by_f["spot_tce.yaml"] == "stale"           # 31 days = stale


def test_check_market_data_missing_file(tmp_path):
    inputs = tmp_path / "inputs"
    (inputs / "market_data").mkdir(parents=True)
    # Create only some of the expected files.
    (inputs / "market_data" / "vessel_value_curves.yaml").write_text("dummy")

    items = check_market_data(inputs_dir=inputs, today=date(2026, 6, 1))
    by_f = {it.label: it.status for it in items}
    assert by_f["vessel_value_curves.yaml"] == "ok"
    assert by_f["spot_tce.yaml"] == "missing"
    assert by_f["twelve_month_tc.yaml"] == "missing"


# ----------------------------------------------------------------------------
# Watchlist freshness + APPROX detection
# ----------------------------------------------------------------------------
def test_approx_detection_isolates_per_ticker_block(tmp_path, monkeypatch):
    """The APPROX scanner must not bleed across ticker blocks: a `# APPROX`
    comment in one ticker's section can't make an adjacent clean ticker
    falsely report APPROX.
    """
    # Build a fake inputs/ tree where the refresh module's path constant
    # `INPUTS_DIR` points to our tmp tree. Easiest: monkeypatch the constant.
    inputs = tmp_path / "inputs"
    inputs.mkdir()
    watchlist_yaml = """\
ALPHA:
  current_price: 10.0
  analyst_target: 12.0
  consensus_pnav: 0.95
  as_of: 2026-05-29
BETA:
  current_price: 20.0
  analyst_target: 22.0
  consensus_pnav: 0.80     # APPROX -- replace with Pareto when available
  as_of: 2026-05-29
GAMMA:
  current_price: 30.0
  analyst_target: 35.0
  consensus_pnav: 0.90
  as_of: 2026-05-29
"""
    (inputs / "watchlist.yaml").write_text(watchlist_yaml)

    monkeypatch.setattr("crude_tanker_fv.refresh.INPUTS_DIR", inputs)

    watchlist = yaml.safe_load(watchlist_yaml)
    items = check_watchlist_freshness(watchlist, today=date(2026, 6, 1))
    by_t = {it.label: it.status for it in items}
    assert by_t["ALPHA"] == "ok"        # clean — no APPROX in its block
    assert by_t["BETA"] == "approx"     # has APPROX
    assert by_t["GAMMA"] == "ok"        # clean — APPROX is BEFORE its block, not within


def test_watchlist_stale_threshold(tmp_path, monkeypatch):
    """as_of older than 14 days → stale."""
    inputs = tmp_path / "inputs"
    inputs.mkdir()
    (inputs / "watchlist.yaml").write_text("""\
ALPHA:
  current_price: 10.0
  analyst_target: 12.0
  consensus_pnav: 0.95
  as_of: 2026-05-01
""")
    monkeypatch.setattr("crude_tanker_fv.refresh.INPUTS_DIR", inputs)
    watchlist = {"ALPHA": {"as_of": date(2026, 5, 1)}}
    items = check_watchlist_freshness(watchlist, today=date(2026, 6, 1))
    assert items[0].status == "stale"   # 31 days old


# ----------------------------------------------------------------------------
# Integration: build_checklist + render don't crash + write
# ----------------------------------------------------------------------------
def test_build_checklist_and_write_smoke(tmp_path):
    """End-to-end smoke test against the live inputs/ tree — exercises every
    section, confirms no crashes, writes a non-empty markdown file."""
    checklist = build_checklist(target_quarter="2026-Q1", today=date(2026, 6, 1))
    assert checklist.target_quarter == "2026-Q1"
    # Ticker counts grow as we onboard names — assert lower bound (>= 11 after
    # TRMD onboarding 2026-06-03) rather than exact count so future onboardings
    # don't require test rebases. The data_sources subset assertion below
    # provides per-name coverage verification.
    assert len(checklist.balance_sheets) >= 11
    assert len(checklist.market_data) == 5
    assert len(checklist.watchlist) >= 11
    assert len(checklist.per_ticker_ages) >= 11
    # Data sources must cover every ticker that's actually on the watchlist
    # (not just a known subset — protects against silent watchlist additions
    # that lack IR URLs in data_sources.yaml).
    from crude_tanker_fv.loaders import load_watchlist
    assert set(checklist.data_sources.keys()) >= set(load_watchlist().keys())
    # Render + write succeeds, file is non-trivial size.
    path = write_checklist(checklist, outputs_dir=tmp_path)
    content = path.read_text()
    assert "Refresh Checklist — 2026-Q1" in content
    assert "## 1. Missing quarterly balance sheets" in content
    assert "## 2. Stale market data" in content
    assert "## 3. Watchlist freshness" in content
    assert "## 4. Per-ticker file age table" in content
    assert "## 5. IR URL playbook" in content


def test_data_sources_covers_all_watchlist():
    """Every watchlist ticker must have a corresponding data_sources.yaml
    entry; otherwise the IR-playbook section renders ‘no data_sources entry’
    for that ticker — usable but a quality regression.
    """
    from crude_tanker_fv.loaders import load_watchlist
    from crude_tanker_fv.refresh import load_data_sources
    watchlist = set(load_watchlist().keys())
    sources = set(load_data_sources().keys())
    missing = watchlist - sources
    assert not missing, f"data_sources.yaml missing entries for: {missing}"


def test_forward_looking_quarter_flags_all_missing(tmp_path):
    """The killer use case: it's 2026-08-01, Q2 just closed, we have only Q1
    balance sheets on disk. The checklist must flag every watchlist BS as
    missing and surface the IR URLs to pull from.
    """
    # We can't easily backdate the today inside build_checklist without
    # touching the live inputs, so directly call with future today.
    from crude_tanker_fv.loaders import load_watchlist
    checklist = build_checklist(target_quarter=None, today=date(2026, 8, 1))
    assert checklist.target_quarter == "2026-Q2"
    # Every watchlist ticker must be flagged missing (we have only Q1 BSes).
    assert checklist.missing_bs_count == len(load_watchlist())
    # Render + spot-check that ASC's IR URLs surface in the missing section.
    path = write_checklist(checklist, outputs_dir=tmp_path)
    content = path.read_text()
    assert "ardmoreshipping.com" in content       # ASC's IR home / fleet
    assert "scorpiotankers.com" in content        # STNG's IR home / fleet
    assert "missing: DHT, ECO, FRO" in content    # status summary lists missing
