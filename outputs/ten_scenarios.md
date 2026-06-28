# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.9%) + product (15.7%) + lng (11.4%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $36.72
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $87.70 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $64.93 (+76.8% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $119.85 | $83.96 | $82.91–$85.17 | 4.40× | 0.70 | $84.10 | $148,320 | 84682661610880228294091866112.00× |
| Pre-MoU baseline | 45% | 1.04× | $98.71 | $68.89 | $68.24–$69.61 | 2.87× | 0.70 | $68.87 | $92,356 | 52730458994036939688874344448.00× |
| MoU base case | 18% | 0.75× | $61.24 | $44.66 | $44.20–$45.13 | 1.43× | 0.60 | $47.28 | $45,914 | 26214555497332057365907767296.00× |
| MoU bear | 12% | 0.71× | $54.85 | $40.82 | $40.41–$41.25 | 1.20× | 0.60 | $43.75 | $37,998 | 21695004009450586979742777344.00× |
| **Probability-weighted** | | | | **$64.93** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+47.24
- **Downside (worst scenario − price):** $+4.10
- **Expected value vs current** (weighted FV − price): $+28.21 (+76.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
