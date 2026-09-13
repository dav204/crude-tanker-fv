"""Watchlist pair rebase (2026-09-13): the anchors of record are preserved exactly, the
three fields move together to one vintage, comments survive, and the price basis is guarded
(fresh, unflagged, from prices_daily — never prose)."""

from datetime import date

import pytest
import yaml

from crude_tanker_fv import rebase

WATCHLIST = """# header stays
AAA:
  current_price: 37.14     # NYSE close 10 Jun 2026
  analyst_target: 51.50
  consensus_pnav: 0.34     # APPROX 37.14/109.24
  sector: crude
  consensus_fwd_pe: 4.6    # 37.14 / $8 EPS
  as_of: 2026-06-10        # one vintage

BBB:
  current_price: 10.00
  analyst_target: 12.00
  consensus_pnav: null
  consensus_fwd_pe: null
  as_of: 2026-06-10
"""


def _inputs(tmp_path, asof="2026-09-11", extra=None):
    inp = tmp_path / "inputs"
    (inp / "market_data").mkdir(parents=True)
    (inp / "watchlist.yaml").write_text(WATCHLIST)
    row = {"AAA": {"price": 44.32, "asof": f"{asof}T20:00:02+00:00"},
           "BBB": {"price": 11.5, "asof": f"{asof}T20:00:02+00:00"}}
    if extra:
        row.update(extra)
    (inp / "market_data" / "prices_daily.yaml").write_text(yaml.safe_dump({"prices": row}))
    return inp


def test_compute_preserves_the_anchors(tmp_path):
    inp = _inputs(tmp_path)
    v = rebase.compute("AAA", inp, today=date(2026, 9, 13))
    assert v["implied_broker_nav"] == 109.24 and v["eps_basis"] == 8.07
    assert v["pnav"] == 0.41 and v["fwd_pe"] == 5.5 and v["as_of"] == "2026-09-11"


def test_apply_edits_the_block_textually_and_keeps_comments(tmp_path):
    inp = _inputs(tmp_path)
    rebase.apply("AAA", inp, values=rebase.compute("AAA", inp, today=date(2026, 9, 13)), today=date(2026, 9, 13))
    t = (inp / "watchlist.yaml").read_text()
    assert "# header stays" in t and "# NYSE close 10 Jun 2026" in t and "# 37.14 / $8 EPS" in t
    assert "  current_price: 44.32     # NYSE close 10 Jun 2026" in t
    assert "  consensus_pnav: 0.41     # APPROX 37.14/109.24" in t
    assert "  consensus_fwd_pe: 5.5    # 37.14 / $8 EPS" in t
    assert "  as_of: 2026-09-11        # one vintage" in t
    assert "# rebased 2026-09-13 by crude_tanker_fv.rebase" in t
    d = yaml.safe_load(t)
    assert d["AAA"]["current_price"] == 44.32 and d["BBB"]["current_price"] == 10.0
    # a name with no coverage moves price + as_of only
    rebase.apply("BBB", inp, values=rebase.compute("BBB", inp, today=date(2026, 9, 13)), today=date(2026, 9, 13))
    d = yaml.safe_load((inp / "watchlist.yaml").read_text())
    assert d["BBB"]["current_price"] == 11.5 and d["BBB"]["consensus_pnav"] is None


def test_draft_is_written_with_the_not_applied_marker(tmp_path):
    inp = _inputs(tmp_path)
    p = rebase.write_draft("AAA", inp, values=rebase.compute("AAA", inp, today=date(2026, 9, 13)), today=date(2026, 9, 13))
    assert p.name == "watchlist_rebase_2026-09-13_aaa.yaml.draft"
    assert p.read_text().startswith("# NOT-APPLIED")
    assert yaml.safe_load(p.read_text().split("\n", 1)[1])["AAA"]["consensus_pnav"] == 0.41


def test_price_basis_is_guarded(tmp_path):
    with pytest.raises(SystemExit, match="older than"):
        rebase.compute("AAA", _inputs(tmp_path, asof="2026-09-11"), today=date(2026, 9, 20))
    inp = _inputs(tmp_path / "b", extra={"AAA": {"price": 44.32, "asof": "2026-09-11T20:00:02+00:00",
                                                  "price_review": "vs-static +36%"}})
    with pytest.raises(SystemExit, match="flagged"):
        rebase.compute("AAA", inp, today=date(2026, 9, 13))

