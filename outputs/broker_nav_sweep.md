# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.22 | +58.9% | +80.8% | +102.6% | BUY→BUY | NAV>px→NAV>px | +44 | wide-spread |
| BRUT | 0.72× | 0.97 | +61.8% | +54.8% | +47.7% | BUY→BUY | NAV>px→NAV>px | -14 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.2% | +47.9% | +46.7% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.69× | 1.19 | +11.0% | +27.9% | +44.8% | BUY→BUY | $53,520→NAV>px | +34 | wide-spread |
| STNG | 0.69× | 1.56 | +0.8% | +21.6% | +42.4% | HOLD→BUY | $68,460→NAV>px | +42 | wide-spread |
| TRMD | 0.82× | 1.14 | +15.9% | +24.1% | +32.2% | BUY→BUY | $33,992→NAV>px | +16 | wide-spread |
| TNK | 0.73× | 1.53 | +3.5% | +17.6% | +31.7% | HOLD→BUY | $49,193→NAV>px | +28 | wide-spread |
| GSL | 0.75× | 1.29 | +4.0% | +17.0% | +30.0% | HOLD→BUY | NAV>px→NAV>px | +26 | wide-spread |
| HAFN | 0.86× | 1.48 | -12.5% | +6.9% | +26.4% | TRIM/SHORT→BUY | $95,853→$7,832 | +39 | wide-spread |
| ASC | 0.75× | 1.26 | -1.8% | +10.7% | +23.1% | HOLD→BUY | $21,702→NAV>px | +25 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.23 | -14.2% | +1.9% | +18.0% | TRIM/SHORT→BUY | $120,740→NAV>px | +32 | wide-spread |
| SBLK | 0.78× | 1.08 | +6.8% | +11.2% | +15.6% | BUY→BUY | $8,480→NAV>px | +9 | narrow-spread |
| NAT | 0.85× | 2.22 | -52.6% | -20.6% | +11.4% | TRIM/SHORT→BUY | $617,242→NAV>px | +64 | wide-spread |
| SB | 0.88× | 0.88 | +27.8% | +16.0% | +4.2% | BUY→HOLD | NAV>px→NAV>px | -24 | wide-spread |
| LPG | 0.84× | 1.53 | -28.9% | -12.5% | +3.8% | TRIM/SHORT→HOLD | $208,723→NAV>px | +33 | wide-spread |
| CMDB | 0.62× | 0.87 | +13.7% | +7.8% | +1.9% | BUY→HOLD | NAV>px→$14,626 | -12 | wide-spread |
| GNK | 0.89× | 1.10 | -10.2% | -5.0% | +0.3% | TRIM/SHORT→HOLD | $31,418→$14,250 | +11 | wide-spread |
| 2343 | 0.98× | 0.98 | +1.4% | +0.4% | -0.7% | HOLD→HOLD | $14,262→$15,478 | -2 | narrow-spread |
| MPCC | 1.04× | 1.11 | -18.8% | -12.6% | -6.5% | TRIM/SHORT→TRIM/SHORT | $136,966→$48,452 | +12 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.53 | -35.7% | -21.7% | -7.7% | TRIM/SHORT→TRIM/SHORT | $468,801→$201,602 | +28 | wide-spread |
| BWLP | 0.97× | 1.35 | -34.5% | -21.4% | -8.3% | TRIM/SHORT→TRIM/SHORT | $207,795→$61,942 | +26 | wide-spread |
| DHT | 1.14× | 1.09 | -15.2% | -11.8% | -8.4% | TRIM/SHORT→TRIM/SHORT | $489,951→$361,780 | +7 | narrow-spread |
| FLNG | 1.35× | 0.88 | +4.0% | -6.4% | -16.8% | HOLD→TRIM/SHORT | $135,338→$442,649 | -21 | wide-spread |
| FRO | 1.37× | 1.09 | -30.3% | -26.3% | -22.3% | TRIM/SHORT→TRIM/SHORT | $540,231→$442,731 | +8 | narrow-spread |
| ECO | 1.35× | 1.14 | -34.1% | -29.1% | -24.1% | TRIM/SHORT→TRIM/SHORT | $549,197→$431,507 | +10 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
