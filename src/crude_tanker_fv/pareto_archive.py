"""Inventory + classify the Pareto research PDF archive.

Walks `inputs/research_pareto/` and produces a manifest at
`inputs/research_pareto/_manifest.json` that tags each PDF as one of:

  - shipping_daily   — daily research with the right-column rate tables
  - container_weekly — Pareto's weekly container-segment report
  - company_report   — initiating coverage / update notes / sector deep-dives
  - other            — anything else (we'll see what's left after the others)

Classification is two-pass: filename pattern first (fast), then a first-page
content check for the bare-numeric files (where filenames carry no signal).

This module is read-only by design — it only writes the manifest JSON.
Refoldering (Phase B) is a separate step that consumes the manifest.

CLI:
    python -m crude_tanker_fv.pareto_archive --build-manifest
    python -m crude_tanker_fv.pareto_archive --summary
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "inputs" / "research_pareto"
ARCHIVE_OTHER = ROOT / "inputs" / "research_pareto_other"
ARCHIVE_ROOTS = (ARCHIVE, ARCHIVE_OTHER)
# Manifest lives at the primary archive root (where the launchd ingest writes);
# its scope covers both ARCHIVE and ARCHIVE_OTHER subtrees.
MANIFEST_PATH = ARCHIVE / "_manifest.json"

# Filename patterns. Order matters — match the most specific first.
_FN_CONTAINER_WEEKLY = re.compile(
    r"Container[%2B\s+]*Weekly", re.IGNORECASE,
)
_FN_SHIPPING_DAILY = re.compile(r"ShippingDaily", re.IGNORECASE)
_FN_COMPANY_REPORT = re.compile(
    r"CompanyReport|InitiatingCoverage|QuarterlyReview|QuarterlyPreview",
    re.IGNORECASE,
)
_FN_BARE_NUMERIC = re.compile(r"^\d{4}-\d{2}-\d{2}_\d+\.pdf$")
_FN_DATE_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})_")

# Content fingerprints.
_CONTENT_SHIPPING_DAILY = re.compile(
    r"Shipping Daily|Capesize USD/day|VLCC \(TD3_C\)|Drybulk \(VLSFO\)",
)
_CONTENT_CONTAINER_WEEKLY = re.compile(r"Container Weekly", re.IGNORECASE)
# Pareto's single-company / sector research uses many header formats:
# INITIATING COVERAGE | COMPANY REPORT | QUARTERLY PREVIEW | QUARTERLY REVIEW |
# UPDATE | NEWSFLASH | KEY TAKEAWAYS (for conference reports / sector pieces).
# All structurally the same: ~5-15pp PDFs with no right-column rate table, so
# downstream extraction (Phase D) doesn't target them.
_CONTENT_COMPANY_REPORT = re.compile(
    r"INITIATING COVERAGE|COMPANY REPORT|COMPANY UPDATE|UPDATE NOTE|"
    r"QUARTERLY PREVIEW|QUARTERLY REVIEW|QUARTERLY UPDATE|"
    r"NEWSFLASH|KEY TAKEAWAYS|RESEARCH REPORT|"
    r"SECTOR REPORT|SECTOR UPDATE|SECTOR REVIEW|"
    # "UPDATE | <DATE>" is Pareto's header for short-form company / sector
    # updates (e.g. "Rig UPDATE | 16 OCT 2024", "Frontline UPDATE | 12 JAN 2026").
    # Anchor with the pipe to avoid matching the word "UPDATE" in body text.
    r"UPDATE \| \d",
)


@dataclass
class ClassifiedFile:
    """One row in the manifest."""
    path: str                       # relative to repo root
    filename: str
    type: str                       # shipping_daily | container_weekly | company_report | other
    report_date: Optional[str]      # YYYY-MM-DD, from filename or content
    downloaded_at: str              # ISO timestamp, filesystem mtime (proxy for download time)
    parsed_at: Optional[str]        # filled by Phase D extraction; null at inventory time
    page_count: Optional[int]
    size_bytes: int
    classification_signal: str      # short string explaining the classification (e.g. "filename:Container Weekly")


def _first_page_text(path: Path) -> str:
    """Extract first-page text only. Returns '' on parse error."""
    try:
        reader = PdfReader(path)
        if not reader.pages:
            return ""
        return reader.pages[0].extract_text() or ""
    except Exception:
        return ""


def _page_count(path: Path) -> Optional[int]:
    try:
        return len(PdfReader(path).pages)
    except Exception:
        return None


def _classify_by_filename(filename: str) -> tuple[Optional[str], Optional[str]]:
    """First-pass: look at filename only. Returns (type, signal) or (None, None)."""
    if _FN_CONTAINER_WEEKLY.search(filename):
        return "container_weekly", "filename:Container Weekly"
    if _FN_SHIPPING_DAILY.search(filename):
        return "shipping_daily", "filename:ShippingDaily"
    m = _FN_COMPANY_REPORT.search(filename)
    if m:
        return "company_report", f"filename:{m.group(0)}"
    return None, None


def _classify_by_content(text: str) -> tuple[str, str]:
    """Second-pass: look at first-page text. Always returns a (type, signal)."""
    # Shipping Daily fingerprint is strong — the right-column rate table is unique.
    m = _CONTENT_SHIPPING_DAILY.search(text)
    if m:
        return "shipping_daily", f"content:{m.group(0)[:30]}"
    m = _CONTENT_CONTAINER_WEEKLY.search(text)
    if m:
        return "container_weekly", f"content:Container Weekly"
    m = _CONTENT_COMPANY_REPORT.search(text)
    if m:
        return "company_report", f"content:{m.group(0)[:30]}"
    return "other", "content:no-fingerprint-matched"


def _report_date_from_filename(filename: str) -> Optional[str]:
    m = _FN_DATE_PREFIX.match(filename)
    return m.group(1) if m else None


def classify_pdf(path: Path) -> ClassifiedFile:
    """Inspect one PDF and return a ClassifiedFile manifest entry."""
    stat = path.stat()
    rel = path.relative_to(ROOT)
    filename = path.name

    file_type, signal = _classify_by_filename(filename)
    if file_type is None:
        text = _first_page_text(path)
        file_type, signal = _classify_by_content(text)

    return ClassifiedFile(
        path=str(rel),
        filename=filename,
        type=file_type,
        report_date=_report_date_from_filename(filename),
        downloaded_at=dt.datetime.fromtimestamp(
            stat.st_mtime, tz=dt.timezone.utc,
        ).isoformat(),
        parsed_at=None,
        page_count=_page_count(path),
        size_bytes=stat.st_size,
        classification_signal=signal,
    )


def build_manifest(roots: tuple[Path, ...] = ARCHIVE_ROOTS,
                   verbose: bool = True) -> list[ClassifiedFile]:
    """Walk the archive roots, classify every PDF, write _manifest.json.

    `roots` defaults to (ARCHIVE, ARCHIVE_OTHER) so the manifest stays whole
    after Phase B refoldering moves non-dailies into the sibling tree.
    """
    pdfs: list[Path] = []
    for root in roots:
        if root.exists():
            pdfs.extend(root.rglob("*.pdf"))
    pdfs.sort()
    total = len(pdfs)
    results: list[ClassifiedFile] = []
    for i, pdf in enumerate(pdfs):
        if verbose and i % 50 == 0:
            sys.stderr.write(f"  [{i}/{total}] {pdf.name[:60]}\n")
        results.append(classify_pdf(pdf))

    manifest = {
        "generated_at": dt.datetime.now(tz=dt.timezone.utc).isoformat(),
        "archive_roots": [str(r.relative_to(ROOT)) for r in roots if r.exists()],
        "total_files": len(results),
        "files": [asdict(r) for r in results],
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n")
    if verbose:
        sys.stderr.write(f"  wrote manifest: {MANIFEST_PATH.relative_to(ROOT)}\n")
    return results


def load_manifest(archive: Path = ARCHIVE) -> Optional[dict]:
    """Read the existing manifest if it exists."""
    path = archive / "_manifest.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def print_summary(results: list[ClassifiedFile]) -> None:
    """Counts by type + date range + sample by type."""
    by_type: dict[str, list[ClassifiedFile]] = {}
    for r in results:
        by_type.setdefault(r.type, []).append(r)

    print(f"\n{'=' * 60}")
    print(f"PARETO ARCHIVE MANIFEST — {len(results)} files")
    print(f"{'=' * 60}")
    for t in ["shipping_daily", "container_weekly", "company_report", "other"]:
        items = by_type.get(t, [])
        print(f"\n  {t:<20} {len(items):>4}")
        if items:
            dates = [r.report_date for r in items if r.report_date]
            if dates:
                print(f"    date range: {min(dates)} → {max(dates)}")
            # 3 samples per type
            for r in items[:3]:
                print(f"    e.g. {r.path}")
                print(f"         signal: {r.classification_signal}")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="crude_tanker_fv.pareto_archive",
        description="Inventory + classify the Pareto research PDF archive.",
    )
    parser.add_argument("--build-manifest", action="store_true",
                        help="walk archive, classify every PDF, write _manifest.json")
    parser.add_argument("--summary", action="store_true",
                        help="print summary from existing _manifest.json")
    args = parser.parse_args()
    if args.build_manifest:
        results = build_manifest()
        print_summary(results)
        return 0
    if args.summary:
        m = load_manifest()
        if m is None:
            sys.stderr.write("No manifest yet. Run --build-manifest first.\n")
            return 1
        results = [ClassifiedFile(**r) for r in m["files"]]
        print_summary(results)
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
