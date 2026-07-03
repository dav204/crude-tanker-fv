"""Read-only cron sentinel (WO1 Task 2) — one manufactured flag per class,
stable routing tags, exit codes, and the spec log format."""

import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

from crude_tanker_fv.sentinel import collect_flags, main

# Check 5 (NOTIFY-UNCONFIGURED) reads the environ — configured here so the
# content-check tests stay isolated from the machine's real env.
FAKE_ENV = {"CRUDE_FV_SMTP_HOST": "smtp.example.com", "CRUDE_FV_SMTP_USER": "u",
            "CRUDE_FV_SMTP_PASS": "p", "CRUDE_FV_SMTP_TO": "owner@example.com"}


def _fixture(tmp_path: Path, *, trigger_due=False, stale_watchlist=False,
             incoherent=False, static_fallback=False, fresh_prices=True,
             sidecar_stale=False):
    from crude_tanker_fv.scorecard import scenario_inputs_sha

    inputs = tmp_path / "inputs"
    outputs = tmp_path / "outputs"
    (inputs / "market_data").mkdir(parents=True)
    outputs.mkdir()
    (inputs / "scenario_inputs.yaml").write_text("sectors: {}\n")
    sha = "000badc0ffee" if sidecar_stale else scenario_inputs_sha(inputs)
    (outputs / "weight_robustness.yaml").write_text(yaml.safe_dump({
        "computed_against": {"crude": sha},
        "weight_sets": {"crude": {}},
        "names": {"DHT": {"ev_sign_stable": True, "ev_min_pct": 8.0, "ev_max_pct": 20.0}},
    }))
    (inputs / "reweight_triggers.yaml").write_text(yaml.safe_dump({
        "t1": {"sector": "crude", "due": date(2026, 6, 1) if trigger_due else date(2099, 1, 1),
               "observable": "x", "action": "y", "status": "armed", "added": date(2026, 7, 2)},
    }))
    as_of = (date.today() - timedelta(days=40)).isoformat() if stale_watchlist \
        else date.today().isoformat()
    (inputs / "watchlist.yaml").write_text(yaml.safe_dump({
        "DHT": {"current_price": 16.5, "analyst_target": 18.0, "as_of": as_of},
    }))
    fetched = (datetime.now(timezone.utc) - timedelta(days=0 if fresh_prices else 5))
    (inputs / "market_data" / "prices_daily.yaml").write_text(yaml.safe_dump({
        "fetched_at": fetched.isoformat(timespec="seconds"),
        "prices": {"DHT": {"price": 16.5, "asof": fetched.isoformat(timespec="seconds")}},
    }))
    for f in ("vessel_value_curves.yaml", "spot_tce.yaml", "twelve_month_tc.yaml",
              "historical_tce_means.yaml", "ffa_forward_curve.yaml"):
        (inputs / "market_data" / f).write_text("{}\n")
    pb = {"total": 1, "static_fallback": {}, "oldest_static_as_of": None,
          "market_event_review": {}}
    if static_fallback:
        pb["static_fallback"] = {"DHT": {"as_of": "2026-06-04", "reason": "day move -17.2%"}}
    (outputs / "book_scorecard.json").write_text(json.dumps({
        "schema_version": "2.1",
        "price_basis": pb,
        "names": [{"ticker": "DHT", "void": False, "ev_pct": 12.0, "fv": 18.0,
                   "position": "TRIM/SHORT (overvalued)" if incoherent
                   else "BUY (undervalued)"}],
    }))
    # Matching scenario doc so the fv-identity scan has its counterpart surface.
    (outputs / "dht_scenarios.md").write_text(
        "- **Probability-weighted fair value:** $18.00 (+9.1% vs price)\n")
    # Routing table for main(--notify) paths.
    (inputs / "notify.yaml").write_text(yaml.safe_dump({
        "subject_prefix": "[crude-fv]",
        "routes": {"page": ["TRIGGER-DUE"], "digest": ["STALE-INPUT", "FETCH-FAILED"],
                   "record_only": ["NOTIFY-DOWN"]}}))
    return inputs, outputs


