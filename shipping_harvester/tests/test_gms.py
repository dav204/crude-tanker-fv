"""GMS parser tests. Fixture mirrors GMS's canonical demo-rankings format with
invented numbers, plus decoy steel/oil prices that must NOT be captured.

Run:  pytest -q tests/test_gms.py
"""
from __future__ import annotations

import datetime as dt

from shipping_harvester.models import ReportRef
from shipping_harvester.parse import get_parser
from shipping_harvester.parse.gms import GmsParser


GMS_TEXT = (
    "GMS WEEKLY SHIP RECYCLING DEMO RANKINGS\n"
    "Bangladesh Sentiment: Strong Gen Cargo (Dry): USD 460-465/LT LDT "
    "Tankers (Wet): USD 480-485/LT LDT Containers: USD 470-475/LT LDT\n"
    "India Sentiment: Steady Gen Cargo (Dry): USD 420-425/LT LDT "
    "Tankers (Wet): USD 440-445/LT LDT\n"
    "Pakistan Sentiment: Steady Gen Cargo (Dry): USD 445-450/LT LDT "
    "Tankers (Wet): USD 465-470/LT LDT\n"
    "Turkey Sentiment: Steady Gen Cargo (Dry): USD 268-270/LT LDT "
    "Tankers (Wet): USD 278-280/LT LDT\n"
    "Local steel plate prices fell by USD 9 per ton to USD 540. "
    "Oil prices slipped to USD 62 per barrel.\n"
)


def test_gms_extracts_per_market_per_type_midpoints():
    marks = GmsParser().extract([], GMS_TEXT)
    got = {(m.note, m.vessel_class): m.value for m in marks}

    # ranges -> midpoints
    assert got[("bangladesh", "Dry")] == 462.5
    assert got[("bangladesh", "Tanker")] == 482.5
    assert got[("bangladesh", "Container")] == 472.5
    assert got[("india", "Dry")] == 422.5
    assert got[("india", "Tanker")] == 442.5
    assert got[("pakistan", "Tanker")] == 467.5
    assert got[("turkey", "Dry")] == 269.0

    # India had no container line -> no container mark for india
    assert ("india", "Container") not in got
    # everything is a $/ldt demolition mark
    assert all(m.kind == "demolition" and m.unit == "usd_per_ldt" for m in marks)


def test_gms_ignores_steel_and_oil_prices():
    """Steel ($540/ton) and oil ($62/barrel) are not LDT-anchored, so no mark
    should carry those values."""
    values = {m.value for m in GmsParser().extract([], GMS_TEXT)}
    assert 540.0 not in values
    assert 62.0 not in values
    # and no demolition mark should land outside the four real markets
    markets = {m.note for m in GmsParser().extract([], GMS_TEXT)}
    assert markets <= {"bangladesh", "india", "pakistan", "turkey"}


def test_gms_single_value_not_range():
    text = "Bangladesh Gen Cargo (Dry): USD 410/LDT Tankers (Wet): USD 430/LDT\n"
    got = {(m.note, m.vessel_class): m.value for m in GmsParser().extract([], text)}
    assert got[("bangladesh", "Dry")] == 410.0
    assert got[("bangladesh", "Tanker")] == 430.0


def _make_gms_pdf(path):
    from reportlab.platypus import SimpleDocTemplate, Preformatted
    from reportlab.lib.styles import ParagraphStyle

    text = (
        "GMS WEEKLY DEMO RANKINGS\n"
        "Bangladesh Gen Cargo (Dry): USD 460/LT LDT Tankers (Wet): USD 480/LT LDT\n"
        "India Gen Cargo (Dry): USD 420/LT LDT Tankers (Wet): USD 440/LT LDT\n"
        "Steel plate USD 540 per ton. Oil USD 62 per barrel.\n"
    )
    style = ParagraphStyle("gms", fontName="Courier", fontSize=7, leading=9)
    SimpleDocTemplate(str(path)).build([Preformatted(text, style)])


def test_gms_parser_end_to_end(tmp_path):
    pdf = tmp_path / "gms_sample.pdf"
    _make_gms_pdf(pdf)

    parser = get_parser("gms")
    assert parser.broker_id == "gms"
    ref = ReportRef("gms", "capitallink", "GMS Weekly", "http://x", str(pdf),
                    dt.date(2026, 6, 12))
    mm = parser.parse(pdf, ref)

    assert mm.parser_ok
    got = {(m.note, m.vessel_class): m.value for m in mm.marks}
    assert got[("bangladesh", "Tanker")] == 480.0
    assert got[("india", "Dry")] == 420.0
    assert 540.0 not in {m.value for m in mm.marks}
