"""Format-version dispatch tests: probe-based routing, date fallback, the
unrecognised-layout safety net, and end-to-end routing of a legacy vs current
Weber PDF to the right parser.

Run:  pytest -q tests/test_dispatch.py
"""
from __future__ import annotations

import datetime as dt

from shipping_harvester.models import ReportRef
from shipping_harvester.parse import resolve_parser, dispatch_parse, get_parser


# --- resolution: simple (single-version) broker -----------------------------
def test_simple_broker_resolves_regardless_of_text_or_date():
    p, ver, conf = resolve_parser("allied", dt.date(2026, 6, 1), "whatever")
    assert ver == "allied" and conf and p.broker_id == "allied"
    p2, ver2, conf2 = resolve_parser("allied", dt.date(2014, 1, 1), "")
    assert ver2 == "allied" and conf2


# --- resolution: multi-version broker via probe -----------------------------
def test_weber_current_routed_by_tanker_routes_probe():
    _, ver, conf = resolve_parser("weber", dt.date(2025, 1, 10),
                                  "...TANKER ROUTES... VLCC Average Earnings + $20,490")
    assert ver == "weber_2024" and conf


def test_weber_legacy_routed_when_no_tanker_routes():
    _, ver, conf = resolve_parser("weber", dt.date(2019, 4, 12),
                                  "Spot Market ... VLCC Average Earnings $17,520 $15,700")
    assert ver == "weber_2017" and conf


def test_probe_beats_date_when_they_disagree():
    # date says current era, but the content is clearly the legacy layout
    _, ver, _ = resolve_parser("weber", dt.date(2025, 1, 10),
                               "VLCC Average Earnings $1 $2")  # no TANKER ROUTES
    assert ver == "weber_2017"


# --- safety net: unrecognised layout doesn't get mis-parsed -----------------
def test_unrecognised_layout_falls_back_to_generic():
    p, ver, conf = resolve_parser("weber", dt.date(2030, 1, 1),
                                  "totally unrelated content with no markers")
    assert ver == "generic:unrecognized-format"
    assert not conf and p.broker_id == "generic"


def test_unknown_broker_is_generic():
    p, ver, conf = resolve_parser("braemar", dt.date(2026, 1, 1), "x")
    assert ver == "generic" and not conf and p.broker_id == "generic"


# --- date fallback when text is unavailable ---------------------------------
def test_empty_text_falls_back_to_date_window():
    _, ver_old, conf_old = resolve_parser("weber", dt.date(2019, 4, 12), "")
    assert ver_old == "weber_2017" and conf_old
    _, ver_new, _ = resolve_parser("weber", dt.date(2025, 1, 1), "")
    assert ver_new == "weber_2024"


# --- get_parser returns the newest (no dispatch) ----------------------------
def test_get_parser_returns_newest_version():
    assert get_parser("weber").__class__.__name__ == "WeberParser"


# --- legacy parser extraction ----------------------------------------------
WEBER_LEGACY = "\n".join([
    "Spot Market WS/LS TCE WS/LS TCE",
    "VLCC (13.0 Kts L/B) 5-Apr 12-Apr",
    "AG>SPORE 270k 38.6 $15,007 37.8 $14,054",
    "WAFR>CHINA 260k 43.4 $20,297 41.6 $17,873",
    "VLCC Average Earnings $17,520 $15,700",
    "SUEZMAX (13.0 Kts L/B) WAFR>USG 130k 50.0 $8,017 65.0 $16,333",
    "SUEZMAX Average Earnings $10,200 $14,150",
])

CURRENT_MIN = "\n".join([
    "TANKER ROUTES (13kts L|B) Week 1 Week 2 Week 1 Week 2",
    "VLCC WS|L$ WS|L$ TCE* TCE**",
    "AG>SPORE 270000 41.50 45.50 $17,089 $21,766 Time Charter 1 Year v. 3 Years ($|day):",
    "AG>JPN 265000 39.50 43.50 $14,290 $18,951 $45,000 $47,000",
    "VLCC Average Earnings +",
    "-- -- $17,283 $20,490",
    "THE WEEK IN CHARTS",
])


def test_legacy_parser_extracts_average_earnings():
    from shipping_harvester.parse.weber_2019 import WeberParser2019
    spot = {m.vessel_class: m.value for m in WeberParser2019().extract([], WEBER_LEGACY)}
    assert spot["VLCC"] == 15700.0      # latest (week-2) column
    assert spot["Suezmax"] == 14150.0


def _pdf(path, text):
    from reportlab.platypus import SimpleDocTemplate, Preformatted
    from reportlab.lib.styles import ParagraphStyle
    style = ParagraphStyle("w", fontName="Courier", fontSize=7, leading=9)
    SimpleDocTemplate(str(path)).build([Preformatted(text, style)])


def test_dispatch_routes_legacy_pdf_to_legacy_parser(tmp_path):
    pdf = tmp_path / "weber_2019.pdf"
    _pdf(pdf, WEBER_LEGACY)
    ref = ReportRef("weber", "capitallink", "Weber 2019", "http://x", str(pdf),
                    dt.date(2019, 4, 12))
    mm, conf = dispatch_parse("weber", pdf, ref)
    assert mm.parser == "weber_2017" and conf
    spot = {m.vessel_class: m.value for m in mm.marks if m.kind == "spot_tce"}
    assert spot["VLCC"] == 15700.0


def test_dispatch_routes_current_pdf_to_current_parser(tmp_path):
    pdf = tmp_path / "weber_2025.pdf"
    _pdf(pdf, CURRENT_MIN)
    ref = ReportRef("weber", "capitallink", "Weber 2025", "http://x", str(pdf),
                    dt.date(2025, 1, 10))
    mm, conf = dispatch_parse("weber", pdf, ref)
    assert mm.parser == "weber_2024" and conf
    spot = {m.vessel_class: m.value for m in mm.marks if m.kind == "spot_tce"}
    assert spot["VLCC"] == 20490.0
    # current parser also pulls period TC, which the legacy era lacks
    tc = [m for m in mm.marks if m.kind == "period_tc" and m.metric == "1yr_tc"]
    assert any(m.value == 45000.0 for m in tc)
