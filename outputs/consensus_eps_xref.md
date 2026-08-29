# Consensus forward-EPS cross-check

The **earnings-leg analog of the broker-NAV sweep** (METHODOLOGY §9.11 / §9.9). The sweep asks whether our *NAV* agrees with broker consensus; this asks whether our modelled *forward earnings* — the input that drives the dividend strip — agree with sell-side consensus.

`consensus_fwd_eps = price / consensus_fwd_pe` (Pareto Shipping Daily, 1Y FWD P/E). `tool_fwd_eps` = sum of the first 4 quarters of our dividend strip's per-quarter EPS (NTM operating EPS, net of tax, FFA-forward-curve-implied). Both are operating-EPS constructs (each excludes one-off vessel-sale gains).

**Reading the gap.** A large positive gap (tool > consensus) means our forward-curve earnings run hotter than the street — typically the FFA curve holding near-peak rates while consensus prices mean-reversion. This is *expected* near a cycle peak, and the framework compensates: `w_earn` (the strip's weight in the blend) is low exactly when the gap is widest. **A wide gap + low `w_earn` is the cycle weighting working as designed, not an error.**

| Name | Sector | Price | Cons. fwd P/E | Cons. fwd EPS | Tool fwd EPS | Tool impl. P/E | EPS gap | Cons. earn. yld | Cycle (band) | w_earn | Read |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| CAPT | crude | $14.14 | 22.2× | $0.64 | $2.91 | 4.9× | +356% | 4.5% | 2.32× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| NAT | crude | $6.40 | 18.7× | $0.34 | $1.51 | 4.2× | +343% | 5.3% | 2.09× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| BRUT | crude | $6.32 | 22.6× | $0.28 | $1.06 | 5.9× | +281% | 4.4% | 2.64× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| ASC | product | $17.00 | 15.5× | $1.10 | $3.59 | 4.7× | +227% | 6.5% | 1.68× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TRMD | product | $29.50 | 9.9× | $2.98 | $8.63 | 3.4× | +190% | 10.1% | 1.84× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| INSW **(WHOLE-CO)** | crude | $93.20 | 12.8× | $7.28 | $20.63 | 4.5× | +183% | 7.8% | 2.10× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CCEC | lng | $22.80 | 7.9× | $2.89 | $7.95 | 2.9× | +175% | 12.7% | 0.78× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| GNK | dry_bulk | $25.10 | 13.7× | $1.83 | $4.99 | 5.0× | +172% | 7.3% | 1.28× (elevated) | 0.40 | earnings-driven (tool>cons) |
| CMDB | dry_bulk | $17.25 | 10.5× | $1.64 | $4.36 | 4.0× | +165% | 9.5% | 1.31× (elevated) | 0.40 | earnings-driven (tool>cons) |
| DHT | crude | $18.40 | 9.7× | $1.90 | $5.03 | 3.7× | +165% | 10.3% | 2.64× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| SB | dry_bulk | $6.39 | 8.0× | $0.80 | $2.08 | 3.1× | +160% | 12.5% | 1.51× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| FRO | crude | $39.60 | 9.9× | $4.00 | $10.23 | 3.9× | +156% | 10.1% | 2.43× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| ECO | crude | $63.80 | 10.9× | $5.85 | $14.82 | 4.3× | +153% | 9.2% | 2.38× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CMBT | crude | $16.40 | 10.2× | $1.61 | $4.03 | 4.1× | +151% | 9.8% | 1.60× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| HAFN | product | $7.60 | 9.5× | $0.80 | $1.96 | 3.9× | +145% | 10.5% | 1.79× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| 2343 | dry_bulk | $0.39 | 13.0× | $0.03 | $0.07 | 5.3× | +145% | 7.7% | 1.17× (mid-cycle) | 0.50 | earnings-driven (tool>cons) |
| TNK | crude | $77.10 | 8.9× | $8.66 | $18.53 | 4.2× | +114% | 11.2% | 1.78× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TEN | crude | $37.14 | 4.6× | $8.07 | $15.88 | 2.3× | +97% | 21.7% | 1.67× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| FLNG | lng | $31.00 | 14.9× | $2.08 | $3.74 | 8.3× | +80% | 6.7% | 0.71× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| BWLP | lpg | $21.77 | 11.6× | $1.88 | $3.23 | 6.7× | +72% | 8.6% | 1.59× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| MPCC | containerships | $2.55 | 8.1× | $0.31 | $0.54 | 4.7× | +72% | 12.3% | 1.32× (elevated) | 0.40 | earnings-driven (tool>cons) |
| STNG | product | $76.40 | 13.0× | $5.88 | $9.68 | 7.9× | +65% | 7.7% | 1.81× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| SBLK | dry_bulk | $28.60 | 7.2× | $3.97 | $5.97 | 4.8× | +50% | 13.9% | 1.35× (elevated) | 0.40 | earnings-driven (tool>cons) |
| GSL | containerships | $38.99 | 3.8× | $10.26 | $14.08 | 2.8× | +37% | 26.3% | 1.51× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| LPG | lpg | $44.40 | 12.2× | $3.64 | $4.36 | 10.2× | +20% | 8.2% | 1.59× (late-cycle/peak) | 0.30 | earnings-aligned |

_**(WHOLE-CO)** = hybrid name; the tool forward EPS here is the whole-company FFA strip (a proxy — the headline FV uses the crude+product carve-out aggregation)._


_Earnings-driven threshold: |gap| ≥ 25%. Near a cycle peak most names trip it on the high side by construction (FFA holds elevated rates; consensus normalises) — the signal is the **magnitude, direction, and cross-name pattern**, read alongside `w_earn`. Limitations: 1-year horizon only (strip is 8q + terminal NAV); EPS ≠ dividends (buyback channels like STNG are invisible); shipping consensus EPS is dispersed and lags spot. Directional cross-check, not a calibration target._
