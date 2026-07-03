"""Arrival validation at staging (WO2 1.5, invariant 6): good PDFs stage +
ledger; garbage quarantines with a reason file + ledger line — never sits in
the archive looking like data."""

import json
from pathlib import Path

from pypdf import PdfWriter

from crude_tanker_fv.arrivals import record_arrival, stage_pdf, validate_pdf


def _good_pdf(path: Path) -> Path:
    w = PdfWriter()
    w.add_blank_page(width=72, height=72)
    with path.open("wb") as fh:
        w.write(fh)
    return path


def test_valid_pdf_stages_and_ledgers(tmp_path):
    pdf = _good_pdf(tmp_path / "daily.pdf")
    ok, final = stage_pdf(pdf, "pareto-daily", "msg-123", state_dir=tmp_path / "state")
    assert ok and final == pdf and pdf.exists()
    line = json.loads((tmp_path / "state" / "arrivals.jsonl").read_text())
    assert line["disposition"] == "staged" and line["identity"] == "msg-123"


def test_garbage_quarantines_with_reason(tmp_path):
    junk = tmp_path / "daily.pdf"
    junk.write_bytes(b"<html>404 not found</html>")
    ok, final = stage_pdf(junk, "pareto-daily", "msg-666", state_dir=tmp_path / "state")
    assert not ok
    assert not junk.exists()
    assert final == tmp_path / "_quarantine" / "daily.pdf" and final.exists()
    assert "no %PDF magic" in (final.parent / "daily.pdf.reason").read_text()
    line = json.loads((tmp_path / "state" / "arrivals.jsonl").read_text())
    assert line["disposition"] == "quarantined"


def test_truncated_pdf_fails_open(tmp_path):
    broken = tmp_path / "cut.pdf"
    broken.write_bytes(b"%PDF-1.4\ngarbage that is not a pdf body")
    ok, note = validate_pdf(broken)
    assert not ok


def test_ledger_appends(tmp_path):
    record_arrival("edgar", "0001234567-26-000001", "staged",
                   state_dir=tmp_path / "state")
    record_arrival("edgar", "0001234567-26-000001", "duplicate",
                   state_dir=tmp_path / "state")
    lines = (tmp_path / "state" / "arrivals.jsonl").read_text().strip().splitlines()
    assert len(lines) == 2
    assert json.loads(lines[1])["disposition"] == "duplicate"
