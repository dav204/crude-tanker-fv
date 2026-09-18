"""Email-only notification channel (WO2 Phase 0.1) — routing partition,
send/record semantics, doctor. All network mocked; the REAL inputs/notify.yaml
is the routing table under test (change-control: every tag lands with a route
entry + a fixture test)."""


from datetime import date

import yaml

from crude_tanker_fv import notify, refresh
from crude_tanker_fv.loaders import INPUTS_DIR

FAKE_ENV = {"CRUDE_FV_SMTP_HOST": "smtp.example.com", "CRUDE_FV_SMTP_USER": "u",
            "CRUDE_FV_SMTP_PASS": "p", "CRUDE_FV_SMTP_TO": "owner@example.com"}


class FakeSMTP:
    sent: list = []
    raise_on_send = False

    def __init__(self, host, port, timeout=None):
        self.host, self.port = host, port

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def starttls(self):
        self.tls = True

    def login(self, user, password):
        self.creds = (user, password)

    def send_message(self, msg):
        if FakeSMTP.raise_on_send:
            raise OSError("connection dropped")
        FakeSMTP.sent.append(msg)


def setup_function(_):
    FakeSMTP.sent = []
    FakeSMTP.raise_on_send = False


# Tags a regex over sentinel.py finds that are NOT flag tags (status words the
# module prints); keep this list honest — an unknown tag PAGES by design.
NOT_TAGS = {"META-DIRTY", "PING-SENT", "PING-SKIPPED", "PING-WITHHELD",
            "PING-FAILED", "FAILED-4XX"}


def live_sentinel_tags() -> set:
    """2026-09-02: derived from the source, not hand-typed — the hand-typed set
    omitted EARNINGS-UNCONFIRMED and EARNINGS-SWEEP-STALE, which paged for six
    weeks through the unknown-tag rule while this test stayed green."""
    import re
    src = (INPUTS_DIR.parent / "src" / "crude_tanker_fv" / "sentinel.py").read_text()
    found = set(re.findall(r'"([A-Z]{3,}(?:-[A-Z0-9]{2,})+)(?=[ :"])', src))
    return found - NOT_TAGS


def test_real_routing_table_covers_every_live_sentinel_tag():
    routes = notify.load_routes(INPUTS_DIR)["routes"]
    routed = (set(routes["page"]) | set(routes.get("page_once", []))
              | set(routes["digest"]) | set(routes.get("record_only", [])))
    live = live_sentinel_tags()
    assert {"TRIGGER-DUE", "FILING-LANDED", "EARNINGS-UNCONFIRMED",
            "EARNINGS-SWEEP-STALE", "REAUTH-NEEDED"} <= live
    assert live <= routed, f"unrouted sentinel tags: {live - routed}"
    lists = [set(routes["page"]), set(routes.get("page_once", [])),
             set(routes["digest"]), set(routes.get("record_only", []))]
    for i, a in enumerate(lists):
        for b in lists[i + 1:]:
            assert not (a & b), f"tags routed two ways: {a & b}"
    # record_only tags are written by other modules (NOTIFY-DOWN by notify.py);
    # the mailed routes must all have a live emitter in sentinel.py.
    mailed = set(routes["page"]) | set(routes.get("page_once", [])) | set(routes["digest"])
    stale = mailed - live
    assert not stale, f"routed tags no sentinel check emits: {stale}"


def test_every_page_class_tag_names_the_owner_action():
    """2026-09-11 (owner ruling): a page means the OWNER's action is needed and the
    line must say what. Every tag routed to page / page_once carries an action
    text; agent-class tags (filings triage, earnings sweeps, static rebases) may
    not sit in a page route at all."""
    routes = notify.load_routes(INPUTS_DIR)["routes"]
    paged = set(routes["page"]) | set(routes.get("page_once", []))
    missing = paged - set(notify.PAGE_ACTIONS)
    assert not missing, f"page-class tags with no owner action text: {missing}"
    agent_class = {"FILING-LANDED", "FILING-UNREADABLE", "STALE-STATIC",
                   "EARNINGS-UNCONFIRMED", "EARNINGS-SWEEP-STALE"}
    assert not (paged & agent_class), paged & agent_class
    assert agent_class <= set(routes["digest"])
    assert notify.page_action("FORK-EXECUTABLE x").startswith("OWNER (optional)")
    assert "no action text registered" in notify.page_action("NEW-TAG thing")


