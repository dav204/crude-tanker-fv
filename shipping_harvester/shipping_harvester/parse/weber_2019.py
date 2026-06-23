"""Charles R. Weber weekly -- LEGACY format parser (~2015-2022).

The pre-2023 Weber tanker report used a single 'Spot Market' table: per class a
'(13.0 Kts L/B)' header, route rows carrying WS + TCE for two dates, and a
'<Class> Average Earnings  $wk1  $wk2' summary row. We pull spot TCE per class
from that summary (latest = week-2 column). This era predates the 'Time Charter
1 Year v. 3 Years' callout, so it yields spot_tce only -- no period TC.

The dispatcher routes issues whose text lacks 'TANKER ROUTES' (the current-format
marker) here. Based on a 2019 sample; confirm with `cli inspect` against a real
legacy issue before trusting a deep backfill.
"""
from __future__ import annotations

import re

from ..models import KIND_SPOT_TCE, Mark
from . import base
from .weber import _CLASS_DISPLAY


class WeberParser2019(base.BrokerParser):
    broker_id = "weber"

    def extract(self, tables, text: str) -> list[Mark]:
        norm = re.sub(r"\s+", " ", text)
        marks: list[Mark] = []
        for upper, disp in _CLASS_DISPLAY.items():
            # "<CLASS> Average Earnings  $17,520  $15,700"  (latest = 2nd)
            m = re.search(
                rf"\b{upper}\b\s+Average\s+Earnings\s*\+?\s*\$([\d,]+)\s+\$([\d,]+)",
                norm, re.I,
            )
            if m:
                week2 = float(m.group(2).replace(",", ""))
                marks.append(Mark(
                    KIND_SPOT_TCE, disp, "spot_tce", week2, "usd_per_day",
                    note="weighted average earnings (latest week, legacy format)",
                ))
        return marks
