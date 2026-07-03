"""Committed launchd plists stay coherent with themselves and the inventory.

WO2 pre-work 0.0 (2026-07-03). The sentinel plist shipped as a copy-paste of
price-refresh — wrong log paths (two jobs interleaving one file) and an 18:30
NYSE comment over an 08:15 schedule (D-1); the RC-ingest job ran for weeks with
no committed plist at all (D-4). The one-time machine sweep lives in
decisions/launchagents_reconciliation_2026-07-03.md; these guards keep the
known failure classes from recurring. Text-level only — green on a clean clone.
"""

import plistlib
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLISTS = sorted((ROOT / "scripts").glob("*.plist"))
RECON = ROOT / "decisions" / "launchagents_reconciliation_2026-07-03.md"


def _load(path):
    return plistlib.loads(path.read_bytes())


def test_label_matches_filename():
    for path in PLISTS:
        assert _load(path)["Label"] == path.stem, path.name


def test_log_paths_unique_and_job_named():
    """D-1 class: no two jobs may share a log file, and a job's logs carry its
    own name — a copy-pasted StandardOutPath is exactly what this catches."""
    seen = {}
    for path in PLISTS:
        doc = _load(path)
        for key in ("StandardOutPath", "StandardErrorPath"):
            log = doc[key]
            assert log not in seen, f"{path.name} shares {log} with {seen[log]}"
            seen[log] = path.name


def test_comment_states_the_actual_schedule():
    """D-1 class: the human-facing schedule comment must contain the HH:MM the
    StartCalendarInterval actually encodes (the sentinel plist said 18:30 and
    fired at 08:15)."""
    for path in PLISTS:
        cal = _load(path)["StartCalendarInterval"]
        hhmm = f"{cal['Hour']:02d}:{cal['Minute']:02d}"
        comments = " ".join(re.findall(r"<!--(.*?)-->", path.read_text(), re.S))
        assert hhmm in comments, f"{path.name}: comment omits schedule {hhmm}"


def test_wrapper_exists_and_committed():
    for path in PLISTS:
        wrapper = Path(_load(path)["ProgramArguments"][0])
        assert (ROOT / "scripts" / wrapper.name).exists(), (
            f"{path.name} points at uncommitted wrapper {wrapper.name}")


def test_committed_set_matches_documented_inventory():
    """D-4 class: every job the reconciliation record says is committed exists
    in scripts/, and nothing ships uninventoried — a new plist and the
    inventory block move in the same commit."""
    block = re.search(r"```yaml\n(.*?)```", RECON.read_text(), re.S).group(1)
    jobs = yaml.safe_load(block)["jobs"]
    documented = {name for name, j in jobs.items() if j["plist_committed"]}
    committed = {p.stem for p in PLISTS}
    assert committed == documented, (
        f"scripts/*.plist vs inventory: only-committed={committed - documented} "
        f"only-documented={documented - committed}")
