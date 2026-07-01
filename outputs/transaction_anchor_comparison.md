# Transaction-anchor recalibration — comparison

Each name valued twice: with the existing curve (baseline) and with the mid-age leg of every class with a populated transactions file recalibrated to disclosed S&P prints (recency-weighted, ~15mo half-life; quality-flag uplifts: financing +5%, distressed +10%). Newbuild + old-age anchors are left unchanged. Toggle: `use_transaction_anchored=True`.

## Transaction inputs in scope

- **Aframax** (13 prints, as_of 2026-06-12):
  - 2026-01-15 • age 10 • $47.2M, financing (+5%) • TNK Q1 2026 ER (3-vessel 2016-built package, $141.5M total)
  - 2026-03-15 • age 8 • $71.0M • trade press (Splash247 / TradeWinds market commentary, Mar 2026)
  - 2025-08-01 • age 7 • $73.5M • trade press summary (LR2-spec, $73-74M)
  - 2026-04-16 • age 16 • $42.65M • Performance Shipping (PSHG) Form 6-K — sale of M/T P. Aliki to Trafigura
  - 2026-02-01 • age 17 • $35.65M • Performance Shipping (PSHG) press release — sale of M/T P. Sophia
  - 2025-04-01 • age 14 • $39.0M • Performance Shipping (PSHG) press release — sale of M/T P. Yanbu
  - 2026-02-15 • age 11 • $70.0M • Compass Maritime weekly report — sale of STI Condotti
  - 2025-01-24 • age 15 • $33.8M • Pareto Shipping Daily 2025-01-24 — broker reports
  - 2025-01-31 • age 15 • $37.0M • Pareto Shipping Daily 2025-01-31 — broker reports
  - 2025-04-30 • age 15 • $33.5M • Pareto Shipping Daily 2025-04-30 — broker reports
  - 2025-06-19 • age 17 • $31.0M • Pareto Shipping Daily 2025-06-19 — Yasa disclosure
  - 2025-09-23 • age 17 • $29.5M • Pareto Shipping Daily 2025-09-23 — broker reports
  - 2026-06-12 • age 17 • $52.5M • MB Shipbrokers Tanker Weekly 24/2026 — S&P column
