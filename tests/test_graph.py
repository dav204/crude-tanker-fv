"""The declared automation graph (2026-09-13): graph.yaml must describe the installed
automation, every tracked write must name its committer (the Saturday-freeze rule), and the
render in OPERATING.md must be the current render — the human map and the machine map are one
artifact."""

from pathlib import Path

from crude_tanker_fv import graph as g

ROOT = Path(__file__).resolve().parents[1]


def test_real_graph_checks_clean():
    problems = g.check(g.load())
    assert not problems, "\n".join(problems)


def test_operating_md_carries_the_current_render():
    assert g.rendered_block() == g.render(g.load()), \
        "OPERATING.md graph block is stale — run: python -m crude_tanker_fv.graph render --write"


def _mini(**over):
    base = {
        "version": 1, "repo": "crude-tanker-fv",
        "kinds": ["launchd", "lane", "scheduled-task", "script", "human", "external"],
        "nodes": [
            {"id": "writer", "kind": "lane", "repo": "crude-tanker-fv", "triggers": ["clock"],
             "reads": [], "writes": ["outputs/weekly_report_*.md"], "commits": "committer"},
            {"id": "committer", "kind": "lane", "repo": "crude-tanker-fv", "triggers": ["writer"],
             "reads": ["outputs/weekly_report_*.md"], "writes": [], "commits": "self",
             "commit_subject_prefix": "outputs:"},
            {"id": "lander", "kind": "lane", "repo": "crude-tanker-fv", "triggers": ["committer"],
             "reads": ["scripts/drift_files.txt"], "writes": ["baselines/reconcile_baseline.yaml"],
             "commits": "self", "commit_subject_prefix": "baseline:"},
        ],
    }
    base.update(over)
    return base


def test_edges_are_derived_from_writes_and_reads_and_triggers():
    e = g.edges(_mini())
    assert ("writer", "committer", "outputs/weekly_report_*.md") in e
    assert ("writer", "committer", "trigger") in e and ("committer", "lander", "trigger") in e
    assert g.downstream(_mini(), "writer") == ["committer", "lander"]


def test_uncommitted_tracked_write_is_refused(tmp_path):
    """The 2026-09-12 Saturday freeze: a node writing a tracked, non-drift path with no committer."""
    mini = _mini()
    mini["nodes"][0]["commits"] = "none"
    probs = g.check(mini, ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path, drift=[], commits=[])
    assert any(p.startswith("R4 writer writes tracked non-drift path outputs/weekly_report_*.md") for p in probs)
    mini["nodes"][0]["commits"] = "committer"
    assert not g.check(mini, ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path, drift=[], commits=[])


def test_gitignored_and_drift_writes_need_no_committer(tmp_path):
    mini = _mini()
    mini["nodes"][0]["writes"] = ["state/anything.json", "inputs/market_data/prices_daily.yaml"]
    mini["nodes"][0]["commits"] = "none"
    probs = g.check(mini, ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path,
                    drift=["inputs/market_data/prices_daily.yaml"], commits=[])
    assert not probs, probs


def test_drift_list_paths_need_a_declared_writer(tmp_path):
    probs = g.check(_mini(), ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path,
                    drift=["inputs/market_data/prices_daily.yaml"], commits=[])
    assert probs == ["R3 drift-list path inputs/market_data/prices_daily.yaml has no declared writer"]


def test_unknown_references_are_refused(tmp_path):
    mini = _mini()
    mini["nodes"][0]["triggers"] = ["ghost"]
    mini["nodes"][1]["commits"] = "phantom"
    probs = g.check(mini, ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path, drift=[], commits=[])
    assert any("R2 writer: trigger 'ghost'" in p for p in probs)
    assert any("R2 committer: commits 'phantom'" in p for p in probs)


def test_automation_commit_touching_an_undeclared_path_is_refused(tmp_path):
    commits = [("abc1234", "baseline: auto-land — cause", ["baselines/reconcile_baseline.yaml", "PLAN.md"])]
    probs = g.check(_mini(), ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path, drift=[], commits=commits)
    assert probs == ["R6 commit abc1234 (baseline:) touched PLAN.md, not a declared write of lander"]
    commits = [("abc1234", "outputs: weekly report", ["outputs/weekly_report_2026-09-12.md"])]
    assert not g.check(_mini(), ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path, drift=[], commits=commits)


def test_missing_launchd_or_task_node_is_refused(tmp_path):
    (tmp_path / "la").mkdir()
    (tmp_path / "la" / "com.crude-tanker-fv.ghost.plist").write_bytes(
        b'<?xml version="1.0"?><plist version="1.0"><dict><key>ProgramArguments</key><array><string>x</string></array></dict></plist>')
    (tmp_path / "st" / "crude-fv-ghost-task").mkdir(parents=True)
    probs = g.check(_mini(), ROOT, launch_agents=tmp_path / "la", scheduled_tasks=tmp_path / "st", drift=[], commits=[])
    assert "R5 launchd job com.crude-tanker-fv.ghost has no node" in probs
    assert "R5 scheduled task crude-fv-ghost-task has no node" in probs


def _plist(path, hour, minute, script):
    import plistlib
    with open(path, "wb") as fh:
        plistlib.dump({"ProgramArguments": [script], "StartCalendarInterval": {"Hour": hour, "Minute": minute}}, fh)


