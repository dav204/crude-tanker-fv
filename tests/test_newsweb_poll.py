"""Oslo/Euronext issuer poller: slug discovery, JSON Feed parsing, the ob/mfn
duplicate collapse, the near-inclusive relevance filter, quiet bootstrap,
watermark, backoff, download cap, attachment extraction.

The load-bearing test here is `test_known_historical_misses_survive_the_filter`:
it pins the four releases whose absence is the reason this module exists. Any
future tightening of NOISE_TAGS into an allowlist reds the suite instead of
silently re-opening the hole. All network stubbed at the module's fetch seam.
"""

import json
from datetime import datetime, timedelta, timezone

import crude_tanker_fv.newsweb_poll as nw
from crude_tanker_fv.newsweb_poll import (attachment_urls, covered_slugs, dedupe,
                                          normalize_title, parse_feed, poll_slug,
                                          release_text)


def _item(news_id, title, publish_date="2026-08-13T05:31:58Z", tags=("sub:ci", "sub:ci:other"),
          source="mfn", html="<div class=\"mfn-body\"><p>Body text.</p></div>", url=None):
    return {"news_id": news_id, "group_id": f"g-{news_id}", "source": source,
            "url": url or f"https://mfn.se/a/issuer/{news_id}",
            "properties": {"lang": "en", "tags": list(tags), "type": "ir"},
            "content": {"title": title, "publish_date": publish_date, "html": html}}


def _feed(items):
    return json.dumps({"version": "https://jsonfeed.org/version/1.1",
                       "title": "Issuer", "items": items}).encode()


def _fake_fetch(payload, doc_body=b"%PDF release", status=200):
    calls = []

    def fetch(url, headers):
        calls.append((url, headers))
        if url.endswith(".json"):
            return status, payload, {}
        return 200, doc_body, {}
    fetch.calls = calls
    return fetch


# The four covered Oslo/Euronext names. A slug change must be re-verified
# against the live feed and re-pinned here (same two-surfaces rule as the
# EDGAR CIK pin and the HKEX stockId pin).
VERIFIED_SLUGS = {"BRUT": "bruton-limited", "BWLP": "bw-lpg",
                  "CAPT": "capital-tankers", "MPCC": "mpc-container-ships"}


def test_covered_slugs_match_the_verified_pin():
    assert covered_slugs() == VERIFIED_SLUGS


def test_oslo_names_do_not_leak_into_the_other_venue_pollers():
    from crude_tanker_fv.edgar_poll import covered_ciks
    from crude_tanker_fv.hkex_poll import covered_stockids
    ciks, stockids = covered_ciks(), covered_stockids()
    for ticker in ("BRUT", "CAPT", "MPCC"):
        assert ticker not in ciks, f"{ticker} has no SEC lane"
        assert ticker not in stockids
    # BWLP is dual-listed (Oslo primary + NYSE FPI) and legitimately has both;
    # its releases dedupe by news_id per venue, not across venues.
    assert "BWLP" in ciks


def test_parse_feed_and_empty_envelope():
    items = [_item("a", "Title A")]
    assert parse_feed(_feed(items)) == items
    assert parse_feed(_feed([])) == []


def test_normalize_title_strips_the_exchange_ticker_prefix():
    assert (normalize_title("CAPT: CAPITAL TANKERS CORP. ANNOUNCES DELIVERY")
            == normalize_title("CAPITAL TANKERS CORP. ANNOUNCES DELIVERY"))
    assert normalize_title("MPCC - Major Shareholding") == "major shareholding"
    # A colon inside a real sentence must NOT be eaten as a prefix (the token
    # before it is longer than a ticker).
    assert normalize_title("Oslo, Norway: acquisition").startswith("oslo norway")


def test_normalize_title_survives_the_en_dash_rewrite():
    """CAPT 2026-06-04 leaked a duplicate through whitespace-only normalization:
    the issuer wrote 'Corp. – Ex Dividend Date', the Oslo mirror rendered the
    en-dash as whitespace. Punctuation is not identity."""
    assert (normalize_title("Capital Tankers Corp. – Ex Dividend Date")
            == normalize_title("CAPT: Capital Tankers Corp.   Ex Dividend Date"))