def _write_plist(scripts: Path, label: str, weekly=False):
    import plistlib

    cal = {"Hour": 8, "Minute": 0}
    if weekly:
        cal["Weekday"] = 6
    (scripts / f"{label}.plist").write_bytes(plistlib.dumps({
        "Label": label, "ProgramArguments": ["/x.sh"], "StartCalendarInterval": cal,
        "StandardOutPath": "/tmp/x.log", "StandardErrorPath": "/tmp/x.err"}))


def test_quiet_when_clean(tmp_path):
    inputs, outputs = _fixture(tmp_path)
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []


def test_one_flag_per_class_with_stable_tags(tmp_path):
    inputs, outputs = _fixture(tmp_path, trigger_due=True, stale_watchlist=True,
                               incoherent=True, static_fallback=True, sidecar_stale=True)
    flags = collect_flags(inputs, outputs, environ={})
    tags = {f.split()[0] for f in flags}
    assert tags == {"TRIGGER-DUE", "STALE-INPUT", "SURFACE-INCOHERENT",
                    "PRICE-BASIS", "SIDECAR-STALE", "NOTIFY-UNCONFIGURED"}


def test_notify_unconfigured_flag_alone(tmp_path):
    """WO2 0.1: an otherwise-clean tree with no SMTP env pages nowhere — the
    sentinel nags until ~/.config/crude-tanker-fv.env carries the creds."""
    inputs, outputs = _fixture(tmp_path)
    flags = collect_flags(inputs, outputs, environ={})
    assert len(flags) == 1 and flags[0].startswith("NOTIFY-UNCONFIGURED")
    assert "CRUDE_FV_SMTP_HOST" in flags[0]


def test_sidecar_stale_flag_alone(tmp_path):
    """WO1-F4: a fragility sidecar lagging scenario_inputs.yaml pages on its
    own — the mechanism behind the Jul-2 ⚠-list churn (field lagged engine)."""
    inputs, outputs = _fixture(tmp_path, sidecar_stale=True)
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and flags[0].startswith("SIDECAR-STALE")
    assert "crude" in flags[0]


def test_fv_identity_scan_catches_surface_divergence(tmp_path):
    inputs, outputs = _fixture(tmp_path)
    (outputs / "dht_scenarios.md").write_text(
        "- **Probability-weighted fair value:** $9.27 (+79.0% vs price)\n")
    flags = collect_flags(inputs, outputs)
    assert any(f.startswith("SURFACE-INCOHERENT DHT: JSON fv") for f in flags)


def test_fetch_failed_from_heartbeats(tmp_path):
    """WO2 0.2 (invariant 1): job health reads ONLY heartbeats — missing,
    stale-past-cadence, and outcome=error each flag; a fresh ok/skip is quiet."""
    import os
    import time

    inputs, outputs = _fixture(tmp_path)
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    _write_plist(scripts, "com.crude-tanker-fv.price-refresh")

    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and "FETCH-FAILED price-refresh: no heartbeat" in flags[0]

    hb_dir = tmp_path / "state" / "heartbeat"
    hb_dir.mkdir(parents=True)
    hb = hb_dir / "price-refresh"
    hb.write_text("ts=x job=price-refresh outcome=ok rc=0 note=\n")
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []

    hb.write_text("ts=x job=price-refresh outcome=skipped-dirty rc=0 note=\n")
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []   # a skip is alive

    hb.write_text("ts=x job=price-refresh outcome=error rc=2 note=\n")
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and "last run errored" in flags[0]

    hb.write_text("ts=x job=price-refresh outcome=ok rc=0 note=\n")
    old = time.time() - 3 * 86400
    os.utime(hb, (old, old))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and "heartbeat 3d old" in flags[0]

    # Weekly cadence tolerates a 3d-old heartbeat (9d limit).
    _write_plist(scripts, "com.crude-tanker-fv.news-pull", weekly=True)
    (hb_dir / "news-pull").write_text("ts=x job=news-pull outcome=ok rc=0 note=\n")
    os.utime(hb_dir / "news-pull", (old, old))
    hb.touch()
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []


