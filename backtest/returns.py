"""Forward returns + equal-weight crude market-neutralization.

DATA CAVEAT (declared, not hidden): the only price series on disk is the
Pareto weekly print column, which is a PRICE series, not a total-return
series. Crude-tanker dividends are large and uneven across names (DHT/NAT
~full payout, FRO variable), so these PRICE returns omit a materially
cross-sectional component. The pre-registered metric calls for *total*
return; supplying dividends (or adjusted close) is on the data-needs list.
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from .vintage_loader import Observation, obs_nearest


def forward_price_returns(
    obs: list[Observation],
    entry_panel: dict[str, Observation],
    next_cutoff: date,
    names: dict[str, str],
    max_gap_days: int = 21,
) -> dict[str, float]:
    """Realized ~1q-forward price return per name.

    Entry price = the as-of (signal-date) observation already in
    ``entry_panel`` (dated <= signal cutoff). Forward price = the observation
    nearest the next quarter-end (an outcome, legitimately after the signal).
    """
    out: dict[str, float] = {}
    for symbol, entry in entry_panel.items():
        fwd = obs_nearest(obs, names[symbol], next_cutoff, max_gap_days=max_gap_days)
        if fwd is None or fwd.price is None or entry.price in (None, 0):
            continue
        # Forward observation must post-date the signal observation.
        if fwd.obs_date <= entry.obs_date:
            continue
        out[symbol] = fwd.price / entry.price - 1.0
    return out


def market_neutralize(rets: dict[str, float]) -> dict[str, float]:
    """Subtract the equal-weight average return of the names present."""
    if not rets:
        return {}
    bench = sum(rets.values()) / len(rets)
    return {k: v - bench for k, v in rets.items()}
