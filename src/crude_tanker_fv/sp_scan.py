"""Scan the Pareto Shipping Daily archive for S&P prints and name mentions.

Two modes:

1. S&P PRINT SCAN (default) — feeds the transaction-anchored recalibration
   layer (METHODOLOGY 9.9): mines the daily commentary for disclosed
   secondhand vessel sales (name, age, price) that become candidate prints
   for inputs/market_data/transactions/<class>.yaml.

   The scan is INCREMENTAL by default. A cursor at
   inputs/market_data/transactions/_scan_state.json records the newest
   report_date already scanned; subsequent runs only read PDFs dated after
   it. `--full` ignores the cursor (first run, or after changing the
   keyword patterns).

   Candidates are sentences, not parsed prints: a human classifies each hit
   (class, age, clean price, en-bloc splits, quality flag) before it enters
   a transactions YAML. The output at outputs/sp_print_candidates.md is a
   review queue, not data — Pareto's prose mixes sales, rumours, demolitions,
   and rate-table noise; auto-parsing would silently mis-file prints.

2. NAME-MENTION SCAN (`--names`) — per-ticker free-text sweep for the
   onboarding workflow + quarterly refresh (added 2026-06-10 after the GNK
   onboarding showed the dailies carry name-specific gold the structured
   columns miss: Pareto's own dated NAV statements, stance changes, deal
   commentary, name-attributed S&P references). Alias-aware (Pareto uses
   Oslo tickers / company names: OET=ECO, HAFNI=HAFN, TORM=TRMD,
   Tsakos=TEN). Does NOT use or advance the print-scan cursor — a name
   sweep always covers the full archive window requested.

3. LINKED-REPORT HARVEST (`--links`, plus `crude_tanker_fv.fetch_links`) —
   the dailies carry PDF link annotations (pypdf's extract_text() never
   sees them: they live in /Annots) pointing at Pareto's detailed research
   (company quarterly reviews/previews, newsflashes, sector notes) hosted
   publicly on FactSet/BlueMatrix tracked-download URLs — no auth, tokens
   long-lived (a 2024-08 token still served in 2026-06). Some arrive
   Proofpoint-wrapped (urldefense.com /v3/) and are unwrapped offline.
   `--links` extracts annotations into the inventory at
   outputs/pareto_daily_links.json; `python -m crude_tanker_fv.fetch_links`
   downloads inventory entries whose BlueMatrix report ID is not already
   in the archive, into inputs/research_pareto_other/linked/ (then rebuild
   the manifest with `pareto_archive --build-manifest`). The download step
   is a SEPARATE entry point on purpose (2026-06-12): every sp_scan mode
   is local-only, so the permission allowlist can pass `sp_scan *` while
   the one network-touching step still prompts — a flag on this module
   would leak through prefix-matched permission rules when reordered.
   The 2026-06-10 retro-harvest pulled 220 reports (217 classified
   company_report) from 240 link-bearing dailies.

CLI:
    python -m crude_tanker_fv.sp_scan              # incremental print scan
    python -m crude_tanker_fv.sp_scan --full       # ignore cursor, scan all
    python -m crude_tanker_fv.sp_scan --since 2026-01-01
    python -m crude_tanker_fv.sp_scan --names DHT,FRO          # name sweep
    python -m crude_tanker_fv.sp_scan --names all --since 2025-01-01
    python -m crude_tanker_fv.sp_scan --links      # refresh link inventory
    python -m crude_tanker_fv.fetch_links          # download new reports
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "inputs" / "research_pareto" / "_manifest.json"
STATE_PATH = ROOT / "inputs" / "market_data" / "transactions" / "_scan_state.json"
OUTPUT_PATH = ROOT / "outputs" / "sp_print_candidates.md"

# Class keywords. Keys are the transaction-file class names (or the closest
# grouping for classes we don't yet anchor — kept in the scan so a future
# sample can accumulate before a YAML exists). MR/MGC are case-sensitive to
# avoid "Mr." / prose collisions; everything else case-insensitive.
CLASS_KEYWORDS: dict[str, re.Pattern] = {
    "VLCC": re.compile(r"\bVLCC[s]?\b", re.IGNORECASE),
    "Suezmax": re.compile(r"\bsuezmax(?:es)?\b", re.IGNORECASE),
    "Aframax": re.compile(r"\baframax(?:es)?\b", re.IGNORECASE),
    "LR2": re.compile(r"\bLR2[s]?\b", re.IGNORECASE),
    "LR1": re.compile(r"\bLR1[s]?\b", re.IGNORECASE),
    "MR": re.compile(r"\bMR[s]?\b"),
    "Cape": re.compile(r"\bcapesize[s]?\b|\bnewcastlemax(?:es)?\b|\bnmax(?:es)?\b", re.IGNORECASE),
    "Pana": re.compile(r"\bkamsarmax(?:es)?\b|\bpanamax(?:es)?\b|\bpost.?panamax(?:es)?\b", re.IGNORECASE),
    "Supra-Ultra": re.compile(r"\bultramax(?:es)?\b|\bsupramax(?:es)?\b", re.IGNORECASE),
    "Handy": re.compile(r"\bhandymax(?:es)?\b|\bhandysize[s]?\b", re.IGNORECASE),
    "LNGC": re.compile(r"\bLNGC[s]?\b|\bLNG carrier[s]?\b", re.IGNORECASE),
    "VLGC": re.compile(r"\bVLGC[s]?\b", re.IGNORECASE),
    "MGC": re.compile(r"\bMGC[s]?\b"),
}
SALE_PATTERN = re.compile(
    r"\b(sold|sale|bought|acquired|S\&P|secondhand|second-hand|fetched|bagged"
    r"|disposal|disposed|delivered to new owners)\b",
    re.IGNORECASE,
)
PRICE_PATTERN = re.compile(r"\$\s*\d{1,3}(?:\.\d+)?\s*[mM]\b|USD\s*\d{1,3}(?:\.\d+)?\s*m\b")
# Demolition prints are not S&P prints (the old-age leg is disposal-validated
# separately) but worth surfacing in their own bucket for the scrap anchor.
DEMOLITION_PATTERN = re.compile(r"\b(demolition|scrap(?:ped|ping)?|recycl)", re.IGNORECASE)

MIN_SENT, MAX_SENT = 50, 700

# Name-mention scan: per-ticker alias patterns. Pareto's dailies mix US
# tickers, Oslo tickers, and company names — each entry lists every form
# Pareto actually uses. Word-boundary + case-sensitive for short tickers
# (TEN, NAT) to avoid prose collisions; company names case-insensitive.
NAME_ALIASES: dict[str, list[re.Pattern]] = {
    "DHT": [re.compile(r"\bDHT\b")],
    "ECO": [re.compile(r"\bOET\b"), re.compile(r"\bOkeanis\b", re.IGNORECASE)],
    "FRO": [re.compile(r"\bFRO\b"), re.compile(r"\bFrontline\b", re.IGNORECASE)],
    "INSW": [re.compile(r"\bINSW\b"), re.compile(r"\bInternational Seaways\b", re.IGNORECASE),
             re.compile(r"\bSeaways\b")],
    "TNK": [re.compile(r"\bTNK\b"), re.compile(r"\bTeekay Tankers\b", re.IGNORECASE)],
    "NAT": [re.compile(r"\bNAT\b"), re.compile(r"\bNordic American\b", re.IGNORECASE)],
    "FLNG": [re.compile(r"\bFLNG\b"), re.compile(r"\bFlex LNG\b", re.IGNORECASE)],
    "CCEC": [re.compile(r"\bCCEC\b"), re.compile(r"\bCapital Clean\b", re.IGNORECASE),
             re.compile(r"\bCapital Product\b", re.IGNORECASE)],
    "STNG": [re.compile(r"\bSTNG\b"), re.compile(r"\bScorpio Tankers\b", re.IGNORECASE),
             re.compile(r"\bScorpio\b")],
    "HAFN": [re.compile(r"\bHAFNI?\b"), re.compile(r"\bHafnia\b", re.IGNORECASE)],
    "TRMD": [re.compile(r"\bTORM\b", re.IGNORECASE), re.compile(r"\bTRMD\b")],
    "ASC": [re.compile(r"\bASC\b"), re.compile(r"\bArdmore\b", re.IGNORECASE)],
    "TEN": [re.compile(r"\bTEN\b"), re.compile(r"\bTsakos\b", re.IGNORECASE)],
    "SBLK": [re.compile(r"\bSBLK\b"), re.compile(r"\bStar Bulk\b", re.IGNORECASE)],
    "GNK": [re.compile(r"\bGNK\b"), re.compile(r"\bGenco\b", re.IGNORECASE)],
    # "Costamare Bulk" prefix only — bare "Costamare" is CMRE (containership
    # parent), a different listing Pareto DOES discuss.
    "CMDB": [re.compile(r"\bCMDB\b"), re.compile(r"\bCostamare Bulk", re.IGNORECASE),
             re.compile(r"\bCBI\b")],
    # "Capital Tankers" only — bare "Capital" collides with Capital Clean
    # Energy (CCEC) and Capital Product Partners, same Marinakis group.
    "CAPT": [re.compile(r"\bCAPT\b"), re.compile(r"\bCapital Tankers\b", re.IGNORECASE)],
}
# A name mention is interesting when it carries valuation / stance / action
# context — bare ticker drops in rate tables and peer lists are noise.
NAME_CONTEXT = re.compile(
    r"\b(NAV|GAV|TP|target|P/NAV|BUY|HOLD|SELL|TRIM|upgrade|downgrade"
    r"|sold|sale|acquire[ds]?|bought|order(?:ed|s)?|newbuild|dividend|DPS"
    r"|buyback|tender|offer|merger|spin|charter|backlog|guidance|estimate"
    r"|EPS|EBITDA|P/E|discount|premium|net cash|net debt)\b",
    re.IGNORECASE,
)
# The daily share-price table names every ticker alongside P/NAV + P/E columns
# — pure noise for a free-text sweep. These fingerprints appear only in the
# tabular blocks, never in prose.
NAME_TABLE_NOISE = re.compile(
    r"Share prices 6 days|P/E 1Y FWD|imports mtons|Market indicators|USD/day\$",
)


def extract_sp_candidates(text: str) -> list[tuple[str, str, bool]]:
    """Pull (class, sentence, is_demolition) candidates from one report's text.

    A candidate needs a class keyword + a sale phrase + a $-amount in the same
    sentence. The rate-table header (which names every class with $-figures
    but no sale phrase) is excluded by the SALE_PATTERN requirement.
    """
    out: list[tuple[str, str, bool]] = []
    for sent in re.split(r"(?<=[.!?\n])\s+", text):
        if not SALE_PATTERN.search(sent) or not PRICE_PATTERN.search(sent):
            continue
        s = re.sub(r"\s+", " ", sent).strip()
        if not (MIN_SENT < len(s) < MAX_SENT):
            continue
        demo = bool(DEMOLITION_PATTERN.search(sent))
        for cls, kw in CLASS_KEYWORDS.items():
            if kw.search(sent):
                out.append((cls, s, demo))
    return out


def load_scan_state(path: Path = STATE_PATH) -> str | None:
    """Return the cursor date (YYYY-MM-DD) or None if no scan has run."""
    if not path.exists():
        return None
    return json.loads(path.read_text()).get("last_scanned_report_date")


def save_scan_state(report_date: str, path: Path = STATE_PATH) -> None:
    path.write_text(json.dumps({
        "last_scanned_report_date": report_date,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2) + "\n")


def select_files(manifest: dict, since: str | None) -> list[dict]:
    """shipping_daily manifest entries strictly after the cursor, oldest first."""
    files = [f for f in manifest["files"]
             if f["type"] == "shipping_daily" and f.get("report_date")]
    if since:
        files = [f for f in files if f["report_date"] > since]
    return sorted(files, key=lambda f: f["report_date"])


def run_scan(since: str | None, manifest_path: Path = MANIFEST_PATH,
             output_path: Path = OUTPUT_PATH) -> tuple[int, int, str | None]:
    """Scan PDFs after `since`; write the review queue. Returns
    (n_files_scanned, n_candidates, newest_report_date)."""
    from pypdf import PdfReader   # deferred: keeps module import light for tests

    manifest = json.loads(manifest_path.read_text())
    files = select_files(manifest, since)
    if not files:
        return 0, 0, None

    hits: dict[str, list[tuple[str, str, bool]]] = {cls: [] for cls in CLASS_KEYWORDS}
    newest = since
    for f in files:
        path = ROOT / f["path"]
        if not path.exists():
            continue
        try:
            text = "\n".join(pg.extract_text() for pg in PdfReader(str(path)).pages)
        except Exception:
            continue   # corrupt/unparseable PDF: skip, do not advance past silently
        for cls, sent, demo in extract_sp_candidates(text):
            hits[cls].append((f["report_date"], sent, demo))
        if newest is None or f["report_date"] > newest:
            newest = f["report_date"]

    n = sum(len(v) for v in hits.values())
    lines = [
        "# S&P print candidates — Pareto Shipping Daily scan",
        "",
        f"Scanned {len(files)} reports "
        f"({files[0]['report_date']} → {files[-1]['report_date']}); "
        f"{n} candidate sentences. Review each hit and promote real prints to",
        "`inputs/market_data/transactions/<class>.yaml` (en-bloc packages: one",
        "row per vessel; rumours: note as unconfirmed; demolitions go to the",
        "scrap anchor, NOT the mid-age fit).",
        "",
    ]
    for cls, items in hits.items():
        if not items:
            continue
        lines.append(f"## {cls} ({len(items)})")
        lines.append("")
        for date, sent, demo in items:
            tag = " **[DEMOLITION]**" if demo else ""
            lines.append(f"- `{date}`{tag} {sent}")
        lines.append("")
    output_path.write_text("\n".join(lines))
    return len(files), n, newest


def extract_name_mentions(text: str, tickers: list[str]) -> list[tuple[str, str]]:
    """Pull (ticker, sentence) hits with valuation/stance/action context."""
    out: list[tuple[str, str]] = []
    for sent in re.split(r"(?<=[.!?\n])\s+", text):
        if not NAME_CONTEXT.search(sent) or NAME_TABLE_NOISE.search(sent):
            continue
        s = re.sub(r"\s+", " ", sent).strip()
        if not (MIN_SENT < len(s) < MAX_SENT):
            continue
        for ticker in tickers:
            if any(p.search(sent) for p in NAME_ALIASES[ticker]):
                out.append((ticker, s))
    return out


def run_name_scan(tickers: list[str], since: str | None,
                  manifest_path: Path = MANIFEST_PATH,
                  outputs_dir: Path = ROOT / "outputs") -> dict[str, int]:
    """Sweep the archive for per-ticker free-text mentions; one review file
    per ticker at outputs/pareto_mentions_<ticker>.md. Independent of the
    print-scan cursor."""
    from pypdf import PdfReader

    manifest = json.loads(manifest_path.read_text())
    files = select_files(manifest, since)
    hits: dict[str, list[tuple[str, str]]] = {t: [] for t in tickers}
    for f in files:
        path = ROOT / f["path"]
        if not path.exists():
            continue
        try:
            text = "\n".join(pg.extract_text() for pg in PdfReader(str(path)).pages)
        except Exception:
            continue
        for ticker, sent in extract_name_mentions(text, tickers):
            hits[ticker].append((f["report_date"], sent))

    counts: dict[str, int] = {}
    for ticker, items in hits.items():
        counts[ticker] = len(items)
        lines = [
            f"# Pareto Shipping Daily free-text mentions — {ticker}",
            "",
            f"{len(items)} context-bearing sentences across {len(files)} reports "
            f"({files[0]['report_date']} → {files[-1]['report_date']})." if files else "No reports in window.",
            "Review for: dated Pareto NAV/TP statements, stance changes,",
            "name-attributed S&P prints, corporate events. Distill into",
            f"decisions/{ticker.lower()}_log.md — do not treat this file as data.",
            "",
        ]
        for date, sent in items:
            lines.append(f"- `{date}` {sent}")
        (outputs_dir / f"pareto_mentions_{ticker.lower()}.md").write_text("\n".join(lines) + "\n")
    return counts


LINKS_INVENTORY = ROOT / "outputs" / "pareto_daily_links.json"
LINKED_DIR = ROOT / "inputs" / "research_pareto_other" / "linked"


def unwrap_tracked_url(uri: str) -> str | None:
    """Normalize a daily's link annotation to a fetchable report URL.

    Direct FactSet/BlueMatrix tracked links pass through; Proofpoint v3
    wrappers (urldefense.com) are decoded offline (*HH escapes -> %HH, and
    the single-slash scheme artifact fixed). Returns None for everything
    that is not a tracked report link (mailto, news sites, share pages).
    """
    if "urldefense.com" in uri:
        m = re.search(r"/v3/__(.+?)__;", uri)
        if not m:
            return None
        uri = re.sub(r"\*([0-9A-Fa-f]{2})", r"%\1", m.group(1))
        uri = uri.replace("https:/p", "https://p")
    return uri if "factset" in uri or "bluematrix" in uri else None


def extract_link_annotations(reader) -> list[str]:
    """URI link annotations from an open PdfReader (text layer never has these)."""
    uris: list[str] = []
    for page in reader.pages:
        annots = page.get("/Annots")
        if not annots:
            continue
        for a in annots:
            try:
                action = a.get_object().get("/A")
                if action and action.get("/URI"):
                    uris.append(str(action["/URI"]))
            except Exception:
                continue
    return uris


def run_link_inventory(since: str | None, manifest_path: Path = MANIFEST_PATH) -> int:
    """Extract link annotations from dailies into the inventory; returns new-link count."""
    from pypdf import PdfReader

    inventory = json.loads(LINKS_INVENTORY.read_text()) if LINKS_INVENTORY.exists() else []
    known = {e["uri"] for e in inventory}
    manifest = json.loads(manifest_path.read_text())
    new = 0
    for f in select_files(manifest, since):
        path = ROOT / f["path"]
        if not path.exists():
            continue
        try:
            uris = extract_link_annotations(PdfReader(str(path)))
        except Exception:
            continue
        for u in uris:
            if u in known or u.startswith("mailto:"):
                continue
            known.add(u)
            kind = ("factset_report" if "factset" in u
                    else "urldefense_wrapped" if "urldefense" in u
                    else "pareto_share" if "paretosec" in u
                    else "external")
            inventory.append({"report_date": f["report_date"], "kind": kind, "uri": u})
            new += 1
    inventory.sort(key=lambda e: e["report_date"])
    LINKS_INVENTORY.write_text(json.dumps(inventory, indent=1) + "\n")
    return new


def existing_report_ids() -> set[str]:
    """BlueMatrix report IDs already present anywhere in the archive."""
    ids: set[str] = set()
    for root in (ROOT / "inputs" / "research_pareto", ROOT / "inputs" / "research_pareto_other"):
        for p in root.rglob("*.pdf"):
            m = re.search(r"(\d{6})\.pdf$", p.name)
            if m:
                ids.add(m.group(1))
    return ids


def run_fetch_links() -> tuple[int, int, int]:
    """Download inventory entries whose report ID isn't in the archive yet.

    Returns (downloaded, skipped_dupe, failed). Polite 0.4s spacing; tokens
    are long-lived but a future-expired token just lands in `failed`.

    The resolved BlueMatrix report_id is written back onto each inventory
    entry after its first fetch, so re-runs skip already-resolved links
    WITHOUT network round-trips — only never-fetched links cost a request.
    """
    import time
    import urllib.request

    inventory = json.loads(LINKS_INVENTORY.read_text()) if LINKS_INVENTORY.exists() else []
    LINKED_DIR.mkdir(parents=True, exist_ok=True)
    existing = existing_report_ids()

    # One representative inventory entry per unique fetch URL.
    by_url: dict[str, dict] = {}
    for e in inventory:
        u = unwrap_tracked_url(e["uri"])
        if u and u not in by_url:
            by_url[u] = e

    got = skipped = failed = 0
    for url, entry in sorted(by_url.items(), key=lambda kv: kv[1]["report_date"]):
        rid = entry.get("report_id")
        if rid and rid in existing:
            skipped += 1
            continue   # resolved on a prior run; no network needed
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                cd = resp.headers.get("Content-Disposition", "")
                m = re.search(r'filename="?(\d+)\.pdf', cd)
                rid = m.group(1) if m else None
                if rid:
                    entry["report_id"] = rid
                if rid is None or rid in existing:
                    skipped += 1
                    continue
                data = resp.read()
                if not data.startswith(b"%PDF"):
                    failed += 1
                    continue
                existing.add(rid)
                (LINKED_DIR / f"{entry['report_date']}_linked-{rid}.pdf").write_bytes(data)
                got += 1
        except Exception:
            failed += 1
        time.sleep(0.4)

    LINKS_INVENTORY.write_text(json.dumps(inventory, indent=1) + "\n")
    return got, skipped, failed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Pareto archive scans (S&P prints / name mentions)")
    ap.add_argument("--full", action="store_true", help="ignore the cursor, scan everything")
    ap.add_argument("--since", help="scan reports strictly after this date (YYYY-MM-DD)")
    ap.add_argument("--names", help="comma-separated tickers (or 'all') for a free-text "
                                    "name-mention sweep; skips the print scan + cursor")
    ap.add_argument("--links", action="store_true",
                    help="extract link annotations into outputs/pareto_daily_links.json "
                         "(downloads moved to: python -m crude_tanker_fv.fetch_links)")
    args = ap.parse_args(argv)

    if args.links:
        n = run_link_inventory(args.since)
        print(f"{n} new links -> {LINKS_INVENTORY}")
        return 0

    if args.names:
        tickers = list(NAME_ALIASES) if args.names.lower() == "all" else \
            [t.strip().upper() for t in args.names.split(",")]
        unknown = [t for t in tickers if t not in NAME_ALIASES]
        if unknown:
            print(f"unknown ticker(s) {unknown}; known: {', '.join(NAME_ALIASES)}")
            return 1
        counts = run_name_scan(tickers, args.since)
        for t, n in counts.items():
            print(f"{t:6s} {n:4d} mentions -> outputs/pareto_mentions_{t.lower()}.md")
        return 0

    since = None if args.full else (args.since or load_scan_state())
    n_files, n_hits, newest = run_scan(since)
    if n_files == 0:
        print(f"nothing to scan (cursor at {since})")
        return 0
    save_scan_state(newest)
    print(f"scanned {n_files} reports -> {n_hits} candidates -> {OUTPUT_PATH}")
    print(f"cursor advanced to {newest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