def _notify_harness(tmp_path, monkeypatch, sends_succeed=True, **fixture_kw):
    """Common main(--notify) setup: FAKE env, stubbed send_email, tmp state."""
    import crude_tanker_fv.notify as notify
    import crude_tanker_fv.sentinel as s

    for k, v in FAKE_ENV.items():
        monkeypatch.setenv(k, v)
    monkeypatch.setenv("CRUDE_FV_HEALTHCHECK_URL", "https://hc.example/ping")
    inputs, outputs = _fixture(tmp_path, **fixture_kw)
    monkeypatch.setattr(s, "INPUTS_DIR", inputs)
    monkeypatch.setattr(s, "OUTPUTS_DIR", outputs)
    sent = []
    monkeypatch.setattr(notify, "send_email", lambda subj, body, **kw:
                        sent.append((subj, body)) or sends_succeed)
    pings = []
    monkeypatch.setattr(s, "_urlopen", lambda url, timeout=None: pings.append(url))
    return s, inputs, outputs, sent, pings, str(tmp_path / "st.json")


def test_notify_pages_and_ping_withholds_on_send_failure(tmp_path, monkeypatch, capsys):
    """Invariant 2: PAGE flags email via notify; a failed send withholds the
    dead-man ping (healthchecks pages by absence)."""
    s, *_, sent, pings, st = _notify_harness(tmp_path, monkeypatch,
                                             sends_succeed=False, trigger_due=True)
    assert s.main(["--notify", "--ping", "--state", st]) == 1
    assert "PAGE: 1 flag(s)" in sent[0][0] and "TRIGGER-DUE" in sent[0][1]
    assert len(sent) == 2   # page + the unconditional digest
    assert not pings
    assert "PING-WITHHELD" in capsys.readouterr().out


def test_ping_fires_on_quiet_run_with_ok_digest(tmp_path, monkeypatch, capsys):
    """0.3: the digest goes out on an OK day too — the unconditional send is
    what makes notifier death detectable — and the ping follows it."""
    s, *_, sent, pings, st = _notify_harness(tmp_path, monkeypatch)
    assert s.main(["--notify", "--ping", "--state", st]) == 0
    assert len(sent) == 1 and "daily digest — OK" in sent[0][0]
    assert "All checks quiet." in sent[0][1]
    assert pings == ["https://hc.example/ping"]
    assert "PING-SENT" in capsys.readouterr().out


def test_dark_period_prefix_after_gap(tmp_path, monkeypatch):
    """0.3: first digest after a >48h gap says DARK <n> days — accumulated:."""
    import json as _json

    s, *_, sent, pings, st = _notify_harness(tmp_path, monkeypatch)
    assert s.main(["--notify", "--state", st]) == 0
    doc = _json.loads(Path(st).read_text())
    doc["last_run"] = (datetime.now(timezone.utc) - timedelta(hours=73)).isoformat()
    Path(st).write_text(_json.dumps(doc))
    sent.clear()
    s.main(["--notify", "--state", st])
    assert "DARK 3d" in sent[0][0]
    assert sent[0][1].startswith("DARK 3 days — accumulated:")


def test_digest_streak_escalates_once(tmp_path, monkeypatch):
    """0.3: a digest tag present escalate_after (3) consecutive runs pages
    ONCE, then stays quiet until the tag clears."""
    s, *_, sent, pings, st = _notify_harness(tmp_path, monkeypatch,
                                             stale_watchlist=True)
    for _ in range(2):
        s.main(["--notify", "--state", st])
    assert not [x for x in sent if "escalated" in x[0]]
    s.main(["--notify", "--state", st])   # third consecutive run
    esc = [x for x in sent if "escalated" in x[0]]
    assert len(esc) == 1 and "STALE-INPUT" in esc[0][0]
    s.main(["--notify", "--state", st])   # fourth — no re-page
    assert len([x for x in sent if "escalated" in x[0]]) == 1