- **Cape** (30 prints, as_of 2026-06-09):
  - 2025-12-15 • age 5 • $73.5M • Pareto Shipping Daily 2025-12-17 — broker reports
  - 2026-01-09 • age 5 • $76.25M • Pareto Shipping Daily 2026-01-09 — Norden disclosure
  - 2025-09-26 • age 5 • $69.67M • Pareto Shipping Daily 2025-09-26 — 2020 Bulkers disclosure
  - 2025-09-26 • age 6 • $69.67M • Pareto Shipping Daily 2025-09-26 — 2020 Bulkers disclosure
  - 2025-09-26 • age 6 • $69.67M • Pareto Shipping Daily 2025-09-26 — 2020 Bulkers disclosure
  - 2025-06-20 • age 6 • $64.0M • Pareto Shipping Daily 2025-06-20 — broker reports
  - 2026-04-16 • age 7 • $65.0M • GNK Q1 2026 10-Q (accession 0001104659-26-056337) — subsequent-events note; first reported Pareto Shipping Daily 2026-04-21
  - 2025-11-15 • age 5 • $72.75M • GNK Q1 2026 10-Q Note 5 — 2x Newcastlemax purchase agreement
  - 2025-11-15 • age 5 • $72.75M • GNK Q1 2026 10-Q Note 5 — 2x Newcastlemax purchase agreement
  - 2025-07-10 • age 5 • $63.55M • GNK Q1 2026 10-Q Note 5 — Capesize purchase agreement
  - 2026-06-05 • age 17 • $30.0M • Pareto Shipping Daily 2026-06-05 — Maran disclosure
  - 2025-10-06 • age 6 • $65.5M • Pareto Shipping Daily 2025-10-06 — broker reports
  - 2025-08-15 • age 9 • $55.0M • Pareto Shipping Daily 2025-08-18 — broker reports
  - 2025-08-15 • age 10 • $55.0M • Pareto Shipping Daily 2025-08-18 — broker reports
  - 2025-08-15 • age 10 • $55.0M • Pareto Shipping Daily 2025-08-18 — broker reports
  - 2025-05-22 • age 10 • $51.0M • Pareto Shipping Daily 2025-05-22 — Oldendorff disclosure
  - 2025-09-19 • age 12 • $37.0M • Pareto Shipping Daily 2025-09-19 — broker reports
  - 2025-05-22 • age 14 • $29.0M • Pareto Shipping Daily 2025-05-22 — Enesel disclosure
  - 2025-09-15 • age 14 • $25.0M • Pareto Shipping Daily 2025-09-15 — broker reports
  - 2025-03-12 • age 15 • $27.5M • Pareto Shipping Daily 2025-03-12 — EPS disclosure
  - 2025-03-12 • age 15 • $27.0M • Pareto Shipping Daily 2025-03-12 — EPS disclosure
  - 2025-09-15 • age 15 • $26.5M • Pareto Shipping Daily 2025-09-15 — broker reports
  - 2025-10-02 • age 16 • $24.8M • Pareto Shipping Daily 2025-10-02 — CMB.TECH (Bocimar) disclosure
  - 2025-10-02 • age 16 • $24.8M • Pareto Shipping Daily 2025-10-02 — CMB.TECH (Bocimar) disclosure
  - 2025-10-21 • age 16 • $25.5M • Pareto Shipping Daily 2025-10-21 — broker reports
  - 2025-10-22 • age 16 • $26.2M • Pareto Shipping Daily 2025-10-22 — broker reports
  - 2025-10-21 • age 19 • $25.0M • Pareto Shipping Daily 2025-10-21 — broker reports
  - 2026-03-02 • age 20 • $26.0M • Pareto Shipping Daily 2026-03-02 — broker reports
  - 2026-03-10 • age 19 • $23.0M • Pareto Shipping Daily 2026-03-10 — broker reports
  - 2026-06-05 • age 18 • $30.0M • Pareto Shipping Daily 2026-06-05 — Maran disclosure
- **LR2** (12 prints, as_of 2026-06-09):
  - 2026-03-31 • age 10 • $52.3M • Scorpio Tankers (STNG) press release Dec 2025; closing Q1 2026
  - 2026-03-31 • age 10 • $52.3M • Scorpio Tankers (STNG) press release Dec 2025; closing Q1 2026
  - 2025-01-10 • age 13 • $45.3M • Pareto Shipping Daily 2025-01-10 — Affinity broker reports
  - 2025-03-14 • age 17 • $35.0M • Pareto Shipping Daily 2025-03-14 — broker reports
  - 2025-08-26 • age 16 • $32.0M • Pareto Shipping Daily 2025-08-26 — broker reports
  - 2026-01-13 • age 11 • $57.5M • Pareto Shipping Daily 2026-01-13 — Scorpio Tankers disclosure
  - 2026-03-04 • age 17 • $41.0M • Pareto Shipping Daily 2026-03-04 — broker reports
  - 2026-03-06 • age 11 • $60.0M • Pareto Shipping Daily 2026-03-06 — Scorpio Tankers disclosure
  - 2026-04-21 • age 12 • $65.0M • Pareto Shipping Daily 2026-04-21 — Scorpio Tankers disclosure
  - 2026-04-21 • age 12 • $65.0M • Pareto Shipping Daily 2026-04-21 — Scorpio Tankers disclosure
  - 2026-04-21 • age 12 • $65.0M • Pareto Shipping Daily 2026-04-21 — Scorpio Tankers disclosure
  - 2026-06-12 • age 0 • $90.0M, newbuild_resale (+0%) • MB Shipbrokers Tanker Weekly 24/2026 — S&P column
