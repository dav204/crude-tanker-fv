"""Shared test constants.

BOOK_QUARTER — the committed book quarter, read from the tracked scorecard.
Tests that value the LIVE tree must follow the book across quarter rolls: a
hardcoded quarter constant reds at every transition (2026-08-08, first roll —
the pair guard fired at collection in test_newbuild_convention because TNK's
manifest had advanced past the constant). Lagging names resolve to the same
sheets either way (loader newest-at-or-before), so per-name value pins are
unaffected by following the book.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_QUARTER = json.loads(
    (ROOT / "outputs" / "book_scorecard.json").read_text())["quarter"]
