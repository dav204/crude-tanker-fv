"""Static configuration: where to crawl, who the brokers are, how to behave.

Nothing here hits the network. Edit BROKERS to add a house, edit REQUEST_POLICY
to tune politeness.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


# --- filesystem layout ------------------------------------------------------
DATA_ROOT = Path("./data")
PDF_CACHE = DATA_ROOT / "pdfs"           # raw downloaded issues (content-addressed)
MARKS_STORE = DATA_ROOT / "marks"        # per-(broker, quarter) JSON
MANIFEST = DATA_ROOT / "manifest.jsonl"  # append-only log of everything crawled
PANEL_PARQUET = DATA_ROOT / "marks_panel.parquet"  # tidy long-format output
FACTOR_PARQUET = DATA_ROOT / "factor_marks.parquet"  # resolved -> factor schema


# --- politeness -------------------------------------------------------------
@dataclass(frozen=True)
class RequestPolicy:
    user_agent: str = (
        "shipping-harvester/0.1 (personal research; contact: dav204@gmail.com)"
    )
    min_interval_s: float = 2.0   # min delay between requests to the SAME host
    timeout_s: float = 30.0
    max_retries: int = 3
    backoff_base_s: float = 2.0
    respect_robots: bool = True   # check robots.txt before crawling a host


REQUEST_POLICY = RequestPolicy()


# --- sources ----------------------------------------------------------------
# Both aggregators run WordPress, so we prefer the WP REST API and fall back to
# HTML scraping. Slugs below were confirmed live; adjust if a site reorganises.

HSN_BASE = "https://www.hellenicshippingnews.com"
HSN_CATEGORY_SLUG = "weekly-shipbrokers-reports"

CAPITALLINK_BASE = "https://capitallinkshipping.com"
# Capital Link files reports under per-contributor categories:
#   /category/contributors/<slug>/
CAPITALLINK_CONTRIBUTOR_SLUGS = (
    "allied-shipbroking",
    "intermodal-shipbrokers",
    "banchero-costa",
    "charles-r-weber",
    "fearnleys-shipbroking",
)


# --- broker registry --------------------------------------------------------
@dataclass(frozen=True)
class Broker:
    broker_id: str
    display: str
    # regex matched (case-insensitive) against a post title to attribute it
    title_pattern: re.Pattern
    # which fields this house's weekly is worth scraping for (documentation +
    # lets you skip parsing PDFs that won't carry what you need)
    provides: tuple[str, ...]


def _p(rx: str) -> re.Pattern:
    return re.compile(rx, re.IGNORECASE)


# Ordered: first matching pattern wins, so keep specific ones above generic.
BROKERS: tuple[Broker, ...] = (
    Broker("allied", "Allied Shipbroking", _p(r"\ballied\b"),
           provides=("vessel_value", "period_tc", "demolition")),
    Broker("intermodal", "Intermodal Shipbrokers", _p(r"\bintermodal\b"),
           provides=("vessel_value", "period_tc", "spot_tce", "demolition")),
    Broker("xclusiv", "Xclusiv Shipbrokers", _p(r"\bxclusiv\b"),
           provides=("vessel_value", "period_tc", "spot_tce", "demolition")),
    Broker("weber", "Charles R. Weber", _p(r"\bweber\b"),
           provides=("spot_tce", "period_tc")),
    Broker("banchero", "Banchero Costa", _p(r"banchero|bancosta"),
           provides=("vessel_value", "period_tc", "spot_tce")),
    Broker("braemar", "Braemar", _p(r"\bbraemar\b"),
           provides=("spot_tce",)),
    Broker("fearnleys", "Fearnleys", _p(r"\bfearnle"),
           provides=("spot_tce", "period_tc")),  # incl. gas/LNG rates
    Broker("gms", "GMS", _p(r"\bgms\b"),
           provides=("demolition",)),
    Broker("advanced", "Advanced Shipping & Trading", _p(r"advanced shipping"),
           provides=("spot_tce", "period_tc")),
)

_BY_ID = {b.broker_id: b for b in BROKERS}


def identify_broker(title: str) -> Broker | None:
    """Return the Broker whose pattern matches a post title, else None."""
    for b in BROKERS:
        if b.title_pattern.search(title):
            return b
    return None


def get_broker(broker_id: str) -> Broker | None:
    return _BY_ID.get(broker_id)