- **MR** (25 prints, as_of 2026-06-09):
  - 2026-03-31 • age 12 • $32.0M • Scorpio Tankers (STNG) press release Nov 2025; closing Q1 2026
  - 2026-06-30 • age 11 • $35.0M • Scorpio Tankers (STNG) 6-K — closing Q2 2026
  - 2025-03-21 • age 5 • $40.0M • Pareto Shipping Daily 2025-03-21 — Union Maritime disclosure
  - 2025-08-29 • age 5 • $42.0M • Pareto Shipping Daily 2025-08-29 — broker reports
  - 2026-03-04 • age 6 • $44.0M • Pareto Shipping Daily 2026-03-04 — NORDEN disclosure
  - 2026-03-04 • age 6 • $44.0M • Pareto Shipping Daily 2026-03-04 — NORDEN disclosure
  - 2026-03-04 • age 9 • $38.0M • Pareto Shipping Daily 2026-03-04 — broker reports
  - 2025-11-11 • age 10 • $32.0M • Pareto Shipping Daily 2025-11-11 — Latsco disclosure
  - 2026-04-21 • age 12 • $35.0M • Pareto Shipping Daily 2026-04-21 — Scorpio Tankers disclosure
  - 2026-04-21 • age 12 • $35.0M • Pareto Shipping Daily 2026-04-21 — Scorpio Tankers disclosure
  - 2026-04-21 • age 12 • $35.0M • Pareto Shipping Daily 2026-04-21 — Scorpio Tankers disclosure
  - 2026-01-19 • age 13 • $29.5M • Pareto Shipping Daily 2026-01-19 — broker reports
  - 2026-01-27 • age 14 • $27.0M • Pareto Shipping Daily 2026-01-27 — broker reports
  - 2026-03-26 • age 14 • $27.6M • Pareto Shipping Daily 2026-03-26 — d'Amico disclosure
  - 2025-06-24 • age 14 • $18.15M • Pareto Shipping Daily 2025-06-24 — d'Amico disclosure
  - 2025-06-24 • age 14 • $18.15M • Pareto Shipping Daily 2025-06-24 — d'Amico disclosure
  - 2025-09-03 • age 14 • $18.2M • Pareto Shipping Daily 2025-09-03 — broker reports
  - 2025-11-28 • age 14 • $19.5M • Pareto Shipping Daily 2025-11-28 — d'Amico disclosure
  - 2025-01-16 • age 17 • $21.0M • Pareto Shipping Daily 2025-01-16 — broker reports
  - 2025-12-17 • age 17 • $16.0M • Pareto Shipping Daily 2025-12-17 — INSW disclosure
  - 2025-12-17 • age 17 • $16.0M • Pareto Shipping Daily 2025-12-17 — INSW disclosure
  - 2026-02-15 • age 0 • $49.5M • Compass Maritime weekly report (Feb 2026)
  - 2025-11-15 • age 0 • $45.0M, newbuild_resale (+0%) • Scorpio Tankers (STNG) press release Nov 2025
  - 2026-01-23 • age -3 • $45.4M • d'Amico (DIS) press release / Splash247
  - 2025-12-15 • age -3 • $43.2M • d'Amico (DIS) press release / Marine Link
- **Pana** (8 prints, as_of 2026-06-12):
  - 2025-09-19 • age 9 • $27.5M • Pareto Shipping Daily 2025-09-19 — broker reports
  - 2025-10-06 • age 9 • $26.5M • Pareto Shipping Daily 2025-10-06 — broker reports
  - 2026-06-12 • age 11 • $26.0M • MB Shipbrokers Dry Bulk Weekly 24/2026 — S&P table
  - 2025-06-17 • age 15 • $11.8M • Pareto Shipping Daily 2025-06-17 — Diana disclosure
  - 2025-04-28 • age 17 • $14.25M • Pareto Shipping Daily 2025-04-28 — Thenamaris disclosure
  - 2025-11-14 • age 0 • $35.0M, newbuild_resale (+0%) • Pareto Shipping Daily 2025-11-14 — broker reports
  - 2026-06-05 • age 2 • $42.7M • Pareto Shipping Daily 2026-06-05 — broker reports
  - 2026-06-12 • age 21 • $12.1M • MB Shipbrokers Dry Bulk Weekly 24/2026 — S&P table
