"""The declared automation graph (2026-09-13): graph.yaml is the machine map, OPERATING.md
carries its render, and `check` refuses the build when the two drift from the code.

    python -m crude_tanker_fv.graph check               # R1-R6 (see graph.yaml header)
    python -m crude_tanker_fv.graph render [--write]    # markdown + mermaid; --write patches OPERATING.md

Edges are derived: a node that writes a path another node reads. Nothing here is hand-drawn.
"""

from __future__ import annotations

import argparse
import fnmatch
import plistlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "graph.yaml"
OPERATING = ROOT / "OPERATING.md"
DRIFT_LIST = ROOT / "scripts" / "drift_files.txt"
LAUNCH_AGENTS = Path.home() / "Library" / "LaunchAgents"
SCHEDULED_TASKS = Path.home() / ".claude" / "scheduled-tasks"
BEGIN, END = "<!-- graph:begin -->", "<!-- graph:end -->"


def load(path: Path = GRAPH_PATH) -> dict:
    return yaml.safe_load(path.read_text())


def _sample(pattern: str) -> str:
    """A concrete path that the pattern matches (for git check-ignore and overlap tests)."""
    return pattern.replace("**", "x/x").replace("*", "x")


def _match(pattern: str, path: str) -> bool:
    return fnmatch.fnmatchcase(path, pattern.replace("**", "*"))


def _overlaps(write: str, read: str) -> bool:
    return _match(read, _sample(write)) or _match(write, _sample(read))


def _repo_path(p: str) -> bool:
    return not p.startswith(("external:", "governance:"))


def drift_paths(path: Path = DRIFT_LIST) -> list[str]:
    if not path.exists():
        return []
    return [ln.strip() for ln in path.read_text().splitlines() if ln.strip() and not ln.startswith("#")]


def _tracked(pattern: str, root: Path) -> bool:
    """True if a path matching the pattern would be tracked (not git-ignored)."""
    r = subprocess.run(["git", "check-ignore", "-q", _sample(pattern)], cwd=root, capture_output=True)
    return r.returncode != 0


def _catch_all(pattern: str) -> bool:
    """`inputs/**`-style reads declare "everything under here"; they make an edge for the
    downstream analysis but would bury the drawing, so the render skips them."""
    return pattern.endswith("/**") and pattern.count("/") == 1


def edges(graph: dict, *, specific_only: bool = False) -> list[tuple[str, str, str]]:
    """(writer, reader, path) for every write pattern some other node reads, plus declared
    triggers. specific_only drops overlaps that exist only through a catch-all read."""
    out = []
    for w in graph["nodes"]:
        for wp in w.get("writes") or []:
            for r in graph["nodes"]:
                if r["id"] == w["id"]:
                    continue
                hits = [rp for rp in (r.get("reads") or []) if _overlaps(wp, rp)]
                if specific_only:
                    hits = [rp for rp in hits if not _catch_all(rp)]
                if hits:
                    out.append((w["id"], r["id"], wp))
    for n in graph["nodes"]:
        for t in n.get("triggers") or []:
            if any(t == m["id"] for m in graph["nodes"]):
                out.append((t, n["id"], "trigger"))
    return sorted(set(out))


def downstream(graph: dict, node_id: str) -> list[str]:
    adj: dict[str, set] = {}
    for a, b, _ in edges(graph):
        adj.setdefault(a, set()).add(b)
    seen, stack = set(), [node_id]
    while stack:
        cur = stack.pop()
        for nxt in adj.get(cur, ()):
            if nxt not in seen and nxt != node_id:
                seen.add(nxt)
                stack.append(nxt)
    return sorted(seen)


def _automation_commits(root: Path, days: int = 30) -> list[tuple[str, str, list[str]]]:
    r = subprocess.run(["git", "log", f"--since={days}.days", "--format=%H%x00%s", "--name-only"],
                       cwd=root, capture_output=True, text=True)
    out, cur = [], None
    for ln in r.stdout.splitlines():
        if "\x00" in ln:
            sha, subj = ln.split("\x00", 1)
            cur = (sha[:7], subj, [])
            out.append(cur)
        elif ln.strip() and cur is not None:
            cur[2].append(ln.strip())
    return out


