"""The Q2 cluster transition mechanism (ruled 2026-08-08 — decisions/
q2_cluster_transition_2026-07-31.md, Decision block).

Balance sheets are quarter-keyed files; fleet manifests are one
quarter-agnostic file each. On 2026-07-31 three per-name Q2 refreshes ran on
the 2026-Q1 book and applied only the ASSET half (ASC printed +16.9% with its
$183.6M commitment invisible; paired inputs give ≈ −2.9%). Two mechanisms,
both here:

- the LOADER-VINTAGE FALLBACK: ``resolve_balance_sheet_path`` returns the
  newest sheet at-or-before the run quarter and self-reports the vintage;
- the ATOMIC-QUARTER (pair) GUARD: ``load_company_inputs`` hard-fails when
  the manifest's quarter label disagrees with the resolved sheet vintage.

The four case rows from the ruled proposal are the named tests below.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

from crude_tanker_fv.loaders import (
    INPUTS_DIR,
    current_book_quarter,
    load_balance_sheet,
    load_company_inputs,
    load_fleet_manifest,
    load_watchlist,
    preflight_pair_coherence,
    resolve_balance_sheet_path,
)

ROOT = Path(__file__).resolve().parents[1]


# ---------------------------------------------------------------- fixtures

@pytest.fixture()
def inputs_copy(tmp_path):
    """A minimal writable copy of inputs/ — market data + the ASC and DHT
    artefact sets (ASC has a staged Q2 sheet; DHT is Q1-only)."""
    dst = tmp_path / "inputs"
    (dst / "fleet_manifests").mkdir(parents=True)
    (dst / "balance_sheets").mkdir()
    shutil.copytree(INPUTS_DIR / "market_data", dst / "market_data")
    for t in ("asc", "dht"):
        shutil.copy(INPUTS_DIR / "fleet_manifests" / f"{t}.yaml",
                    dst / "fleet_manifests" / f"{t}.yaml")
        for bs in (INPUTS_DIR / "balance_sheets").glob(f"{t}_*.yaml"):
            shutil.copy(bs, dst / "balance_sheets" / bs.name)
        for aux in ("cost_structures", "dividend_policies"):
            src = INPUTS_DIR / aux / f"{t}.yaml"
            if src.exists():
                (dst / aux).mkdir(exist_ok=True)
                shutil.copy(src, dst / aux / f"{t}.yaml")
    return dst


def _set_manifest_quarter(inputs_dir: Path, ticker: str, quarter: str) -> None:
    """Force the fixture manifest's label — regex on whatever the tree carries,
    so these tests survive the book's quarter rolls."""
    import re

    p = inputs_dir / "fleet_manifests" / f"{ticker}.yaml"
    doc, n = re.subn(r"(?m)^report_date: \S+", f"report_date: {quarter}", p.read_text())
    assert n == 1
    p.write_text(doc)


def _drop_sheets_after(inputs_dir: Path, ticker: str, quarter: str) -> None:
    """Remove fixture sheets keyed after ``quarter`` so a case can pin the
    no-newer-sheet world regardless of what the real tree has staged."""
    for p in (inputs_dir / "balance_sheets").glob(f"{ticker}_*.yaml"):
        if p.stem.rpartition("_")[2] > quarter:
            p.unlink()


# ------------------------------------------- the four ruled case rows (B)

def test_case_row_1_the_asc_incident_manifest_ahead_on_old_run(inputs_copy):
    """Manifest Q2 + Q1 run (exact Q1 sheet) → hard fail naming both vintages."""
    _set_manifest_quarter(inputs_copy, "asc", "2026-Q2")
    with pytest.raises(ValueError, match="2026-Q2.*2026-Q1|as-of 2026-Q2"):
        load_company_inputs("ASC", "2026-Q1", inputs_copy)


def test_case_row_2_rolling_reported_name_passes(inputs_copy):
    """Manifest Q2 + Q2 run with the staged Q2 sheet → coherent pass."""
    _set_manifest_quarter(inputs_copy, "asc", "2026-Q2")
    ci = load_company_inputs("ASC", "2026-Q2", inputs_copy)
    assert ci.balance_sheet.quarter == "2026-Q2"