def test_fetch_failed_promotes_to_page_in_open_window(tmp_path, monkeypatch):
    """Taxonomy: FETCH-FAILED is digest-class off-season but a blind fetch
    layer inside an open earnings window pages immediately."""
    from datetime import date

    s, inputs, outputs, sent, pings, st = _notify_harness(tmp_path, monkeypatch)
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    _write_plist(scripts, "com.crude-tanker-fv.price-refresh")   # no heartbeat → FETCH-FAILED
    (inputs / "earnings_calendar.yaml").write_text(yaml.safe_dump({
        "meta": {"quarter": "2026-Q2"},
        "names": {"DHT": {"window_start": date.today(), "window_end": date.today(),
                          "status": "confirmed", "basis": "t"}}}))
    assert s.main(["--notify", "--state", st]) == 1
    pages = [x for x in sent if " PAGE:" in x[0]]
    assert len(pages) == 1 and "FETCH-FAILED price-refresh" in pages[0][1]


def test_stuck_quote_flags_lagging_asof(tmp_path):
    """WO2 1.2 (D-3): a per-ticker asof lagging the run stamp past any weekend
    is a quote nobody is actually fetching — carried-over or Yahoo-static."""
    inputs, outputs = _fixture(tmp_path)
    fetched = datetime.now(timezone.utc)
    (inputs / "market_data" / "prices_daily.yaml").write_text(yaml.safe_dump({
        "fetched_at": fetched.isoformat(timespec="seconds"),
        "prices": {
            "DHT": {"price": 16.5, "asof": fetched.isoformat(timespec="seconds")},
            "TEN": {"price": 20.0, "carried_over": True,
                    "asof": (fetched - timedelta(days=6)).isoformat(timespec="seconds")}}}))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1
    assert "TEN stuck quote" in flags[0] and "carried-over" in flags[0]


def test_uningested_prints_pareto_lane(tmp_path):
    """WO2 1.2: dailies staged >7d past spot_tce's as_of.default flag; held
    classes live in overrides and never trip this lane."""
    from datetime import date

    inputs, outputs = _fixture(tmp_path)
    staged = inputs / "research_pareto" / "2026" / "07"
    staged.mkdir(parents=True)
    (staged / f"{date.today().isoformat()}_Periodical-ShippingDaily.pdf").write_bytes(b"x")

    (inputs / "market_data" / "spot_tce.yaml").write_text(yaml.safe_dump({
        "as_of": {"default": date.today() - timedelta(days=20),
                  "LNGC": date.today() - timedelta(days=40)},   # held — must not flag
        "spot_tce": {"VLCC": 100000, "LNGC": 40000}}))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and flags[0].startswith("UNINGESTED-PRINTS spot_tce.yaml")

    (inputs / "market_data" / "spot_tce.yaml").write_text(yaml.safe_dump({
        "as_of": {"default": date.today() - timedelta(days=3)},
        "spot_tce": {"VLCC": 100000}}))
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []


def test_uningested_prints_ocr_lane(tmp_path):
    from datetime import date

    inputs, outputs = _fixture(tmp_path)
    (inputs / "market_data" / "ffa_forward_curve.yaml").write_text(yaml.safe_dump({
        "as_of": {"default": date.today() - timedelta(days=20)},
        "ffa_forward_curve": {"Cape": [1, 2]}}))
    state = tmp_path / "state"
    state.mkdir(exist_ok=True)
    (state / "ffa_ocr_curves.json").write_text(json.dumps(
        {date.today().isoformat(): {"Cape": {}}, "not-a-date": {}}))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and flags[0].startswith("UNINGESTED-PRINTS ffa_forward_curve.yaml")


def test_source_silence_per_feed(tmp_path):
    """WO2 1.2: per-source silence off the staged artifacts themselves —
    business-day aware for daily feeds, explicit silence_days respected."""
    from datetime import date

    inputs, outputs = _fixture(tmp_path)
    (inputs / "rocketchat_sources.yaml").write_text(yaml.safe_dump({
        "sources": [
            {"name": "pareto_research", "kind": "file", "single_sender": True,
             "dest_dir": "inputs/research_pareto", "expect_cadence": "business-daily"},
            {"name": "baltic_indexes", "kind": "text", "silence_days": 3,
             "dest_file": "inputs/market_data/baltic.csv",
             "expect_cadence": "business-daily"}]}))

    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 2 and all("no staged artifacts" in f for f in flags)

    staged = inputs / "research_pareto" / "2026"
    staged.mkdir(parents=True)
    (staged / f"{date.today().isoformat()}_x.pdf").write_bytes(b"x")
    (inputs / "market_data" / "baltic.csv").write_text(
        f"date,BDI\n{date.today().isoformat()},2500\n")
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []

    old = (date.today() - timedelta(days=9)).isoformat()
    (staged / f"{date.today().isoformat()}_x.pdf").unlink()
    (staged / f"{old}_x.pdf").write_bytes(b"x")
    (inputs / "market_data" / "baltic.csv").write_text(f"date,BDI\n{old},2500\n")
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 2
    pareto = next(f for f in flags if "pareto_research" in f)
    assert "business days silent" in pareto and "single-sender" in pareto
    assert any("baltic_indexes" in f and "9d silent (limit 3d)" in f for f in flags)


