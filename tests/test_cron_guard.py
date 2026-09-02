"""Cron collision guard (WO1 Task 3): both entrypoints stand down on a dirty
tree or a PAUSE file — automation never runs through live surgery (the
2026-07-02 18:52 price cron fired mid-F-13 fix)."""

import re
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
    drift_file = "inputs/market_data/transactions/_scan_state.json"
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


# --- Multi-lane wrappers: one outcome word, three venues (2026-08-16) --------
# edgar_poll_cron.sh runs THREE venue adapters (SEC / HKEX / Oslo) on one row,
# so a single `outcome=error` cannot say which lane died. Caught live: mfn.se
# threw URLError, `set -e` killed the wrapper before CRON_OUTCOME was set, and
# the sentinel flagged a bare `outcome=error rc=1 note=` while EDGAR and HKEX
# had both already succeeded — red-on-a-sibling masking a healthy lane, the
# inverse of the 2026-07-18 camouflage rule. Text-level, like test_plists:
# green on a clean clone, and it fails the day a fourth adapter is appended as
# a bare line.
MULTI_LANE = ROOT / "scripts" / "edgar_poll_cron.sh"


def test_every_venue_adapter_runs_through_a_named_lane():
    """No adapter may be invoked bare — a bare line aborts the wrapper under
    `set -e` and takes the sibling lanes' outcome with it."""
    text = MULTI_LANE.read_text()
    bare = [ln.strip() for ln in text.splitlines()
            if re.match(r"^\s*\./\.venv/bin/python -m crude_tanker_fv\.\w*_poll\b", ln)]
    assert not bare, f"adapter(s) invoked outside cron_lane: {bare}"
    lanes = re.findall(r"^\s*cron_lane\s+(\w+)\s+\./\.venv/bin/python -m crude_tanker_fv\.(\w+)",
                       text, re.M)
    assert {m for _, m in lanes} == {"edgar_poll", "hkex_poll", "newsweb_poll"}, lanes


def test_multi_lane_outcome_names_the_failing_lane():
    """The wrapper must record per-lane status in CRON_NOTE and still report
    `error` when any lane fails — visible AND attributable. A `|| true` that
    merely silenced the failure would make a persistent outage look like a
    quiet week, which is the silent-watchdog failure this repo has been bitten
    by; assert the loud half too."""
    text = MULTI_LANE.read_text()
    # CODE only — the wrapper's comments discuss `|| true` precisely to explain
    # why it is not used, and a naive substring check reads that as the bug.
    code = "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith("#"))
    assert "CRON_NOTE=" in code and "CRON_LANE_FAILED" in code
    assert "CRON_OUTCOME=error" in code, "a failing lane must still surface as error"
    assert "|| true" not in code, "lane failures must not be swallowed"
    # `cmd || var=$?` is the only set -e-safe form that preserves the real rc;
    # `if cmd; then` records every failure as rc0 (the bug this was written with).
    assert '"$@" || cron_lane_rc=$?' in text


def _cmd_line_index(text: str, needle: str) -> int:
    """Index of the first NON-comment line invoking `needle` (comments and the
    chain header mention modules by name; only a command counts)."""
    pos = 0
    for line in text.splitlines(keepends=True):
        if not line.lstrip().startswith("#") and needle in line:
            return pos
        pos += len(line)
    raise AssertionError(f"no command line runs {needle}")


@pytest.mark.parametrize("script", ["ingest_rocketchat_cron.sh", "news_pull_cron.sh"])
def test_ingest_chains_rebuild_manifest_before_scan(script):
    """2026-09-02 (Stage 0): sp_scan reads _manifest.json, so both chains must
    index before they scan — the daily chain never did (9/01 false clean) and
    the Saturday chain did it after."""
    text = (ROOT / "scripts" / script).read_text()
    assert (_cmd_line_index(text, "crude_tanker_fv.pareto_archive --build-manifest")
            < _cmd_line_index(text, "crude_tanker_fv.sp_scan"))
