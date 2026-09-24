# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.1%) + product (16.1%) + lng (11.7%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $46.97
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $91.91 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $68.15 (+45.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $123.07 | $85.19 | $84.21–$86.32 | 4.30× | 0.70 | $82.95 | $144,265 | n/a |
| Pre-MoU baseline | 59% | 1.00× | $98.87 | $67.91 | $67.34–$68.52 | 2.12× | 0.70 | $65.43 | $73,869 | n/a |
| MoU base case | 0% | 0.90× | $81.21 | $55.92 | $55.52–$56.34 | 1.73× | 0.70 | $53.42 | $52,503 | n/a |
| MoU bear | 13% | 0.80× | $69.01 | $48.70 | $48.30–$49.11 | 1.28× | 0.60 | $48.80 | $39,378 | n/a |
| **Probability-weighted** | | | | **$68.15** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+38.22
- **Downside (worst scenario − price):** $-0.91
- **Expected value vs current** (weighted FV − price): $+21.18 (+45.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
