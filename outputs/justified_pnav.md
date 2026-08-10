# Justified P/NAV diagnostic

A **coverage-independent** fair-multiple benchmark (METHODOLOGY §17). The broker-NAV sweep (§9.9) and consensus-EPS cross-check (§9.11) lean on Pareto coverage; this asks a question answerable from fundamentals alone — **does the fleet earn its cost of capital on its own marked NAV (net asset value)?** — so the APPROX / no-Pareto names (SB, CMDB, GSL, MPCC, CCEC, NAT, ASC, TEN, CMBT) get a NAV benchmark too.

**`RONAV` = return on NAV** — the asset-NAV analog of return on equity: annual earnings ÷ NAV per share. Two variants appear below. **`RONAV_norm`** (normalized) is what the fleet *would* earn on its marked NAV at mid-cycle rates; **`RONAV_implied`** is the return on NAV the *market price* is implying, backed out of the same identity.

`P/NAV* = (RONAV_norm − g)/(r − g) = 1 + (RONAV_norm − r)/(r − g)`; `Justified FV/sh = P/NAV* × NAV/sh`; `RONAV_implied = g + P/NAV(mkt)·(r − g)`. `r` = cost of equity 11% (constant in v1). `NAV/sh` is the tool's CLEAN, un-haircut marked NAV — transaction-anchored (METHODOLOGY §9.9), the SAME basis the headline FV and broker sweep use; governance discount is applied downstream, never inside it.

**RONAV_norm is return on *marked NAV*, not on accounting book**, and **through-cycle, not NTM (next-twelve-months)**: `normalized_annual_EPS / NAV/sh`, where the EPS runs the dividend-strip earnings machinery with every vessel class's day-rate (TCE, time-charter equivalent) pinned to a through-cycle anchor, NOT the FFA (forward freight agreement) forward curve. Book always 'earns well' mid-cycle and says nothing about whether the market value is justified; the FFA front end is the hot near-term number that would inflate the multiple — both are deliberately avoided.

**Two normal-rate bases (P1, §18; PRE_REGISTRATION_NORMAL_RATES.md).** Each name is shown under BOTH: **`parity`** (headline) — replacement economics, the TCE that lets a newbuild earn its cost of capital (closes the loop: justified-P/NAV = 1 for a newbuild); and **`historical_mean`** (cross-check) — the realized through-cycle anchor (current `historical_tce_means`). The per-class divergence (`historical − parity`) is the under-/over-ordered signal. The deliverable is whether the cheap/rich call **survives the basis choice** (`Robust` column): survives → a genuine read; **flips → the call depends on the normalization philosophy**, which is itself the finding. PROVISIONAL pending the §18.5b orderbook validation of the divergence.

**Read this as an ORDERING tool, not a precision estimate.** `r − g` is a small denominator, so the multiple is hypersensitive: ±1pp on `g` or `RONAV_norm` swings it 10-20% (see the per-sector sensitivity grids below). **Anchor-bias caveats — RONAV_norm inherits the cycle anchors, which are not all true long-run means:** (1) **dry-bulk** anchors are 22-month firm-window medians, biased elevated (§11.7.5), so its multiples are an **upper bound**; (2) **containership** anchors are FY2021-2025 calendar averages (boom-tilted, `fy_calendar_avg` per §10 — NOT a through-cycle mean), so containership `RONAV_norm` is biased high even more than dry-bulk — GSL/MPCC's multiples are a **loose upper bound, not a real target**; (3) NAV dwt-scales per vessel but strip revenue is per-class count-based, so large-hull dry-bulk names (SB, CMBT) are biased toward 'rich' (partially offsetting (1)).

**A crude name reading `rich` near a cycle peak is cycle POSITION, not a short signal.** RONAV_norm is pinned to a through-cycle anchor while the market price embeds the hot near-peak NTM rate, so a crude pure-play at/near peak (DHT/FRO/ECO/NAT) reads `rich` BY CONSTRUCTION (the §12 NAT mechanism) — it says where in the cycle the name sits, not TRIM/SHORT. Read the crude `rich` column together with the cycle position, never as a standalone call.

**Not in the headline FV** (diagnostic only); whether justified-P/NAV ranking predicts forward returns is a separate pre-registered study.

