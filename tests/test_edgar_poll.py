"""EDGAR poller (WO2 2.2): CIK discovery, quiet bootstrap, new-accession
detection with amended flag, conditional GETs, backoff, download cap. All
network stubbed at the module's fetch seam."""

import json
from datetime import datetime, timedelta, timezone

import crude_tanker_fv.edgar_poll as ep
from crude_tanker_fv.edgar_poll import covered_ciks, poll_cik


def _submissions(accessions_forms):
    # Filed "tomorrow" so fixtures always clear a today-defaulted bootstrap
    # watermark (an empty-relevant bootstrap watermarks at date.today()).
    from datetime import date, timedelta

    filed = (date.today() + timedelta(days=1)).isoformat()
    recent = {"accessionNumber": [a for a, _ in accessions_forms],
              "form": [f for _, f in accessions_forms],
              "filingDate": [filed] * len(accessions_forms),
              "primaryDocument": [f"doc{i}.htm" for i in range(len(accessions_forms))]}
    return json.dumps({"filings": {"recent": recent}}).encode()


def _fake_fetch(payload, doc_body=b"<html>filing</html>", status=200):
    calls = []

    def fetch(url, headers):
        calls.append((url, headers))
        if "data.sec.gov" in url:
            return status, payload, {"ETag": "abc123"}
        return 200, doc_body, {}
    fetch.calls = calls
    return fetch


# Every CIK verified against SEC company_tickers.json 2026-07-03 (WO2 2.2).
# The sweep caught THREE wrong CIKs that had sat in data_sources.yaml: FLNG
# pointed at a Form-D fund, CCEC at Blackstone's BXSL, INSW at nothing — three
# names whose filings the poller would have silently missed all season. This
# pin is the two-surfaces rule: re-verify against SEC before changing a value.
VERIFIED_CIKS = {
    "ASC": "0001577437", "CCEC": "0001392326", "CMBT": "0001604481",
    "CMDB": "0002033535", "DHT": "0001331284", "ECO": "0001964954",
    "FLNG": "0001772253", "FRO": "0000913290", "GNK": "0001326200",
    "GSL": "0001430725", "HAFN": "0001815779", "INSW": "0001679049",
    "NAT": "0001000177", "SB": "0001434754", "SBLK": "0001386716",
    "STNG": "0001483934", "TEN": "0001166663", "TNK": "0001419945",
    "TRMD": "0001655891",
    # LPG validators (WO3 Phase 4): verified against SEC company_tickers.json
    # 2026-07-09 (LPG -> "DORIAN LPG LTD.", BWLP -> "BW LPG Ltd", exact match
    # both — the FLNG/CCEC/INSW wrong-CIK class ruled out) and re-confirmed
    # 2026-07-10 by pulling both submissions JSONs at onboarding.
    "LPG": "0001596993", "BWLP": "0001649313",
    # Stage-3 intake prep (2026-07-14): PANL verified against SEC
    # company_tickers.json same day (1606909 -> "Pangaea Logistics Solutions
    # Ltd.", exact match). Entry added at Stage-3 PREP so the poller watches
    # filings pre-onboarding; 2343 is HKEX (sec_edgar: null, hkex_poll.py).
    "PANL": "0001606909",
}


def test_covered_ciks_match_the_verified_pin():
    ciks = covered_ciks()
    assert ciks == VERIFIED_CIKS, (
        f"diff: {set(ciks.items()) ^ set(VERIFIED_CIKS.items())} — a CIK change "
        "must be re-verified against SEC company_tickers.json and re-pinned")
    for oslo in ("BRUT", "CAPT", "MPCC"):
        assert oslo not in ciks   # Oslo names: no SEC filings by design