def test_load_env_file_fills_missing_vars_only(tmp_path):
    """2026-09-12: a scheduled-task session has no wrapper to source the secrets file, so the
    module loads it; a variable already in the environment wins; junk lines are ignored."""
    f = tmp_path / "x.env"
    f.write_text('# comment\nexport CRUDE_FV_SMTP_HOST="smtp.example"\nCRUDE_FV_SMTP_USER=u@example\nJUNK LINE\n')
    env = notify.load_env_file(f, environ={"CRUDE_FV_SMTP_USER": "keep"})
    assert env["CRUDE_FV_SMTP_HOST"] == "smtp.example" and env["CRUDE_FV_SMTP_USER"] == "keep"
    assert notify.load_env_file(tmp_path / "missing.env", environ={}) == {}


def test_send_cli_reads_subject_from_first_line_and_stamps_the_owner_header(tmp_path, monkeypatch):
    """2026-09-12: the governor's monitor/notify.sh sends through this CLI. A page carries the
    'YOUR action is needed' header; the subject is the body file's first line; the ledger goes
    to the caller's state dir (the governor keeps its own)."""
    calls = []
    monkeypatch.setattr(notify, "send_email",
                        lambda subject, body, **kw: calls.append((subject, body, kw)) or True)
    monkeypatch.setattr(notify, "load_env_file", lambda *a, **k: {})
    bf = tmp_path / "2026-09-12.md"
    bf.write_text("# SBLK hit its take-profit\n\nSBLK $28.14 > $28 leg.\n  ACTION: OWNER — open a mini-review\n")
    rc = notify.main(["--send", "page", "--body-file", str(bf), "--prefix", "[portfolio]",
                      "--state-dir", str(tmp_path)])
    assert rc == 0
    subject, body, kw = calls[0]
    assert subject == "[portfolio] PAGE: SBLK hit its take-profit"
    assert body.startswith("This page means YOUR action is needed") and "ACTION: OWNER" in body
    assert kw["state_dir"] == tmp_path
    rc = notify.main(["--send", "digest", "--body-file", str(bf), "--prefix", "[portfolio]",
                      "--state-dir", str(tmp_path)])
    assert rc == 0 and calls[1][0] == "[portfolio] digest: SBLK hit its take-profit"
    assert not calls[1][1].startswith("This page")
    assert notify.main(["--send", "page", "--body-file", str(tmp_path / "nope.md")]) == 2


