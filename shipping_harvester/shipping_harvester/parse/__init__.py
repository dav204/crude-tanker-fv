"""Parser package. Format-version dispatch lives in `dispatch`; this module
re-exports the public surface so existing imports keep working.

  get_parser(broker_id)                 -> newest parser (no dispatch)
  resolve_parser(broker_id, date, text) -> (parser, version, confident)
  dispatch_parse(broker_id, pdf, ref)   -> (MarketMarks, confident)  [date+probe]
  implemented()                         -> set of broker_ids with a parser
"""
from .base import BrokerParser, GenericParser
from .allied import AlliedParser
from .intermodal import IntermodalParser
from .xclusiv import XclusivParser
from .weber import WeberParser
from .weber_2019 import WeberParser2019
from .gms import GmsParser
from .dispatch import (
    FormatVersion,
    get_parser,
    resolve_parser,
    dispatch_parse,
    implemented,
    versions_for,
)

__all__ = [
    "BrokerParser", "GenericParser",
    "AlliedParser", "IntermodalParser", "XclusivParser",
    "WeberParser", "WeberParser2019", "GmsParser",
    "FormatVersion", "get_parser", "resolve_parser", "dispatch_parse",
    "implemented", "versions_for",
]
