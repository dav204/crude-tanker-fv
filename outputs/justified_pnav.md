# Justified P/NAV diagnostic

A **coverage-independent** fair-multiple benchmark (METHODOLOGY §17). The broker-NAV sweep (§9.9) and consensus-EPS cross-check (§9.11) lean on Pareto coverage; this asks a question answerable from fundamentals alone — **does the fleet earn its cost of capital on its own marked NAV (net asset value)?** — so the APPROX / no-Pareto names (SB, CMDB, GSL, MPCC, CCEC, NAT, ASC, TEN, CMBT) get a NAV benchmark too.

**`RONAV` = return on NAV** — the asset-NAV analog of return on equity: annual earnings ÷ NAV per share. Two variants appear below. **`RONAV_norm`** (normalized) is what the fleet *would* earn on its marked NAV at mid-cycle rates; **`RONAV_implied`** is the return on NAV the *market price* is implying, backed out of the same identity.

`P/NAV* = (RONAV_norm − g)/(r − g) = 1 + (RONAV_norm − r)/(r − g)`; `Justified FV/sh = P/NAV* × NAV/sh`; `RONAV_implied = g + P/NAV(mkt)·(r − g)`. `r` = cost of equity 11% (constant in v1). `NAV/sh` is the tool's CLEAN, un-haircut marked NAV — transaction-anchored (METHODOLOGY §9.9), the SAME basis the headline FV and broker sweep use; governance discount is applied downstream, never inside it.

**RONAV_norm is return on *marked NAV*, not on accounting book**, and **through-cycle, not NTM (next-twelve-months)**: `normalized_annual_EPS / NAV/sh`, where the EPS runs the dividend-strip earnings machinery with every vessel class's day-rate (TCE, time-charter equivalent) pinned to its cycle anchor (`historical_tce_means`), NOT the FFA (forward freight agreement) forward curve. Book always 'earns well' mid-cycle and says nothing about whether the market value is justified; the FFA front end is the hot near-term number that would inflate the multiple — both are deliberately avoided.

**Read this as an ORDERING tool, not a precision estimate.** `r − g` is a small denominator, so the multiple is hypersensitive: ±1pp on `g` or `RONAV_norm` swings it 10-20% (see the per-sector sensitivity grids below). **Anchor-bias caveats — RONAV_norm inherits the cycle anchors, which are not all true long-run means:** (1) **dry-bulk** anchors are 22-month firm-window medians, biased elevated (§11.7.5), so its multiples are an **upper bound**; (2) **containership** anchors are FY2021-2025 calendar averages (boom-tilted, `fy_calendar_avg` per §10 — NOT a through-cycle mean), so containership `RONAV_norm` is biased high even more than dry-bulk — GSL/MPCC's multiples are a **loose upper bound, not a real target**; (3) NAV dwt-scales per vessel but strip revenue is per-class count-based, so large-hull dry-bulk names (SB, CMBT) are biased toward 'rich' (partially offsetting (1)).

**Not in the headline FV** (diagnostic only); whether justified-P/NAV ranking predicts forward returns is a separate pre-registered study.

