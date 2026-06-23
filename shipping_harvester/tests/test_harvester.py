"""Network-independent tests. Validates the logic that doesn't need live sites:
quarter keying, dedupe, broker attribution, PDF-link extraction, and an
end-to-end parse against a PDF we synthesise on the fly.

Run:  pytest -q
"""
from __future__ import annotations

import datetime as dt

import pytest

from shipping_harvester import config, quarters
from shipping_harvester.crawl import _extract_pdf_url
from shipping_harvester.download import dedupe
from shipping_harvester.models import ReportRef
from shipping_harvester.parse import get_parser
from shipping_harvester.parse import base


def ref(broker, d, pdf="http://x/p.pdf"):
    return ReportRef(broker, "hsn", f"{broker} weekly", "http://x/post", pdf, d)


# --- quarters ---------------------------------------------------------------
def test_quarter_of_and_end():
    assert quarters.quarter_of(dt.date(2026, 4, 1)) == "2026Q2"
    assert quarters.quarter_of(dt.date(2026, 6, 30)) == "2026Q2"
    assert quarters.quarter_end("2026Q2") == dt.date(2026, 6, 30)
    assert quarters.quarter_end("2024Q1") == dt.date(2024, 3, 31)  # not a leap edge
    assert quarters.quarter_start("2026Q3") == dt.date(2026, 7, 1)


def test_quarter_range():
    assert quarters.quarter_range("2025Q3", "2026Q2") == [
        "2025Q3", "2025Q4", "2026Q1", "2026Q2",
    ]
    with pytest.raises(ValueError):
        quarters.quarter_range("2026Q2", "2025Q1")


def test_select_for_quarter_picks_latest_on_or_before_qend():
    refs = [
        ref("allied", dt.date(2026, 6, 22)),   # in-quarter, latest <= 6/30
        ref("allied", dt.date(2026, 6, 8)),
        ref("allied", dt.date(2026, 7, 6)),    # after q-end, must be ignored
        ref("intermodal", dt.date(2026, 3, 31)),  # stale for Q2 (no fresh issue)
    ]
    chosen = quarters.select_for_quarter(refs, "2026Q2", stale_after_days=14)
    allied_ref, allied_stale = chosen["allied"]
    assert allied_ref.published == dt.date(2026, 6, 22)
    assert allied_stale is False
    inter_ref, inter_stale = chosen["intermodal"]
    assert inter_ref.published == dt.date(2026, 3, 31)
    assert inter_stale is True  # reached back across the quarter boundary


# --- dedupe & attribution ---------------------------------------------------
def test_dedupe_collapses_same_broker_week_prefers_pdf():
    d = dt.date(2026, 6, 10)
    a = ref("allied", d, pdf=None)
    b = ref("allied", d, pdf="http://x/real.pdf")
    out = dedupe([a, b])
    assert len(out) == 1
    assert out[0].pdf_url == "http://x/real.pdf"  # the one with a PDF wins


@pytest.mark.parametrize("title,expected", [
    ("Allied Weekly S&P Statistics – WEEK 50", "allied"),
    ("Intermodal Weekly Market Report Week 51 2025", "intermodal"),
    ("Xclusiv Shipbrokers Weekly 01st June 2026", "xclusiv"),
    ("Charles R. Weber – Weber Weekly Tanker Report – Week 53", "weber"),
    ("Fearnleys Weekly Report Week 34", "fearnleys"),
    ("Some Unrelated Maritime News", None),
])
def test_identify_broker(title, expected):
    b = config.identify_broker(title)
    assert (b.broker_id if b else None) == expected


# --- pdf link extraction ----------------------------------------------------
def test_extract_pdf_url_prefers_pdf_href():
    html = '<div><a href="/wp-content/uploads/2026/06/allied_w24.pdf">Download PDF</a></div>'
    assert _extract_pdf_url(html, "https://capitallinkshipping.com").endswith(
        "/wp-content/uploads/2026/06/allied_w24.pdf"
    )


def test_extract_pdf_url_falls_back_to_download_text():
    html = '<a href="https://cdn.example.com/report?id=9">DOWNLOAD report</a>'
    assert _extract_pdf_url(html, "https://x") == "https://cdn.example.com/report?id=9"


# --- value cleaning ---------------------------------------------------------
@pytest.mark.parametrize("s,expected", [
    ("$ 92.5m", 92.5),
    ("45,000 /day", 45000.0),
    ("40-45", 42.5),        # range -> midpoint
    ("n/a", None),
])
def test_clean_num(s, expected):
    assert base.clean_num(s) == expected


