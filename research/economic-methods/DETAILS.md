# Full-book method detail

USD per share; current-market strips below are distinct from scenario-weighted headline FV. Legacy terminal cash is the old implied cash-plus-retained-earnings amount; it is not a reconciled balance sheet. Research terminal cash/debt comes from the last explicit ledger quarter. The legacy extra terminal discount quarter is retained. Hybrid current-ledger common horizon is in `results/hybrid_current_cash.json`; new hybrid scenario cash FV is unavailable.

## 2343

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 0.3699 | 0.31–0.42 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| cash | 0.3646 | 0.30–0.42 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| reference | 0.3699 | 0.31–0.42 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| risk | 0.3794 | 0.32–0.43 | TRIM/SHORT (overvalued) | True | robust | 7.43 |
| smooth | 0.3709 | 0.31–0.43 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| cash_reference | 0.3646 | 0.30–0.42 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| cash_reference_risk | 0.3746 | 0.31–0.43 | TRIM/SHORT (overvalued) | True | robust | 7.43 |
| combined | 0.3759 | 0.31–0.43 | TRIM/SHORT (overvalued) | True | robust | 7.43 |
| reference_risk_smooth | 0.3810 | 0.32–0.44 | TRIM/SHORT (overvalued) | True | robust | 7.43 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 0.1166 | 206.53 | 143.27 | 0.2567 |
| cash | 0.0624 | 429.79 | 128.94 | 0.2930 |
| reference | 0.1166 | 206.53 | 143.27 | 0.2567 |
| risk | 0.1166 | 206.53 | 143.27 | 0.2762 |
| smooth | 0.1166 | 206.53 | 143.27 | 0.2599 |
| cash_reference | 0.0624 | 429.79 | 128.94 | 0.2930 |
| cash_reference_risk | 0.0624 | 429.79 | 128.94 | 0.3154 |
| combined | 0.0624 | 429.79 | 128.94 | 0.3189 |
| reference_risk_smooth | 0.1166 | 206.53 | 143.27 | 0.2798 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / dry_bulk | 0.4109 issuer | 0.1581 | 206.53 | 143.27 | 0.35 | 1.2548 / elevated |
| cash / dry_bulk | 0.4109 issuer | 0.1024 | 437.65 | 128.94 | 0.40 | 1.2548 / elevated |
| risk / dry_bulk | 0.4109 issuer | 0.1581 | 206.53 | 143.27 | 0.35 | 1.2548 / elevated |
| smooth / dry_bulk | 0.4109 issuer | 0.1581 | 206.53 | 143.27 | 0.36 | 1.2548 / elevated |
| combined / dry_bulk | 0.4109 issuer | 0.1024 | 437.65 | 128.94 | 0.40 | 1.2548 / elevated |
| reference_risk_smooth / dry_bulk | 0.4109 issuer | 0.1581 | 206.53 | 143.27 | 0.36 | 1.2548 / elevated |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## ASC

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 16.2830 | 12.60–19.42 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash | 16.1401 | 12.40–19.30 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| reference | 16.2830 | 12.60–19.42 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| risk | 16.7420 | 13.11–19.90 | TRIM/SHORT (overvalued) | True | n/a | 6.69 |
| smooth | 16.2831 | 12.60–19.42 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference | 16.1401 | 12.40–19.30 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference_risk | 16.6051 | 12.92–19.78 | TRIM/SHORT (overvalued) | True | n/a | 6.69 |
| combined | 16.6051 | 12.91–19.78 | TRIM/SHORT (overvalued) | True | n/a | 6.69 |
| reference_risk_smooth | 16.7420 | 13.10–19.90 | TRIM/SHORT (overvalued) | True | n/a | 6.69 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 3.6952 | 123.50 | 34.98 | 12.6476 |
| cash | 2.4729 | 155.81 | 31.48 | 13.3407 |
| reference | 3.6952 | 123.50 | 34.98 | 12.6476 |
| risk | 3.6952 | 123.50 | 34.98 | 13.8276 |
| smooth | 3.6952 | 123.50 | 34.98 | 12.6472 |
| cash_reference | 2.4729 | 155.81 | 31.48 | 13.3407 |
| cash_reference_risk | 2.4729 | 155.81 | 31.48 | 14.5854 |
| combined | 2.4729 | 155.81 | 31.48 | 14.5850 |
| reference_risk_smooth | 3.6952 | 123.50 | 34.98 | 13.8272 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / product | 17.3734 issuer | 4.3206 | 136.26 | 34.98 | 16.58 | 1.7166 / late-cycle/peak |
| cash / product | 17.3734 issuer | 3.0725 | 169.62 | 31.48 | 17.48 | 1.7166 / late-cycle/peak |
| risk / product | 17.3734 issuer | 4.3206 | 136.26 | 34.98 | 16.58 | 1.7166 / late-cycle/peak |
| smooth / product | 17.3734 issuer | 4.3206 | 136.26 | 34.98 | 16.58 | 1.7166 / late-cycle/peak |
| combined / product | 17.3734 issuer | 3.0725 | 169.62 | 31.48 | 17.48 | 1.7166 / late-cycle/peak |
| reference_risk_smooth / product | 17.3734 issuer | 4.3206 | 136.26 | 34.98 | 16.58 | 1.7166 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## BRUT

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 5.5106 | 2.46–8.54 | unreliable read (not actionable) | False | n/a | 11.00 |
| cash | 5.5496 | 2.50–8.58 | unreliable read (not actionable) | False | n/a | 11.00 |
| reference | 5.5106 | 2.46–8.54 | unreliable read (not actionable) | False | n/a | 11.00 |
| risk | 5.6365 | 2.50–8.77 | unreliable read (not actionable) | False | n/a | 7.58 |
| smooth | 5.5113 | 2.47–8.54 | unreliable read (not actionable) | False | n/a | 11.00 |
| cash_reference | 5.5496 | 2.50–8.58 | unreliable read (not actionable) | False | n/a | 11.00 |
| cash_reference_risk | 5.6783 | 2.54–8.82 | unreliable read (not actionable) | False | n/a | 7.58 |
| combined | 5.6797 | 2.56–8.82 | unreliable read (not actionable) | False | n/a | 7.58 |
| reference_risk_smooth | 5.6376 | 2.51–8.77 | unreliable read (not actionable) | False | n/a | 7.58 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 0.0000 | 212.83 | 0.00 | 5.7422 |
| cash | 0.0000 | -175.08 | 0.00 | 5.8720 |
| reference | 0.0000 | 212.83 | 0.00 | 5.7422 |
| risk | 0.0000 | 212.83 | 0.00 | 6.1617 |
| smooth | 0.0000 | 212.83 | 0.00 | 5.7493 |
| cash_reference | 0.0000 | -175.08 | 0.00 | 5.8720 |
| cash_reference_risk | 0.0000 | -175.08 | 0.00 | 6.3010 |
| combined | 0.0000 | -175.08 | 0.00 | 6.3087 |
| reference_risk_smooth | 0.0000 | 212.83 | 0.00 | 6.1694 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 4.9209 issuer | 0.0000 | 118.95 | 0.00 | 5.31 | 2.6425 / late-cycle/peak |
| cash / crude | 4.9209 issuer | 0.0000 | -268.96 | 0.00 | 5.48 | 2.6425 / late-cycle/peak |
| risk / crude | 4.9209 issuer | 0.0000 | 118.95 | 0.00 | 5.31 | 2.6425 / late-cycle/peak |
| smooth / crude | 4.9209 issuer | 0.0000 | 118.95 | 0.00 | 5.31 | 2.6425 / late-cycle/peak |
| combined / crude | 4.9209 issuer | 0.0000 | -268.96 | 0.00 | 5.48 | 2.6425 / late-cycle/peak |
| reference_risk_smooth / crude | 4.9209 issuer | 0.0000 | 118.95 | 0.00 | 5.31 | 2.6425 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## BWLP

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; issuer net leverage/NLTV differs from independent NAV fleet proxy; reconcile before adoption; preferred/NCI allocation and distributions require separate reconciliation; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 14.5216 | 10.92–18.28 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash | 14.3868 | 10.75–18.21 | rich · cycle position (not a short) | True | n/a | 11.00 |
| reference | 14.5216 | 10.92–18.28 | rich · cycle position (not a short) | True | n/a | 11.00 |
| risk | 14.7710 | 11.14–18.49 | rich · cycle position (not a short) | True | n/a | 8.72 |
| smooth | 14.5257 | 10.97–18.34 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference | 14.3868 | 10.75–18.21 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference_risk | 14.6317 | 10.96–18.42 | rich · cycle position (not a short) | True | n/a | 8.72 |
| combined | 14.6376 | 11.02–18.49 | rich · cycle position (not a short) | True | n/a | 8.72 |
| reference_risk_smooth | 14.7777 | 11.21–18.58 | rich · cycle position (not a short) | True | n/a | 8.72 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 3.4484 | 478.36 | 932.63 | 11.0175 |
| cash | 3.1454 | 375.69 | 839.37 | 10.9686 |
| reference | 3.4484 | 478.36 | 932.63 | 11.0175 |
| risk | 3.4484 | 478.36 | 932.63 | 11.5442 |
| smooth | 3.4484 | 478.36 | 932.63 | 11.0444 |
| cash_reference | 3.1454 | 375.69 | 839.37 | 10.9686 |
| cash_reference_risk | 3.1454 | 375.69 | 839.37 | 11.4928 |
| combined | 3.1454 | 375.69 | 839.37 | 11.5209 |
| reference_risk_smooth | 3.4484 | 478.36 | 932.63 | 11.5723 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / lpg | 15.8339 issuer | 4.0887 | 510.76 | 932.63 | 13.86 | 1.5904 / late-cycle/peak |
| cash / lpg | 15.8339 issuer | 3.9295 | 386.31 | 839.37 | 13.65 | 1.5904 / late-cycle/peak |
| risk / lpg | 15.8339 issuer | 4.0887 | 510.76 | 932.63 | 13.86 | 1.5904 / late-cycle/peak |
| smooth / lpg | 15.8339 issuer | 4.0887 | 510.76 | 932.63 | 14.14 | 1.5904 / late-cycle/peak |
| combined / lpg | 15.8339 issuer | 3.9295 | 386.31 | 839.37 | 13.94 | 1.5904 / late-cycle/peak |
| reference_risk_smooth / lpg | 15.8339 issuer | 4.0887 | 510.76 | 932.63 | 14.14 | 1.5904 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## CAPT

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 18.5712 | 10.62–25.92 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash | 18.4671 | 10.54–25.79 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| reference | 18.5712 | 10.62–25.92 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| risk | 18.8698 | 10.79–26.35 | HOLD (fairly valued) | True | n/a | 8.25 |
| smooth | 18.5887 | 10.76–25.92 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference | 18.4671 | 10.54–25.79 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference_risk | 18.7746 | 10.71–26.24 | HOLD (fairly valued) | True | n/a | 8.25 |
| combined | 18.7952 | 10.87–26.24 | HOLD (fairly valued) | True | n/a | 8.25 |
| reference_risk_smooth | 18.8919 | 10.96–26.35 | HOLD (fairly valued) | True | n/a | 8.25 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 3.4247 | 909.81 | 520.84 | 15.5693 |
| cash | 0.7631 | -619.86 | 468.75 | 17.5152 |
| reference | 3.4247 | 909.81 | 520.84 | 15.5693 |
| risk | 3.4247 | 909.81 | 520.84 | 16.4717 |
| smooth | 3.4247 | 909.81 | 520.84 | 15.6314 |
| cash_reference | 0.7631 | -619.86 | 468.75 | 17.5152 |
| cash_reference_risk | 0.7631 | -619.86 | 468.75 | 18.5304 |
| combined | 0.7631 | -619.86 | 468.75 | 18.5962 |
| reference_risk_smooth | 3.4247 | 909.81 | 520.84 | 16.5375 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 17.3155 issuer | 2.8060 | 808.71 | 520.84 | 17.80 | 2.5348 / late-cycle/peak |
| cash / crude | 17.3155 issuer | 0.6094 | -783.15 | 468.75 | 19.79 | 2.5348 / late-cycle/peak |
| risk / crude | 17.3155 issuer | 2.8060 | 808.71 | 520.84 | 17.80 | 2.5348 / late-cycle/peak |
| smooth / crude | 17.3155 issuer | 2.8060 | 808.71 | 520.84 | 17.80 | 2.5348 / late-cycle/peak |
| combined / crude | 17.3155 issuer | 0.6094 | -783.15 | 468.75 | 19.79 | 2.5348 / late-cycle/peak |
| reference_risk_smooth / crude | 17.3155 issuer | 2.8060 | 808.71 | 520.84 | 17.80 | 2.5348 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## CCEC

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; continuation of board-set dividend is a forecast, not a contractual payment; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; commitments have no mapped delivery schedule; remain outstanding, not assumed paid; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 33.7004 | 16.27–47.20 | BUY (undervalued) | True | n/a | 11.00 |
| cash | 33.0255 | 15.46–46.80 | BUY (undervalued) | True | n/a | 11.00 |
| reference | 33.7004 | 16.27–47.20 | BUY (undervalued) | True | n/a | 11.00 |
| risk | 32.2920 | 15.22–46.15 | BUY (undervalued) | True | n/a | 15.66 |
| smooth | 33.4624 | 16.96–47.20 | BUY (undervalued) | True | n/a | 11.00 |
| cash_reference | 33.0255 | 15.46–46.80 | BUY (undervalued) | True | n/a | 11.00 |
| cash_reference_risk | 31.6767 | 14.48–45.79 | BUY (undervalued) | True | n/a | 15.66 |
| combined | 31.4908 | 15.07–45.79 | BUY (undervalued) | True | n/a | 15.66 |
| reference_risk_smooth | 32.0954 | 15.83–46.15 | BUY (undervalued) | True | n/a | 15.66 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 1.2000 | 1,202.04 | 2,930.83 | 32.5643 |
| cash | 1.2000 | 804.54 | 2,637.75 | 31.2143 |
| reference | 1.2000 | 1,202.04 | 2,930.83 | 32.5643 |
| risk | 1.2000 | 1,202.04 | 2,930.83 | 29.6838 |
| smooth | 1.2000 | 1,202.04 | 2,930.83 | 32.2380 |
| cash_reference | 1.2000 | 804.54 | 2,637.75 | 31.2143 |
| cash_reference_risk | 1.2000 | 804.54 | 2,637.75 | 28.4533 |
| combined | 1.2000 | 804.54 | 2,637.75 | 28.1559 |
| reference_risk_smooth | 1.2000 | 1,202.04 | 2,930.83 | 29.3864 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / lng | 25.7017 issuer | 1.2000 | 1,168.49 | 2,930.83 | 40.14 | 0.7808 / below-mid |
| cash / lng | 25.7017 issuer | 1.2000 | 770.99 | 2,637.75 | 38.43 | 0.7808 / below-mid |
| risk / lng | 25.7017 issuer | 1.2000 | 1,168.49 | 2,930.83 | 40.14 | 0.7808 / below-mid |
| smooth / lng | 25.7017 issuer | 1.2000 | 1,168.49 | 2,930.83 | 38.40 | 0.7808 / below-mid |
| combined / lng | 25.7017 issuer | 1.2000 | 770.99 | 2,637.75 | 36.69 | 0.7808 / below-mid |
| reference_risk_smooth / lng | 25.7017 issuer | 1.2000 | 1,168.49 | 2,930.83 | 38.40 | 0.7808 / below-mid |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## CMBT

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; joint sector scenario mapping required for one issuer-level cash policy; no marginal-sleeve payout summation; payout percentage is a discretionary forecast, not a binding formula; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; commitments have no mapped delivery schedule; remain outstanding, not assumed paid; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 10.7546 | 5.64–16.37 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash | unavailable | — | — | — | — | — |
| reference | 10.7546 | 5.64–16.37 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| risk | 10.7440 | 5.63–16.36 | TRIM/SHORT (overvalued) | True | n/a | 11.16 |
| smooth | 10.7454 | 5.66–16.39 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference | unavailable | — | — | — | — | — |
| cash_reference_risk | unavailable | — | — | — | — | — |
| combined | unavailable | — | — | — | — | — |
| reference_risk_smooth | 10.7350 | 5.65–16.37 | TRIM/SHORT (overvalued) | True | n/a | 11.16 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 3.1958 | 1,081.96 | 5,452.66 | 7.7746 |
| reference | 3.1958 | 1,081.96 | 5,452.66 | 7.7746 |
| risk | 3.1958 | 1,081.96 | 5,452.66 | 7.7490 |
| smooth | 3.1958 | 1,081.96 | 5,452.66 | 7.7334 |
| reference_risk_smooth | 3.1958 | 1,081.96 | 5,452.66 | 7.7079 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 13.3592 issuer | 1.0757 | corporate; see joint ledger | corporate | 2.81 | 2.6697 / late-cycle/peak |
| legacy / dry_bulk | 13.3592 issuer | 2.3965 | corporate; see joint ledger | corporate | 7.99 | 1.6870 / late-cycle/peak |
| legacy / containerships | 13.3592 issuer | 0.2410 | corporate; see joint ledger | corporate | 0.55 | 1.5610 / late-cycle/peak |
| risk / crude | 13.3592 issuer | 1.0757 | corporate; see joint ledger | corporate | 2.81 | 2.6697 / late-cycle/peak |
| risk / dry_bulk | 13.3592 issuer | 2.3965 | corporate; see joint ledger | corporate | 7.99 | 1.6870 / late-cycle/peak |
| risk / containerships | 13.3592 issuer | 0.2410 | corporate; see joint ledger | corporate | 0.55 | 1.5610 / late-cycle/peak |
| smooth / crude | 13.3592 issuer | 1.0757 | corporate; see joint ledger | corporate | 2.81 | 2.6697 / late-cycle/peak |
| smooth / dry_bulk | 13.3592 issuer | 2.3965 | corporate; see joint ledger | corporate | 8.02 | 1.6870 / late-cycle/peak |
| smooth / containerships | 13.3592 issuer | 0.2410 | corporate; see joint ledger | corporate | 0.56 | 1.5610 / late-cycle/peak |
| reference_risk_smooth / crude | 13.3592 issuer | 1.0757 | corporate; see joint ledger | corporate | 2.81 | 2.6697 / late-cycle/peak |
| reference_risk_smooth / dry_bulk | 13.3592 issuer | 2.3965 | corporate; see joint ledger | corporate | 8.02 | 1.6870 / late-cycle/peak |
| reference_risk_smooth / containerships | 13.3592 issuer | 0.2410 | corporate; see joint ledger | corporate | 0.56 | 1.5610 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## CMDB

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; current policy primary-source recheck incomplete; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 19.2967 | 16.01–22.78 | TRIM/SHORT (overvalued) | True | flips (fair/rich) | 11.00 |
| cash | 19.1716 | 15.86–22.69 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| reference | 19.2967 | 16.01–22.78 | TRIM/SHORT (overvalued) | True | flips (fair/rich) | 11.00 |
| risk | 19.8832 | 16.57–23.30 | TRIM/SHORT (overvalued) | True | robust | 7.18 |
| smooth | 19.2990 | 15.98–22.78 | TRIM/SHORT (overvalued) | True | flips (fair/rich) | 11.00 |
| cash_reference | 19.1716 | 15.86–22.69 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference_risk | 19.7478 | 16.41–23.20 | TRIM/SHORT (overvalued) | True | n/a | 7.18 |
| combined | 19.7424 | 16.40–23.20 | TRIM/SHORT (overvalued) | True | n/a | 7.18 |
| reference_risk_smooth | 19.8760 | 16.56–23.30 | TRIM/SHORT (overvalued) | True | robust | 7.18 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 0.0000 | 388.14 | 172.20 | 17.3860 |
| cash | 0.0000 | 357.86 | 154.98 | 17.0880 |
| reference | 0.0000 | 388.14 | 172.20 | 17.3860 |
| risk | 0.0000 | 388.14 | 172.20 | 18.8131 |
| smooth | 0.0000 | 388.14 | 172.20 | 17.3511 |
| cash_reference | 0.0000 | 357.86 | 154.98 | 17.0880 |
| cash_reference_risk | 0.0000 | 357.86 | 154.98 | 18.4906 |
| combined | 0.0000 | 357.86 | 154.98 | 18.4528 |
| reference_risk_smooth | 0.0000 | 388.14 | 172.20 | 18.7753 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / dry_bulk | 32.6010 issuer | 0.0000 | 476.30 | 172.20 | 25.26 | 1.5466 / late-cycle/peak |
| cash / dry_bulk | 32.6010 issuer | 0.0000 | 446.03 | 154.98 | 24.88 | 1.5466 / late-cycle/peak |
| risk / dry_bulk | 32.6010 issuer | 0.0000 | 476.30 | 172.20 | 25.26 | 1.5466 / late-cycle/peak |
| smooth / dry_bulk | 32.6010 issuer | 0.0000 | 476.30 | 172.20 | 25.64 | 1.5466 / late-cycle/peak |
| combined / dry_bulk | 32.6010 issuer | 0.0000 | 446.03 | 154.98 | 25.26 | 1.5466 / late-cycle/peak |
| reference_risk_smooth / dry_bulk | 32.6010 issuer | 0.0000 | 476.30 | 172.20 | 25.64 | 1.5466 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## DHT

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 16.5611 | 11.82–21.53 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash | 16.4461 | 11.70–21.41 | rich · cycle position (not a short) | True | robust | 11.00 |
| reference | 16.5611 | 11.82–21.53 | rich · cycle position (not a short) | True | robust | 11.00 |
| risk | 16.8308 | 12.00–21.89 | rich · cycle position (not a short) | True | robust | 7.84 |
| smooth | 16.5646 | 11.85–21.53 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference | 16.4461 | 11.70–21.41 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference_risk | 16.7209 | 11.89–21.78 | rich · cycle position (not a short) | True | robust | 7.84 |
| combined | 16.7251 | 11.93–21.78 | rich · cycle position (not a short) | True | robust | 7.84 |
| reference_risk_smooth | 16.8358 | 12.04–21.89 | rich · cycle position (not a short) | True | robust | 7.84 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 9.8818 | 161.68 | 435.79 | 9.6069 |
| cash | 8.5198 | 209.97 | 392.21 | 10.4374 |
| reference | 9.8818 | 161.68 | 435.79 | 9.6069 |
| risk | 9.8818 | 161.68 | 435.79 | 10.2509 |
| smooth | 9.8818 | 161.68 | 435.79 | 9.6162 |
| cash_reference | 8.5198 | 209.97 | 392.21 | 10.4374 |
| cash_reference_risk | 8.5198 | 209.97 | 392.21 | 11.1371 |
| combined | 8.5198 | 209.97 | 392.21 | 11.1471 |
| reference_risk_smooth | 9.8818 | 161.68 | 435.79 | 10.2609 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 15.0054 issuer | 7.4036 | 161.68 | 435.79 | 11.58 | 2.6425 / late-cycle/peak |
| cash / crude | 15.0054 issuer | 6.0415 | 209.97 | 392.21 | 12.63 | 2.6425 / late-cycle/peak |
| risk / crude | 15.0054 issuer | 7.4036 | 161.68 | 435.79 | 11.58 | 2.6425 / late-cycle/peak |
| smooth / crude | 15.0054 issuer | 7.4036 | 161.68 | 435.79 | 11.58 | 2.6425 / late-cycle/peak |
| combined / crude | 15.0054 issuer | 6.0415 | 209.97 | 392.21 | 12.63 | 2.6425 / late-cycle/peak |
| reference_risk_smooth / crude | 15.0054 issuer | 7.4036 | 161.68 | 435.79 | 11.58 | 2.6425 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## ECO

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; payout percentage is a discretionary forecast, not a binding formula; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 44.1538 | 28.33–60.70 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash | 43.8279 | 28.01–60.37 | rich · cycle position (not a short) | True | n/a | 11.00 |
| reference | 44.1538 | 28.33–60.70 | rich · cycle position (not a short) | True | robust | 11.00 |
| risk | 44.8098 | 28.71–61.69 | rich · cycle position (not a short) | True | robust | 8.23 |
| smooth | 44.1567 | 28.35–60.70 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference | 43.8279 | 28.01–60.37 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference_risk | 44.4948 | 28.39–61.37 | rich · cycle position (not a short) | True | n/a | 8.23 |
| combined | 44.4994 | 28.43–61.37 | rich · cycle position (not a short) | True | n/a | 8.23 |
| reference_risk_smooth | 44.8184 | 28.77–61.69 | rich · cycle position (not a short) | True | robust | 8.23 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 23.4429 | 409.33 | 722.49 | 28.5628 |
| cash | 19.8032 | 364.28 | 650.24 | 30.7214 |
| reference | 23.4429 | 409.33 | 722.49 | 28.5628 |
| risk | 23.4429 | 409.33 | 722.49 | 30.2370 |
| smooth | 23.4429 | 409.33 | 722.49 | 28.6153 |
| cash_reference | 19.8032 | 364.28 | 650.24 | 30.7214 |
| cash_reference_risk | 19.8032 | 364.28 | 650.24 | 32.5222 |
| combined | 19.8032 | 364.28 | 650.24 | 32.5777 |
| reference_risk_smooth | 23.4429 | 409.33 | 722.49 | 30.2926 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 39.5374 issuer | 15.7885 | 356.59 | 722.49 | 32.98 | 2.6635 / late-cycle/peak |
| cash / crude | 39.5374 issuer | 12.1488 | 311.53 | 650.24 | 35.71 | 2.6635 / late-cycle/peak |
| risk / crude | 39.5374 issuer | 15.7885 | 356.59 | 722.49 | 32.98 | 2.6635 / late-cycle/peak |
| smooth / crude | 39.5374 issuer | 15.7885 | 356.59 | 722.49 | 32.98 | 2.6635 / late-cycle/peak |
| combined / crude | 39.5374 issuer | 12.1488 | 311.53 | 650.24 | 35.71 | 2.6635 / late-cycle/peak |
| reference_risk_smooth / crude | 39.5374 issuer | 15.7885 | 356.59 | 722.49 | 32.98 | 2.6635 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## FLNG

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; continuation of board-set dividend is a forecast, not a contractual payment; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 29.4742 | 19.34–38.00 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash | 29.1474 | 18.95–37.81 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| reference | 29.4742 | 19.34–38.00 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| risk | 29.5240 | 19.38–38.04 | TRIM/SHORT (overvalued) | True | n/a | 10.80 |
| smooth | 29.5318 | 19.80–38.00 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference | 29.1474 | 18.95–37.81 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference_risk | 29.1959 | 18.99–37.84 | TRIM/SHORT (overvalued) | True | n/a | 10.80 |
| combined | 29.2502 | 19.43–37.84 | TRIM/SHORT (overvalued) | True | n/a | 10.80 |
| reference_risk_smooth | 29.5826 | 19.85–38.04 | TRIM/SHORT (overvalued) | True | n/a | 10.80 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 6.0000 | 519.83 | 1,793.67 | 22.2696 |
| cash | 6.0000 | 259.13 | 1,577.67 | 21.6160 |
| reference | 6.0000 | 519.83 | 1,793.67 | 22.2696 |
| risk | 6.0000 | 519.83 | 1,793.67 | 22.3620 |
| smooth | 6.0000 | 519.83 | 1,793.67 | 22.3984 |
| cash_reference | 6.0000 | 259.13 | 1,577.67 | 21.6160 |
| cash_reference_risk | 6.0000 | 259.13 | 1,577.67 | 21.7058 |
| combined | 6.0000 | 259.13 | 1,577.67 | 21.8352 |
| reference_risk_smooth | 6.0000 | 519.83 | 1,793.67 | 22.4914 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / lng | 27.2220 issuer | 6.0000 | 478.50 | 1,793.67 | 27.22 | 0.7059 / below-mid |
| cash / lng | 27.2220 issuer | 6.0000 | 217.79 | 1,577.67 | 26.40 | 0.7059 / below-mid |
| risk / lng | 27.2220 issuer | 6.0000 | 478.50 | 1,793.67 | 27.22 | 0.7059 / below-mid |
| smooth / lng | 27.2220 issuer | 6.0000 | 478.50 | 1,793.67 | 26.83 | 0.7059 / below-mid |
| combined / lng | 27.2220 issuer | 6.0000 | 217.79 | 1,577.67 | 26.01 | 0.7059 / below-mid |
| reference_risk_smooth / lng | 27.2220 issuer | 6.0000 | 478.50 | 1,793.67 | 26.83 | 0.7059 / below-mid |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## FRO

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; payout percentage is a discretionary forecast, not a binding formula; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 29.3766 | 18.37–41.29 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash | 29.1123 | 18.09–41.04 | rich · cycle position (not a short) | True | robust | 11.00 |
| reference | 29.3766 | 18.37–41.29 | rich · cycle position (not a short) | True | robust | 11.00 |
| risk | 29.8230 | 18.62–41.97 | rich · cycle position (not a short) | True | robust | 8.08 |
| smooth | 29.3942 | 18.50–41.29 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference | 29.1123 | 18.09–41.04 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference_risk | 29.5728 | 18.36–41.73 | rich · cycle position (not a short) | True | robust | 8.08 |
| combined | 29.5915 | 18.51–41.73 | rich · cycle position (not a short) | True | robust | 8.08 |
| reference_risk_smooth | 29.8467 | 18.80–41.97 | rich · cycle position (not a short) | True | robust | 8.08 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 19.1763 | 547.00 | 2,434.84 | 16.7012 |
| cash | 15.8343 | 297.82 | 2,191.36 | 18.8160 |
| reference | 19.1763 | 547.00 | 2,434.84 | 16.7012 |
| risk | 19.1763 | 547.00 | 2,434.84 | 17.7329 |
| smooth | 19.1763 | 547.00 | 2,434.84 | 16.7596 |
| cash_reference | 15.8343 | 297.82 | 2,191.36 | 18.8160 |
| cash_reference_risk | 15.8343 | 297.82 | 2,191.36 | 19.9784 |
| combined | 15.8343 | 297.82 | 2,191.36 | 20.0404 |
| reference_risk_smooth | 19.1763 | 547.00 | 2,434.84 | 17.7949 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 26.0436 issuer | 13.8856 | 485.00 | 2,434.84 | 19.75 | 2.5660 / late-cycle/peak |
| cash / crude | 26.0436 issuer | 10.5007 | 245.38 | 2,191.36 | 22.47 | 2.5660 / late-cycle/peak |
| risk / crude | 26.0436 issuer | 13.8856 | 485.00 | 2,434.84 | 19.75 | 2.5660 / late-cycle/peak |
| smooth / crude | 26.0436 issuer | 13.8856 | 485.00 | 2,434.84 | 19.75 | 2.5660 / late-cycle/peak |
| combined / crude | 26.0436 issuer | 10.5007 | 245.38 | 2,191.36 | 22.47 | 2.5660 / late-cycle/peak |
| reference_risk_smooth / crude | 26.0436 issuer | 13.8856 | 485.00 | 2,434.84 | 19.75 | 2.5660 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## GNK

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 21.0500 | 16.39–26.23 | TRIM/SHORT (overvalued) | True | flips (cheap/fair) | 11.00 |
| cash | 20.7026 | 15.98–25.98 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| reference | 21.0500 | 16.39–26.23 | TRIM/SHORT (overvalued) | True | flips (cheap/fair) | 11.00 |
| risk | 21.4500 | 16.77–26.59 | TRIM/SHORT (overvalued) | True | robust | 8.19 |
| smooth | 21.0574 | 16.45–26.23 | TRIM/SHORT (overvalued) | True | flips (cheap/fair) | 11.00 |
| cash_reference | 20.7026 | 15.98–25.98 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| cash_reference_risk | 21.1220 | 16.39–26.35 | TRIM/SHORT (overvalued) | True | robust | 8.19 |
| combined | 21.1306 | 16.45–26.35 | TRIM/SHORT (overvalued) | True | robust | 8.19 |
| reference_risk_smooth | 21.4614 | 16.86–26.59 | TRIM/SHORT (overvalued) | True | robust | 8.19 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 7.9444 | 73.59 | 335.69 | 13.3177 |
| cash | 4.5206 | 108.03 | 302.12 | 15.5442 |
| reference | 7.9444 | 73.59 | 335.69 | 13.3177 |
| risk | 7.9444 | 73.59 | 335.69 | 14.1087 |
| smooth | 7.9444 | 73.59 | 335.69 | 13.3510 |
| cash_reference | 4.5206 | 108.03 | 302.12 | 15.5442 |
| cash_reference_risk | 4.5206 | 108.03 | 302.12 | 16.4675 |
| combined | 4.5206 | 108.03 | 302.12 | 16.5028 |
| reference_risk_smooth | 7.9444 | 73.59 | 335.69 | 14.1440 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / dry_bulk | 25.3734 issuer | 11.4423 | 73.59 | 335.69 | 18.46 | 1.5692 / late-cycle/peak |
| cash / dry_bulk | 25.3734 issuer | 7.9777 | 109.84 | 302.12 | 21.32 | 1.5692 / late-cycle/peak |
| risk / dry_bulk | 25.3734 issuer | 11.4423 | 73.59 | 335.69 | 18.46 | 1.5692 / late-cycle/peak |
| smooth / dry_bulk | 25.3734 issuer | 11.4423 | 73.59 | 335.69 | 18.98 | 1.5692 / late-cycle/peak |
| combined / dry_bulk | 25.3734 issuer | 7.9777 | 109.84 | 302.12 | 21.84 | 1.5692 / late-cycle/peak |
| reference_risk_smooth / dry_bulk | 25.3734 issuer | 11.4423 | 73.59 | 335.69 | 18.98 | 1.5692 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## GSL

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; continuation of board-set dividend is a forecast, not a contractual payment; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 42.9399 | 38.63–46.70 | TRIM/SHORT (overvalued) | None | n/a | 11.00 |
| cash | 42.4004 | 38.10–46.16 | TRIM/SHORT (overvalued) | None | n/a | 11.00 |
| reference | 42.9399 | 38.63–46.70 | TRIM/SHORT (overvalued) | None | n/a | 11.00 |
| risk | 43.8135 | 39.41–47.65 | HOLD (fairly valued) | None | n/a | 9.15 |
| smooth | 42.9028 | 39.18–46.27 | TRIM/SHORT (overvalued) | None | n/a | 11.00 |
| cash_reference | 42.4004 | 38.10–46.16 | TRIM/SHORT (overvalued) | None | n/a | 11.00 |
| cash_reference_risk | 43.2485 | 38.85–47.08 | TRIM/SHORT (overvalued) | None | n/a | 9.15 |
| combined | 43.2066 | 39.42–46.62 | TRIM/SHORT (overvalued) | None | n/a | 9.15 |
| reference_risk_smooth | 43.7695 | 40.04–47.15 | HOLD (fairly valued) | None | n/a | 9.15 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 6.2500 | 1,624.43 | 676.42 | 43.6056 |
| cash | 6.2500 | 1,475.12 | 591.87 | 42.2568 |
| reference | 6.2500 | 1,624.43 | 676.42 | 43.6056 |
| risk | 6.2500 | 1,624.43 | 676.42 | 45.6673 |
| smooth | 6.2500 | 1,624.43 | 676.42 | 43.5704 |
| cash_reference | 6.2500 | 1,475.12 | 591.87 | 42.2568 |
| cash_reference_risk | 6.2500 | 1,475.12 | 591.87 | 44.2547 |
| combined | 6.2500 | 1,475.12 | 591.87 | 44.2179 |
| reference_risk_smooth | 6.2500 | 1,624.43 | 676.42 | 45.6304 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / containerships | 41.3701 issuer | 6.2500 | 1,705.51 | 676.42 | 60.34 | 1.5156 / late-cycle/peak |
| cash / containerships | 41.3701 issuer | 6.2500 | 1,556.20 | 591.87 | 58.54 | 1.5156 / late-cycle/peak |
| risk / containerships | 41.3701 issuer | 6.2500 | 1,705.51 | 676.42 | 60.34 | 1.5156 / late-cycle/peak |
| smooth / containerships | 41.3701 issuer | 6.2500 | 1,705.51 | 676.42 | 61.31 | 1.5156 / late-cycle/peak |
| combined / containerships | 41.3701 issuer | 6.2500 | 1,556.20 | 591.87 | 59.51 | 1.5156 / late-cycle/peak |
| reference_risk_smooth / containerships | 41.3701 issuer | 6.2500 | 1,705.51 | 676.42 | 61.31 | 1.5156 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## HAFN

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; issuer net leverage/NLTV differs from independent NAV fleet proxy; reconcile before adoption; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 5.4681 | 3.08–7.69 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash | 5.4341 | 3.02–7.68 | rich · cycle position (not a short) | True | n/a | 11.00 |
| reference | 5.4681 | 3.08–7.69 | rich · cycle position (not a short) | True | n/a | 11.00 |
| risk | 5.5580 | 3.15–7.82 | rich · cycle position (not a short) | True | n/a | 8.44 |
| smooth | 5.4678 | 3.07–7.69 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference | 5.4341 | 3.02–7.68 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference_risk | 5.5240 | 3.09–7.80 | rich · cycle position (not a short) | True | n/a | 8.44 |
| combined | 5.5237 | 3.08–7.80 | rich · cycle position (not a short) | True | n/a | 8.44 |
| reference_risk_smooth | 5.5576 | 3.13–7.82 | rich · cycle position (not a short) | True | n/a | 8.44 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 3.4602 | 708.72 | 885.36 | 3.6526 |
| cash | 3.2610 | 674.00 | 796.83 | 3.7366 |
| reference | 3.4602 | 708.72 | 885.36 | 3.6526 |
| risk | 3.4602 | 708.72 | 885.36 | 3.8494 |
| smooth | 3.4602 | 708.72 | 885.36 | 3.6515 |
| cash_reference | 3.2610 | 674.00 | 796.83 | 3.7366 |
| cash_reference_risk | 3.2610 | 674.00 | 796.83 | 3.9380 |
| combined | 3.2610 | 674.00 | 796.83 | 3.9369 |
| reference_risk_smooth | 3.4602 | 708.72 | 885.36 | 3.8483 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / product | 4.6359 issuer | 2.6309 | 603.81 | 885.36 | 4.06 | 1.8878 / late-cycle/peak |
| cash / product | 4.6359 issuer | 2.3271 | 622.01 | 796.83 | 4.27 | 1.8878 / late-cycle/peak |
| risk / product | 4.6359 issuer | 2.6309 | 603.81 | 885.36 | 4.06 | 1.8878 / late-cycle/peak |
| smooth / product | 4.6359 issuer | 2.6309 | 603.81 | 885.36 | 4.06 | 1.8878 / late-cycle/peak |
| combined / product | 4.6359 issuer | 2.3271 | 622.01 | 796.83 | 4.27 | 1.8878 / late-cycle/peak |
| reference_risk_smooth / product | 4.6359 issuer | 2.6309 | 603.81 | 885.36 | 4.06 | 1.8878 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## INSW

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; joint sector scenario mapping required for one issuer-level cash policy; no marginal-sleeve payout summation; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 61.8119 | 42.87–80.41 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash | unavailable | — | — | — | — | — |
| reference | 61.8119 | 42.87–80.41 | rich · cycle position (not a short) | True | n/a | 11.00 |
| risk | 63.0117 | 43.74–82.07 | rich · cycle position (not a short) | True | n/a | 7.77 |
| smooth | 61.8221 | 42.95–80.41 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference | unavailable | — | — | — | — | — |
| cash_reference_risk | unavailable | — | — | — | — | — |
| combined | unavailable | — | — | — | — | — |
| reference_risk_smooth | 63.0339 | 43.90–82.07 | rich · cycle position (not a short) | True | n/a | 7.77 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 30.3066 | 920.22 | 652.77 | 44.1829 |
| reference | 30.3066 | 920.22 | 652.77 | 44.1829 |
| risk | 30.3066 | 920.22 | 652.77 | 47.2196 |
| smooth | 30.3066 | 920.22 | 652.77 | 44.2460 |
| reference_risk_smooth | 30.3066 | 920.22 | 652.77 | 47.2870 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 54.6378 issuer | 15.3580 | corporate; see joint ledger | corporate | 34.19 | 2.5140 / late-cycle/peak |
| legacy / product | 54.6378 issuer | 6.5202 | corporate; see joint ledger | corporate | 15.21 | 1.7729 / late-cycle/peak |
| risk / crude | 54.6378 issuer | 15.3580 | corporate; see joint ledger | corporate | 34.19 | 2.5140 / late-cycle/peak |
| risk / product | 54.6378 issuer | 6.5202 | corporate; see joint ledger | corporate | 15.21 | 1.7729 / late-cycle/peak |
| smooth / crude | 54.6378 issuer | 15.3580 | corporate; see joint ledger | corporate | 34.19 | 2.5140 / late-cycle/peak |
| smooth / product | 54.6378 issuer | 6.5202 | corporate; see joint ledger | corporate | 15.21 | 1.7729 / late-cycle/peak |
| reference_risk_smooth / crude | 54.6378 issuer | 15.3580 | corporate; see joint ledger | corporate | 34.19 | 2.5140 / late-cycle/peak |
| reference_risk_smooth / product | 54.6378 issuer | 6.5202 | corporate; see joint ledger | corporate | 15.21 | 1.7729 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## LPG

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; payout percentage is a discretionary forecast, not a binding formula; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 31.8242 | 25.61–38.58 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash | 31.5587 | 25.33–38.39 | rich · cycle position (not a short) | True | n/a | 11.00 |
| reference | 31.8242 | 25.61–38.58 | rich · cycle position (not a short) | True | n/a | 11.00 |
| risk | 32.4591 | 26.20–39.11 | rich · cycle position (not a short) | True | n/a | 8.39 |
| smooth | 31.8176 | 25.55–38.58 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference | 31.5587 | 25.33–38.39 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference_risk | 32.1940 | 25.92–38.93 | rich · cycle position (not a short) | True | n/a | 8.39 |
| combined | 32.1919 | 25.90–38.96 | rich · cycle position (not a short) | True | n/a | 8.39 |
| reference_risk_smooth | 32.4588 | 26.20–39.17 | rich · cycle position (not a short) | True | n/a | 8.39 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 3.4302 | 437.28 | 651.10 | 25.8862 |
| cash | 2.1539 | 401.07 | 585.99 | 26.4204 |
| reference | 3.4302 | 437.28 | 651.10 | 25.8862 |
| risk | 3.4302 | 437.28 | 651.10 | 27.3076 |
| smooth | 3.4302 | 437.28 | 651.10 | 25.9310 |
| cash_reference | 2.1539 | 401.07 | 585.99 | 26.4204 |
| cash_reference_risk | 2.1539 | 401.07 | 585.99 | 27.8711 |
| combined | 2.1539 | 401.07 | 585.99 | 27.9184 |
| reference_risk_smooth | 3.4302 | 437.28 | 651.10 | 27.3548 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / lpg | 35.6908 issuer | 4.2355 | 462.95 | 651.10 | 32.85 | 1.5904 / late-cycle/peak |
| cash / lpg | 35.6908 issuer | 2.7467 | 435.83 | 585.99 | 33.74 | 1.5904 / late-cycle/peak |
| risk / lpg | 35.6908 issuer | 4.2355 | 462.95 | 651.10 | 32.85 | 1.5904 / late-cycle/peak |
| smooth / lpg | 35.6908 issuer | 4.2355 | 462.95 | 651.10 | 33.33 | 1.5904 / late-cycle/peak |
| combined / lpg | 35.6908 issuer | 2.7467 | 435.83 | 585.99 | 34.22 | 1.5904 / late-cycle/peak |
| reference_risk_smooth / lpg | 35.6908 issuer | 4.2355 | 462.95 | 651.10 | 33.33 | 1.5904 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## MPCC

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; current policy primary-source recheck incomplete; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 2.1617 | 1.80–2.30 | unreliable read (not actionable) | None | n/a | 11.00 |
| cash | 2.1234 | 1.76–2.27 | unreliable read (not actionable) | None | n/a | 11.00 |
| reference | 2.1617 | 1.80–2.30 | unreliable read (not actionable) | None | n/a | 11.00 |
| risk | 2.2308 | 1.86–2.36 | unreliable read (not actionable) | None | n/a | 8.31 |
| smooth | 2.1459 | 1.80–2.34 | unreliable read (not actionable) | None | n/a | 11.00 |
| cash_reference | 2.1234 | 1.76–2.27 | unreliable read (not actionable) | None | n/a | 11.00 |
| cash_reference_risk | 2.1927 | 1.82–2.33 | unreliable read (not actionable) | None | n/a | 8.31 |
| combined | 2.1754 | 1.82–2.37 | unreliable read (not actionable) | None | n/a | 8.31 |
| reference_risk_smooth | 2.2123 | 1.86–2.41 | unreliable read (not actionable) | None | n/a | 8.31 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 0.7874 | 663.41 | 436.79 | 1.7505 |
| cash | 0.6029 | 108.52 | 382.19 | 1.8303 |
| reference | 0.7874 | 663.41 | 436.79 | 1.7505 |
| risk | 0.7874 | 663.41 | 436.79 | 1.8725 |
| smooth | 0.7874 | 663.41 | 436.79 | 1.7353 |
| cash_reference | 0.6029 | 108.52 | 382.19 | 1.8303 |
| cash_reference_risk | 0.6029 | 108.52 | 382.19 | 1.9578 |
| combined | 0.6029 | 108.52 | 382.19 | 1.9417 |
| reference_risk_smooth | 0.7874 | 663.41 | 436.79 | 1.8563 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / containerships | 2.1519 issuer | 0.8493 | 690.90 | 436.79 | 2.49 | 1.3604 / elevated |
| cash / containerships | 2.1519 issuer | 0.6649 | 136.02 | 382.19 | 2.60 | 1.3604 / elevated |
| risk / containerships | 2.1519 issuer | 0.8493 | 690.90 | 436.79 | 2.49 | 1.3604 / elevated |
| smooth / containerships | 2.1519 issuer | 0.8493 | 690.90 | 436.79 | 2.49 | 1.3604 / elevated |
| combined / containerships | 2.1519 issuer | 0.6649 | 136.02 | 382.19 | 2.59 | 1.3604 / elevated |
| reference_risk_smooth / containerships | 2.1519 issuer | 0.8493 | 690.90 | 436.79 | 2.49 | 1.3604 / elevated |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## NAT

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; current policy primary-source recheck incomplete; payout percentage is a discretionary forecast, not a binding formula; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 3.2358 | 2.03–4.43 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash | 3.2059 | 2.00–4.40 | rich · cycle position (not a short) | True | n/a | 11.00 |
| reference | 3.2358 | 2.03–4.43 | rich · cycle position (not a short) | True | robust | 11.00 |
| risk | 3.2892 | 2.06–4.51 | rich · cycle position (not a short) | True | robust | 7.75 |
| smooth | 3.2378 | 2.05–4.43 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference | 3.2059 | 2.00–4.40 | rich · cycle position (not a short) | True | n/a | 11.00 |
| cash_reference_risk | 3.2629 | 2.04–4.49 | rich · cycle position (not a short) | True | n/a | 7.75 |
| combined | 3.2651 | 2.05–4.49 | rich · cycle position (not a short) | True | n/a | 7.75 |
| reference_risk_smooth | 3.2919 | 2.08–4.51 | rich · cycle position (not a short) | True | robust | 7.75 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 2.7034 | 133.29 | 406.84 | 1.5224 |
| cash | 2.1143 | 206.52 | 366.16 | 1.9477 |
| reference | 2.7034 | 133.29 | 406.84 | 1.5224 |
| risk | 2.7034 | 133.29 | 406.84 | 1.6276 |
| smooth | 2.7034 | 133.29 | 406.84 | 1.5275 |
| cash_reference | 2.1143 | 206.52 | 366.16 | 1.9477 |
| cash_reference_risk | 2.1143 | 206.52 | 366.16 | 2.0823 |
| combined | 2.1143 | 206.52 | 366.16 | 2.0878 |
| reference_risk_smooth | 2.7034 | 133.29 | 406.84 | 1.6330 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 2.7633 issuer | 2.1103 | 133.29 | 406.84 | 1.80 | 2.6850 / late-cycle/peak |
| cash / crude | 2.7633 issuer | 1.5211 | 206.52 | 366.16 | 2.34 | 2.6850 / late-cycle/peak |
| risk / crude | 2.7633 issuer | 2.1103 | 133.29 | 406.84 | 1.80 | 2.6850 / late-cycle/peak |
| smooth / crude | 2.7633 issuer | 2.1103 | 133.29 | 406.84 | 1.80 | 2.6850 / late-cycle/peak |
| combined / crude | 2.7633 issuer | 1.5211 | 206.52 | 366.16 | 2.34 | 2.6850 / late-cycle/peak |
| reference_risk_smooth / crude | 2.7633 issuer | 2.1103 | 133.29 | 406.84 | 1.80 | 2.6850 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## SB

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; continuation of board-set dividend is a forecast, not a contractual payment; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 9.0070 | 7.00–11.37 | HOLD (fairly valued) | False | robust | 11.00 |
| cash | 8.8091 | 6.76–11.21 | HOLD (fairly valued) | True | robust | 11.00 |
| reference | 9.0070 | 7.00–11.37 | HOLD (fairly valued) | False | robust | 11.00 |
| risk | 9.1754 | 7.18–11.52 | HOLD (fairly valued) | False | robust | 8.51 |
| smooth | 8.9734 | 6.94–11.37 | HOLD (fairly valued) | False | robust | 11.00 |
| cash_reference | 8.8091 | 6.76–11.21 | HOLD (fairly valued) | True | robust | 11.00 |
| cash_reference_risk | 8.9727 | 6.93–11.37 | HOLD (fairly valued) | False | flips (cheap/rich) | 8.51 |
| combined | 8.9386 | 6.86–11.37 | HOLD (fairly valued) | False | flips (cheap/rich) | 8.51 |
| reference_risk_smooth | 9.1331 | 7.10–11.52 | HOLD (fairly valued) | False | robust | 8.51 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 1.1520 | 408.27 | 511.45 | 7.8126 |
| cash | 0.6000 | 129.41 | 397.75 | 7.8059 |
| reference | 1.1520 | 408.27 | 511.45 | 7.8126 |
| risk | 1.1520 | 408.27 | 511.45 | 8.2215 |
| smooth | 1.1520 | 408.27 | 511.45 | 7.7189 |
| cash_reference | 0.6000 | 129.41 | 397.75 | 7.8059 |
| cash_reference_risk | 0.6000 | 129.41 | 397.75 | 8.2144 |
| combined | 0.6000 | 129.41 | 397.75 | 8.1157 |
| reference_risk_smooth | 1.1520 | 408.27 | 511.45 | 8.1228 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / dry_bulk | 10.7186 issuer | 1.2717 | 436.70 | 511.45 | 10.87 | 1.7216 / late-cycle/peak |
| cash / dry_bulk | 10.7186 issuer | 0.6000 | 170.02 | 397.75 | 10.98 | 1.7216 / late-cycle/peak |
| risk / dry_bulk | 10.7186 issuer | 1.2717 | 436.70 | 511.45 | 10.87 | 1.7216 / late-cycle/peak |
| smooth / dry_bulk | 10.7186 issuer | 1.2717 | 436.70 | 511.45 | 10.87 | 1.7216 / late-cycle/peak |
| combined / dry_bulk | 10.7186 issuer | 0.6000 | 170.02 | 397.75 | 10.98 | 1.7216 / late-cycle/peak |
| reference_risk_smooth / dry_bulk | 10.7186 issuer | 1.2717 | 436.70 | 511.45 | 10.87 | 1.7216 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## SBLK

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 28.2003 | 22.28–34.49 | TRIM/SHORT (overvalued) | True | flips (cheap/fair) | 11.00 |
| cash | 27.8987 | 21.91–34.29 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| reference | 28.2003 | 22.28–34.49 | TRIM/SHORT (overvalued) | True | flips (cheap/fair) | 11.00 |
| risk | 28.7271 | 22.79–34.95 | TRIM/SHORT (overvalued) | True | robust | 8.29 |
| smooth | 28.1599 | 22.29–34.49 | TRIM/SHORT (overvalued) | True | flips (cheap/fair) | 11.00 |
| cash_reference | 27.8987 | 21.91–34.29 | TRIM/SHORT (overvalued) | True | robust | 11.00 |
| cash_reference_risk | 28.4229 | 22.42–34.74 | TRIM/SHORT (overvalued) | True | flips (fair/rich) | 8.29 |
| combined | 28.3724 | 22.43–34.74 | TRIM/SHORT (overvalued) | True | flips (fair/rich) | 8.29 |
| reference_risk_smooth | 28.6674 | 22.81–34.95 | TRIM/SHORT (overvalued) | True | robust | 8.29 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 8.8749 | 617.40 | 1,179.00 | 19.0387 |
| cash | 7.5551 | 441.98 | 1,061.10 | 19.4959 |
| reference | 8.8749 | 617.40 | 1,179.00 | 19.0387 |
| risk | 8.8749 | 617.40 | 1,179.00 | 20.1256 |
| smooth | 8.8749 | 617.40 | 1,179.00 | 18.8923 |
| cash_reference | 7.5551 | 441.98 | 1,061.10 | 19.4959 |
| cash_reference_risk | 7.5551 | 441.98 | 1,061.10 | 20.6088 |
| combined | 7.5551 | 441.98 | 1,061.10 | 20.4540 |
| reference_risk_smooth | 8.8749 | 617.40 | 1,179.00 | 19.9708 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / dry_bulk | 33.2679 issuer | 12.6096 | 639.34 | 1,179.00 | 25.81 | 1.5987 / late-cycle/peak |
| cash / dry_bulk | 33.2679 issuer | 11.4750 | 443.25 | 1,061.10 | 26.21 | 1.5987 / late-cycle/peak |
| risk / dry_bulk | 33.2679 issuer | 12.6096 | 639.34 | 1,179.00 | 25.81 | 1.5987 / late-cycle/peak |
| smooth / dry_bulk | 33.2679 issuer | 12.6096 | 639.34 | 1,179.00 | 26.31 | 1.5987 / late-cycle/peak |
| combined / dry_bulk | 33.2679 issuer | 11.4750 | 443.25 | 1,061.10 | 26.70 | 1.5987 / late-cycle/peak |
| reference_risk_smooth / dry_bulk | 33.2679 issuer | 12.6096 | 639.34 | 1,179.00 | 26.31 | 1.5987 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## STNG

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; continuation of board-set dividend is a forecast, not a contractual payment; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; commitments have no mapped delivery schedule; remain outstanding, not assumed paid; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 75.9705 | 55.01–92.63 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash | 75.6452 | 54.56–92.36 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| reference | 75.9705 | 55.01–92.63 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| risk | 78.1194 | 57.13–95.17 | TRIM/SHORT (overvalued) | True | n/a | 6.82 |
| smooth | 75.9541 | 55.08–92.63 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference | 75.6452 | 54.56–92.36 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference_risk | 77.7647 | 56.63–94.87 | TRIM/SHORT (overvalued) | True | n/a | 6.82 |
| combined | 77.7612 | 56.65–94.87 | TRIM/SHORT (overvalued) | True | n/a | 6.82 |
| reference_risk_smooth | 78.1187 | 57.13–95.17 | TRIM/SHORT (overvalued) | True | n/a | 6.82 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 3.6000 | 2,820.75 | 855.00 | 68.0548 |
| cash | 3.6000 | 2,678.02 | 769.50 | 67.1512 |
| reference | 3.6000 | 2,820.75 | 855.00 | 68.0548 |
| risk | 3.6000 | 2,820.75 | 855.00 | 74.1985 |
| smooth | 3.6000 | 2,820.75 | 855.00 | 68.1068 |
| cash_reference | 3.6000 | 2,678.02 | 769.50 | 67.1512 |
| cash_reference_risk | 3.6000 | 2,678.02 | 769.50 | 73.2134 |
| combined | 3.6000 | 2,678.02 | 769.50 | 73.2701 |
| reference_risk_smooth | 3.6000 | 2,820.75 | 855.00 | 74.2553 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / product | 76.2196 issuer | 3.6000 | 2,557.91 | 855.00 | 77.31 | 1.9094 / late-cycle/peak |
| cash / product | 76.2196 issuer | 3.6000 | 2,415.18 | 769.50 | 76.17 | 1.9094 / late-cycle/peak |
| risk / product | 76.2196 issuer | 3.6000 | 2,557.91 | 855.00 | 77.31 | 1.9094 / late-cycle/peak |
| smooth / product | 76.2196 issuer | 3.6000 | 2,557.91 | 855.00 | 77.31 | 1.9094 / late-cycle/peak |
| combined / product | 76.2196 issuer | 3.6000 | 2,415.18 | 769.50 | 76.17 | 1.9094 / late-cycle/peak |
| reference_risk_smooth / product | 76.2196 issuer | 3.6000 | 2,557.91 | 855.00 | 77.31 | 1.9094 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## TEN

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; continuation of board-set dividend is a forecast, not a contractual payment; joint sector scenario mapping required for one issuer-level cash policy; no marginal-sleeve payout summation; preferred/NCI allocation and distributions require separate reconciliation; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 68.1457 | 48.70–85.19 | BUY (undervalued) | True | n/a | 11.00 |
| cash | unavailable | — | — | — | — | — |
| reference | 68.1457 | 48.70–85.19 | BUY (undervalued) | True | n/a | 11.00 |
| risk | 68.5330 | 49.07–85.63 | BUY (undervalued) | True | n/a | 10.03 |
| smooth | 68.1696 | 48.83–85.19 | BUY (undervalued) | True | n/a | 11.00 |
| cash_reference | unavailable | — | — | — | — | — |
| cash_reference_risk | unavailable | — | — | — | — | — |
| combined | unavailable | — | — | — | — | — |
| reference_risk_smooth | 68.5598 | 49.22–85.63 | BUY (undervalued) | True | n/a | 10.03 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 15.7965 | 1,067.93 | 2,102.18 | 51.5963 |
| reference | 15.7965 | 1,067.93 | 2,102.18 | 51.5963 |
| risk | 15.7965 | 1,067.93 | 2,102.18 | 52.6204 |
| smooth | 15.7965 | 1,067.93 | 2,102.18 | 51.6667 |
| reference_risk_smooth | 15.7965 | 1,067.93 | 2,102.18 | 52.6922 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 91.9147 issuer | 7.0597 | corporate; see joint ledger | corporate | 43.17 | 2.0838 / late-cycle/peak |
| legacy / product | 91.9147 issuer | 4.3195 | corporate; see joint ledger | corporate | 8.86 | 1.6775 / late-cycle/peak |
| legacy / lng | 91.9147 issuer | 3.2292 | corporate; see joint ledger | corporate | 5.76 | 0.7059 / below-mid |
| risk / crude | 91.9147 issuer | 7.0597 | corporate; see joint ledger | corporate | 43.17 | 2.0838 / late-cycle/peak |
| risk / product | 91.9147 issuer | 4.3195 | corporate; see joint ledger | corporate | 8.86 | 1.6775 / late-cycle/peak |
| risk / lng | 91.9147 issuer | 3.2292 | corporate; see joint ledger | corporate | 5.76 | 0.7059 / below-mid |
| smooth / crude | 91.9147 issuer | 7.0597 | corporate; see joint ledger | corporate | 43.17 | 2.0838 / late-cycle/peak |
| smooth / product | 91.9147 issuer | 4.3195 | corporate; see joint ledger | corporate | 8.90 | 1.6775 / late-cycle/peak |
| smooth / lng | 91.9147 issuer | 3.2292 | corporate; see joint ledger | corporate | 5.68 | 0.7059 / below-mid |
| reference_risk_smooth / crude | 91.9147 issuer | 7.0597 | corporate; see joint ledger | corporate | 43.17 | 2.0838 / late-cycle/peak |
| reference_risk_smooth / product | 91.9147 issuer | 4.3195 | corporate; see joint ledger | corporate | 8.90 | 1.6775 / late-cycle/peak |
| reference_risk_smooth / lng | 91.9147 issuer | 3.2292 | corporate; see joint ledger | corporate | 5.68 | 0.7059 / below-mid |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## TNK

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; continuation of board-set dividend is a forecast, not a contractual payment; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 87.5918 | 71.81–102.30 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash | 87.1074 | 71.39–101.65 | rich · cycle position (not a short) | True | robust | 11.00 |
| reference | 87.5918 | 71.81–102.30 | rich · cycle position (not a short) | True | robust | 11.00 |
| risk | 90.1514 | 74.34–105.42 | rich · cycle position (not a short) | True | flips (fair/cheap) | 6.48 |
| smooth | 87.5895 | 71.79–102.30 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference | 87.1074 | 71.39–101.65 | rich · cycle position (not a short) | True | robust | 11.00 |
| cash_reference_risk | 89.7604 | 73.96–104.93 | rich · cycle position (not a short) | True | robust | 6.48 |
| combined | 89.7674 | 74.02–104.93 | rich · cycle position (not a short) | True | robust | 6.48 |
| reference_risk_smooth | 90.1599 | 74.40–105.42 | rich · cycle position (not a short) | True | flips (fair/cheap) | 6.48 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 11.1885 | 2,098.21 | 0.00 | 79.7026 |
| cash | 2.0000 | 2,235.42 | 0.00 | 86.4017 |
| reference | 11.1885 | 2,098.21 | 0.00 | 79.7026 |
| risk | 11.1885 | 2,098.21 | 0.00 | 87.5259 |
| smooth | 11.1885 | 2,098.21 | 0.00 | 79.7240 |
| cash_reference | 2.0000 | 2,235.42 | 0.00 | 86.4017 |
| cash_reference_risk | 2.0000 | 2,235.42 | 0.00 | 94.8826 |
| combined | 2.0000 | 2,235.42 | 0.00 | 94.9061 |
| reference_risk_smooth | 11.1885 | 2,098.21 | 0.00 | 87.5494 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / crude | 84.6025 issuer | 9.5555 | 1,928.31 | 0.00 | 93.98 | 2.1638 / late-cycle/peak |
| cash / crude | 84.6025 issuer | 2.0000 | 2,008.89 | 0.00 | 100.82 | 2.1638 / late-cycle/peak |
| risk / crude | 84.6025 issuer | 9.5555 | 1,928.31 | 0.00 | 93.98 | 2.1638 / late-cycle/peak |
| smooth / crude | 84.6025 issuer | 9.5555 | 1,928.31 | 0.00 | 93.98 | 2.1638 / late-cycle/peak |
| combined / crude | 84.6025 issuer | 2.0000 | 2,008.89 | 0.00 | 100.82 | 2.1638 / late-cycle/peak |
| reference_risk_smooth / crude | 84.6025 issuer | 9.5555 | 1,928.31 | 0.00 | 93.98 | 2.1638 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.

