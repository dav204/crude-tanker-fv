"""Smoke tests for the /add-ticker scaffold itself.

Tests run against a temp-copy of the repo's templates so we don't dirty the
real inputs/ tree. The contract: scaffold produces files, refuses to
overwrite, and emits warnings (not errors) for new sectors.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from crude_tanker_fv import add_ticker


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def sandboxed_repo(tmp_path, monkeypatch):
    """Copy the templates + a stub watchlist into a tmp tree and point
    add_ticker at it. Yields the tmp ROOT."""
    for sub in ("inputs/fleet_manifests", "inputs/balance_sheets",
                "inputs/cost_structures", "inputs/dividend_policies",
                "tests", "decisions", "state"):
        (tmp_path / sub).mkdir(parents=True)

    # Copy real templates so substitution paths match production.
    for sub in ("fleet_manifests", "balance_sheets",
                "cost_structures", "dividend_policies"):
        src = ROOT / "inputs" / sub / "_template.yaml"
        if src.exists():
            shutil.copy(src, tmp_path / "inputs" / sub / "_template.yaml")

    # Stub watchlist (the scaffold appends; don't need real entries).
    (tmp_path / "inputs" / "watchlist.yaml").write_text(
        "# stub watchlist\nDHT:\n  current_price: 16.40\n"
    )

    monkeypatch.setattr(add_ticker, "ROOT", tmp_path)
    monkeypatch.setattr(add_ticker, "INPUTS", tmp_path / "inputs")
    monkeypatch.setattr(add_ticker, "TESTS", tmp_path / "tests")
    monkeypatch.setattr(add_ticker, "DECISIONS", tmp_path / "decisions")
    return tmp_path


def test_scaffold_creates_all_files(sandboxed_repo):
    rc = add_ticker.scaffold("SBLK", "dry_bulk", "2026-Q1", force=False, dry_run=False)
    assert rc == 0
    expected = [
        "inputs/fleet_manifests/sblk.yaml",
        "inputs/balance_sheets/sblk_2026-Q1.yaml",
        "inputs/cost_structures/sblk.yaml",
        "inputs/dividend_policies/sblk.yaml",
        "tests/test_sblk.py",
        "decisions/sblk_log.md",
    ]
    for rel in expected:
        assert (sandboxed_repo / rel).exists(), f"missing {rel}"


def test_scaffold_appends_watchlist_row_without_destroying_existing(sandboxed_repo):
    add_ticker.scaffold("SBLK", "dry_bulk", "2026-Q1", force=False, dry_run=False)
    wl = (sandboxed_repo / "inputs" / "watchlist.yaml").read_text()
    assert "DHT:" in wl, "existing entry got clobbered"
    assert "\nSBLK:" in wl, "new entry not appended"
    assert "sector: dry_bulk" in wl


def test_scaffold_refuses_to_overwrite_without_force(sandboxed_repo):
    add_ticker.scaffold("SBLK", "dry_bulk", "2026-Q1", force=False, dry_run=False)
    rc = add_ticker.scaffold("SBLK", "dry_bulk", "2026-Q1", force=False, dry_run=False)
    assert rc == 1, "second scaffold should refuse without --force"


def test_dry_run_writes_nothing(sandboxed_repo):
    rc = add_ticker.scaffold("SBLK", "dry_bulk", "2026-Q1", force=False, dry_run=True)
    assert rc == 0
    assert not (sandboxed_repo / "inputs" / "fleet_manifests" / "sblk.yaml").exists()


def test_test_stub_carries_skip_marker(sandboxed_repo):
    add_ticker.scaffold("SBLK", "dry_bulk", "2026-Q1", force=False, dry_run=False)
    test_text = (sandboxed_repo / "tests" / "test_sblk.py").read_text()
    assert "pytest.mark.skip" in test_text, "stub should skip until data is filled in"


def test_fleet_manifest_uses_sector_appropriate_classes(sandboxed_repo):
    add_ticker.scaffold("SBLK", "dry_bulk", "2026-Q1", force=False, dry_run=False)
    fleet = (sandboxed_repo / "inputs" / "fleet_manifests" / "sblk.yaml").read_text()
    # dry_bulk → Cape / Pana / Supra / Ultra (not VLCC / Suezmax / etc.)
    assert "Cape" in fleet
    assert "VLCC" not in fleet


def test_existing_sector_keeps_canonical_classes(sandboxed_repo):
    add_ticker.scaffold("NEWNAME", "crude", "2026-Q1", force=False, dry_run=False)
    fleet = (sandboxed_repo / "inputs" / "fleet_manifests" / "newname.yaml").read_text()
    assert "VLCC" in fleet


def test_balance_sheet_stub_declares_clean_ticker_and_quarter():
    """The 2026-08-08 regression class: a substring replace that ends inside a
    template comment leaves the comment's tail BARE on the value line — every
    scaffolded sheet is then born mislabeled and the vintage guards refuse the
    book. The stub must parse clean against the REAL template."""
    import yaml

    doc = yaml.safe_load(add_ticker._balance_sheet_stub("GASS", "2026-Q2"))
    assert doc["ticker"] == "GASS"
    assert doc["quarter"] == "2026-Q2"