def test_harvester_silence_and_marks_trail(tmp_path):
    """WO2 1.3: mirror silence >10d flags; broker issues staged >7d past the
    newest PROMOTED transaction print flag the marks trail; fresh both = quiet."""
    from datetime import date

    inputs, outputs = _fixture(tmp_path)
    sh = tmp_path / "shipping_harvester" / "data"
    sh.mkdir(parents=True)
    manifest = sh / "manifest.jsonl"

    manifest.write_text(json.dumps(
        {"published": (date.today() - timedelta(days=15)).isoformat()}) + "\n")
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and flags[0].startswith("STALE-INPUT harvester")

    manifest.write_text(
        json.dumps({"published": (date.today() - timedelta(days=2)).isoformat()})
        + "\nnot-json garbage line\n")
    tx = inputs / "market_data" / "transactions"
    tx.mkdir(parents=True)
    (tx / "aframax.yaml").write_text(yaml.safe_dump({
        "class": "Aframax",
        "prints": [{"date": date.today() - timedelta(days=30),
                    "sale_price_usd_m": 40.0}]}))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and flags[0].startswith("UNINGESTED-PRINTS marks-trail")

    (tx / "aframax.yaml").write_text(yaml.safe_dump({
        "prints": [{"date": date.today() - timedelta(days=1)}]}))
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []


def test_trigger_evidence_from_tanker_period_signals(tmp_path):
    """WO2 1.4: scanned period-market signals newer than the tanker hold flag
    TRIGGER-EVIDENCE; signals predating the hold (or no hold left) are quiet."""
    from datetime import date as _date

    inputs, outputs = _fixture(tmp_path)
    (inputs / "market_data" / "ffa_forward_curve.yaml").write_text(yaml.safe_dump({
        "as_of": {"default": _date(2026, 7, 2), "VLCC": _date(2026, 6, 7),
                  "Ctr-Feeder": _date(2026, 4, 1)},
        "ffa_forward_curve": {"VLCC": [1], "Ctr-Feeder": [1]}}))
    tx = inputs / "market_data" / "transactions"
    tx.mkdir(parents=True)
    scan = tx / "_scan_state.json"

    scan.write_text(json.dumps({"tanker_period_signals": {"hits": [
        {"date": "2026-06-30", "kind": "period-tc", "sentence": "a VLCC fixed..."}]}}))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1
    assert flags[0].startswith("TRIGGER-EVIDENCE tanker_forward_print_lands")
    assert "since the 2026-06-07 hold" in flags[0]

    scan.write_text(json.dumps({"tanker_period_signals": {"hits": [
        {"date": "2026-06-01", "kind": "period-tc", "sentence": "pre-hold noise"}]}}))
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []

    # Hold resolved (no tanker overrides) — evidence lane retires itself.
    (inputs / "market_data" / "ffa_forward_curve.yaml").write_text(yaml.safe_dump({
        "as_of": {"default": _date(2026, 7, 20), "Ctr-Feeder": _date(2026, 4, 1)},
        "ffa_forward_curve": {"VLCC": [1], "Ctr-Feeder": [1]}}))
    scan.write_text(json.dumps({"tanker_period_signals": {"hits": [
        {"date": "2026-07-10", "kind": "tanker-ffa", "sentence": "TD3C FFA..."}]}}))
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []


