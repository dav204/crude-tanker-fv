# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (73.0%) + product (15.6%) + lng (11.4%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $37.11
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.13 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $62.56 (+68.6% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $120.40 | $80.95 | $80.66–$81.28 | 4.38× | 0.70 | $73.17 | $147,925 | 84612398095385195910413680640.00× |
| Pre-MoU baseline | 45% | 1.04× | $99.11 | $66.91 | $66.74–$67.11 | 2.86× | 0.70 | $60.89 | $92,156 | 52712710963434568926980210688.00× |
| MoU base case | 18% | 0.75× | $61.56 | $42.25 | $42.13–$42.38 | 1.42× | 0.60 | $40.55 | $45,842 | 26221150031079880596656226304.00× |
| MoU bear | 12% | 0.71× | $55.16 | $38.38 | $38.27–$38.50 | 1.20× | 0.60 | $37.18 | $37,949 | 21706881690567670700787630080.00× |
| **Probability-weighted** | | | | **$62.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+43.84
- **Downside (worst scenario − price):** $+1.27
- **Expected value vs current** (weighted FV − price): $+25.45 (+68.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
