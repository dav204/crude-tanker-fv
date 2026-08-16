"""Oslo/Euronext issuer-release poller — the ISSUER CHANNEL the book lacked.

The third venue adapter after edgar_poll.py (SEC) and hkex_poll.py (HKEX), and
the one `edgar_poll.covered_ciks` promised in its own docstring: *"Oslo names
carry sec_edgar: null and are correctly absent (their net is the calendar +
FILING-OVERDUE until the Oslo poller follow-up)."* This is that follow-up.

WHY IT EXISTS. Every Oslo/Euronext name in the book (BRUT, MPCC, CAPT, BWLP)
had NO filing lane at all — no EDGAR, no HKEX. The only channel that could see
their corporate actions was the weekly agent news sweep, and when that sweep
lapsed for eight weeks nothing caught it. The cost is on the record:

  - BRUT 2026-07-07 — demerger + first delivery + sale-leaseback + CEO change,
    unread five weeks, into a frozen report-day prereg.
  - MPCC 2026-06-25 — 4 ships / $340m + a $375m loan, unread seven weeks.
  - MPCC 2026-06-30..07-02 — a completed placement of 44,370,027 shares,
    EXACTLY +10.0% of the share count the model still carries. A denominator
    change that no scanner in the repo could see.
  - CAPT 2026-08-06 and 2026-08-13 — two newbuild DELIVERIES (§9.6 schedule
    moves) plus $117.5m of new financing, both missed by the sweep built to
    catch them, because that sweep read trade press instead of the issuer.

The 2026-08-13 audit ruled the cause was NOT a lost archive file — Pareto was
source-quiet and nothing existed to backfill. The load-bearing cause was the
absence of THIS channel.

RELEVANCE, and the trap in it. MFN tags every item, and the obvious filter —
keep `:regulatory` and `ext:ob:inside-information` — is WRONG. Verified against
the live feeds 2026-08-16: CAPT's two vessel deliveries carry
`ext:ob:non-regulatory`, the same tag as the noise bucket. An allowlist filter
would have dropped the exact releases that motivated this module. So the filter
is NEAR-INCLUSIVE — everything except an explicitly justified noise set — which
is affordable because post-dedup volume is ~2-4 releases per issuer per month.
A missed demerger costs weeks; a surplus insider notice costs one line.

DEDUP. Each release can arrive twice: `source: "ob"` is the Oslo Børs NewsWeb
mirror (title prefixed `TICKER: `, body in <pre>), `source: "mfn"` the issuer's
own distribution (richer tags, clean HTML). They publish seconds apart under
DIFFERENT news_id AND different group_id, so identity must key on (publish
date, normalized title). Measured 2026-08-16: 16 duplicate pairs across the
four covered feeds. Emitting both would double-count into the same manifest the
2026-08-09 unnamed-print duplicate rule already had to be written for.

Politeness mirrors hkex_poll: serialized requests at >=500ms, contact
User-Agent, >=60min persisted backoff on 403/429, <=10 document downloads per
run, quiet bootstrap. No conditional GETs — mfn.se sends neither ETag nor
Last-Modified (verified 2026-08-16), and its HEAD handler returns text/html for
a JSON resource, so a HEAD probe cannot be trusted either.

Coverage comes from `mfn_slug:` keys in inputs/data_sources.yaml, the per-ticker
analog of `sec_edgar:` (EDGAR) and `hkex_stockid:` (HKEX).

  python -m crude_tanker_fv.newsweb_poll [--dry-run] [--all]
"""

from __future__ import annotations

import argparse
import html as htmllib
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
STATE_FILE = ROOT / "state" / "newsweb_poll.json"
FILINGS_DIR = INPUTS / "filings"

HOST = "https://mfn.se"
USER_AGENT = "crude-tanker-fv research (dav204@gmail.com)"
REQUEST_SPACING_S = 0.5
BACKOFF_MIN = 60
MAX_DOCS_PER_RUN = 10
OFF_SEASON_POLL_HOURS = 12
SEEN_CAP = 200

# Excluded, each with its reason. Kept deliberately tiny — see RELEVANCE above.
# `sub:ci:insider` is the primary-insider dealing notice (PDMR mandatory
# disclosure): high volume, never a NAV input. Everything else is kept.
NOISE_TAGS = frozenset({"sub:ci:insider"})

