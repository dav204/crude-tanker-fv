"""Quarter keying. Your marks are '[Q], dated <= quarter-end', so the core
operation is: for a target quarter, pick each broker's latest issue dated on or
before that quarter-end (and flag it if it's stale).
"""
from __future__ import annotations

import calendar
import datetime as dt
import re
from typing import Iterable

from .models import ReportRef

_Q_RE = re.compile(r"^(\d{4})Q([1-4])$")


def quarter_of(d: dt.date) -> str:
    """date -> '2026Q2'."""
    return f"{d.year}Q{(d.month - 1) // 3 + 1}"


def parse_quarter(label: str) -> tuple[int, int]:
    """'2026Q2' -> (2026, 2)."""
    m = _Q_RE.match(label.strip().upper())
    if not m:
        raise ValueError(f"bad quarter label: {label!r} (expected e.g. 2026Q2)")
    return int(m.group(1)), int(m.group(2))


def quarter_end(label: str) -> dt.date:
    """'2026Q2' -> date(2026, 6, 30)."""
    year, q = parse_quarter(label)
    end_month = q * 3
    last_day = calendar.monthrange(year, end_month)[1]
    return dt.date(year, end_month, last_day)


def quarter_start(label: str) -> dt.date:
    year, q = parse_quarter(label)
    return dt.date(year, (q - 1) * 3 + 1, 1)


def quarter_range(since: str, until: str) -> list[str]:
    """Inclusive list of quarter labels from `since` to `until`."""
    y0, q0 = parse_quarter(since)
    y1, q1 = parse_quarter(until)
    start, end = y0 * 4 + (q0 - 1), y1 * 4 + (q1 - 1)
    if end < start:
        raise ValueError(f"{until} is before {since}")
    out = []
    for n in range(start, end + 1):
        out.append(f"{n // 4}Q{n % 4 + 1}")
    return out


def select_for_quarter(
    refs: Iterable[ReportRef],
    label: str,
    stale_after_days: int = 14,
) -> dict[str, tuple[ReportRef, bool]]:
    """For one quarter, choose each broker's mark.

    Returns {broker_id: (chosen_ref, is_stale)}.

    Rule: latest issue with published date <= quarter_end. `is_stale` is True
    when the chosen issue is more than `stale_after_days` before quarter-end
    (i.e. the broker had no fresh issue near the cutoff and we reached back).
    """
    qend = quarter_end(label)
    best: dict[str, ReportRef] = {}
    for r in refs:
        if r.published > qend:
            continue
        cur = best.get(r.broker_id)
        if cur is None or r.published > cur.published:
            best[r.broker_id] = r

    out: dict[str, tuple[ReportRef, bool]] = {}
    for bid, r in best.items():
        is_stale = (qend - r.published).days > stale_after_days
        out[bid] = (r, is_stale)
    return out
