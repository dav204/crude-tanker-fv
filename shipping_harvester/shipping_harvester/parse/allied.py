"""Allied Shipbroking — Weekly Market Report parser.

Two distinct Allied products appear in the free archives:

  * **Weekly Market Report** (Capital Link, recovered from the Wayback Machine for
    2019-2020): carries the value age-curve we need — 'Indicative Dry Bulk Values'
    and 'Indicative Tanker Values' (Resale / 5 / 10 / 15-year by class) plus
    'Indicative Dry/Wet NB Prices'. THIS is what we parse.
  * **S&P Statistics** (Hellenic Shipping News, 2021-2023): a transaction-statistics
    supplement — deal counts, invested capital, scrapping averages — with NO value
    grid. We deliberately yield nothing on it (the value curve for 2021+ comes from
    Xclusiv).

So the parser probes for the 'Indicative … Values' tables and only emits marks for
the Weekly Market Report. pdfplumber scrambles these PDFs' glyph order, so we read
poppler text (the same path as the Xclusiv flat-row era).
"""
from __future__ import annotations

import re

from ..models import KIND_PERIOD_TC, KIND_VESSEL_VALUE, Mark, MarketMarks
from ..quarters import quarter_of
from . import base

# classes Allied tabulates (dry: Cape/Pana/Supra/Handy; wet: VLCC/Suez/Afra/MR + LR)
_DRY = ("Capesize", "Newcastlemax", "Kamsarmax", "Panamax", "Ultramax", "Supramax", "Handysize")
_WET = ("VLCC", "Suezmax", "Aframax", "LR2", "LR1", "MR2", "MR")
_ALL = _DRY + _WET
_CANON = {c.lower(): c for c in _ALL}

_HDR = re.compile(r"^\s*(" + "|".join(_ALL) + r")\b", re.I)
_AGEROW = re.compile(
    r"\d{2,3}k\s*dwt\s+(Resale|5 year old|10 year old|15 year old)\s+(\d+\.?\d*)", re.I)
_NB = re.compile(r"(" + "|".join(_ALL) + r")\s*\([\d,]+\s*dwt\)\s+(\d+\.?\d*)", re.I)
_AGE = {"resale": "resale", "5 year old": "five_year",
        "10 year old": "ten_year", "15 year old": "fifteen_year"}

# 'period market TC rates' tables (the only TC source for the 2019-2020 vintages,
# since Intermodal/Xclusiv aren't on HSN that far back). A class header on its own
# line, then a '12 months $X …' row. Emit class names aligned to HARV_TC_KEY so
# build_vintage consumes them: pana->Kamsarmax, supra_ultra->Ultramax.
_TC_HDR = re.compile(r"^\s*(" + "|".join(_ALL) + r")\b", re.I)
_TC_12MO = re.compile(r"12\s*months?\s+\$?\s*([\d,]+)", re.I)
_TC_CANON = {"capesize": "Capesize", "newcastlemax": "Capesize",
             "panamax": "Kamsarmax", "kamsarmax": "Kamsarmax",
             "supramax": "Ultramax", "ultramax": "Ultramax", "handysize": "Handysize",
             "vlcc": "VLCC", "suezmax": "Suezmax", "aframax": "Aframax",
             "lr2": "LR2", "lr1": "LR2", "mr2": "MR", "mr": "MR"}


def _section(text: str, start: str, ends: tuple) -> str:
    low = text.lower()
    i = low.find(start.lower())
    if i < 0:
        return ""
    j = len(text)
    for e in ends:
        k = low.find(e.lower(), i + len(start))
        if 0 <= k < j:
            j = k
    return text[i:j]


class AlliedParser(base.BrokerParser):
    broker_id = "allied"

    def extract(self, tables, text: str) -> list[Mark]:
        # unused — parse() drives extraction from poppler text (see module docstring)
        return []

    def parse(self, pdf_path, ref) -> MarketMarks:
        ptext = base.extract_text_poppler(pdf_path)
        marks = self._secondhand(ptext) + self._newbuild(ptext) + self._period_tc(ptext)
        return MarketMarks(
            broker_id=ref.broker_id, report_date=ref.published,
            quarter=quarter_of(ref.published), source_post=ref.post_url,
            source_pdf=ref.pdf_url, parser=self.broker_id,
            parser_ok=bool(marks), marks=marks, raw_text_chars=len(ptext),
        )

    @staticmethod
    def _secondhand(text: str) -> list[Mark]:
        out: list[Mark] = []
        seen: set = set()
        windows = (
            _section(text, "Indicative Dry Bulk Values", ("Indicative Tanker Values",)),
            _section(text, "Indicative Tanker Values",
                     ("Indicative Dry NB", "Reported Transactions", "Sale & Purchase", "Disclaimer")),
        )
        for win in windows:
            cur = None
            for line in win.splitlines():
                if "dwt" not in line.lower():
                    h = _HDR.match(line)
                    if h:
                        cur = _CANON[h.group(1).lower()]
                    continue
                m = _AGEROW.search(line)
                if m and cur:
                    age = _AGE[m.group(1).lower()]
                    if (cur, age) not in seen:
                        seen.add((cur, age))
                        out.append(Mark(kind=KIND_VESSEL_VALUE, vessel_class=cur, metric="value",
                                        value=float(m.group(2)), unit="musd", age_anchor=age))
        return out

    @staticmethod
    def _period_tc(text: str) -> list[Mark]:
        secs = (_section(text, "Dry Bulk period market TC rates", ("Latest indicative", "Indicative"))
                + "\n"
                + _section(text, "Tanker period market TC rates", ("Latest indicative", "Indicative")))
        out: list[Mark] = []
        seen: set = set()
        cur = None
        for line in secs.splitlines():
            low = line.lower()
            if "month" not in low:
                h = _TC_HDR.match(line)
                if h:
                    cur = _TC_CANON.get(h.group(1).lower())
                continue
            m = _TC_12MO.search(line)
            if m and cur and cur not in seen:
                val = float(m.group(1).replace(",", ""))
                if 3000 <= val <= 200000:
                    seen.add(cur)
                    out.append(Mark(kind=KIND_PERIOD_TC, vessel_class=cur, metric="1yr_tc",
                                    value=val, unit="usd_per_day"))
        return out

    @staticmethod
    def _newbuild(text: str) -> list[Mark]:
        win = (_section(text, "Indicative Dry NB",
                        ("Reported Transactions", "Sale & Purchase", "Indicative Dry Bulk Values", "Disclaimer"))
               + _section(text, "Indicative Wet NB",
                          ("Reported Transactions", "Indicative Dry Bulk Values", "Disclaimer")))
        out: list[Mark] = []
        seen: set = set()
        for m in _NB.finditer(win):
            c = _CANON[m.group(1).lower()]
            if c not in seen:
                seen.add(c)
                out.append(Mark(kind=KIND_VESSEL_VALUE, vessel_class=c, metric="value",
                                value=float(m.group(2)), unit="musd", age_anchor="newbuild"))
        return out
