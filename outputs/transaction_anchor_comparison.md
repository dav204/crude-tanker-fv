# Transaction-anchor recalibration — comparison

Each name valued twice: with the existing curve (baseline) and with the mid-age leg of every class with a populated transactions file recalibrated to disclosed S&P prints (recency-weighted, ~15mo half-life; quality-flag uplifts: financing +5%, distressed +10%). Newbuild + old-age anchors are left unchanged. Toggle: `use_transaction_anchored=True`.

## Transaction inputs in scope

- **Aframax** (7 prints, as_of 2026-05-29):
  - 2026-01-15 • age 10 • $47.2M, financing (+5%) • TNK Q1 2026 ER (3-vessel 2016-built package, $141.5M total)
  - 2026-03-15 • age 8 • $71.0M • trade press (Splash247 / TradeWinds market commentary, Mar 2026)
  - 2025-08-01 • age 7 • $73.5M • trade press summary (LR2-spec, $73-74M)
  - 2026-04-16 • age 16 • $42.65M • Performance Shipping (PSHG) Form 6-K — sale of M/T P. Aliki to Trafigura
  - 2026-02-01 • age 17 • $35.65M • Performance Shipping (PSHG) press release — sale of M/T P. Sophia
  - 2025-04-01 • age 14 • $39.0M • Performance Shipping (PSHG) press release — sale of M/T P. Yanbu
  - 2026-02-15 • age 11 • $70.0M • Compass Maritime weekly report — sale of STI Condotti
- **LR2** (1 prints, as_of 2026-05-29):
  - 2026-03-31 • age 10 • $52.3M • Scorpio Tankers (STNG) press release Dec 2025; closing Q1 2026
- **MR** (6 prints, as_of 2026-05-29):
  - 2026-03-31 • age 12 • $32.0M • Scorpio Tankers (STNG) press release Nov 2025; closing Q1 2026
  - 2026-06-30 • age 11 • $35.0M • Scorpio Tankers (STNG) 6-K — closing Q2 2026
  - 2026-02-15 • age 0 • $49.5M • Compass Maritime weekly report (Feb 2026)
  - 2025-11-15 • age 0 • $45.0M, newbuild_resale (+0%) • Scorpio Tankers (STNG) press release Nov 2025
  - 2026-01-23 • age -3 • $45.4M • d'Amico (DIS) press release / Splash247
  - 2025-12-15 • age -3 • $43.2M • d'Amico (DIS) press release / Marine Link
- **Suezmax** (11 prints, as_of 2026-05-29):
  - 2026-05-15 • age 17 • $53.5M • TNK Q2 2026 ER (subsequent-events disclosure — disposal of 2009-built Suezmax)
  - 2025-08-15 • age 6 • $96.0M • trade press (Splash247 / TradeWinds S&P column, Aug 2025 — modern Suezmax market commentary)
  - 2025-10-15 • age 8 • $88.0M • trade press (Hellenic Shipping News / Splash247 weekly S&P, Oct 2025)
  - 2025-12-15 • age 10 • $83.0M • trade press (TradeWinds S&P column, Q4 2025)
  - 2026-03-15 • age 12 • $73.0M • trade press (Splash247 / Hellenic Shipping News market summary, Q1 2026)
  - 2026-04-15 • age 11.5 • $70.0M • Frontline (FRO) Q2 2026 disclosure (Front Ull + Front Idun sale)
  - 2026-02-15 • age 18 • $36.5M • TNK Q1 2026 ER (2-vessel package, 2007+2009-built, $73M total / $36.5M avg)
  - 2026-01-31 • age 21 • $25.0M • NAT Q1 2026 ER / press release (2-vessel package, 2004+2005-built, $50M total / $25M avg)
  - 2026-01-15 • age 0 • $99.3M, newbuild_resale (+0%) • Compass Maritime weekly (Arctic Star + Tromso Star NB resale)
  - 2026-02-15 • age 0 • $95.0M, newbuild_resale (+0%) • Compass Maritime weekly (Olympic Star + Daehan Hull 5118 NB resale)
  - 2026-03-02 • age -2.5 • $81.5M • Performance Shipping (PSHG) press release (2x Suezmax NB order at SWS)
- **VLCC** (7 prints, as_of 2026-05-29):
  - 2026-01-15 • age 4 • $125.0M • trade press (Splash247 — two 4-yr-old VLCCs sold to European buyer)
  - 2026-01-31 • age 5 • $112.0M • Splash247 (CSSC Liaoning sale to Greek interests)
  - 2026-03-15 • age 10.5 • $103.9M • Frontline (FRO) Q1 2026 ER (8-VLCC en bloc disposal)
  - 2026-02-15 • age 13 • $84.5M • Teekay Tankers (TNK) Q1 2026 ER / Splash247 (VLCC-sector exit)
  - 2026-02-28 • age 14 • $89.0M • CMB.TECH press release / Splash247 (Ingrid + Ilma sale to Sinokor)
  - 2026-03-31 • age 12 • $71.0M • Veson / IndexBox (Sinokor 2026 VLCC buying campaign Q1 summary)
  - 2026-01-08 • age 0 • $136.0M, newbuild_resale (+0%) • Frontline (FRO) press release / Splash247 (9 latest-gen ECO VLCC NBs from Fredriksen affiliate)

## Per-name impact

| Name | NAV base→txn | Δ% | EV base→txn | Δpp | Position |
|---|--:|--:|--:|--:|---|
| CCEC | $28.10→$28.10 | +0.0% | +20.8%→+20.8% | +0.0 | BUY→BUY |
| TEN | $88.56→$85.29 | -3.7% | +12.2%→+8.1% | -4.1 | BUY→BUY |
| ASC | $15.96→$17.32 | +8.5% | -9.4%→-1.9% | +7.4 | TRIM/SHORT→HOLD ⚠️ |
| STNG | $83.87→$83.03 | -1.0% | -2.9%→-3.9% | -1.0 | HOLD→HOLD |
| TNK | $83.32→$80.83 | -3.0% | -2.1%→-4.1% | -2.0 | HOLD→HOLD |
| FLNG | $28.45→$28.45 | +0.0% | -5.6%→-5.6% | +0.0 | TRIM/SHORT→TRIM/SHORT |
| TRMD | $26.74→$27.45 | +2.7% | -9.3%→-7.0% | +2.3 | TRIM/SHORT→TRIM/SHORT |
| DHT | $15.29→$13.53 | -11.5% | -18.7%→-26.9% | -8.2 | TRIM/SHORT→TRIM/SHORT |
| HAFN | $5.34→$5.52 | +3.5% | -29.7%→-27.5% | +2.2 | TRIM/SHORT→TRIM/SHORT |
| INSW **(WHOLE-CO)** | $57.91→$56.74 | -2.0% | -33.2%→-34.3% | -1.0 | TRIM/SHORT→TRIM/SHORT |
| FRO | $28.79→$26.21 | -8.9% | -30.8%→-37.0% | -6.2 | TRIM/SHORT→TRIM/SHORT |
| ECO | $39.93→$36.50 | -8.6% | -31.8%→-37.2% | -5.4 | TRIM/SHORT→TRIM/SHORT |
| NAT | $2.63→$2.64 | +0.2% | -56.1%→-56.1% | +0.1 | TRIM/SHORT→TRIM/SHORT |

_Δ% = (txn − base) / base. Names with no exposure to a recalibrated class show Δ ≈ 0 — useful as a control. ⚠️ flags a position-call flip._

_**(WHOLE-CO)** = hybrid name valued via crude + product carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2)._
