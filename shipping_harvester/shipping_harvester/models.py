"""Typed records that flow through the harvester.

The pipeline is:  ReportRef  -->  (downloaded PDF)  -->  MarketMarks  -->  store
Everything is plain dataclasses so it serialises cleanly to JSON and pandas.
"""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field, asdict
from typing import Optional


# --- canonical vocab --------------------------------------------------------
# Keep these controlled so downstream joins (your [Q] merge) are stable.

AGE_ANCHORS = ("newbuild", "five_year", "ten_year", "scrap")

# Field "kinds" a parser can emit. Mirrors the source-map you wrote.
KIND_VESSEL_VALUE = "vessel_value"   # $m by class x age anchor
KIND_PERIOD_TC = "period_tc"         # 1-yr / period time-charter, $/day
KIND_SPOT_TCE = "spot_tce"           # route TCE assessment, $/day
KIND_DEMOLITION = "demolition"       # $/ldt by recycling market


@dataclass(slots=True)
class ReportRef:
    """One weekly issue from one broker, discovered during crawl.

    `published` is the authoritative date (from the CMS), used for both
    de-duplication (broker + ISO week) and [Q] assignment.
    """
    broker_id: str                 # canonical id, e.g. "allied"
    source: str                    # aggregator id, e.g. "hsn" | "capitallink"
    title: str
    post_url: str
    pdf_url: Optional[str]
    published: dt.date

    @property
    def iso_year(self) -> int:
        return self.published.isocalendar().year

    @property
    def iso_week(self) -> int:
        return self.published.isocalendar().week

    @property
    def dedupe_key(self) -> tuple[str, int, int]:
        return (self.broker_id, self.iso_year, self.iso_week)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["published"] = self.published.isoformat()
        d["iso_year"] = self.iso_year
        d["iso_week"] = self.iso_week
        return d


@dataclass(slots=True)
class Mark:
    """A single extracted data point. Long/tidy format on purpose -- this is
    what plugs straight into a [Q]-keyed factor table.
    """
    kind: str                      # one of KIND_*
    vessel_class: str              # "VLCC", "Suezmax", "Capesize", "LNGC", ...
    metric: str                    # "value" | "1yr_tc" | "spot_tce" | "$/ldt" | "scrubber_premium" | ...
    value: float
    unit: str                      # "musd" | "usd_per_day" | "usd_per_ldt" | "pct"
    age_anchor: Optional[str] = None   # only for KIND_VESSEL_VALUE
    note: Optional[str] = None         # free text, e.g. recycling market or route code


@dataclass(slots=True)
class MarketMarks:
    """All marks parsed out of one issue, plus provenance for auditing."""
    broker_id: str
    report_date: dt.date
    quarter: str                   # "2026Q2"
    source_post: str
    source_pdf: Optional[str]
    parser: str                    # which parser produced this (or "generic")
    parser_ok: bool                # did a real (non-generic) parser run?
    marks: list[Mark] = field(default_factory=list)
    raw_text_chars: int = 0        # sanity signal: did we get a text layer at all?

    def to_records(self) -> list[dict]:
        """Explode to tidy rows for a DataFrame / parquet."""
        rows = []
        for m in self.marks:
            rows.append(
                {
                    "quarter": self.quarter,
                    "broker": self.broker_id,
                    "report_date": self.report_date.isoformat(),
                    "kind": m.kind,
                    "vessel_class": m.vessel_class,
                    "age_anchor": m.age_anchor,
                    "metric": m.metric,
                    "value": m.value,
                    "unit": m.unit,
                    "note": m.note,
                    "parser": self.parser,
                    "source_pdf": self.source_pdf,
                    "source_post": self.source_post,
                }
            )
        return rows
