"""WO2 acceptance compiler: joins render honestly — ✅ on satisfied streams,
❌ rows (and a NOT ACCEPTED verdict) on failed joins. Synthetic state only."""

import json
from datetime import date
from pathlib import Path

from crude_tanker_fv.close_acceptance import compile_acceptance

START, END = date(2026, 7, 28), date(2026, 8, 6)


def _root(tmp_path) -> Path:
    (tmp_path / "state").mkdir()
    (tmp_path / "inputs").mkdir()
    (tmp_path / "decisions").mkdir()
    return tmp_path


def test_manual_fetch_fails_the_join_and_designed_exception_passes(tmp_path):
    root = _root(tmp_path)
    (root / "state" / "automation_runs.log").write_text(
        "2026-07-29T18:30:00Z job=price-refresh initiator=com.crude-tanker-fv.price-refresh outcome=ok rc=0\n"
        "2026-08-01T09:00:00Z job=news-pull initiator=session:mb-batch outcome=ok rc=0\n")
    text, ok = compile_acceptance(START, END, root)
    assert "✅ **Zero manual fetch initiators**" in text
    assert "designed-exception" in text

    (root / "state" / "automation_runs.log").write_text(
        "2026-07-30T10:00:00Z job=rocketchat-ingest initiator=manual:dan@ttys001 outcome=ok rc=0\n")
    text, ok = compile_acceptance(START, END, root)
    assert "❌ **Zero manual fetch initiators**" in text and not ok


def test_flag_days_join_to_sends_and_orphans_fail(tmp_path):
    root = _root(tmp_path)
    (root / "state" / "sentinel.log").write_text(
        "2026-07-30T08:15:00+00:00 FLAG 2: TRIGGER-DUE x | STALE-INPUT y\n")
    (root / "state" / "notify_sent.log").write_text(
        "2026-07-30T08:15:20+00:00 SENT [crude-fv] PAGE: 1 flag(s)\n")
    text, _ = compile_acceptance(START, END, root)
    assert "✅ **Every flag day joined to a sent email**" in text

    (root / "state" / "notify_sent.log").unlink()
    text, ok = compile_acceptance(START, END, root)
    assert "orphaned: ['2026-07-30']" in text and not ok


def test_quarantine_residue_fails(tmp_path):
    root = _root(tmp_path)
    q = root / "inputs" / "research_pareto" / "_quarantine"
    q.mkdir(parents=True)
    (q / "bad.pdf").write_bytes(b"x")
    (q / "bad.pdf.reason").write_text("no magic")
    text, ok = compile_acceptance(START, END, root)
    assert "❌ **Zero quarantine residue** — 1 file(s)" in text and not ok


def test_verdict_line_present(tmp_path):
    text, ok = compile_acceptance(START, END, _root(tmp_path))
    assert "**VERDICT: NOT ACCEPTED**" in text and not ok