# Attachments worth staging. Excludes the .zip (ESEF XBRL bundles) and .jpeg
# (brand images) also seen on these feeds.
ATTACHMENT_RE = re.compile(r"https://storage\.mfn\.se/[^\s\"'<>)]+\.pdf", re.I)

_TICKER_PREFIX_RE = re.compile(r"^\s*[A-Z0-9]{2,6}\s*[:\-–]\s*")
_TAG_RE = re.compile(r"<[^>]+>")
# The two copies of one release are retyped, not copied: the ob mirror renders
# the issuer's en-dash as whitespace (verified on CAPT's 2026-06-04 ex-dividend
# pair, which leaked through a whitespace-only normalization). Punctuation is
# therefore not identity — words are.
_PUNCT_RE = re.compile(r"[^\w\s]+", re.UNICODE)


def covered_slugs(inputs_dir: Path = INPUTS) -> "dict[str, str]":
    """ticker -> MFN issuer slug, from mfn_slug keys in data_sources.yaml."""
    doc = yaml.safe_load((inputs_dir / "data_sources.yaml").read_text())
    out = {}
    for ticker, entry in doc.items():
        if isinstance(entry, dict) and entry.get("mfn_slug"):
            out[str(ticker)] = str(entry["mfn_slug"])
    return out


def feed_url(slug: str) -> str:
    return f"{HOST}/all/a/{slug}.json"


def normalize_title(title: str) -> str:
    """Dedup key half: strip the `TICKER: ` prefix the Oslo Børs mirror adds,
    drop punctuation, collapse whitespace. Reduces to the word sequence, which
    is what the two copies of one release actually share. Entities are decoded
    first — the two copies are retyped independently, so one may carry `&amp;`
    where the other carries `&`, and after the punctuation strip that would
    otherwise become the content word "amp" on one side only."""
    stripped = _TICKER_PREFIX_RE.sub("", htmllib.unescape(title or ""))
    return re.sub(r"\s+", " ", _PUNCT_RE.sub(" ", stripped)).strip().casefold()


def is_report(item: dict) -> bool:
    """Does this release carry the issuer's periodic REPORT?

    Load-bearing beyond classification: `sentinel._filing_event_flags` clears
    FILING-OVERDUE on any manifest arrival, and FILING-OVERDUE is the Oslo
    names' only net. Without this distinction a routine ex-dividend or
    financial-calendar notice would silence the overdue flag for a report that
    never landed — i.e. adding this poller would have REMOVED a safety net.

    MFN's `sub:report*` namespace is the discriminator, and it is more precise
    than title keywords: verified across all four feeds 2026-08-16, it excludes
    "Results of Annual General Meeting" (an AGM outcome, not a report) and
    "Q2 2026 Financial Report Release ... on 28 August" (a scheduling notice
    for a future report) while catching the real reports on both twin sources.
    """
    return any(t.startswith("sub:report") for t in _tags(item))


def release_kind(item: dict) -> str:
    """Short human label for the manifest `form` field — what the sentinel's
    FILING-LANDED line renders. The raw tag list is machine noise in a pager."""
    tags = _tags(item)
    if any(t.startswith("sub:report:annual") for t in tags):
        return "annual report"
    if any(t.startswith("sub:report:interim") for t in tags):
        return "interim report"
    if any(t.startswith("sub:report") for t in tags):
        return "report"
    if "ext:ob:inside-information" in tags:
        return "inside information"
    if any(t.startswith("sub:ca") for t in tags):
        return "corporate action"
    if any(t.startswith("sub:ci:calendar") for t in tags):
        return "financial calendar"
    return "release"


def _published(item: dict) -> str:
    return str((item.get("content") or {}).get("publish_date") or "")


def _tags(item: dict) -> "set[str]":
    return set((item.get("properties") or {}).get("tags") or [])


def _relevant(item: dict) -> bool:
    return not (_tags(item) & NOISE_TAGS)


def parse_feed(body: bytes) -> "list[dict]":
    """JSON Feed 1.x envelope -> item dicts."""
    doc = json.loads(body)
    items = doc.get("items") if isinstance(doc, dict) else doc
    return [i for i in (items or []) if isinstance(i, dict)]