def test_fleet_transaction_unreviewed_counter(tmp_path):
    """WO2 3.2: cumulative candidates past the --mark-reviewed ack flag; a
    full ack silences."""
    inputs, outputs = _fixture(tmp_path)
    tx = inputs / "market_data" / "transactions"
    tx.mkdir(parents=True)
    scan = tx / "_scan_state.json"

    scan.write_text(json.dumps({"candidates_cumulative": 7, "candidates_reviewed": 4}))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and flags[0].startswith("FLEET-TRANSACTION 3 unreviewed")

    scan.write_text(json.dumps({"candidates_cumulative": 7, "candidates_reviewed": 7}))
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []


def test_pure_mode_keeps_content_checks_drops_machine_local(tmp_path):
    """WO2 0.4: --pure sees dated triggers + committed surfaces; machine-local
    signals (prices fetch age, notify env, heartbeats) are the Mac's job."""
    inputs, outputs = _fixture(tmp_path, trigger_due=True, fresh_prices=False)
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    _write_plist(scripts, "com.crude-tanker-fv.price-refresh")   # no heartbeat

    normal = {f.split()[0] for f in collect_flags(inputs, outputs, environ={})}
    assert normal == {"TRIGGER-DUE", "PRICE-BASIS", "NOTIFY-UNCONFIGURED",
                      "FETCH-FAILED"}
    pure = collect_flags(inputs, outputs, environ={}, pure=True)
    assert [f.split()[0] for f in pure] == ["TRIGGER-DUE"]


def test_pure_mode_flags_stale_head_in_open_window(tmp_path):
    """0.4: in an open earnings window, a HEAD older than 3d means the Action
    is watching a stale world — flag it on the backstop itself."""
    import subprocess
    from datetime import date

    inputs, outputs = _fixture(tmp_path)
    (inputs / "earnings_calendar.yaml").write_text(yaml.safe_dump({
        "meta": {"quarter": "2026-Q2"},
        "names": {"DHT": {"window_start": date.today(), "window_end": date.today(),
                          "status": "confirmed", "basis": "t"}}}))
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    old = (datetime.now(timezone.utc) - timedelta(days=5)).isoformat()
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t",
                    "commit", "-qm", "old"], cwd=tmp_path, check=True,
                   env={"GIT_AUTHOR_DATE": old, "GIT_COMMITTER_DATE": old,
                        "PATH": "/usr/bin:/bin"})
    flags = collect_flags(inputs, outputs, environ={}, pure=True)
    assert any("repo HEAD 5d old" in f for f in flags)
    # (the same open window legitimately emits calendar flags for DHT — 2.3)
    assert all(f.split()[0] in ("STALE-INPUT", "EARNINGS-DUE",
                                "STALE-BALANCE-SHEET") for f in flags)


def test_filing_events_landed_overdue_unseeded(tmp_path):
    """WO2 2.3: fresh manifest arrivals page FILING-LANDED (+AMENDED); a
    passed window with no arrival and no balance sheet pages FILING-OVERDUE
    (the Oslo net); a watchlist name with no calendar entry is
    CALENDAR-UNSEEDED; a landed balance sheet clears the overdue."""
    from datetime import date as _date

    inputs, outputs = _fixture(tmp_path)
    state = tmp_path / "state"
    state.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc)
    old_end = _date.today() - timedelta(days=10)
    (inputs / "earnings_calendar.yaml").write_text(yaml.safe_dump({
        "meta": {"quarter": "2026-Q2"},
        "names": {"DHT": {"window_start": old_end - timedelta(days=2),
                          "window_end": old_end,
                          "status": "confirmed", "basis": "t"}}}))

    # Fresh arrival: FILING-LANDED pages, overdue is satisfied by the arrival.
    (state / "edgar_manifest.jsonl").write_text(json.dumps({
        "ts": now.isoformat(timespec="seconds"), "ticker": "DHT", "cik": "x",
        "accession": "0001-26-000009", "form": "6-K/A",
        "filed": _date.today().isoformat(), "staged_path": None,
        "amended": True}) + "\n")
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    landed = [f for f in flags if f.startswith("FILING-LANDED")]
    assert len(landed) == 1 and "6-K/A AMENDED" in landed[0]
    assert not any(f.startswith("FILING-OVERDUE") for f in flags)
    # STALE-BALANCE-SHEET rides the same calendar (report out, no Q2 sheet).
    assert any(f.startswith("STALE-BALANCE-SHEET DHT") for f in flags)

    # No arrival at all: FILING-OVERDUE pages; a landed balance sheet clears it.
    (state / "edgar_manifest.jsonl").unlink()
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert any(f.startswith("FILING-OVERDUE DHT") for f in flags)
    bs = inputs / "balance_sheets"
    bs.mkdir()
    (bs / "dht_2026-Q2.yaml").write_text("{}\n")
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert not any(f.startswith("FILING-OVERDUE") for f in flags)
    assert not any(f.startswith("STALE-BALANCE-SHEET") for f in flags)

    # A watchlist name missing from the calendar = CALENDAR-UNSEEDED.
    (inputs / "watchlist.yaml").write_text(yaml.safe_dump({
        "DHT": {"current_price": 16.5, "analyst_target": 18.0,
                "as_of": str(_date.today())},
        "CMBT": {"current_price": 10.0, "analyst_target": 12.0,
                 "as_of": str(_date.today())}}))
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert any(f.startswith("CALENDAR-UNSEEDED CMBT") for f in flags)


