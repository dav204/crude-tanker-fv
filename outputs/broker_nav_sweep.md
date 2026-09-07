# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.33 | +43.3% | +72.3% | +101.4% | BUY→BUY | NAV>px→NAV>px | +58 | wide-spread |
| CCEC | 0.90× | 0.99 | +48.8% | +47.7% | +46.6% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.72× | 1.26 | -5.1% | +15.8% | +36.8% | TRIM/SHORT→BUY | $278,983→NAV>px | +42 | wide-spread |
| STNG | 0.73× | 1.60 | -6.8% | +13.8% | +34.5% | TRIM/SHORT→BUY | $110,143→NAV>px | +41 | wide-spread |
| GSL | 0.75× | 1.44 | -7.6% | +9.8% | +27.1% | TRIM/SHORT→BUY | $166,118→NAV>px | +35 | wide-spread |
| ASC | 0.75× | 1.37 | -9.9% | +6.3% | +22.4% | TRIM/SHORT→BUY | $36,712→NAV>px | +32 | wide-spread |
| TRMD | 0.92× | 1.16 | +1.7% | +9.6% | +17.4% | HOLD→BUY | $60,448→$25,445 | +16 | wide-spread |
| NAT | 0.85× | 2.55 | -58.7% | -24.0% | +10.7% | TRIM/SHORT→BUY | $751,639→NAV>px | +69 | wide-spread |
| TNK | 0.91× | 1.36 | -10.1% | -1.7% | +6.8% | TRIM/SHORT→BUY | $178,597→$13,683 | +17 | wide-spread |
| HAFN | 1.03× | 1.67 | -39.4% | -17.4% | +4.5% | TRIM/SHORT→HOLD | $184,356→$56,463 | +44 | wide-spread |
| BRUT | 1.03× | 1.00 | +1.9% | +1.5% | +1.1% | HOLD→HOLD | $223,241→$232,316 | -1 | narrow-spread |
| CMDB | 0.62× | 1.21 | -18.5% | -11.6% | -4.8% | TRIM/SHORT→HOLD | $37,814→$15,710 | +14 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.22 | -30.0% | -17.4% | -4.8% | TRIM/SHORT→TRIM/SHORT | $203,681→$34,167 | +25 | wide-spread |
| SBLK | 0.91× | 1.06 | -11.8% | -9.0% | -6.1% | TRIM/SHORT→TRIM/SHORT | $24,876→$14,480 | +6 | narrow-spread |
| MPCC | 1.04× | 1.21 | -26.1% | -16.7% | -7.4% | TRIM/SHORT→TRIM/SHORT | $203,957→$56,677 | +19 | wide-spread |
| DHT | 1.14× | 1.20 | -23.5% | -16.4% | -9.3% | TRIM/SHORT→TRIM/SHORT | $709,286→$410,360 | +14 | wide-spread |
| GNK | 0.95× | 1.12 | -22.3% | -17.1% | -11.9% | TRIM/SHORT→TRIM/SHORT | $44,779→$25,108 | +10 | wide-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.59 | -43.0% | -29.2% | -15.5% | TRIM/SHORT→TRIM/SHORT | $596,699→$300,165 | +28 | wide-spread |
| LPG | 1.06× | 1.50 | -42.3% | -30.0% | -17.7% | TRIM/SHORT→TRIM/SHORT | $360,145→$147,695 | +25 | wide-spread |
| FRO | 1.33× | 1.24 | -38.7% | -30.2% | -21.8% | TRIM/SHORT→TRIM/SHORT | $780,942→$520,857 | +17 | wide-spread |
| FLNG | 1.44× | 0.90 | -6.5% | -14.3% | -22.2% | TRIM/SHORT→TRIM/SHORT | $305,969→$554,093 | -16 | wide-spread |
| SB | 1.13× | 0.85 | -1.1% | -12.5% | -23.9% | HOLD→TRIM/SHORT | NAV>px→$63,901 | -23 | wide-spread |
| 2343 | 1.24× | 1.06 | -30.7% | -28.7% | -26.7% | TRIM/SHORT→TRIM/SHORT | $41,842→$37,563 | +4 | narrow-spread |
| BWLP | 1.27× | 1.14 | -38.7% | -33.7% | -28.8% | TRIM/SHORT→TRIM/SHORT | $244,312→$185,251 | +10 | narrow-spread |
| ECO | 1.47× | 1.18 | -41.6% | -35.9% | -30.2% | TRIM/SHORT→TRIM/SHORT | $709,243→$557,884 | +11 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
