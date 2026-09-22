"""Filings triage ledger (2026-09-11): an acked accession stops flagging; a bad
disposition is refused; the ledger survives a round trip."""

from datetime import datetime, timezone

import pytest

from crude_tanker_fv import filings
import subprocess


def commit_record(root, record, text):
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    path = root / record
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    subprocess.run(["git", "add", record], cwd=root, check=True)
    subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=test@localhost", "commit", "-qm", "record"], cwd=root, check=True)



def test_ack_round_trip_and_unacked_filter(tmp_path):
    p = tmp_path / "state" / "filings_triaged.json"
    assert filings.load(p) == {}
    now = datetime(2026, 9, 11, 14, 0, tzinfo=timezone.utc)
    commit_record(tmp_path, "decisions/sb_log.md", "0001317861-26-000047 record-only: AGM results")
    rec = filings.ack("0001317861-26-000047", "record-only: AGM results",
                      "decisions/sb_log.md", path=p, now=now)
    assert rec["disposition"].startswith("record-only")
    assert rec["at"] == "2026-09-11T14:00:00+00:00"
    assert filings.is_acked("0001317861-26-000047", p)
    assert not filings.is_acked("0001317861-26-000048", p)
    entries = [{"accession": "0001317861-26-000047"}, {"accession": "0001317861-26-000048"},
               {"ticker": "X"}]
    assert filings.unacked(entries, p) == [{"accession": "0001317861-26-000048"}]
    assert filings.load(p)["0001317861-26-000047"]["record"] == "decisions/sb_log.md"


def test_ack_refuses_an_unregistered_disposition(tmp_path):
    p = tmp_path / "state" / "filings_triaged.json"
    with pytest.raises(SystemExit):
        filings.ack("acc", "shrug", path=p)
    assert filings.load(p) == {}


def test_cli_ack_writes_the_ledger(tmp_path, monkeypatch):
    p = tmp_path / "state" / "filings_triaged.json"
    commit_record(tmp_path, "decisions/cmbt_log.md", "mfn-abc calendar: Q3 results 2026-11-26")
    monkeypatch.setattr(filings, "STATE_PATH", p)
    assert filings.main(["ack", "mfn-abc", "calendar: Q3 results 2026-11-26",
                         "--record", "decisions/cmbt_log.md"]) == 0
    assert filings.load(p)["mfn-abc"]["by"] == "agent"


def test_queue_survives_weekend_and_more_than_eighty_arrivals(tmp_path):
    from datetime import timedelta
    now = datetime(2026, 9, 22, 15, tzinfo=timezone.utc)
    entries = [{'accession': 'old', 'ts': (now - timedelta(days=5)).isoformat()}]
    entries += [{'accession': str(i), 'ts': now.isoformat()} for i in range(100)]
    entries += [entries[0]]
    q = filings.queue(entries, tmp_path / 'state/filings_triaged.json', now)
    assert q['pending_total'] == 101 and q['pending'][0]['accession'] == 'old'
    assert q['oldest_business_days'] == 3


def test_bad_timestamp_stays_visible_and_corrupt_ledger_is_not_empty(tmp_path):
    state = tmp_path / 'ledger.json'
    q = filings.queue([{'accession': 'mfn-1', 'ts': 'oops'}], state)
    assert q['pending_total'] == 1 and q['invalid']
    state.write_text('broken')
    with pytest.raises(ValueError):
        filings.load(state)


def test_ack_requires_committed_evidence(tmp_path):
    commit_record(tmp_path, 'decisions/test.md', 'accession1 record-only: reviewed')
    with pytest.raises(ValueError):
        filings.ack('accession2', 'record-only: reviewed', 'decisions/test.md', path=tmp_path/'state/filings_triaged.json')
