"""Filings triage ledger (2026-09-11): an acked accession stops flagging; a bad
disposition is refused; the ledger survives a round trip."""

from datetime import datetime, timezone

import pytest

from crude_tanker_fv import filings


def test_ack_round_trip_and_unacked_filter(tmp_path):
    p = tmp_path / "state" / "filings_triaged.json"
    assert filings.load(p) == {}
    now = datetime(2026, 9, 11, 14, 0, tzinfo=timezone.utc)
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
    monkeypatch.setattr(filings, "STATE_PATH", p)
    assert filings.main(["ack", "mfn-abc", "calendar: Q3 results 2026-11-26",
                         "--record", "decisions/cmbt_log.md"]) == 0
    assert filings.load(p)["mfn-abc"]["by"] == "agent"
