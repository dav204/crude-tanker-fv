"""HKEXnews filings poller — the venue-annex light adapter (F-3, Stage-3 intake).

The HKEX counterpart of edgar_poll.py, scoped exactly to the venue annex's
commitment (`../portfolio-governance/funnels/drybulk_2026H2/venue_annex.md`,
HKEX section): poll the per-company HKEXnews JSON index
(`titleSearchServlet.do?stockId=<id>`), stage new relevant filings' PDFs to
inputs/filings/<ticker>/ (gitignored), and append arrival lines to the SAME
state-side manifest edgar_poll writes (state/edgar_manifest.jsonl) with
`source: "hkexnews"` — so FILING-LANDED paging (sentinel), the draft queue,
and the commit_drift snapshot all work unchanged. Identity: HKEX NEWS_ID
plays the accession role (invariant 4); FILE_LINK is the fallback.

Coverage comes from `hkex_stockid:` keys in inputs/data_sources.yaml (the
per-ticker analog of the sec_edgar CIK URLs). Listing the HKEXnews URLs in
that entry also puts www1.hkexnews.hk on the fetch_pdf.py allowlist — the
annex's "one host entry" is the data_sources entry itself.

Politeness mirrors edgar_poll but more conservatively — the endpoint is the
search UI's undocumented-but-stable backend, not a published contract:
serialized requests at >=500ms spacing, contact User-Agent, >=60min persisted
backoff on 403/429, <=10 document downloads per run, quiet bootstrap (history
is not an event). No conditional GETs (the servlet doesn't honor them);
HK's semi-annual reporting cadence keeps polling load trivial.

  python -m crude_tanker_fv.hkex_poll [--dry-run] [--all]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

from .edgar_poll import record_manifest_line

ROOT = Path(__file__).resolve().parents[2]
INPUTS = ROOT / "inputs"
STATE_FILE = ROOT / "state" / "hkex_poll.json"
FILINGS_DIR = INPUTS / "filings"

HOST = "https://www1.hkexnews.hk"
USER_AGENT = "crude-tanker-fv research (dav204@gmail.com)"
REQUEST_SPACING_S = 0.5
BACKOFF_MIN = 60
MAX_DOCS_PER_RUN = 10
OFF_SEASON_POLL_HOURS = 12

# HKEX has no form-code taxonomy; relevance keys on the filing category text
# (SHORT_TEXT, falling back to TITLE). The set mirrors the EDGAR RELEVANT_FORMS
# intent: reports of record + results + the 8-K-analog announcements category +
# monthly returns (the share-count source the Stage-2 packet already used).
# Deliberately excluded noise: "Next Day Disclosure Return" (daily buyback
# prints), trading-halt notices, listing documents of other issuers.
# Excluded governance boilerplate (2026-09-02, prune ledger row 11): committee
# terms of reference, corporate-governance notices and "Circulars - [Other]"
# carry no figure, no date and no event — most of August's 2343 pages.
EXCLUDED_KEYWORDS = (
    "next day disclosure return", "terms of reference",
    "corporate governance", "circulars - [other]",
)
RELEVANT_KEYWORDS = (
    "annual report", "interim report", "quarterly report",
    "final results", "interim results", "results announcement",
    "monthly return", "circular", "announcements and notices",
)


def covered_stockids(inputs_dir: Path = INPUTS) -> "dict[str, str]":
    """ticker -> HKEXnews stockId, from hkex_stockid keys in data_sources.yaml."""
    doc = yaml.safe_load((inputs_dir / "data_sources.yaml").read_text())
    out = {}
    for ticker, entry in doc.items():
        if isinstance(entry, dict) and entry.get("hkex_stockid"):
            out[ticker] = str(entry["hkex_stockid"])
    return out


def _clean(text: str) -> str:
    """SHORT_TEXT carries HTML tags on the live servlet ('Monthly Returns<br/>')."""
    return re.sub(r"<[^>]+>", "", text or "").strip()


def _relevant(row: dict) -> bool:
    text = f"{_clean(row.get('SHORT_TEXT'))} {_clean(row.get('TITLE'))}".lower()
    if any(x in text for x in EXCLUDED_KEYWORDS):
        return False
    return any(k in text for k in RELEVANT_KEYWORDS)


def _filed_date(row: dict) -> str:
    """DATE_TIME 'dd/mm/yyyy HH:MM' (or date-only) -> ISO date; '' if unparseable."""
    raw = str(row.get("DATE_TIME") or "").strip()
    for fmt in ("%d/%m/%Y %H:%M", "%d/%m/%Y"):
        try:
            return datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            continue
    return ""


def _news_id(row: dict) -> str:
    nid = str(row.get("NEWS_ID") or "").strip()
    return nid or str(row.get("FILE_LINK") or "").strip()


def parse_index(body: bytes) -> "list[dict]":
    """titleSearchServlet JSON -> row dicts. The servlet's `result` field is a
    JSON-encoded STRING inside the JSON envelope (verified on stockId 7703);
    tolerate the already-a-list shape too."""
    doc = json.loads(body)
    result = doc.get("result") if isinstance(doc, dict) else doc
    if isinstance(result, str):
        result = json.loads(result) if result.strip() else []
    return [r for r in (result or []) if isinstance(r, dict)]


def _load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def _save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".json.part")
    tmp.write_text(json.dumps(state, indent=1, sort_keys=True))
    tmp.replace(STATE_FILE)


def _fetch(url: str, headers: dict) -> "tuple[int, bytes, dict]":
    """One HTTP GET (module seam — tests stub this)."""
    req = urllib.request.Request(url, headers=dict(headers, **{"User-Agent": USER_AGENT}))
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as exc:
        return exc.code, b"", dict(exc.headers or {})


def index_url(stock_id: str) -> str:
    return (f"{HOST}/search/titleSearchServlet.do?sortDir=0"
            f"&sortByOptions=DateTime&category=0&market=SEHK"
            f"&stockId={stock_id}&documentType=-1&searchType=1")


def poll_stockid(ticker: str, stock_id: str, state: dict, *, fetch=_fetch,
                 dry_run: bool = False, downloads_left: int = MAX_DOCS_PER_RUN,
                 now=None) -> "tuple[list[dict], int]":
    """Poll one stockId; returns (new manifest lines, downloads used)."""
    now = now or datetime.now(timezone.utc)
    st = state.setdefault(stock_id, {})

    status, body, _ = fetch(index_url(stock_id), {})
    if status in (403, 429):
        st["backoff_until"] = (now + timedelta(minutes=BACKOFF_MIN)).isoformat()
        print(f"{ticker}: HTTP {status} — backing off {BACKOFF_MIN}min", file=sys.stderr)
        return [], 0
    st["last_polled"] = now.isoformat()
    if status != 200:
        print(f"{ticker}: HTTP {status} on HKEXnews index", file=sys.stderr)
        return [], 0
    try:
        rows = parse_index(body)
    except (ValueError, json.JSONDecodeError):
        print(f"{ticker}: unparseable HKEXnews index payload", file=sys.stderr)
        return [], 0

    relevant = [(r, _news_id(r), _filed_date(r)) for r in rows if _relevant(r)]
    relevant = [(r, nid, filed) for r, nid, filed in relevant if nid]

    seen = set(st.get("seen_ids", []))
    if not st.get("bootstrapped"):
        # Quiet bootstrap: history is not an event (edgar_poll invariant,
        # incl. the sticky-on-zero-relevant case and the date watermark that
        # makes the seen cap safe against deep archives).
        st["seen_ids"] = [nid for _, nid, _ in relevant][:200]
        st["watermark"] = max((f for _, _, f in relevant if f),
                              default=str(date.today()))
        st["bootstrapped"] = True
        print(f"{ticker}: bootstrap — {len(relevant)} relevant filings marked seen "
              f"(watermark {st['watermark']})")
        return [], 0

    watermark = st.get("watermark", "1900-01-01")
    lines: list[dict] = []
    used = 0
    for row, nid, filed in relevant:
        if nid in seen or (filed and filed < watermark):
            continue
        file_link = str(row.get("FILE_LINK") or "").strip()
        staged = None
        if not dry_run and file_link and used < downloads_left:
            doc_url = file_link if file_link.startswith("http") else (
                HOST + (file_link if file_link.startswith("/") else "/" + file_link))
            time.sleep(REQUEST_SPACING_S)
            s2, b2, _ = fetch(doc_url, {})
            if s2 == 200 and b2:
                safe_nid = re.sub(r"[^A-Za-z0-9._-]", "_", nid)
                dest = FILINGS_DIR / ticker / f"{safe_nid}_{Path(file_link).name}"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(b2)
                try:
                    staged = str(dest.relative_to(ROOT))
                except ValueError:   # staging dir outside ROOT (tests)
                    staged = str(dest)
                used += 1
        line = {"ts": now.isoformat(timespec="seconds"), "ticker": ticker,
                "cik": f"hkex:{stock_id}", "accession": f"hkex-{nid}",
                "form": _clean(row.get("SHORT_TEXT") or row.get("TITLE") or "")[:80],
                "filed": filed, "primary_doc": file_link, "staged_path": staged,
                "amended": False, "source": "hkexnews"}
        lines.append(line)
        seen.add(nid)
    st["seen_ids"] = [nid for _, nid, _ in relevant if nid in seen][:200]
    return lines, used


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(description="HKEXnews filings poller (staging-only)")
    ap.add_argument("--dry-run", action="store_true",
                    help="detect + manifest, no document downloads")
    ap.add_argument("--all", action="store_true",
                    help="ignore the off-season 12h cadence filter (poll every name)")
    args = ap.parse_args(argv)

    from .edgar_poll import _in_window

    stockids = covered_stockids()
    state = _load_state()
    now = datetime.now(timezone.utc)
    total_new, total_docs = 0, 0
    for ticker, stock_id in sorted(stockids.items()):
        st = state.get(stock_id, {})
        if st.get("backoff_until") and datetime.fromisoformat(st["backoff_until"]) > now:
            print(f"{ticker}: in backoff until {st['backoff_until']}")
            continue
        if not args.all and not _in_window(ticker, INPUTS):
            last = st.get("last_polled")
            if last and (now - datetime.fromisoformat(last)) < timedelta(hours=OFF_SEASON_POLL_HOURS):
                continue
        time.sleep(REQUEST_SPACING_S)
        lines, used = poll_stockid(ticker, stock_id, state, dry_run=args.dry_run,
                                   downloads_left=MAX_DOCS_PER_RUN - total_docs, now=now)
        total_docs += used
        for line in lines:
            record_manifest_line(line)
            print(f"{ticker}: NEW {line['form']} {line['accession']} "
                  f"filed {line['filed']} -> {line['staged_path'] or 'manifest-only'}")
        total_new += len(lines)
    _save_state(state)
    print(f"polled {len(stockids)} names: {total_new} new filing(s), {total_docs} doc(s) staged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