## TRMD

**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.

Blockers: forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence; book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only; remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved; transportation beta proxy requires shipping-sector calibration; funding-cost and cash-risk conventions require owner review.

| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |
|---|---:|---|---|---|---|---:|
| legacy | 35.1413 | 21.09–47.75 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash | 35.1213 | 20.90–47.93 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| reference | 35.1413 | 21.09–47.75 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| risk | 35.9008 | 21.73–48.74 | TRIM/SHORT (overvalued) | True | n/a | 7.57 |
| smooth | 35.1445 | 21.08–47.75 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference | 35.1213 | 20.90–47.93 | TRIM/SHORT (overvalued) | True | n/a | 11.00 |
| cash_reference_risk | 35.8235 | 21.50–48.82 | TRIM/SHORT (overvalued) | True | n/a | 7.57 |
| combined | 35.8287 | 21.48–48.82 | TRIM/SHORT (overvalued) | True | n/a | 7.57 |
| reference_risk_smooth | 35.9066 | 21.70–48.74 | TRIM/SHORT (overvalued) | True | n/a | 7.57 |

| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |
|---|---:|---:|---:|---:|
| legacy | 15.5050 | 905.71 | 1,076.20 | 24.9209 |
| cash | 18.5701 | 193.43 | 968.58 | 21.9944 |
| reference | 15.5050 | 905.71 | 1,076.20 | 24.9209 |
| risk | 15.5050 | 905.71 | 1,076.20 | 26.7455 |
| smooth | 15.5050 | 905.71 | 1,076.20 | 24.9364 |
| cash_reference | 18.5701 | 193.43 | 968.58 | 21.9944 |
| cash_reference_risk | 18.5701 | 193.43 | 968.58 | 23.6048 |
| combined | 18.5701 | 193.43 | 968.58 | 23.6215 |
| reference_risk_smooth | 15.5050 | 905.71 | 1,076.20 | 26.7622 |

| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |
|---|---:|---:|---:|---:|---:|---|
| legacy / product | 32.3026 issuer | 12.0838 | 787.11 | 1,076.20 | 28.38 | 1.9384 / late-cycle/peak |
| cash / product | 32.3026 issuer | 13.8892 | 206.00 | 968.58 | 25.94 | 1.9384 / late-cycle/peak |
| risk / product | 32.3026 issuer | 12.0838 | 787.11 | 1,076.20 | 28.38 | 1.9384 / late-cycle/peak |
| smooth / product | 32.3026 issuer | 12.0838 | 787.11 | 1,076.20 | 28.38 | 1.9384 / late-cycle/peak |
| combined / product | 32.3026 issuer | 13.8892 | 206.00 | 968.58 | 25.94 | 1.9384 / late-cycle/peak |
| reference_risk_smooth / product | 32.3026 issuer | 12.0838 | 787.11 | 1,076.20 | 28.38 | 1.9384 / late-cycle/peak |

Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.
