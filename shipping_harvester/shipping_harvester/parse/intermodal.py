"""Intermodal weekly -- EXAMPLE parser. Same pattern as Allied; Intermodal also
prints route spot TCE, so we show that field too. Tune keywords against a real
issue with `cli inspect`.
"""
from __future__ import annotations

from ..models import (
    KIND_PERIOD_TC, KIND_SPOT_TCE, KIND_VESSEL_VALUE, Mark,
)
from . import base


class IntermodalParser(base.BrokerParser):
    broker_id = "intermodal"

    VALUE_COLUMNS = {
        "newbuild": ["resale", "newbuild"],
        "five_year": ["5 year", "5yr", "five"],
        "ten_year": ["10 year", "10yr", "ten"],
        "scrap": ["scrap"],
    }
    PERIOD_TC_COLUMNS = {None: ["12 months", "1 year", "period"]}
    SPOT_TCE_COLUMNS = {None: ["tce", "$/day", "spot"]}

    def extract(self, tables, text: str) -> list[Mark]:
        marks: list[Mark] = []

        vtab = base.find_table(tables, ["value"]) or base.find_table(tables, ["price"])
        if vtab:
            marks += base.map_value_table(
                vtab, self.VALUE_COLUMNS,
                kind=KIND_VESSEL_VALUE, metric="value", unit="musd",
            )

        ttab = base.find_table(tables, ["period"]) or base.find_table(tables, ["12 months"])
        if ttab:
            marks += base.map_value_table(
                ttab, self.PERIOD_TC_COLUMNS,
                kind=KIND_PERIOD_TC, metric="1yr_tc", unit="usd_per_day",
            )

        stab = base.find_table(tables, ["tce"])
        if stab:
            marks += base.map_value_table(
                stab, self.SPOT_TCE_COLUMNS,
                kind=KIND_SPOT_TCE, metric="spot_tce", unit="usd_per_day",
            )

        return marks
