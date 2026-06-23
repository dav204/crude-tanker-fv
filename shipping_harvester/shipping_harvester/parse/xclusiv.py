"""Xclusiv Shipbrokers weekly parser.

Built against the real issue (week 23, 08 Jun 2026), not guessed. Xclusiv's
layout differs from Allied/Intermodal in three ways that matter:

  * Spot TCE lives in PROSE, not a table -- e.g.
    "VLCC: average T/CE ended the week ... at USD 193,873/day"
    "Capesize: C5TC average ... closing the week at USD 40,871/day"
    so we regex it. The change is quoted as "5.5k/day"; the level as a
    comma-grouped number "40,871/day" -- we capture the comma-grouped level,
    which side-steps the change figures.
  * Secondhand values are TRANSPOSED: age is the row (Resale / 5 / 10 / 15 Year)
    grouped under each class, value in the "Jun 2026" column. Handled by
    base.map_transposed_value_table.
  * Newbuild prices are a separate class-per-row table; current value first.

Verified here: spot TCE markers and newbuild lines (unit-tested on fixtures
mirroring the real issue's wording). The secondhand table extraction relies on
pdfplumber detecting the ruled grid -- confirm once with `cli inspect` on a real
issue in your env, since cell geometry can differ from my text view.

NOT yet implemented: demolition $/ldt (that page wasn't in view). Scrap can come
from GMS in the meantime; add a `_demolition` here once you `inspect` a real
Xclusiv recycling table.
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import replace

import pdfplumber

from ..models import (
    KIND_PERIOD_TC, KIND_SPOT_TCE, KIND_VESSEL_VALUE, Mark, MarketMarks,
)
from ..quarters import quarter_of
from . import base


# comma-grouped USD/day level (e.g. 40,871 or 193,873); ignores "5.5k/day" changes
_LEVEL = re.compile(r"USD\s*(\d{1,3}(?:,\d{3})+)\s*/?\s*day")

# 1-year T/C prose runs alongside spot; both quote "USD n/day", so a level is a
# TC mark only when "1y T/C" is the nearer rate-type keyword before it (vs the
# spot "T/CE"). Class = the nearest class word before the level.
_TC_CLASS = re.compile(
    r"\b(VLCC|Suezmax|Aframax|LR2|MR2|MR|Capesize|Kamsarmax|Panamax|Ultramax|Supramax|Handy)\b",
    re.I)

# (canonical class, marker regex). We take the first comma-grouped level after
# the marker. Markers use \s+ so they survive layout-mode multi-spacing.
_SPOT_MARKERS: list[tuple[str, re.Pattern]] = [
    # 2024 issues say "average T/CE"; the 2025 redesign abbreviates to "avg T/CE".
    ("VLCC", re.compile(r"VLCC:\s*(?:average|avg)\s+T/?CE", re.I)),
    ("Suezmax", re.compile(r"Suezmax:\s*(?:average|avg)\s+T/?CE", re.I)),
    ("Aframax", re.compile(r"Aframax:\s*(?:average|avg)\s+T/?CE", re.I)),
    ("Capesize", re.compile(r"Capesize:\s*C5TC", re.I)),
    ("Kamsarmax", re.compile(r"P5TC", re.I)),
    ("Ultramax", re.compile(r"Ultramax\s+S11TC", re.I)),
    ("Supramax", re.compile(r"Supramax\s+S10TC", re.I)),
    ("Handysize", re.compile(r"HS7TC", re.I)),
    ("MR", re.compile(r"MR\s+Atlantic\s+Basket", re.I)),
]

# classes printed in the newbuilding price tables (dry + tanker)
_NB_CLASSES = (
    "Capesize", "Kamsarmax", "Ultramax", "Handysize",
    "VLCC", "Suezmax", "Aframax", "Panamax", "MR2",
)

# row labels in the secondhand price tables -> canonical anchors
_AGE_LABELS = {
    "resale": ["resale"],
    "five_year": ["5 year"],
    "ten_year": ["10 year"],
    "fifteen_year": ["15 year"],
}

# --- flat-row era (2021-2023) -----------------------------------------------
# The pre-2024 issues print secondhand prices one row per (class, age) with an
# inline dwt ("VLCC 320k Resale  101.5 …", "Handy 38k 10y  19.3 …"); pdfplumber
# scrambles their glyph order, so we read poppler text and anchor on a KNOWN
# class word (the page is multi-column: TC prose shares each line with the table
# cell on the right, so a line-start anchor fails). The 2024 redesign drops the
# per-row dwt and floats the class label, which the geometry pass handles.
_FLAT_CLASSWORD = (
    r"(Capesize|Newcastlemax|Kamsarmax|Panamax|Ultramax|Supramax|"
    r"Handysize|Handy|VLCC|Suezmax|Aframax|LR2|LR1|MR2|MR)"
)
_FLAT_SH = re.compile(
    _FLAT_CLASSWORD + r"\s+\d{2,3}k\s+(Resale|5y|10y|15y)\s+\$?\s*(\d+\.?\d*)", re.I)
_FLAT_NB = re.compile(_FLAT_CLASSWORD + r"\s+\$?\s*(\d+\.?\d*)\s+\$?\s*\d", re.I)
_FLAT_AGE = {"resale": "resale", "5y": "five_year", "10y": "ten_year", "15y": "fifteen_year"}
# captured word -> harvester canonical; Handy->Handysize and MR2->MR so segment_of
# and build_vintage.CLASS_MAP agree with the rest of the codebase.
_FLAT_CLS = {
    "capesize": "Capesize", "newcastlemax": "Newcastlemax", "kamsarmax": "Kamsarmax",
    "panamax": "Panamax", "ultramax": "Ultramax", "supramax": "Supramax",
    "handysize": "Handysize", "handy": "Handysize", "vlcc": "VLCC",
    "suezmax": "Suezmax", "aframax": "Aframax", "lr2": "LR2", "lr1": "LR1",
    "mr2": "MR", "mr": "MR",
}


class XclusivParser(base.BrokerParser):
    broker_id = "xclusiv"

    def extract(self, tables, text: str) -> list[Mark]:
        return (self._spot(text) + self._period_tc(text)
                + self._newbuild(text) + self._secondhand(tables))

    # -- 1-year period TC (prose) -------------------------------------------
    @staticmethod
    def _period_tc(text: str) -> list[Mark]:
        norm = re.sub(r"\s+", " ", text)
        out: list[Mark] = []
        seen: set = set()
        for vm in _LEVEL.finditer(norm):
            val = float(vm.group(1).replace(",", ""))
            if not (8000 <= val <= 200000):        # TC band: drops change figures + spot spikes
                continue
            fwd = norm[vm.end():vm.end() + 16].lower()
            if re.match(r"\s*(firmer|softer|firm|soft|higher|lower)\b", fwd):
                continue                           # a change figure; real level follows "at USD"
            back = norm[max(0, vm.start() - 115):vm.start()].lower()
            i_tc = max(back.rfind("1y t/c"), back.rfind("1y tc"))
            i_sp = max(back.rfind("t/ce"), back.rfind(" tce"))
            if i_tc <= i_sp:                       # nearer rate-type is spot, skip
                continue
            cms = list(_TC_CLASS.finditer(back))
            if not cms:
                continue
            kw = cms[-1].group(1)
            cls = base.normalise_class("Handysize" if kw.lower() == "handy" else kw) or kw
            if cls in seen:
                continue
            seen.add(cls)
            out.append(Mark(kind=KIND_PERIOD_TC, vessel_class=cls, metric="1yr_tc",
                            value=val, unit="usd_per_day"))
        return out

    def parse(self, pdf_path, ref):
        """Two format eras. 2021-2023 ('flat-row' secondhand: class+dwt+age per
        line) parses from poppler text — pdfplumber scrambles these issues. 2024+
        (transposed, prose-interleaved two-column) uses the pdfplumber geometry
        pass, falling back to the table parser when geometry yields nothing."""
        ptext = base.extract_text_poppler(pdf_path)
        if self._is_flat(ptext):
            marks = (self._secondhand_flat(ptext) + self._newbuild_flat(ptext)
                     + self._period_tc(ptext) + self._spot(ptext))
            return MarketMarks(
                broker_id=ref.broker_id, report_date=ref.published,
                quarter=quarter_of(ref.published), source_post=ref.post_url,
                source_pdf=ref.pdf_url, parser=self.broker_id,
                parser_ok=bool(marks), marks=marks, raw_text_chars=len(ptext),
            )
        mm = super().parse(pdf_path, ref)
        geom = self._secondhand_geom(pdf_path)
        if not geom:
            return mm
        # geometry wins for the age curve; keep spot + newbuild from the text pass
        keep = [m for m in mm.marks
                if not (m.kind == KIND_VESSEL_VALUE and m.age_anchor and m.age_anchor != "newbuild")]
        marks = keep + geom
        return replace(mm, marks=marks, parser_ok=bool(marks))

    # -- flat-row era (2021-2023): poppler text -----------------------------
    @staticmethod
    def _is_flat(text: str) -> bool:
        """2021-2023 signature: secondhand rows carry an inline dwt+age
        ('180k Resale', '110k 5y'); the 2024 redesign drops the per-row dwt."""
        return bool(re.search(r"\d{2,3}k\s+(?:Resale|5y|10y|15y)\b", text, re.I))

    @staticmethod
    def _secondhand_flat(text: str) -> list[Mark]:
        out: list[Mark] = []
        seen: set = set()
        for m in _FLAT_SH.finditer(text):
            cls = _FLAT_CLS.get(m.group(1).lower())
            age = _FLAT_AGE.get(m.group(2).lower())
            if cls and age and (cls, age) not in seen:
                seen.add((cls, age))
                out.append(Mark(kind=KIND_VESSEL_VALUE, vessel_class=cls, metric="value",
                                value=float(m.group(3)), unit="musd", age_anchor=age))
        return out

    @staticmethod
    def _newbuild_flat(text: str) -> list[Mark]:
        a = re.search(r"NEWBUILDING PRICES", text, re.I)
        if not a:
            return []
        b = re.search(r"SECONDHAND", text[a.end():], re.I)
        window = text[a.start(): a.end() + b.start()] if b else text[a.start(): a.start() + 2500]
        out: list[Mark] = []
        seen: set = set()
        for m in _FLAT_NB.finditer(window):
            cls = _FLAT_CLS.get(m.group(1).lower())
            if cls and cls not in seen:
                seen.add(cls)
                out.append(Mark(kind=KIND_VESSEL_VALUE, vessel_class=cls, metric="value",
                                value=float(m.group(2)), unit="musd", age_anchor="newbuild"))
        return out

    # -- secondhand values, geometry (two-column text layout, pre-2025) -------
    @staticmethod
    def _age_in(tokens: list[str]) -> str | None:
        t = " ".join(tokens).lower()
        if re.search(r"\bresale\b", t):
            return "resale"
        m = re.search(r"\b(5|10|15)\s*year", t)
        return {"5": "five_year", "10": "ten_year", "15": "fifteen_year"}[m.group(1)] if m else None

    @staticmethod
    def _secondhand_geom(pdf_path) -> list[Mark]:
        """Reconstruct the secondhand age-curve from word coordinates: the value
        table sits in the left column (x0 < ~310), age label at x0 ~85, the
        current value the first numeric to its right. Classes are one-per-block
        (Resale→5→10→15yr); a monotonic-curve sanity filter drops mis-joins."""
        marks: list[Mark] = []
        try:
            pdf = pdfplumber.open(pdf_path)
        except Exception:
            return []
        with pdf:
            for page in pdf.pages:
                words = page.extract_words()
                if "SECONDHAND" not in " ".join(w["text"] for w in words).upper():
                    continue
                left = [w for w in words if w["x0"] < 310]
                rows: dict[int, list] = defaultdict(list)
                for w in left:
                    rows[round(w["top"])].append(w)
                blocks: list[dict] = []
                labels: list[tuple[float, str]] = []
                for top in sorted(rows):
                    line = sorted(rows[top], key=lambda w: w["x0"])
                    age = XclusivParser._age_in([w["text"] for w in line if w["x0"] < 140])
                    val = next((float(w["text"]) for w in line
                                if 120 < w["x0"] < 200 and re.fullmatch(r"\d+\.?\d*", w["text"])), None)
                    if age and val is not None:
                        if age == "resale":
                            blocks.append({"top": top, "vals": {}})
                        if blocks:
                            blocks[-1]["vals"][age] = val
                    for w in line:
                        c = base.normalise_class(w["text"])
                        if c and w["x0"] < 95:
                            labels.append((w["top"], c))
                labels.sort()
                # A block's class = the FIRST (topmost) class label inside its
                # vertical span [resale_top, resale_top+50). Where a tier shares
                # one curve (Xclusiv groups Kamsarmax/Panamax, Ultramax/Supramax —
                # the same Pana / Supra-Ultra tiers the engine uses), the topmost
                # label wins and reconciles with the newbuild from the text pass.
                if not labels:
                    continue
                for b in blocks:
                    inside = [c for t, c in labels if b["top"] <= t < b["top"] + 50]
                    cls = inside[0] if inside else min(labels, key=lambda L: abs(L[0] - b["top"]))[1]
                    seq = [b["vals"][a] for a in ("resale", "five_year", "ten_year", "fifteen_year")
                           if a in b["vals"]]
                    if seq != sorted(seq, reverse=True):     # age curve must be monotonic
                        continue
                    for age, val in b["vals"].items():
                        marks.append(Mark(kind=KIND_VESSEL_VALUE, vessel_class=cls,
                                          metric="value", value=val, unit="musd", age_anchor=age))
        return marks

    # -- spot TCE (prose) ----------------------------------------------------
    @staticmethod
    def _spot(text: str) -> list[Mark]:
        norm = re.sub(r"\s+", " ", text)
        marks: list[Mark] = []
        for vclass, marker in _SPOT_MARKERS:
            m = marker.search(norm)
            if not m:
                continue
            lm = _LEVEL.search(norm, m.end(), m.end() + 400)
            if lm:
                marks.append(
                    Mark(kind=KIND_SPOT_TCE, vessel_class=vclass, metric="spot_tce",
                         value=float(lm.group(1).replace(",", "")),
                         unit="usd_per_day", note="benchmark")
                )
        return marks

    # -- newbuild prices (class-per-row table, value = Jun 2026) -------------
    @staticmethod
    def _newbuild(text: str) -> list[Mark]:
        start = re.search(r"Newbuilding Prices", text, re.I)
        end = re.search(r"SECONDHAND|Sale\s*&\s*Purchase|S&P Activity", text, re.I)
        zone = text[(start.start() if start else 0): (end.start() if end else len(text))]
        marks: list[Mark] = []
        for cls in _NB_CLASSES:
            m = re.search(rf"(?m)^\s*{re.escape(cls)}\s+(\d+\.?\d*)\b", zone)
            if m:
                marks.append(
                    Mark(kind=KIND_VESSEL_VALUE,
                         vessel_class=base.normalise_class(cls) or cls,
                         metric="value", value=float(m.group(1)),
                         unit="musd", age_anchor="newbuild")
                )
        return marks

    # -- secondhand values (transposed table) -------------------------------
    @staticmethod
    def _secondhand(tables) -> list[Mark]:
        marks: list[Mark] = []
        for tbl in tables:
            flat = " ".join(" ".join(r) for r in tbl).lower()
            if "resale" in flat and "5 year" in flat:
                marks += base.map_transposed_value_table(
                    tbl, anchor_labels=_AGE_LABELS,
                    kind=KIND_VESSEL_VALUE, metric="value", unit="musd",
                )
        return marks
