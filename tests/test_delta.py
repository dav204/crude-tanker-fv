"""Tests for the delta + decision-log machinery (METHODOLOGY §7.7, §7.8).

Coverage targets:
  - First-run case (no prior snapshot) renders cleanly without exceptions.
  - Material-change classification (position flip, FV >10%, spread >5pp,
    NAV >5%) flags the right deltas as material and lets the rest pass.
  - Decision-log prepend creates the file with the header if missing AND
    preserves user-edited content below when the file already exists.
  - Snapshot round-trip (save → load) is lossless.
"""



from crude_tanker_fv.delta import (
    RunSnapshot,
    TickerSnapshot,
    compute_deltas,
    load_previous_snapshot,
    prepend_decision_log_entries,
    save_snapshot,
    snapshot_current_run,
    write_delta_report,
)


# ----------------------------------------------------------------------------
# Helpers — minimal stub objects matching the pipeline's return shapes
# ----------------------------------------------------------------------------
class _StubBlended:
    def __init__(self, fv): self.fair_value_per_share = fv


class _StubFV:
    def __init__(self, ticker, fv): self.ticker = ticker; self.blended = _StubBlended(fv)


class _StubScenario:
    def __init__(self, ticker, price, pw_fv, nav, ev, pos, breakeven, sector="crude"):
        self.ticker = ticker
        self.current_price = price
        self.probability_weighted_fv = pw_fv
        self.base_nav_per_share = nav
        self.expected_value_vs_current = ev
        self.position_recommendation = pos
        self.breakeven_tce = breakeven
        self.sector = sector


class _StubBroker:
    def __init__(self, ticker, spread, k):
        self.ticker = ticker
        self.spread = spread
        self.k_broker = k


def _make_snapshot(ticker_states: dict, run_at: str = "2026-06-01T00:00:00+00:00") -> RunSnapshot:
    """Build a RunSnapshot directly (bypassing pipeline objects) for diff tests."""
    return RunSnapshot(
        run_at=run_at,
        quarter="2026-Q1",
        tickers={t: TickerSnapshot(**fields) for t, fields in ticker_states.items()},
        input_file_hashes={},
    )


def _base_state(**overrides) -> dict:
    """Default ticker state — all fields populated; override individual keys per test."""
    state = dict(
        current_price=20.0,
        single_point_fv=18.0,
        scenario_pw_fv=17.0,
        nav_per_share=19.0,
        ev_pct=-15.0,
        position="TRIM/SHORT",
        breakeven_tce=45000.0,
        broker_spread_pp=-2.0,
        k_broker=0.98,
        sector="product",
    )
    state.update(overrides)
    return state


# ----------------------------------------------------------------------------
# Snapshot capture from pipeline objects
# ----------------------------------------------------------------------------
def test_snapshot_current_run_cross_indexes_by_ticker():
    """The three pipeline result lists (fv, scenarios, broker_rows) come in
    independent order. snapshot_current_run must merge by ticker, not position."""
    fv = [_StubFV("ASC", 14.59), _StubFV("DHT", 16.49)]
    # Scenarios in DIFFERENT order from FV — exercises the cross-indexing.
    sc = [
        _StubScenario("DHT", 16.40, 13.34, 15.29, -3.06, "TRIM/SHORT", 60000, sector="crude"),
        _StubScenario("ASC", 18.50, 13.59, 15.78, -4.91, "TRIM/SHORT", 77000, sector="product"),
    ]
    # Broker with one ticker missing — should default to 0pp spread / k=1.
    br = [_StubBroker("DHT", -1.1, 0.99)]

    snap = snapshot_current_run("2026-Q1", fv, sc, br)
    assert set(snap.tickers.keys()) == {"DHT", "ASC"}
    assert snap.tickers["DHT"].scenario_pw_fv == 13.34
    assert snap.tickers["DHT"].single_point_fv == 16.49
    assert snap.tickers["DHT"].sector == "crude"
    assert snap.tickers["ASC"].sector == "product"
    # Missing broker row → spread defaults to 0, k_broker to 1.0
    assert snap.tickers["ASC"].broker_spread_pp == 0.0
    assert snap.tickers["ASC"].k_broker == 1.0


# ----------------------------------------------------------------------------
# Diff: first-run case
# ----------------------------------------------------------------------------
def test_compute_deltas_first_run_marks_everyone_new():
    current = _make_snapshot({"DHT": _base_state(), "ASC": _base_state()})
    report = compute_deltas(current, previous=None)
    assert report.is_first_run is True
    assert report.previous_run_at is None
    assert len(report.deltas) == 2
    assert all(d.is_new for d in report.deltas)
    assert all(d.material is False for d in report.deltas)  # nothing to compare
    assert all(d.delta_fv is None for d in report.deltas)