def test_bootstrap_is_quiet_and_sticky(tmp_path, monkeypatch):
    monkeypatch.setattr(ep, "FILINGS_DIR", tmp_path / "filings")
    fetch = _fake_fetch(_submissions([("0001-26-000001", "6-K")]))
    state = {}
    lines, used = poll_cik("DHT", "0001331284", state, fetch=fetch)
    assert lines == [] and used == 0
    assert state["0001331284"]["bootstrapped"] is True

    # A CIK with ZERO relevant recent forms must also bootstrap sticky —
    # not re-bootstrap forever and eat its first real filing.
    fetch2 = _fake_fetch(_submissions([("0002-26-000001", "SC 13G")]))
    state2 = {}
    poll_cik("TNK", "0001419945", state2, fetch=fetch2)
    assert state2["0001419945"]["bootstrapped"] is True
    fetch3 = _fake_fetch(_submissions([("0002-26-000001", "SC 13G"),
                                       ("0002-26-000002", "6-K")]))
    lines, _ = poll_cik("TNK", "0001419945", state2, fetch=fetch3)
    assert [l["accession"] for l in lines] == ["0002-26-000002"]


def test_new_accession_stages_manifests_and_flags_amended(tmp_path, monkeypatch):
    monkeypatch.setattr(ep, "FILINGS_DIR", tmp_path / "filings")
    state = {"0001331284": {"bootstrapped": True,
                            "seen_accessions": ["0001-26-000001"]}}
    fetch = _fake_fetch(_submissions([("0001-26-000002", "6-K/A"),
                                      ("0001-26-000001", "6-K")]))
    lines, used = poll_cik("DHT", "0001331284", state, fetch=fetch)
    assert len(lines) == 1 and used == 1
    line = lines[0]
    assert line["accession"] == "0001-26-000002"
    assert line["form"] == "6-K/A" and line["amended"] is True
    assert line["staged_path"] and (ep.ROOT / line["staged_path"]).name.startswith(
        "0001-26-000002_6-KA")
    assert (tmp_path / "filings" / "DHT").exists()
    # second poll: nothing new
    lines2, _ = poll_cik("DHT", "0001331284", state, fetch=fetch)
    assert lines2 == []


def test_watermark_blocks_pre_bootstrap_history(tmp_path, monkeypatch):
    """Live-bootstrap catch (2026-07-03): `recent` can hold 577 relevant
    filings while seen caps at 200 — anything filed before the bootstrap
    watermark is history, never an event, even when absent from seen."""
    monkeypatch.setattr(ep, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(ep, "REQUEST_SPACING_S", 0)
    state = {"0001331284": {"bootstrapped": True, "watermark": "2026-07-03",
                            "seen_accessions": ["0001-26-000200"]}}
    recent = {"accessionNumber": ["0001-26-000201", "0001-15-000042"],
              "form": ["6-K", "6-K"],
              "filingDate": ["2026-07-05", "2015-03-01"],
              "primaryDocument": ["a.htm", "b.htm"]}
    payload = json.dumps({"filings": {"recent": recent}}).encode()
    lines, _ = poll_cik("DHT", "0001331284", state, fetch=_fake_fetch(payload))
    assert [l["accession"] for l in lines] == ["0001-26-000201"]


def test_conditional_get_304_short_circuits():
    state = {"0001331284": {"bootstrapped": True, "etag": "abc123",
                            "seen_accessions": ["x"]}}
    fetch = _fake_fetch(b"", status=304)
    lines, used = poll_cik("DHT", "0001331284", state, fetch=fetch)
    assert lines == [] and used == 0
    assert fetch.calls[0][1].get("If-None-Match") == "abc123"


def test_403_sets_backoff(monkeypatch):
    state = {}
    fetch = _fake_fetch(b"", status=403)
    now = datetime.now(timezone.utc)
    lines, _ = poll_cik("DHT", "0001331284", state, fetch=fetch, now=now)
    assert lines == []
    until = datetime.fromisoformat(state["0001331284"]["backoff_until"])
    assert until >= now + timedelta(minutes=29)


def test_download_cap_respected(tmp_path, monkeypatch):
    monkeypatch.setattr(ep, "FILINGS_DIR", tmp_path / "filings")
    monkeypatch.setattr(ep, "REQUEST_SPACING_S", 0)
    new = [(f"0001-26-{i:06d}", "6-K") for i in range(2, 8)]
    state = {"0001331284": {"bootstrapped": True, "seen_accessions": ["old"]}}
    fetch = _fake_fetch(_submissions(new))
    lines, used = poll_cik("DHT", "0001331284", state, fetch=fetch, downloads_left=3)
    assert len(lines) == 6           # ALL detected + manifested
    assert used == 3                 # only 3 staged
    assert sum(1 for l in lines if l["staged_path"]) == 3
