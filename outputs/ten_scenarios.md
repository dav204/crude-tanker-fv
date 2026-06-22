# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.9%) + product (15.7%) + lng (11.4%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $38.29
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $87.56 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $64.84 (+69.3% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $119.69 | $83.85 | $82.80–$85.06 | 4.39× | 0.70 | $84.01 | $148,125 | 84660658735880967186139840512.00× |
| Pre-MoU baseline | 45% | 1.04× | $98.56 | $68.79 | $68.14–$69.51 | 2.87× | 0.70 | $68.79 | $92,256 | 52728889875248467293167943680.00× |
| MoU base case | 18% | 0.75× | $61.14 | $44.59 | $44.14–$45.07 | 1.42× | 0.60 | $47.22 | $45,874 | 26219257313437483837834657792.00× |
| MoU bear | 12% | 0.71× | $54.76 | $40.77 | $40.35–$41.19 | 1.20× | 0.60 | $43.70 | $37,970 | 21701827189887371263072010240.00× |
| **Probability-weighted** | | | | **$64.84** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+45.56
- **Downside (worst scenario − price):** $+2.48
- **Expected value vs current** (weighted FV − price): $+26.55 (+69.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