def test_normalize_title_does_not_over_collapse_distinct_releases():
    assert (normalize_title("Contemplated Private Placement")
            != normalize_title("Successfully Completed Private Placement"))


def test_dedupe_collapses_the_ob_and_mfn_twins_keeping_richer_tags():
    ob = _item("id-ob", "CAPT: DELIVERY OF ONE SUEZMAX", source="ob", tags=(":regulatory",),
               publish_date="2026-08-13T05:32:00Z")
    mfn = _item("id-mfn", "DELIVERY OF ONE SUEZMAX", source="mfn",
                tags=("ext:ob", "ext:ob:non-regulatory", "sub:ci", "sub:ci:other"),
                publish_date="2026-08-13T05:31:58Z")
    out = dedupe([ob, mfn])
    assert len(out) == 1
    assert out[0]["news_id"] == "id-mfn"


def test_dedupe_keeps_genuinely_distinct_releases_on_one_day():
    a = _item("x", "Contemplated Private Placement", publish_date="2026-06-30T16:39:00Z")
    b = _item("y", "Successfully Completed Private Placement", publish_date="2026-06-30T22:00:00Z")
    assert len(dedupe([a, b])) == 2


def test_known_historical_misses_survive_the_filter():
    """The releases this module exists because the book missed.

    Tags are verbatim from the live MFN feeds on 2026-08-16. Note CAPT's two
    deliveries carry `ext:ob:non-regulatory` — the same tag as the noise
    bucket — which is exactly why the filter is a deny-list, not an allow-list.
    """
    misses = [
        _item("brut-demerger", "Bruton Limited (BRUT) – Delivery of Mount Vision, sale "
              "leaseback financing secured, demerger and new CEO",
              publish_date="2026-07-07T06:00:00Z",
              tags=(":regulatory", ":regulatory:listing", "ext:ob",
                    "ext:ob:inside-information", "sub:ci", "sub:ci:other")),
        _item("mpcc-acq", "MPC Container Ships ASA to acquire four 7,000 TEU vessels",
              publish_date="2026-06-25T07:00:00Z",
              tags=(":regulatory", ":regulatory:mar", ":regulatory:nsta", "ext:ob",
                    "ext:ob:inside-information", "sub:ci", "sub:ci:other")),
        _item("mpcc-shares", "MPC Container Ships ASA: Registration of share capital increase",
              publish_date="2026-07-02T09:52:00Z",
              tags=(":regulatory", ":regulatory:nsta", "sub:ca", "sub:ca:shares")),
        _item("capt-lr2", "CAPITAL TANKERS CORP. ANNOUNCES THE SUCCESSFUL DELIVERY OF ONE "
              "DUAL FUEL LR2 TANKER", publish_date="2026-08-06T07:58:21Z",
              tags=("ext:ob", "ext:ob:non-regulatory", "sub:ci", "sub:ci:other")),
        _item("capt-smax", "CAPITAL TANKERS CORP. ANNOUNCES THE SUCCESSFUL DELIVERY OF ONE "
              "DUAL FUEL SUEZMAX TANKER", publish_date="2026-08-13T05:31:58Z",
              tags=("ext:ob", "ext:ob:non-regulatory", "sub:ci", "sub:ci:other")),
    ]
    kept = {i["news_id"] for i in dedupe([i for i in misses if nw._relevant(i)])}
    assert kept == {i["news_id"] for i in misses}, "a historical miss was filtered out"


def test_noise_filter_drops_only_insider_dealing_notices():
    insider = _item("ins", "Transaction by primary insider", tags=(":regulatory", "sub:ci:insider"))
    keeper = _item("keep", "Financial calendar", tags=(":regulatory", "sub:ci", "sub:ci:calendar"))
    assert not nw._relevant(insider)
    assert nw._relevant(keeper)


