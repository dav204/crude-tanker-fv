# Justified P/NAV diagnostic

A **coverage-independent** fair-multiple benchmark (METHODOLOGY §17). The broker-NAV sweep (§9.9) and consensus-EPS cross-check (§9.11) lean on Pareto coverage; this asks a question answerable from fundamentals alone — **does the fleet earn its cost of capital on its own marked NAV (net asset value)?** — so the APPROX / no-Pareto names (SB, CMDB, GSL, MPCC, CCEC, NAT, ASC, TEN, CMBT) get a NAV benchmark too.

**`RONAV` = return on NAV** — the asset-NAV analog of return on equity: annual earnings ÷ NAV per share. Two variants appear below. **`RONAV_norm`** (normalized) is what the fleet *would* earn on its marked NAV at mid-cycle rates; **`RONAV_implied`** is the return on NAV the *market price* is implying, backed out of the same identity.

`P/NAV* = (RONAV_norm − g)/(r − g) = 1 + (RONAV_norm − r)/(r − g)`; `Justified FV/sh = P/NAV* × NAV/sh`; `RONAV_implied = g + P/NAV(mkt)·(r − g)`. `r` = cost of equity 11% (constant in v1). `NAV/sh` is the tool's CLEAN, un-haircut marked NAV (governance discount is applied downstream, never inside it).

**RONAV_norm is return on *marked NAV*, not on accounting book**, and **through-cycle, not NTM (next-twelve-months)**: `normalized_annual_EPS / NAV/sh`, where the EPS runs the dividend-strip earnings machinery with every vessel class's day-rate (TCE, time-charter equivalent) pinned to its cycle anchor (`historical_tce_means`), NOT the FFA (forward freight agreement) forward curve. Book always 'earns well' mid-cycle and says nothing about whether the market value is justified; the FFA front end is the hot near-term number that would inflate the multiple — both are deliberately avoided.

**Read this as an ORDERING tool, not a precision estimate.** `r − g` is a small denominator, so the multiple is hypersensitive: ±1pp on `g` or `RONAV_norm` swings it 10-20% (see the per-sector sensitivity grids below). **Anchor-bias caveats — RONAV_norm inherits the cycle anchors, which are not all true long-run means:** (1) **dry-bulk** anchors are 22-month firm-window medians, biased elevated (§11.7.5), so its multiples are an **upper bound**; (2) **containership** anchors are FY2021-2025 calendar averages (boom-tilted, `fy_calendar_avg` per §10 — NOT a through-cycle mean), so containership `RONAV_norm` is biased high even more than dry-bulk — GSL/MPCC's multiples are a **loose upper bound, not a real target**; (3) NAV dwt-scales per vessel but strip revenue is per-class count-based, so large-hull dry-bulk names (SB, CMBT) are biased toward 'rich' (partially offsetting (1)).

**Not in the headline FV** (diagnostic only); whether justified-P/NAV ranking predicts forward returns is a separate pre-registered study.

