"""Allied Shipbroking weekly -- EXAMPLE parser.

The keyword maps below encode the typical Allied free-weekly layout. They WILL
need a quick check against a real issue (`cli inspect`) before you trust the
numbers -- treat the specific keywords as a starting point, not gospel.

Allied's free 'S&P Statistics' weekly carries: secondhand values by class/age,
period (1-yr) TC, and demolition $/ldt by recycling market.
"""
from __future__ import annotations

from ..models import KIND_DEMOLITION, KIND_PERIOD_TC, KIND_VESSEL_VALUE, Mark
from . import base


class AlliedParser(base.BrokerParser):
    broker_id = "allied"

    # header keywords -> age anchor, for the secondhand value table
    VALUE_COLUMNS = {
        "newbuild": ["newbuild", "resale", "newbuilding"],
        "five_year": ["5 year", "5 yr", "5year", "5-year", "five"],
        "ten_year": ["10 year", "10 yr", "10year", "10-year", "ten"],
        # scrap usually lives in the demolition table; if Allied prints a
        # scrap-equivalent column here, add its keyword:
        # "scrap": ["scrap"],
    }
    PERIOD_TC_COLUMNS = {None: ["12 months", "1 year", "period", "1yr", "12 mos"]}
    DEMO_COLUMNS = {None: ["$/ldt", "usd/ldt", "$ /ldt", "ldt"]}

    def extract(self, tables, text: str) -> list[Mark]:
        marks: list[Mark] = []

        # 1) vessel values ($m, by class x age anchor)
        vtab = base.find_table(tables, must_have=["second"], header_rows=2) \
            or base.find_table(tables, must_have=["value"], header_rows=2)
        if vtab:
            marks += base.map_value_table(
                vtab, self.VALUE_COLUMNS,
                kind=KIND_VESSEL_VALUE, metric="value", unit="musd",
            )

        # 2) period / 1-yr TC ($/day)
        ttab = base.find_table(tables, must_have=["period"], header_rows=2) \
            or base.find_table(tables, must_have=["12 months"], header_rows=2)
        if ttab:
            marks += base.map_value_table(
                ttab, self.PERIOD_TC_COLUMNS,
                kind=KIND_PERIOD_TC, metric="1yr_tc", unit="usd_per_day",
            )

        # 3) demolition ($/ldt) -- note column key here is recycling market,
        #    so we map by market name rather than vessel class. Kept simple:
        dtab = base.find_table(tables, must_have=["ldt"], header_rows=2)
        if dtab:
            marks += self._demolition(dtab)

        return marks

    @staticmethod
    def _demolition(table) -> list[Mark]:
        """Demolition tables are organised by recycling market, not class.
        Pull each market's $/ldt for tankers/bulkers if labelled, else the
        first numeric per market row."""
        out: list[Mark] = []
        markets = ("bangladesh", "india", "pakistan", "turkey", "china")
        for row in table:
            label = (row[0] if row else "").lower()
            market = next((m for m in markets if m in label), None)
            if market is None:
                continue
            for cell in row[1:]:
                val = base.clean_num(cell)
                if val and val > 100:  # $/ldt sanity floor
                    out.append(
                        Mark(kind=KIND_DEMOLITION, vessel_class="*",
                             metric="$/ldt", value=val, unit="usd_per_ldt",
                             note=market)
                    )
                    break
        return out
