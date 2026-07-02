# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.8%) + product (15.8%) + lng (11.3%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $35.37
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.70 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $64.35 (+81.9% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $121.10 | $84.64 | $83.59–$85.85 | 4.40× | 0.70 | $84.33 | $148,031 | n/a |
| Pre-MoU baseline | 45% | 1.04× | $99.85 | $69.51 | $68.86–$70.23 | 2.87× | 0.70 | $69.09 | $92,217 | n/a |
| MoU base case | 18% | 0.75× | $62.04 | $45.06 | $44.60–$45.54 | 1.43× | 0.60 | $47.44 | $45,848 | n/a |
| MoU bear | 12% | 0.72× | $55.61 | $41.19 | $40.77–$41.62 | 1.20× | 0.60 | $43.90 | $37,947 | n/a |
| **Probability-weighted** | | | | **$64.35** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+49.27
- **Downside (worst scenario − price):** $+3.32
- **Expected value vs current** (weighted FV − price): $+28.98 (+81.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
