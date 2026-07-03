"""Cron collision guard (WO1 Task 3): both entrypoints stand down on a dirty
tree or a PAUSE file — automation never runs through live surgery (the
2026-07-02 18:52 price cron fired mid-F-13 fix)."""

import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [ROOT / "scripts" / "price_refresh_cron.sh",
           ROOT / "scripts" / "sentinel_cron.sh"]


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
    return subprocess.run([str(script)], capture_output=True, text=True,
                          env={"CRUDE_TANKER_FV_ROOT": str(repo), "PATH": "/usr/bin:/bin",
                               "HOME": str(repo)})


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda s: s.name)
def test_skips_on_pause_file(tmp_path, script):
    repo = _tmp_repo(tmp_path)
    (repo / "PAUSE").write_text("")
    r = _run(script, repo)
    assert r.returncode == 0
    assert "SKIPPED: paused" in r.stdout


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda s: s.name)
def test_skips_on_dirty_tree(tmp_path, script):
    repo = _tmp_repo(tmp_path)
    (repo / "a.txt").write_text("modified\n")
    r = _run(script, repo)
    assert r.returncode == 0
    assert "SKIPPED: dirty-tree" in r.stdout