def check(graph: dict, root: Path = ROOT, *, launch_agents: Path = LAUNCH_AGENTS,
          scheduled_tasks: Path = SCHEDULED_TASKS, drift: list[str] | None = None,
          commits: list[tuple[str, str, list[str]]] | None = None) -> list[str]:
    problems: list[str] = []
    nodes = graph["nodes"]
    ids = [n["id"] for n in nodes]
    by_id = {n["id"]: n for n in nodes}
    kinds = set(graph.get("kinds") or [])
    repo = graph.get("repo", "crude-tanker-fv")

    # R1
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        problems.append(f"R1 duplicate ids: {sorted(dup)}")
    for n in nodes:
        if n.get("kind") not in kinds:
            problems.append(f"R1 {n['id']}: kind {n.get('kind')!r} not in {sorted(kinds)}")
        if n.get("repo") not in (repo, "portfolio-governance", "both"):
            problems.append(f"R1 {n['id']}: repo {n.get('repo')!r} unknown")

    # R2
    for n in nodes:
        for t in n.get("triggers") or []:
            if t != "clock" and t not in by_id and not t.startswith(("email ", "healthchecks")):
                problems.append(f"R2 {n['id']}: trigger {t!r} is not a node id")
        c = n.get("commits")
        if c not in (None, "none", "self") and c not in by_id:
            problems.append(f"R2 {n['id']}: commits {c!r} is not a node id")
    for t in graph.get("tree_drift_only_required_by") or []:
        if t not in by_id:
            problems.append(f"R2 tree_drift_only_required_by names unknown node {t!r}")

    # R3
    drift = drift_paths() if drift is None else drift
    for p in drift:
        if not any(_match(wp, p) or wp == p for n in nodes for wp in (n.get("writes") or []) if _repo_path(wp)):
            problems.append(f"R3 drift-list path {p} has no declared writer")

    # R4
    drift_set = set(drift)
    for n in nodes:
        if n.get("repo") != repo or n.get("kind") == "human":
            continue
        for wp in n.get("writes") or []:
            if not _repo_path(wp) or wp in drift_set or any(_match(d, wp) for d in drift_set):
                continue
            if not _tracked(wp, root):
                continue
            c = n.get("commits")
            if c in (None, "none"):
                problems.append(f"R4 {n['id']} writes tracked non-drift path {wp} and names no committer "
                                f"(an uncommitted write freezes auto-land / holds auto-push / starves price-refresh)")

    # R5
    if launch_agents.exists():
        plists = {p.stem for p in launch_agents.glob("com.crude-tanker-fv.*.plist")}
        declared = {n.get("plist") for n in nodes if n.get("plist")}
        for p in sorted(plists - declared):
            problems.append(f"R5 launchd job {p} has no node")
        for p in sorted(declared - plists):
            problems.append(f"R5 node declares plist {p} which is not installed")
        for n in nodes:
            if n.get("plist") and (launch_agents / f"{n['plist']}.plist").exists():
                d = plistlib.load((launch_agents / f"{n['plist']}.plist").open("rb"))
                args = " ".join(d.get("ProgramArguments") or [])
                if n.get("entry") and n["entry"].split("/")[-1] not in args:
                    problems.append(f"R5 {n['id']}: plist runs {args!r}, node says entry {n['entry']}")
    if scheduled_tasks.exists():
        tasks = {p.name for p in scheduled_tasks.iterdir() if p.is_dir() and p.name.startswith("crude-fv-")}
        declared = {n["id"] for n in nodes if n.get("kind") == "scheduled-task"}
        for t in sorted(tasks - declared):
            problems.append(f"R5 scheduled task {t} has no node")
        for t in sorted(declared - tasks):
            if t.startswith("crude-fv-"):
                problems.append(f"R5 node {t} names a scheduled task that does not exist")

    # R6
    commits = _automation_commits(root) if commits is None else commits
    for n in nodes:
        pref = n.get("commit_subject_prefix")
        if not pref:
            continue
        allowed = list(n.get("writes") or [])
        for m in nodes:
            if m.get("commits") == n["id"]:
                allowed += m.get("writes") or []
        for sha, subj, files in commits:
            if not subj.startswith(pref):
                continue
            for f in files:
                if not any(_match(a, f) or a == f for a in allowed if _repo_path(a)):
                    problems.append(f"R6 commit {sha} ({pref}) touched {f}, not a declared write of {n['id']}")
    return problems


