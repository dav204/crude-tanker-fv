# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.9%) + dry_bulk (72.9%) + containerships (3.2%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $15.74
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $16.19 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.05 (-10.7% vs price)
- **Breakeven TCE (scenario-invariant):** $73,290/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.02 | $21.30 | $20.59–$22.05 | 6.37× | 0.70 | $21.94 | $82,095 | 1.12× |
| Pre-MoU baseline | 45% | 0.82× | $14.66 | $13.76 | $13.27–$14.26 | 2.25× | 0.70 | $12.42 | $41,278 | 0.56× |
| MoU base case | 18% | 0.76× | $11.96 | $10.80 | $10.34–$11.26 | 1.85× | 0.70 | $9.54 | $32,613 | 0.44× |
| MoU bear | 12% | 0.72× | $10.27 | $8.86 | $8.48–$9.24 | 1.53× | 0.70 | $7.27 | $27,888 | 0.38× |
| **Probability-weighted** | | | | **$14.05** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.56
- **Downside (worst scenario − price):** $-6.88
- **Expected value vs current** (weighted FV − price): $-1.69 (-10.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
