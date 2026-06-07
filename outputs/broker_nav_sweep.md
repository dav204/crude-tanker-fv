# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, conservative independent), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). The **tool→broker spread** shows how much of a name's call is a genuine price-vs-value signal vs a NAV-mark choice — small for mark-validated pure-plays, wide for mark-uncertain names.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.40× | 1.17 | +12.2% | +25.4% | +38.6% | BUY→BUY | NAV>px→NAV>px | +26 | mark-driven |
| STNG | 0.70× | 1.31 | -2.9% | +10.8% | +24.4% | HOLD→BUY | NAV>px→NAV>px | +27 | mark-driven |
| ASC | 0.75× | 1.33 | -9.4% | +5.1% | +19.6% | TRIM/SHORT→BUY | $38,252→NAV>px | +29 | mark-driven |
| TRMD | 0.83× | 1.19 | -9.3% | +1.7% | +12.8% | TRIM/SHORT→BUY | $58,812→NAV>px | +22 | mark-driven |
| TNK | 0.76× | 1.19 | -2.1% | +2.9% | +8.0% | HOLD→BUY | NAV>px→NAV>px | +10 | mark-driven |
| CCEC | 0.90× | 0.96 | +20.8% | +13.1% | +5.3% | BUY→BUY | NAV>px→$2,977,992 | -15 | mark-driven |
| HAFN | 0.95× | 1.41 | -29.7% | -14.4% | +1.0% | TRIM/SHORT→HOLD | $123,511→$28,991 | +31 | mark-driven |
| NAT | 0.85× | 1.74 | -56.1% | -30.6% | -5.0% | TRIM/SHORT→TRIM/SHORT | $287,175→NAV>px | +51 | mark-driven |
| INSW **(WHOLE-CO)** | 0.98× | 1.37 | -33.2% | -22.1% | -11.1% | TRIM/SHORT→TRIM/SHORT | $303,978→$72,181 | +22 | mark-driven |
| DHT | 1.09× | 0.99 | -18.7% | -19.2% | -19.8% | TRIM/SHORT→TRIM/SHORT | $148,415→$165,372 | -1 | mark-robust |
| FLNG | 1.37× | 0.87 | -5.6% | -15.7% | -25.8% | TRIM/SHORT→TRIM/SHORT | $3,162,500→$3,162,500 | -20 | mark-driven |
| FRO | 1.20× | 1.00 | -30.8% | -30.8% | -30.9% | TRIM/SHORT→TRIM/SHORT | $207,932→$208,756 | -0 | mark-robust |
| ECO | 1.21× | 0.99 | -31.8% | -32.2% | -32.6% | TRIM/SHORT→TRIM/SHORT | $207,393→$215,201 | -1 | mark-robust |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_k_broker ≈ 1.0 ⇒ tool marks already reconcile to broker (validated). k_broker ≫ 1 ⇒ tool NAV sits well below broker; the name's apparent cheapness is largely a NAV-mark choice. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
