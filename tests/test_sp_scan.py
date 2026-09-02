"""Tests for the incremental Pareto S&P scan (sp_scan.py)."""

from crude_tanker_fv.sp_scan import (
    NAME_ALIASES,
    extract_name_mentions,
    extract_sp_candidates,
    extract_tanker_period_signals,
    load_scan_state,
    save_scan_state,
    select_files,
    unwrap_tracked_url,
)


def test_extracts_sale_sentence_with_class_and_price():
    text = ("Brokers are reporting that the 2009-built LR2 'Zenovia Lady' "
            "(scrubber-fitted) has been sold for $41m, far ahead of generic quotes.")
    hits = extract_sp_candidates(text)
    assert ("LR2" in [cls for cls, _, _ in hits])
    assert all(not demo for _, _, demo in hits)


def test_rejects_rate_table_noise():
    # The daily rate-table header names every class with $-figures but no
    # sale phrase — the historical source of false positives.
    text = ("Tanker spot rates Scrubber Average of key routes: Yesterday change % "
            "VLCC USD/day $22 800 -0.8% Suezmax $19 000 -1.7% Aframax $28 900 -3.6% "
            "LR2 $26 800 0.7% MR $16 800 -4.5% Market indicators: Last price 1-day ch.")
    assert extract_sp_candidates(text) == []


def test_demolition_flagged_not_dropped():
    text = ("According to VesselsValue, the 2002-built capesize 'Douga' (178k dwt) "
            "has been sold for demolition at $11m to Bangladesh breakers.")
    hits = extract_sp_candidates(text)
    assert hits and all(demo for _, _, demo in hits)
    assert hits[0][0] == "Cape"


def test_en_bloc_multi_class_sentence_hits_both_classes():
    text = ("Yesterday, Scorpio announced the sale of six vessels for $300m; split "
            "between 3x 2014-built LR2s ($195m) and 3x 2014-built MRs ($105m).")
    classes = {cls for cls, _, _ in extract_sp_candidates(text)}
    assert {"LR2", "MR"} <= classes


def test_scan_state_round_trip(tmp_path):
    state = tmp_path / "_scan_state.json"
    assert load_scan_state(state) is None
    save_scan_state("2026-06-08", state)
    assert load_scan_state(state) == "2026-06-08"


def test_scan_state_merge_preserves_additive_keys(tmp_path):
    """WO2 1.4: a cursor-only save must not clobber the tanker-signal hits."""
    import json

    state = tmp_path / "_scan_state.json"
    save_scan_state("2026-06-08", state,
                    extra={"tanker_period_signals": {"hits": [{"date": "2026-06-08"}]}})
    save_scan_state("2026-06-09", state)   # cursor-only follow-up
    doc = json.loads(state.read_text())
    assert doc["last_scanned_report_date"] == "2026-06-09"
    assert doc["tanker_period_signals"]["hits"] == [{"date": "2026-06-08"}]


def test_tanker_period_signal_extraction():
    """WO2 1.4: 1-yr TC / tanker-FFA prose hits; spot-table noise stays out."""
    tc = ("Brokers report a modern VLCC was fixed on a 1-year time charter at "
          "$52,500/day to an oil major, the first period fixture since the ceasefire.")
    assert [k for k, _ in extract_tanker_period_signals(tc)] == ["period-tc"]

    ffa = ("Tanker FFAs firmed with TD3C paper for Q4 changing hands around "
           "$48,000/day as period interest returned to the crude space broadly.")
    assert [k for k, _ in extract_tanker_period_signals(ffa)] == ["tanker-ffa"]

    spot_table = ("Tanker spot rates Scrubber Average of key routes: Yesterday "
                  "change % VLCC USD/day $285,500 -1.1% Suezmax $124,800 +4.7% "
                  "Aframax $42,400 -8.2% MR $35,600 +2.7% Market indicators here.")
    assert extract_tanker_period_signals(spot_table) == []

    dry = ("A capesize was fixed on a 1-year period at $28,000/day yesterday, "
           "reflecting the firmer FFA curve into the fourth quarter this year.")
    assert extract_tanker_period_signals(dry) == []


def test_name_mentions_alias_aware():
    # Pareto uses Oslo tickers / company names — OET is ECO, HAFNI is HAFN.
    text = ("OET also entered into two $50m bank facilities for the previously "
            "announced refinancings; we peg the company at ~1.55x NAV. "
            "HAFNI: Finishes up buyback program at sub-0.8x NAV with 3.95m shares bought.")
    hits = extract_name_mentions(text, ["ECO", "HAFN", "DHT"])
    tickers = {t for t, _ in hits}
    assert tickers == {"ECO", "HAFN"}


