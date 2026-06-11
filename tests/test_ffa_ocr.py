"""FFA-OCR Stage 1: tenor normalization, positional parse, sanity model.

No tesseract calls — parsing runs on canned TSV word dicts. The sanity
model under test is the DISCOVERED one (ffa_ocr.py docstring): months and
Cal tenors tick in $12.5 (displayed truncated), Q tenors display the
unrounded 3-month average; continuity is calendar-day-ordered.
"""

from crude_tanker_fv.ffa_ocr import (
    _norm_tenor,
    is_ffa_widget,
    parse_widget,
    sanity_issues,
)


def _w(text, x, line=1, conf=95.0, width=200):
    return {"text": text, "x": x, "line": ("1", "1", str(line)),
            "conf": conf, "width": width}


def _widget_words():
    """Three-panel row set mimicking the Jun-11 2026 capture."""
    rows = [
        ("Jun", [36875, 21075, 19050]),
        ("Jul", [31375, 22050, 19900]),
        ("Q3", [31766, 21416, 19358]),
        ("Q4", [31875, 19825, 17750]),
        ("Cal27", [26550, 15775, 13675]),
    ]
    words = []
    for li, (tenor, prices) in enumerate(rows, start=3):
        for panel_i, price in enumerate(prices):
            x0 = panel_i * 1000
            words.append(_w(tenor, x0 + 76, line=li))
            words.append(_w(str(price), x0 + 412, line=li))
    return words


def test_norm_tenor_ocr_confusions():
    assert _norm_tenor("Q3") == "q3"
    assert _norm_tenor("O3") == "q3"   # OCR reads Q as O
    assert _norm_tenor("a4") == "q4"   # ... and as a
    assert _norm_tenor("04") == "q4"   # ... and as 0
    assert _norm_tenor("Cal27") == "cal27"
    assert _norm_tenor("Jun") == "jun"
    assert _norm_tenor("36875") is None
    assert _norm_tenor("Change") is None


def test_parse_widget_full_grid():
    curves = parse_widget(_widget_words())
    assert curves["cape"]["jun"] == 36875
    assert curves["pmax"]["q4"] == 19825
    assert curves["smax"]["cal27"] == 13675
    assert all(len(c) == 5 for c in curves.values())


def test_parse_majority_vote_recovers_garbled_tenor():
    words = _widget_words()
    # Smax Q4 label OCRs as bare "4" (the observed Jun-11 failure)
    for w in words:
        if w["text"] == "Q4" and w["x"] > 2000:
            w["text"] = "4"
    curves = parse_widget(words)
    assert curves["smax"]["q4"] == 17750  # row survives on 2/3 vote


def test_parse_rejects_leading_mangled_price():
    words = _widget_words()
    for w in words:
        if w["text"] == "31766":
            w["text"] = "(3800"  # digit eaten -> must NOT become 3800
    curves = parse_widget(words)
    assert "q3" not in curves["cape"]


def test_parse_rejects_low_confidence_price():
    words = _widget_words()
    for w in words:
        if w["text"] == "31766":
            w["conf"] = 40.0
    curves = parse_widget(words)
    assert "q3" not in curves["cape"]


def test_parse_strips_trailing_punctuation():
    words = _widget_words()
    for w in words:
        if w["text"] == "21075":
            w["text"] = "21075,"  # the observed Jun-08 Pmax artifact
    curves = parse_widget(words)
    assert curves["pmax"]["jun"] == 21075


def _clean_curves():
    return parse_widget(_widget_words())


def test_sanity_clean_grid_passes():
    assert sanity_issues(_clean_curves()) == []


def test_sanity_quarter_average_not_flagged():
    # 31766 = 95300/3 — unrounded Q average must pass (the discovered model)
    issues = sanity_issues(_clean_curves())
    assert not any("q3" in i for i in issues)


def test_sanity_half_tick_passes_and_off_tick_fails():
    curves = _clean_curves()
    curves["pmax"]["jul"] = 21312  # 21312.5 truncated — real half-tick
    assert not any("21312" in i for i in sanity_issues(curves))
    curves["pmax"]["jul"] = 21307  # genuinely off-tick
    assert any("21307" in i for i in sanity_issues(curves))


def test_sanity_incomplete_grid_flagged():
    curves = _clean_curves()
    del curves["cape"]["q4"]
    assert any("incomplete grid" in i for i in sanity_issues(curves))


def test_sanity_intra_curve_outlier_flagged():
    curves = _clean_curves()
    curves["cape"]["q3"] = 3800  # digit-loss survivor
    assert any("intra-curve spread" in i for i in sanity_issues(curves))


def test_sanity_continuity_band():
    prev = _clean_curves()
    curves = _clean_curves()
    curves["cape"]["jun"] = int(prev["cape"]["jun"] * 1.2)
    issues = sanity_issues(curves, prev)
    assert any("exceeds ±10%" in i for i in issues)
    assert sanity_issues(_clean_curves(), prev) == []


def test_classifier_requires_all_three_signatures():
    good = "Markets Cape Pmax Smax\nProduct Price Change\nJun 36875\nCal27 26550"
    assert is_ffa_widget(good)
    assert not is_ffa_widget(good.replace("Cal27", "2027"))
    assert not is_ffa_widget("Cape Town container report Cal27")
