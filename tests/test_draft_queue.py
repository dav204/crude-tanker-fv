"""Draft queue (WO2 2.4a): staged quarterly filings with no packet yet; a
packet dated on/after the filing clears it. No network, no claude invocation
— the queue logic only."""

import json

import crude_tanker_fv.draft_queue as dq


def _manifest(tmp_path, entries):
    p = tmp_path / "edgar_manifest.jsonl"
    p.write_text("\n".join(json.dumps(e) for e in entries) + "\n")
    return p


def test_pending_packets_dedups_and_clears(tmp_path, monkeypatch):
    monkeypatch.setattr(dq, "MANIFEST", _manifest(tmp_path, [
        {"ticker": "DHT", "form": "6-K", "filed": "2026-08-05",
         "accession": "a1", "staged_path": "inputs/filings/DHT/a1.htm"},
        {"ticker": "DHT", "form": "6-K/A", "filed": "2026-08-06",
         "accession": "a2", "staged_path": "inputs/filings/DHT/a2.htm"},
        {"ticker": "TNK", "form": "8-K", "filed": "2026-08-05",
         "accession": "a3", "staged_path": "x"},          # not quarterly
        {"ticker": "GNK", "form": "10-Q", "filed": "2026-08-06",
         "accession": "a4", "staged_path": None},          # manifest-only
    ]))
    monkeypatch.setattr(dq, "DECISIONS", tmp_path / "decisions")
    (tmp_path / "decisions").mkdir()

    q = dq.pending_packets()
    assert [e["accession"] for e in q] == ["a2"]   # newest DHT only

    # A packet dated on/after the filing clears the ticker.
    (tmp_path / "decisions" / "dht_reconciliation_prereg_2026-08-07.md").write_text("x")
    assert dq.pending_packets() == []

    # An OLDER packet (last quarter's) does not.
    (tmp_path / "decisions" / "dht_reconciliation_prereg_2026-08-07.md").unlink()
    (tmp_path / "decisions" / "dht_reconciliation_prereg_2026-05-07.md").write_text("x")
    assert [e["accession"] for e in dq.pending_packets()] == ["a2"]
