"""HKEXnews poller (F-3 light adapter): stockId discovery, the servlet's
embedded-JSON `result` quirk, dd/mm/yyyy date parsing, relevance filter,
quiet bootstrap, new-NEWS_ID detection, watermark, backoff, download cap.
All network stubbed at the module's fetch seam."""

import json
from datetime import datetime, timedelta, timezone

import crude_tanker_fv.hkex_poll as hp
from crude_tanker_fv.hkex_poll import (covered_stockids, parse_index,
                                       poll_stockid)


def _row(news_id, short_text, date_time="30/06/2026 16:30",
         file_link="/listedco/listconews/sehk/2026/0630/doc.pdf"):
    return {"NEWS_ID": news_id, "SHORT_TEXT": short_text, "TITLE": short_text,
            "DATE_TIME": date_time, "FILE_LINK": file_link, "FILE_TYPE": "PDF",
            "STOCK_CODE": "02343", "STOCK_NAME": "PACIFIC BASIN"}


def _index(rows, embed_as_string=True):
    """The live servlet returns result as a JSON-encoded STRING (verified on
    stockId 7703); embed_as_string=False covers the tolerated list shape."""
    result = json.dumps(rows) if embed_as_string else rows
    return json.dumps({"hasNextRow": False, "result": result}).encode()


def _fake_fetch(payload, doc_body=b"%PDF filing", status=200):
    calls = []

    def fetch(url, headers):
        calls.append((url, headers))
        if "titleSearchServlet" in url:
            return status, payload, {}
        return 200, doc_body, {}
    fetch.calls = calls
    return fetch


# stockId 7703 = "PACIFIC BASIN" per the venue annex's prefix.do verification
# (venue_annex.md HKEX §(i), 2026-07-09). Same two-surfaces rule as the EDGAR
# CIK pin: a stockId change must be re-verified against prefix.do and re-pinned.
VERIFIED_STOCKIDS = {"2343": "7703"}


def test_covered_stockids_match_the_verified_pin():
    assert covered_stockids() == VERIFIED_STOCKIDS
    # HKEX names carry sec_edgar: null — they must NOT leak into the EDGAR poller.
    from crude_tanker_fv.edgar_poll import covered_ciks
    assert "2343" not in covered_ciks()


def test_parse_index_handles_embedded_json_string_and_list():
    rows = [_row("1001", "Annual Report")]
    assert parse_index(_index(rows, embed_as_string=True)) == rows
    assert parse_index(_index(rows, embed_as_string=False)) == rows
    assert parse_index(json.dumps({"hasNextRow": False, "result": ""}).encode()) == []


def test_relevance_filter_and_date_parse():
    assert hp._relevant(_row("1", "Announcements and Notices - [Interim Results]"))
    assert hp._relevant(_row("2", "Monthly Returns",))
    # live servlet shapes (2026-07-14 probe): HTML tags + plural form
    assert hp._relevant(_row("2b", "Monthly Returns<br/>"))
    assert not hp._relevant(_row("3b", "Next Day Disclosure Returns - [Others]<br/>"))
    assert hp._clean("Monthly Returns<br/>") == "Monthly Returns"
    assert not hp._relevant(_row("3", "Next Day Disclosure Return"))
    assert not hp._relevant(_row("4", "Trading Information of Exchange Traded Fund"))
    # 2026-09-02: governance boilerplate no longer pages (7 of August's 11 HKEX pages)
    assert not hp._relevant(_row("8", "Announcements and Notices - [Terms of Reference of the Audit Committee]"))
    assert not hp._relevant(_row("9", "Announcements and Notices - [Other - Corporate Governance Related Matters]"))
    assert not hp._relevant(_row("10", "Circulars - [Other]"))
    assert hp._relevant(_row("11", "Circulars - [Major Transaction]"))
    assert hp._filed_date(_row("5", "x", date_time="30/06/2026 16:30")) == "2026-06-30"
    assert hp._filed_date(_row("6", "x", date_time="03/03/2026")) == "2026-03-03"
    assert hp._filed_date(_row("7", "x", date_time="junk")) == ""


