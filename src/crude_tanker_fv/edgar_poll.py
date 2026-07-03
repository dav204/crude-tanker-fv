"""EDGAR filings poller (WO2 2.2) — filings become events.

Polls each covered CIK's submissions JSON and stages new relevant filings'
primary documents to inputs/filings/<ticker>/ (gitignored). The authoritative
arrival record is STATE-SIDE (R-2): state/edgar_manifest.jsonl — one line per
new accession (invariant 4: accession number IS the identity; a /A form
carries amended=true). The sentinel reads the manifest for
FILING-LANDED/OVERDUE (2.3); commit_drift.sh promotes a snapshot for the
Action's --pure view at refresh events.

Politeness (invariant 8, the fetch_pdf 403 precedent): serialized requests
with >=200ms spacing, a contact User-Agent, conditional GETs on the
submissions JSON (ETag/Last-Modified), >=30min backoff persisted on 403/429,
and <=30 document downloads per run. Bootstrap is quiet: the first poll of a
CIK marks its recent filings seen WITHOUT downloading — history is not an
event.

Cadence (invariant 5 — the calendar modulates cadence, never gates
detection): run hourly via launchd; a name OUTSIDE an open earnings window is
polled only when its last poll is >12h old (2x/day off-season), a name inside
its window polls every run.

Staging-only writer (invariant 3): PAUSE stops it (wrapper), a dirty tree
does not — filing detection must not blind during a reconciliation week.

  python -m crude_tanker_fv.edgar_poll [--dry-run] [--all]
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

ROOT = Path(__file__).resolve().parents[2]
INPUTS = ROOT / "inputs"
STATE_FILE = ROOT / "state" / "edgar_poll.json"
MANIFEST = ROOT / "state" / "edgar_manifest.jsonl"
FILINGS_DIR = INPUTS / "filings"

USER_AGENT = "crude-tanker-fv research (dav204@gmail.com)"
RELEVANT_FORMS = {"6-K", "6-K/A", "10-Q", "10-Q/A", "10-K", "10-K/A",
                  "20-F", "20-F/A", "8-K", "8-K/A"}
REQUEST_SPACING_S = 0.25
BACKOFF_MIN = 30
MAX_DOCS_PER_RUN = 30
OFF_SEASON_POLL_HOURS = 12


def covered_ciks(inputs_dir: Path = INPUTS) -> "dict[str, str]":
    """ticker -> 10-digit CIK, from the sec_edgar URLs in data_sources.yaml.
    Oslo names carry sec_edgar: null and are correctly absent (their net is
    the calendar + FILING-OVERDUE until the Oslo poller follow-up)."""
    doc = yaml.safe_load((inputs_dir / "data_sources.yaml").read_text())
    out = {}
    for ticker, entry in doc.items():
        if not isinstance(entry, dict):
            continue
        url = entry.get("sec_edgar") or ""
        m = re.search(r"CIK=(\d+)", str(url))
        if m:
            out[ticker] = m.group(1).zfill(10)
    return out


def _in_window(ticker: str, inputs_dir: Path, today=None) -> bool:
    path = inputs_dir / "earnings_calendar.yaml"
    if not path.exists():
        return False
    cal = yaml.safe_load(path.read_text()) or {}
    e = cal.get(ticker)
    if not isinstance(e, dict) or "window_start" not in e:
        return False
    today = today or date.today()
    return (e["window_start"] - timedelta(days=1) <= today
            <= e["window_end"] + timedelta(days=3))


def _load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def _save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".json.part")
    tmp.write_text(json.dumps(state, indent=1, sort_keys=True))
    tmp.replace(STATE_FILE)   # invariant 10


def _fetch(url: str, headers: dict) -> "tuple[int, bytes, dict]":
    """One HTTP GET (module seam — tests stub this). Returns (status, body,
    response headers). 304 returns empty body."""
    req = urllib.request.Request(url, headers=dict(headers, **{"User-Agent": USER_AGENT}))
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as exc:
        return exc.code, b"", dict(exc.headers or {})


def record_manifest_line(line: dict, manifest: Path = MANIFEST) -> None:
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("a") as fh:
        fh.write(json.dumps(line) + "\n")


def poll_cik(ticker: str, cik: str, state: dict, *, fetch=_fetch,
             dry_run: bool = False, downloads_left: int = MAX_DOCS_PER_RUN,
             now=None) -> "tuple[list[dict], int]":
    """Poll one CIK; returns (new manifest lines, downloads used)."""
    now = now or datetime.now(timezone.utc)
    st = state.setdefault(cik, {})
    headers = {}
    if st.get("etag"):
        headers["If-None-Match"] = st["etag"]
    if st.get("last_modified"):
        headers["If-Modified-Since"] = st["last_modified"]

    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    status, body, resp_headers = fetch(url, headers)
    if status in (403, 429):
        st["backoff_until"] = (now + timedelta(minutes=BACKOFF_MIN)).isoformat()
        print(f"{ticker}: HTTP {status} — backing off {BACKOFF_MIN}min", file=sys.stderr)
        return [], 0
    st["last_polled"] = now.isoformat()
    if status == 304:
        return [], 0
    if status != 200:
        print(f"{ticker}: HTTP {status} on submissions JSON", file=sys.stderr)
        return [], 0
    if resp_headers.get("ETag"):
        st["etag"] = resp_headers["ETag"]
    if resp_headers.get("Last-Modified"):
        st["last_modified"] = resp_headers["Last-Modified"]

    doc = json.loads(body)
    recent = doc.get("filings", {}).get("recent", {})
    rows = list(zip(recent.get("accessionNumber", []), recent.get("form", []),
                    recent.get("filingDate", []), recent.get("primaryDocument", [])))
    relevant = [r for r in rows if r[1] in RELEVANT_FORMS]

    seen = set(st.get("seen_accessions", []))
    if not st.get("bootstrapped"):
        # Quiet bootstrap: history is not an event. Explicit flag — a CIK
        # whose recent window happens to hold zero relevant forms must not
        # re-bootstrap forever (that would eat its first real filing). The
        # date WATERMARK is what makes the 200-entry seen cap safe: STNG
        # carries 577 relevant filings in `recent` (caught on the live
        # bootstrap 2026-07-03) — without it, entries past the cap would
        # re-surface as "new" ancient filings on the next poll.
        st["seen_accessions"] = [r[0] for r in relevant][:200]
        st["watermark"] = max((r[2] for r in relevant), default=str(date.today()))
        st["bootstrapped"] = True
        print(f"{ticker}: bootstrap — {len(relevant)} relevant filings marked seen "
              f"(watermark {st['watermark']})")
        return [], 0

    watermark = st.get("watermark", "1900-01-01")
    lines: list[dict] = []
    used = 0
    for accession, form, filed, primary in relevant:
        if accession in seen or filed < watermark:
            continue
        staged = None
        if not dry_run and primary and used < downloads_left:
            acc_nodash = accession.replace("-", "")
            doc_url = (f"https://www.sec.gov/Archives/edgar/data/"
                       f"{int(cik)}/{acc_nodash}/{primary}")
            time.sleep(REQUEST_SPACING_S)
            s2, b2, _ = fetch(doc_url, {})
            if s2 == 200 and b2:
                dest = FILINGS_DIR / ticker / f"{accession}_{form.replace('/', '')}_{Path(primary).name}"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(b2)
                try:
                    staged = str(dest.relative_to(ROOT))
                except ValueError:   # staging dir outside ROOT (tests)
                    staged = str(dest)
                used += 1
        line = {"ts": now.isoformat(timespec="seconds"), "ticker": ticker,
                "cik": cik, "accession": accession, "form": form,
                "filed": filed, "primary_doc": primary, "staged_path": staged,
                "amended": form.endswith("/A")}
        lines.append(line)
        seen.add(accession)
    st["seen_accessions"] = ([r[0] for r in relevant if r[0] in seen])[:200]
    return lines, used


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(description="EDGAR filings poller (staging-only)")
    ap.add_argument("--dry-run", action="store_true",
                    help="detect + manifest, no document downloads")
    ap.add_argument("--all", action="store_true",
                    help="ignore the off-season 12h cadence filter (poll every name)")
    args = ap.parse_args(argv)

    ciks = covered_ciks()
    state = _load_state()
    now = datetime.now(timezone.utc)
    total_new, total_docs = 0, 0
    for ticker, cik in sorted(ciks.items()):
        st = state.get(cik, {})
        if st.get("backoff_until") and datetime.fromisoformat(st["backoff_until"]) > now:
            print(f"{ticker}: in backoff until {st['backoff_until']}")
            continue
        if not args.all and not _in_window(ticker, INPUTS):
            last = st.get("last_polled")
            if last and (now - datetime.fromisoformat(last)) < timedelta(hours=OFF_SEASON_POLL_HOURS):
                continue   # off-season 2x/day cadence; detection never gated, only spaced
        time.sleep(REQUEST_SPACING_S)
        lines, used = poll_cik(ticker, cik, state, dry_run=args.dry_run,
                               downloads_left=MAX_DOCS_PER_RUN - total_docs, now=now)
        total_docs += used
        for line in lines:
            record_manifest_line(line)
            tag = " AMENDED" if line["amended"] else ""
            print(f"{ticker}: NEW {line['form']}{tag} {line['accession']} "
                  f"filed {line['filed']} -> {line['staged_path'] or 'manifest-only'}")
        total_new += len(lines)
    _save_state(state)
    print(f"polled {len(ciks)} names: {total_new} new filing(s), {total_docs} doc(s) staged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
