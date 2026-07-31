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
from datetime import date, datetime, timezone

import pytest
import yaml

from crude_tanker_fv.refresh import (
    MARKET_DATA_FILES,
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
    assert items[0].status == "ok"      # 31d — inside the 42d threshold (owner 2026-07-06)
    items = check_watchlist_freshness(watchlist, today=date(2026, 6, 15))
    assert items[0].status == "stale"   # 45d — beyond it


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


def test_reweight_triggers_due_fired_and_upcoming(tmp_path):
    """§13.3 triggers (audit F-2: the 'MoU signs' prose trigger fired Jun-17
    and sat 15 days unwatched). The preflight must red a due/overdue or FIRED
    trigger, amber one due within the horizon, and pass armed-future /
    standing-watch / done ones."""
    import yaml

    from crude_tanker_fv.refresh import check_reweight_triggers

    (tmp_path / "reweight_triggers.yaml").write_text(yaml.safe_dump({
        "overdue_one": {"sector": "crude", "due": date(2026, 7, 1),
                        "observable": "x", "action": "y", "status": "armed"},
        "fired_one": {"sector": "crude", "due": None,
                      "observable": "x", "action": "y", "status": "fired"},
        "soon_one": {"sector": "crude", "due": date(2026, 7, 10),
                     "observable": "x", "action": "y", "status": "armed"},
        "future_one": {"sector": "all", "due": date(2026, 10, 2),
                       "observable": "x", "action": "y", "status": "armed"},
        "watch_one": {"sector": "crude", "due": None,
                      "observable": "x", "action": "y", "status": "armed"},
        "done_one": {"sector": "crude", "due": date(2026, 6, 1),
                     "observable": "x", "action": "y", "status": "done"},
    }))
    items = {i.label: i for i in check_reweight_triggers(tmp_path, today=date(2026, 7, 2))}
    assert items["overdue_one"].status == "missing" and "DUE" in items["overdue_one"].detail
    assert items["fired_one"].status == "missing" and "OWED" in items["fired_one"].detail
    assert items["soon_one"].status == "warn"
    assert items["future_one"].status == "ok"
    assert items["watch_one"].status == "ok" and "event-watch" in items["watch_one"].detail
    assert items["done_one"].status == "ok"


def test_reweight_triggers_missing_file_warns(tmp_path):
    from crude_tanker_fv.refresh import check_reweight_triggers

    items = check_reweight_triggers(tmp_path, today=date(2026, 7, 2))
    assert len(items) == 1 and items[0].status == "warn"


def test_live_trigger_file_loads_and_renders():
    """The committed inputs/reweight_triggers.yaml parses, every entry carries
    the required fields, and the checklist renders the section."""
    import yaml

    from crude_tanker_fv.refresh import REWEIGHT_TRIGGERS_PATH, check_reweight_triggers

    doc = yaml.safe_load(REWEIGHT_TRIGGERS_PATH.read_text())
    assert doc, "trigger file empty"
    for name, entry in doc.items():
        for f in ("sector", "observable", "action", "status", "added"):
            assert f in entry, f"{name} missing {f}"
        assert "due" in entry, f"{name} missing due (use null for event-watch)"
    items = check_reweight_triggers(today=date(2026, 7, 2))
    assert len(items) == len(doc)
    # The two dated 2026 checkpoints from the 2026-07-02 review must be present.
    assert "crude_mou_implementation_check" in doc and doc["crude_mou_implementation_check"]["due"] == date(2026, 7, 17)
    assert "crude_day60_toll_cliff" in doc and doc["crude_day60_toll_cliff"]["due"] == date(2026, 8, 16)


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
    # 2026-07-31: Q2 balance sheets are now ARRIVING (SB first) — the "all missing"
    # premise expires file-by-file. Assert against the actual on-disk census instead
    # of a hard 25 so each refresh doesn't re-red this test.
    import glob as _glob
    n_q2_on_disk = len(_glob.glob("inputs/balance_sheets/*_2026-Q2.yaml"))
    assert checklist.target_quarter == "2026-Q2"
    # Every watchlist ticker must be flagged missing (we have only Q1 BSes).
    assert checklist.missing_bs_count == len(load_watchlist()) - n_q2_on_disk
    # Render + spot-check that ASC's IR URLs surface in the missing section.
    path = write_checklist(checklist, outputs_dir=tmp_path)
    content = path.read_text()
    assert "ardmoreshipping.com" in content       # ASC's IR home / fleet
    assert "scorpiotankers.com" in content        # STNG's IR home / fleet
    assert "missing: DHT, ECO, FRO" in content    # status summary lists missing


# ----------------------------------------------------------------------------
# Earnings calendar check (added 2026-06-11, Q2 earnings-readiness pass)
# ----------------------------------------------------------------------------
def _cal_fixture(tmp_path, window_start, window_end):
    inputs = tmp_path / "inputs"
    (inputs / "balance_sheets").mkdir(parents=True)
    (inputs / "earnings_calendar.yaml").write_text(yaml.safe_dump({
        "meta": {"quarter": "2026-Q2"},
        "names": {"DHT": {"window_start": window_start, "window_end": window_end,
                          "status": "expected", "basis": "test"}},
    }))
    return inputs


def test_earnings_future_date_is_ok(tmp_path):
    from crude_tanker_fv.refresh import check_earnings_calendar
    inputs = _cal_fixture(tmp_path, date(2026, 8, 5), date(2026, 8, 6))
    items = check_earnings_calendar("2026-Q1", {"DHT": {}}, inputs,
                                    today=date(2026, 6, 11))
    assert items[0].status == "ok"


def test_earnings_upcoming_within_horizon_warns(tmp_path):
    from crude_tanker_fv.refresh import check_earnings_calendar
    inputs = _cal_fixture(tmp_path, date(2026, 8, 5), date(2026, 8, 6))
    items = check_earnings_calendar("2026-Q2", {"DHT": {}}, inputs,
                                    today=date(2026, 7, 25))
    assert items[0].status == "warn"
    assert "reports in 11d" in items[0].detail


def test_earnings_report_out_no_bs_is_due(tmp_path):
    from crude_tanker_fv.refresh import check_earnings_calendar
    inputs = _cal_fixture(tmp_path, date(2026, 8, 5), date(2026, 8, 6))
    items = check_earnings_calendar("2026-Q2", {"DHT": {}}, inputs,
                                    today=date(2026, 8, 10))
    assert items[0].status == "missing"
    assert "refresh due" in items[0].detail


def test_earnings_report_out_with_bs_is_ok(tmp_path):
    from crude_tanker_fv.refresh import check_earnings_calendar
    inputs = _cal_fixture(tmp_path, date(2026, 8, 5), date(2026, 8, 6))
    (inputs / "balance_sheets" / "dht_2026-Q2.yaml").write_text("{}")
    items = check_earnings_calendar("2026-Q2", {"DHT": {}}, inputs,
                                    today=date(2026, 8, 10))
    assert items[0].status == "ok"


def test_earnings_no_entry_warns(tmp_path):
    from crude_tanker_fv.refresh import check_earnings_calendar
    inputs = _cal_fixture(tmp_path, date(2026, 8, 5), date(2026, 8, 6))
    items = check_earnings_calendar("2026-Q2", {"DHT": {}, "ECO": {}}, inputs,
                                    today=date(2026, 6, 11))
    eco = next(i for i in items if i.label == "ECO")
    assert eco.status == "warn"
    assert "no earnings date" in eco.detail


def test_reweight_trigger_fired_ruled_deferred_ambers_then_escalates(tmp_path):
    """Signed-ruling deferral (tanker forward-print ruling §6, signed 2026-07-15):
    fired-ruled-deferred must surface as WARN every run (AMBER — visible without
    daily re-triage) while the stage_a_deadline holds, and ESCALATE to red the
    day after it passes unpromoted (Rider 2's unconditional exit, enforced by
    code not prose). A bare novel status would have fallen to the ok branch and
    silently un-paged the item — the exact opposite of the ruling's intent."""
    import yaml as _yaml

    from crude_tanker_fv.refresh import check_reweight_triggers

    (tmp_path / "reweight_triggers.yaml").write_text(_yaml.safe_dump({
        "deferred_one": {"sector": "crude+product", "due": None,
                         "observable": "x", "action": "y",
                         "status": "fired-ruled-deferred",
                         "stage_a_deadline": date(2026, 8, 15),
                         "ruling": "decisions/tanker_forward_print_ruling_2026-07-14.md"},
    }))
    before = {i.label: i for i in check_reweight_triggers(tmp_path, today=date(2026, 7, 20))}
    assert before["deferred_one"].status == "warn"
    assert "Stage A" in before["deferred_one"].detail

    on_deadline = {i.label: i for i in check_reweight_triggers(tmp_path, today=date(2026, 8, 15))}
    assert on_deadline["deferred_one"].status == "warn"   # the deadline day itself is still execution day

    after = {i.label: i for i in check_reweight_triggers(tmp_path, today=date(2026, 8, 16))}
    assert after["deferred_one"].status == "missing"
    assert "BREACHED" in after["deferred_one"].detail
