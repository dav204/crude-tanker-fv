# Proposed parameters · not approved for production

The broad Transportation asset-risk grid is 6.9216% / 7.6894% / 9.6505% for all six sectors. This does **not** satisfy separate shipping-sector calibration. Base = 4.75% risk-free + 0.71 × 4.14% ERP. Low/high combine an analyst ±0.10 beta sensitivity with published alternative ERP constructions; they are not confidence limits. Source dates: beta January 2026; risk-free/ERP September 1, 2026.

[Damodaran current premium inputs](https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm), [industry betas](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html). Exact formula and conventions: [PREREGISTRATION.md](PREREGISTRATION.md).

| Ticker | Policy forecast | rE low/base/high % | Funding % | D&A per quarter $m | Evidence basis |
|---|---|---:|---:|---:|---|
| 2343 | net_cash_earnings; ratio 1.0; base DPS 0.0 | 6.69/7.43/9.34 | 7.26 | 36.48 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| ASC | earnings; ratio 0.6666666666666666; base DPS 0 | 5.93/6.69/8.61 | 24.01 | 9.66 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| BRUT | none; ratio 0; base DPS 0 | 6.84/7.58/9.46 | 0.00 | 0.00 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| BWLP | leverage_earnings; ratio 0.75; base DPS 0.0 | 7.75/8.72/11.19 | 4.07 | 29.45 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| CAPT | free_cash; ratio 0.35; base DPS 0 | 7.43/8.25/10.36 | 3.20 | 12.44 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| CCEC | fixed; ratio 0; base DPS 0.15 | 13.60/15.66/20.95 | 3.14 | 49.60 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| CMBT | earnings; ratio 0.5; base DPS 0.0 | 9.34/11.16/15.80 | 5.14 | 87.05 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| CMDB | none; ratio 0; base DPS 0 | 6.47/7.18/8.98 | 6.04 | 12.64 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| DHT | earnings; ratio 1; base DPS 0 | 6.99/7.84/10.03 | 5.74 | 27.75 | reported quarterly/H1 run-rate; GNK Q1; fleet changes still need a roll-forward |
| ECO | earnings; ratio 0.85; base DPS 0.0 | 7.22/8.23/10.79 | 5.54 | 21.36 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| FLNG | fixed; ratio 0; base DPS 0.75 | 9.30/10.80/14.62 | 4.49 | 27.30 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| FRO | earnings; ratio 0.95; base DPS 0.0 | 7.03/8.08/10.76 | 6.37 | 89.36 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| GNK | operating_cash; ratio 1; base DPS 0 | 7.24/8.19/10.61 | 5.36 | 21.00 | reported quarterly/H1 run-rate; GNK Q1; fleet changes still need a roll-forward |
| GSL | fixed; ratio 0; base DPS 0.625 | 8.24/9.15/11.49 | 2.13 | 33.43 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| HAFN | leverage_earnings; ratio 0.8; base DPS 0.0 | 7.47/8.44/10.92 | 4.80 | 46.78 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| INSW | earnings; ratio 0.85; base DPS 0.12 | 6.93/7.77/9.90 | 5.51 | 43.97 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| LPG | earnings; ratio 0.6; base DPS 0.0 | 7.47/8.39/10.75 | 4.49 | 13.59 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| MPCC | earnings; ratio 0.5; base DPS 0.04 | 7.45/8.31/10.53 | 4.21 | 16.63 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| NAT | earnings; ratio 1.0; base DPS 0.0 | 6.63/7.75/10.63 | 6.64 | 16.21 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| SB | fixed; ratio 0; base DPS 0.075 | 7.41/8.51/11.33 | 5.10 | 14.45 | reported quarterly/H1 run-rate; GNK Q1; fleet changes still need a roll-forward |
| SBLK | free_cash; ratio 1; base DPS 0.05 | 7.40/8.29/10.58 | 4.37 | 39.68 | reported quarterly/H1 run-rate; GNK Q1; fleet changes still need a roll-forward |
| STNG | fixed; ratio 0; base DPS 0.45 | 6.25/6.82/8.27 | 5.26 | 43.84 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| TEN | fixed; ratio 0; base DPS 0.375 | 8.81/10.03/13.15 | 3.95 | 50.75 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| TNK | fixed; ratio 0; base DPS 0.25 | 6.02/6.48/7.63 | 0.00 | 29.21 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |
| TRMD | liquidity; ratio 1; base DPS 0 | 6.64/7.57/9.94 | 7.06 | 55.48 | replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation |

Policy source dates/URLs, all quarterly schedule values, low/base/high policy details, corporate opening claims, sector asset weights and reference mark hashes are in `assumptions.json`. One reference is stored per issuer/sleeve. Sources or zero/default forecast entries must not be promoted as verified schedules.