def test_bootstrap_is_quiet_and_sticky(tmp_path, monkeypatch):
    monkeypatch.setattr(hp, "FILINGS_DIR", tmp_path / "filings")
    state = {}
    fetch = _fake_fetch(_index([_row("1001", "Annual Report")]))
    lines, used = poll_stockid("2343", "7703", state, fetch=fetch)
    assert lines == [] and used == 0
    assert state["7703"]["bootstrapped"] is True
    assert state["7703"]["watermark"] == "2026-06-30"

    # Zero relevant rows must still bootstrap sticky (the edgar_poll rule) —
    # not re-bootstrap forever and eat the first real filing.
    state2 = {}
    poll_stockid("2343", "7703", state2,
                 fetch=_fake_fetch(_index([_row("9", "Next Day Disclosure Return")])))
    assert state2["7703"]["bootstrapped"] is True
    fetch3 = _fake_fetch(_index([_row("9", "Next Day Disclosure Return"),
                                 _row("10", "Interim Report",
                                      date_time="31/12/2026 08:00")]))
    lines, _ = poll_stockid("2343", "7703", state2, fetch=fetch3)
    assert [l["accession"] for l in lines] == ["hkex-10"]


def test_new_filing_stages_and_manifests(tmp_path, monkeypatch):
    monkeypatch.setattr(hp, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(hp, "REQUEST_SPACING_S", 0)
    state = {"7703": {"bootstrapped": True, "seen_ids": ["1001"],
                      "watermark": "2026-01-01"}}
    fetch = _fake_fetch(_index([
        _row("1002", "Announcements and Notices - [Final Results]",
             date_time="02/07/2026 17:11",
             file_link="/listedco/listconews/sehk/2026/0702/2026070200123.pdf"),
        _row("1001", "Annual Report"),
    ]))
    lines, used = poll_stockid("2343", "7703", state, fetch=fetch)
    assert len(lines) == 1 and used == 1
    line = lines[0]
    assert line["accession"] == "hkex-1002"
    assert line["cik"] == "hkex:7703"
    assert line["source"] == "hkexnews"
    assert line["filed"] == "2026-07-02"
    assert line["staged_path"]
    assert (tmp_path / "filings" / "2343").exists()
    # doc fetched from the HKEX host with the FILE_LINK path
    doc_urls = [u for u, _ in fetch.calls if "listedco" in u]
    assert doc_urls == ["https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070200123.pdf"]
    # second poll: nothing new
    lines2, _ = poll_stockid("2343", "7703", state, fetch=fetch)
    assert lines2 == []


def test_watermark_blocks_pre_bootstrap_history(tmp_path, monkeypatch):
    monkeypatch.setattr(hp, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(hp, "REQUEST_SPACING_S", 0)
    state = {"7703": {"bootstrapped": True, "watermark": "2026-07-01",
                      "seen_ids": ["2001"]}}
    fetch = _fake_fetch(_index([
        _row("2002", "Interim Report", date_time="05/07/2026 12:00"),
        _row("0042", "Annual Report", date_time="15/03/2015 09:00"),
    ]))
    lines, _ = poll_stockid("2343", "7703", state, fetch=fetch)
    assert [l["accession"] for l in lines] == ["hkex-2002"]


def test_403_sets_backoff():
    state = {}
    now = datetime.now(timezone.utc)
    lines, _ = poll_stockid("2343", "7703", state,
                            fetch=_fake_fetch(b"", status=403), now=now)
    assert lines == []
    until = datetime.fromisoformat(state["7703"]["backoff_until"])
    assert until >= now + timedelta(minutes=59)


def test_download_cap_respected(tmp_path, monkeypatch):
    monkeypatch.setattr(hp, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(hp, "REQUEST_SPACING_S", 0)
    rows = [_row(f"3{i:03d}", "Annual Report", date_time="05/07/2026 12:00",
                 file_link=f"/listedco/doc{i}.pdf") for i in range(6)]
    state = {"7703": {"bootstrapped": True, "seen_ids": ["old"],
                      "watermark": "2026-01-01"}}
    lines, used = poll_stockid("2343", "7703", state,
                               fetch=_fake_fetch(_index(rows)), downloads_left=3)
    assert len(lines) == 6           # ALL detected + manifested
    assert used == 3                 # only 3 staged
    assert sum(1 for l in lines if l["staged_path"]) == 3
