# Consensus forward-EPS cross-check

The **earnings-leg analog of the broker-NAV sweep** (METHODOLOGY §9.11 / §9.9). The sweep asks whether our *NAV* agrees with broker consensus; this asks whether our modelled *forward earnings* — the input that drives the dividend strip — agree with sell-side consensus.

`consensus_fwd_eps = price / consensus_fwd_pe` (Pareto Shipping Daily, 1Y FWD P/E). `tool_fwd_eps` = sum of the first 4 quarters of our dividend strip's per-quarter EPS (NTM operating EPS, net of tax, FFA-forward-curve-implied). Both are operating-EPS constructs (each excludes one-off vessel-sale gains).

**Reading the gap.** A large positive gap (tool > consensus) means our forward-curve earnings run hotter than the street — typically the FFA curve holding near-peak rates while consensus prices mean-reversion. This is *expected* near a cycle peak, and the framework compensates: `w_earn` (the strip's weight in the blend) is low exactly when the gap is widest. **A wide gap + low `w_earn` is the cycle weighting working as designed, not an error.**

| Name | Sector | Price | Cons. fwd P/E | Cons. fwd EPS | Tool fwd EPS | Tool impl. P/E | EPS gap | Cons. earn. yld | Cycle (band) | w_earn | Read |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| NAT | crude | $5.80 | 19.2× | $0.30 | $1.45 | 4.0× | +381% | 5.2% | 2.21× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CAPT | crude | $13.31 | 15.5× | $0.86 | $3.60 | 3.7× | +319% | 6.5% | 2.45× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| BRUT | crude | $5.30 | 19.0× | $0.28 | $1.00 | 5.3× | +258% | 5.3% | 2.79× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TRMD | product | $27.70 | 9.3× | $2.98 | $9.61 | 2.9× | +223% | 10.8% | 1.69× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| INSW **(WHOLE-CO)** | crude | $82.40 | 12.0× | $6.87 | $21.72 | 3.8× | +216% | 8.3% | 2.11× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CCEC | lng | $21.60 | 8.1× | $2.67 | $7.95 | 2.7× | +198% | 12.3% | 0.78× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| DHT | crude | $17.20 | 9.3× | $1.85 | $5.51 | 3.1× | +198% | 10.8% | 2.79× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| HAFN | product | $7.00 | 8.7× | $0.80 | $2.39 | 2.9× | +198% | 11.5% | 1.66× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| FRO | crude | $36.80 | 9.4× | $3.91 | $11.31 | 3.3× | +189% | 10.6% | 2.57× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| GNK | dry_bulk | $24.50 | 14.2× | $1.73 | $4.79 | 5.1× | +178% | 7.0% | 1.44× (elevated) | 0.40 | earnings-driven (tool>cons) |
| ASC | product | $14.90 | 13.2× | $1.13 | $3.09 | 4.8× | +173% | 7.6% | 1.38× (elevated) | 0.40 | earnings-driven (tool>cons) |
| ECO | crude | $53.10 | 9.4× | $5.65 | $15.30 | 3.5× | +171% | 10.6% | 2.51× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TNK | crude | $67.60 | 8.4× | $8.05 | $21.33 | 3.2× | +165% | 11.9% | 1.90× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CMDB | dry_bulk | $17.25 | 10.5× | $1.64 | $4.23 | 4.1× | +157% | 9.5% | 1.44× (elevated) | 0.40 | earnings-driven (tool>cons) |
| SB | dry_bulk | $6.39 | 8.0× | $0.80 | $2.05 | 3.1× | +156% | 12.5% | 1.59× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CMBT | crude | $14.60 | 8.9× | $1.64 | $3.95 | 3.7× | +141% | 11.2% | 1.74× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| 2343 | dry_bulk | $0.39 | 13.0× | $0.03 | $0.07 | 5.5× | +135% | 7.7% | 1.24× (elevated) | 0.40 | earnings-driven (tool>cons) |
| TEN | crude | $37.14 | 4.6× | $8.07 | $17.68 | 2.1× | +119% | 21.7% | 1.77× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| FLNG | lng | $29.30 | 14.1× | $2.08 | $3.74 | 7.8× | +80% | 7.1% | 0.71× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| BWLP | lpg | $18.52 | 9.9× | $1.87 | $3.23 | 5.7× | +73% | 10.1% | 1.59× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| STNG | product | $73.00 | 11.1× | $6.58 | $11.29 | 6.5× | +72% | 9.0% | 1.73× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| MPCC | containerships | $2.44 | 7.7× | $0.32 | $0.54 | 4.5× | +71% | 13.0% | 1.32× (elevated) | 0.40 | earnings-driven (tool>cons) |
| SBLK | dry_bulk | $25.20 | 6.4× | $3.94 | $5.67 | 4.4× | +44% | 15.6% | 1.48× (elevated) | 0.40 | earnings-driven (tool>cons) |
| GSL | containerships | $38.99 | 3.8× | $10.26 | $14.08 | 2.8× | +37% | 26.3% | 1.49× (elevated) | 0.40 | earnings-driven (tool>cons) |
| LPG | lpg | $36.00 | 9.3× | $3.87 | $4.36 | 8.3× | +13% | 10.8% | 1.59× (late-cycle/peak) | 0.30 | earnings-aligned |

_**(WHOLE-CO)** = hybrid name; the tool forward EPS here is the whole-company FFA strip (a proxy — the headline FV uses the crude+product carve-out aggregation)._


_Earnings-driven threshold: |gap| ≥ 25%. Near a cycle peak most names trip it on the high side by construction (FFA holds elevated rates; consensus normalises) — the signal is the **magnitude, direction, and cross-name pattern**, read alongside `w_earn`. Limitations: 1-year horizon only (strip is 8q + terminal NAV); EPS ≠ dividends (buyback channels like STNG are invisible); shipping consensus EPS is dispersed and lags spot. Directional cross-check, not a calibration target._
