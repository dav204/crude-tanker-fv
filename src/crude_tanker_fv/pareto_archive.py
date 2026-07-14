"""Inventory + classify + extract the Pareto research PDF archive.

Three jobs:
  1. Classify every PDF in inputs/research_pareto/ (and the sibling _other/
     tree) — `--build-manifest`. Tags each as shipping_daily /
     container_weekly / company_report / other in _manifest.json.
  2. Extract structured data from every shipping_daily — `--extract`. Writes
     inputs/market_data/pareto_daily.csv (wide, ~45 fields per report) and
     inputs/market_data/pareto_share_prices.csv (long, 1 row per ticker per
     report). Handles the 4 schema epochs documented in Phase C.
  3. Summarize — `--summary` prints counts from the existing manifest.

CLI:
    python -m crude_tanker_fv.pareto_archive --build-manifest
    python -m crude_tanker_fv.pareto_archive --extract
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
        return "container_weekly", "content:Container Weekly"
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


# =====================================================================
# PHASE D — extract structured data from shipping_daily PDFs
# =====================================================================
#
# The right column of every Shipping Daily has stable structure across the
# 24-month archive, but with 4 documented format shifts (Phase C):
#   Epoch 1 (Aug-2024 – Apr-2025): Tanker "VLCC USD/day" (no route label),
#       comma thousands. Bulk: Cape / Pana / Supramax.
#   Epoch 2 (Apr-2025 – Sep-2025): Tanker route labels added "VLCC (TD3_C)";
#       space thousands separator. Bulk still Supramax.
#   Epoch 3 (Sep-2025 – May-2026): Bulk class swap Supramax → Ultramax.
#   Epoch 4 (May-2026 – ...): MR splits to "MR (West)" / "MR (East)".
#
# Strategy: tolerant regex with the rate-percent boundary trick
# `[\d,\s ]*\d\s*-?\d+\.\d+%` (greedy match the rate ending on a digit,
# then the change percentage). One internal CSV column per stable field;
# null when a field wasn't in the schema yet (e.g. ultramax pre-Sep 2025).

OUTPUTS_DIR = ROOT / "inputs" / "market_data"
DAILY_CSV = OUTPUTS_DIR / "pareto_daily.csv"
SHARE_PRICES_CSV = OUTPUTS_DIR / "pareto_share_prices.csv"

# Regex toolkit. The "rate-percent" pair is the load-bearing trick: greedy
# match the rate, ending on a digit, then a small-form percentage.
_RATE_PCT = r"\$([\d,\s ]+?)\s*(-?\d{1,2}\.\d+)%"


def _to_int(s: Optional[str]) -> Optional[int]:
    if s is None:
        return None
    cleaned = re.sub(r"[\s ,]", "", s)
    return int(cleaned) if cleaned else None


def _to_float(s: Optional[str]) -> Optional[float]:
    if s is None:
        return None
    cleaned = re.sub(r"[\s ,]", "", s)
    return float(cleaned) if cleaned else None


def _parse_tanker_row(text: str, cls: str, route: Optional[str]) -> tuple[Optional[int], Optional[int]]:
    """Return (scrubber, non_scrubber) USD/day for the given tanker class.
    Skips the premium column (derivable as scrubber − non_scrubber)."""
    if route:
        anchor = rf"{re.escape(cls)}\s*\(\s*{re.escape(route)}\s*\)"
    else:
        # Class WITHOUT a route label (e.g., early-format VLCC, MR pre-May-2026)
        anchor = rf"{re.escape(cls)}(?!\s*\()"
    pat = re.compile(
        rf"{anchor}"
        r"[^$\n]*"
        rf"{_RATE_PCT}"
        rf"\s*{_RATE_PCT}",
    )
    m = pat.search(text)
    if m:
        return _to_int(m.group(1)), _to_int(m.group(3))
    return None, None


def _parse_simple_rate(text: str, anchor: str) -> Optional[int]:
    """Anchor followed by $rate<change>%. Rate/change boundary is ambiguous
    after PDF text-extraction strips column-boundary spaces (e.g.
    '$44 67216.3%' could be rate=44672+chg=16.3% or rate=446721+chg=6.3%).
    Capture the full digit block + decimal portion, try ALL plausible
    splits, pick the one with a typical daily-change magnitude."""
    # Capture: $ then any digits/commas/spaces/optional minus, then .digits %
    pat = re.compile(
        rf"{anchor}[^$\n]*\$([\d,\s ]+?(?:-?[\d,\s ]+?)?)\.(\d+)%"
    )
    m = pat.search(text)
    if not m:
        return None
    pre_decimal = m.group(1)
    post_decimal = m.group(2)
    # Handle explicit negative (clean case): rate is before the "-", change is "-<...>"
    minus_idx = pre_decimal.rfind("-")
    if minus_idx >= 0:
        rate_str = pre_decimal[:minus_idx]
        change_pre = pre_decimal[minus_idx+1:]
        rate_digits = re.sub(r"[\s ,]", "", rate_str)
        change_digits = re.sub(r"[\s ,]", "", change_pre)
        if rate_digits and change_digits:
            try:
                return int(rate_digits)
            except ValueError:
                return None
    # No minus: digits are ambiguously split between rate and change
    all_digits = re.sub(r"[\s ,]", "", pre_decimal)
    candidates = []
    # Try every split where rate >= 1 digit and change has 1-2 digits before decimal
    for change_pre_len in (1, 2):
        if len(all_digits) <= change_pre_len:
            continue
        rate_part = all_digits[:-change_pre_len]
        change_part = all_digits[-change_pre_len:]
        try:
            rate_v = int(rate_part)
            change_v = float(change_part + "." + post_decimal)
        except ValueError:
            continue
        candidates.append((rate_v, change_v))
    # Plausibility: rate in [3000, 150000], |change| <= 30
    plausible = [(r, c) for r, c in candidates if 3000 <= r <= 150000 and abs(c) <= 30]
    if not plausible:
        plausible = [(r, c) for r, c in candidates if 3000 <= r <= 150000]
    if not plausible:
        return None
    # Prefer smaller |change| (typical daily move)
    return min(plausible, key=lambda x: abs(x[1]))[0]


def _parse_simple_price(text: str, anchor: str) -> Optional[float]:
    """For oil prices / gas prices: anchor followed by $price (decimal).
    Capture digits-optional-dot-digits with NO whitespace in the class, so
    the regex auto-terminates at the column boundary (the space between
    adjacent table values) regardless of whether the change-% column starts
    with a minus sign. Prevents the prior bug where 'Saudi propane $690
    1.4%' captured '690 1.4' and produced 6901.4."""
    pat = re.compile(rf"{anchor}[^$\n]*\$\s*(\d+(?:\.\d+)?)")
    m = pat.search(text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def _parse_indicator_small(text: str, anchor: str) -> Optional[float]:
    """Indicators that are SMALL floats with exactly one decimal place —
    imports (mtons), production (mmboe/day), iron ore tonnage. Pareto's PDF
    extraction sometimes concatenates adjacent table values without separator
    (e.g. China iron ore '103.9104.7'), so we require exactly one digit after
    the decimal point to avoid over-capturing into the next column."""
    pat = re.compile(rf"{anchor}[^\d\n]*(\d+\.\d)")
    m = pat.search(text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def _parse_indicator(text: str, anchor: str) -> Optional[float]:
    """For BDI / iron ore / imports: anchor followed by a number (no $)."""
    pat = re.compile(rf"{anchor}[^\d\n]*([\d,\.\s ]+?)(?:[-%]|\s[A-Za-z])")
    m = pat.search(text)
    if m:
        try:
            return _to_float(m.group(1).strip())
        except (ValueError, AttributeError):
            return None
    return None


# Tanker classes and their route labels by epoch. Pattern: try with route label,
# fall back to no label (handles epoch 1 where labels didn't exist).
_TANKER_CLASSES = [
    ("vlcc_td3c",      "VLCC",    "TD3_C"),
    ("vlcc_td22",      "VLCC",    "TD22"),
    ("suezmax_td20",   "Suezmax", "TD20"),
    ("aframax",        "Aframax", None),
    ("lr2",            "LR2",     None),
    ("lr1",            "LR1",     None),
    ("mr",             "MR",      None),
    ("mr_west",        "MR",      "West"),
    ("mr_east",        "MR",      "East"),
]


def extract_daily_row(path: Path, report_date: str) -> dict:
    """Pull the right-column data points from one shipping_daily PDF.

    Returns a dict keyed by field name. Missing fields are None — that's
    correct (e.g. Ultramax in epoch 1 genuinely wasn't published)."""
    try:
        text = "\n".join(p.extract_text() for p in PdfReader(path).pages)
    except Exception:
        return {"report_date": report_date, "source_file": str(path.relative_to(ROOT)),
                "parse_error": True}

    row: dict = {
        "report_date": report_date,
        "source_file": str(path.relative_to(ROOT)),
        "parse_error": False,
    }

    # --- Tanker TCEs (scrubber + non-scrubber per route) ---
    for field, cls, route in _TANKER_CLASSES:
        sc, ns = _parse_tanker_row(text, cls, route)
        # Skip MR-with-route fields if the file pre-dates the May-2026 split:
        # the anchor regex won't match anyway, so they'll be None — fine.
        # Skip plain MR if MR (West) hit (avoids double-counting in epoch 4).
        if field == "mr" and row.get("mr_west_scrubber") is not None:
            continue
        row[f"{field}_scrubber"] = sc
        row[f"{field}_non_scrubber"] = ns

    # --- Dry bulk: Cape / Pana / Supra-Ultra (with source-label transparency) ---
    row["bulk_cape_usd_day"] = _parse_simple_rate(text, r"Capesize\s+USD/day")
    row["bulk_pana_usd_day"] = _parse_simple_rate(text, r"Panamax")
    # Supra-Ultra: try Ultramax first (newer); fall back to Supramax (epoch 1-2)
    ultra = _parse_simple_rate(text, r"Ultramax")
    if ultra is not None:
        row["bulk_supra_ultra_usd_day"] = ultra
        row["bulk_supra_ultra_source"] = "Ultramax"
    else:
        supra = _parse_simple_rate(text, r"Supramax")
        row["bulk_supra_ultra_usd_day"] = supra
        row["bulk_supra_ultra_source"] = "Supramax" if supra is not None else None

    # --- Macro / oil (prices in USD; imports in mboe/day) ---
    row["brent_usd_bbl"] = _parse_simple_price(text, r"Brent oil price")
    row["wti_usd_bbl"] = _parse_simple_price(text, r"WTI oil price")
    row["us_crude_imports_mmboe_day"] = _parse_indicator_small(text, r"US crude oil imports.*?day")
    row["china_crude_imports_mmboe_day"] = _parse_indicator_small(text, r"China crude oil imports")
    row["opec_oil_production_mmboe_day"] = _parse_indicator_small(text, r"OPEC oil production")

    # --- Bulk indicators ---
    row["iron_ore_china_usd_ton"] = _parse_simple_price(text, r"Iron ore import price")
    row["bdi"] = _parse_indicator(text, r"Baltic Dry Index\s+Index")
    row["china_iron_ore_imports_mt"] = _parse_indicator_small(text, r"China iron ore imports")
    row["china_coal_imports_mt"] = _parse_indicator_small(text, r"China coal imports")

    # --- LPG ---
    row["vlgc_me_asia_usd_day"] = _parse_simple_rate(text, r"VLGC: Middle East - Asia")
    row["vlgc_usgom_asia_usd_day"] = _parse_simple_rate(text, r"VLGC: USGoM")
    row["mt_belvieu_propane_usd_ton"] = _parse_simple_price(text, r"Mt\.?\s*Belvieu spot propane")
    row["japan_fwd_propane_usd_ton"] = _parse_simple_price(text, r"Japan.{0,5}fwd propane")
    row["japan_naphtha_usd_ton"] = _parse_simple_price(text, r"Japan spot naphtha")
    row["saudi_propane_usd_ton"] = _parse_simple_price(text, r"Saudi Arabia spot propane")
    row["japan_lpg_imports_mt"] = _parse_indicator_small(text, r"Japan LPG imports")
    row["india_lpg_imports_mt"] = _parse_indicator_small(text, r"India LPG imports")
    row["china_lpg_imports_mt"] = _parse_indicator_small(text, r"China LPG imports")

    # --- LNG ---
    row["lng_tfde_usd_day"] = _parse_simple_rate(text, r"LNG Carrier spot rate")
    row["henry_hub_usd_mmbtu"] = _parse_simple_price(text, r"Henry Hub spot natural gas")
    row["japan_lng_usd_mmbtu"] = _parse_simple_price(text, r"Japan spot LNG")
    row["ttf_usd_mmbtu"] = _parse_simple_price(text, r"TTF \(EU nat gas\)")
    row["japan_lng_imports_mt"] = _parse_indicator_small(text, r"Japan LNG imports")
    row["china_lng_imports_mt"] = _parse_indicator_small(text, r"China LNG imports")
    row["korea_lng_imports_mt"] = _parse_indicator_small(text, r"Korea LNG imports")
    row["india_lng_imports_mt"] = _parse_indicator_small(text, r"India LNG imports")

    return row


# --- Share-price table extraction ---
# The left column of page 1 has a per-ticker table. Format:
#   <Company Name> <currency-prefix><price> <-1d%> <-1w%> <ytd%> <pnav> <fwd_pe>
# Companies known to appear across the archive. Map display name → ticker.
_SHARE_TABLE_COMPANIES: list[tuple[str, str]] = [
    ("Ardmore Shipping",          "ASC"),
    ("Bruton Ltd\\.",             "BRUTON"),
    ("Capital Tankers",           "CAPITAL_TNKR"),
    ("d'Amico International",     "DIS"),
    ("DHT Holdings",              "DHT"),
    ("Frontline",                 "FRO"),
    ("Hafnia Ltd\\.",             "HAFN"),
    ("International Seaways",     "INSW"),
    ("Nordic American Tankers",   "NAT"),
    ("Okeanis Eco Tankers",       "ECO"),
    ("Scorpio Tankers",           "STNG"),
    ("Teekay Tankers",            "TNK"),
    ("TORM",                      "TRMD"),
    ("CMB\\.TECH",                "CMBT"),
    ("Genco Shipping",            "GNK"),
    ("Himalaya Shipping",         "HSHP"),
    ("Star Bulk Carriers",        "SBLK"),
    ("BW LPG",                    "BWLP"),
    ("Dorian LPG",                "LPG"),
    ("Navigator Holdings",        "NVGS"),
    ("Awilco LNG",                "AWILCO"),
    ("Capital Clean Energy",      "CCEC"),
    ("Flex LNG",                  "FLNG"),
    ("Golar LNG",                 "GLNG"),
    ("SFL Corp",                  "SFL"),
    ("Odfjell SE",                "ODFB"),
    ("Stolt-Nielsen",             "SNI"),
    ("Klaveness Combination",     "KCC"),
    ("Maersk B",                  "MAERSKB"),
    ("MPC Container Ships",       "MPCC"),
    ("Höegh Autoliners",          "HAUTO"),
    ("Wallenius Wilhelmsen",      "WAWI"),
]


# Per-row regex: company name, optional currency tag (kr / €), price (float),
# 1d% / 1w% / ytd% / pnav / fwd_pe. P/NAV and P/E can be "-" (not published)
# or "na" — handled by a permissive pattern.
_SHARE_ROW = re.compile(
    r"(?P<currency>kr|€|\$)?\s*"
    r"(?P<price>[\d,\.]+)\s*"
    r"(?P<d1>-?\d+\.?\d*%?)\s*"
    r"(?P<w1>-?[\d\.\s]+%)\s*"
    r"(?P<ytd>-?[\d\.\s]+%)\s*"
    r"(?P<pnav>[\d\.]+x|-)\s*"
    r"(?P<fwd_pe>[\d\.]+x|na|-)",
)


def extract_share_prices(path: Path, report_date: str) -> list[dict]:
    """Pull the per-ticker share-price + P/NAV + P/E rows from one PDF.

    Returns a list of dicts, one per ticker found. Tickers missing from a
    given report are simply not in the list (more honest than null rows)."""
    try:
        text = "\n".join(p.extract_text() for p in PdfReader(path).pages)
    except Exception:
        return []

    rows: list[dict] = []
    for display, ticker in _SHARE_TABLE_COMPANIES:
        # Search for company name followed by the row's numeric block. Two
        # rendering quirks, both caught 2026-06-14 while assembling the crude
        # backtest panel:
        #  (1) an optional parenthetical can sit between name and numbers
        #      ("Frontline (US)", "Himalaya Shipping (US)") — Pareto tags the
        #      US line of dual-listed names this way;
        #  (2) the name→row separator is OPTIONAL whitespace, not required:
        #      later issues glue the currency to the name for kr-prefixed rows
        #      ("Okeanis Eco Tankerskr 275-0.7%...") so a required \s+ dropped
        #      Okeanis (ECO) from 2025-04 onward. \s* matches both the spaced
        #      ("DHT Holdings $11.7") and glued ("Tankerskr 275") cases.
        pat = re.compile(rf"{display}(?:\s*\([^)]*\))?\s*{_SHARE_ROW.pattern}")
        m = pat.search(text)
        if not m:
            continue
        try:
            price = _to_float(m.group("price"))
            pnav_raw = m.group("pnav")
            fwd_pe_raw = m.group("fwd_pe")
            rows.append({
                "report_date": report_date,
                "ticker": ticker,
                "display_name": display.replace("\\.", "."),
                "currency": m.group("currency") or "$",
                "price": price,
                "pnav": _to_float(pnav_raw.replace("x", "")) if pnav_raw not in ("-", "na") else None,
                "fwd_pe": _to_float(fwd_pe_raw.replace("x", "")) if fwd_pe_raw not in ("-", "na") else None,
            })
        except (ValueError, AttributeError):
            continue
    return rows


def run_extraction(verbose: bool = True) -> tuple[int, int, int]:
    """Walk the manifest's shipping_daily entries, extract both tables,
    write CSVs, update manifest with parsed_at timestamps.

    Returns (n_files_parsed, n_daily_rows, n_share_price_rows)."""
    import csv

    m = load_manifest()
    if m is None:
        sys.stderr.write("No manifest. Run --build-manifest first.\n")
        return 0, 0, 0

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    daily_rows: list[dict] = []
    share_rows: list[dict] = []
    parsed_paths: set[str] = set()
    parse_failures: list[str] = []

    dailies = [f for f in m["files"] if f["type"] == "shipping_daily"]
    total = len(dailies)
    for i, f in enumerate(dailies):
        if verbose and i % 50 == 0:
            sys.stderr.write(f"  [{i}/{total}] {f['filename'][:60]}\n")
        path = ROOT / f["path"]
        if not path.exists():
            continue
        report_date = f["report_date"] or f["downloaded_at"][:10]
        daily = extract_daily_row(path, report_date)
        daily_rows.append(daily)
        if daily.get("parse_error"):
            parse_failures.append(f["path"])
            continue
        share_rows.extend(extract_share_prices(path, report_date))
        parsed_paths.add(f["path"])

    # Sort by date for cleaner CSV diffs
    daily_rows.sort(key=lambda r: r["report_date"])
    share_rows.sort(key=lambda r: (r["report_date"], r["ticker"]))

    # Write the wide daily table
    if daily_rows:
        # Union of all keys (some rows may lack newer fields)
        all_keys: list[str] = []
        seen: set[str] = set()
        for r in daily_rows:
            for k in r:
                if k not in seen:
                    all_keys.append(k)
                    seen.add(k)
        with DAILY_CSV.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=all_keys)
            w.writeheader()
            for r in daily_rows:
                w.writerow(r)

    # Write the long share-price table
    if share_rows:
        keys = ["report_date", "ticker", "display_name", "currency", "price", "pnav", "fwd_pe"]
        with SHARE_PRICES_CSV.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=keys)
            w.writeheader()
            for r in share_rows:
                w.writerow(r)

    # Update manifest with parsed_at timestamps for files we successfully parsed
    now = dt.datetime.now(tz=dt.timezone.utc).isoformat()
    for f in m["files"]:
        if f["path"] in parsed_paths:
            f["parsed_at"] = now
    MANIFEST_PATH.write_text(json.dumps(m, indent=2) + "\n")

    if verbose:
        sys.stderr.write(f"\n  parsed {len(parsed_paths)}/{total} shipping_daily files\n")
        sys.stderr.write(f"  daily rows:        {len(daily_rows)}  → {DAILY_CSV.relative_to(ROOT)}\n")
        sys.stderr.write(f"  share-price rows:  {len(share_rows)}  → {SHARE_PRICES_CSV.relative_to(ROOT)}\n")
        if parse_failures:
            sys.stderr.write(f"  parse failures: {len(parse_failures)}\n")
            for p in parse_failures[:5]:
                sys.stderr.write(f"    {p}\n")

    return len(parsed_paths), len(daily_rows), len(share_rows)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="crude_tanker_fv.pareto_archive",
        description="Inventory + classify + extract the Pareto research PDF archive.",
    )
    parser.add_argument("--build-manifest", action="store_true",
                        help="walk archive, classify every PDF, write _manifest.json")
    parser.add_argument("--extract", action="store_true",
                        help="extract right-column data from shipping_daily files to "
                             "inputs/market_data/pareto_daily.csv + pareto_share_prices.csv")
    parser.add_argument("--summary", action="store_true",
                        help="print summary from existing _manifest.json")
    args = parser.parse_args()
    if args.build_manifest:
        results = build_manifest()
        print_summary(results)
        return 0
    if args.extract:
        run_extraction()
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
