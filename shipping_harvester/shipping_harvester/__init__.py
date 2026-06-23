"""shipping_harvester -- pull broker weekly PDFs into [Q]-keyed market marks.

    from shipping_harvester.net import PoliteSession
    from shipping_harvester import crawl, download, store
    from shipping_harvester.parse import get_parser

Or just use the CLI:  python -m shipping_harvester.cli run --since 2024Q1 --until 2026Q2
"""
from . import config, crawl, download, factor, quarters, store  # noqa: F401
from .models import Mark, MarketMarks, ReportRef  # noqa: F401
from .net import PoliteSession  # noqa: F401
from .parse import get_parser  # noqa: F401

__version__ = "0.1.0"