| Ticker | Sector | NAV/sh | Price | P/NAV (mkt) | RONAV (par) | Just P/NAV (par) | RONAV (hist) | Just P/NAV (hist) | Read: par → hist | Robust? |
|---|---|--:|--:|--:|--:|--:|--:|--:|---|---|
| SB | dry_bulk | $10.58 | $6.39 | 0.604× | 14.8% | 1.381× | 9.9% | 0.892× | cheap → cheap | robust |
| SBLK | dry_bulk | $32.78 | $25.20 | 0.769× | 12.2% | 1.116× | 10.3% | 0.930× | cheap → cheap | robust |
| GNK | dry_bulk | $25.12 | $24.50 | 0.975× | 12.3% | 1.134× | 11.2% | 1.019× | cheap → fair | flips (cheap/fair) |
| CMDB | dry_bulk | $32.13 | $17.25 | 0.537× | 7.8% | 0.683× | 6.5% | 0.554× | cheap → fair | flips (cheap/fair) |
| 2343 | dry_bulk | $0.41 | $0.39 | 0.958× | 12.0% | 1.100× | 12.6% | 1.158× | cheap → cheap | robust |
| TNK | crude | $84.60 | $67.60 | 0.799× | 6.9% | 0.589× | 8.2% | 0.716× | rich → rich | robust |
| DHT | crude | $15.01 | $17.20 | 1.146× | 9.0% | 0.805× | 8.5% | 0.747× | rich → rich | robust |
| FRO | crude | $25.34 | $36.80 | 1.452× | 10.0% | 0.903× | 9.2% | 0.818× | rich → rich | robust |
| ECO | crude | $39.54 | $53.10 | 1.343× | 6.7% | 0.568× | 5.6% | 0.456× | rich → rich | robust |
| NAT | crude | $2.85 | $5.80 | 2.039× | 12.9% | 1.191× | 9.7% | 0.865× | rich → rich | robust |
| INSW **(WHOLE-CO)** | crude | $54.64 | $82.40 | 1.508× | n/a | — | 9.7% | 0.873× | no anchor → rich | n/a |
| FLNG | lng | $28.45 | $29.30 | 1.030× | n/a | — | 14.6% | 1.405× | no anchor → cheap | n/a |
| CCEC | lng | $25.70 | $21.60 | 0.840× | n/a | — | 30.0% | 3.112× | no anchor → cheap | n/a |
| STNG | product | $76.22 | $73.00 | 0.958× | n/a | — | 3.5% | 0.248× | no anchor → rich | n/a |
| HAFN | product | $5.56 | $7.00 | 1.258× | n/a | — | 13.2% | 1.218× | no anchor → fair | n/a |
| TRMD | product | $30.22 | $27.70 | 0.917× | n/a | — | 7.4% | 0.644× | no anchor → rich | n/a |
| ASC | product | $17.37 | $14.90 | 0.858× | n/a | — | 7.2% | 0.621× | no anchor → rich | n/a |
| TEN **(WHOLE-CO)** | crude | $88.16 | $37.14 | 0.421× | n/a | — | 12.1% | 1.106× | no anchor → cheap | n/a |
| CAPT | crude | $15.48 | $13.31 | 0.860× | 11.0% | — | 10.8% | — | newbuild-heavy (unreliable) → newbuild-heavy (unreliable) | n/a |
| MPCC | containerships | $2.05 | $2.44 | 1.190× | n/a | — | 49.3% | — | no anchor → newbuild-heavy (unreliable) | n/a |
| GSL | containerships | $41.20 | $38.99 | 0.946× | n/a | — | 47.8% | 4.877× | no anchor → cheap | n/a |
| BRUT | crude | $8.80 | $5.30 | 0.602× | 23.7% | — | 22.3% | — | newbuild-heavy (unreliable) → newbuild-heavy (unreliable) | n/a |
| CMBT **(WHOLE-CO)** | crude | $16.46 | $14.60 | 0.887× | n/a | — | 7.0% | 0.597× | no anchor → rich | n/a |
| LPG | lpg | $35.69 | $36.00 | 1.009× | n/a | — | 6.9% | 0.594× | no anchor → rich | n/a |
| BWLP | lpg | $15.80 | $18.52 | 1.172× | n/a | — | 13.2% | 1.220× | no anchor → fair | n/a |

## Subsector vector — median Justified P/NAV (parity headline, historical cross-check)

| Sector | Median Just P/NAV (parity) | Median (historical) | n |
|---|--:|--:|--:|
| dry_bulk | 1.116× | 0.930× | 5 |
| crude | 0.805× | 0.783× | 5 |

_The two columns ARE the signal: where parity ≫ historical, the sector reads cheaper under replacement economics than under its (boom/firm-window-biased) historical anchor — the §18 under-ordering. The §17.6 anchor-bias caveats apply to the historical column only; parity is independent of those biases (it is built from newbuild cost, not a rate-history window)._


_The headline vector covers the COMPOSABLE sectors only (crude / product / dry_bulk). **LNG and containership medians are suppressed** as non-composable (§10: containerships on `fy_calendar_avg`, LNG spike-inclusive) — their per-name reads remain in the table above but do not roll into a cross-sector median._


## Sensitivity grids — Justified P/NAV across g × RONAV_norm (r = 11%, base = sector median RONAV_norm)


**crude** (base RONAV_norm 9.0%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 7.0% | 0.64× | 0.60× | 0.56× |
| 9.0% | 0.82× | 0.80× | 0.78× |
| 11.0% | 1.00× | 1.00× | 1.01× |

**dry_bulk** (base RONAV_norm 12.2%)

| RONAV_norm \ g | g=0% | g=1% | g=2% |
|---|--:|--:|--:|
| 10.2% | 0.92× | 0.92× | 0.91× |
| 12.2% | 1.11× | 1.12× | 1.13× |
| 14.2% | 1.29× | 1.32× | 1.35× |

_**(WHOLE-CO)** = hybrid (INSW / TEN / CMBT) valued whole-company: whole-company normalized EPS ÷ whole-company NAV, with the lead-sleeve `g` (the watchlist sector tag). Value-weighted `g` is the intended v2 refinement._


_Flags: `non-positive NAV`, `no cost data`, `no anchor`, `r≤g (invalid)`, `newbuild-heavy (unreliable)` (newbuild value share > 25% — a not-yet-delivered hull earns a full anchor-year in the strip while its NAV is PV-haircut), `negative mid-cycle EPS`, `sub-growth returns` (RONAV_norm < g ⇒ P/NAV* unstable). Flagged rows carry no multiple. Names with a sub-threshold newbuild program (e.g. FRO ~17%) compute but carry a mild residual upward RONAV bias. Per-subsector `r` is a documented v2 extension._


_**§15 governance dual-read.** CMDB (30%), TEN (30%) carry a realisation haircut applied at the blend layer + dividend-strip terminal but NOT in this leg, which uses CLEAN marked NAV by design. So the P/NAV* and Justified FV above are the **clean-NAV** reads; the **haircut basis** scales NAV — and Justified FV — by (1 − haircut) and lifts P/NAV(mkt) by the same factor (e.g. a 30% haircut ⇒ FV × 0.70, P/NAV(mkt) ÷ 0.70). Read these two names on both._
