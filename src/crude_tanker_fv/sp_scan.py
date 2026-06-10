"""Scan the Pareto Shipping Daily archive for S&P (sale & purchase) prints.

Feeds the transaction-anchored recalibration layer (METHODOLOGY 9.9): mines
the daily commentary for disclosed secondhand vessel sales (name, age, price)
that become candidate prints for inputs/market_data/transactions/<class>.yaml.

The scan is INCREMENTAL by default. A cursor at
inputs/market_data/transactions/_scan_state.json records the newest
report_date already scanned; subsequent runs only read PDFs dated after it,
so the weekly Pareto ingest doesn't trigger a 280-PDF re-scan. `--full`
ignores the cursor (first run, or after changing the keyword patterns —
pattern changes invalidate old scans, so bump the cursor back deliberately).

Candidates are sentences, not parsed prints: a human classifies each hit
(class, age, clean price, en-bloc splits, quality flag) before it enters a
transactions YAML. The output at outputs/sp_print_candidates.md is a review
queue, not data. This is deliberate — Pareto's prose mixes sales, rumours,
demolitions, and rate-table noise; auto-parsing would silently mis-file
prints that the YAML schema records as load-bearing fit inputs.

CLI:
    python -m crude_tanker_fv.sp_scan              # incremental from cursor
    python -m crude_tanker_fv.sp_scan --full       # ignore cursor, scan all
    python -m crude_tanker_fv.sp_scan --since 2026-01-01
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Incremental Pareto S&P print scan")
    ap.add_argument("--full", action="store_true", help="ignore the cursor, scan everything")
    ap.add_argument("--since", help="scan reports strictly after this date (YYYY-MM-DD)")
    args = ap.parse_args(argv)

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
