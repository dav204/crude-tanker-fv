# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.9%) + product (15.7%) + lng (11.4%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $38.29
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $87.56 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $62.23 (+62.5% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $119.69 | $80.51 | $80.22–$80.85 | 4.39× | 0.70 | $72.88 | $148,125 | 84660658735880984778325884928.00× |
| Pre-MoU baseline | 45% | 1.04× | $98.56 | $66.58 | $66.40–$66.77 | 2.87× | 0.70 | $60.67 | $92,256 | 52728889875248467293167943680.00× |
| MoU base case | 18% | 0.75× | $61.14 | $42.01 | $41.88–$42.14 | 1.42× | 0.60 | $40.38 | $45,874 | 26219257313437483837834657792.00× |
| MoU bear | 12% | 0.71× | $54.76 | $38.15 | $38.03–$38.27 | 1.20× | 0.60 | $37.01 | $37,970 | 21701827189887371263072010240.00× |
| **Probability-weighted** | | | | **$62.23** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+42.22
- **Downside (worst scenario − price):** $-0.14
- **Expected value vs current** (weighted FV − price): $+23.94 (+62.5%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