def test_map_value_table_single_header_row():
    table = [
        ["Vessel", "Resale", "5 year", "10 year"],
        ["VLCC", "$129.0m", "105.0", "80.0"],
        ["Suezmax", "86.0", "72.0", "58.0"],
    ]
    marks = base.map_value_table(
        table,
        {"newbuild": ["resale"], "five_year": ["5 year"], "ten_year": ["10 year"]},
        kind="vessel_value", metric="value", unit="musd",
    )
    got = {(m.vessel_class, m.age_anchor): m.value for m in marks}
    assert got[("VLCC", "newbuild")] == 129.0
    assert got[("Suezmax", "five_year")] == 72.0
    assert got[("VLCC", "ten_year")] == 80.0


# --- end-to-end parse against a synthesised PDF -----------------------------
def _make_values_pdf(path):
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

    data = [
        ["Vessel", "Resale Value", "5 year", "10 year"],
        ["Suezmax", "92.5", "82.0", "70.0"],
        ["Aframax", "78.0", "68.0", "60.0"],
        ["MR", "45.0", "40.0", "33.0"],
    ]
    t = Table(data)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.black)]))
    SimpleDocTemplate(str(path)).build([t])


def _make_allied_weekly_pdf(path):
    """Allied Weekly Market Report layout: an 'Indicative … Values' section with a
    class-header line, then per-dwt age rows (Resale / 5 / 10 / 15 year old)."""
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Preformatted, SimpleDocTemplate

    text = (
        "Indicative Tanker Values (US$ million)\n"
        "                       08 May   03 Apr   +/-\n"
        "Suezmax\n"
        "160k dwt     Resale       92.5    90.0   2.0%\n"
        "150k dwt 5 year old       82.0    80.0   2.5%\n"
        "150k dwt 10 year old      70.0    68.0   2.9%\n"
        "150k dwt 15 year old      48.0    47.0   2.1%\n"
        "Aframax\n"
        "110k dwt     Resale       78.0    77.0   1.3%\n"
        "105k dwt 10 year old      60.0    59.0   1.7%\n"
        "MR\n"
        "52k dwt      Resale       45.0    44.0   2.3%\n"
    )
    style = getSampleStyleSheet()["Code"]
    SimpleDocTemplate(str(path)).build([Preformatted(text, style)])


def test_allied_parser_end_to_end(tmp_path):
    pdf = tmp_path / "allied_sample.pdf"
    _make_allied_weekly_pdf(pdf)

    parser = get_parser("allied")
    assert parser.broker_id == "allied"
    mm = parser.parse(pdf, ref("allied", dt.date(2026, 6, 20)))

    assert mm.parser_ok
    assert mm.quarter == "2026Q2"
    got = {(m.vessel_class, m.age_anchor): m.value for m in mm.marks}
    assert got[("Suezmax", "five_year")] == 82.0
    assert got[("Aframax", "ten_year")] == 60.0
    assert got[("MR", "resale")] == 45.0  # Resale -> 'resale' (build_vintage maps it to the newbuild proxy)


def _make_xclusiv_flat_pdf(path):
    """Xclusiv 2021-2023 'flat-row' secondhand layout: class+dwt+age per line."""
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Preformatted, SimpleDocTemplate

    text = (
        "DRY NEWBUILDING PRICES (in USD mills)\n"
        "Capesize         63.0     58.0     9%\n"
        "WET SECONDHAND PRICES (in USD mills)\n"
        "Size            Jun/22   Jun/21\n"
        "VLCC 320k Resale    101.5    95.3   7%\n"
        "VLCC 320k 5y         76.8    70.3   9%\n"
        "VLCC 300k 10y        52.4    48.3   9%\n"
        "Suezmax 160k Resale  72.8    65.3  12%\n"
        "Suezmax 150k 10y     37.4    32.3  16%\n"
    )
    style = getSampleStyleSheet()["Code"]
    SimpleDocTemplate(str(path)).build([Preformatted(text, style)])


def test_xclusiv_flat_row_era(tmp_path):
    pdf = tmp_path / "xclusiv_2022.pdf"
    _make_xclusiv_flat_pdf(pdf)
    parser = get_parser("xclusiv")
    mm = parser.parse(pdf, ref("xclusiv", dt.date(2022, 6, 28)))
    assert mm.parser_ok
    got = {(m.vessel_class, m.age_anchor): m.value for m in mm.marks}
    assert got[("VLCC", "resale")] == 101.5
    assert got[("VLCC", "ten_year")] == 52.4
    assert got[("Suezmax", "resale")] == 72.8
    assert got[("Capesize", "newbuild")] == 63.0  # dry NB from the section


def test_generic_parser_records_but_extracts_nothing(tmp_path):
    pdf = tmp_path / "x.pdf"
    _make_values_pdf(pdf)
    parser = get_parser("braemar")  # no parser implemented -> generic
    mm = parser.parse(pdf, ref("braemar", dt.date(2026, 6, 20)))
    assert parser.broker_id == "generic"
    assert mm.parser_ok is False
    assert mm.marks == []
    assert mm.raw_text_chars > 0  # text layer was read
