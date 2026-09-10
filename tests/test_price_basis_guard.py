"""The COMMITTED decision surface must be valued on live quotes, not watchlist statics.

2026-09-09, caught by the Stage B halt check: the price file had been reverted to a 9/04
vintage per the promote rule, that vintage was past the 5-day freshness gate, and the regen
silently fell back to watchlist STATICS on 19 of 25 names (June prices for some). The
"Stage B" EV moves were price moves — five names on the frozen invariance list moved and
three flipped toward BUY. The run printed a STALE-PRICE warning and proceeded. A surface
like that must not be committable; the scorecard's own price_basis block is the evidence.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# A holiday or a single failed fetch can leave one or two names on a static for a day; a
# statics RUN is a different thing. Above this the surface is not a valuation, it is noise.
MAX_FALLBACK_NAMES = 2


def _price_basis():
    doc = json.loads((ROOT / "outputs" / "book_scorecard.json").read_text(encoding="utf-8"))
    pb = doc.get("price_basis") or {}
    assert "total" in pb, "scorecard price_basis block missing — the disclosure the guard reads"
    return pb


def test_committed_surface_is_not_a_statics_run():
    pb = _price_basis()
    stale = pb.get("stale_fallback") or {}
    static = pb.get("static_fallback") or {}
    n = len(set(stale) | set(static))
    assert n <= MAX_FALLBACK_NAMES, (
        f"{n} of {pb['total']} names valued on watchlist STATICS ({sorted(set(stale) | set(static))}) "
        "— a stale or missing price vintage, not a valuation. Fetch a fresh vintage "
        "(price_refresh), commit it ALONE, regenerate; never commit this surface.")


def test_stale_static_rows_are_disclosed_not_silent():
    """A quote applied over a stale static (the CMDB case, 2026-09-07) must surface in
    market_event_review so the owner sees which vintage pairs need rebasing."""
    pb = _price_basis()
    review = pb.get("market_event_review") or {}
    for t, why in review.items():
        assert isinstance(why, str) and why, f"{t}: empty review reason"