def test_name_mentions_require_context():
    # A bare peer-list drop with no valuation/action context is noise.
    text = ("Shipping equities traded lower across the board yesterday, with "
            "DHT, FRO and TNK among the laggards in an otherwise quiet session "
            "for the broader tanker complex across both basins worldwide.")
    assert extract_name_mentions(text, ["DHT", "FRO", "TNK"]) == []


def test_name_mentions_short_ticker_case_sensitivity():
    # 'TEN' must not fire on the word 'ten'; 'Tsakos' fires case-insensitively.
    noise = ("The fleet has grown by more than ten vessels over the period, with "
             "the dividend policy unchanged across all of the company's segments.")
    assert extract_name_mentions(noise, ["TEN"]) == []
    real = ("Tsakos Energy Navigation declared a quarterly dividend and trades "
            "at a steep discount to NAV on our numbers per yesterday's close.")
    assert {t for t, _ in extract_name_mentions(real, ["TEN"])} == {"TEN"}


def test_all_watchlist_names_have_aliases():
    assert set(NAME_ALIASES) >= {"DHT", "ECO", "FRO", "INSW", "TNK", "NAT", "FLNG",
                                 "CCEC", "STNG", "HAFN", "TRMD", "ASC", "TEN",
                                 "SBLK", "GNK"}


def test_unwrap_tracked_url_passthrough_and_proofpoint():
    direct = "https://parp.hosting.factset.com/PARTNERS_TD_TRACK/external/download?q=abc123"
    assert unwrap_tracked_url(direct) == direct
    # Proofpoint v3 wrapper: extract between __ and __; decode *HH escapes;
    # fix the single-slash scheme artifact.
    wrapped = ("https://urldefense.com/v3/__https:/parp.hosting.factset.com/"
               "PARTNERS_TD_TRACK/external/download?q=tok*2Babc*2Fdef__;KyU!!extra!!")
    out = unwrap_tracked_url(wrapped)
    assert out == ("https://parp.hosting.factset.com/PARTNERS_TD_TRACK/"
                   "external/download?q=tok%2Babc%2Fdef")


def test_unwrap_tracked_url_rejects_non_report_links():
    assert unwrap_tracked_url("mailto:analyst@paretosec.com") is None
    assert unwrap_tracked_url("https://www.ft.com/content/abc") is None
    assert unwrap_tracked_url("https://urldefense.com/v3/__https:/www.ft.com/x__;!!") is None


def test_select_files_filters_by_cursor_and_sorts():
    manifest = {"files": [
        {"type": "shipping_daily", "report_date": "2026-06-08", "path": "c.pdf"},
        {"type": "shipping_daily", "report_date": "2026-06-04", "path": "a.pdf"},
        {"type": "company_report", "report_date": "2026-06-09", "path": "x.pdf"},
        {"type": "shipping_daily", "report_date": "2026-06-05", "path": "b.pdf"},
    ]}
    # No cursor: all shipping_daily, oldest first
    assert [f["path"] for f in select_files(manifest, None)] == ["a.pdf", "b.pdf", "c.pdf"]
    # Cursor at 2026-06-04: strictly-after filtering
    assert [f["path"] for f in select_files(manifest, "2026-06-04")] == ["b.pdf", "c.pdf"]
    # Cursor at newest: nothing to do
    assert select_files(manifest, "2026-06-08") == []


def test_select_files_scans_late_arrivals_behind_the_cursor():
    """2026-09-02 (Stage 0): with a scanned-path set, a daily whose report_date
    predates the cursor but was never scanned is due — the date cursor alone
    hid the 8/31 + 9/01 dailies (and any backfilled issue) until a rebuild."""
    manifest = {"files": [
        {"path": "a.pdf", "type": "shipping_daily", "report_date": "2026-06-03"},
        {"path": "late.pdf", "type": "shipping_daily", "report_date": "2026-06-02"},
        {"path": "c.pdf", "type": "shipping_daily", "report_date": "2026-06-05"},
        {"path": "x.pdf", "type": "other", "report_date": "2026-06-04"},
    ]}
    scanned = {"a.pdf"}
    due = [f["path"] for f in select_files(manifest, "2026-06-03", scanned)]
    assert due == ["late.pdf", "c.pdf"]
    assert [f["path"] for f in select_files(manifest, "2026-06-03")] == ["c.pdf"]
