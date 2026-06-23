"""Persistence. Two layers:

  * per-(broker, quarter) JSON       -- human-auditable, one file per mark set
  * one tidy long-format parquet     -- the [Q]-keyed table you join against

The parquet is the artefact your factor pipeline consumes:
  columns = quarter, broker, report_date, kind, vessel_class, age_anchor,
            metric, value, unit, note, parser, source_pdf, source_post
"""
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

import pandas as pd

from . import config
from .models import MarketMarks


def save_marks(mm: MarketMarks) -> Path:
    folder = config.MARKS_STORE / mm.broker_id
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{mm.quarter}.json"
    payload = {
        "broker_id": mm.broker_id,
        "report_date": mm.report_date.isoformat(),
        "quarter": mm.quarter,
        "source_post": mm.source_post,
        "source_pdf": mm.source_pdf,
        "parser": mm.parser,
        "parser_ok": mm.parser_ok,
        "raw_text_chars": mm.raw_text_chars,
        "marks": [asdict(m) for m in mm.marks],
    }
    path.write_text(json.dumps(payload, indent=2))
    return path


def _iter_record_dicts():
    if not config.MARKS_STORE.exists():
        return
    for jf in config.MARKS_STORE.rglob("*.json"):
        doc = json.loads(jf.read_text())
        for m in doc["marks"]:
            yield {
                "quarter": doc["quarter"],
                "broker": doc["broker_id"],
                "report_date": doc["report_date"],
                "kind": m["kind"],
                "vessel_class": m["vessel_class"],
                "age_anchor": m.get("age_anchor"),
                "metric": m["metric"],
                "value": m["value"],
                "unit": m["unit"],
                "note": m.get("note"),
                "parser": doc["parser"],
                "source_pdf": doc.get("source_pdf"),
                "source_post": doc.get("source_post"),
            }


def build_panel(write: bool = True) -> pd.DataFrame:
    """Assemble all saved marks into one tidy DataFrame (and write parquet)."""
    df = pd.DataFrame(list(_iter_record_dicts()))
    if not df.empty:
        df = df.sort_values(["quarter", "broker", "kind", "vessel_class"]).reset_index(drop=True)
    if write and not df.empty:
        config.PANEL_PARQUET.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(config.PANEL_PARQUET, index=False)
    return df


def coverage_report(df: pd.DataFrame) -> pd.DataFrame:
    """Quick QA: count of marks by quarter x kind, so you can see holes before
    they bite the factor build."""
    if df.empty:
        return df
    return (
        df.groupby(["quarter", "kind"]).size()
        .unstack(fill_value=0).sort_index()
    )
