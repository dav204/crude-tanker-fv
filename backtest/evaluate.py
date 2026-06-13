"""Evaluation primitives for the crude edge backtest (pure stdlib).

Spearman rank IC, mean-IC t-stat, and a Newey-West SE — implemented without
numpy/scipy so the backtest runs in a bare container.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

# Two-sided t critical values at alpha = 0.05, df = 1..12. Used to state the
# bar honestly given the tiny sample (no scipy available for exact p-values).
T_CRIT_05 = {
    1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447,
    7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179,
}


def _ranks(xs: list[float]) -> list[float]:
    """Average ranks (ties shared), 1-based."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0  # average of the 1-based positions
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def _pearson(xs: list[float], ys: list[float]) -> Optional[float]:
    n = len(xs)
    if n < 2:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    if sxx <= 0 or syy <= 0:
        return None  # zero variance -> undefined
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / math.sqrt(sxx * syy)


def spearman(xs: list[float], ys: list[float]) -> Optional[float]:
    """Spearman rank correlation. None if n<2 or a side has zero variance.

    NOTE on small n (declared in PRE_REGISTRATION): n=2 -> result in {-1,+1};
    n=3 -> result in {-1,-0.5,+0.5,+1}. Degenerate; interpret accordingly.
    """
    if len(xs) != len(ys) or len(xs) < 2:
        return None
    return _pearson(_ranks(xs), _ranks(ys))


@dataclass
class ICSummary:
    n_quarters: int
    mean_ic: Optional[float]
    std_ic: Optional[float]
    t_stat: Optional[float]
    t_crit_05: Optional[float]
    nw_se: Optional[float]
    nw_t: Optional[float]
    per_quarter: list  # list[(label, ic, cross_section_n)]

    def significant_05(self) -> Optional[bool]:
        if self.t_stat is None or self.t_crit_05 is None:
            return None
        return abs(self.t_stat) >= self.t_crit_05


def _newey_west_se_of_mean(series: list[float], lag: int) -> Optional[float]:
    """Newey-West SE of the sample mean (lag-truncated, Bartlett weights)."""
    n = len(series)
    if n < 2:
        return None
    mu = sum(series) / n
    dev = [x - mu for x in series]
    gamma0 = sum(d * d for d in dev) / n
    var = gamma0
    for l in range(1, min(lag, n - 1) + 1):
        w = 1.0 - l / (lag + 1.0)
        gl = sum(dev[t] * dev[t - l] for t in range(l, n)) / n
        var += 2.0 * w * gl
    if var <= 0:
        return None
    return math.sqrt(var / n)


def summarize_ics(per_quarter: list, nw_lag: int = 1) -> ICSummary:
    """Aggregate per-quarter ICs into the pre-registered primary statistic.

    ``per_quarter`` is a list of (label, ic_or_None, cross_section_n). ICs
    that are None (cross-section too thin / zero variance) are dropped from
    the mean and the count.
    """
    ics = [ic for (_lbl, ic, _n) in per_quarter if ic is not None]
    n = len(ics)
    if n == 0:
        return ICSummary(0, None, None, None, None, None, None, per_quarter)
    mean_ic = sum(ics) / n
    if n < 2:
        return ICSummary(n, mean_ic, None, None, None, None, None, per_quarter)
    var = sum((x - mean_ic) ** 2 for x in ics) / (n - 1)
    std_ic = math.sqrt(var)
    t_stat = mean_ic / (std_ic / math.sqrt(n)) if std_ic > 0 else None
    df = n - 1
    t_crit = T_CRIT_05.get(df)
    nw_se = _newey_west_se_of_mean(ics, nw_lag)
    nw_t = (mean_ic / nw_se) if (nw_se and nw_se > 0) else None
    return ICSummary(n, mean_ic, std_ic, t_stat, t_crit, nw_se, nw_t, per_quarter)
