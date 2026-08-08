"""Consensus forward-EPS cross-check tests (METHODOLOGY §9.11)."""

from pathlib import Path

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
import pytest

from crude_tanker_fv.consensus_eps import (
    EARNINGS_DRIVEN_THRESHOLD_PCT,
    ConsensusEpsRow,
    compute_consensus_eps_rows,
    run_consensus_eps_xref,
    write_consensus_eps_xref,
)
from crude_tanker_fv.loaders import load_watchlist


def test_rows_cover_names_with_published_fwd_pe():
    rows = compute_consensus_eps_rows(BOOK_QUARTER)
    by = {r.ticker: r for r in rows}
    wl = load_watchlist()
    expected = {t for t, e in wl.items() if e.get("consensus_fwd_pe")}
    assert expected.issubset(set(by)), "every name with a consensus_fwd_pe should produce a row"
    assert len(rows) >= 10


def test_consensus_eps_is_price_over_pe():
    rows = {r.ticker: r for r in compute_consensus_eps_rows(BOOK_QUARTER)}
    wl = load_watchlist()
    r = rows["DHT"]
    assert r.consensus_fwd_eps == pytest.approx(wl["DHT"]["current_price"] / wl["DHT"]["consensus_fwd_pe"])
    # earnings yield is the reciprocal of the P/E
    assert r.consensus_earnings_yield_pct == pytest.approx(100.0 / r.consensus_fwd_pe)


def test_gap_sign_and_earnings_driven_flag():
    rows = {r.ticker: r for r in compute_consensus_eps_rows(BOOK_QUARTER)}
    r = rows["DHT"]
    # gap is 100*(tool-cons)/cons
    expected_gap = 100.0 * (r.tool_fwd_eps - r.consensus_fwd_eps) / r.consensus_fwd_eps
    assert r.eps_gap_pct == pytest.approx(expected_gap)
    # at the 2026 cycle peak the FFA strip runs hotter than consensus for crude
    assert r.eps_gap_pct > 0
    assert r.earnings_driven == (abs(r.eps_gap_pct) >= EARNINGS_DRIVEN_THRESHOLD_PCT)


def test_peak_names_carry_low_w_earn_mitigation():
    """The whole point: where the tool-vs-consensus EPS gap is widest (cycle
    peak), the strip weight w_earn is lowest — the framework compensates."""
    rows = {r.ticker: r for r in compute_consensus_eps_rows(BOOK_QUARTER)}
    dht = rows["DHT"]
    assert dht.band_label == "late-cycle/peak"
    assert dht.w_earn <= 0.35            # strip heavily down-weighted at peak
    assert dht.eps_gap_pct > 50          # and the gap is large — the mitigation is real


def test_hybrid_flagged():
    rows = {r.ticker: r for r in compute_consensus_eps_rows(BOOK_QUARTER)}
    assert rows["INSW"].hybrid is True
    assert rows["DHT"].hybrid is False


def test_tool_implied_pe_consistent():
    rows = compute_consensus_eps_rows(BOOK_QUARTER)
    for r in rows:
        if r.tool_fwd_eps > 0:
            assert r.tool_implied_pe == pytest.approx(r.price / r.tool_fwd_eps)
        else:
            assert r.tool_implied_pe is None


def test_writer_emits_md_and_xlsx(tmp_path: Path):
    rows = compute_consensus_eps_rows(BOOK_QUARTER)
    write_consensus_eps_xref(rows, outputs_dir=tmp_path)
    md = tmp_path / "consensus_eps_xref.md"
    xlsx = tmp_path / "consensus_eps_xref.xlsx"
    assert md.exists() and xlsx.exists()
    text = md.read_text()
    assert "Consensus forward-EPS cross-check" in text
    assert "w_earn" in text


def test_run_returns_rows(tmp_path: Path):
    rows = run_consensus_eps_xref(BOOK_QUARTER, outputs_dir=tmp_path)
    assert rows
    assert all(isinstance(r, ConsensusEpsRow) for r in rows)