| Ticker | Sector | NAV/sh | Price | P/NAV (mkt) | RONAV_norm | r | g | Justified P/NAV | Justified FV/sh | RONAV_implied (mkt) | Gap (RONAV−impl) | Read |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| GSL | containerships | $38.59 | $38.99 | 1.010× | 51.1% | 11% | 1.5% | 5.219× | $201.38 | 11.1% | +40.0% | cheap |
| CCEC | lng | $28.10 | $21.90 | 0.779× | 27.5% | 11% | 2.0% | 2.835× | $79.65 | 9.0% | +18.5% | cheap |
| TEN **(WHOLE-CO)** | crude | $87.70 | $37.14 | 0.424× | 13.3% | 11% | 1.0% | 1.234× | $108.20 | 5.2% | +8.1% | cheap |
| FLNG | lng | $28.45 | $29.70 | 1.044× | 14.6% | 11% | 2.0% | 1.405× | $39.99 | 11.4% | +3.3% | cheap |
| SB | dry_bulk | $10.14 | $6.39 | 0.630× | 8.2% | 11% | 1.0% | 0.724× | $7.34 | 7.3% | +0.9% | cheap |
| SBLK | dry_bulk | $26.91 | $27.20 | 1.011× | 11.6% | 11% | 1.0% | 1.061× | $28.56 | 11.1% | +0.5% | fair |
| GNK | dry_bulk | $24.64 | $24.00 | 0.974× | 11.2% | 11% | 1.0% | 1.020× | $25.12 | 10.7% | +0.5% | fair |
| CMDB | dry_bulk | $31.33 | $17.25 | 0.551× | 6.7% | 11% | 1.0% | 0.572× | $17.92 | 6.5% | +0.2% | fair |
| TNK | crude | $77.51 | $70.80 | 0.913× | 8.8% | 11% | 1.0% | 0.782× | $60.60 | 10.1% | -1.3% | rich |
| HAFN | product | $5.22 | $7.70 | 1.476× | 14.2% | 11% | 1.0% | 1.320× | $6.89 | 15.8% | -1.6% | rich |
| CMBT **(WHOLE-CO)** | crude | $15.27 | $14.90 | 0.976× | 7.5% | 11% | 1.0% | 0.651× | $9.95 | 10.8% | -3.2% | rich |
| TRMD | product | $25.43 | $28.20 | 1.109× | 8.6% | 11% | 1.0% | 0.763× | $19.42 | 12.1% | -3.5% | rich |
| DHT | crude | $13.10 | $16.40 | 1.252× | 9.2% | 11% | 1.0% | 0.820× | $10.74 | 13.5% | -4.3% | rich |
| STNG | product | $80.35 | $75.60 | 0.941× | 4.9% | 11% | 1.0% | 0.387× | $31.11 | 10.4% | -5.5% | rich |
| FRO | crude | $24.22 | $34.50 | 1.424× | 9.6% | 11% | 1.0% | 0.860× | $20.84 | 15.2% | -5.6% | rich |
| INSW **(WHOLE-CO)** | crude | $52.59 | $78.00 | 1.483× | 9.9% | 11% | 1.0% | 0.888× | $46.69 | 15.8% | -6.0% | rich |
| ASC | product | $15.93 | $16.00 | 1.004× | 4.8% | 11% | 1.0% | 0.378× | $6.03 | 11.0% | -6.3% | rich |
| ECO | crude | $33.88 | $47.70 | 1.408× | 6.5% | 11% | 1.0% | 0.549× | $18.60 | 15.1% | -8.6% | rich |
| NAT | crude | $2.07 | $5.20 | 2.508× | 16.1% | 11% | 1.0% | 1.513× | $3.14 | 26.1% | -10.0% | rich |
| CAPT | crude | $15.03 | $12.20 | 0.812× | 11.1% | 11% | 1.0% | — | — | 9.1% | +2.0% | newbuild-heavy (unreliable) |
| MPCC | containerships | $2.02 | $2.78 | 1.374× | 50.0% | 11% | 1.5% | — | — | 14.6% | +35.4% | newbuild-heavy (unreliable) |
| BRUT | crude | $9.40 | $5.40 | 0.574× | 20.9% | 11% | 1.0% | — | — | 6.7% | +14.2% | newbuild-heavy (unreliable) |

## Subsector vector — median Justified P/NAV

| Sector | Median Justified P/NAV | n |
|---|--:|--:|
| containerships | 5.219× | 1 |
| lng | 2.120× | 2 |
| dry_bulk | 0.872× | 4 |
| crude | 0.840× | 8 |
| product | 0.575× | 4 |

_Expected ordering lng / containerships ≥ tankers ≥ dry bulk — but the dry-bulk anchor-bias (upward) and dwt-scaling (downward on the multiple) caveats above make a strict ordering indicative only._


## Sensitivity grids — Justified P/NAV across g × RONAV_norm (r = 11%, base = sector median RONAV_norm)


**containerships** (base RONAV_norm 51.1%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 49.1% | 4.46× | 4.81× | 5.23× |
| 51.1% | 4.64× | 5.01× | 5.45× |
| 53.1% | 4.83× | 5.21× | 5.68× |

**crude** (base RONAV_norm 9.4%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 7.4% | 0.67× | 0.64× | 0.60× |
| 9.4% | 0.85× | 0.84× | 0.82× |
| 11.4% | 1.04× | 1.04× | 1.04× |

**dry_bulk** (base RONAV_norm 9.7%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 7.7% | 0.70× | 0.67× | 0.64× |
| 9.7% | 0.88× | 0.87× | 0.86× |
| 11.7% | 1.07× | 1.07× | 1.08× |

**lng** (base RONAV_norm 21.1%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 19.1% | 1.73× | 1.81× | 1.90× |
| 21.1% | 1.92× | 2.01× | 2.12× |
| 23.1% | 2.10× | 2.21× | 2.34× |

**product** (base RONAV_norm 6.8%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 4.8% | 0.43× | 0.38× | 0.31× |
| 6.8% | 0.61× | 0.58× | 0.53× |
| 8.8% | 0.80× | 0.78× | 0.75× |

_**(WHOLE-CO)** = hybrid (INSW / TEN / CMBT) valued whole-company: whole-company normalized EPS ÷ whole-company NAV, with the lead-sleeve `g` (the watchlist sector tag). Value-weighted `g` is the intended v2 refinement._


_Flags: `non-positive NAV`, `no cost data`, `no anchor`, `r≤g (invalid)`, `newbuild-heavy (unreliable)` (newbuild value share > 25% — a not-yet-delivered hull earns a full anchor-year in the strip while its NAV is PV-haircut), `negative mid-cycle EPS`, `sub-growth returns` (RONAV_norm < g ⇒ P/NAV* unstable). Flagged rows carry no multiple. Names with a sub-threshold newbuild program (e.g. FRO ~17%) compute but carry a mild residual upward RONAV bias. Per-subsector `r` is a documented v2 extension._
