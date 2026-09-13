"""The fork registry as a tool (2026-09-13): executable forks are the open ones past their
window; marking rewrites one status line in place and keeps every comment; opening appends a
block with the window computed in business days (state-tracking executes on its own date)."""

from datetime import date

from crude_tanker_fv import forks

SAMPLE = """# header comment stays
policy:
  silence_business_days: 3
forks:
  - id: alpha
    kind: judgment
    doc: decisions/a.md
    opened: 2026-09-10
    execute_after: 2026-09-15
    recommendation: "do A"
    status: open
  - id: beta        # trailing comment stays
    doc: decisions/b.md
    opened: 2026-09-08
    execute_after: 2026-09-11
    recommendation: "do B"
    status: open
  - id: gamma
    doc: decisions/c.md
    opened: 2026-09-01
    execute_after: 2026-09-04
    recommendation: "done"
    status: executed   # 2026-09-05, commit abc
"""


def test_executable_is_open_and_past_window(tmp_path):
    p = tmp_path / "forks.yaml"
    p.write_text(SAMPLE)
    ids = [f["id"] for f in forks.executable(date(2026, 9, 13), path=p)]
    assert ids == ["beta"]
    ids = [f["id"] for f in forks.executable(date(2026, 9, 15), path=p)]
    assert ids == ["alpha", "beta"]


def test_mark_rewrites_status_in_place_and_keeps_comments(tmp_path):
    p = tmp_path / "forks.yaml"
    p.write_text(SAMPLE)
    forks.mark("beta", "executed", "commit 1234567 — B landed", path=p, today=date(2026, 9, 13))
    t = p.read_text()
    assert "# header comment stays" in t and "# trailing comment stays" in t
    assert "    status: executed   # 2026-09-13 — commit 1234567 — B landed" in t
    assert forks.find("beta", p)["status"] == "executed"
    assert forks.find("alpha", p)["status"] == "open"
    assert forks.find("gamma", p)["status"] == "executed"


def test_open_appends_block_with_business_day_window(tmp_path):
    p = tmp_path / "forks.yaml"
    p.write_text(SAMPLE)
    f = forks.open_fork("buyflip_x_2026-09-11", kind="judgment", doc="decisions/x_log.md",
                        recommendation='land the "flip"', opened=date(2026, 9, 11), path=p)
    assert f["execute_after"] == "2026-09-16"          # Fri + 3 business days = Wed
    assert forks.find("buyflip_x_2026-09-11", p)["recommendation"] == "land the 'flip'"
    f = forks.open_fork("st", kind="state-tracking", doc="d", recommendation="r",
                        opened=date(2026, 9, 11), path=p)
    assert f["execute_after"] == "2026-09-11"
    assert forks.add_business_days(date(2026, 9, 12), 3) == date(2026, 9, 16)   # Sat start
