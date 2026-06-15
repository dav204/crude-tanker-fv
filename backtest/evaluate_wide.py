"""Sector-neutral pooled IC for the wide shipping panel (Amendment 1).

Per quarter: within each (sector, quarter) cell of >=2 names, average-rank the
names by cheapness (-P/NAV) and by forward total return, center each rank by
the cell mean (so cells compose), pool across sectors, and take the Pearson
correlation of the pooled centered ranks. That pooled correlation is the
quarter's sector-neutral IC. Positive = cheap predicts peer-relative
outperformance.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .evaluate import _avg_ranks, _pearson, spearman


@dataclass
class WideQuarter:
    asof: str
    n_pooled: int
    sectors: int
    ic_sector_neutral: float | None
    ic_raw_panel: float | None       # whole-panel, not sector-neutral
    ew_panel_ret: float


def _centered_ranks(vals: list[float]) -> list[float]:
    r = _avg_ranks(vals)
    m = sum(r) / len(r)
    return [x - m for x in r]


def wide_quarter_ic(names_data: dict[str, tuple[float, float, str]]) -> WideQuarter | None:
    """names_data: name -> (pnav, fwd_ret, sector). Returns one quarter's ICs."""
    if not names_data:
        return None
    rets = [v[1] for v in names_data.values()]
    ew = sum(rets) / len(rets)

    # --- sector-neutral pooled IC ---
    by_sector: dict[str, list[str]] = {}
    for nm, (_, _, sec) in names_data.items():
        by_sector.setdefault(sec, []).append(nm)
    pooled_cheap: list[float] = []
    pooled_ret: list[float] = []
    sectors_used = 0
    for sec, members in by_sector.items():
        if len(members) < 2:
            continue                       # singletons carry no within-sector info
        sectors_used += 1
        cheap = _centered_ranks([-names_data[m][0] for m in members])
        rret = _centered_ranks([names_data[m][1] for m in members])
        pooled_cheap.extend(cheap)
        pooled_ret.extend(rret)
    ic_sn = _pearson(pooled_cheap, pooled_ret) if len(pooled_cheap) >= 2 else None

    # --- raw whole-panel IC (cross-sector confounded) ---
    allnames = sorted(names_data)
    ic_raw = spearman([-names_data[n][0] for n in allnames],
                      [names_data[n][1] - ew for n in allnames])

    return WideQuarter(asof="", n_pooled=len(pooled_cheap), sectors=sectors_used,
                       ic_sector_neutral=ic_sn, ic_raw_panel=ic_raw, ew_panel_ret=ew)


def mean_t(xs: list[float]) -> tuple[float | None, float | None]:
    xs = [x for x in xs if x is not None]
    if not xs:
        return None, None
    n = len(xs)
    m = sum(xs) / n
    if n < 2:
        return m, None
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    return m, (m / (sd / math.sqrt(n)) if sd > 0 else None)
