import json
import subprocess
from datetime import date

import pytest
from crude_tanker_fv import work_items as wi


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def fixture(tmp_path):
    root = tmp_path / "crude-tanker-fv"
    root.mkdir()
    git(root, "init", "-q")
    git(root, "config", "user.name", "Test")
    git(root, "config", "user.email", "test@localhost")
    (root / "decisions").mkdir()
    (root / "decisions/ten.md").write_text("TEN owner blocked\n")
    (root / "inputs").mkdir()
    (root / "inputs/forks.yaml").write_text("forks: []\n")
    (root / "inputs/reweight_triggers.yaml").write_text("{}")
    git(root, "add", ".")
    git(root, "commit", "-qm", "initial")
    row = wi.item(
        "roadmap:ten-q2",
        "producer",
        "blocked",
        "Owner must rule the shuttle basis",
        "owner",
        evidence=[{"path": "decisions/ten.md", "project": "producer", "contains": "owner blocked"}],
        waiting="ruling",
        blockers=["TEN-basis"],
        verified_at="2026-09-22",
    )
    (root / "work_items.yaml").write_text(
        json.dumps({"version": 1, "integration_enabled": True, "items": [row]})
    )
    return root


def test_owner_block_then_committed_completion(tmp_path):
    root = fixture(tmp_path)
    doc = wi.project(root, date(2026, 9, 22))
    owner, agent = wi.queues(doc)
    assert any("TEN-basis" in s and "owner" in s for s in owner)
    (root / "decisions/ten.md").write_text("TEN pair is landed; candidate gate still applies\n")
    data = json.loads((root / "work_items.yaml").read_text())
    data["items"][0].update(
        status="done", evidence=[{"path": "decisions/ten.md", "contains": "pair is landed"}]
    )
    (root / "work_items.yaml").write_text(json.dumps(data))
    doc = wi.project(root, date(2026, 9, 22))
    assert (
        doc["items"][next(i for i, r in enumerate(doc["items"]) if r["id"] == "roadmap:ten-q2")][
            "status"
        ]
        == "unknown"
    )
    git(root, "add", "decisions/ten.md")
    git(root, "commit", "-qm", "land pair")
    assert (
        next(
            r for r in wi.project(root, date(2026, 9, 22))["items"] if r["id"] == "roadmap:ten-q2"
        )["status"]
        == "done"
    )


def test_missing_conflicting_stale_and_scoped_commit(tmp_path):
    root = fixture(tmp_path)
    assert (
        next(r for r in wi.project(root, date(2027, 1, 1))["items"] if r["id"] == "roadmap:ten-q2")[
            "status"
        ]
        == "unknown"
    )
    (root / "unrelated").write_text("owner draft")
    git(root, "add", "unrelated")
    wi.sync(root)
    assert git(root, "diff", "--cached", "--name-only") == "unrelated"
    assert "unrelated" not in git(root, "show", "--pretty=", "--name-only", "HEAD").splitlines()
    (root / "work_items.yaml").unlink()
    doc = wi.project(root)
    assert not doc["complete"] and any(r["id"] == "repair:registry" for r in doc["items"])


def test_shadow_needs_committed_record_and_named_resolver(tmp_path):
    root = fixture(tmp_path)
    report = "decisions/ten_shadow_build_2026-09-22.md"
    (root / report).write_text("WOULD HOLD for owner basis decision")
    blockers = [
        {
            "id": "basis",
            "resolver": "owner",
            "next_action": "Rule basis",
            "condition": "owner ruling",
            "blocking_decision_ids": ["TEN-basis"],
        }
    ]
    with pytest.raises(subprocess.CalledProcessError):
        wi.record_shadow(report, blockers, root)
    git(root, "add", report)
    git(root, "commit", "-qm", "shadow report")
    wi.record_shadow(report, blockers, root)
    doc = wi.project(root, date(2026, 9, 22))
    r = next(r for r in doc["items"] if r["id"] == "shadow:ten:basis")
    assert r["resolver"] == "owner" and r["blocking_decision_ids"] == ["TEN-basis"]


def test_invalid_registry_status():
    with pytest.raises(ValueError):
        wi.validate({"version": 1, "items": [{"id": "x", "status": "fine"}]})


def test_malformed_registry_is_retained_and_deduplicated_without_stopping_delivery(tmp_path):
    from crude_tanker_fv import delivery

    root = fixture(tmp_path)
    path = root / "work_items.yaml"
    path.write_text("{broken")
    for _ in range(2):
        assert wi.refresh_worker(root)["status"] == "blocked"
    assert path.read_text() == "{broken"
    assert len(delivery.pending(root / "state")) == 1


def test_commit_failure_retries_identical_registry(tmp_path, monkeypatch):
    root = fixture(tmp_path)
    real = wi.commit_paths
    attempts = []

    def fail_once(*args, **kwargs):
        attempts.append(1)
        if len(attempts) == 1:
            raise subprocess.CalledProcessError(1, ["git", "commit"])
        return real(*args, **kwargs)

    monkeypatch.setattr(wi, "commit_paths", fail_once)
    with pytest.raises(subprocess.CalledProcessError):
        wi.sync(root)
    wi.sync(root)
    assert len(attempts) == 2 and git(root, "diff", "--name-only", "--", "work_items.yaml") == ""


def test_unchanged_conditions_quiet_but_recurrence_and_recovery_notify(tmp_path):
    from crude_tanker_fv import delivery

    root = fixture(tmp_path)
    condition = {
        "x": {
            "status": "unknown",
            "resolver": "agent",
            "next_action": "repair",
            "blocking_decision_ids": [],
        }
    }
    for _ in range(2):
        wi.observe_conditions(condition, root)
    assert len(delivery.pending(root / "state")) == 1
    wi.observe_conditions({}, root)
    wi.observe_conditions(condition, root)
    assert len(delivery.pending(root / "state")) == 3
