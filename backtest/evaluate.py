"""Evaluation: Spearman rank IC, mean-IC t-stat, and a cheap-minus-rich
spread readout. Stdlib + the tiny rank helper below; no scipy needed.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .loaders import QuarterCross


def _avg_ranks(xs: list[float]) -> list[float]:
    """Ranks with ties averaged (1-based), matching Spearman convention."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0           # average of 1-based positions
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def _pearson(a: list[float], b: list[float]) -> float | None:
    n = len(a)
    if n < 2:
        return None
    ma, mb = sum(a) / n, sum(b) / n
    va = sum((x - ma) ** 2 for x in a)
    vb = sum((x - mb) ** 2 for x in b)
    if va == 0 or vb == 0:                   # no cross-sectional dispersion -> undefined
        return None
    cov = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
    return cov / math.sqrt(va * vb)


def spearman(x: list[float], y: list[float]) -> float | None:
    if len(x) != len(y) or len(x) < 2:
        return None
    return _pearson(_avg_ranks(x), _avg_ranks(y))


@dataclass
class QuarterIC:
    asof: str
    n: int
    ic: float


@dataclass
class ICResult:
    quarter_ics: list[QuarterIC]
    mean_ic: float | None
    t_stat: float | None
    n_quarters: int
    min_names: int


def ic_series(crosses: list[QuarterCross], min_names: int = 3) -> ICResult:
    """Per-quarter Spearman IC between cheapness (-P/NAV) and relative return.

    Positive IC = cheap (low P/NAV) predicts outperformance.
    """
    qics: list[QuarterIC] = []
    for c in crosses:
        names = sorted(c.pnav)
        if len(names) < min_names:
            continue
        cheap = [-c.pnav[n] for n in names]          # low P/NAV -> high cheapness
        rel = [c.rel_ret[n] for n in names]
        ic = spearman(cheap, rel)
        if ic is None:
            continue
        qics.append(QuarterIC(asof=c.asof.isoformat(), n=len(names), ic=ic))
    mean_ic = t = None
    if qics:
        ics = [q.ic for q in qics]
        nq = len(ics)
        mean_ic = sum(ics) / nq
        if nq >= 2:
            sd = math.sqrt(sum((x - mean_ic) ** 2 for x in ics) / (nq - 1))
            t = mean_ic / (sd / math.sqrt(nq)) if sd > 0 else None
    return ICResult(quarter_ics=qics, mean_ic=mean_ic, t_stat=t,
                    n_quarters=len(qics), min_names=min_names)


@dataclass
class SpreadResult:
    mean_spread: float | None
    t_stat: float | None
    n_quarters: int
    per_quarter: list[tuple[str, float]]


def cheap_minus_rich(crosses: list[QuarterCross], min_names: int = 3) -> SpreadResult:
    """EXPLORATORY: long the below-median-P/NAV names, short the rest, equal
    weight; quarterly spread of relative returns. Portfolio construction is a
    researcher degree of freedom — read as illustrative, not the verdict."""
    rows: list[tuple[str, float]] = []
    for c in crosses:
        names = sorted(c.pnav)
        if len(names) < min_names:
            continue
        med = sorted(c.pnav[n] for n in names)[len(names) // 2]
        cheap = [n for n in names if c.pnav[n] < med]
        rich = [n for n in names if c.pnav[n] > med]
        if not cheap or not rich:
            continue
        long_r = sum(c.rel_ret[n] for n in cheap) / len(cheap)
        short_r = sum(c.rel_ret[n] for n in rich) / len(rich)
        rows.append((c.asof.isoformat(), long_r - short_r))
    mean = t = None
    if rows:
        vals = [v for _, v in rows]
        nq = len(vals)
        mean = sum(vals) / nq
        if nq >= 2:
            sd = math.sqrt(sum((x - mean) ** 2 for x in vals) / (nq - 1))
            t = mean / (sd / math.sqrt(nq)) if sd > 0 else None
    return SpreadResult(mean_spread=mean, t_stat=t, n_quarters=len(rows), per_quarter=rows)
