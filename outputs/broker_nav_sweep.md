# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, conservative independent), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). The **tool→broker spread** shows how much of a name's call is a genuine price-vs-value signal vs a NAV-mark choice — small for mark-validated pure-plays, wide for mark-uncertain names.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.16 | +68.6% | +86.9% | +105.3% | BUY→BUY | NAV>px→NAV>px | +37 | mark-driven |
| CAPT | 0.67× | 1.04 | +38.2% | +43.1% | +48.0% | BUY→BUY | NAV>px→NAV>px | +10 | mark-robust |
| STNG | 0.70× | 1.38 | -4.0% | +12.7% | +29.4% | HOLD→BUY | $2,725,019→NAV>px | +33 | mark-driven |
| NAT | 0.85× | 1.96 | -44.4% | -8.5% | +27.3% | TRIM/SHORT→BUY | $329,458→NAV>px | +72 | mark-driven |
| ASC | 0.75× | 1.36 | -8.1% | +8.0% | +24.1% | TRIM/SHORT→BUY | $43,209→NAV>px | +32 | mark-driven |
| TNK | 0.76× | 1.39 | +1.7% | +12.7% | +23.8% | HOLD→BUY | $39,706→NAV>px | +22 | mark-driven |
| TRMD | 0.83× | 1.26 | -7.9% | +6.7% | +21.3% | TRIM/SHORT→BUY | $76,149→NAV>px | +29 | mark-driven |
| CCEC | 0.90× | 0.96 | +37.7% | +28.6% | +19.5% | BUY→BUY | NAV>px→$2,977,992 | -18 | mark-driven |
| SBLK | 0.82× | 1.21 | -5.3% | +5.8% | +16.8% | TRIM/SHORT→BUY | $28,367→NAV>px | +22 | mark-driven |
| GNK | 0.87× | 1.03 | +8.6% | +10.4% | +12.3% | BUY→BUY | $16,716→$12,427 | +4 | mark-robust |
| HAFN | 0.95× | 1.37 | -20.8% | -5.8% | +9.1% | TRIM/SHORT→BUY | $110,531→$27,874 | +30 | mark-driven |
| INSW **(WHOLE-CO)** | 0.98× | 1.61 | -28.0% | -9.5% | +9.0% | TRIM/SHORT→BUY | $392,822→$71,660 | +37 | mark-driven |
| DHT | 1.09× | 1.16 | -9.4% | -2.9% | +3.7% | TRIM/SHORT→HOLD | $334,603→$171,590 | +13 | mark-driven |
| CMDB | 0.62× | 0.86 | +12.6% | +6.0% | -0.7% | BUY→HOLD | NAV>px→$1,070,509 | -13 | mark-driven |
| FRO | 1.20× | 1.18 | -20.9% | -12.6% | -4.4% | TRIM/SHORT→HOLD | $375,677→$230,245 | +17 | mark-driven |
| ECO | 1.21× | 1.15 | -21.0% | -13.9% | -6.9% | TRIM/SHORT→TRIM/SHORT | $333,248→$222,848 | +14 | mark-driven |
| FLNG | 1.37× | 0.89 | -2.5% | -11.9% | -21.3% | HOLD→TRIM/SHORT | $3,162,500→$3,162,500 | -19 | mark-driven |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_k_broker ≈ 1.0 ⇒ tool marks already reconcile to broker (validated). k_broker ≫ 1 ⇒ tool NAV sits well below broker; the name's apparent cheapness is largely a NAV-mark choice. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
