# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.0%) + containerships (3.2%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $18.27
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $16.54 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.65 (-25.3% vs price)
- **Breakeven TCE (scenario-invariant):** $165,601/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $19.26 | $19.76 | $19.05–$20.51 | 6.38× | 0.70 | $20.92 | $81,946 | 0.49× |
| Pre-MoU baseline | 62% | 0.95× | $14.23 | $13.44 | $12.95–$13.94 | 2.26× | 0.70 | $12.17 | $41,165 | 0.25× |
| MoU base case | 0% | 0.86× | $11.70 | $10.64 | $10.17–$11.10 | 1.86× | 0.70 | $9.38 | $32,539 | 0.20× |
| MoU bear | 13% | 0.80× | $10.11 | $8.77 | $8.39–$9.15 | 1.53× | 0.70 | $7.17 | $27,809 | 0.17× |
| **Probability-weighted** | | | | **$13.65** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.49
- **Downside (worst scenario − price):** $-9.50
- **Expected value vs current** (weighted FV − price): $-4.62 (-25.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