def test_noise_filter_is_not_defeated_by_the_untagged_twin(tmp_path, monkeypatch):
    """The deny-list must be applied AFTER the twin collapse, not before.

    Live case (BRUT 2026-06-19 PDMR notice): the mfn copy carries
    `sub:ci:insider`, the Oslo mirror carries only `:regulatory`. Filtering
    per-copy drops the tagged one and emits the untagged one, so the filter
    silently fails for the single class it exists to exclude.
    """
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    mfn = _item("pdmr-mfn", "Mandatory Notification of Trade by PDMR",
                publish_date="2026-06-19T06:00:00Z",
                tags=(":regulatory", ":regulatory:listing", "sub:ci", "sub:ci:insider"))
    ob = _item("pdmr-ob", "BRUT: Mandatory Notification of Trade by PDMR",
               publish_date="2026-06-19T06:00:02Z", source="ob", tags=(":regulatory",))
    state = {"bruton-limited": {"bootstrapped": True, "seen_ids": [], "watermark": "2026-01-01"}}
    lines, _ = poll_slug("BRUT", "bruton-limited", state, fetch=_fake_fetch(_feed([mfn, ob])))
    assert lines == [], f"insider notice leaked via its untagged twin: {lines}"


def test_seen_ids_cap_retains_the_NEWEST_ids(tmp_path, monkeypatch):
    """dedupe() returns ascending, so a bare [:200] would keep the OLDEST ids
    and let recent releases fall out of the seen-set — the inverse of the
    property that makes the cap safe in edgar_poll/hkex_poll."""
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    monkeypatch.setattr(nw, "SEEN_CAP", 3)
    items = [_item(f"n{n}", f"Release {n}", publish_date=f"2026-0{n}-01T06:00:00Z")
             for n in range(1, 7)]
    state = {}
    poll_slug("BRUT", "bruton-limited", state, fetch=_fake_fetch(_feed(items)))
    assert state["bruton-limited"]["seen_ids"] == ["n6", "n5", "n4"]


