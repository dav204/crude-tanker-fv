# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (22.7%) + dry_bulk (74.0%) + containerships (3.3%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $14.10
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $15.40 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.69 (+11.3% vs price)
- **Breakeven TCE (scenario-invariant):** $43,759/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.32 | $21.61 | $20.91–$22.37 | 6.31× | 0.70 | $22.29 | $79,243 | 1.81× |
| Pre-MoU baseline | 45% | 1.11× | $16.63 | $16.15 | $15.58–$16.75 | 3.97× | 0.70 | $15.88 | $53,220 | 1.22× |
| MoU base case | 18% | 0.76× | $12.04 | $10.88 | $10.41–$11.34 | 1.85× | 0.70 | $9.72 | $32,027 | 0.73× |
| MoU bear | 12% | 0.72× | $10.26 | $8.85 | $8.47–$9.23 | 1.53× | 0.70 | $7.37 | $27,455 | 0.63× |
| **Probability-weighted** | | | | **$15.69** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.51
- **Downside (worst scenario − price):** $-5.25
- **Expected value vs current** (weighted FV − price): $+1.59 (+11.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
