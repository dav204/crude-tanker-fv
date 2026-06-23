"""Xclusiv parser tests. Fixtures mirror the structure of the real week-23
(08 Jun 2026) issue but use invented numbers, so they're clearly synthetic.

Run:  pytest -q tests/test_xclusiv.py
"""
from __future__ import annotations

import datetime as dt

from shipping_harvester.models import ReportRef
from shipping_harvester.parse import get_parser
from shipping_harvester.parse import base
from shipping_harvester.parse.xclusiv import XclusivParser, _AGE_LABELS


# --- spot TCE prose ---------------------------------------------------------
SPOT_TEXT = (
    "Capesize: C5TC average declined by USD 5.5k/day closing the week at "
    "USD 40,871/day. Transatlantic R/V is lower at USD 53,488/day. "
    "Kamsarmax/Panamax: P5TC Timecharter average started the week at "
    "USD 21,086/day closing with a decline at USD 20,121/day. "
    "Ultramax/Supramax: The Ultramax S11TC average closed at USD 20,067/day. "
    "The Supramax S10TC average closed at USD 18,033/day. "
    "Handysize: HS7TC average closed the week at USD 15,546/day. "
    "VLCC: average T/CE ended the week down by 4.1k/day at USD 193,873/day. "
    "Suezmax: average T/CE closed softer by 2.6k/day at USD 88,573/day. "
    "Aframax: average T/CE closed higher by 13.7k/day at USD 58,531/day. "
    "The MR Atlantic Basket is increased by 7.5k/day at USD 41,069/day."
)


def test_spot_skips_change_grabs_level():
    marks = XclusivParser._spot(SPOT_TEXT)
    got = {m.vessel_class: m.value for m in marks}
    # tanker T/CE levels
    assert got["VLCC"] == 193873.0
    assert got["Suezmax"] == 88573.0
    assert got["Aframax"] == 58531.0
    # Capesize: the "5.5k/day" change must be ignored, level captured
    assert got["Capesize"] == 40871.0
    # dry benchmark codes
    assert got["Ultramax"] == 20067.0
    assert got["Supramax"] == 18033.0
    assert got["Handysize"] == 15546.0
    assert got["MR"] == 41069.0
    # all marks are spot_tce / per-day
    assert all(m.kind == "spot_tce" and m.unit == "usd_per_day" for m in marks)


# --- newbuild prices --------------------------------------------------------
NB_TEXT = (
    "Dry Newbuilding Prices ($ mills)\n"
    "Capesize 75.5 74.0 2% 74.9 74.2 73.2\n"
    "Kamsarmax 37.5 36.5 3% 36.8\n"
    "Ultramax 34.5 33.5 3% 34.1\n"
    "Handysize 30.5 30.0 2% 29.8\n"
    "Tanker Newbuilding Prices ($ mills)\n"
    "VLCC 131.5 125.3 5% 129.7\n"
    "Suezmax 90.0 87.4 3% 88.1\n"
    "Aframax 75.0 73.1 3% 73.9\n"
    "Panamax 60.0 59.0 2% 58.5\n"
    "MR2 52.0 48.5 7% 50.3\n"
    "DRY SECONDHAND PRICES ($ mills)\n"
    "Capesize 999.9 ignore me after the secondhand boundary\n"
)


def test_newbuild_takes_first_column_within_nb_zone():
    marks = XclusivParser._newbuild(NB_TEXT)
    got = {m.vessel_class: m.value for m in marks}
    assert got["Capesize"] == 75.5          # not 999.9 (that's past the boundary)
    assert got["Kamsarmax"] == 37.5
    assert got["VLCC"] == 131.5
    assert got["Panamax"] == 60.0
    assert got["MR"] == 52.0                 # MR2 normalised to MR
    assert all(m.age_anchor == "newbuild" and m.unit == "musd" for m in marks)