def test_page_once_keys(tmp_path):
    k = notify.page_once_key
    a = k("FILING-LANDED CMBT: 6-K 0000919574-26-005821 filed 2026-08-28 -> inputs/filings/x.htm")
    b = k("FILING-LANDED CMBT: 6-K 0000919574-26-005821 filed 2026-08-29 -> inputs/filings/x.htm")
    assert a == b == "FILING-LANDED CMBT: 6-K 0000919574-26-005821"
    assert k("EARNINGS-UNCONFIRMED CAPT: window opens 2026-09-01 (5d)") == "EARNINGS-UNCONFIRMED CAPT:"
    assert k("EARNINGS-SWEEP-STALE windows open within 21d but the calendar's last_date_sweep is 2026-08-31 (>7d)") \
        == "EARNINGS-SWEEP-STALE 2026-08-31"
    assert k("REAUTH-NEEDED smtp: SMTP auth refused — since 2026-09-02") == "REAUTH-NEEDED smtp:"
    assert k("DIRTY-TOO-LONG tree dirty 40h") == "DIRTY-TOO-LONG"

    # 2026-09-17: the key read a lowercase "due" while refresh emits "DUE {due}", so the
    # date was dropped and the first page's key swallowed every re-arm of a weekly card for
    # 60 days. The flag is BUILT from the production emitter (2026-07-02 rule: two surfaces
    # assumed to agree need a test that they agree), never hand-typed.
    def due_flag(due):
        (tmp_path / "reweight_triggers.yaml").write_text(yaml.safe_dump({
            "crude_geopolitics_weekly": {"sector": "crude+product", "due": due,
                                         "observable": "x", "status": "armed"}}))
        items = [it for it in refresh.check_reweight_triggers(tmp_path, today=date(2026, 10, 1))
                 if it.status == "missing"]
        assert len(items) == 1
        return f"TRIGGER-DUE {items[0].label}: {items[0].detail}"   # sentinel.collect_flags shape

    first, rearmed = due_flag(date(2026, 9, 17)), due_flag(date(2026, 9, 24))
    assert k(first) == "TRIGGER-DUE crude_geopolitics_weekly: 2026-09-17"
    assert k(rearmed) == "TRIGGER-DUE crude_geopolitics_weekly: 2026-09-24"
    assert k(first) != k(rearmed)


def test_route_flags_partition_and_unknown_pages():
    routes = notify.load_routes(INPUTS_DIR)
    flags = ["TRIGGER-DUE t1: overdue",
             "STALE-INPUT spot_tce: 5d",
             "NOTIFY-DOWN send failed",
             "SOME-NEW-TAG nobody routed this"]
    page, digest = notify.route_flags(flags, routes)
    assert page == ["TRIGGER-DUE t1: overdue", "SOME-NEW-TAG nobody routed this"]
    assert digest == ["STALE-INPUT spot_tce: 5d"]


def test_send_email_happy_path_and_ledgers(tmp_path):
    ok = notify.send_email("s", "b", environ=FAKE_ENV, smtp_factory=FakeSMTP,
                           state_dir=tmp_path)
    assert ok and len(FakeSMTP.sent) == 1
    msg = FakeSMTP.sent[0]
    assert msg["To"] == "owner@example.com" and msg["Subject"] == "s"
    # WO2 close: the acceptance compiler joins flags to SENT lines.
    assert "SENT s" in (tmp_path / "notify_sent.log").read_text()


def test_send_unconfigured_records_down_and_returns_false(tmp_path):
    ok = notify.send_email("s", "b", environ={}, smtp_factory=FakeSMTP,
                           state_dir=tmp_path)
    assert not ok and not FakeSMTP.sent
    line = (tmp_path / "notify_down.log").read_text()
    assert "NOTIFY-DOWN unconfigured" in line and "CRUDE_FV_SMTP_HOST" in line


def test_send_failure_records_down_and_returns_false(tmp_path):
    FakeSMTP.raise_on_send = True
    ok = notify.send_email("s", "b", environ=FAKE_ENV, smtp_factory=FakeSMTP,
                           state_dir=tmp_path)
    assert not ok
    assert "NOTIFY-DOWN send failed" in (tmp_path / "notify_down.log").read_text()


def test_doctor_flags_loose_perms_and_missing_env(tmp_path):
    env_file = tmp_path / "crude-tanker-fv.env"
    env_file.write_text("export CRUDE_FV_SMTP_HOST=smtp.example.com\n")
    env_file.chmod(0o644)
    problems = notify.doctor(environ={}, inputs_dir=INPUTS_DIR, env_file=env_file)
    assert any("must be 0o600" in p for p in problems)
    assert any("env missing" in p for p in problems)

    env_file.chmod(0o600)
    assert notify.doctor(environ=FAKE_ENV, inputs_dir=INPUTS_DIR,
                         env_file=env_file) == []