def test_empty_feed_response_does_not_wipe_the_seen_set(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    state = {"bw-lpg": {"bootstrapped": True, "seen_ids": ["keep-1", "keep-2"],
                        "watermark": "2026-01-01"}}
    lines, _ = poll_slug("BWLP", "bw-lpg", state, fetch=_fake_fetch(_feed([])))
    assert lines == []
    assert state["bw-lpg"]["seen_ids"] == ["keep-1", "keep-2"]


def test_is_report_marks_reports_and_not_agm_or_scheduling_notices():
    report = _item("r", "Results for the six months ended June 30, 2026",
                   tags=(":regulatory", "sub:report", "sub:report:interim",
                         "sub:report:interim:q2"))
    agm = _item("a", "Results of 2026 Annual General Meeting",
                tags=(":regulatory", "sub:ci", "sub:ci:other"))
    notice = _item("n", "Q2 2026 Financial Report Release and Earnings Presentation on 28 August",
                   tags=("ext:ob", "ext:ob:non-regulatory", "sub:ci", "sub:ci:other"))
    assert nw.is_report(report)
    assert not nw.is_report(agm), "an AGM outcome is not the periodic report"
    assert not nw.is_report(notice), "scheduling a report is not filing one"
    assert nw.release_kind(report) == "interim report"
    assert nw.release_kind(agm) == "release"


def test_manifest_line_carries_report_flag_and_attachments(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    state = {"bruton-limited": {"bootstrapped": True, "seen_ids": [], "watermark": "2026-01-01"}}
    item = _item("h1", "Results for the six months ended June 30, 2026",
                 publish_date="2026-08-13T06:00:00Z",
                 tags=(":regulatory", "sub:report", "sub:report:interim"),
                 html='<a href="https://storage.mfn.se/a/fs.pdf">fs</a>')
    lines, _ = poll_slug("BRUT", "bruton-limited", state, fetch=_fake_fetch(_feed([item])))
    assert lines[0]["report"] is True
    assert lines[0]["form"] == "interim report"
    assert lines[0]["attachments"] == ["filings/BRUT/h1_fs.pdf"]


def test_remote_publish_date_cannot_shape_the_staged_path(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    # Empty watermark so the malformed date reaches the filename builder — with
    # a real watermark it happens to sort below and gets skipped first, which is
    # defence but not the defence under test.
    state = {"bruton-limited": {"bootstrapped": True, "seen_ids": [], "watermark": ""}}
    evil = _item("e1", "Release", publish_date="../../../etc/passwd")
    lines, _ = poll_slug("BRUT", "bruton-limited", state, fetch=_fake_fetch(_feed([evil])))
    staged = lines[0]["staged_path"]
    assert ".." not in staged
    assert (tmp_path / staged).resolve().is_relative_to((tmp_path / "filings").resolve())


def test_bootstrap_is_quiet_and_sticky(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    state = {}
    fetch = _fake_fetch(_feed([_item("a", "Historic release", publish_date="2026-05-01T06:00:00Z")]))
    lines, used = poll_slug("BRUT", "bruton-limited", state, fetch=fetch)
    assert lines == [] and used == 0
    assert state["bruton-limited"]["bootstrapped"] is True
    assert state["bruton-limited"]["watermark"] == "2026-05-01"

    fetch2 = _fake_fetch(_feed([]))
    poll_slug("BRUT", "bruton-limited", state, fetch=fetch2)
    assert state["bruton-limited"]["bootstrapped"] is True


def test_new_release_stages_body_and_manifests(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    state = {"capital-tankers": {"bootstrapped": True, "seen_ids": [], "watermark": "2026-01-01"}}
    html = ('<div class="mfn-body"><p>M/T Aristodimos (155,378 DWT) delivered.</p>'
            '<a href="https://storage.mfn.se/abc/report.pdf">report</a></div>')
    item = _item("new-1", "CAPITAL TANKERS CORP. ANNOUNCES DELIVERY",
                 publish_date="2026-08-13T05:31:58Z", html=html)
    fetch = _fake_fetch(_feed([item]))
    lines, used = poll_slug("CAPT", "capital-tankers", state, fetch=fetch)

    assert len(lines) == 1 and used == 1
    line = lines[0]
    assert line["ticker"] == "CAPT"
    assert line["accession"] == "mfn-new-1"
    assert line["source"] == "newsweb"
    assert line["cik"] == "newsweb:capital-tankers"
    assert line["filed"] == "2026-08-13"
    staged = tmp_path / line["staged_path"]
    assert "Aristodimos" in staged.read_text()
    assert (tmp_path / "filings" / "CAPT" / "new-1_report.pdf").exists()
    assert "new-1" in state["capital-tankers"]["seen_ids"]


def test_seen_release_is_not_re_emitted(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    state = {"bruton-limited": {"bootstrapped": True, "seen_ids": ["dup-1"],
                                "watermark": "2026-01-01"}}
    fetch = _fake_fetch(_feed([_item("dup-1", "Already seen", publish_date="2026-08-13T06:00:00Z")]))
    lines, _ = poll_slug("BRUT", "bruton-limited", state, fetch=fetch)
    assert lines == []


def test_watermark_blocks_pre_bootstrap_history(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    state = {"bw-lpg": {"bootstrapped": True, "seen_ids": [], "watermark": "2026-08-01"}}
    old = _item("old-1", "Ancient release", publish_date="2025-03-04T06:00:00Z")
    new = _item("new-2", "Fresh release", publish_date="2026-08-14T07:00:00Z")
    fetch = _fake_fetch(_feed([old, new]))
    lines, _ = poll_slug("BWLP", "bw-lpg", state, fetch=fetch)
    assert [line["accession"] for line in lines] == ["mfn-new-2"]


def test_403_sets_backoff_and_emits_nothing():
    state = {}
    fetch = _fake_fetch(b"", status=403)
    now = datetime(2026, 8, 16, 12, 0, tzinfo=timezone.utc)
    lines, used = poll_slug("MPCC", "mpc-container-ships", state, fetch=fetch, now=now)
    assert lines == [] and used == 0
    until = datetime.fromisoformat(state["mpc-container-ships"]["backoff_until"])
    assert until - now == timedelta(minutes=nw.BACKOFF_MIN)


def test_download_cap_respected(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    state = {"bruton-limited": {"bootstrapped": True, "seen_ids": [], "watermark": "2026-01-01"}}
    html = "".join(f'<a href="https://storage.mfn.se/x{n}/doc{n}.pdf">d</a>' for n in range(5))
    fetch = _fake_fetch(_feed([_item("cap-1", "Many attachments", html=html)]))
    lines, used = poll_slug("BRUT", "bruton-limited", state, fetch=fetch, downloads_left=2)
    assert len(lines) == 1
    assert used == 2


def test_dry_run_writes_nothing(tmp_path, monkeypatch):
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    state = {"bruton-limited": {"bootstrapped": True, "seen_ids": [], "watermark": "2026-01-01"}}
    fetch = _fake_fetch(_feed([_item("dry-1", "Release", html='<a href="https://storage.mfn.se/a/b.pdf">x</a>')]))
    lines, used = poll_slug("BRUT", "bruton-limited", state, fetch=fetch, dry_run=True)
    assert len(lines) == 1 and used == 0
    assert lines[0]["staged_path"] is None
    assert not (tmp_path / "filings").exists()


def test_attachment_urls_take_pdfs_only_and_dedupe():
    html = ('<a href="https://storage.mfn.se/a/one.pdf">1</a>'
            '<a href="https://storage.mfn.se/a/one.pdf">dup</a>'
            '<a href="https://storage.mfn.se/b/esef.zip">z</a>'
            '<a href="https://storage.mfn.se/c/brand.jpeg">j</a>')
    assert attachment_urls(_item("x", "t", html=html)) == ["https://storage.mfn.se/a/one.pdf"]


def test_release_text_strips_markup_from_both_body_shapes():
    assert "Aristodimos" in release_text(
        _item("a", "t", html="<pre>M/T Aristodimos<br/>155,378 DWT</pre>"))
    assert release_text(_item("b", "t", html="<p>Smith &amp; Co</p>")) == "Smith & Co"


def test_twin_winner_flip_across_polls_does_not_re_emit(tmp_path, monkeypatch):
    """The two copies can be indexed in different polls. A poll that sees only
    the ob copy elects it; the next poll sees both and elects the richer mfn
    copy, whose news_id is unseen. Marking every id in the collapsed group as
    seen is what keeps that from emitting the same release twice."""
    monkeypatch.setattr(nw, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(nw, "ROOT", tmp_path)
    ob = _item("twin-ob", "CAPT: DELIVERY OF ONE SUEZMAX", source="ob",
               tags=(":regulatory",), publish_date="2026-08-13T05:32:00Z")
    mfn = _item("twin-mfn", "DELIVERY OF ONE SUEZMAX", source="mfn",
                tags=("ext:ob", "ext:ob:non-regulatory", "sub:ci", "sub:ci:other"),
                publish_date="2026-08-13T05:31:58Z")
    state = {"capital-tankers": {"bootstrapped": True, "seen_ids": [],
                                 "watermark": "2026-01-01"}}
    first, _ = poll_slug("CAPT", "capital-tankers", state, fetch=_fake_fetch(_feed([ob])))
    assert len(first) == 1 and first[0]["accession"] == "mfn-twin-ob"
    second, _ = poll_slug("CAPT", "capital-tankers", state,
                          fetch=_fake_fetch(_feed([ob, mfn])))
    assert second == [], f"winner flip re-emitted the release: {second}"


def test_dedupe_groups_returns_every_id_in_the_group():
    ob = _item("g-ob", "CAPT: SAME RELEASE", source="ob", tags=(":regulatory",))
    mfn = _item("g-mfn", "SAME RELEASE", source="mfn", tags=("sub:ci", "sub:ci:other"))
    groups = nw.dedupe_groups([ob, mfn])
    assert len(groups) == 1
    winner, ids = groups[0]
    assert winner["news_id"] == "g-mfn"
    assert sorted(ids) == ["g-mfn", "g-ob"]