| Ticker | Sector | NAV/sh | Price | P/NAV (mkt) | RONAV_norm | r | g | Justified P/NAV | Justified FV/sh | RONAV_implied (mkt) | Gap (RONAV−impl) | Read |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| GSL | containerships | $38.59 | $38.99 | 1.010× | 51.1% | 11% | 1.5% | 5.219× | $201.38 | 11.1% | +40.0% | cheap |
| CCEC | lng | $28.10 | $21.90 | 0.779× | 27.5% | 11% | 2.0% | 2.835× | $79.65 | 9.0% | +18.5% | cheap |
| TEN **(WHOLE-CO)** | crude | $95.95 | $37.14 | 0.387× | 12.2% | 11% | 1.0% | 1.119× | $107.38 | 4.9% | +7.3% | cheap |
| FLNG | lng | $28.45 | $29.70 | 1.044× | 14.6% | 11% | 2.0% | 1.405× | $39.99 | 11.4% | +3.3% | cheap |
| SB | dry_bulk | $9.48 | $6.39 | 0.674× | 8.8% | 11% | 1.0% | 0.781× | $7.40 | 7.7% | +1.1% | cheap |
| SBLK | dry_bulk | $27.34 | $27.20 | 0.995× | 11.4% | 11% | 1.0% | 1.043× | $28.51 | 11.0% | +0.5% | fair |
| GNK | dry_bulk | $25.48 | $24.00 | 0.942× | 10.8% | 11% | 1.0% | 0.983× | $25.04 | 10.4% | +0.4% | fair |
| CMDB | dry_bulk | $32.12 | $17.25 | 0.537× | 6.6% | 11% | 1.0% | 0.556× | $17.84 | 6.4% | +0.2% | fair |
| TNK | crude | $83.32 | $70.80 | 0.850× | 8.2% | 11% | 1.0% | 0.720× | $60.01 | 9.5% | -1.3% | rich |
| HAFN | product | $5.34 | $7.70 | 1.443× | 13.9% | 11% | 1.0% | 1.288× | $6.88 | 15.4% | -1.5% | rich |
| CMBT **(WHOLE-CO)** | crude | $15.24 | $14.90 | 0.978× | 7.5% | 11% | 1.0% | 0.653× | $9.95 | 10.8% | -3.2% | rich |
| TRMD | product | $26.74 | $28.20 | 1.055× | 8.2% | 11% | 1.0% | 0.721× | $19.29 | 11.5% | -3.3% | rich |
| DHT | crude | $15.29 | $16.40 | 1.073× | 7.9% | 11% | 1.0% | 0.688× | $10.52 | 11.7% | -3.8% | rich |
| FRO | crude | $28.47 | $34.50 | 1.212× | 8.2% | 11% | 1.0% | 0.717× | $20.41 | 13.1% | -4.9% | rich |
| STNG | product | $83.87 | $75.60 | 0.901× | 4.7% | 11% | 1.0% | 0.367× | $30.76 | 10.0% | -5.3% | rich |
| INSW **(WHOLE-CO)** | crude | $57.91 | $78.00 | 1.347× | 9.0% | 11% | 1.0% | 0.797× | $46.16 | 14.5% | -5.5% | rich |
| ASC | product | $15.96 | $16.00 | 1.003× | 4.8% | 11% | 1.0% | 0.377× | $6.02 | 11.0% | -6.3% | rich |
| ECO | crude | $39.93 | $47.70 | 1.194× | 5.5% | 11% | 1.0% | 0.451× | $17.99 | 12.9% | -7.4% | rich |
| NAT | crude | $2.63 | $5.20 | 1.976× | 12.7% | 11% | 1.0% | 1.170× | $3.08 | 20.8% | -8.1% | rich |
| CAPT | crude | $15.20 | $12.20 | 0.802× | 10.9% | 11% | 1.0% | — | — | 9.0% | +1.9% | newbuild-heavy (unreliable) |
| MPCC | containerships | $2.02 | $2.78 | 1.374× | 50.0% | 11% | 1.5% | — | — | 14.6% | +35.4% | newbuild-heavy (unreliable) |
| BRUT | crude | $9.40 | $5.40 | 0.574× | 20.9% | 11% | 1.0% | — | — | 6.7% | +14.2% | newbuild-heavy (unreliable) |

## Subsector vector — median Justified P/NAV

| Sector | Median Justified P/NAV | n |
|---|--:|--:|
| containerships | 5.219× | 1 |
| lng | 2.120× | 2 |
| dry_bulk | 0.882× | 4 |
| crude | 0.719× | 8 |
| product | 0.549× | 4 |

_Expected ordering lng / containerships ≥ tankers ≥ dry bulk — but the dry-bulk anchor-bias (upward) and dwt-scaling (downward on the multiple) caveats above make a strict ordering indicative only._


## Sensitivity grids — Justified P/NAV across g × RONAV_norm (r = 11%, base = sector median RONAV_norm)


**containerships** (base RONAV_norm 51.1%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 49.1% | 4.46× | 4.81× | 5.23× |
| 51.1% | 4.64× | 5.01× | 5.45× |
| 53.1% | 4.83× | 5.21× | 5.68× |

**crude** (base RONAV_norm 8.2%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 6.2% | 0.56× | 0.52× | 0.47× |
| 8.2% | 0.74× | 0.72× | 0.69× |
| 10.2% | 0.93× | 0.92× | 0.91× |

**dry_bulk** (base RONAV_norm 9.8%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 7.8% | 0.71× | 0.68× | 0.65× |
| 9.8% | 0.89× | 0.88× | 0.87× |
| 11.8% | 1.07× | 1.08× | 1.09× |

**lng** (base RONAV_norm 21.1%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 19.1% | 1.73× | 1.81× | 1.90× |
| 21.1% | 1.92× | 2.01× | 2.12× |
| 23.1% | 2.10× | 2.21× | 2.34× |

**product** (base RONAV_norm 6.5%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 4.5% | 0.41× | 0.35× | 0.28× |
| 6.5% | 0.59× | 0.55× | 0.50× |
| 8.5% | 0.77× | 0.75× | 0.72× |

_**(WHOLE-CO)** = hybrid (INSW / TEN / CMBT) valued whole-company: whole-company normalized EPS ÷ whole-company NAV, with the lead-sleeve `g` (the watchlist sector tag). Value-weighted `g` is the intended v2 refinement._


_Flags: `non-positive NAV`, `no cost data`, `no anchor`, `r≤g (invalid)`, `newbuild-heavy (unreliable)` (newbuild value share > 25% — a not-yet-delivered hull earns a full anchor-year in the strip while its NAV is PV-haircut), `negative mid-cycle EPS`, `sub-growth returns` (RONAV_norm < g ⇒ P/NAV* unstable). Flagged rows carry no multiple. Names with a sub-threshold newbuild program (e.g. FRO ~17%) compute but carry a mild residual upward RONAV bias. Per-subsector `r` is a documented v2 extension._