# ----------------------------------------------------------------------------
# Diff: material vs non-material classification
# ----------------------------------------------------------------------------
def test_position_flip_is_always_material():
    prev = _make_snapshot({"X": _base_state(position="TRIM/SHORT")})
    cur = _make_snapshot({"X": _base_state(position="BUY")})
    r = compute_deltas(cur, prev)
    d = r.deltas[0]
    assert d.position_changed is True
    assert d.material is True
    assert any("position" in reason for reason in d.material_reasons)


def test_fv_under_threshold_not_material():
    prev = _make_snapshot({"X": _base_state(single_point_fv=18.0, scenario_pw_fv=17.0)})
    # +5% on single FV, +5% on PW FV — both under 10% material threshold.
    cur = _make_snapshot({"X": _base_state(single_point_fv=18.9, scenario_pw_fv=17.85)})
    r = compute_deltas(cur, prev)
    d = r.deltas[0]
    assert d.material is False
    assert d.delta_fv_pct == 5.0


def test_fv_over_threshold_material():
    prev = _make_snapshot({"X": _base_state(single_point_fv=18.0)})
    cur = _make_snapshot({"X": _base_state(single_point_fv=22.0)})  # +22%
    r = compute_deltas(cur, prev)
    d = r.deltas[0]
    assert d.material is True
    assert any("single-point FV" in reason for reason in d.material_reasons)


def test_broker_spread_shift_classification():
    """5.1pp = material, exactly 5.0pp = not material (strict > threshold)."""
    prev = _make_snapshot({"X": _base_state(broker_spread_pp=-2.0)})
    cur51 = _make_snapshot({"X": _base_state(broker_spread_pp=3.1)})   # +5.1pp
    cur50 = _make_snapshot({"X": _base_state(broker_spread_pp=3.0)})   # +5.0pp exact
    assert compute_deltas(cur51, prev).deltas[0].material is True
    assert compute_deltas(cur50, prev).deltas[0].material is False


def test_nav_move_material_threshold():
    """5.1% NAV shift is material; 5.0% exactly is not."""
    prev = _make_snapshot({"X": _base_state(nav_per_share=19.0)})
    cur = _make_snapshot({"X": _base_state(nav_per_share=20.0)})  # +5.26% → material
    assert compute_deltas(cur, prev).deltas[0].material is True


# ----------------------------------------------------------------------------
# Diff: new and dropped tickers
# ----------------------------------------------------------------------------
def test_new_ticker_flagged_and_dropped_ticker_tracked():
    prev = _make_snapshot({"DHT": _base_state(), "DROP": _base_state()})
    cur = _make_snapshot({"DHT": _base_state(), "NEW": _base_state()})
    r = compute_deltas(cur, prev)
    new_deltas = [d for d in r.deltas if d.is_new]
    assert {d.ticker for d in new_deltas} == {"NEW"}
    assert r.dropped_tickers == ["DROP"]


# ----------------------------------------------------------------------------
# Input file hash diff
# ----------------------------------------------------------------------------
def test_input_file_hash_diff_categorises_changes():
    prev = _make_snapshot({})
    prev.input_file_hashes = {"a.yaml": "h1", "b.yaml": "h2", "removed.yaml": "h3"}
    cur = _make_snapshot({})
    cur.input_file_hashes = {"a.yaml": "h1", "b.yaml": "h2_NEW", "added.yaml": "h4"}
    r = compute_deltas(cur, prev)
    assert "b.yaml" in r.changed_input_files
    assert "added.yaml" in r.new_input_files
    assert "removed.yaml" in r.removed_input_files
    assert "a.yaml" not in r.changed_input_files  # unchanged hash


# ----------------------------------------------------------------------------
# Snapshot persistence
# ----------------------------------------------------------------------------
def test_snapshot_save_load_roundtrip(tmp_path):
    state = _make_snapshot({"DHT": _base_state(), "ASC": _base_state(sector="product")})
    state.input_file_hashes = {"inputs/watchlist.yaml": "deadbeef"}
    path = tmp_path / "last_run.json"
    save_snapshot(state, path)
    loaded = load_previous_snapshot(path)
    assert loaded is not None
    assert loaded.tickers["DHT"].current_price == state.tickers["DHT"].current_price
    assert loaded.tickers["ASC"].sector == "product"
    assert loaded.input_file_hashes == {"inputs/watchlist.yaml": "deadbeef"}


def test_load_previous_snapshot_returns_none_when_absent(tmp_path):
    assert load_previous_snapshot(tmp_path / "does_not_exist.json") is None


# ----------------------------------------------------------------------------
# Decision-log prepend
# ----------------------------------------------------------------------------
def test_decision_log_creates_file_with_header_on_first_run(tmp_path):
    cur = _make_snapshot({"NEWNAME": _base_state()})
    report = compute_deltas(cur, previous=None)
    paths = prepend_decision_log_entries(report, decisions_dir=tmp_path)
    assert len(paths) == 1
    content = paths[0].read_text()
    # Header present, ticker tagged, model state section, decision placeholder.
    assert "NEWNAME — Decision Log" in content
    assert "Chronological record" in content
    assert "## 2026-06-01" in content
    assert "- Position: **TRIM/SHORT**" in content
    assert "**Decision:** _[pending annotation]_" in content
    assert "_First snapshot — no prior state to compare._" in content


