# Consensus forward-EPS cross-check

The **earnings-leg analog of the broker-NAV sweep** (METHODOLOGY §9.11 / §9.9). The sweep asks whether our *NAV* agrees with broker consensus; this asks whether our modelled *forward earnings* — the input that drives the dividend strip — agree with sell-side consensus.

`consensus_fwd_eps = price / consensus_fwd_pe` (Pareto Shipping Daily, 1Y FWD P/E). `tool_fwd_eps` = sum of the first 4 quarters of our dividend strip's per-quarter EPS (NTM operating EPS, net of tax, FFA-forward-curve-implied). Both are operating-EPS constructs (each excludes one-off vessel-sale gains).

**Reading the gap.** A large positive gap (tool > consensus) means our forward-curve earnings run hotter than the street — typically the FFA curve holding near-peak rates while consensus prices mean-reversion. This is *expected* near a cycle peak, and the framework compensates: `w_earn` (the strip's weight in the blend) is low exactly when the gap is widest. **A wide gap + low `w_earn` is the cycle weighting working as designed, not an error.**

| Name | Sector | Price | Cons. fwd P/E | Cons. fwd EPS | Tool fwd EPS | Tool impl. P/E | EPS gap | Cons. earn. yld | Cycle (band) | w_earn | Read |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| NAT | crude | $5.20 | 17.2× | $0.30 | $1.70 | 3.1× | +462% | 5.8% | 2.21× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| BRUT | crude | $5.40 | 22.0× | $0.25 | $1.00 | 5.4× | +307% | 4.5% | 2.79× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CAPT | crude | $12.20 | 11.1× | $1.10 | $3.60 | 3.4× | +228% | 9.0% | 2.45× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TRMD | product | $28.20 | 9.5× | $2.97 | $9.50 | 3.0× | +220% | 10.5% | 1.69× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CCEC | lng | $21.90 | 8.8× | $2.49 | $7.93 | 2.8× | +219% | 11.4% | 0.77× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| INSW **(WHOLE-CO)** | crude | $78.00 | 11.4× | $6.84 | $21.72 | 3.6× | +217% | 8.8% | 2.11× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| FRO | crude | $34.50 | 9.4× | $3.67 | $11.31 | 3.1× | +208% | 10.6% | 2.57× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| HAFN | product | $7.70 | 9.8× | $0.79 | $2.42 | 3.2× | +208% | 10.2% | 1.66× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| DHT | crude | $16.40 | 8.8× | $1.86 | $5.26 | 3.1× | +182% | 11.4% | 2.79× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| ECO | crude | $47.70 | 8.4× | $5.68 | $15.30 | 3.1× | +169% | 11.9% | 2.51× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| STNG | product | $75.60 | 11.4× | $6.63 | $17.36 | 4.4× | +162% | 8.8% | 1.76× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TNK | crude | $70.80 | 8.7× | $8.14 | $21.13 | 3.4× | +160% | 11.5% | 1.91× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| TEN | crude | $37.14 | 4.6× | $8.07 | $20.53 | 1.8× | +154% | 21.7% | 1.81× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| GNK | dry_bulk | $24.00 | 13.9× | $1.73 | $4.29 | 5.6× | +149% | 7.2% | 1.14× (mid-cycle) | 0.50 | earnings-driven (tool>cons) |
| CMBT | crude | $14.90 | 9.7× | $1.54 | $3.68 | 4.1× | +139% | 10.3% | 1.51× (late-cycle/peak) | 0.30 | earnings-driven (tool>cons) |
| CMDB | dry_bulk | $17.25 | 10.5× | $1.64 | $3.89 | 4.4× | +137% | 9.5% | 1.21× (elevated) | 0.40 | earnings-driven (tool>cons) |
| SB | dry_bulk | $6.39 | 8.0× | $0.80 | $1.74 | 3.7× | +118% | 12.5% | 1.41× (elevated) | 0.40 | earnings-driven (tool>cons) |
| ASC | product | $16.00 | 14.2× | $1.13 | $2.36 | 6.8× | +110% | 7.0% | 1.38× (elevated) | 0.40 | earnings-driven (tool>cons) |
| FLNG | lng | $29.70 | 14.5× | $2.05 | $3.74 | 7.9× | +83% | 6.9% | 0.71× (below-mid) | 0.60 | earnings-driven (tool>cons) |
| MPCC | containerships | $2.78 | 8.0× | $0.35 | $0.54 | 5.2× | +55% | 12.5% | 1.21× (elevated) | 0.40 | earnings-driven (tool>cons) |
| GSL | containerships | $38.99 | 3.8× | $10.26 | $14.04 | 2.8× | +37% | 26.3% | 1.45× (elevated) | 0.40 | earnings-driven (tool>cons) |
| SBLK | dry_bulk | $27.20 | 6.9× | $3.94 | $5.03 | 5.4× | +28% | 14.5% | 1.22× (elevated) | 0.40 | earnings-driven (tool>cons) |

_**(WHOLE-CO)** = hybrid name; the tool forward EPS here is the whole-company FFA strip (a proxy — the headline FV uses the crude+product carve-out aggregation)._


_Earnings-driven threshold: |gap| ≥ 25%. Near a cycle peak most names trip it on the high side by construction (FFA holds elevated rates; consensus normalises) — the signal is the **magnitude, direction, and cross-name pattern**, read alongside `w_earn`. Limitations: 1-year horizon only (strip is 8q + terminal NAV); EPS ≠ dividends (buyback channels like STNG are invisible); shipping consensus EPS is dispersed and lags spot. Directional cross-check, not a calibration target._
