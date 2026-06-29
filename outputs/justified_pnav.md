# Justified P/NAV diagnostic

A **coverage-independent** fair-multiple benchmark (METHODOLOGY §17). The broker-NAV sweep (§9.9) and consensus-EPS cross-check (§9.11) lean on Pareto coverage; this asks a question answerable from fundamentals alone — **does the fleet earn its cost of capital on its own marked NAV (net asset value)?** — so the APPROX / no-Pareto names (SB, CMDB, GSL, MPCC, CCEC, NAT, ASC, TEN, CMBT) get a NAV benchmark too.

**`RONAV` = return on NAV** — the asset-NAV analog of return on equity: annual earnings ÷ NAV per share. Two variants appear below. **`RONAV_norm`** (normalized) is what the fleet *would* earn on its marked NAV at mid-cycle rates; **`RONAV_implied`** is the return on NAV the *market price* is implying, backed out of the same identity.

`P/NAV* = (RONAV_norm − g)/(r − g) = 1 + (RONAV_norm − r)/(r − g)`; `Justified FV/sh = P/NAV* × NAV/sh`; `RONAV_implied = g + P/NAV(mkt)·(r − g)`. `r` = cost of equity 11% (constant in v1). `NAV/sh` is the tool's CLEAN, un-haircut marked NAV — transaction-anchored (METHODOLOGY §9.9), the SAME basis the headline FV and broker sweep use; governance discount is applied downstream, never inside it.

**RONAV_norm is return on *marked NAV*, not on accounting book**, and **through-cycle, not NTM (next-twelve-months)**: `normalized_annual_EPS / NAV/sh`, where the EPS runs the dividend-strip earnings machinery with every vessel class's day-rate (TCE, time-charter equivalent) pinned to a through-cycle anchor, NOT the FFA (forward freight agreement) forward curve. Book always 'earns well' mid-cycle and says nothing about whether the market value is justified; the FFA front end is the hot near-term number that would inflate the multiple — both are deliberately avoided.

**Two normal-rate bases (P1, §18; PRE_REGISTRATION_NORMAL_RATES.md).** Each name is shown under BOTH: **`parity`** (headline) — replacement economics, the TCE that lets a newbuild earn its cost of capital (closes the loop: justified-P/NAV = 1 for a newbuild); and **`historical_mean`** (cross-check) — the realized through-cycle anchor (current `historical_tce_means`). The per-class divergence (`historical − parity`) is the under-/over-ordered signal. The deliverable is whether the cheap/rich call **survives the basis choice** (`Robust` column): survives → a genuine read; **flips → the call depends on the normalization philosophy**, which is itself the finding. PROVISIONAL pending the §18.5b orderbook validation of the divergence.

**Read this as an ORDERING tool, not a precision estimate.** `r − g` is a small denominator, so the multiple is hypersensitive: ±1pp on `g` or `RONAV_norm` swings it 10-20% (see the per-sector sensitivity grids below). **Anchor-bias caveats — RONAV_norm inherits the cycle anchors, which are not all true long-run means:** (1) **dry-bulk** anchors are 22-month firm-window medians, biased elevated (§11.7.5), so its multiples are an **upper bound**; (2) **containership** anchors are FY2021-2025 calendar averages (boom-tilted, `fy_calendar_avg` per §10 — NOT a through-cycle mean), so containership `RONAV_norm` is biased high even more than dry-bulk — GSL/MPCC's multiples are a **loose upper bound, not a real target**; (3) NAV dwt-scales per vessel but strip revenue is per-class count-based, so large-hull dry-bulk names (SB, CMBT) are biased toward 'rich' (partially offsetting (1)).

**Not in the headline FV** (diagnostic only); whether justified-P/NAV ranking predicts forward returns is a separate pre-registered study.

