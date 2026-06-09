"""Parse Daily Shipping Index posts from Rocket.Chat into structured rows.

Handles two formats observed in the Value Investor's Edge channel:

John.Pace (current source)::

    *Daily Shipping Indexes*
    BCTI: 1,379 (+3) (6/8)
    BDTI: 2,099 (-11) (6/8)
    ...

Chris.Palun (historical source, mostly Jan-Apr 2026)::

    Shipping Index 4/24:

    - BCTI: 2197 (-4)
    - BDTI: 2812 (-25)
    ...

Plus standalone Capesize index posts from Chris::

    Capesize index: 35,333 (-301)

The two main-Baltic formats yield ``parse_baltic_post`` → dict with date +
the five Baltic series. The Capesize standalone yields ``parse_capesize_post``
→ int. The caller combines them by date.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from typing import Optional

INDEX_NAMES = ("BCTI", "BDTI", "BLPG", "BDI", "FBX")

_HEADER_RE = re.compile(
    r"\b(daily\s+shipping\s+indexes|shipping\s+index)\s*(\d{1,2}/\d{1,2})?",
    re.IGNORECASE,
)

# Single-line value: "BCTI: 1,379 (+3) (6/8)", "- BCTI: 2197 (-4)",
# "BCTI: 1,376 ▼ (6/5)". Applied with re.match() against each line.
_LINE_RE = re.compile(
    r"\s*[-*]?\s*([A-Z]{3,4})\s*:\s*([\d,]+)"
    r"(?:[ \t]*(?:\(([+\-]?[\d,]+)\)|[▲▼▲▼]))?"
    r"(?:[ \t]*\((\d{1,2}/\d{1,2})\))?"
)

_CAPESIZE_RE = re.compile(
    r"capesize\s+index\s*:\s*([\d,]+)"
    r"(?:[ \t]*\(\s*([+\-]?[\d,]+)\s*\))?",
    re.IGNORECASE,
)


def _to_int(s: Optional[str]) -> Optional[int]:
    if s is None:
        return None
    return int(s.replace(",", "").lstrip("+"))


def _infer_year(month: int, day: int, ref: datetime) -> int:
    """Pick the year for an (M/D) token given the message timestamp.

    Posts are same-day or next-morning, so the data date should not be
    after the message date. If it would be, roll back a year (Dec/Jan wrap).
    """
    candidate = date(ref.year, month, day)
    if candidate > ref.date():
        return ref.year - 1
    return ref.year


def _resolve_date(token: Optional[str], msg_ts: datetime) -> date:
    if token:
        m, d = (int(x) for x in token.split("/"))
        return date(_infer_year(m, d, msg_ts), m, d)
    return msg_ts.date()


def parse_baltic_post(text: str, msg_ts: datetime) -> Optional[dict]:
    """Parse a Daily Shipping Indexes post into a dict.

    Returns ``{"date": "YYYY-MM-DD", "BCTI": int|None, ...}`` for all five
    series, or None if this message isn't a recognised Baltic post.
    """
    if not text:
        return None

    header = _HEADER_RE.search(text)
    if not header:
        return None

    values: dict[str, Optional[int]] = {n: None for n in INDEX_NAMES}
    inline_dates: list[str] = []
    for line in text.splitlines():
        m = _LINE_RE.match(line)
        if not m:
            continue
        name = m.group(1)
        if name not in INDEX_NAMES:
            continue
        values[name] = _to_int(m.group(2))
        if m.group(4):
            inline_dates.append(m.group(4))

    if not any(v is not None for v in values.values()):
        return None  # header matched but no recognised index lines

    raw_date = header.group(2) or (inline_dates[0] if inline_dates else None)
    return {"date": _resolve_date(raw_date, msg_ts).isoformat(), **values}


def parse_capesize_post(text: str) -> Optional[int]:
    """Return the Capesize index value if this text contains one, else None."""
    if not text:
        return None
    m = _CAPESIZE_RE.search(text)
    if not m:
        return None
    return _to_int(m.group(1))
