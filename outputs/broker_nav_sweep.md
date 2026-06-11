# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, conservative independent), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). The **tool→broker spread** shows how much of a name's call is a genuine price-vs-value signal vs a NAV-mark choice — small for mark-validated pure-plays, wide for mark-uncertain names.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.25 | +51.7% | +78.0% | +104.3% | BUY→BUY | NAV>px→NAV>px | +53 | mark-driven |
| CAPT | 0.67× | 1.04 | +38.8% | +43.4% | +48.1% | BUY→BUY | NAV>px→NAV>px | +9 | mark-robust |
| STNG | 0.70× | 1.42 | -6.2% | +11.6% | +29.3% | TRIM/SHORT→BUY | $2,725,019→NAV>px | +36 | mark-driven |
| NAT | 0.85× | 2.00 | -45.6% | -9.3% | +27.0% | TRIM/SHORT→BUY | $339,977→NAV>px | +73 | mark-driven |
| ASC | 0.75× | 1.40 | -10.9% | +6.5% | +23.9% | TRIM/SHORT→BUY | $49,486→NAV>px | +35 | mark-driven |
| TNK | 0.76× | 1.44 | -0.5% | +11.6% | +23.6% | HOLD→BUY | $88,915→NAV>px | +24 | mark-driven |
| TRMD | 0.83× | 1.30 | -11.0% | +4.9% | +20.8% | TRIM/SHORT→BUY | $85,983→NAV>px | +32 | mark-driven |
| CCEC | 0.90× | 0.97 | +33.5% | +26.2% | +19.0% | BUY→BUY | NAV>px→$2,977,992 | -14 | mark-driven |
| SBLK | 0.82× | 1.21 | -5.0% | +6.0% | +16.9% | HOLD→BUY | $27,977→NAV>px | +22 | mark-driven |
| GNK | 0.87× | 1.03 | +8.1% | +10.2% | +12.2% | BUY→BUY | $17,309→$12,444 | +4 | mark-robust |
| HAFN | 0.95× | 1.39 | -22.5% | -6.9% | +8.8% | TRIM/SHORT→BUY | $116,528→$28,178 | +31 | mark-driven |
| INSW **(WHOLE-CO)** | 0.98× | 1.64 | -29.4% | -10.3% | +8.8% | TRIM/SHORT→BUY | $412,112→$73,095 | +38 | mark-driven |
| DHT | 1.09× | 1.18 | -10.9% | -3.7% | +3.4% | TRIM/SHORT→HOLD | $355,677→$175,108 | +14 | mark-driven |
| CMDB | 0.62× | 0.85 | +14.0% | +6.6% | -0.7% | BUY→HOLD | NAV>px→$1,070,509 | -15 | mark-driven |
| FRO | 1.20× | 1.20 | -22.9% | -13.9% | -4.8% | TRIM/SHORT→HOLD | $398,919→$235,896 | +18 | mark-driven |
| ECO | 1.21× | 1.17 | -22.2% | -14.7% | -7.1% | TRIM/SHORT→TRIM/SHORT | $346,455→$226,085 | +15 | mark-driven |
| FLNG | 1.37× | 0.89 | -4.4% | -12.9% | -21.5% | HOLD→TRIM/SHORT | $3,162,500→$3,162,500 | -17 | mark-driven |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_k_broker ≈ 1.0 ⇒ tool marks already reconcile to broker (validated). k_broker ≫ 1 ⇒ tool NAV sits well below broker; the name's apparent cheapness is largely a NAV-mark choice. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
