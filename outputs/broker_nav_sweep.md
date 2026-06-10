# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, conservative independent), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). The **tool→broker spread** shows how much of a name's call is a genuine price-vs-value signal vs a NAV-mark choice — small for mark-validated pure-plays, wide for mark-uncertain names.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.40× | 1.24 | +30.9% | +52.4% | +73.9% | BUY→BUY | NAV>px→NAV>px | +43 | mark-driven |
| STNG | 0.70× | 1.37 | -3.3% | +13.1% | +29.4% | HOLD→BUY | $2,725,019→NAV>px | +33 | mark-driven |
| NAT | 0.85× | 1.98 | -44.9% | -8.9% | +27.2% | TRIM/SHORT→BUY | $334,239→NAV>px | +72 | mark-driven |
| ASC | 0.75× | 1.33 | -5.9% | +9.1% | +24.2% | TRIM/SHORT→BUY | $38,532→NAV>px | +30 | mark-driven |
| TNK | 0.76× | 1.34 | +4.1% | +14.0% | +23.9% | HOLD→BUY | NAV>px→NAV>px | +20 | mark-driven |
| TRMD | 0.83× | 1.24 | -5.4% | +8.1% | +21.7% | TRIM/SHORT→BUY | $68,988→NAV>px | +27 | mark-driven |
| CCEC | 0.90× | 0.96 | +35.3% | +27.3% | +19.2% | BUY→BUY | NAV>px→$2,977,992 | -16 | mark-driven |
| SBLK | 0.82× | 1.21 | -5.4% | +5.7% | +16.8% | TRIM/SHORT→BUY | $28,583→NAV>px | +22 | mark-driven |
| GNK | 0.87× | 1.04 | +7.2% | +9.7% | +12.1% | BUY→BUY | $18,314→$12,474 | +5 | mark-robust |
| INSW **(WHOLE-CO)** | 0.98× | 1.52 | -23.8% | -7.0% | +9.7% | TRIM/SHORT→BUY | $342,121→$67,887 | +33 | mark-driven |
| HAFN | 0.95× | 1.43 | -25.1% | -8.4% | +8.3% | TRIM/SHORT→BUY | $126,273→$28,673 | +33 | mark-driven |
| DHT | 1.09× | 1.14 | -8.1% | -2.0% | +4.0% | TRIM/SHORT→HOLD | $315,444→$168,393 | +12 | mark-driven |
| CMDB | 0.62× | 0.84 | +14.9% | +7.1% | -0.7% | BUY→HOLD | NAV>px→$1,070,509 | -16 | mark-driven |
| FRO | 1.20× | 1.12 | -14.9% | -9.0% | -3.0% | TRIM/SHORT→HOLD | $311,332→$214,599 | +12 | mark-driven |
| ECO | 1.21× | 1.12 | -17.5% | -11.9% | -6.2% | TRIM/SHORT→TRIM/SHORT | $299,660→$214,617 | +11 | mark-driven |
| FLNG | 1.37× | 0.87 | +0.1% | -10.4% | -21.0% | HOLD→TRIM/SHORT | $3,162,500→$3,162,500 | -21 | mark-driven |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_k_broker ≈ 1.0 ⇒ tool marks already reconcile to broker (validated). k_broker ≫ 1 ⇒ tool NAV sits well below broker; the name's apparent cheapness is largely a NAV-mark choice. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