# --- transposed secondhand table (age-as-row) -------------------------------
SECONDHAND_TABLE = [
    ["", "", "Jun 2026", "Jun 2025", "±%", "2026", "2025", "2024"],
    ["Capesize", "Resale", "81.5", "75.8", "8%", "80.4", "75.7", "75.7"],
    ["", "5 Year", "72.0", "62.8", "15%", "69.4", "62.6", "62.6"],
    ["", "10 Year", "56.5", "45.4", "25%", "53.7", "45.6", "43.1"],
    ["", "15 Year", "36.5", "26.1", "40%", "35.2", "27.4", "27.9"],
    ["Kamsarmax", "Resale", "46.0", "37.9", "21%", "42.3", "38.7", "41.8"],
    ["", "5 Year", "38.0", "30.5", "25%", "36.1", "32.3", "32.3"],
    ["", "10 Year", "29.0", "23.8", "22%", "27.2", "24.8", "27.3"],
    ["", "15 Year", "20.8", "14.9", "39%", "19.0", "15.6", "18.1"],
]


def test_transposed_value_table():
    marks = base.map_transposed_value_table(
        SECONDHAND_TABLE, anchor_labels=_AGE_LABELS,
        kind="vessel_value", metric="value", unit="musd",
    )
    got = {(m.vessel_class, m.age_anchor): m.value for m in marks}
    # value comes from the "Jun 2026" column (first numeric after the age label)
    assert got[("Capesize", "five_year")] == 72.0
    assert got[("Capesize", "ten_year")] == 56.5
    assert got[("Capesize", "resale")] == 81.5
    assert got[("Kamsarmax", "five_year")] == 38.0
    assert got[("Kamsarmax", "ten_year")] == 29.0
    assert got[("Kamsarmax", "fifteen_year")] == 20.8
    # class persisted across the blank-label rows in each group
    assert ("Kamsarmax", "resale") in got


# --- end-to-end parse on a synthesised PDF ----------------------------------
def _make_xclusiv_pdf(path):
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Table, TableStyle, Preformatted, Spacer,
    )
    from reportlab.lib.styles import getSampleStyleSheet

    styles = getSampleStyleSheet()
    spot_lines = [
        "Capesize: C5TC average closing the week at USD 40,871/day.",
        "Handysize: HS7TC average closed at USD 15,546/day.",
        "VLCC: average T/CE ended the week at USD 193,873/day.",
        "Aframax: average T/CE closed at USD 58,531/day.",
        "MR Atlantic Basket increased at USD 41,069/day.",
        "",
        "Dry Newbuilding Prices ($ mills)",
        "Capesize 75.5 74.0 2% 74.9",
        "Tanker Newbuilding Prices ($ mills)",
        "VLCC 131.5 125.3 5% 129.7",
        "MR2 52.0 48.5 7% 50.3",
        "DRY SECONDHAND PRICES ($ mills)",
    ]
    pre = Preformatted("\n".join(spot_lines), styles["Code"])
    tbl = Table(SECONDHAND_TABLE)
    tbl.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.black)]))
    SimpleDocTemplate(str(path)).build([pre, Spacer(1, 12), tbl])


def test_xclusiv_parser_end_to_end(tmp_path):
    pdf = tmp_path / "xclusiv_sample.pdf"
    _make_xclusiv_pdf(pdf)

    parser = get_parser("xclusiv")
    assert parser.broker_id == "xclusiv"
    ref = ReportRef("xclusiv", "hsn", "Xclusiv Weekly", "http://x", str(pdf),
                    dt.date(2026, 6, 8))
    mm = parser.parse(pdf, ref)

    assert mm.parser_ok
    assert mm.quarter == "2026Q2"
    kinds = {m.kind for m in mm.marks}
    assert {"spot_tce", "vessel_value"} <= kinds

    spot = {m.vessel_class: m.value for m in mm.marks if m.kind == "spot_tce"}
    assert spot["VLCC"] == 193873.0

    nb = {m.vessel_class: m.value for m in mm.marks
          if m.kind == "vessel_value" and m.age_anchor == "newbuild"}
    assert nb["VLCC"] == 131.5

    sh = {(m.vessel_class, m.age_anchor): m.value for m in mm.marks
          if m.kind == "vessel_value" and m.age_anchor == "five_year"}
    assert sh[("Capesize", "five_year")] == 72.0
