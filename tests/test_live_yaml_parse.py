"""Every live YAML under inputs/ must parse (2026-09-02, Stage 0 guard).

The 2026-08-31 archive-gap adjudication was appended to inputs/archive_gaps.yaml
as a root-level list item under a mapping; the file stopped parsing and the
2026-09-01 08:15 sentinel crashed before writing a log line — no digest, no
PAGE, no healthchecks ping — while the heartbeat recorded a normal
`outcome=flags`. No test loaded the live file. This one loads every live
input YAML (drafts excluded: `*.draft` is by definition unpromoted).
"""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LIVE = sorted(p for p in (ROOT / "inputs").rglob("*.yaml")
              if not p.name.endswith(".draft") and "_staged" not in p.parts)


@pytest.mark.parametrize("path", LIVE, ids=[str(p.relative_to(ROOT)) for p in LIVE])
def test_live_yaml_parses(path):
    with path.open() as fh:
        yaml.safe_load(fh)


def test_the_sentinel_inputs_are_covered():
    names = {p.name for p in LIVE}
    for must in ("archive_gaps.yaml", "notify.yaml", "agent_duties.yaml",
                 "reweight_triggers.yaml", "earnings_calendar.yaml",
                 "rocketchat_sources.yaml", "watchlist.yaml"):
        assert must in names, must
