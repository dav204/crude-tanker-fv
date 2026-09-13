"""The dry FFA promote lane (2026-09-13) reproduces the ruled construction exactly — pinned
against the 2026-09-01 promote the owner ratified (decisions/ffa_promotion_2026-09-02.md) —
and FREEZES on everything it was never ruled on: a flagged parse, an unruled panel shape, a
stale print, and the one conjunct that always needed a word, a cycle-band crossing (Q-7)."""

from datetime import date

import pytest
import yaml

from crude_tanker_fv import ffa_promote as fp

# The 2026-09-01 panel, image-verified in the promotion record.
PANEL_0901 = {
    "cape": {"sep": 45125, "oct": 46000, "q4": 44125, "q1": 29925, "cal27": 33200},
    "pmax": {"sep": 22200, "oct": 23800, "q4": 23083, "q1": 18100, "cal27": 18225},
    "smax": {"sep": 19775, "oct": 21725, "q4": 20883, "q1": 15900, "cal27": 16150},
}
CURVE_FILE = """as_of:
  default: 2026-08-31
  Cape: 2026-08-31          # prior promote
  Pana: 2026-08-31
  Post-Panamax: 2026-08-31
  Supra-Ultra: 2026-08-31
  Handy-Bulk: 2026-07-10    # own cadence
ffa_forward_curve:
  Cape:              # FFA 31-Aug (image-verified). A comment that must survive.
                     # second comment line
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  Pana:              # pana comment
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  Post-Panamax:     # shares the Pana freight basin
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  Supra-Ultra:       # supra comment
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  Handy-Bulk:      # DERIVED = Supra-Ultra x 0.90
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
"""
TWELVE_FILE = """rate_basis:
  note: keep me
as_of:
  Cape: 2026-08-31
  Pana: 2026-08-31
  Post-Panamax: 2026-08-31
  Supra-Ultra: 2026-08-31
  Handy-Bulk: 2026-07-10
twelve_month_tc:
  Cape: 37300           # prior vintage comment
  Pana: 20550
  Post-Panamax: 20550
  Supra-Ultra: 18467
  Handy-Bulk: 14500     # MB dry weekly — NOT the FFA loop
"""
MEANS = {"historical_tce_means": {"Cape": 23650, "Pana": 11900, "Post-Panamax": 11900,
                                  "Supra-Ultra": 13930, "Handy-Bulk": 12850}}


def _inputs(tmp_path):
    md = tmp_path / "market_data"
    md.mkdir(parents=True)
    (md / "ffa_forward_curve.yaml").write_text(CURVE_FILE)
    (md / "twelve_month_tc.yaml").write_text(TWELVE_FILE)
    (md / "historical_tce_means.yaml").write_text(yaml.safe_dump(MEANS))
    return tmp_path


def _db(iso="2026-09-01", panel=None, status="ok"):
    return {iso: {"curves": panel or PANEL_0901, "status": status, "issues": []}}


def test_construction_matches_the_ratified_2026_09_01_promote(tmp_path):
    built = fp.construct("2026-09-01", _db()["2026-09-01"])
    # The committed file's own numbers, from decisions/ffa_promotion_2026-09-02.md.
    assert built["curves"]["Cape"] == [45125, 44125, 29925, 34292, 34292, 34291, 33791, 33291]
    assert built["curves"]["Pana"] == [22200, 23083, 18100, 18267, 18267, 18266, 17866, 17566]
    assert built["curves"]["Supra-Ultra"] == [19775, 20883, 15900, 16234, 16233, 16233, 15933, 15633]
    assert built["curves"]["Post-Panamax"] == built["curves"]["Pana"]
    assert built["curves"]["Handy-Bulk"] == [17800, 18790, 14310, 14610, 14610, 14610, 14340, 14070]
    # 12M proxy, unrounded half-up (Q-1)
    assert built["twelve_month"] == {"Cape": 37025, "Pana": 20592, "Supra-Ultra": 18392,
                                     "Post-Panamax": 20592}
    assert "Handy-Bulk" not in built["twelve_month"]
    # the Cal-27 identity is exact for every class
    for cls, cal in (("Cape", 33200), ("Pana", 18225), ("Supra-Ultra", 16150)):
        c = built["curves"][cls]
        assert sum(c[2:6]) == 4 * cal


