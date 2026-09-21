# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.1%) + containerships (3.1%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $20.29
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $13.36 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.75 (-47.0% vs price)
- **Breakeven TCE (scenario-invariant):** $325,779/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $15.71 | $16.37 | $15.68–$17.11 | 6.47× | 0.70 | $17.91 | $83,364 | 0.26× |
| Pre-MoU baseline | 59% | 1.00× | $11.06 | $10.62 | $10.11–$11.15 | 2.65× | 0.70 | $9.97 | $44,171 | 0.14× |
| MoU base case | 0% | 0.90× | $8.49 | $7.81 | $7.33–$8.29 | 2.17× | 0.70 | $7.06 | $35,031 | 0.11× |
| MoU bear | 13% | 0.80× | $6.64 | $5.64 | $5.25–$6.02 | 1.59× | 0.70 | $4.44 | $28,380 | 0.09× |
| **Probability-weighted** | | | | **$10.75** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-3.92
- **Downside (worst scenario − price):** $-14.65
- **Expected value vs current** (weighted FV − price): $-9.54 (-47.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
