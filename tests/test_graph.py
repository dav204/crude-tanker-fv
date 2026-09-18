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


def _launchd_pair(tmp_path):
    mini = _mini(launchd_utc_offset_hours=7)
    la = tmp_path / "la"; la.mkdir()
    for job, hour, minute in (("sentinel", 8, 15), ("price-refresh", 18, 30)):
        mini["nodes"].append({"id": job, "kind": "launchd", "repo": "crude-tanker-fv",
                              "plist": f"com.crude-tanker-fv.{job}", "entry": f"scripts/{job}_cron.sh",
                              "triggers": ["clock"], "reads": [], "writes": ["state/x.log"], "commits": "none"})
        _plist(la / f"com.crude-tanker-fv.{job}.plist", hour, minute, f"/x/scripts/{job}_cron.sh")
    return mini, la


def _r7(mini, la, tmp_path, *lines, notes=None):
    log = tmp_path / "runs.log"
    log.write_text("".join(ln + "\n" for ln in lines))
    return g.check(mini, ROOT, launch_agents=la, scheduled_tasks=tmp_path, drift=[], commits=[],
                   runs_log=log, notes=notes)


def _run(job, stamp):
    return f"{stamp} job={job} initiator=com.crude-tanker-fv.{job} outcome=ok rc=0"


def test_launchd_clock_shift_is_refused(tmp_path):
    """R7: a job off its slot is a NOTE until an hour-bearing sibling runs; the first sibling to
    run decides — off by the SAME offset = the clock shifted (2026-09-18: the indeterminate case
    used to red the suite the fork executor gates on, so a Mac nap halted forks)."""
    mini, la = _launchd_pair(tmp_path)
    assert not _r7(mini, la, tmp_path, _run("sentinel", "2026-09-12T15:15:05Z"))
    notes = []
    assert not _r7(mini, la, tmp_path, _run("sentinel", "2026-09-13T12:15:05Z"), notes=notes)
    assert len(notes) == 1 and notes[0].startswith("R7 sentinel ran off its slot") and "offset 4h" in notes[0]
    probs = _r7(mini, la, tmp_path, _run("sentinel", "2026-09-13T12:15:05Z"),
                _run("price-refresh", "2026-09-13T22:30:03Z"))          # 22 - 18 = 4h too
    assert len(probs) == 1 and probs[0].startswith("R7 launchd clock shifted for sentinel: plist hour 08")
    assert "offset 4h, graph expects 7h" in probs[0]


def test_launchd_wake_catch_up_is_not_a_clock_shift(tmp_path):
    """2026-09-15 / 09-17: the Mac hibernated through the 01:30Z price-refresh slot and launchd
    fired it once at the 13:3xZ wake (offset 19h). Alone it is a note; a sibling on its slot
    afterwards clears it; a shift is confirmed only by a sibling off by the same offset."""
    mini, la = _launchd_pair(tmp_path)
    catch_up = _run("price-refresh", "2026-09-17T13:34:34Z")
    notes = []
    assert not _r7(mini, la, tmp_path, catch_up, notes=notes)
    assert len(notes) == 1 and "no hour-bearing job has run since" in notes[0]
    notes = []
    assert not _r7(mini, la, tmp_path, catch_up, _run("sentinel", "2026-09-17T15:15:05Z"), notes=notes)
    assert len(notes) == 1 and "cleared by sentinel" in notes[0] and "on its slot" in notes[0]
    shifted = _run("sentinel", "2026-09-18T12:15:05Z")                  # offset 4h: not 19h
    notes = []
    assert not _r7(mini, la, tmp_path, catch_up, shifted, notes=notes) and len(notes) == 2
    probs = _r7(mini, la, tmp_path, catch_up, shifted, _run("price-refresh", "2026-09-18T22:30:03Z"))
    assert [p.split(":")[0] for p in probs] == ["R7 launchd clock shifted for sentinel"]


def test_two_naps_in_one_day_are_not_a_shift(tmp_path):
    """A second nap fires the next slept-through slot at a different offset; a shift moves every
    job by the SAME offset. Two off-slot runs with different offsets are two notes."""
    mini, la = _launchd_pair(tmp_path)
    notes = []
    assert not _r7(mini, la, tmp_path, _run("price-refresh", "2026-09-19T13:30:10Z"),   # 19h
                   _run("sentinel", "2026-09-19T18:02:00Z"), notes=notes)                # 10h
    assert len(notes) == 2 and "another nap" in notes[0]


def test_wake_cluster_is_not_a_clock_shift(tmp_path):
    """2026-08-29 / 09-07 / 09-10: every slept-through slot fired within seconds of the wake. Runs
    inside the wake window are one event, not siblings of each other: notes, not failures; the
    next scheduled slot on time clears them all."""
    mini, la = _launchd_pair(tmp_path)
    cluster = (_run("price-refresh", "2026-09-07T13:07:42Z"), _run("sentinel", "2026-09-07T13:07:44Z"))
    notes = []
    assert not _r7(mini, la, tmp_path, *cluster, notes=notes)
    assert len(notes) == 2
    assert not _r7(mini, la, tmp_path, *cluster, _run("price-refresh", "2026-09-08T01:30:02Z"))


