# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, conservative independent), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). The **tool→broker spread** shows how much of a name's call is a genuine price-vs-value signal vs a NAV-mark choice — small for mark-validated pure-plays, wide for mark-uncertain names.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.23 | +55.1% | +79.9% | +104.7% | BUY→BUY | NAV>px→NAV>px | +50 | mark-driven |
| STNG | 0.70× | 1.39 | -4.4% | +12.5% | +29.4% | HOLD→BUY | $2,725,019→NAV>px | +34 | mark-driven |
| NAT | 0.85× | 1.97 | -44.7% | -8.7% | +27.2% | TRIM/SHORT→BUY | $332,327→NAV>px | +72 | mark-driven |
| ASC | 0.75× | 1.37 | -8.4% | +7.8% | +24.1% | TRIM/SHORT→BUY | $43,825→NAV>px | +32 | mark-driven |
| TNK | 0.76× | 1.40 | +1.3% | +12.5% | +23.7% | HOLD→BUY | $47,855→NAV>px | +22 | mark-driven |
| TRMD | 0.83× | 1.27 | -8.6% | +6.3% | +21.2% | TRIM/SHORT→BUY | $78,345→NAV>px | +30 | mark-driven |
| CCEC | 0.90× | 0.96 | +38.1% | +28.8% | +19.5% | BUY→BUY | NAV>px→$2,977,992 | -19 | mark-driven |
| SBLK | 0.82× | 1.19 | -3.2% | +6.9% | +17.0% | HOLD→BUY | $25,856→NAV>px | +20 | mark-driven |
| GNK | 0.87× | 1.02 | +9.5% | +10.9% | +12.4% | BUY→BUY | $15,736→$12,398 | +3 | mark-robust |
| INSW **(WHOLE-CO)** | 0.98× | 1.61 | -28.0% | -9.5% | +9.0% | TRIM/SHORT→BUY | $393,378→$71,701 | +37 | mark-driven |
| HAFN | 0.95× | 1.38 | -21.7% | -6.4% | +8.9% | TRIM/SHORT→BUY | $113,530→$28,026 | +31 | mark-driven |
| DHT | 1.09× | 1.16 | -9.2% | -2.7% | +3.8% | TRIM/SHORT→HOLD | $330,771→$170,951 | +13 | mark-driven |
| CMDB | 0.62× | 0.84 | +15.0% | +7.1% | -0.7% | BUY→HOLD | NAV>px→$1,070,509 | -16 | mark-driven |
| FRO | 1.20× | 1.16 | -19.1% | -11.5% | -4.0% | TRIM/SHORT→HOLD | $354,881→$225,188 | +15 | mark-driven |
| ECO | 1.21× | 1.14 | -20.1% | -13.4% | -6.7% | TRIM/SHORT→TRIM/SHORT | $324,117→$220,611 | +13 | mark-driven |
| FLNG | 1.37× | 0.88 | -2.0% | -11.6% | -21.2% | HOLD→TRIM/SHORT | $3,162,500→$3,162,500 | -19 | mark-driven |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_k_broker ≈ 1.0 ⇒ tool marks already reconcile to broker (validated). k_broker ≫ 1 ⇒ tool NAV sits well below broker; the name's apparent cheapness is largely a NAV-mark choice. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