- **Suezmax** (24 prints, as_of 2026-06-09):
  - 2026-05-15 • age 17 • $53.5M • TNK Q2 2026 ER (subsequent-events disclosure — disposal of 2009-built Suezmax)
  - 2025-08-15 • age 6 • $96.0M • trade press (Splash247 / TradeWinds S&P column, Aug 2025 — modern Suezmax market commentary)
  - 2025-10-15 • age 8 • $88.0M • trade press (Hellenic Shipping News / Splash247 weekly S&P, Oct 2025)
  - 2025-12-15 • age 10 • $83.0M • trade press (TradeWinds S&P column, Q4 2025)
  - 2026-03-15 • age 12 • $73.0M • trade press (Splash247 / Hellenic Shipping News market summary, Q1 2026)
  - 2026-04-15 • age 11.5 • $70.0M • Frontline (FRO) Q2 2026 disclosure (Front Ull + Front Idun sale)
  - 2025-10-09 • age 6 • $76.0M • Pareto Shipping Daily 2025-10-09 — Performance Shipping disclosure
  - 2025-10-09 • age 6 • $76.0M • Pareto Shipping Daily 2025-10-09 — Performance Shipping disclosure
  - 2025-06-20 • age 8 • $66.0M • Pareto Shipping Daily 2025-06-20 — broker reports
  - 2025-08-19 • age 11 • $38.0M • Pareto Shipping Daily 2025-08-19 — broker reports
  - 2025-08-28 • age 15 • $40.0M • Pareto Shipping Daily 2025-08-28 — broker reports
  - 2025-08-29 • age 16 • $40.0M • Pareto Shipping Daily 2025-08-29 — broker reports
  - 2025-10-09 • age 13 • $44.0M • Pareto Shipping Daily 2025-10-09 — Eastern Pacific disclosure
  - 2025-11-20 • age 12 • $58.0M • Pareto Shipping Daily 2025-11-20 — Stena disclosure
  - 2025-05-22 • age 16 • $36.4M • Pareto Shipping Daily 2025-05-22 — Advantage Tankers disclosure
  - 2025-03-14 • age 16 • $40.0M • Pareto Shipping Daily 2025-03-14 — broker reports (Tsakos disposal)
  - 2026-02-16 • age 17 • $46.0M • Pareto Shipping Daily 2026-02-16 — Maran disclosure
  - 2026-05-05 • age 15 • $67.0M • Pareto Shipping Daily 2026-05-05 — CMBT disclosure
  - 2026-05-11 • age 15 • $67.0M • Pareto Shipping Daily 2026-05-11 — broker reports
  - 2026-02-15 • age 18 • $36.5M • TNK Q1 2026 ER (2-vessel package, 2007+2009-built, $73M total / $36.5M avg)
  - 2026-01-31 • age 21 • $25.0M • NAT Q1 2026 ER / press release (2-vessel package, 2004+2005-built, $50M total / $25M avg)
  - 2026-01-15 • age 0 • $99.3M, newbuild_resale (+0%) • Compass Maritime weekly (Arctic Star + Tromso Star NB resale)
  - 2026-02-15 • age 0 • $95.0M, newbuild_resale (+0%) • Compass Maritime weekly (Olympic Star + Daehan Hull 5118 NB resale)
  - 2026-03-02 • age -2.5 • $81.5M • Performance Shipping (PSHG) press release (2x Suezmax NB order at SWS)
