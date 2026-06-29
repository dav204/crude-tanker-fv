# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.5%) + product (16.0%) + lng (11.5%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $36.72
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $86.95 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $64.54 (+75.7% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $118.92 | $83.45 | $82.41–$84.67 | 4.39× | 0.70 | $83.94 | $148,079 | 84499698246516870173570367488.00× |
| Pre-MoU baseline | 45% | 1.04× | $97.94 | $68.47 | $67.82–$69.19 | 2.86× | 0.70 | $68.74 | $92,159 | 52589726012158229980702048256.00× |
| MoU base case | 18% | 0.75× | $60.71 | $44.40 | $43.94–$44.87 | 1.42× | 0.60 | $47.19 | $45,853 | 26165499452979909790196039680.00× |
| MoU bear | 12% | 0.71× | $54.33 | $40.56 | $40.15–$40.99 | 1.20× | 0.60 | $43.66 | $37,933 | 21646141668465160043339186176.00× |
| **Probability-weighted** | | | | **$64.54** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+46.73
- **Downside (worst scenario − price):** $+3.84
- **Expected value vs current** (weighted FV − price): $+27.82 (+75.7%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