| Ticker | Sector | NAV/sh | Price | P/NAV (mkt) | RONAV (par) | Just P/NAV (par) | RONAV (hist) | Just P/NAV (hist) | Read: par → hist | Robust? |
|---|---|--:|--:|--:|--:|--:|--:|--:|---|---|
| GSL | containerships | $38.59 | $38.99 | 1.010× | 22.8% | 2.244× | 51.1% | 5.219× | cheap → cheap | robust |
| TEN **(WHOLE-CO)** | crude | $87.70 | $37.14 | 0.424× | 14.2% | 1.320× | 13.3% | 1.234× | cheap → cheap | robust |
| SB | dry_bulk | $9.82 | $6.39 | 0.651× | 12.7% | 1.175× | 8.3% | 0.733× | cheap → cheap | robust |
| SBLK | dry_bulk | $26.91 | $27.20 | 1.011× | 14.2% | 1.321× | 11.6% | 1.061× | cheap → fair | flips (cheap/fair) |
| NAT | crude | $2.07 | $5.20 | 2.508× | 28.7% | 2.768× | 16.1% | 1.513× | cheap → rich | flips (cheap/rich) |
| FLNG | lng | $28.45 | $29.70 | 1.044× | 13.6% | 1.292× | 14.6% | 1.405× | cheap → cheap | robust |
| CMDB | dry_bulk | $31.33 | $17.25 | 0.551× | 8.7% | 0.772× | 6.7% | 0.572× | cheap → fair | flips (cheap/fair) |
| GNK | dry_bulk | $24.64 | $24.00 | 0.974× | 12.8% | 1.185× | 11.2% | 1.020× | cheap → fair | flips (cheap/fair) |
| HAFN | product | $5.22 | $7.70 | 1.476× | 16.8% | 1.583× | 14.2% | 1.320× | fair → rich | flips (fair/rich) |
| TRMD | product | $25.43 | $28.20 | 1.109× | 13.2% | 1.216× | 8.6% | 0.763× | fair → rich | flips (fair/rich) |
| DHT | crude | $13.10 | $16.40 | 1.252× | 14.4% | 1.340× | 9.2% | 0.820× | fair → rich | flips (fair/rich) |
| FRO | crude | $24.22 | $34.50 | 1.424× | 15.2% | 1.417× | 9.6% | 0.860× | fair → rich | flips (fair/rich) |
| CMBT **(WHOLE-CO)** | crude | $15.27 | $14.90 | 0.976× | 10.3% | 0.926× | 7.5% | 0.651× | fair → rich | flips (fair/rich) |
| TNK | crude | $77.51 | $70.80 | 0.913× | 9.5% | 0.852× | 8.8% | 0.782× | fair → rich | flips (fair/rich) |
| ASC | product | $15.93 | $16.00 | 1.004× | 9.8% | 0.879× | 4.8% | 0.378× | rich → rich | robust |
| INSW **(WHOLE-CO)** | crude | $52.59 | $78.00 | 1.483× | 13.7% | 1.266× | 9.9% | 0.888× | rich → rich | robust |
| STNG | product | $80.35 | $75.60 | 0.941× | 8.1% | 0.709× | 4.9% | 0.387× | rich → rich | robust |
| ECO | crude | $33.88 | $47.70 | 1.408× | 11.9% | 1.086× | 6.5% | 0.549× | rich → rich | robust |
| CCEC | lng | $28.10 | $21.90 | 0.779× | n/a | — | 27.5% | 2.835× | no anchor → cheap | n/a |
| CAPT | crude | $15.03 | $12.20 | 0.812× | 15.6% | — | 11.1% | — | newbuild-heavy (unreliable) → newbuild-heavy (unreliable) | n/a |
| MPCC | containerships | $2.02 | $2.78 | 1.374× | 19.9% | — | 50.0% | — | newbuild-heavy (unreliable) → newbuild-heavy (unreliable) | n/a |
| BRUT | crude | $9.40 | $5.40 | 0.574× | 31.2% | — | 20.9% | — | newbuild-heavy (unreliable) → newbuild-heavy (unreliable) | n/a |

## Subsector vector — median Justified P/NAV (parity headline, historical cross-check)

| Sector | Median Just P/NAV (parity) | Median (historical) | n |
|---|--:|--:|--:|
| containerships | 2.244× | 5.219× | 1 |
| crude | 1.293× | 0.840× | 8 |
| lng | 1.292× | 2.120× | 1 |
| dry_bulk | 1.180× | 0.876× | 4 |
| product | 1.047× | 0.575× | 4 |

_The two columns ARE the signal: where parity ≫ historical, the sector reads cheaper under replacement economics than under its (boom/firm-window-biased) historical anchor — the §18 under-ordering. The §17.6 anchor-bias caveats apply to the historical column only; parity is independent of those biases (it is built from newbuild cost, not a rate-history window)._


## Sensitivity grids — Justified P/NAV across g × RONAV_norm (r = 11%, base = sector median RONAV_norm)


**containerships** (base RONAV_norm 22.8%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 20.8% | 1.89× | 1.98× | 2.09× |
| 22.8% | 2.07× | 2.18× | 2.31× |
| 24.8% | 2.26× | 2.38× | 2.53× |

**crude** (base RONAV_norm 13.9%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 11.9% | 1.08× | 1.09× | 1.10× |
| 13.9% | 1.27× | 1.29× | 1.33× |
| 15.9% | 1.45× | 1.49× | 1.55× |

**dry_bulk** (base RONAV_norm 12.8%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 10.8% | 0.98× | 0.98× | 0.98× |
| 12.8% | 1.16× | 1.18× | 1.20× |
| 14.8% | 1.35× | 1.38× | 1.42× |

**lng** (base RONAV_norm 13.6%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 11.6% | 1.06× | 1.06× | 1.07× |
| 13.6% | 1.24× | 1.26× | 1.29× |
| 15.6% | 1.42× | 1.46× | 1.51× |

**product** (base RONAV_norm 11.5%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 9.5% | 0.86× | 0.85× | 0.83× |
| 11.5% | 1.04× | 1.05× | 1.05× |
| 13.5% | 1.22× | 1.25× | 1.27× |

_**(WHOLE-CO)** = hybrid (INSW / TEN / CMBT) valued whole-company: whole-company normalized EPS ÷ whole-company NAV, with the lead-sleeve `g` (the watchlist sector tag). Value-weighted `g` is the intended v2 refinement._


_Flags: `non-positive NAV`, `no cost data`, `no anchor`, `r≤g (invalid)`, `newbuild-heavy (unreliable)` (newbuild value share > 25% — a not-yet-delivered hull earns a full anchor-year in the strip while its NAV is PV-haircut), `negative mid-cycle EPS`, `sub-growth returns` (RONAV_norm < g ⇒ P/NAV* unstable). Flagged rows carry no multiple. Names with a sub-threshold newbuild program (e.g. FRO ~17%) compute but carry a mild residual upward RONAV bias. Per-subsector `r` is a documented v2 extension._
