# Economic-method experiment, 2026-09-22

Owner authority: implement the approved economic-method review in isolation. Nothing
in this study authorizes production adoption, a baseline reset or an order.
The frozen manifest identifies the production commit, accepted publication and
consumer registry. `assumptions.json` is committed before changed-FV evaluation.

## Experiments and attribution

Evaluate legacy, cash only, reference only, risk only, smooth only; then cash →
reference → risk → smooth. Report the combined delta less the sum of independent
deltas as interaction, not independent causal attribution. Low/base/high are
input corners, not probabilistic confidence intervals or guaranteed FV ordering.
Retain every ticker and sleeve; unavailable computations print null and a reason.
Parity is a separate registered three-vintage A/B with its original kill condition.

Price, probabilities, scenarios, vessel marks, family sets, categorical cycle bands,
governance haircuts, fleet schedules and valuation date stay frozen. Newbuild NAV
discount remains 11%, parity WACC remains 8% with its existing 7–10% grid. Reference
clamps/elasticity/structural multipliers are untouched. No tests or research calls
publish, consume live state, email or ping a healthcheck.

## Cash contract

Dollar ledgers distinguish ordinary common accounting income from pre-depreciation
operating earnings and operating cash. Depreciation is noncash; reserves restrict
distribution without destroying assets. Interest follows opening financing on the
frozen funding-cost assumption. Preferred distributions reduce common income/cash;
NCI must not be treated as a preferred coupon. Terminal claims roll forward cash,
debt, leases, working capital, outstanding commitments, advances and sale assets.
No external financing or buybacks are invented. Negative cash remains a disclosed
funding gap; common distributions cannot exceed available cash above the specified
minimum. A declared/intended floor that cannot be funded produces a shortfall.

All 25 rows require verified forward schedules before adoption. Current source
observations and analyst forecast assumptions are separate. DHT/SBLK/SB depreciation
uses dated reported run rates; GNK uses the existing Q1 observation. Other names use
a **replacement-mark/25-year proxy**, NOT reported book depreciation, with 0.5/1/1.5
stress. This is a bounded diagnostic, never evidence that an accounting schedule
has been sourced. Maintenance-capex stress is 0/1/2% of opening fleet value annually;
unmapped debt amortization is 0/5/10% annually. These are analyst stresses, not
company guidance. FLNG/INSW scheduled-amortization estimates retain their committed
preregistration evidence. SB's committed annual capex and February 2027 bond are
explicit; within-year capex allocation remains assumed. Other newbuild obligations
use disclosed total commitments allocated by hull count at delivery; installment
timing/draws remain adoption blockers. Missing asset-sales and advances-release
reconciliations remain open, never silently certified as zero actual activity.

GNK reserve base $19.5m is Q3 guidance, then a flat forecast with ±50% stress. SBLK
uses the revised cash-flow formula and $2.1m per operating vessel minimum. TRMD's
liquidity policy uses an explicitly unsourced $1/2/3m-per-vessel reserve bracket;
the actual issuer threshold must be supplied before adoption. Fixed declared DPS
continuation is a forecast; discretionary earnings ratios span zero to full payout.
HAFN/BWLP ladders use independent fleet values only as a disclosed diagnostic proxy
until the issuer's NLTV/net-leverage definition is reconciled. Semiannual policies
retain their payment cadence. Hybrids have **no** new scenario-weighted cash FV until
an issuer-level joint-scenario mapping is approved; cash-capacity constraints are
nonlinear and cannot be applied independently to marginal sleeves.

## Risk and reference proposals

External calibration: Damodaran September 1, 2026 USD Treasury convention 4.75% plus
4.14% trailing adjusted ERP, January 2026 cash-corrected Transportation beta 0.71.
Base operating asset return = 7.6894%. Low/high: beta 0.61/0.81 (analyst sensitivity)
with published alternative ERP 3.56%/6.05%, giving 6.9216%/9.6505%. All six shipping
sectors initially inherit this broad proxy; **sector-level risk differentiation is
not established**, an adoption blocker rather than invented precision. Sector
weights are exported for hybrids. Funding cost is annual interest/carried financing
unless a dated disclosed weighted rate is available. This is not a fresh marginal
borrowing quote; no tax shield is assumed for the tonnage-tax/low-tax book.

Relevering: E = unhaircut independent common NAV, D = carried debt + separate leases,
P = preferred/NCI claims, C = carried cash. Operating claims = E+D+P-C.
`rE = [rA*(E+D+P-C) + rf*C - rD*D - preferred_return]/E`.
Known preferred coupons are used for SB/GSL; unresolved NCI/preferred stacks use
asset-risk-return sensitivity only and remain blocked. Nonpositive equity or
nonfinite values are unavailable. No artificial caps or broker fitting.
Freeze parent-company rE across scenario/mark sensitivities to isolate cash/marks;
do not recompute leverage on scenario-flexed NAV. Justified P/NAV and breakevens use
that same rE. Newbuild delivery discount and parity WACC stay separate.

Reference experiment: freeze the current curve with its exact mark hash and calendar
periods as a **proposed pair**, not a claimed historical strike-vintage match. Export
source dates and reference identity. Missing historical pairing blocks adoption;
reference-level ±10% stress is registered before outcomes. FFA-only refresh must
not change fixed-case FV with these references; scenario weight changes must not
change individual case NAV. No market-relative deck regeneration is authorized.

Cycle smoothing interpolates `(ratio,wNAV,terminal)` through
`(.30,.30,1.10),(.65,.40,1.05),(1,.50,1),(1.35,.60,.95),(1.70,.70,.90)`;
clamp tails. Outer anchors are a proposal awaiting owner review. Labels retain
the existing strict-boundary convention. Expected mixed-sign FV effects near bands;
invariant at anchor centres and outside the outer anchors.

## Expected moves and stop rules

All independent current NAVs must remain exactly unchanged. Cash changes dividends
and terminal claims together: depreciation-only lowers accounting payout but retains
cash; principal repayment reduces both cash and debt. Maintenance consumes cash.
Newbuild payment reduces cash and the outstanding obligation together; the vessel is
already in the terminal fleet. Timing, tax and haircut effects prevent general FV
neutrality claims. Lower rE raises PV for positive cash flows; higher rE lowers it.
Reference base is a migration control expected to be invariant for aligned horizons;
brackets expose reference uncertainty. Calendar extensions are not silently added.

Use existing >2pp drift / band-flip / >0.05 broker-second-difference checks and sanity
rules. Gate failures are reported, not waived, re-ratified or used to tune inputs.
Unexplained independent NAV movement, violated ledger identities, reference leakage,
changed probabilities or production writes fail the experiment. Missing material
inputs or dependencies block adoption, even when arithmetic/tests pass.

The LR1 anchor round stays separately registered and blocks adoption sequencing.
Parity retains its existing full-book ≥80% dated-class coverage requirement,
three-vintage stability criterion and lock-time family tests. A failed/void run
does not authorize a narrower retroactive test or denominator adoption.

## Evidence sources

Per-name URLs, dates, mappings, schedules and known gaps are in `assumptions.json`.
Committed source inputs remain recoverable from `frozen/manifest.json`'s commit.
Existing policies in `inputs/dividend_policies` are evidence of the old model only.
Methods and source coverage must be reviewed separately from their numeric effect.
