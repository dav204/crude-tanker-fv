# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.8%) + product (15.8%) + lng (11.3%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $35.76
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.70 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $65.49 (+83.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $121.10 | $84.64 | $83.59–$85.85 | 4.40× | 0.70 | $84.33 | $148,031 | 84556351217838733123823599616.00× |
| Pre-MoU baseline | 45% | 1.04× | $99.85 | $69.51 | $68.86–$70.23 | 2.87× | 0.70 | $69.09 | $92,217 | 52675262577190058982543196160.00× |
| MoU base case | 18% | 0.75× | $62.04 | $45.06 | $44.60–$45.54 | 1.43× | 0.60 | $47.44 | $45,848 | 26188856601998336671570984960.00× |
| MoU bear | 12% | 0.72× | $55.61 | $41.19 | $40.77–$41.62 | 1.20× | 0.60 | $43.90 | $37,947 | 21675889616647792688308944896.00× |
| **Probability-weighted** | | | | **$65.49** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+48.88
- **Downside (worst scenario − price):** $+5.43
- **Expected value vs current** (weighted FV − price): $+29.73 (+83.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
