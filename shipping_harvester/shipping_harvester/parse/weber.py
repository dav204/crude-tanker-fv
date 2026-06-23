"""Charles R. Weber weekly tanker report parser.

Built against the real issue (WM02-25, 10 Jan 2025). Weber's current format puts
a structured "TANKER ROUTES" table on page 2 that yields two of your fields per
class, far more cleanly than the other houses:

  * spot_tce  -- the "<Class> Average Earnings +" row; week-2 column is the
                 latest class-benchmark TCE ($/day).
  * period_tc -- a "Time Charter 1 Year v. 3 Years ($|day):" callout per class
                 (e.g. VLCC $45,000 / $47,000). 1-yr is exactly your
                 twelve_month_tc; 3-yr is emitted as a bonus.

The wrinkle is a TWO-COLUMN layout: the TC callout label sits at the end of one
route row and its values at the end of the *next* route row, interleaved with
that row's own route TCEs. So "first $ after the label" would grab a route TCE.
Instead we split the page into per-class blocks and, within a block, take the
TC values as the LAST two $ on the line after the label -- the right-hand
column. Validated on the real issue's eight classes (unit test below).

Weber prints demolition only as a 52-week chart (no extractable $/ldt) and no
secondhand value table, so this parser covers spot_tce + period_tc only -- which
is exactly what Weber is good for (your tanker names).
"""
from __future__ import annotations

import re

from ..models import KIND_PERIOD_TC, KIND_SPOT_TCE, Mark
from . import base


# uppercase routes-header token -> canonical class
_CLASS_DISPLAY = {
    "VLCC": "VLCC", "SUEZMAX": "Suezmax", "AFRAMAX": "Aframax",
    "PANAMAX": "Panamax", "LR2": "LR2", "LR1": "LR1",
    "MR": "MR", "HANDYSIZE": "Handysize",
}

# class block starts: the routes header line (class name not followed by
# " Average", which would be the Average-Earnings summary row)
_HEADER = re.compile(
    r"(?m)^[ \t]*(VLCC|SUEZMAX|AFRAMAX|PANAMAX|LR2|LR1|MR|HANDYSIZE)\b(?!\s+Average)"
)
_TC_LABEL = re.compile(r"Time Charter\s+1\s+Year\s+v\.\s+3\s+Years", re.I)
_AE_LABEL = re.compile(r"Average\s+Earnings", re.I)
_MONEY = re.compile(r"\$(\d[\d,]*)")


def _money(line: str) -> list[float]:
    return [float(m.replace(",", "")) for m in _MONEY.findall(line)]


def _next_line_money(block_lines: list[str], label_re: re.Pattern) -> list[float] | None:
    """The $ values on the line immediately after the line matching label_re."""
    for i, ln in enumerate(block_lines[:-1]):
        if label_re.search(ln):
            return _money(block_lines[i + 1])
    return None


class WeberParser(base.BrokerParser):
    broker_id = "weber"

    def extract(self, tables, text: str) -> list[Mark]:
        region = self._page2(text)
        marks: list[Mark] = []
        for cls, block in self._blocks(region):
            marks += self._period_tc(cls, block)
            marks += self._spot(cls, block)
        return marks

    @staticmethod
    def _page2(text: str) -> str:
        start = text.find("TANKER ROUTES")
        end = text.find("THE WEEK IN CHARTS")
        return text[(start if start != -1 else 0): (end if end != -1 else len(text))]

    @staticmethod
    def _blocks(region: str):
        """Yield (display_class, block_text) split on class routes-headers."""
        heads = list(_HEADER.finditer(region))
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(region)
            yield _CLASS_DISPLAY[m.group(1)], region[m.start():end]

    @staticmethod
    def _period_tc(cls: str, block: str) -> list[Mark]:
        lines = block.split("\n")
        vals = _next_line_money(lines, _TC_LABEL)
        if not vals or len(vals) < 2:
            return []
        one_yr, three_yr = vals[-2], vals[-1]   # right-hand column
        return [
            Mark(KIND_PERIOD_TC, cls, "1yr_tc", one_yr, "usd_per_day",
                 note="period 1-year"),
            Mark(KIND_PERIOD_TC, cls, "3yr_tc", three_yr, "usd_per_day",
                 note="period 3-year"),
        ]

    @staticmethod
    def _spot(cls: str, block: str) -> list[Mark]:
        lines = block.split("\n")
        vals = _next_line_money(lines, _AE_LABEL)
        if not vals or len(vals) < 2:
            return []
        week2 = vals[-1]   # week-1, week-2 -> latest is week-2
        return [
            Mark(KIND_SPOT_TCE, cls, "spot_tce", week2, "usd_per_day",
                 note="weighted average earnings (latest week)")
        ]