def test_launchd_clock_shift_is_refused(tmp_path):
    """R7 (2026-09-13): the jobs fire at plist hour + a fixed offset to UTC (+7h observed). A
    reload or DST change moves them all; the check must say so instead of letting the ordering
    assumptions (news task before the sentinel, the drill sums) silently break."""
    mini = _mini(launchd_utc_offset_hours=7)
    mini["nodes"].append({"id": "sentinel", "kind": "launchd", "repo": "crude-tanker-fv",
                          "plist": "com.crude-tanker-fv.sentinel", "entry": "scripts/sentinel_cron.sh",
                          "triggers": ["clock"], "reads": [], "writes": ["state/x.log"], "commits": "none"})
    la = tmp_path / "la"; la.mkdir()
    _plist(la / "com.crude-tanker-fv.sentinel.plist", 8, 15, "/x/scripts/sentinel_cron.sh")
    log = tmp_path / "runs.log"
    log.write_text("2026-09-12T15:15:05Z job=sentinel initiator=com.crude-tanker-fv.sentinel outcome=flags rc=2\n")
    assert not g.check(mini, ROOT, launch_agents=la, scheduled_tasks=tmp_path, drift=[], commits=[], runs_log=log)
    log.write_text("2026-09-13T12:15:05Z job=sentinel initiator=com.crude-tanker-fv.sentinel outcome=flags rc=2\n")
    probs = g.check(mini, ROOT, launch_agents=la, scheduled_tasks=tmp_path, drift=[], commits=[], runs_log=log)
    assert len(probs) == 1 and probs[0].startswith("R7 launchd clock shifted for sentinel: plist hour 08")
    assert "offset 4h, graph expects 7h" in probs[0]


def _launchd_pair(tmp_path):
    mini = _mini(launchd_utc_offset_hours=7)
    la = tmp_path / "la"; la.mkdir()
    for job, hour, minute in (("sentinel", 8, 15), ("price-refresh", 18, 30)):
        mini["nodes"].append({"id": job, "kind": "launchd", "repo": "crude-tanker-fv",
                              "plist": f"com.crude-tanker-fv.{job}", "entry": f"scripts/{job}_cron.sh",
                              "triggers": ["clock"], "reads": [], "writes": ["state/x.log"], "commits": "none"})
        _plist(la / f"com.crude-tanker-fv.{job}.plist", hour, minute, f"/x/scripts/{job}_cron.sh")
    return mini, la


def _r7(mini, la, tmp_path, *lines):
    log = tmp_path / "runs.log"
    log.write_text("".join(ln + "\n" for ln in lines))
    return g.check(mini, ROOT, launch_agents=la, scheduled_tasks=tmp_path, drift=[], commits=[], runs_log=log)


def test_launchd_wake_catch_up_is_not_a_clock_shift(tmp_path):
    """2026-09-15 / 09-17: the Mac hibernated at 1% battery through the 01:30Z price-refresh slot and
    launchd fired it once at the 13:3xZ wake (offset 19h). A slept-through slot moves ONE job; a
    sibling on the expected offset AFTER it says the clock did not shift. Until that sibling runs a
    catch-up and a shift look the same, so the check still fails — and a real shift moves the
    sibling too, so it keeps failing."""
    mini, la = _launchd_pair(tmp_path)
    catch_up = "2026-09-17T13:34:34Z job=price-refresh initiator=com.crude-tanker-fv.price-refresh outcome=ok rc=0"
    probs = _r7(mini, la, tmp_path, catch_up)
    assert len(probs) == 1 and probs[0].startswith("R7 launchd clock shifted for price-refresh: plist hour 18")
    assert "offset 19h, graph expects 7h" in probs[0]
    assert not _r7(mini, la, tmp_path, catch_up,
                   "2026-09-17T15:15:05Z job=sentinel initiator=com.crude-tanker-fv.sentinel outcome=flags rc=2")
    probs = _r7(mini, la, tmp_path, catch_up,
                "2026-09-18T12:15:05Z job=sentinel initiator=com.crude-tanker-fv.sentinel outcome=flags rc=2")
    assert sorted(p.split(":")[0] for p in probs) == ["R7 launchd clock shifted for price-refresh",
                                                       "R7 launchd clock shifted for sentinel"]


def test_manual_runs_say_nothing_about_the_launchd_clock(tmp_path):
    mini, la = _launchd_pair(tmp_path)
    assert not _r7(mini, la, tmp_path,
                   "2026-09-17T15:15:05Z job=sentinel initiator=com.crude-tanker-fv.sentinel outcome=flags rc=2",
                   "2026-09-17T20:00:00Z job=sentinel initiator=manual:dan@ttys001 outcome=ok rc=0 note=bare-run",
                   "2026-09-17T20:05:00Z job=price-refresh initiator=session:mb-batch outcome=ok rc=0")


def test_governor_tasks_are_enumerated_too(tmp_path):
    (tmp_path / "st" / "portfolio-ghost-task").mkdir(parents=True)
    probs = g.check(_mini(), ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path / "st", drift=[], commits=[])
    assert "R5 scheduled task portfolio-ghost-task has no node" in probs