def test_first_sibling_after_the_wake_decides_not_the_last(tmp_path):
    """A Saturday catch-up cleared by the next on-slot run must stay cleared when a later nap
    cluster lands at the same offset (2026-09-10: news-pull/harvester were read as shifted)."""
    mini, la = _launchd_pair(tmp_path)
    notes = []
    probs = _r7(mini, la, tmp_path, _run("price-refresh", "2026-09-07T13:07:42Z"),   # 19h catch-up
                _run("sentinel", "2026-09-07T15:15:05Z"),                            # on slot: clears it
                _run("sentinel", "2026-09-10T03:15:00Z"), notes=notes)               # 19h again, a new nap
    assert not probs
    assert [n.split(" ")[1] for n in notes] == ["sentinel", "price-refresh"] or \
           [n.split(" ")[1] for n in notes] == ["price-refresh", "sentinel"]
    assert any("cleared by sentinel at 2026-09-07T15:15Z, on its slot" in n for n in notes)


def test_late_start_is_still_on_slot_within_the_observed_slack(tmp_path):
    """On-slot launchd starts run up to 16 minutes late in the live log (ingest 14:14:48Z for a
    14:00 slot on 2026-09-16), so a start inside R7_START_SLACK_MIN is clock evidence; one far
    outside it (a wake catch-up that happened to land in the expected hour) is not."""
    mini, la = _launchd_pair(tmp_path)
    shifted = _run("price-refresh", "2026-09-16T22:30:03Z")                     # 4h
    assert not _r7(mini, la, tmp_path, shifted, _run("sentinel", "2026-09-17T15:29:10Z"))   # 14 min late: on slot
    notes = []
    assert not _r7(mini, la, tmp_path, shifted, _run("sentinel", "2026-09-17T15:41:00Z"), notes=notes)
    assert len(notes) == 2 and any("another nap" in n for n in notes)          # 7h vs 4h: not the same offset


def test_graph_check_cli_prints_notes_and_stays_green(monkeypatch, capsys):
    monkeypatch.setattr(g, "load", lambda: {})
    monkeypatch.setattr(g, "check", lambda graph, notes=None, **kw: (notes.append("R7 x ran off its slot"), [])[1])
    assert g.main(["check"]) == 0
    out = capsys.readouterr().out
    assert "GRAPH: note R7 x ran off its slot" in out and out.rstrip().endswith("GRAPH: ok")


def test_manual_runs_say_nothing_about_the_launchd_clock(tmp_path):
    mini, la = _launchd_pair(tmp_path)
    assert not _r7(mini, la, tmp_path,
                   "2026-09-17T15:15:05Z job=sentinel initiator=com.crude-tanker-fv.sentinel outcome=flags rc=2",
                   "2026-09-17T20:00:00Z job=sentinel initiator=manual:dan@ttys001 outcome=ok rc=0 note=bare-run",
                   "2026-09-17T20:05:00Z job=price-refresh initiator=session:mb-batch outcome=ok rc=0")


def test_planned_task_is_tolerated_until_installed_then_must_drop_the_flag(tmp_path):
    """A declared scheduled-task node the owner has not installed yet carries planned: true (R5 is
    quiet); once the task folder exists the flag must go, or R5 says so (2026-09-18)."""
    mini = _mini()
    mini["nodes"].append({"id": "crude-fv-x", "kind": "scheduled-task", "repo": "crude-tanker-fv", "planned": True,
                          "triggers": ["clock"], "reads": [], "writes": [], "commits": "none"})
    st = tmp_path / "st"; st.mkdir()
    assert not g.check(mini, ROOT, launch_agents=tmp_path, scheduled_tasks=st, drift=[], commits=[])
    (st / "crude-fv-x").mkdir()
    probs = g.check(mini, ROOT, launch_agents=tmp_path, scheduled_tasks=st, drift=[], commits=[])
    assert probs == ["R5 node crude-fv-x is marked planned but its scheduled task exists — drop planned: true"]
    del mini["nodes"][-1]["planned"]
    assert not g.check(mini, ROOT, launch_agents=tmp_path, scheduled_tasks=st, drift=[], commits=[])


def test_governor_tasks_are_enumerated_too(tmp_path):
    (tmp_path / "st" / "portfolio-ghost-task").mkdir(parents=True)
    probs = g.check(_mini(), ROOT, launch_agents=tmp_path, scheduled_tasks=tmp_path / "st", drift=[], commits=[])
    assert "R5 scheduled task portfolio-ghost-task has no node" in probs
