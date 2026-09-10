"""The promoter's lane-D predicate (2026-09-02).

This predicate decides whether standing drift may be absorbed without the owner. Its ONLY
acceptable failure direction is freezing something it could have absorbed; absorbing
something it should have frozen is the incident this repo cannot afford, so every conjunct
is tested for the FREEZE direction explicitly.
"""

from pathlib import Path


from crude_tanker_fv import promote
from crude_tanker_fv.drift_gate import DriftRow

ROOT = Path(__file__).resolve().parents[1]


def _rows(*rows):
    return list(rows)


def _stable(t="AAA"):
    return DriftRow(ticker=t, pnav_basis="pareto", status="stable")


def _ev_only(t="BBB", d_ev=-3.0):
    return DriftRow(ticker=t, pnav_basis="pareto", status="explained", breaches=["ev_pct"],
                    d_ev=d_ev, d_nav_pct=0.0)


def _run(monkeypatch, rows, dirt=None):
    monkeypatch.setattr(promote, "_non_drift_dirt", lambda root=None: dirt or [])
    from crude_tanker_fv import drift_gate
    monkeypatch.setattr(drift_gate, "evaluate", lambda *a, **k: rows)
    monkeypatch.setattr(drift_gate, "load_baseline", lambda *a, **k: {"thresholds": {"k_broker": 0.05}})
    monkeypatch.setattr(promote.Path, "exists", lambda self: True)
    monkeypatch.setattr(promote.json, "loads", lambda *_a, **_k: {"tickers": {}})
    monkeypatch.setattr(promote.Path, "read_text", lambda self, *a, **k: "{}")
    return promote.evaluate_price_absorb()


def test_ev_only_drift_is_absorbable(monkeypatch):
    v = _run(monkeypatch, _rows(_stable(), _ev_only()))
    assert v.ok, v.render()


def test_a_nav_move_freezes(monkeypatch):
    row = DriftRow(ticker="CAPT", pnav_basis="pareto", status="explained",
                   breaches=["ev_pct", "tool_nav"], d_nav_pct=11.89, d_ev=-2.4)
    v = _run(monkeypatch, _rows(row))
    assert not v.ok
    assert any("SOURCING event" in r for r in v.freeze_reasons)


def test_a_band_exit_freezes(monkeypatch):
    row = DriftRow(ticker="SBLK", pnav_basis="pareto", status="explained", breaches=["position_band"],
                   d_nav_pct=0.0, band_from="HOLD (fairly valued)", band_to="TRIM/SHORT (overvalued)")
    v = _run(monkeypatch, _rows(row))
    assert not v.ok
    assert any("band EXIT" in r for r in v.freeze_reasons)


def test_a_flip_toward_buy_freezes(monkeypatch):
    row = DriftRow(ticker="SB", pnav_basis="pareto", status="explained",
                   breaches=["position_band band-mech"], d_nav_pct=0.0,
                   band_from="HOLD (fairly valued)", band_to="BUY (undervalued)")
    v = _run(monkeypatch, _rows(row))
    assert not v.ok
    assert any("toward BUY" in r for r in v.freeze_reasons)


def test_a_relabelled_name_does_not_count_as_buyward(monkeypatch):
    """CAPT/BRUT/TNK/MPCC carry a governed relabel — their raw band is not what the book
    acts on, so a raw BUY there must not freeze the lane forever."""
    row = DriftRow(ticker="CAPT", pnav_basis="pareto", status="explained",
                   breaches=["position_band band-mech"], d_nav_pct=0.0,
                   band_from="HOLD (fairly valued)", band_to="BUY (undervalued)")
    v = _run(monkeypatch, _rows(row))
    assert not any("toward BUY" in r for r in v.freeze_reasons), v.render()


def test_a_k_breach_freezes(monkeypatch):
    row = DriftRow(ticker="ECO", pnav_basis="pareto", status="explained", breaches=["k_broker"],
                   d_nav_pct=0.0, d_k=-0.09)
    v = _run(monkeypatch, _rows(row))
    assert not v.ok
    assert any("k_broker" in r for r in v.freeze_reasons)


def test_non_drift_dirt_freezes(monkeypatch):
    v = _run(monkeypatch, _rows(_ev_only()), dirt=["src/crude_tanker_fv/nav.py"])
    assert not v.ok
    assert any("mid-surgery" in r for r in v.freeze_reasons)


