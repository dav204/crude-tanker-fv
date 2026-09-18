"""The owner's weekly report (2026-09-02) — derived, honest, and write-free.

The report replaces reading a 30-flag daily digest, so its failure modes are: claiming a
health problem that is only a weekly job's normal cadence, inventing an actionable long,
and writing anything it shouldn't.
"""

from datetime import date
from pathlib import Path

from crude_tanker_fv import weekly_report as wr

ROOT = Path(__file__).resolve().parents[1]


def test_edge_cleared_parse_ignores_prose_words():
    """The generated sentence reads 'SB — dry bulk, cheap on both NAV bases': NAV is prose,
    not a ticker. Intersecting with the book's own roster is what keeps it out."""
    md = ROOT / "outputs" / "book_scorecard.md"
    if not md.exists():
        return
    got = wr._edge_cleared_from_md(md, known={"SB", "SBLK", "DHT"})
    assert got is not None
    names, _inner = got
    assert "NAV" not in names
    assert set(names) <= {"SB", "SBLK", "DHT"}


def test_weekly_job_is_not_late_at_four_days(tmp_path):
    """A Saturday job at 96h is on cadence; judging it on the daily 48h limit is the false
    alarm the report exists to remove."""
    import plistlib

    weekly = tmp_path / "com.crude-tanker-fv.news-pull.plist"
    weekly.write_bytes(plistlib.dumps({
        "Label": "x", "ProgramArguments": ["/x.sh"],
        "StartCalendarInterval": {"Hour": 8, "Minute": 0, "Weekday": 6}}))
    daily = tmp_path / "com.crude-tanker-fv.sentinel.plist"
    daily.write_bytes(plistlib.dumps({
        "Label": "y", "ProgramArguments": ["/y.sh"],
        "StartCalendarInterval": {"Hour": 8, "Minute": 15}}))
    hourly = tmp_path / "com.crude-tanker-fv.edgar-poll.plist"
    hourly.write_bytes(plistlib.dumps({
        "Label": "z", "ProgramArguments": ["/z.sh"],
        "StartCalendarInterval": {"Minute": 20}}))
    assert wr._cadence_limit_hours(weekly) == 9 * 24.0
    assert wr._cadence_limit_hours(daily) == 48.0
    assert wr._cadence_limit_hours(hourly) == 6.0


def test_book_moves_reports_only_threshold_crossings():
    def row(**kw):
        base = {"ticker": "AAA", "position": "HOLD", "confidence_tier": "VALIDATED-TIGHT",
                "read_flag": "robust", "nav_per_share": 10.0, "ev_pct": 1.0}
        base.update(kw)
        return base

    now = {"AAA": row(), "BBB": row(ticker="BBB", nav_per_share=10.15),
           "CCC": row(ticker="CCC", position="BUY (undervalued)"), "DDD": row(ticker="DDD")}
    prior = {"AAA": row(), "BBB": row(ticker="BBB", nav_per_share=10.0),
             "CCC": row(ticker="CCC"), "EEE": row(ticker="EEE")}
    kinds = {(m.ticker, m.kind) for m in wr._book_moves(now, prior)}
    assert ("AAA", "NAV") not in kinds          # unchanged
    assert ("BBB", "NAV") not in kinds          # +1.5% is under the 2% threshold
    assert ("CCC", "BAND") in kinds             # a band flip always reports
    assert ("DDD", "NEW") in kinds
    assert ("EEE", "GONE") in kinds


def test_build_report_writes_nothing(tmp_path, monkeypatch):
    """A report build must never write governed state — the file is written by main() only
    (the 2026-07-18 / 08-14 shared-state doctrine)."""
    before = {p: p.stat().st_mtime_ns for p in (ROOT / "outputs").glob("*") if p.is_file()}
    state_before = {p: p.stat().st_mtime_ns for p in (ROOT / "state").rglob("*") if p.is_file()}
    text = wr.build_report()
    assert text.startswith("# Weekly report — ")
    for section in ("## 1. The book", "## 2. Needs your word", "## 3. What the machine did",
                    "## 4. Health", "## 5. Next 14 days"):
        assert section in text
    after = {p: p.stat().st_mtime_ns for p in (ROOT / "outputs").glob("*") if p.is_file()}
    state_after = {p: p.stat().st_mtime_ns for p in (ROOT / "state").rglob("*") if p.is_file()}
    assert after == before, "build_report wrote into outputs/"
    assert state_after == state_before, "build_report wrote into state/"


def test_calendar_flags_overdue_triggers():
    items = wr._calendar(days=14)
    assert all(len(w) == 2 for w in items)
    overdue = [what for when, what in items if when < date.today().isoformat()]
    assert all("OVERDUE" in w for w in overdue), overdue