def test_apply_writes_both_files_and_keeps_comments(tmp_path):
    inp = _inputs(tmp_path)
    res = fp.run(inp, apply_it=True, today=date(2026, 9, 2), db_path=_write_db(tmp_path, _db()))
    assert res["applied"] and res["committed_was"] == "2026-08-31"
    curve_text = (inp / "market_data" / "ffa_forward_curve.yaml").read_text()
    assert "A comment that must survive." in curve_text and "# second comment line" in curve_text
    assert "promoted 2026-09-02 by crude_tanker_fv.ffa_promote" in curve_text
    d = yaml.safe_load(curve_text)
    assert d["ffa_forward_curve"]["Cape"] == [45125, 44125, 29925, 34292, 34292, 34291, 33791, 33291]
    # unquoted ISO dates parse as date objects here exactly as they do in the real file
    assert d["as_of"]["Cape"] == date(2026, 9, 1) and d["as_of"]["Handy-Bulk"] == date(2026, 9, 1)
    assert d["as_of"]["default"] == date(2026, 8, 31)     # the tanker default is not ours to move
    t = yaml.safe_load((inp / "market_data" / "twelve_month_tc.yaml").read_text())
    assert t["twelve_month_tc"]["Cape"] == 37025 and t["twelve_month_tc"]["Supra-Ultra"] == 18392
    assert t["twelve_month_tc"]["Handy-Bulk"] == 14500     # MB cadence, untouched
    assert t["rate_basis"]["note"] == "keep me"
    assert "MB dry weekly — NOT the FFA loop" in (inp / "market_data" / "twelve_month_tc.yaml").read_text()


def test_a_band_crossing_freezes_the_lane(tmp_path):
    inp = _inputs(tmp_path)
    hot = {p: dict(v) for p, v in PANEL_0901.items()}
    hot["smax"]["q4"] = 30000                      # lifts the Supra 12M through 1.5x
    with pytest.raises(fp.Freeze, match="cycle BAND crossing"):
        fp.run(inp, apply_it=True, today=date(2026, 9, 2), db_path=_write_db(tmp_path, _db(panel=hot)))
    assert yaml.safe_load((inp / "market_data" / "twelve_month_tc.yaml").read_text())["twelve_month_tc"]["Supra-Ultra"] == 18467


def test_flagged_stale_and_already_committed_prints_are_refused(tmp_path):
    inp = _inputs(tmp_path)
    with pytest.raises(fp.Freeze, match="no promotable print"):
        fp.run(inp, today=date(2026, 9, 2), db_path=_write_db(tmp_path, _db(status="flagged")))
    with pytest.raises(fp.Freeze, match="no promotable print"):
        fp.run(inp, today=date(2026, 9, 30), db_path=_write_db(tmp_path, _db()))
    with pytest.raises(fp.Freeze, match="no promotable print"):
        fp.run(inp, today=date(2026, 9, 2), db_path=_write_db(tmp_path, _db(iso="2026-08-30")))


def test_an_unruled_panel_shape_freezes(tmp_path):
    # the 2026-07-13 shape: two months INSIDE one quarter — a different construction the
    # owner ruled separately; the lane must not guess it
    mid = {p: {"jul": 1, "aug": 2, "q3": 3, "q4": 4, "cal27": 5} for p in fp.PANELS}
    with pytest.raises(fp.Freeze, match="not the ruled STRADDLING shape"):
        fp.construct("2026-07-13", {"curves": mid, "status": "ok"})
    four = {p: {"sep": 1, "q4": 2, "q1": 3, "cal27": 4} for p in fp.PANELS}
    with pytest.raises(fp.Freeze, match="unruled panel shape"):
        fp.construct("2026-09-02", {"curves": four, "status": "ok"})


def test_packet_states_the_bands(tmp_path):
    inp = _inputs(tmp_path)
    res = fp.run(inp, today=date(2026, 9, 2), db_path=_write_db(tmp_path, _db()))
    p = res["packet"]
    assert "| Cape | 37300 | 37025 | -0.74% |" in p
    assert "late-cycle/peak" in p and "Handy-Bulk's 12M TC is untouched" in p
    assert not res["applied"]


def _write_db(tmp_path, db):
    import json
    p = tmp_path / "curves.json"
    p.write_text(json.dumps(db))
    return p
