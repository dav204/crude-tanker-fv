"""Parser foundation.

PDF table extraction is the one part that genuinely needs tuning against each
broker's real layout -- column order, header wording and units differ by house
and even drift over time. So the design is:

  * shared extraction utilities (pdfplumber-based, per the pdf-reading guide),
  * a BrokerParser ABC,
  * a GenericParser that never fails (records the issue, extracts no marks),
  * per-broker subclasses that fill in the field mapping.

Workflow to add/repair a parser:
  1. `python -m shipping_harvester.cli inspect <issue.pdf>` to dump tables.
  2. Read the dump, identify which table index holds values / TC / demolition.
  3. Set the COLUMN_MAP / header keywords in that broker's module.
"""
from __future__ import annotations

import re
from abc import ABC, abstractmethod
from pathlib import Path

import pdfplumber

from ..models import Mark, MarketMarks, ReportRef
from ..quarters import quarter_of


# --- extraction -------------------------------------------------------------
def extract_tables(pdf_path: str | Path) -> list[list[list[str]]]:
    """All tables across all pages, cells coerced to stripped strings."""
    out: list[list[list[str]]] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            for tbl in page.extract_tables() or []:
                cleaned = [
                    [("" if c is None else str(c).strip()) for c in row]
                    for row in tbl
                ]
                out.append(cleaned)
    return out


def extract_text(pdf_path: str | Path, layout: bool = True) -> str:
    """Full text. layout=True keeps column positioning (better for the many
    multi-column broker weeklies) per the pdf-reading guidance."""
    chunks = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            chunks.append(page.extract_text(layout=layout) or "")
    return "\n".join(chunks)


def extract_text_poppler(pdf_path: str | Path, layout: bool = True) -> str:
    """Text via poppler's ``pdftotext``. Several broker weeklies (Allied; Xclusiv
    pre-2024) embed fonts whose glyph ORDER pdfplumber scrambles — the text layer
    is there but mis-sequenced — while poppler reads them correctly. Falls back to
    the pdfplumber extractor when pdftotext is unavailable."""
    import shutil
    import subprocess
    exe = shutil.which("pdftotext")
    if exe:
        cmd = [exe] + (["-layout"] if layout else []) + [str(pdf_path), "-"]
        try:
            return subprocess.run(cmd, capture_output=True, text=True, timeout=90).stdout
        except subprocess.SubprocessError:
            pass
    return extract_text(pdf_path, layout=layout)


# --- value cleaning ---------------------------------------------------------
_RANGE = re.compile(r"(\d[\d.]*)\s*[-–—]\s*(\d[\d.]*)")
_NUM = re.compile(r"-?\d[\d.]*")


def clean_num(s: str) -> float | None:
    """'$ 92.5m' -> 92.5 ; '45,000 /day' -> 45000 ; '40-45' -> 42.5 (midpoint).

    A hyphen flanked by digits is treated as a range separator (midpoint),
    not a minus sign.
    """
    if not s:
        return None
    s2 = s.replace(",", "")
    rng = _RANGE.search(s2)
    if rng:
        return (float(rng.group(1)) + float(rng.group(2))) / 2.0
    m = _NUM.search(s2)
    return float(m.group()) if m else None


# --- vessel class normalisation --------------------------------------------
VESSEL_CLASS_ALIASES: dict[str, str] = {
    # tankers
    "vlcc": "VLCC", "suezmax": "Suezmax", "aframax": "Aframax",
    "lr2": "LR2", "lr1": "LR1", "mr": "MR", "mr2": "MR", "handy": "Handy",
    # dry
    "capesize": "Capesize", "cape": "Capesize", "newcastlemax": "Newcastlemax",
    "kamsarmax": "Kamsarmax", "panamax": "Panamax", "ultramax": "Ultramax",
    "supramax": "Supramax", "handysize": "Handysize", "handymax": "Handymax",
    # gas
    "lng": "LNGC", "lngc": "LNGC", "vlgc": "VLGC", "mgc": "MGC", "lpg": "VLGC",
}


def normalise_class(s: str) -> str | None:
    key = s.strip().lower()
    for alias, canon in VESSEL_CLASS_ALIASES.items():
        if alias in key:
            return canon
    return None


def flatten_header(table: list[list[str]], n_rows: int = 2) -> str:
    return " ".join(" ".join(r) for r in table[:n_rows]).lower()


def _kw_match(text: str, kw: str) -> bool:
    """Keyword test that won't let '5 year' match '15 year': the keyword must
    not be immediately preceded by a digit. Case-insensitive (text pre-lowered
    by callers; kw lowered here)."""
    return re.search(r"(?<!\d)" + re.escape(kw.lower()), text) is not None


def find_table(
    tables: list[list[list[str]]], must_have: list[str], header_rows: int = 2
) -> list[list[str]] | None:
    """First table whose first `header_rows` rows contain ALL keywords."""
    for tbl in tables:
        head = flatten_header(tbl, header_rows)
        if all(k.lower() in head for k in must_have):
            return tbl
    return None


def col_index_by_keyword(
    table: list[list[str]], keywords: list[str], header_rows: int = 2
) -> int | None:
    """Index of the first column whose header cell(s) contain any keyword.

    Located by header text, not fixed position, so it survives column reorders.
    """
    if not table:
        return None
    width = max((len(r) for r in table[:header_rows]), default=0)
    for ci in range(width):
        cell = " ".join(
            table[ri][ci]
            for ri in range(min(header_rows, len(table)))
            if ci < len(table[ri])
        ).lower()
        if any(_kw_match(cell, k) for k in keywords):
            return ci
    return None