Cycle proposal: ratio/NAV weight/terminal multiplier = (0.30,0.30,1.10), (0.65,0.40,1.05), (1.00,0.50,1.00), (1.35,0.60,0.95), (1.70,0.70,0.90). Clamp outside. Existing labels and categorical boundaries remain unchanged.

## Frozen issuer policy sources

These are source observations, not certifications of the entire forecast schedule. Later observations are kept in SOURCE_SUPPLEMENT.md.

| Issuer | Source date | Reference / observation |
|---|---|---|
| 2343 | 2026-09-22 | [annual ordinary income ex-disposals 50%, up to100% when net cash; interim/final cadence](https://www.pacificbasin.com/en/media/faq.php) |
| ASC | 2026-04-29 | [two thirds adjusted earnings](https://ardmoreshipping.investorroom.com/2026-04-29-Ardmore-Shipping-Provides-Update-on-Fleet-Investment%2C-Dividend-Policy%2C-and-Vessel-Sale) |
| BRUT | 2026-08-13 | [pre-delivery; existing zero distribution assumption retained, not a permanent policy](https://www.mfn.se/a/bruton-limited/bruton-limited-brut-results-for-the-six-months-ended-june-30-2026.iframe) |
| BWLP | 2026-09-22 | [shipping NPAT ladder 50/75/100%; net leverage <=30/20%; NCI is not preferred debt](https://www.bwlpg.com/investor/dividends/) |
| CAPT | 2026-09-01 | [NOK3 return of capital declared; construction-phase FCF and FX assumptions need review](https://mfn.se/a/capital-tankers/capital-tankers-corp-board-of-directors-declares-dividend-of-nok-3-00-per-share) |
| CCEC | 2026-07-23 | [$0.15 quarterly declaration; forward continuation assumption](https://ir.capitalcleanenergycarriers.com/press-releases) |
| CMBT | 2026-08-27 | [discretionary distribution includes share premium; joint sleeve dependence unresolved](https://mfn.se/one/a/cmb-tech/cmb-tech-announces-q2-2026-results-04b1527a) |
| CMDB | 2026-08-08 | [existing policy estimate retained pending current disclosure review](https://www.sec.gov/Archives/edgar/data/2033535/000117184326005131/) |
| DHT | 2026-08-05 | [ordinary income; 100%; remove unsupported nominal floor](https://www.sec.gov/Archives/edgar/data/1331284/000095015726000847/ex99-1.htm) |
| ECO | 2026-08-04 | [board discretion; retained 85% estimate is not an issuer formula](https://www.sec.gov/Archives/edgar/data/1964954/000110465926090429/eco-20260630xex99d2.htm) |
| FLNG | 2026-08-26 | [$0.75 declared; surplus cash policy; continuation is an assumption](https://www.flexlng.com/flex-lng-second-quarter-2026-earnings-release/) |
| FRO | 2026-08-28 | [Q2 distribution equals adjusted EPS; future payout discretionary](https://www.frontlineplc.cy/fro-second-quarter-and-six-months-2026-results/) |
| GNK | 2026-08-05 | [cash operating profit less voluntary reserve; Q3 target $19.5m](https://investors.gencoshipping.com/news/press-releases/news-details/2026/Genco-Shipping--Trading-Limited-Announces-Q2-2026-Financial-Results/default.aspx) |
| GSL | 2026-03-16 | [2026 expected quarterly common distribution $0.625; preferred coupon 8.75%](https://www.globalshiplease.com/static-files/27597ccc-72ab-48f6-be44-6706626ea783) |
| HAFN | 2024-05-15 | [net LTV ladder; 90% <=20%, 80% <=30%; issuer LTV must be reconciled](https://investor.hafnia.com/ir-news/news-details/2024/Hafnia-Limited--Increase-in-Quarterly-Dividend-Payout-Ratio-2024-RZ2rQvypGq/default.aspx) |
| INSW | 2026-08-11 | [current practice at least 85% adjusted income in combined distribution; not 70% plus a duplicated base](https://www.sec.gov/Archives/edgar/data/1679049/000110465926093033/tm2622617d1_ex99-1.htm) |
| LPG | 2026-09-22 | [irregular declared distributions; no mechanical forward payout formula](https://dorianlpg.com/investors/stock-analysts/dividend-history/default.aspx) |
| MPCC | 2026-08-29 | [existing policy estimate retained pending current disclosure review](https://mfn.se/ob/a/mpc-container-ships/mpc-container-ships-reports-q2-2026-results-d9624eca) |
| NAT | 2026-08-31 | [existing policy estimate retained pending current disclosure review](https://www.sec.gov/Archives/edgar/data/1000177/000091957426005786/) |
| SB | 2026-07-28 | [board-set $0.075 latest quarter; not a contractual 30% income formula](https://www.sec.gov/Archives/edgar/data/1434754/000131786126000037/f072926sb6k.htm) |
| SBLK | 2026-02-25 | [100% operating cash less debt amortization, maintenance/upgrades and $2.1m/vessel cash deficit; $0.05 minimum](https://www.starbulk.com/gr/en/dividend-policy/) |
| STNG | 2026-07-29 | [fixed $0.45; no assumed future buybacks](https://www.scorpiotankers.com/scorpio-tankers-inc-announces-financial-results-for-the-second-quarter-of-2026-and-the-declaration-of-a-dividend/) |
| TEN | 2026-09-22 | [semiannual declarations; remove unsubstantiated extra 19% variable layer](https://www.tenn.gr/earnings-releases/) |
| TNK | 2026-07-29 | [fixed $0.25 quarterly; no automatic recurring special](https://www.teekay.com/blog/2026/07/29/teekay-tankers-ltd-reports-second-quarter-2026-results-and-declares-dividend/) |
| TRMD | 2026-09-22 | [excess liquidity less per-vessel threshold and board discretionary reserve; not an EPS percentage](https://www.torm.com/investor/share/distribution/default.aspx) |

Exact base policy parameters (all remain forecasts subject to the stated source gaps):

- 2343: `{"additive_base": false, "base_dps": 0.0, "basis": "net_cash_earnings", "net_cash_ratio": 1, "net_debt_ratio": 0.5, "payment_quarters": [2, 4], "ratio": 1.0}`
- ASC: `{"additive_base": false, "base_dps": 0, "basis": "earnings", "ratio": 0.6666666666666666}`
- BRUT: `{"additive_base": false, "base_dps": 0, "basis": "none", "ratio": 0}`
- BWLP: `{"additive_base": false, "base_dps": 0.0, "basis": "leverage_earnings", "inclusive_tiers": true, "ratio": 0.75, "tiers": [[0.2, 1], [0.3, 0.75], [1000000.0, 0.5]]}`
- CAPT: `{"additive_base": false, "base_dps": 0, "basis": "free_cash", "ratio": 0.35}`
- CCEC: `{"additive_base": true, "base_dps": 0.15, "basis": "fixed", "ratio": 0}`
- CMBT: `{"additive_base": false, "base_dps": 0.0, "basis": "earnings", "ratio": 0.5}`
- CMDB: `{"additive_base": false, "base_dps": 0, "basis": "none", "ratio": 0}`
- DHT: `{"additive_base": false, "base_dps": 0, "basis": "earnings", "ratio": 1}`
- ECO: `{"additive_base": false, "base_dps": 0.0, "basis": "earnings", "ratio": 0.85}`
- FLNG: `{"additive_base": true, "base_dps": 0.75, "basis": "fixed", "ratio": 0}`
- FRO: `{"additive_base": false, "base_dps": 0.0, "basis": "earnings", "ratio": 0.95}`
- GNK: `{"additive_base": false, "base_dps": 0, "basis": "operating_cash", "ratio": 1}`
- GSL: `{"additive_base": true, "base_dps": 0.625, "basis": "fixed", "ratio": 0}`
- HAFN: `{"additive_base": false, "base_dps": 0.0, "basis": "leverage_earnings", "inclusive_tiers": true, "ratio": 0.8, "tiers": [[0.2, 0.9], [0.3, 0.8], [0.4, 0.6], [1000000.0, 0.5]]}`
- INSW: `{"additive_base": false, "base_dps": 0.12, "basis": "earnings", "ratio": 0.85}`
- LPG: `{"additive_base": false, "base_dps": 0.0, "basis": "earnings", "ratio": 0.6}`
- MPCC: `{"additive_base": false, "base_dps": 0.04, "basis": "earnings", "ratio": 0.5}`
- NAT: `{"additive_base": false, "base_dps": 0.0, "basis": "earnings", "ratio": 1.0}`
- SB: `{"additive_base": false, "base_dps": 0.075, "basis": "fixed", "ratio": 0}`
- SBLK: `{"additive_base": false, "base_dps": 0.05, "basis": "free_cash", "minimum_cash_deficit": true, "ratio": 1}`
- STNG: `{"additive_base": true, "base_dps": 0.45, "basis": "fixed", "ratio": 0}`
- TEN: `{"additive_base": true, "base_dps": 0.375, "base_period_multiplier": 2, "basis": "fixed", "payment_quarters": [2, 4], "ratio": 0}`
- TNK: `{"additive_base": true, "base_dps": 0.25, "basis": "fixed", "ratio": 0}`
- TRMD: `{"additive_base": false, "base_dps": 0, "basis": "liquidity", "ratio": 1}`