def dedupe_groups(items: "list[dict]") -> "list[tuple[dict, list[str]]]":
    """Collapse the ob/mfn twins on (date, normalized title), keeping the copy
    with the richer tag set — that is the issuer distribution, whose tags carry
    the inside-information and corporate-action classifications.

    Returns (winner, every news_id in the group). The alias ids matter: the two
    copies can be indexed in different polls, so a poll that sees only the ob
    copy records ob's id, and the next poll — now seeing both — would elect the
    mfn copy, whose id is unseen, and re-emit the same release. Marking every
    id in the group as seen makes the collapse stable across that flip.
    """
    best: "dict[tuple, dict]" = {}
    group_ids: "dict[tuple, list[str]]" = {}
    for item in items:
        key = (_published(item)[:10], normalize_title((item.get("content") or {}).get("title", "")))
        nid = str(item.get("news_id") or "")
        if nid:
            group_ids.setdefault(key, []).append(nid)
        prior = best.get(key)
        if prior is None or len(_tags(item)) > len(_tags(prior)):
            best[key] = item
    ordered = sorted(best.items(), key=lambda kv: _published(kv[1]))
    return [(item, group_ids.get(key, [])) for key, item in ordered]


def dedupe(items: "list[dict]") -> "list[dict]":
    return [winner for winner, _ in dedupe_groups(items)]


def attachment_urls(item: dict) -> "list[str]":
    body = (item.get("content") or {}).get("html") or ""
    seen, out = set(), []
    for url in ATTACHMENT_RE.findall(htmllib.unescape(body)):
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def release_text(item: dict) -> str:
    """Plain text of the release body — the thing the sweep actually reads."""
    body = (item.get("content") or {}).get("html") or ""
    text = _TAG_RE.sub("", body.replace("<br/>", "\n").replace("</p>", "\n"))
    return re.sub(r"\n{3,}", "\n\n", htmllib.unescape(text)).strip()


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