def test_case_row_3_rolling_unreported_name_falls_back_disclosed(inputs_copy):
    """Manifest Q1 + Q2 run, no Q2 sheet → Q1 pair via fallback, self-reported."""
    _set_manifest_quarter(inputs_copy, "dht", "2026-Q1")
    _drop_sheets_after(inputs_copy, "dht", "2026-Q1")
    ci = load_company_inputs("DHT", "2026-Q2", inputs_copy)
    assert ci.balance_sheet.quarter == "2026-Q1"
    assert ci.fleet.report_date == "2026-Q1"


def test_case_row_4_manifest_edited_sheet_not(inputs_copy):
    """Manifest bumped to Q2, no Q2 sheet anywhere → fallback resolves Q1 → fail."""
    _set_manifest_quarter(inputs_copy, "dht", "2026-Q2")
    _drop_sheets_after(inputs_copy, "dht", "2026-Q1")
    with pytest.raises(ValueError, match="half|as-of 2026-Q2"):
        load_company_inputs("DHT", "2026-Q2", inputs_copy)


def test_mirror_case_sheet_ahead_of_manifest(inputs_copy):
    """Staged Q2 sheet + manifest still Q1, run at Q2 → exact Q2 sheet wins
    resolution → pair guard fails (liability half ahead of asset half — the
    mirror of the incident; the tree's real state between 7/31 and the 8/08
    transition)."""
    _set_manifest_quarter(inputs_copy, "asc", "2026-Q1")
    with pytest.raises(ValueError, match="as-of 2026-Q1"):
        load_company_inputs("ASC", "2026-Q2", inputs_copy)


# ------------------------------------------------------- resolver (A)

def test_exact_match_wins_and_no_forward_reads(inputs_copy):
    path, vintage = resolve_balance_sheet_path("asc", "2026-Q1", inputs_copy)
    assert vintage == "2026-Q1" and path.name == "asc_2026-Q1.yaml"
    bs = load_balance_sheet("asc", "2026-Q1", inputs_copy)
    assert bs.quarter == "2026-Q1"  # the staged Q2 sheet never leaks backward


def test_fallback_resolves_newest_at_or_before(inputs_copy):
    _, vintage = resolve_balance_sheet_path("asc", "2026-Q3", inputs_copy)
    assert vintage == "2026-Q2"
    _, vintage = resolve_balance_sheet_path("dht", "2026-Q4", inputs_copy)
    assert vintage == "2026-Q1"


def test_nothing_at_or_before_raises_filenotfound(inputs_copy):
    with pytest.raises(FileNotFoundError, match="at or before 2025-Q4"):
        resolve_balance_sheet_path("dht", "2025-Q4", inputs_copy)


def test_mislabeled_sheet_hard_fails(inputs_copy):
    """A file keyed Q2 whose content declares Q1 would silently mislabel every
    vintage disclosure — it must fail at the named file, not resolve."""
    q1 = (inputs_copy / "balance_sheets" / "dht_2026-Q1.yaml").read_text()
    (inputs_copy / "balance_sheets" / "dht_2026-Q2.yaml").write_text(q1)
    with pytest.raises(ValueError, match="keyed 2026-Q2 but declares"):
        load_balance_sheet("dht", "2026-Q2", inputs_copy)


# ------------------------------------------------- repo-wide sweeps

def test_every_committed_sheet_declares_its_own_key():
    """Mislabels are only caught at resolution time, so a mislabeled FUTURE-
    keyed sheet would detonate at the transition regen — the worst moment.
    Sweep the whole directory instead (vet 2026-08-08)."""
    bad = []
    for p in sorted((INPUTS_DIR / "balance_sheets").glob("*_*.yaml")):
        if p.name.startswith("_"):
            continue
        stem_ticker, _, key = p.stem.rpartition("_")
        declared = str(yaml.safe_load(p.read_text()).get("quarter"))
        if declared != key:
            bad.append(f"{p.name}: declares {declared}")
        if str(yaml.safe_load(p.read_text()).get("ticker")).lower() != stem_ticker:
            bad.append(f"{p.name}: ticker mismatch")
    assert not bad, bad