- **Supra-Ultra** (26 prints, as_of 2026-06-12):
  - 2025-09-19 • age 4 • $32.0M • Pareto Shipping Daily 2025-09-19 — CMB → HMM disclosure
  - 2025-09-19 • age 5 • $30.0M • Pareto Shipping Daily 2025-09-19 — broker reports
  - 2025-10-06 • age 6 • $30.5M • Pareto Shipping Daily 2025-10-06 — broker reports
  - 2025-10-06 • age 10 • $23.2M • Pareto Shipping Daily 2025-10-06 — broker reports
  - 2025-09-19 • age 5 • $32.0M • Pareto Shipping Daily 2025-09-19 — CMB → HMM disclosure
  - 2025-09-16 • age 9 • $26.5M • Pareto Shipping Daily 2025-09-19 — Diana disclosure
  - 2025-08-05 • age 9 • $21.0M • Pareto Shipping Daily 2025-08-05 — Belships disclosure
  - 2025-08-05 • age 9 • $21.0M • Pareto Shipping Daily 2025-08-05 — Belships disclosure
  - 2025-08-05 • age 9 • $21.0M • Pareto Shipping Daily 2025-08-05 — Belships disclosure
  - 2025-08-05 • age 10 • $21.0M • Pareto Shipping Daily 2025-08-05 — Belships disclosure
  - 2025-04-28 • age 10 • $20.0M • Pareto Shipping Daily 2025-04-28 — broker reports
  - 2025-01-14 • age 12 • $19.5M • Pareto Shipping Daily 2025-01-14 — broker reports
  - 2025-09-19 • age 13 • $18.0M • Pareto Shipping Daily 2025-09-19 — broker reports
  - 2026-02-03 • age 14 • $19.6M • SBLK Q1 2026 6-K (accession 0000950157-26-000639) — Star Stonington sale
  - 2025-01-14 • age 14 • $15.0M • Pareto Shipping Daily 2025-01-14 — broker reports
  - 2025-06-25 • age 14 • $12.8M • Pareto Shipping Daily 2025-06-25 — broker reports
  - 2025-08-05 • age 14 • $14.25M • Pareto Shipping Daily 2025-08-05 — broker reports
  - 2025-08-05 • age 15 • $14.25M • Pareto Shipping Daily 2025-08-05 — broker reports
  - 2025-06-11 • age 16 • $11.3M • Pareto Shipping Daily 2025-06-11 — broker reports / VesselsValue
  - 2025-04-28 • age 17 • $12.25M • Pareto Shipping Daily 2025-04-28 — Thenamaris disclosure
  - 2026-06-12 • age 14 • $13.7M • MB Shipbrokers Dry Bulk Weekly 24/2026 — S&P table
  - 2026-06-12 • age 16 • $17.2M • MB Shipbrokers Dry Bulk Weekly 24/2026 — S&P table
  - 2025-03-17 • age 19 • $9.3M • Pareto Shipping Daily 2025-03-17 — SBLK disclosure
  - 2026-02-24 • age 21 • $10.6M • GNK Q1 2026 10-Q Note 5 — sale of Genco Picardy
  - 2026-02-24 • age 21 • $10.6M • GNK Q1 2026 10-Q Note 5 — sale of Genco Predator
  - 2026-06-12 • age 22 • $10.0M • MB Shipbrokers Dry Bulk Weekly 24/2026 — S&P table
- **VLCC** (12 prints, as_of 2026-06-09):
  - 2026-01-15 • age 4 • $125.0M • trade press (Splash247 — two 4-yr-old VLCCs sold to European buyer)
  - 2026-01-31 • age 5 • $112.0M • Splash247 (CSSC Liaoning sale to Greek interests)
  - 2026-03-15 • age 10.5 • $103.9M • Frontline (FRO) Q1 2026 ER (8-VLCC en bloc disposal)
  - 2026-02-15 • age 13 • $84.5M • Teekay Tankers (TNK) Q1 2026 ER / Splash247 (VLCC-sector exit)
  - 2026-02-28 • age 14 • $89.0M • CMB.TECH press release / Splash247 (Ingrid + Ilma sale to Sinokor)
  - 2025-04-25 • age 5 • $102.5M • Pareto Shipping Daily 2025-04-25 — broker reports
  - 2025-04-25 • age 6 • $102.5M • Pareto Shipping Daily 2025-04-25 — broker reports
  - 2025-10-09 • age 6 • $103.0M • Pareto Shipping Daily 2025-10-09 — broker reports
  - 2025-03-19 • age 14 • $55.0M • Pareto Shipping Daily 2025-03-19 — broker reports
  - 2025-03-07 • age 16 • $52.0M • Pareto Shipping Daily 2025-03-07 — broker reports
  - 2026-03-31 • age 12 • $71.0M • Veson / IndexBox (Sinokor 2026 VLCC buying campaign Q1 summary)
  - 2026-01-08 • age 0 • $136.0M, newbuild_resale (+0%) • Frontline (FRO) press release / Splash247 (9 latest-gen ECO VLCC NBs from Fredriksen affiliate)

