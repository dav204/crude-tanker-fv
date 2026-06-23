"""Format-version dispatch.

Broker report layouts drift over time (Weber's 2019 'Spot Market' table is a
different beast from its 2024 two-column 'TANKER ROUTES' layout). A parser tuned
to the current format will mis-read or silently fail on an older issue. So each
broker maps to one or more FormatVersions, and an issue is routed by:

  1. a STRUCTURAL PROBE on the PDF text -- strongest, looks at actual content;
  2. then the issue date (since/until) -- fallback / tie-break;
  3. else the newest version, flagged low-confidence.

Crucially, if every version is probe-guarded and none match, we DON'T guess --
we fall back to the generic recorder, so a deep backfill never silently
mis-parses an unrecognised layout (it shows up as parser='generic:...' instead).

Single-format brokers (Allied, Intermodal, Xclusiv, GMS) register one open-ended
version, so their behaviour is unchanged.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Callable

from ..models import MarketMarks, ReportRef
from . import base
from .base import BrokerParser, GenericParser
from .allied import AlliedParser
from .intermodal import IntermodalParser
from .xclusiv import XclusivParser
from .weber import WeberParser
from .weber_2019 import WeberParser2019
from .gms import GmsParser


@dataclass(frozen=True)
class FormatVersion:
    version: str                       # provenance label, e.g. "weber_2024"
    parser: BrokerParser
    since: date | None = None          # effective from (inclusive)
    until: date | None = None          # effective until (exclusive)
    probe: Callable[[str], bool] | None = None   # structural test on PDF text

    def covers(self, d: date) -> bool:
        if self.since and d < self.since:
            return False
        if self.until and d >= self.until:
            return False
        return True


# Registry. Cutover dates are approximate -- the probe is authoritative; dates
# only matter when text can't be read or probes are absent.
_VERSIONS: dict[str, list[FormatVersion]] = {
    "allied": [FormatVersion("allied", AlliedParser())],
    "intermodal": [FormatVersion("intermodal", IntermodalParser())],
    "xclusiv": [FormatVersion("xclusiv", XclusivParser())],
    "gms": [FormatVersion("gms", GmsParser())],
    "weber": [
        FormatVersion(
            "weber_2024", WeberParser(),
            since=date(2023, 1, 1),
            probe=lambda t: "TANKER ROUTES" in t,
        ),
        FormatVersion(
            "weber_2017", WeberParser2019(),
            since=date(2015, 1, 1), until=date(2023, 1, 1),
            probe=lambda t: "TANKER ROUTES" not in t and "Average Earnings" in t,
        ),
    ],
}

_GENERIC = GenericParser()


def _newest(versions: list[FormatVersion]) -> FormatVersion:
    return max(versions, key=lambda v: v.since or date.min)


def resolve_parser(broker_id: str, published: date, text: str):
    """Return (parser, version_label, confident) for an issue."""
    versions = _VERSIONS.get(broker_id)
    if not versions:
        return _GENERIC, "generic", False

    # 1) structural probe -- strongest signal
    if text:
        hits = [v for v in versions if v.probe and v.probe(text)]
        if hits:
            covered = [v for v in hits if v.covers(published)]
            v = _newest(covered) if covered else _newest(hits)
            return v.parser, v.version, True
        # every version is probe-guarded and none matched -> unrecognised layout
        if all(v.probe for v in versions):
            return _GENERIC, "generic:unrecognized-format", False

    # 2) date-based (probe-less versions, or all if none carry probes)
    cands = [v for v in versions if v.probe is None] or versions
    covered = [v for v in cands if v.covers(published)]
    if covered:
        v = _newest(covered)
        return v.parser, v.version, True

    # 3) best-guess: newest, low confidence
    v = _newest(cands)
    return v.parser, v.version, False


def dispatch_parse(broker_id: str, pdf_path, ref: ReportRef) -> tuple[MarketMarks, bool]:
    """Resolve the right format version (probe + date) and parse. Returns
    (marks, confident); marks.parser carries the chosen version label."""
    try:
        text = base.extract_text(pdf_path)
    except Exception:
        text = ""
    parser, version, confident = resolve_parser(broker_id, ref.published, text)
    mm = parser.parse(pdf_path, ref)
    mm.parser = version
    return mm, confident


def get_parser(broker_id: str) -> BrokerParser:
    """Newest parser for a broker (no dispatch). Back-compat convenience; the
    harvester uses dispatch_parse for date/probe-aware routing."""
    versions = _VERSIONS.get(broker_id)
    return _newest(versions).parser if versions else _GENERIC


def implemented() -> set[str]:
    return set(_VERSIONS)


def versions_for(broker_id: str) -> list[str]:
    return [v.version for v in _VERSIONS.get(broker_id, [])]