def class_col_index(table: list[list[str]], start_row: int = 0) -> int | None:
    """Column most likely holding vessel-class labels: the one with the most
    normalisable class names below the header. Needs >=2 hits to qualify."""
    if not table:
        return None
    width = max((len(r) for r in table), default=0)
    best_ci, best_hits = None, 0
    for ci in range(width):
        hits = sum(
            1 for row in table[start_row:]
            if ci < len(row) and normalise_class(row[ci])
        )
        if hits > best_hits:
            best_ci, best_hits = ci, hits
    return best_ci if best_hits >= 2 else None


def map_value_table(
    table: list[list[str]],
    column_keywords: dict[str | None, list[str]],
    *,
    kind: str,
    metric: str,
    unit: str,
) -> list[Mark]:
    """Generic class x column -> Marks.

    `column_keywords` maps each target column to header keywords that identify
    it: use age anchors as keys for value tables
    ({"five_year": ["5", "year"], ...}) or {None: [...]} for a single-metric
    table (period TC, demolition). This is the only thing a broker parser needs
    to supply once you've eyeballed the layout.

    The header region is detected dynamically (first row containing a vessel
    class marks the start of data), so 1- and 2-row headers both work.
    """
    marks: list[Mark] = []
    if not table:
        return marks

    # first row that looks like data (has a class) ends the header region
    first_data = next(
        (i for i, row in enumerate(table) if any(normalise_class(c) for c in row)),
        len(table),
    )
    if first_data == len(table):
        return marks
    header_rows = max(first_data, 1)

    ccol = class_col_index(table, start_row=0)
    if ccol is None:
        return marks
    cols = {
        anchor: ci
        for anchor, kws in column_keywords.items()
        if (ci := col_index_by_keyword(table, kws, header_rows)) is not None
    }
    for row in table[first_data:]:
        if ccol >= len(row):
            continue
        vclass = normalise_class(row[ccol])
        if not vclass:
            continue
        for anchor, ci in cols.items():
            if ci < len(row) and (val := clean_num(row[ci])) is not None:
                marks.append(
                    Mark(kind=kind, vessel_class=vclass, metric=metric,
                         value=val, unit=unit, age_anchor=anchor)
                )
    return marks


def map_transposed_value_table(
    table: list[list[str]],
    *,
    anchor_labels: dict[str, list[str]],
    kind: str,
    metric: str,
    unit: str,
    class_order: list[str] | None = None,
) -> list[Mark]:
    """For tables laid out as age-per-row, class-per-group (e.g. Xclusiv's
    secondhand prices): each class spans a block of rows whose first cell is an
    age label (Resale / 5 Year / ...), and the current value is the first
    numeric cell after that label ("Jun 2026" column).

    `anchor_labels` maps each canonical anchor to row-label keywords
    ({"five_year": ["5 year"], ...}). The class is read from a class-label cell
    that precedes the age label (gridded tables put it in column 0 of the
    group's first row); when class labels are missing/garbled, pass `class_order`
    and groups are assigned by order, advanced each time the first anchor recurs.
    """
    marks: list[Mark] = []
    if not table:
        return marks
    first_anchor = next(iter(anchor_labels), None)
    current: str | None = None
    order_idx = -1

    for row in table:
        low = [c.lower() for c in row]
        anchor, label_ci = None, None
        for a, kws in anchor_labels.items():
            for ci, cell in enumerate(low):
                if any(_kw_match(cell, k) for k in kws):
                    anchor, label_ci = a, ci
                    break
            if anchor:
                break

        if anchor is None:
            # header or class-only row: update current class if one appears
            for cell in row:
                if (c := normalise_class(cell)):
                    current = c
            continue

        # class from any cell before the age label
        found = next(
            (c for ci in range(label_ci) if (c := normalise_class(row[ci]))), None
        )
        if found:
            current = found
        elif class_order and anchor == first_anchor:
            order_idx += 1
            current = class_order[order_idx] if order_idx < len(class_order) else current

        # value = first numeric cell after the label
        val = next(
            (v for cell in row[label_ci + 1:] if (v := clean_num(cell)) is not None),
            None,
        )
        if val is not None and current:
            marks.append(
                Mark(kind=kind, vessel_class=current, metric=metric,
                     value=val, unit=unit, age_anchor=anchor)
            )
    return marks


# --- parser interface -------------------------------------------------------
class BrokerParser(ABC):
    broker_id: str = "base"

    @abstractmethod
    def extract(self, tables, text: str) -> list[Mark]:
        """Return the marks found in this issue. Implemented per broker."""

    def parse(self, pdf_path: str | Path, ref: ReportRef) -> MarketMarks:
        tables = extract_tables(pdf_path)
        text = extract_text(pdf_path)
        marks = self.extract(tables, text)
        return MarketMarks(
            broker_id=ref.broker_id,
            report_date=ref.published,
            quarter=quarter_of(ref.published),
            source_post=ref.post_url,
            source_pdf=ref.pdf_url,
            parser=self.broker_id,
            parser_ok=bool(marks),
            marks=marks,
            raw_text_chars=len(text),
        )


class GenericParser(BrokerParser):
    """Fallback: records the issue, extracts nothing. Never raises."""
    broker_id = "generic"

    def extract(self, tables, text: str) -> list[Mark]:
        return []

    def parse(self, pdf_path: str | Path, ref: ReportRef) -> MarketMarks:
        try:
            text = extract_text(pdf_path)
        except Exception:
            text = ""
        return MarketMarks(
            broker_id=ref.broker_id,
            report_date=ref.published,
            quarter=quarter_of(ref.published),
            source_post=ref.post_url,
            source_pdf=ref.pdf_url,
            parser="generic",
            parser_ok=False,
            marks=[],
            raw_text_chars=len(text),
        )
