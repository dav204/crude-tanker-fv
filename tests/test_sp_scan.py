"""Tests for the incremental Pareto S&P scan (sp_scan.py)."""

from crude_tanker_fv.sp_scan import (
    NAME_ALIASES,
    extract_name_mentions,
    extract_sp_candidates,
    load_scan_state,
    save_scan_state,
    select_files,
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