def test_meta_mode_suspends_content_checks_on_dirty_tree(tmp_path, monkeypatch, capsys):
    """Invariant 3: dirty tree → content checks suspended (a trigger that
    would flag doesn't), digest still goes out, rc 0."""
    import subprocess

    s, *_, sent, pings, st = _notify_harness(tmp_path, monkeypatch, trigger_due=True)
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)   # untracked fixture = dirty
    assert s.main(["--notify", "--state", st]) == 0
    out = capsys.readouterr().out
    assert "META dirty-tree" in out and "TRIGGER-DUE" not in out
    assert len(sent) == 1 and "daily digest — OK" in sent[0][0]
    assert "META dirty-tree" in sent[0][1]


def test_dirty_too_long_pages_at_36h_and_12h_in_window(tmp_path, monkeypatch, capsys):
    import json as _json
    import subprocess
    from datetime import date

    s, inputs, outputs, sent, pings, st = _notify_harness(tmp_path, monkeypatch,
                                                          trigger_due=True)
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    Path(st).write_text(_json.dumps({
        "dirty_since": (datetime.now(timezone.utc) - timedelta(hours=40)).isoformat()}))
    assert s.main(["--state", st]) == 1
    assert "DIRTY-TOO-LONG" in capsys.readouterr().out

    # Inside an open window the limit tightens to 12h.
    (inputs / "earnings_calendar.yaml").write_text(yaml.safe_dump({
        "meta": {"quarter": "2026-Q2"},
        "names": {"DHT": {"window_start": date.today(), "window_end": date.today(),
                          "status": "confirmed", "basis": "t"}}}))
    Path(st).write_text(_json.dumps({
        "dirty_since": (datetime.now(timezone.utc) - timedelta(hours=13)).isoformat()}))
    assert s.main(["--state", st]) == 1
    assert "earnings window open" in capsys.readouterr().out


def test_exit_codes_and_log_format(tmp_path, monkeypatch):
    import crude_tanker_fv.sentinel as s

    for k, v in FAKE_ENV.items():
        monkeypatch.setenv(k, v)
    inputs, outputs = _fixture(tmp_path)
    monkeypatch.setattr(s, "INPUTS_DIR", inputs)
    monkeypatch.setattr(s, "OUTPUTS_DIR", outputs)
    log = tmp_path / "state" / "sentinel.log"
    assert main(["--log", str(log)]) == 0
    assert log.read_text().strip().endswith(" OK")

    inputs2, outputs2 = _fixture(tmp_path / "b", trigger_due=True)
    monkeypatch.setattr(s, "INPUTS_DIR", inputs2)
    monkeypatch.setattr(s, "OUTPUTS_DIR", outputs2)
    assert main(["--log", str(log)]) == 1
    last = log.read_text().strip().splitlines()[-1]
    assert " FLAG 1: TRIGGER-DUE" in last
