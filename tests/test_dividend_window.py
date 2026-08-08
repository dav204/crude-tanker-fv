"""§12 dividend-window diagnostic gate tests (METHODOLOGY §12.5-§12.7).

The diagnostic replaces §12's prior one-way bullish override (audit finding E-3)
with a falsifiable per-name classification. These pins guard the trigger gate and
the NAT resolution.
"""

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
from crude_tanker_fv.dividend_window import evaluate, q_star
from crude_tanker_fv.loaders import load_watchlist


def test_trigger_gate_nat_in_dht_out():
    """§12.5 gate fires for NAT (single-class, 100% payout, peak, large market
    premium over the tool floor) but NOT for DHT (premium ~1.27× < the 1.5× gate)."""
    wl = load_watchlist()
    nat = evaluate("NAT", "2026-Q1", wl["NAT"])
    dht = evaluate("DHT", BOOK_QUARTER, wl["DHT"])
    assert nat.gated is True
    assert dht.gated is False
    assert nat.premium_x > 1.5 > dht.premium_x


def test_nat_trim_stands_not_undervaluation():
    """§12.6: NAT's spot-derived DPS do not bridge the price−NAV premium within the
    strip (Q* = None), so the window is NOT rate-supported → the TRIM stands. The §12
    'treat FV as a floor, do not act on the TRIM' override no longer fires for NAT —
    its TRIM is a computed value-trap call (the resolution of audit E-3)."""
    wl = load_watchlist()
    nat = evaluate("NAT", "2026-Q1", wl["NAT"])
    assert nat.q_star is None
    assert nat.classification == "TRIM-stands"


def test_q_star_arithmetic():
    assert q_star([1.0, 1.0, 1.0, 1.0], 0.0, 3.0) == 3.0   # cum 1,2,3 → bridges at q3
    assert q_star([0.1] * 8, 0.0, 5.0) is None             # never bridges within the strip
    assert q_star([1.0], 0.0, 0.0) == 0.0                  # non-positive gap → 0
