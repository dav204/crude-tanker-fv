"""Cron collision guard (WO1 Task 3): both entrypoints stand down on a dirty
tree or a PAUSE file — automation never runs through live surgery (the
2026-07-02 18:52 price cron fired mid-F-13 fix)."""

import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
# All four cron wrappers carry the PAUSE guard (WO2 1.1 added the two
# staging-only fetchers); job name = heartbeat filename.
JOBS = {"price_refresh_cron.sh": "price-refresh",
        "sentinel_cron.sh": "sentinel",
        "ingest_rocketchat_cron.sh": "rocketchat-ingest",
        "news_pull_cron.sh": "news-pull",
        "harvester_cron.sh": "harvester"}
SCRIPTS = [ROOT / "scripts" / name for name in sorted(JOBS)]


def _tmp_repo(tmp_path: Path) -> Path:
    """A clean throwaway git repo the cron scripts can point at."""
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    (repo / "a.txt").write_text("x\n")
    subprocess.run(["git", "add", "a.txt"], cwd=repo, check=True)
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t",
                    "commit", "-qm", "init"], cwd=repo, check=True)
    return repo


def _run(script: Path, repo: Path) -> subprocess.CompletedProcess:
    # XPC_SERVICE_NAME=0 mimics an interactive macOS shell — the ledger must
    # still stamp these manual (only com.crude-tanker-fv.* labels are launchd).
    return subprocess.run([str(script)], capture_output=True, text=True,
                          env={"CRUDE_TANKER_FV_ROOT": str(repo), "PATH": "/usr/bin:/bin",
                               "HOME": str(repo), "XPC_SERVICE_NAME": "0"})


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda s: s.name)
def test_skips_on_pause_file(tmp_path, script):
    repo = _tmp_repo(tmp_path)
    (repo / "PAUSE").write_text("")
    r = _run(script, repo)
    assert r.returncode == 0
    assert "SKIPPED: paused" in r.stdout
    # WO2 0.2 (invariant 1): a SKIP still heartbeats — a standing-down job is
    # alive; only silence is death. Ledger line carries the manual initiator.
    job = JOBS[script.name]
    hb = (repo / "state" / "heartbeat" / job).read_text()
    assert f"job={job}" in hb and "outcome=skipped-paused" in hb
    ledger = (repo / "state" / "automation_runs.log").read_text()
    assert "initiator=manual:" in ledger and f"job={job}" in ledger


# Dirty-tree: price-refresh only. The sentinel deliberately does NOT skip on a
# dirty tree (WO2 0.3, invariant 3) — it runs in META-MODE inside python
# (content checks suspended, digest/ping alive, DIRTY-TOO-LONG at 36h/12h);
# covered in tests/test_sentinel.py.
@pytest.mark.parametrize("script", [s for s in SCRIPTS if "price" in s.name],
                         ids=lambda s: s.name)
def test_skips_on_dirty_tree(tmp_path, script):
    repo = _tmp_repo(tmp_path)
    (repo / "a.txt").write_text("modified\n")
    r = _run(script, repo)
    assert r.returncode == 0
    assert "SKIPPED: dirty-tree" in r.stdout and "a.txt" in r.stdout
    hb = (repo / "state" / "heartbeat" / "price-refresh").read_text()
    assert "outcome=skipped-dirty" in hb and "non_drift=a.txt" in hb


@pytest.mark.parametrize("script", [s for s in SCRIPTS if "price" in s.name],
                         ids=lambda s: s.name)
def test_drift_only_dirt_does_not_skip(tmp_path, script):
    """Guard re-scope (2026-07-06): the daily RC ingest dirties tracked drift
    files every morning — that starved the price fetch two nights running.
    Dirt confined to scripts/drift_files.txt passes the guard (the run then
    fails on the tmp repo's missing venv, which PROVES it got past the skip);
    drift + surgery together still skips."""
    repo = _tmp_repo(tmp_path)
    drift_file = "inputs/market_data/baltic_indexes_daily.csv"
    (repo / drift_file).parent.mkdir(parents=True)
    (repo / drift_file).write_text("date,BDI\n")
    subprocess.run(["git", "add", drift_file], cwd=repo, check=True)
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t",
                    "commit", "-qm", "seed"], cwd=repo, check=True)
    (repo / drift_file).write_text("date,BDI\n2026-07-06,2500\n")

    r = _run(script, repo)
    assert "SKIPPED: dirty-tree" not in r.stdout
    assert r.returncode != 0   # proceeded to the (absent) venv — guard passed
    hb = (repo / "state" / "heartbeat" / "price-refresh").read_text()
    assert "outcome=error" in hb   # the trap still recorded the real failure

    (repo / "a.txt").write_text("surgery\n")
    r = _run(script, repo)
    assert r.returncode == 0 and "SKIPPED: dirty-tree (a.txt)" in r.stdout
