# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.30 | +47.4% | +74.6% | +101.9% | BUY→BUY | NAV>px→NAV>px | +54 | wide-spread |
| CCEC | 0.90× | 1.00 | +48.3% | +47.4% | +46.4% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.71× | 1.27 | -2.7% | +19.0% | +40.7% | HOLD→BUY | $207,375→NAV>px | +43 | wide-spread |
| STNG | 0.71× | 1.55 | -1.7% | +18.4% | +38.4% | HOLD→BUY | $81,099→NAV>px | +40 | wide-spread |
| BRUT | 0.86× | 0.87 | +108.0% | +70.6% | +33.3% | BUY→BUY | NAV>px→NAV>px | -75 | wide-spread |
| GSL | 0.75× | 1.38 | -3.7% | +12.2% | +28.1% | HOLD→BUY | $106,820→NAV>px | +32 | wide-spread |
| TRMD | 0.86× | 1.15 | +9.7% | +17.7% | +25.8% | BUY→BUY | $43,444→$9,917 | +16 | wide-spread |
| ASC | 0.75× | 1.31 | -5.7% | +8.6% | +22.8% | TRIM/SHORT→BUY | $28,607→NAV>px | +28 | wide-spread |
| TNK | 0.80× | 1.53 | -5.4% | +7.6% | +20.6% | TRIM/SHORT→BUY | $130,174→NAV>px | +26 | wide-spread |
| HAFN | 0.92× | 1.55 | -22.6% | -2.7% | +17.2% | TRIM/SHORT→BUY | $126,841→$25,310 | +40 | wide-spread |
| NAT | 0.85× | 2.32 | -54.7% | -21.6% | +11.4% | TRIM/SHORT→BUY | $667,460→NAV>px | +66 | wide-spread |
| 2343 | 0.91× | 1.05 | +1.4% | +3.8% | +6.2% | HOLD→BUY | $14,262→$11,346 | +5 | narrow-spread |
| SB | 0.88× | 0.81 | +49.2% | +27.4% | +5.7% | BUY→BUY | NAV>px→NAV>px | -44 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.85× | 1.19 | -21.5% | -9.9% | +1.7% | TRIM/SHORT→BUY | $170,829→$28,253 | +23 | wide-spread |
| SBLK | 0.89× | 1.04 | -2.3% | -0.3% | +1.7% | HOLD→HOLD | $18,174→$13,478 | +4 | narrow-spread |
| CMDB | 0.62× | 1.03 | -2.0% | -0.7% | +0.7% | HOLD→HOLD | $18,716→$15,152 | +3 | narrow-spread |
| GNK | 0.92× | 1.09 | -12.4% | -7.6% | -2.9% | TRIM/SHORT→HOLD | $35,200→$19,356 | +9 | narrow-spread |
| DHT | 1.08× | 1.20 | -18.8% | -11.5% | -4.2% | TRIM/SHORT→HOLD | $585,846→$296,274 | +15 | wide-spread |
| MPCC | 1.04× | 1.20 | -27.5% | -17.9% | -8.4% | TRIM/SHORT→TRIM/SHORT | $214,768→$60,522 | +19 | wide-spread |
| LPG | 0.96× | 1.49 | -36.1% | -22.6% | -9.1% | TRIM/SHORT→TRIM/SHORT | $281,759→$72,178 | +27 | wide-spread |
| INSW **(WHOLE-CO)** | 1.17× | 1.55 | -39.7% | -26.0% | -12.3% | TRIM/SHORT→TRIM/SHORT | $536,654→$257,979 | +27 | wide-spread |
| FRO | 1.31× | 1.22 | -37.1% | -28.5% | -19.9% | TRIM/SHORT→TRIM/SHORT | $682,553→$451,717 | +17 | wide-spread |
| BWLP | 1.13× | 1.27 | -39.9% | -30.4% | -20.9% | TRIM/SHORT→TRIM/SHORT | $253,792→$138,973 | +19 | wide-spread |
| FLNG | 1.43× | 0.90 | -6.4% | -14.0% | -21.7% | TRIM/SHORT→TRIM/SHORT | $304,350→$546,338 | -15 | wide-spread |
| ECO | 1.34× | 1.21 | -37.6% | -30.6% | -23.7% | TRIM/SHORT→TRIM/SHORT | $623,698→$450,546 | +14 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