def test_drift_list_dirt_does_not_freeze():
    """The real dirt filter: files on scripts/drift_files.txt are routine, anything else is surgery."""
    listed = [ln.strip() for ln in (ROOT / "scripts" / "drift_files.txt").read_text().splitlines()
              if ln.strip() and not ln.startswith("#")]
    assert "inputs/market_data/prices_daily.yaml" in listed


def test_check_is_read_only():
    """`check` opens committed surfaces and writes nothing — the whole point of shipping it
    before the landing lane exists."""
    src = (ROOT / "src" / "crude_tanker_fv" / "promote.py").read_text()
    for forbidden in ("write_text(", "open(", "mkdir(", "ratify", "commit"):
        assert f".{forbidden}" not in src.replace("# ", ""), forbidden


# ---- LANE LAND (auto-ratify), 2026-09-10 -------------------------------------------------
# The lane may run scripts/ratify_baseline.sh ONLY when every precondition holds. Each test
# below breaks exactly one and asserts the lane refuses; the non-dry path is exercised through
# a patched runner that records argv — the real script is never invoked.

import json as _json
from datetime import date as _date, datetime as _dt, timezone as _tz

import pytest as _pytest

from crude_tanker_fv import promote as _promote
from crude_tanker_fv.drift_gate import DriftRow as _Row


def _row(t, status="explained", band_from="HOLD", band_to="HOLD", d_ev=3.0):
    return _Row(ticker=t, pnav_basis="pareto", status=status, breaches=["ev_pct"] if status != "stable" else [],
                d_ev=d_ev, d_nav_pct=0.0, band_from=band_from, band_to=band_to, d_k=0.0)


def _land_fixture(tmp_path, monkeypatch, rows, *, annotated=True, dirt=(), stamp=None, run_age_h=1.0):
    root = tmp_path
    (root / "baselines").mkdir(); (root / "state").mkdir(); (root / "outputs").mkdir(); (root / "decisions").mkdir()
    (root / "baselines" / "reconcile_baseline.yaml").write_text("meta: {ratified_at: '2026-08-31T20:00:00Z'}\n")
    run_at = (_dt.now(_tz.utc).replace(microsecond=0) - __import__("datetime").timedelta(hours=run_age_h)).isoformat()
    (root / "state" / "last_run.json").write_text(_json.dumps({"run_at": run_at, "quarter": "2026-Q2"}))
    head = "abc1234"
    (root / "outputs" / "book_scorecard.json").write_text(_json.dumps({"source_commit": stamp or head}))
    for r in rows:
        (root / "decisions" / f"{r.ticker.lower()}_log.md").write_text(
            f"# {r.ticker} — Decision Log\n\n## 2026-09-10 — Annotation\n\n"
            f"**Decision:** PRICE LEG for {r.ticker} absorbed as its own commit. More detail follows.\n")
    import crude_tanker_fv.drift_gate as dg
    monkeypatch.setattr(dg, "load_baseline", lambda p: {"meta": {"ratified_at": "2026-08-31T20:00:00Z"}})
    monkeypatch.setattr(dg, "evaluate", lambda baseline, state: rows)
    monkeypatch.setattr(dg, "decision_log_annotated_since", lambda t, since, d: annotated)
    monkeypatch.setattr(_promote, "_non_drift_dirt", lambda root: list(dirt))

    # The surface stamp is normally an ANCESTOR of HEAD (inputs commit -> regen -> outputs
    # commit); "current" = reachable from HEAD with no determinant diff since. Model both.
    def fake_git(root, *a):
        if a[:2] == ("rev-parse", "--short"):
            return head
        if a[0] == "diff":
            return "" if a[2] == head else " src/crude_tanker_fv/nav.py | 1 +"
        return ""

    def fake_git_ok(root, *a):
        if a[:2] == ("merge-base", "--is-ancestor"):
            return a[2] == head
        return True

    monkeypatch.setattr(_promote, "_git", fake_git)
    monkeypatch.setattr(_promote, "_git_ok", fake_git_ok)
    return root


