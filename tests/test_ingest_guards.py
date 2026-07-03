"""RC-ingest cursor guards (WO2 1.1): atomic state writes, the cursor-reset
refusal, and the max-messages sanity cap. All network mocked at the module
seam (auth/resolve/iter_history are module globals).

Note the deliberate asymmetry: a state file MISSING ENTIRELY reads as first
run (bootstrap walks full history — but the default --max-messages cap bounds
it and exits loud); a state file PRESENT with a missing per-source cursor is
a reset event and refuses outright.
"""

import json

import pytest

import crude_tanker_fv.ingest_rocketchat as ing

CFG = {"host": "https://rc.example", "group": "g",
       "sources": [{"name": "pareto_research", "kind": "file", "sender": "Immo",
                    "accept": ["pdf"], "dest_dir": "inputs/research_pareto"}]}


@pytest.fixture
def harness(tmp_path, monkeypatch):
    monkeypatch.setattr(ing, "STATE_FILE", tmp_path / "state" / "rc.json")
    monkeypatch.setattr(ing, "load_config", lambda: CFG)
    monkeypatch.setattr(ing, "auth_headers", lambda: {})
    monkeypatch.setattr(ing, "resolve_room_id", lambda host, group, headers: "room1")
    return tmp_path


def test_save_state_is_atomic_and_leaves_no_part(tmp_path, monkeypatch):
    monkeypatch.setattr(ing, "STATE_FILE", tmp_path / "state" / "rc.json")
    ing.save_state({"a": 1})
    assert json.loads((tmp_path / "state" / "rc.json").read_text()) == {"a": 1}
    assert not list((tmp_path / "state").glob("*.part"))


def test_missing_per_source_cursor_refuses_implicit_full_walk(harness, monkeypatch, capsys):
    ing.save_state({"some_other_source": {"last_seen_ts": "2026-07-01T00:00:00Z"}})
    walked = []
    monkeypatch.setattr(ing, "iter_history",
                        lambda *a, **kw: iter(walked))   # must never be consumed
    assert ing.main([]) == 3
    assert "CURSOR-RESET" in capsys.readouterr().err
    # A deliberate backfill IS allowed through the same state.
    monkeypatch.setattr(ing, "iter_history", lambda *a, **kw: iter([]))
    assert ing.main(["--backfill"]) == 0


def test_max_messages_cap_stops_without_advancing_cursor(harness, monkeypatch, capsys):
    msgs = [{"ts": f"2026-07-0{i}T00:00:00Z", "u": {"username": "nobody"}}
            for i in range(1, 7)]
    monkeypatch.setattr(ing, "iter_history", lambda *a, **kw: iter(msgs))
    assert ing.main(["--max-messages", "5"]) == 3
    assert "MAX-MESSAGES" in capsys.readouterr().err
    assert not ing.STATE_FILE.exists()   # cursor NOT advanced

    # Uncapped (0) completes and persists the cursor.
    monkeypatch.setattr(ing, "iter_history", lambda *a, **kw: iter(msgs))
    assert ing.main(["--max-messages", "0"]) == 0
    assert ing.STATE_FILE.exists()