def test_is_due_catches_up_after_a_dark_weekend(tmp_path, monkeypatch):
    """2026-09-07, found live: the first cut gated the report on a shell `date +%u -eq 6`
    test. The Mac was dark 9/05-9/06; launchd COALESCED the missed firings into one run on
    Monday, where the weekday test is false — so the report silently skipped and, being
    weekday-gated, could never catch up. On a laptop a dark weekend is normal, so the week's
    report belongs to the most recent Saturday and is owed on any later day until written."""
    from datetime import date

    from crude_tanker_fv import weekly_report as wr

    out = tmp_path / "outputs"
    out.mkdir()
    monkeypatch.setattr(wr, "OUTPUTS", out)

    due, why = wr.is_due(date(2026, 9, 7))
    assert due and "never has" not in why           # nothing written yet -> due

    (out / "weekly_report_2026-09-02.md").write_text("x")
    for day, expect in ((date(2026, 9, 5), True),   # Saturday itself
                        (date(2026, 9, 7), True),   # Monday catch-up — the live failure
                        (date(2026, 9, 11), True)): # still owed later that week
        assert wr.is_due(day)[0] is expect, day

    # Once the catch-up report is written, the same week must not fire again...
    (out / "weekly_report_2026-09-07.md").write_text("x")
    assert wr.is_due(date(2026, 9, 7))[0] is False
    assert wr.is_due(date(2026, 9, 9))[0] is False
    # ...but the NEXT Saturday is a new week and is due again.
    assert wr.is_due(date(2026, 9, 12))[0] is True


def test_wrapper_calls_the_report_unconditionally():
    """The weekday decision must live in the module, not the shell — a coalesced run lands
    on whatever day the Mac wakes."""
    from pathlib import Path
    w = (Path(__file__).resolve().parents[1] / "scripts" / "sentinel_cron.sh").read_text()
    cmds = [ln for ln in w.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]
    assert any("--if-due" in ln for ln in cmds), "the wrapper must delegate the due decision"
    assert not any("date +%u" in ln for ln in cmds), (
        "no weekday gate may remain in a COMMAND line (the comment explaining why is fine)")


def test_owner_queue_excludes_agent_class_work(tmp_path):
    """2026-09-12: the report listed 'Refresh owed — TEN reported and has no balance sheet on
    file' under 'Needs your word', and the owner read it as his debt. A balance-sheet refresh,
    filings triage, unreadable exhibits and the S&P ack are agent work: they ride the agent
    queue, with the shadow verdict when a shadow build exists; only page-class tags and the
    ask-tier FFA queue ask for the owner's word."""
    flags = [
        "STALE-BALANCE-SHEET TEN: report OUT (2026-09-10, confirmed) and no 2026-Q2 balance sheet on file",
        "FILING-LANDED SB: 6-K 0001-26-000048 filed 2026-09-11 -> x.htm",
        "FLEET-TRANSACTION 3 unreviewed print candidates",
        "TRIGGER-DUE crude_geopolitics_weekly: [crude+product] DUE 2026-09-17 — check the "
        "observable and record the outcome. x",
        "FORK-EXECUTABLE stage_b_open_items: executable 2026-09-14",
        "FORK-OPENED spot_tce_promote_2026-09-10: opened 2026-09-10, executes after 2026-09-15",
        "UNINGESTED-PRINTS ffa widget newer than curve",
    ]
    owner = wr._queue_lines(flags)
    assert len(owner) == 3
    # the owner tags come from inputs/notify.yaml (page + page_once): FORK-OPENED is the one
    # whose objection window matters; FORK-EXECUTABLE is agent-class since 2026-09-16
    assert owner[0].startswith("TRIGGER-DUE — crude_geopolitics_weekly:")   # the card is named
    assert owner[1].startswith("FORK-OPENED — spot_tce_promote_2026-09-10:")
    assert "ask-tier" in owner[2]
    assert not any(q.startswith("FORK-EXECUTABLE") for q in owner)
    assert not any("Refresh owed" in q or "TEN" in q for q in owner)
    assert "FORK-OPENED" in wr.owner_tags() and "FORK-EXECUTABLE" not in wr.owner_tags()

    (tmp_path / "ten_shadow_build_2026-09-11.md").write_text(
        "# TEN shadow\n\n**VERDICT (one line, repeated at the end): WOULD-HOLD** — top summary\n\n## 9\n\n**VERDICT: WOULD-HOLD** — six fields unverified\n")
    agent = wr._agent_lines(flags, decisions_dir=tmp_path)
    assert agent[0].startswith("Balance-sheet refresh queued (agent) — TEN reported 2026-09-10")
    assert "ten_shadow_build_2026-09-11.md: WOULD-HOLD" in agent[0]
    assert any(q.startswith("Filings triage (agent") for q in agent)
    assert any(q.startswith("S&P queue (agent") for q in agent)
    assert wr._agent_lines(["STALE-BALANCE-SHEET ZZZ: report OUT"], decisions_dir=tmp_path)[0].endswith(
        "stages when it arrives")