def poll_slug(ticker: str, slug: str, state: dict, *, fetch=_fetch,
              dry_run: bool = False, downloads_left: int = MAX_DOCS_PER_RUN,
              now=None) -> "tuple[list[dict], int]":
    """Poll one issuer feed; returns (new manifest lines, downloads used)."""
    now = now or datetime.now(timezone.utc)
    st = state.setdefault(slug, {})

    status, body, _ = fetch(feed_url(slug), {})
    if status in (403, 429):
        st["backoff_until"] = (now + timedelta(minutes=BACKOFF_MIN)).isoformat()
        print(f"{ticker}: HTTP {status} — backing off {BACKOFF_MIN}min", file=sys.stderr)
        return [], 0
    st["last_polled"] = now.isoformat()
    if status != 200:
        print(f"{ticker}: HTTP {status} on MFN feed", file=sys.stderr)
        return [], 0
    try:
        # COLLAPSE BEFORE FILTERING, never the reverse. Filtering per-copy makes
        # the deny-list only as strong as the weaker-tagged twin: BRUT's real
        # 2026-06-19 PDMR notice carries `sub:ci:insider` on the mfn copy and a
        # bare `:regulatory` on the ob copy, so filter-then-collapse drops the
        # tagged copy and emits the untagged one. Verified on the live feed:
        # shipped order emitted 1 line, this order emits 0.
        groups = [(i, g) for i, g in dedupe_groups(parse_feed(body)) if _relevant(i)]
    except (ValueError, json.JSONDecodeError):
        print(f"{ticker}: unparseable MFN feed payload", file=sys.stderr)
        return [], 0

    items = [i for i, _ in groups]
    # Every id in a collapsed group, so a winner flip across polls cannot
    # re-emit the release (see dedupe_groups).
    ids = [nid for _, g in groups for nid in g]
    if not st.get("bootstrapped"):
        # NEWEST-first before the cap. dedupe() returns ascending, so a bare
        # [:200] would retain the OLDEST ids and let recent releases fall out
        # of the seen-set — the inverse of the property that makes the cap safe
        # in edgar_poll/hkex_poll, whose upstream indexes are newest-first.
        st["seen_ids"] = [i for i in reversed(ids) if i][:SEEN_CAP]
        st["watermark"] = max((_published(i)[:10] for i in items if _published(i)),
                              default=str(date.today()))
        st["bootstrapped"] = True
        print(f"{ticker}: bootstrap — {len(items)} releases marked seen "
              f"(watermark {st['watermark']})")
        return [], 0

    seen = set(st.get("seen_ids", []))
    watermark = st.get("watermark", "1900-01-01")
    lines: "list[dict]" = []
    used = 0
    for item, group in groups:
        news_id = str(item.get("news_id") or "")
        published = _published(item)[:10]
        if not news_id or seen.intersection(group) or (published and published < watermark):
            continue
        title = (item.get("content") or {}).get("title") or ""
        staged = None
        attachments: "list[str]" = []
        if not dry_run:
            # Both path components are remote-supplied; neither may shape a path.
            safe = re.sub(r"[^A-Za-z0-9._-]", "_", news_id)[:60]
            safe_date = re.sub(r"[^0-9-]", "_", published) or "undated"
            dest_dir = FILINGS_DIR / ticker
            dest_dir.mkdir(parents=True, exist_ok=True)
            body_path = dest_dir / f"newsweb_{safe_date}_{safe}.txt"
            body_path.write_text(f"{title}\n{item.get('url', '')}\n{published}\n\n"
                                 f"{release_text(item)}\n")

            def _rel(p: Path) -> str:
                try:
                    return str(p.relative_to(ROOT))
                except ValueError:
                    return str(p)

            staged = _rel(body_path)
            for url in attachment_urls(item):
                if used >= downloads_left:
                    print(f"{ticker}: download cap reached — {url} NOT staged "
                          f"(release {news_id} is on the manifest without it)",
                          file=sys.stderr)
                    break
                time.sleep(REQUEST_SPACING_S)
                s2, b2, _ = fetch(url, {})
                if s2 == 200 and b2:
                    dest = dest_dir / f"{safe}_{Path(url).name}"
                    dest.write_bytes(b2)
                    attachments.append(_rel(dest))
                    used += 1
        lines.append({
            "ts": now.isoformat(timespec="seconds"), "ticker": ticker,
            "cik": f"newsweb:{slug}", "accession": f"mfn-{news_id}",
            "form": release_kind(item),
            "filed": published, "primary_doc": str(item.get("url") or ""),
            "staged_path": staged, "amended": False, "source": "newsweb",
            # `report` gates sentinel FILING-OVERDUE: a routine release must NOT
            # count as the periodic report landing. Absent on edgar/hkex lines,
            # which the sentinel defaults to True so their behaviour is unchanged.
            "report": is_report(item),
            "title": title[:200], "attachments": attachments,
        })
        seen.update(group)
    if ids:
        # Only re-derive the seen-set from a feed that actually returned items.
        # A 200 carrying an empty list would otherwise wipe it, and the next
        # good poll would re-emit and re-download everything above the watermark.
        st["seen_ids"] = [i for i in reversed(ids) if i in seen][:SEEN_CAP]
    return lines, used


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(description="Oslo/Euronext issuer-release poller (staging-only)")
    ap.add_argument("--dry-run", action="store_true",
                    help="detect + manifest, no body/attachment writes")
    ap.add_argument("--all", action="store_true",
                    help="ignore the off-season 12h cadence filter (poll every name)")
    args = ap.parse_args(argv)

    from .edgar_poll import _in_window

    slugs = covered_slugs()
    state = _load_state()
    now = datetime.now(timezone.utc)
    total_new, total_docs = 0, 0
    for ticker, slug in sorted(slugs.items()):
        st = state.get(slug, {})
        if st.get("backoff_until") and datetime.fromisoformat(st["backoff_until"]) > now:
            print(f"{ticker}: in backoff until {st['backoff_until']}")
            continue
        if not args.all and not _in_window(ticker, INPUTS):
            last = st.get("last_polled")
            if last and (now - datetime.fromisoformat(last)) < timedelta(hours=OFF_SEASON_POLL_HOURS):
                continue
        time.sleep(REQUEST_SPACING_S)
        lines, used = poll_slug(ticker, slug, state, dry_run=args.dry_run,
                                downloads_left=MAX_DOCS_PER_RUN - total_docs, now=now)
        total_docs += used
        for line in lines:
            record_manifest_line(line)
            print(f"{ticker}: NEW {line['filed']} {line['title'][:70]} "
                  f"-> {line['staged_path'] or 'manifest-only'}")
        total_new += len(lines)
    _save_state(state)
    print(f"polled {len(slugs)} names: {total_new} new release(s), {total_docs} doc(s) staged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