def test_decision_log_prepend_preserves_user_content_below(tmp_path):
    """The killer feature: prior entries (and any user annotation) must
    survive verbatim when a new entry is prepended."""
    # Simulate an existing log with a user annotation in the prior entry.
    log = tmp_path / "x_log.md"
    log.write_text(
        "# X — Decision Log\n\nIntro text.\n\n---\n\n"
        "## 2026-05-01T00:00:00+00:00 — Pipeline run (auto)\n\n"
        "**Model state:** stuff\n\n"
        "**Decision:** Held. Phase 1 thesis intact.\n\n"  # ← user annotation
        "---\n"
    )
    cur = _make_snapshot({"X": _base_state()}, run_at="2026-06-01T00:00:00+00:00")
    prev = _make_snapshot({"X": _base_state()}, run_at="2026-05-01T00:00:00+00:00")
    report = compute_deltas(cur, prev)
    prepend_decision_log_entries(report, decisions_dir=tmp_path)
    new_content = log.read_text()
    # User annotation must be intact.
    assert "Held. Phase 1 thesis intact." in new_content
    # Old timestamp must still be present.
    assert "2026-05-01T00:00:00+00:00" in new_content
    # New entry must be at the top (between header and prior entry).
    new_pos = new_content.index("2026-06-01T00:00:00+00:00")
    old_pos = new_content.index("2026-05-01T00:00:00+00:00")
    assert new_pos < old_pos, "newest entry should be above older entries"


def test_decision_log_filename_is_lowercase(tmp_path):
    """Standardise on lowercase filenames so the ticker case in YAML doesn't
    spawn case-variant duplicate files on case-sensitive filesystems."""
    cur = _make_snapshot({"STNG": _base_state()})
    report = compute_deltas(cur, previous=None)
    paths = prepend_decision_log_entries(report, decisions_dir=tmp_path)
    assert paths[0].name == "stng_log.md"


# ----------------------------------------------------------------------------
# Markdown rendering smoke tests
# ----------------------------------------------------------------------------
def test_delta_report_first_run_renders(tmp_path):
    cur = _make_snapshot({"DHT": _base_state()})
    report = compute_deltas(cur, previous=None)
    path = write_delta_report(report, outputs_dir=tmp_path)
    content = path.read_text()
    assert "# Pipeline Delta Report" in content
    assert "First run." in content
    assert "no deltas computed yet" in content


def test_delta_report_subsequent_run_no_material_renders(tmp_path):
    prev = _make_snapshot({"DHT": _base_state()}, run_at="2026-05-01T00:00:00+00:00")
    cur = _make_snapshot({"DHT": _base_state()}, run_at="2026-06-01T00:00:00+00:00")
    report = compute_deltas(cur, prev)
    path = write_delta_report(report, outputs_dir=tmp_path)
    content = path.read_text()
    assert "No material changes." in content
    assert "no input file changes detected" in content
    assert "(no change)" in content     # full table renders with no-change marks


def test_delta_report_material_change_renders_with_flag(tmp_path):
    prev = _make_snapshot({"DHT": _base_state(position="HOLD")},
                          run_at="2026-05-01T00:00:00+00:00")
    cur = _make_snapshot({"DHT": _base_state(position="BUY")},
                         run_at="2026-06-01T00:00:00+00:00")
    report = compute_deltas(cur, prev)
    path = write_delta_report(report, outputs_dir=tmp_path)
    content = path.read_text()
    assert "**DHT:**" in content
    assert "HOLD → BUY" in content
    assert "⚑" in content       # material flag in full table
    assert "⟵" in content       # position-flip arrow in full table


def test_delta_report_flags_mixed_anchor_basis(tmp_path):
    """A table spanning sectors on different cycle-anchor bases gets the
    MIXED-ANCHOR-BASIS note (B5 — METHODOLOGY §10)."""
    cur = _make_snapshot({
        "DHT": _base_state(sector="crude"),         # tc_10yr_mean
        "SBLK": _base_state(sector="dry_bulk"),     # archive_22mo_median
    })
    report = compute_deltas(cur, previous=None)
    content = write_delta_report(report, outputs_dir=tmp_path).read_text()
    assert "MIXED-ANCHOR-BASIS" in content
    assert "tc_10yr_mean" in content
    assert "archive_22mo_median" in content


def test_delta_report_no_mixed_anchor_basis_flag_within_one_basis(tmp_path):
    """Crude + product + LNG are all tc_10yr_mean → no cross-basis warning."""
    cur = _make_snapshot({
        "DHT": _base_state(sector="crude"),
        "STNG": _base_state(sector="product"),
        "FLNG": _base_state(sector="lng"),
    })
    report = compute_deltas(cur, previous=None)
    content = write_delta_report(report, outputs_dir=tmp_path).read_text()
    assert "MIXED-ANCHOR-BASIS" not in content
