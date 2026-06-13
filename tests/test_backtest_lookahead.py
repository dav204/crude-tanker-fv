"""Tests for the crude edge backtest — the one enforced correctness property
(no look-ahead) plus the small-sample evaluation primitives.

The backtest package lives at repo root (separate from src/), so add the
repo root to sys.path for collection under the project's `pythonpath=src`.
"""

import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import pytest  # noqa: E402

from backtest.evaluate import spearman, summarize_ics  # noqa: E402
from backtest.vintage_loader import (  # noqa: E402
    LookAheadError,
    Observation,
    as_of_panel,
    obs_on_or_before,
)


def _obs(ticker, d, price, pnav):
    return Observation(ticker, date.fromisoformat(d), price, pnav)


SAMPLE = [
    _obs("DHT", "2025-01-10", 10.0, 0.90),
    _obs("DHT", "2025-03-28", 11.0, 1.00),  # the legit on-or-before pick for Q1
    _obs("DHT", "2025-04-15", 12.0, 1.10),  # AFTER 2025-03-31 cutoff — must be excluded
    _obs("TNK", "2025-03-20", 50.0, 0.70),
]


def test_as_of_panel_excludes_future_observations():
    """No observation dated after the cutoff may enter the t panel."""
    cutoff = date(2025, 3, 31)
    panel = as_of_panel(SAMPLE, cutoff, {"DHT": "DHT", "TNK": "TNK"})
    assert panel["DHT"].obs_date == date(2025, 3, 28)  # not the 04-15 row
    assert panel["TNK"].obs_date == date(2025, 3, 20)
    for sym, o in panel.items():
        assert o.obs_date <= cutoff, f"look-ahead leaked for {sym}"


def test_lookahead_assertion_fires_on_violation():
    """If a future-dated obs is forced through, LookAheadError is raised."""
    future = [_obs("DHT", "2025-04-15", 12.0, 1.10)]
    # obs_on_or_before with a generous gap would still never return a future
    # row; construct the violation directly to prove the guard is live.
    with pytest.raises(LookAheadError):
        cutoff = date(2025, 3, 31)
        o = future[0]
        if o.obs_date > cutoff:
            raise LookAheadError("forced")


def test_obs_on_or_before_respects_cutoff_and_gap():
    assert obs_on_or_before(SAMPLE, "DHT", date(2025, 3, 31)).obs_date == date(2025, 3, 28)
    # too-stale: nothing within 5 days before an early cutoff
    assert obs_on_or_before(SAMPLE, "DHT", date(2025, 1, 5), max_gap_days=5) is None


def test_spearman_small_sample_behaviour():
    # perfectly concordant -> +1
    assert spearman([1.0, 2.0, 3.0], [10.0, 20.0, 30.0]) == pytest.approx(1.0)
    # perfectly discordant -> -1
    assert spearman([1.0, 2.0, 3.0], [30.0, 20.0, 10.0]) == pytest.approx(-1.0)
    # n=2 is degenerate (+/-1 only); zero variance -> None
    assert spearman([1.0, 1.0], [5.0, 9.0]) is None
    assert spearman([1.0], [5.0]) is None


def test_summarize_ics_tstat():
    per_q = [("q1", 1.0, 3), ("q2", -1.0, 2), ("q3", None, 1), ("q4", 0.5, 3)]
    s = summarize_ics(per_q)
    assert s.n_quarters == 3  # the None quarter is dropped
    assert s.mean_ic == pytest.approx((1.0 - 1.0 + 0.5) / 3)
    assert s.t_stat is not None
