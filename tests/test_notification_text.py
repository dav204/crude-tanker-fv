import json

from crude_tanker_fv import notification_text as text, notify, work_items, delivery


def backlog():
    return ["FILING-LANDED DHT: 6-K accession-%d filed 2026-07-14 -> inputs/filings/%d.htm" % (i, i) for i in range(100)]


def test_page_separates_optional_choice_and_never_dumps_routine_backlog():
    flags = ["FILING-QUEUE-STALLED accession-0: 100 pending; oldest 2026-07-14T14:20:05+00:00; repair daily triage",
             "FORK-OPENED ten_commitments_convention: executes after 2026-09-24 unless you object — HOLD advances-only; NEEDS A CHAT",
             "FETCH-FAILED delivery-worker: heartbeat 0.825d old (cadence limit 0.010416666666666666d) — launchd stopped firing?"]
    subject, body = text.page_notice(flags, backlog(), "[crude-fv]", notify.page_action)
    assert "2 actions needed; 1 optional objection" in subject
    assert "Optional objections" in body and "2026-09-24" in body and "NEEDS A CHAT" in body
    assert "100 pending filings" in body and "2026-07-14" in body
    assert "19.8 hours" in body and "15 minutes" in body
    assert "restore the local delivery worker" in body and "credentials file" not in body
    assert "inputs/filings" not in body and "accession-99" not in body


def test_digest_aggregates_complete_backlog_and_retains_other_conditions():
    subject, body = text.digest_notice(backlog() + ["UNKNOWN-CONDITION needs investigation"], "[crude-fv]", 3)
    assert "100 filings awaiting triage; 1 other conditions" in subject
    assert "DHT 100" in body and "100 separate requests" in body
    assert "UNKNOWN-CONDITION" in body and "needs investigation" in body
    assert "3-day gap" in body and "state/sentinel.log" in body
    assert len(body.splitlines()) < 20 and "accession-99" not in body


def test_failed_publication_does_not_claim_cached_acceptance_as_run_success():
    body = text.operation_notice({"run_id": "run-123", "publication": {"status": "accepted"}}, {"publication": 1, "auto_land": 1})
    assert "did not confirm a successful publication" in body
    assert "Last recorded publication status: accepted" not in body
    assert "run-123.json" in body and "auto_land=1" in body
    assert '{"' not in body


def test_workflow_notices_are_prose_and_domain_duplicates_stay_recorded(tmp_path):
    conditions = {
        "governor:SYSTEM:PUBLICATION_HELD": {"status": "blocked", "resolver": "owner", "next_action": "resolve publication hold", "notification_owner": "governor"},
        "governor:consumption": {"status": "unknown", "resolver": "agent", "next_action": "repair missing consumption evidence"},
        "governor:TEN:GATES_PENDING": {"status": "blocked", "resolver": "owner", "next_action": "review remaining entry gates"},
    }
    work_items.observe_conditions(conditions, tmp_path)
    messages = list((tmp_path / "state/delivery").glob("*.json"))
    assert len(messages) == 1
    body = json.loads(messages[0].read_text())["body"]
    assert "PUBLICATION_HELD" not in body
    assert "remaining entry gates" in body and "missing consumption evidence" in body
    assert '{"' not in body and "Responsible: agent" in body
    assert work_items.observation(tmp_path)["conditions"] == conditions
    work_items.observe_conditions(conditions, tmp_path)
    assert len(list((tmp_path / "state/delivery").glob("*.json"))) == 1


def test_governor_only_projection_is_silent_but_visible(tmp_path):
    active = {"governor:SB:FV_DRIFT": {"status": "blocked", "notification_owner": "governor"}}
    result = work_items.observe_conditions(active, tmp_path)
    assert result["changes"] == list(active)
    assert not list((tmp_path / "state/delivery").glob("*.json"))
    assert work_items.observation(tmp_path)["conditions"] == active


def test_format_upgrade_never_rewrites_or_requeues_saved_event(tmp_path):
    import pytest
    path = delivery.enqueue("old subject", "exact queued message", tmp_path, key="event-1")
    original = path.read_bytes()
    reused = delivery.enqueue("clear subject", "better wording", tmp_path, key="event-1", reuse_existing=True)
    assert reused == path and path.read_bytes() == original
    with pytest.raises(ValueError):
        delivery.enqueue("different subject", "different body", tmp_path, key="event-1")
    assert len(list((tmp_path / "delivery").glob("*.json"))) == 1