def render(graph: dict) -> str:
    nodes = graph["nodes"]
    lines: list[str] = []
    a = lines.append
    a("Rendered from `graph.yaml` by `python -m crude_tanker_fv.graph render --write`; "
      "`python -m crude_tanker_fv.graph check` and `tests/test_graph.py` keep it honest. Do not edit by hand.")
    a("")
    a("| Node | Kind | Runs | Reads | Writes | Committed by |")
    a("|---|---|---|---|---|---|")
    for n in nodes:
        reads = ", ".join(f"`{p}`" for p in (n.get("reads") or [])[:6]) + (" …" if len(n.get("reads") or []) > 6 else "")
        writes = ", ".join(f"`{p}`" for p in (n.get("writes") or [])[:6]) + (" …" if len(n.get("writes") or []) > 6 else "")
        c = n.get("commits") or "none"
        a(f"| `{n['id']}` | {n['kind']} | {n.get('runs', '')} | {reads or '—'} | {writes or '—'} | {c} |")
    a("")
    a("Shapes: `[[launchd]]` · `[lane]` · `([scheduled task])` · `[/script/]` · `{{human}}` · `((external))`. "
      "Edges are files (labelled) or declared triggers; reads declared as a whole directory "
      "(`inputs/**`) count for the downstream list below but are not drawn.")
    a("")
    a("```mermaid")
    a("flowchart LR")
    shape = {"launchd": ("[[", "]]"), "lane": ("[", "]"), "scheduled-task": ("([", "])"),
             "script": ("[/", "/]"), "human": ("{{", "}}"), "external": ("((", "))")}
    for n in nodes:
        l, r = shape.get(n["kind"], ("[", "]"))
        a(f"  {n['id'].replace('-', '_')}{l}\"{n['id']}\"{r}")
    seen = set()
    for w, r, p in edges(graph, specific_only=True):
        key = (w, r)
        if key in seen:
            continue
        seen.add(key)
        label = p if p == "trigger" else "/".join(Path(p).parts[-2:])
        a(f"  {w.replace('-', '_')} -->|{label}| {r.replace('-', '_')}")
    a("```")
    a("")
    a("**What is downstream of each unattended node** (derived; if it is late or wrong, these are affected):")
    a("")
    for n in nodes:
        if n["kind"] in ("launchd", "scheduled-task", "lane"):
            d = downstream(graph, n["id"])
            a(f"- `{n['id']}` → {', '.join(f'`{x}`' for x in d) if d else 'nothing declared'}")
    req = graph.get("tree_drift_only_required_by") or []
    if req:
        a("")
        a(f"**Nodes that need a drift-only tree** (any uncommitted tracked non-drift write degrades them): "
          + ", ".join(f"`{x}`" for x in req) + ".")
    return "\n".join(lines) + "\n"


def write_operating(text: str, path: Path = OPERATING) -> None:
    doc = path.read_text()
    if BEGIN not in doc or END not in doc:
        raise SystemExit(f"{path} lacks the {BEGIN} / {END} markers")
    head, rest = doc.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    path.write_text(head + BEGIN + "\n" + text + END + tail)


def rendered_block(path: Path = OPERATING) -> str:
    doc = path.read_text()
    if BEGIN not in doc or END not in doc:
        return ""
    return doc.split(BEGIN, 1)[1].split(END, 1)[0].lstrip("\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="the declared automation graph")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    r = sub.add_parser("render")
    r.add_argument("--write", action="store_true", help="patch OPERATING.md between the graph markers")
    args = ap.parse_args(argv)
    g = load()
    if args.cmd == "check":
        probs = check(g)
        for p in probs:
            print(f"GRAPH: {p}")
        print("GRAPH: ok" if not probs else f"GRAPH: {len(probs)} problem(s)")
        return 1 if probs else 0
    text = render(g)
    if args.write:
        write_operating(text)
        print(f"wrote {OPERATING.name} graph block ({len(text)} chars, {len(g['nodes'])} nodes, {len(edges(g))} edges)")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
