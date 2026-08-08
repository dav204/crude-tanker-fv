"""§18.5a mean-reversion gate (Thread 3) + §18.5b orderbook cross-check (Thread 5).

Both gates are DATA-GATED (no Baltic $/day series, no orderbook ratios in-repo) —
these tests exercise the machinery on SYNTHETIC inputs and confirm the real,
data-absent state returns 'pending' (registered-pending), never a crash or proxy.
"""

from __future__ import annotations

import math

from crude_tanker_fv.loaders import INPUTS_DIR
from crude_tanker_fv.normal_rates import (
    mean_reversion_gate,
    mean_reversion_gate_table,
    orderbook_crosscheck,
    orderbook_crosscheck_table,
    winsorize,
)

from conftest import BOOK_QUARTER as QUARTER  # follows the book across quarter rolls


# --- §18.5a mean-reversion gate -------------------------------------------- #

def test_mean_reversion_gate_pass_on_mean_reverting_series():
    """A series oscillating around its anchor with a half-period = the 4q horizon
    reverts perfectly: ratio>1 ⇒ falls, ratio<1 ⇒ rises ⇒ ~100% sign-consistency."""
    series = [100.0 + 35.0 * math.sin(t * math.pi / 4) for t in range(28)]  # period 8q
    v = mean_reversion_gate("Cape", series)
    assert v.status == "pass"
    assert v.hit_rate >= 0.70 and v.n_obs >= 12


def test_mean_reversion_gate_reject_on_trend():
    """A monotonic trend does NOT mean-revert: above-anchor quarters predict a fall
    but the series keeps rising ⇒ sign-consistency ~50% ⇒ reject."""
    series = [100.0 + 4.0 * t for t in range(28)]
    v = mean_reversion_gate("VLCC", series)
    assert v.status == "reject"
    assert v.hit_rate < 0.70


def test_mean_reversion_gate_insufficient_under_12_obs():
    series = [100.0, 110.0, 90.0, 105.0, 95.0, 100.0, 108.0, 92.0, 101.0, 99.0]  # 10 → 6 obs
    v = mean_reversion_gate("MR", series)
    assert v.status == "insufficient" and (v.n_obs or 0) < 12


def test_mean_reversion_gate_table_pending_when_no_series():
    """Data absent (no baltic_tce_series.yaml in INPUTS_DIR) ⇒ every class pending."""
    table = mean_reversion_gate_table(QUARTER, ["VLCC", "Cape", "Pana"], inputs_dir=INPUTS_DIR)
    assert all(v.status == "pending" for v in table.values())


def test_winsorize_clamps_tails():
    vals = [float(i) for i in range(1, 101)]     # 1..100
    w = winsorize(vals)
    assert min(w) > 1.0 and max(w) < 100.0       # both 5/95 tails pulled in
    assert min(w) == 5.0 and max(w) == 95.0      # the 5th / 95th percentiles


# --- §18.5b orderbook cross-check ------------------------------------------ #

def test_orderbook_coincide_under_ordered_thin_book():
    # historical 10% below parity (under-ordered) AND orderbook 6% < neutral 10% (thin).
    v = orderbook_crosscheck("Cape", divergence_pct=-0.10, orderbook_ratio=0.06, neutral_ratio=0.10)
    assert v.status == "coincide" and v.divergence_signal == -1 and v.orderbook_signal == -1


def test_orderbook_contradict_flags_parity_input():
    # historical below parity (under-ordered claim) BUT a THICK book ⇒ contradiction.
    v = orderbook_crosscheck("VLCC", divergence_pct=-0.10, orderbook_ratio=0.15, neutral_ratio=0.10)
    assert v.status == "contradict" and v.divergence_signal == -1 and v.orderbook_signal == 1
    assert "parity INPUT" in v.note


def test_orderbook_balanced_coincide():
    v = orderbook_crosscheck("Aframax", divergence_pct=0.0, orderbook_ratio=0.10, neutral_ratio=0.10)
    assert v.status == "coincide" and v.divergence_signal == 0 and v.orderbook_signal == 0


def test_orderbook_pending_when_inputs_missing():
    assert orderbook_crosscheck("X", None, 0.10, 0.10).status == "pending"
    assert orderbook_crosscheck("X", -0.1, None, 0.10).status == "pending"
    assert orderbook_crosscheck("X", -0.1, 0.06, None).status == "pending"


def test_orderbook_crosscheck_table_pending_when_no_file():
    """Data absent (no orderbook_ratios.yaml) ⇒ pending, even though parity computes."""
    table = orderbook_crosscheck_table(QUARTER, ["Cape"], inputs_dir=INPUTS_DIR)
    assert table["Cape"].status == "pending"
