# Consensus forward-EPS cross-check

The **earnings-leg analog of the broker-NAV sweep** (METHODOLOGY §9.11 / §9.9). The sweep asks whether our *NAV* agrees with broker consensus; this asks whether our modelled *forward earnings* — the input that drives the dividend strip — agree with sell-side consensus.

`consensus_fwd_eps = price / consensus_fwd_pe` (Pareto Shipping Daily, 1Y FWD P/E). `tool_fwd_eps` = sum of the first 4 quarters of our dividend strip's per-quarter EPS (NTM operating EPS, net of tax, FFA-forward-curve-implied). Both are operating-EPS constructs (each excludes one-off vessel-sale gains).

**Reading the gap.** A large positive gap (tool > consensus) means our forward-curve earnings run hotter than the street — typically the FFA curve holding near-peak rates while consensus prices mean-reversion. This is *expected* near a cycle peak, and the framework compensates: `w_earn` (the strip's weight in the blend) is low exactly when the gap is widest. **A wide gap + low `w_earn` is the cycle weighting working as designed, not an error.**

| Name | Sector | Price | Cons. fwd P/E | Cons. fwd EPS | Tool fwd EPS | Tool impl. P/E | EPS gap | Cons. earn. yld | Cycle (band) | w_earn | Read |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| CAPT | crude | $16.06 | 25.5× | $0.63 | $2.91 | 5.5× | +361% | 3.9% | 2.32× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| NAT | crude | $6.80 | 17.7× | $0.38 | $1.51 | 4.5× | +294% | 5.6% | 2.09× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| BRUT | crude | $4.70 | 14.4× | $0.33 | $1.06 | 4.4× | +226% | 6.9% | 2.64× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CMDB | dry_bulk | $17.25 | 10.5× | $1.64 | $4.90 | 3.5× | +198% | 9.5% | 1.41× (elevated) | 0.40 | earnings-driven (tool>cons) |
| INSW **(WHOLE-CO)** | crude | $99.30 | 13.9× | $7.14 | $20.63 | 4.8× | +189% | 7.2% | 2.10× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TRMD | product | $31.80 | 10.6× | $3.00 | $8.63 | 3.7× | +188% | 9.4% | 1.84× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CCEC | lng | $22.80 | 7.9× | $2.89 | $7.95 | 2.9× | +175% | 12.7% | 0.78× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| GNK | dry_bulk | $25.80 | 12.3× | $2.10 | $5.54 | 4.7× | +164% | 8.1% | 1.41× (elevated) | 0.40 | earnings-driven (tool>cons) |
| 2343 | dry_bulk | $0.53 | 17.8× | $0.03 | $0.08 | 6.7× | +164% | 5.6% | 1.20× (elevated) | 0.40 | earnings-driven (tool>cons) |
| DHT | crude | $19.40 | 9.9× | $1.96 | $5.03 | 3.9× | +157% | 10.1% | 2.64× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CMBT | crude | $18.30 | 10.3× | $1.78 | $4.35 | 4.2× | +145% | 9.7% | 1.71× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| FRO | crude | $43.80 | 10.3× | $4.25 | $9.90 | 4.4× | +133% | 9.7% | 2.43× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| ECO | crude | $66.30 | 10.1× | $6.56 | $14.82 | 4.5× | +126% | 9.9% | 2.38× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| HAFN | product | $8.30 | 10.4× | $0.80 | $1.76 | 4.7× | +120% | 9.6% | 1.80× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| ASC | product | $17.70 | 10.6× | $1.67 | $3.59 | 4.9× | +115% | 9.4% | 1.68× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TEN | crude | $37.14 | 4.6× | $8.07 | $15.88 | 2.3× | +97% | 21.7% | 1.67× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TNK | crude | $88.20 | 8.8× | $10.02 | $18.53 | 4.8× | +85% | 11.4% | 1.78× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| STNG | product | $77.40 | 14.0× | $5.53 | $9.68 | 8.0× | +75% | 7.1% | 1.81× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| FLNG | lng | $31.30 | 14.6× | $2.14 | $3.74 | 8.4× | +74% | 6.8% | 0.71× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| SB | dry_bulk | $8.52 | 6.5× | $1.31 | $2.14 | 4.0× | +63% | 15.4% | 1.62× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| MPCC | containerships | $2.90 | 8.4× | $0.35 | $0.55 | 5.3× | +59% | 11.9% | 1.32× (elevated) | 0.40 | earnings-driven (tool>cons) |
| BWLP | lpg | $24.18 | 11.8× | $2.05 | $3.23 | 7.5× | +58% | 8.5% | 1.59× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| SBLK | dry_bulk | $30.40 | 7.1× | $4.28 | $6.56 | 4.6× | +53% | 14.1% | 1.47× (elevated) | 0.40 | earnings-driven (tool>cons) |
| GSL | containerships | $38.99 | 3.8× | $10.26 | $14.08 | 2.8× | +37% | 26.3% | 1.51× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| LPG | lpg | $49.30 | 12.9× | $3.82 | $4.36 | 11.3× | +14% | 7.8% | 1.59× (late-cycle/peak) | 0.30 | earnings-aligned |

_**(WHOLE-CO)** = hybrid name; the tool forward EPS here is the whole-company FFA strip (a proxy — the headline FV uses the crude+product carve-out aggregation)._


_Earnings-driven threshold: |gap| ≥ 25%. Near a cycle peak most names trip it on the high side by construction (FFA holds elevated rates; consensus normalises) — the signal is the **magnitude, direction, and cross-name pattern**, read alongside `w_earn`. Limitations: 1-year horizon only (strip is 8q + terminal NAV); EPS ≠ dividends (buyback channels like STNG are invisible); shipping consensus EPS is dispersed and lags spot. Directional cross-check, not a calibration target._
