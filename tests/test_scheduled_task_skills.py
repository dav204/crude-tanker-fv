"""The tracked scheduled-task skills (scripts/scheduled_tasks/*.SKILL.md) are the source the owner
installs from; each must name a declared graph node and, when the node commits under a subject
prefix (R6), tell the task to commit under exactly that prefix (2026-09-18)."""

import re
from pathlib import Path

from crude_tanker_fv import graph as g

ROOT = Path(__file__).resolve().parents[1]


def _frontmatter(text: str) -> dict:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert m, "no frontmatter"
    return dict(ln.split(":", 1) for ln in m.group(1).splitlines() if ":" in ln)


def test_tracked_skills_match_their_graph_nodes():
    nodes = {n["id"]: n for n in g.load()["nodes"]}
    skills = sorted((ROOT / "scripts" / "scheduled_tasks").glob("*.SKILL.md"))
    assert skills
    for path in skills:
        task = path.name[: -len(".SKILL.md")]
        fm = _frontmatter(path.read_text())
        assert fm.get("name", "").strip() == task, f"{path.name}: frontmatter name != file name"
        assert fm.get("description", "").strip() and fm.get("allowed-tools", "").strip(), f"{path.name}: description/allowed-tools"
        assert task in nodes and nodes[task]["kind"] == "scheduled-task", f"{task}: no scheduled-task node in graph.yaml"
        prefix = nodes[task].get("commit_subject_prefix")
        if prefix:
            body = path.read_text()
            assert re.search(r'git commit -m "' + re.escape(prefix), body), \
                f"{task}: the skill must commit with a subject starting {prefix!r} (R6 matches on it)"
