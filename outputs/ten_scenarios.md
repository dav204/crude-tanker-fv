# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (71.6%) + product (16.5%) + lng (11.9%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $52.55
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.16 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $65.59 (+24.8% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $119.14 | $82.53 | $81.55–$83.66 | 4.27× | 0.70 | $80.52 | $144,175 | n/a |
| Pre-MoU baseline | 59% | 1.00× | $95.21 | $65.42 | $64.85–$66.03 | 2.11× | 0.70 | $63.07 | $73,927 | n/a |
| MoU base case | 0% | 0.90× | $77.55 | $53.43 | $53.03–$53.85 | 1.72× | 0.70 | $51.04 | $52,372 | n/a |
| MoU bear | 13% | 0.80× | $65.43 | $46.26 | $45.86–$46.66 | 1.27× | 0.60 | $46.41 | $39,292 | n/a |
| **Probability-weighted** | | | | **$65.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+29.98
- **Downside (worst scenario − price):** $-8.96
- **Expected value vs current** (weighted FV − price): $+13.04 (+24.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
