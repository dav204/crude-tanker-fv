"""Tests for the Baltic shipping indexes parser.

Uses real message samples captured from the Value Investor's Edge channel
(John.Pace and Chris.Palun) to exercise both formats.
"""

from datetime import datetime

from crude_tanker_fv.baltic_parser import (
    INDEX_NAMES,
    parse_baltic_post,
    parse_capesize_post,
)


def _ts(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def test_john_pace_with_inline_deltas():
    text = """*Daily Shipping Indexes*
BCTI: 1,379 (+3) (6/8)
BDTI: 2,099 (-11) (6/8)
BLPG: 18,057 (-3) (6/8)
BDI: 2,916 (-65) (6/8)
FBX: 2,878 (+43) (6/8)"""
    r = parse_baltic_post(text, _ts("2026-06-08T22:48:26Z"))
    assert r == {
        "date": "2026-06-08",
        "BCTI": 1379,
        "BDTI": 2099,
        "BLPG": 18057,
        "BDI": 2916,
        "FBX": 2878,
    }


def test_john_pace_with_arrows_only():
    text = """*Daily Shipping Indexes*
BCTI: 1,376 ▼ (6/5)
BDTI: 2,110 ▲ (6/5)
BLPG: 18,060 ▲ (6/5)
BDI: 2,981 ▼ (6/5)
FBX: 2,835 ▼ (6/5)"""
    r = parse_baltic_post(text, _ts("2026-06-05T17:51:12Z"))
    assert r["date"] == "2026-06-05"
    assert r["BCTI"] == 1376
    assert r["BDTI"] == 2110
    assert r["FBX"] == 2835


def test_john_no_asterisks():
    text = """Daily Shipping Indexes
BCTI: 1,504 (-53) (5/29)
BDTI: 2,068 (-20) (5/29)
BLPG: 18,262 (-420) (5/29)
BDI: 3,224 (-2) (5/29)
FBX: 2,240 (+1) (5/29)"""
    r = parse_baltic_post(text, _ts("2026-05-29T17:42:14Z"))
    assert r["date"] == "2026-05-29"
    assert r["BDI"] == 3224
    assert r["BLPG"] == 18262


def test_chris_palun_bullet_format():
    text = """Shipping Index 4/24:

- BCTI: 2197 (-4)
- BDTI: 2812 (-25)

- BLPG: 14,147 (-147)

- BDI: 2665 (-8)
- FBX: 1935 (+24)

Small changes again."""
    r = parse_baltic_post(text, _ts("2026-04-24T15:32:57Z"))
    assert r == {
        "date": "2026-04-24",
        "BCTI": 2197,
        "BDTI": 2812,
        "BLPG": 14147,
        "BDI": 2665,
        "FBX": 1935,
    }


def test_chris_palun_with_trailing_commentary():
    text = """Shipping Index 4/14:

- BCTI: 2147 (+1)
- BDTI: 3275 (-147)

- BLPG: 11850 (+1674)

- BDI: 2354 (+104)

- FBX: 1908 (+8)

BLPG 🚀🚀"""
    r = parse_baltic_post(text, _ts("2026-04-14T15:18:58Z"))
    assert r["BLPG"] == 11850
    assert r["FBX"] == 1908


def test_year_wraparound_for_dec_data_posted_in_jan():
    text = """*Daily Shipping Indexes*
BCTI: 1,000 (+0) (12/31)
BDTI: 1,000 (+0) (12/31)
BLPG: 1,000 (+0) (12/31)
BDI: 1,000 (+0) (12/31)
FBX: 1,000 (+0) (12/31)"""
    r = parse_baltic_post(text, _ts("2027-01-02T10:00:00Z"))
    assert r["date"] == "2026-12-31"


def test_non_baltic_text_returns_none():
    assert parse_baltic_post("Yes, how interesting.", _ts("2026-05-26T17:20:00Z")) is None
    assert parse_baltic_post("", _ts("2026-05-26T17:20:00Z")) is None
    assert parse_baltic_post("Random chat about KOS", _ts("2026-05-26T17:20:00Z")) is None


def test_truncated_post_recovers_complete_lines():
    text = """Shipping Index 4/17:

- BCTI: 2123 (+2)
- BDTI: 2831 (-144)

- BLPG: 13770 (+25)

- BDI: 2567 (+44)
- FBX: 1898 (+"""
    r = parse_baltic_post(text, _ts("2026-04-17T15:23:34Z"))
    assert r["date"] == "2026-04-17"
    assert r["BCTI"] == 2123
    assert r["FBX"] == 1898  # incomplete delta still leaves the value usable


def test_all_index_names_in_result():
    text = """*Daily Shipping Indexes*
BCTI: 100 (+0) (6/8)"""
    r = parse_baltic_post(text, _ts("2026-06-08T22:00:00Z"))
    # All five keys must be present even if only one had data
    assert set(r.keys()) == {"date", *INDEX_NAMES}
    assert r["BCTI"] == 100
    assert r["BDTI"] is None


def test_capesize_standalone():
    assert parse_capesize_post("Capesize index: 35,333 (-301)") == 35333
    assert parse_capesize_post("Capesize index: 36,002 (+507)") == 36002


def test_capesize_with_preamble():
    text = "Strong index today:\n\nCapesize index: 27,667 (+1082)"
    assert parse_capesize_post(text) == 27667


def test_capesize_no_delta():
    assert parse_capesize_post("Capesize index: 25,045") == 25045


def test_capesize_none_on_unrelated_text():
    assert parse_capesize_post("just some text") is None
    assert parse_capesize_post("") is None
