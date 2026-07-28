"""The COMMITTED earnings calendar (WO2 2.1) — completeness vs the watchlist,
the R-5 meta/names shape, and per-entry field discipline. The 2026-07-03 full
vet (decisions/earnings_calendar_vet_2026-07-03.md) closed the CMBT/SB gaps,
so completeness is now a hard invariant, suite-enforced."""

from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

VALID_STATUS = {"confirmed", "expected"}


def _doc():
    return yaml.safe_load((ROOT / "inputs" / "earnings_calendar.yaml").read_text())


def test_calendar_shape_is_meta_plus_names():
    doc = _doc()
    assert set(doc) == {"meta", "names"}, (
        "R-5: file metadata lives in meta:, tickers under names: — "
        f"stray top-level keys: {set(doc) - {'meta', 'names'}}")
    assert doc["meta"]["quarter"] and doc["meta"]["vetted"]


def test_every_watchlist_name_is_seeded():
    watch = yaml.safe_load((ROOT / "inputs" / "watchlist.yaml").read_text())
    names = _doc()["names"]
    missing = [t for t in watch if t not in names]
    assert not missing, f"watchlist names with no calendar entry: {missing}"


def test_entries_carry_the_vetted_fields():
    for ticker, e in _doc()["names"].items():
        assert isinstance(e.get("window_start"), date), ticker
        end = e.get("window_end") or e["window_start"]
        assert isinstance(end, date) and end >= e["window_start"], ticker
        assert e.get("status") in VALID_STATUS, f"{ticker}: status {e.get('status')}"
        assert e.get("basis"), f"{ticker}: empty basis (provenance rule)"
        assert e.get("disclosure_type"), f"{ticker}: no disclosure_type"
        assert e.get("venue"), f"{ticker}: no venue"
        # confirmed = a company-announced date; the basis must say where.
        if e["status"] == "confirmed":
            assert any(w in e["basis"].lower() for w in
                       ("calendar", "announc", "newsweb", "newspoint", "mfn", "pr ")), \
                f"{ticker}: confirmed without a citable announcement in basis"


def test_meta_date_fields_are_real_dates():
    """Every meta date must parse as a date, not a string.

    The sentinel does date arithmetic on `meta.last_date_sweep`
    (`(today - sweep_stamp).days` in `_filing_event_flags`), so a hand-written
    "YYYY-MM-DD" string crashes the daily digest at runtime while the rest of
    the suite stays green — the entry-level guard above only covers
    `names.*.window_*`. Caught 2026-07-28 after a date sweep wrote the field
    as a string; the crash would have taken out the next morning's digest.
    """
    meta = _doc()["meta"]
    for field in ("last_date_sweep", "vetted"):
        if field in meta:
            assert isinstance(meta[field], date), (
                f"meta.{field} is {type(meta[field]).__name__}, not a date — "
                "the sentinel does arithmetic on it (quote-free YAML: 2026-07-28)"
            )
