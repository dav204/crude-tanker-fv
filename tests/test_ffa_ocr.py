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


def test_queue_month_columns_are_chronological(tmp_path, monkeypatch):
    """The m1/m2 queue columns must be calendar-ordered, not alphabetical —
    the alphabetical sort put AUG before JUL and the 2-Jul Supra spot proxy
    took the wrong month off the queue (decisions/ffa_promotion_2026-07-13.md).
    Covers the Dec→Jan year wrap too."""
    from crude_tanker_fv import ffa_ocr
    from crude_tanker_fv.ffa_ocr import _tenor_sort_key, _write_queue

    monkeypatch.setattr(ffa_ocr, "QUEUE_PATH", tmp_path / "queue.md")
    db = {
        "2026-07-13": {
            "status": "ok", "issues": [], "source": "img-jul.png",
            "curves": {"cape": {"aug": 34625, "cal27": 28600, "jul": 36000,
                                "q3": 35416, "q4": 35200},
                       "pmax": {}, "smax": {}},
        },
        "2026-12-15": {
            "status": "ok", "issues": [], "source": "img-dec.png",
            "curves": {"cape": {"jan": 21000, "dec": 20000,
                                "q1": 20500, "cal27": 18000},
                       "pmax": {}, "smax": {}},
        },
    }
    _write_queue(db)
    text = (tmp_path / "queue.md").read_text()
    jul_row = next(l for l in text.splitlines() if "2026-07-13" in l)
    dec_row = next(l for l in text.splitlines() if "2026-12-15" in l)
    assert "36000/34625/35416/35200/28600" in jul_row   # jul before aug
    assert "20000/21000/20500/18000" in dec_row          # dec before jan (wrap)

    assert _tenor_sort_key("jul", 7) < _tenor_sort_key("aug", 7)
    assert _tenor_sort_key("dec", 12) < _tenor_sort_key("jan", 12)
    assert _tenor_sort_key("aug", 7) < _tenor_sort_key("q3", 7) \
        < _tenor_sort_key("cal27", 7)


def _wy(text, x, y, line, conf=95.0, width=200):
    return {"text": text, "x": x, "y": y, "line": ("1", "1", str(line)),
            "conf": conf, "width": width}


def test_parse_widget_stacked_layout():
    """Chris.Palun phone captures (2026-07-20 →): the three panels stack
    vertically — header y-bands, not x-thirds, decide the panel."""
    words = []
    li = 1
    for pi, (panel, prices) in enumerate([
        ("Cape", [35125, 33875, 34950, 35500, 28950]),
        ("Pmax", [19600, 18600, 19200, 19050, 16450]),
        ("Smax", [19450, 18800, 19125, 18300, 14300]),
    ]):
        y0 = pi * 6000
        words.append(_wy(panel, 40, y0, li)); li += 1
        for ti, tenor in enumerate(("Jul", "Aug", "Q3", "Q4", "Cal27")):
            y = y0 + 800 + ti * 900
            words.append(_wy(tenor, 45, y, li))
            words.append(_wy(str(prices[ti]), 700, y, li))
            li += 1
    curves = parse_widget(words)
    assert curves["cape"]["cal27"] == 28950
    assert curves["pmax"]["jul"] == 19600
    assert curves["smax"]["q4"] == 18300
    assert len(curves["cape"]) == len(curves["pmax"]) == len(curves["smax"]) == 5


def test_parse_widget_stacked_skips_words_above_first_header():
    # Stacked detection needs >=2 header anchors; words above the first
    # header (cropped chrome / index caption) belong to no panel.
    words = [
        _wy("34569", 700, 10, 1),          # index line above the widget — no panel
        _wy("Cape", 40, 1000, 2),
        _wy("Jul", 45, 1900, 3), _wy("35125", 700, 1900, 3),
        _wy("Pmax", 40, 7000, 4),
        _wy("Jul", 45, 7900, 5), _wy("19600", 700, 7900, 5),
    ]
    curves = parse_widget(words)
    assert curves["cape"] == {"jul": 35125}
    assert curves["pmax"] == {"jul": 19600}
    assert curves["smax"] == {}
