"""Charles R. Weber parser tests. Fixture mirrors the real WM02-25 page-2
TANKER ROUTES structure (two-column: TC callouts on the right) with invented
numbers, so it's clearly synthetic.

Run:  pytest -q tests/test_weber.py
"""
from __future__ import annotations

import datetime as dt

from shipping_harvester.models import ReportRef
from shipping_harvester.parse import get_parser
from shipping_harvester.parse.weber import WeberParser


# page-2 fixture: note the two-column interleave -- the "Time Charter ..." label
# ends a route row and its values end the NEXT route row (after that row's own
# route TCEs). The Average Earnings values sit on the line after their label.
WEBER_PAGE2 = "\n".join([
    "TANKER ROUTES (13kts L|B) Week 1 Week 2 Week 1 Week 2",
    "VLCC WS|L$ WS|L$ TCE* TCE** VLSFO $568/MTD",
    "AG>USG 280,000 27.50 28.50 -- --",
    "AG>SPORE 270,000 41.50 45.50 $17,089 $21,766 Time Charter 1 Year v. 3 Years ($|day):",
    "AG>JPN 265,000 39.50 43.50 $14,290 $18,951 $45,000 $47,000",
    "WAFR>CHINA 260,000 47.60 49.00 $22,857 $24,059 # Ships Trading: 902",
    "VLCC Average Earnings +",
    "-- -- $17,283 $20,490",
    "SUEZMAX",
    "WAFR>USG 130,000 65.00 61.00 $14,651 $11,652",
    "WAFR>UKC 130,000 70.00 66.00 $16,248 $13,156 Time Charter 1 Year v. 3 Years ($|day):",
    "BSEA>MED 140,000 79.70 77.60 $28,338 $26,083 $36,000 $38,000",
    "Suezmax Average Earnings +",
    "-- -- $18,970 $15,672",
    "AFRAMAX",
    "N.SEA>UKC 80,000 132.50 112.00 $66,977 $46,948",
    "BALT>UKC 100,000 N/A N/A N/A N/A Time Charter 1 Year v. 3 Years ($|day):",
    "CBS>USG 70,000 134.00 128.50 $26,283 $23,584 $33,500 $35,000",
    "Aframax Average Earnings +",
    "-- -- $41,982 $32,545",
    "THE WEEK IN CHARTS",
])


def test_weber_extract_spot_and_period():
    marks = WeberParser().extract([], WEBER_PAGE2)

    spot = {m.vessel_class: m.value for m in marks if m.kind == "spot_tce"}
    # latest (week-2) class Average Earnings, NOT a route TCE
    assert spot == {"VLCC": 20490.0, "Suezmax": 15672.0, "Aframax": 32545.0}

    tc1 = {m.vessel_class: m.value for m in marks
           if m.kind == "period_tc" and m.metric == "1yr_tc"}
    # the right-hand TC column, not the interleaved route TCEs ($14,290 etc.)
    assert tc1 == {"VLCC": 45000.0, "Suezmax": 36000.0, "Aframax": 33500.0}

    tc3 = {m.vessel_class: m.value for m in marks
           if m.kind == "period_tc" and m.metric == "3yr_tc"}
    assert tc3 == {"VLCC": 47000.0, "Suezmax": 38000.0, "Aframax": 35000.0}

    assert all(m.unit == "usd_per_day" for m in marks)


def test_weber_ignores_route_tce_for_benchmark():
    """Regression: 'first $ after the TC label' would wrongly capture the AG>JPN
    route TCE ($14,290). Confirm VLCC 1yr TC is the right-column $45,000."""
    marks = WeberParser().extract([], WEBER_PAGE2)
    vlcc_1yr = next(m.value for m in marks
                    if m.vessel_class == "VLCC" and m.metric == "1yr_tc")
    assert vlcc_1yr == 45000.0
    assert vlcc_1yr != 14290.0


def _make_weber_pdf(path):
    from reportlab.platypus import SimpleDocTemplate, Preformatted
    from reportlab.lib.styles import ParagraphStyle

    style = ParagraphStyle("wm", fontName="Courier", fontSize=7, leading=8)
    SimpleDocTemplate(str(path)).build([Preformatted(WEBER_PAGE2, style)])


def test_weber_parser_end_to_end(tmp_path):
    pdf = tmp_path / "weber_sample.pdf"
    _make_weber_pdf(pdf)

    parser = get_parser("weber")
    assert parser.broker_id == "weber"
    ref = ReportRef("weber", "capitallink", "Weber Weekly", "http://x", str(pdf),
                    dt.date(2025, 1, 10))
    mm = parser.parse(pdf, ref)

    assert mm.parser_ok
    assert mm.quarter == "2025Q1"
    spot = {m.vessel_class: m.value for m in mm.marks if m.kind == "spot_tce"}
    assert spot["VLCC"] == 20490.0
    tc1 = {m.vessel_class: m.value for m in mm.marks
           if m.kind == "period_tc" and m.metric == "1yr_tc"}
    assert tc1["Aframax"] == 33500.0