## Per-name impact

| Name | NAV base→txn | Δ% | EV base→txn | Δpp | Position |
|---|--:|--:|--:|--:|---|
| BRUT | $8.80→$8.80 | +0.0% | +99.0%→+96.6% | -2.4 | BUY→BUY |
| TEN | $96.95→$88.70 | -8.5% | +100.3%→+85.2% | -15.2 | BUY→BUY |
| CCEC | $28.10→$28.10 | +0.0% | +68.2%→+68.2% | +0.0 | BUY→BUY |
| SB | $9.72→$10.12 | +4.1% | +47.1%→+53.4% | +6.2 | BUY→BUY |
| CAPT | $15.61→$15.49 | -0.7% | +38.4%→+36.4% | -2.0 | BUY→BUY |
| CMDB | $32.12→$31.33 | -2.4% | +19.0%→+16.3% | -2.7 | BUY→BUY |
| CMBT **(WHOLE-CO)** | $15.84→$15.87 | +0.2% | +14.9%→+14.9% | -0.1 | BUY→BUY |
| SBLK | $29.77→$29.34 | -1.4% | +15.0%→+13.6% | -1.4 | BUY→BUY |
| TNK | $83.32→$77.51 | -7.0% | +19.5%→+12.4% | -7.1 | BUY→BUY |
| FLNG | $28.45→$28.45 | +0.0% | +9.3%→+9.3% | +0.0 | BUY→BUY |
| GSL | $38.59→$38.59 | +0.0% | +8.0%→+8.0% | +0.0 | BUY→BUY |
| STNG | $83.87→$80.35 | -4.2% | +10.0%→+5.8% | -4.2 | BUY→BUY |
| ASC | $17.82→$17.80 | -0.1% | +5.3%→+5.2% | -0.1 | BUY→BUY |
| TRMD | $26.74→$25.43 | -4.9% | +9.2%→+4.8% | -4.3 | BUY→HOLD ⚠️ |
| GNK | $25.53→$24.69 | -3.3% | -0.0%→-2.9% | -2.9 | HOLD→HOLD |
| DHT | $16.07→$13.88 | -13.7% | +8.7%→-3.9% | -12.5 | BUY→HOLD ⚠️ |
| HAFN | $5.34→$5.22 | -2.2% | -9.4%→-11.0% | -1.5 | TRIM/SHORT→TRIM/SHORT |
| FRO | $28.47→$24.22 | -14.9% | -4.5%→-16.5% | -12.0 | HOLD→TRIM/SHORT ⚠️ |
| MPCC | $2.02→$2.02 | +0.0% | -17.4%→-17.4% | +0.0 | TRIM/SHORT→TRIM/SHORT |
| INSW **(WHOLE-CO)** | $57.91→$52.59 | -9.2% | -13.6%→-19.9% | -6.3 | TRIM/SHORT→TRIM/SHORT |
| ECO | $40.40→$34.35 | -15.0% | -8.7%→-20.2% | -11.4 | TRIM/SHORT→TRIM/SHORT |
| NAT | $3.32→$2.79 | -15.8% | -31.4%→-39.9% | -8.4 | TRIM/SHORT→TRIM/SHORT |

_Δ% = (txn − base) / base. Names with no exposure to a recalibrated class show Δ ≈ 0 — useful as a control. ⚠️ flags a position-call flip._

_**(WHOLE-CO)** = hybrid name valued via crude + product carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2)._
