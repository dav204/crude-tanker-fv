"""Book-wide validation scorecard (Thread 4)."""

from __future__ import annotations

import pytest

from crude_tanker_fv.scorecard import (
    _nav_basis_composite,
    _parity_band_status,
    compute_scorecard,
    write_scorecard,
)

QUARTER = "2026-Q1"


# --- pure helpers (deterministic, no IO) ----------------------------------- #

def test_nav_basis_resale_uniform_only_if_all_uniform():
    s = {"VLCC": "resale-uniform", "Suezmax": "resale-uniform"}
    assert _nav_basis_composite(["VLCC", "Suezmax"], s) == ("resale-uniform", "")


def test_nav_basis_primary_is_most_salient_and_detail_shows_all():
    # holds resale-uniform + pending + unverified ⇒ primary pending-sourceable (more
    # salient than unverified), detail lists BOTH non-uniform groups.
    s = {"VLCC": "resale-uniform", "LR1": "pending-sourceable",
         "MR": "unverified-no-current-xclusiv-line"}
    primary, detail = _nav_basis_composite(["VLCC", "LR1", "MR"], s)
    assert primary == "pending-sourceable"
    assert "pending-sourceable: LR1" in detail and "unverified-no-current-xclusiv-line: MR" in detail


def test_nav_basis_structural_outranks_pending():
    s = {"LNGC": "structural-unavailable", "LR1": "pending-sourceable"}
    primary, _ = _nav_basis_composite(["LNGC", "LR1"], s)
    assert primary == "structural-unavailable"


def test_parity_band_clears_and_out_and_unvalidated():
    assert _parity_band_status(["VLCC"], {"VLCC": 41_700.0}) == "clears"        # in [41220,42220]
    assert _parity_band_status(["VLCC"], {"VLCC": 50_000.0}) == "OUT:VLCC"
    assert _parity_band_status(["LNGC"], {"LNGC": None}) == "unvalidated"        # no registered band
    assert _parity_band_status(["VLCC", "LNGC"], {"VLCC": 41_700.0, "LNGC": None}) == "clears (+unvalidated)"


# --- end-to-end (one compute, shared) -------------------------------------- #

@pytest.fixture(scope="module")
def rows():
    return compute_scorecard(QUARTER)


def test_scorecard_covers_whole_book(rows):
    assert len(rows) == 22
    assert {r.ticker for r in rows} >= {"DHT", "SB", "BRUT", "TEN", "FLNG", "MPCC"}


def test_eleven_resale_uniform_comparable_set(rows):
    uniform = {r.ticker for r in rows if r.nav_basis == "resale-uniform"}
    # the 11 fully-corrected names (Thread 1 + Amendment B)
    assert uniform == {"DHT", "ECO", "FRO", "NAT", "TNK", "BRUT", "CAPT",
                       "CMDB", "GNK", "SB", "SBLK"}


def test_both_185_gates_pending_book_wide(rows):
    # No Baltic $/day series, no orderbook ratios in-repo ⇒ every name pending.
    assert all(r.gate_5a == "pending" for r in rows)
    assert all(r.gate_5b == "pending" for r in rows)


def test_pending_not_passed_flagged_names_are_not_resale_uniform(rows):
    by = {r.ticker: r for r in rows}
    assert by["INSW"].nav_basis == "pending-sourceable"      # holds LR1
    assert by["TEN"].nav_basis == "structural-unavailable"   # holds LNGC
    assert by["FLNG"].nav_basis == "structural-unavailable"
    # SB (the canary) is on the uniform basis and cheap on both bases.
    assert by["SB"].nav_basis == "resale-uniform" and by["SB"].robust == "robust"


def test_crude_parity_bands_clear(rows):
    for t in ("DHT", "FRO", "NAT"):
        r = next(x for x in rows if x.ticker == t)
        assert r.parity_band.startswith("clears")


def test_write_scorecard_emits_matrix(tmp_path, rows):
    path = write_scorecard(rows, outputs_dir=tmp_path)
    text = path.read_text()
    assert path.name == "book_scorecard.md"
    assert "Book-wide validation scorecard" in text
    assert "comparability boundary" in text
    assert "registered-PENDING" in text
    assert "| DHT |" in text and "| SB |" in text
