"""Intermodal Shipbrokers weekly — 1-year time-charter rates.

Intermodal's free weekly carries a clean 'TC Rates' table (stable across 2021-2026):
1yr/3yr TC by dwt, lowercase 'k' for tankers and uppercase 'K' for dry bulk — the
case disambiguates a 75k Panamax *tanker* from a 76K Panamax *bulker*. We emit the
1-year TC per class and NOTHING else: no vessel_value, so the value spine stays
single-vendor (Xclusiv / Allied) and Intermodal only enriches the TC forward. It is
the sole TC source for 2025Q3+, where Xclusiv stopped printing its 1y-T/C prose.

Class is mapped from dwt + the k/K segment, NOT the printed labels — the labels
collide with right-column chart legends (e.g. 'VLCC TCE'). Pana = Kamsarmax/Panamax
and Supra-Ultra = Supramax/Ultramax (both fold to one engine class downstream), so
the dwt bands are deliberately coarse.
"""
from __future__ import annotations

import re

from ..models import KIND_PERIOD_TC, Mark, MarketMarks
from ..quarters import quarter_of
from . import base

# (lo_dwt, hi_dwt, canonical class) per segment. Skips the 75k LR1/Panamax tanker
# and 36k handy tanker (not engine TC keys) by leaving gaps in the bands.
_TC_TANKER = [(280, 330, "VLCC"), (140, 170, "Suezmax"), (100, 125, "Aframax"), (45, 58, "MR")]
# Pana->Kamsarmax and Supra-Ultra->Ultramax to match build_vintage.HARV_TC_KEY
# (the engine's pana / supra_ultra anchors read those exact harvester class names).
_TC_DRY = [(165, 205, "Capesize"), (70, 92, "Kamsarmax"), (50, 68, "Ultramax"), (28, 40, "Handysize")]
_TC_ROW = re.compile(r"(\d{2,3})([kK])\s*1\s*yr\s*TC\s+([\d,]+)", re.I)


class IntermodalParser(base.BrokerParser):
    broker_id = "intermodal"

    def extract(self, tables, text: str) -> list[Mark]:
        return []  # parse() drives extraction from poppler text

    def parse(self, pdf_path, ref) -> MarketMarks:
        ptext = base.extract_text_poppler(pdf_path)
        marks = self._period_tc(ptext)
        return MarketMarks(
            broker_id=ref.broker_id, report_date=ref.published,
            quarter=quarter_of(ref.published), source_post=ref.post_url,
            source_pdf=ref.pdf_url, parser=self.broker_id,
            parser_ok=bool(marks), marks=marks, raw_text_chars=len(ptext),
        )

    @staticmethod
    def _period_tc(text: str) -> list[Mark]:
        out: list[Mark] = []
        seen: set = set()
        for m in _TC_ROW.finditer(text):
            dwt = int(m.group(1))
            tanker = m.group(2) == "k"
            val = float(m.group(3).replace(",", ""))
            cls = next((c for lo, hi, c in (_TC_TANKER if tanker else _TC_DRY) if lo <= dwt <= hi), None)
            if cls and cls not in seen and 5000 <= val <= 200000:
                seen.add(cls)
                out.append(Mark(kind=KIND_PERIOD_TC, vessel_class=cls, metric="1yr_tc",
                                value=val, unit="usd_per_day"))
        return out
