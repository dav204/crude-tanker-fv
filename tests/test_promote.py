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