def test_sheets_from_2026_q2_carry_ingest_provenance():
    """The vintage guards check labels against labels; the provenance trio is
    the one anchor OUTSIDE the repo (owner ruling 2026-08-08). Required from
    2026-Q2 sheets on; Q1-and-earlier keep header-comment citations."""
    missing = []
    for p in sorted((INPUTS_DIR / "balance_sheets").glob("*_*.yaml")):
        if p.name.startswith("_"):
            continue
        key = p.stem.rpartition("_")[2]
        if key < "2026-Q2":
            continue
        doc = yaml.safe_load(p.read_text())
        for f in ("source_url", "retrieved_at", "filing_period_end"):
            if not doc.get(f):
                missing.append(f"{p.name}: {f}")
    assert not missing, missing


def test_whole_book_pairs_coherent_at_the_committed_quarter():
    """Every watchlist name's manifest label must match its resolved sheet
    vintage at the book's committed quarter — the invariant every transition
    preserves name-by-name. The quarter comes from the COMMITTED scorecard
    (tracked in git), so this test rolls with the book instead of pinning a
    constant that reds at each transition."""
    import json

    committed_quarter = json.loads(
        (ROOT / "outputs" / "book_scorecard.json").read_text())["quarter"]
    for ticker in load_watchlist():
        fleet = load_fleet_manifest(ticker)
        _, vintage = resolve_balance_sheet_path(ticker, committed_quarter)
        assert fleet.report_date == vintage, ticker


# ------------------------------------------------- preflight + defaults

def test_preflight_clean_at_the_book_quarter_and_flags_the_stale_quarter():
    """The book quarter is ALWAYS preflight-clean, and the PRIOR quarter must
    refuse for exactly the names whose manifests advanced to the book quarter
    (their prior sheets still exist and exact-resolve against a moved-on
    manifest). Both sets derive from the tree, so the rolling backlog drain
    doesn't re-pin this test at every per-name refresh (2026-08-08: the ECO
    refresh grew the advanced set from {ASC, SB, TNK} within hours)."""
    import json

    book = json.loads((ROOT / "outputs" / "book_scorecard.json").read_text())["quarter"]
    assert preflight_pair_coherence(book) == []
    y, q = int(book[:4]), int(book[-1])
    prior = f"{y - 1}-Q4" if q == 1 else f"{y}-Q{q - 1}"
    advanced = {t for t in load_watchlist()
                if load_fleet_manifest(t).report_date == book}
    flagged = {p.split(":")[0] for p in preflight_pair_coherence(prior)}
    assert advanced and flagged == advanced


def test_current_book_quarter_reads_state(tmp_path):
    f = tmp_path / "last_run.json"
    f.write_text('{"quarter": "2026-Q1"}')
    assert current_book_quarter(f) == "2026-Q1"
    f.write_text('{"quarter": "garbage"}')
    assert current_book_quarter(f) is None
    assert current_book_quarter(tmp_path / "absent.json") is None


# ------------------------------------------------- scorecard disclosure

def test_balance_sheet_basis_summary_lagging_and_current():
    from crude_tanker_fv.scorecard import balance_sheet_basis_summary

    s = balance_sheet_basis_summary("2026-Q2", ["SB", "DHT", "TNK"])
    assert s["lagging"] == {"DHT": "2026-Q1"} and s["missing"] == []
    s = balance_sheet_basis_summary("2026-Q1", ["SB", "DHT", "TNK"])
    assert s["lagging"] == {} and s["total"] == 3


def test_balance_sheet_basis_summary_missing_lane():
    """`missing` must be reachable — the summary runs over the WATCHLIST, not
    the surviving scorecard rows (review catch 2026-08-08): a name with no
    resolvable sheet vanishes from names[] and this list is its only trace."""
    from crude_tanker_fv.scorecard import balance_sheet_basis_summary

    s = balance_sheet_basis_summary("2026-Q1", ["SB", "ZZZ"])
    assert s["missing"] == ["ZZZ"] and s["lagging"] == {}