def test_land_dry_run_passes_and_composes_the_cause(tmp_path, monkeypatch, capsys):
    rows = [_row("DHT"), _row("TNK"), _row("SB", status="stable", d_ev=0.0)]
    root = _land_fixture(tmp_path, monkeypatch, rows)
    calls = []
    rc = _promote.land(root, dry_run=True, runner=lambda *a, **k: calls.append(a))
    out = capsys.readouterr().out
    assert rc == 0 and calls == []
    assert "auto-land " in out and "PRICE LEG for DHT absorbed as its own commit." in out
    assert "PRICE LEG for TNK absorbed as its own commit." in out
    assert "DRY RUN" in out and "pending annotation" not in out


@_pytest.mark.parametrize("breaker", ["unexplained", "unannotated", "dirt", "buyward", "stale_state", "stamp_mismatch", "dirty_stamp"])
def test_land_refuses_when_any_precondition_fails(tmp_path, monkeypatch, breaker):
    rows = [_row("DHT"), _row("TNK")]
    kw = {}
    if breaker == "unexplained":
        rows[0] = _row("DHT", status="UNEXPLAINED")
    elif breaker == "unannotated":
        kw["annotated"] = False
    elif breaker == "dirt":
        kw["dirt"] = ["src/crude_tanker_fv/nav.py"]
    elif breaker == "buyward":
        # a NON-relabelled name: TNK/DHT carry governed relabels and are rightly excluded
        rows[1] = _row("SBLK", band_from="HOLD (fairly valued)", band_to="BUY (undervalued)")
    elif breaker == "stale_state":
        kw["run_age_h"] = 30.0
    elif breaker == "stamp_mismatch":
        kw["stamp"] = "deadbee"
    elif breaker == "dirty_stamp":
        kw["stamp"] = "abc1234-dirty"
    root = _land_fixture(tmp_path, monkeypatch, rows, **kw)
    calls = []
    rc = _promote.land(root, dry_run=False, runner=lambda *a, **k: calls.append(a))
    assert rc == 1, breaker
    assert calls == [], f"{breaker}: the lane ran something on a failed precondition"


def test_land_non_dry_invokes_the_ratify_script_then_commits_its_two_files(tmp_path, monkeypatch):
    rows = [_row("DHT")]
    root = _land_fixture(tmp_path, monkeypatch, rows)
    calls = []
    rc = _promote.land(root, dry_run=False, runner=lambda argv, **k: calls.append(argv))
    assert rc == 0
    assert calls[0][0] == "scripts/ratify_baseline.sh" and calls[0][1].startswith("auto-land ")
    assert calls[1] == ["git", "add", "baselines/reconcile_baseline.yaml", "RATIFY_LOG.md"]
    assert calls[2][:3] == ["git", "commit", "-q"] and "auto-land" in calls[2][-1]


def test_cause_never_exceeds_the_cap_and_dedupes(tmp_path):
    d = tmp_path / "decisions"; d.mkdir()
    rows = []
    for i in range(30):
        t = f"T{i:02d}"
        (d / f"{t.lower()}_log.md").write_text(f"# {t}\n\n## 2026-09-10 — x\n\n**Decision:** Same sentence every time. Then more.\n")
        rows.append(_row(t))
    cause = _promote.compose_cause(rows, d, _date(2026, 9, 10))
    assert len(cause) <= _promote.CAUSE_CAP
    assert cause.count("Same sentence every time.") == 1
    assert cause.startswith("auto-land 2026-09-10: ")


def test_cause_skips_placeholders(tmp_path):
    d = tmp_path / "decisions"; d.mkdir()
    (d / "dht_log.md").write_text("# DHT\n\n## 2026-09-10T00:00:00+00:00 — Pipeline run (auto)\n\n**Decision:** _[pending annotation]_\n")
    assert _promote._first_decision_sentence("DHT", d) == ""


def test_land_does_nothing_on_a_quiet_gate(tmp_path, monkeypatch, capsys):
    """Wired into the cron 2026-09-10: a morning with no moved rows must NOT re-ratify an
    unchanged baseline (a daily noise commit with an empty cause). Exit 0, run nothing."""
    rows = [_row("DHT", status="stable", d_ev=0.0), _row("SB", status="stable", d_ev=0.0)]
    root = _land_fixture(tmp_path, monkeypatch, rows)
    calls = []
    rc = _promote.land(root, dry_run=False, runner=lambda *a, **k: calls.append(a))
    assert rc == 0 and calls == []
    assert "NOTHING TO LAND" in capsys.readouterr().out
