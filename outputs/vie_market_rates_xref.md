# VIE Market Rates & Trends Cross-Reference (2026-06-03; reframed 2026-06-04 AM; refined 2026-06-04 PM)

**Purpose:** independent-source observation of the VIE Live Analytics
Platform's "Market Rates & Trends" tab, with the **methodology distinction**
between VIE's published series and our framework's rate inputs documented
explicitly. **This is NOT a calibration-gap analysis** (the original framing,
preserved below as Historical Context for the record) — it's a
documentation of two methodologically defensible approaches to historical
comparability that look numerically comparable but are constructed
differently.

## Methodology refinement (2026-06-04 PM) — VIE's class-specific adjustment factors

**New finding:** VIE applies **constant, class-specific adjustment factors**
on the denominator of their "Vs. 10y Avg" calculation:

| Vessel class group | Adjustment factor | Implied adjustment |
|---|---:|---:|
| Dry bulk (Capesize, Panamax, Supramax) | **1.00** | none |
| Tankers (VLCC, Suezmax, Aframax, LR2, MR2) + VLGC | **0.90** | −10% |
| LNG TFDE | **0.70** | −30% |

The factors are **constant quarter-to-quarter** (not recalibrated) and apply
to the denominator. The effective formula is:

```
VIE-implied 10y mean = Q-Live-Est ÷ adjustment_factor ÷ (1 + Vs10yAvg/100)
```

### Most defensible interpretation: within-window structural adjustment

VIE is compensating for **structural changes within the 10-year lookback
window that affect different classes differently**:

- **LNG TFDE (factor 0.70):** The TFDE → MEGI / X-DF / X-DF2.1 propulsion
  transition post-2018 made earlier TFDE rates **not comparable** to the
  modern X-DF2.1 fleet's earning power. A 30% downward adjustment to the
  historical mean represents "what TFDE rates *would have been* if the
  comparable fleet were today's spec." Aligns with our framework's
  reinterpretation of `eco_premium_pct` on the LNGC curve specifically as a
  latest-generation propulsion premium (METHODOLOGY §3.1).
- **Tankers + VLGC (factor 0.90):** More modest structural changes within
  the window — eco-design adoption (post-2014), IMO 2020 fuel transition,
  sanctioned-fleet evolution, route-mix changes (Atlantic basin to
  Asia-Pacific shifts). A 10% downward adjustment represents the cumulative
  earning-power lift from these structural shifts.
- **Dry bulk (factor 1.00):** Relatively continuous market structure over
  2016-2026 — no propulsion transition, no major regulatory step-function.
  No adjustment needed.

**This is a methodology refinement, not an error.** VIE has implicitly
identified that simple unadjusted 10-year arithmetic means **overstate
historical-comparable conditions for classes experiencing within-window
structural shifts**.

### Corrected VIE-implied 10-year means

Applying the factor structure to back-compute:

| Class | VIE Q2-26 | VIE Vs 10y Avg | Multiplier | Factor | **Corrected VIE-implied** | Our 10y | Refined Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| VLCC | $147,358 | +482% | 5.82 | 0.90 | **$28,131** | $40,000 | +$11,869 / **+42%** |
| Suezmax | $182,281 | +652% | 7.52 | 0.90 | **$26,920** | $27,747 | +$827 / **+3%** |
| Aframax | $145,373 | +505% | 6.05 | 0.90 | **$26,665** | $27,600 | +$935 / **+4%** |
| LR2 (clean) | $91,965 | +351% | 4.51 | 0.90 | **$22,640** | $28,000 | +$5,360 / **+24%** |
| MR2 | $44,550 | +228% | 3.28 | 0.90 | **$15,094** | $16,000 | +$906 / **+6%** |
| VLGC | $102,029 | +200% | 3.00 | 0.90 | **$37,789** | (not on watchlist) | — |
| LNG TFDE | $48,213 | −13% | 0.87 | 0.70 | **$79,200** | LNGC $85,000 | +$5,800 / **+7%** |

**The corrected gaps are substantially smaller than the original
unadjusted comparison:**

- **Suezmax, Aframax, MR, LNG converge to within ~7%** — these are
  well-aligned methodologies producing nearly the same number through
  different routes. Methodology delta within noise of source-data
  differences (Baltic poll vs Compass TC vs broker consensus).
- **VLCC (+42%)** and **LR2 (+24%)** still show meaningful gaps even
  after VIE's structural adjustment. VLCC specifically may reflect:
  (a) different base-period anchoring (TD3C vs broader composite),
  (b) a residual TC-vs-spot baseline difference that VIE's 0.90 factor
  doesn't fully bridge, or (c) our $40,000 anchor sitting above the
  cleanest cross-source consensus. LR2 may reflect product-cycle vs
  crude-cycle mean differences specific to clean-tanker route
  composition.
- **The LNG gap collapsing from +53% to +7%** is the most striking
  result. Our spike-inclusive 10y mean and VIE's 30%-haircut historical
  mean **agree within 7%** — they're producing nearly the same number
  through methodologically opposite routes (we include the spike;
  VIE haircuts the entire pre-X-DF2.1 base). That convergence is
  meaningful corroboration that our LNGC anchor is in the right
  neighborhood.

### Implications for the framework

**Still no rate inputs changed.** The refinement narrows the gaps
substantially but the interpretive frame stays the same: two
methodologically defensible approaches to historical comparability.

- **Our approach** uses TC-anchored historical data, which **implicitly**
  adjusts for fleet/market structural shifts because TC rates at each
  historical point reflect market participants' contemporaneous
  expectations including the relevant structural context.
- **VIE's approach** uses (likely) spot-mean historical data with
  **explicit** class-specific adjustment factors compensating for
  within-window structural shifts.

Both are defensible. They produce different numerical magnitudes by
construction; the convergence on Suezmax / Aframax / MR / LNG to within
~7% suggests both are anchored in the right neighborhood for those
classes. The VLCC and LR2 residuals warrant separate empirical
investigation if/when the calibration discipline calls for it — but
neither is a "wrong" framework, and **no recalibration is implied by
this refinement.**

### Self-check item (added to METHODOLOGY)

**"Verify our 10y means are TC-anchored throughout, not spot-anchored.
If any spot-anchored components exist, consider whether an explicit
within-window structural adjustment (analogous to VIE's 0.9/0.7 factors)
would be appropriate."**

This is a hygiene check rather than a known issue. Our framework's
`historical_tce_means.yaml` was constructed from Compass cross-checks
which are TC-derived, so the question is whether any line item
inadvertently mixes spot data without a corresponding structural
adjustment. Not currently flagged as a concern; included as a
recurring-refresh discipline item.

---

## How to read VIE's numbers (revised, 2026-06-04 PM)

Given the adjustment-factor discovery:

- **VIE's published "Vs. 10y Avg" multipliers already include the
  class-specific structural adjustment.** When VIE shows VLCC at "+482%
  vs 10y avg," that 482% is computed against VIE's structurally-adjusted
  10y mean ($28,131 by back-computation), not against a raw unadjusted
  mean. Their published cycle reading is **internally consistent** for
  their methodology.
- **Our cycle position ratio (12M TC / 10y TC mean) is internally
  consistent for our methodology** — TC numerator over TC denominator,
  no structural-adjustment factor needed because the TC anchor
  implicitly captures it.
- **Direct numerical comparison of "VIE's +482%" vs "our 2.79×" is
  still not meaningful** — they're computed against different
  denominators (VIE's structurally-adjusted spot mean vs our TC anchor).
  The unit mismatch from the prior reframe still applies.
- **Directional commentary** ("rates are elevated vs history") reads
  correctly under either framework — both methodologies agree on
  direction across all classes.

The refinement narrows the methodology gap but doesn't eliminate the
non-composability of the magnitudes.

**Source:** VIE Live Analytics Platform, Market Rates & Trends tab
(gid 1944362638), accessed via Claude in Chrome MCP on 2026-06-03.

**Snapshot date:** VIE "Date Last Updated" = 29 May 2026 (same as our
Pareto-anchored watchlist `as_of`).

**Refresh cadence:** quarterly (refresh checklist) and on any material
intra-quarter rate event.

---

## The substantive finding (reframe, 2026-06-04)

**Our 10-year means and VIE's are different physical quantities, not
different estimates of the same quantity.** The +14% to +58% gaps across
vessel classes between our values and back-computed VIE-implied values are
the **expected structural signature of a TC-anchored vs spot-mean baseline
difference, not calibration errors.**

### What our `historical_tce_means.yaml` represents

A **time-charter-anchored 10-year mean** — what you would have locked in
on a one-year time charter over a 10-year window, smoothed by the TC
contract structure. **TC rates structurally exclude negative spot prints**
(owners don't offer multi-month charters at a loss; the floor is at
operating cost, not at zero or negative). Our $40,000/day VLCC anchor
reflects this convention.

### What VIE's implied 10-year mean most plausibly represents

**A raw Baltic spot TCE arithmetic mean** — the equally-weighted average
of daily TD3C (or equivalent) prints over a 10-year window. **Spot TCE
includes deep-negative periods** when freight clearing is below operating
cost: SpotMarketCap reports a 2020-2022 VLCC TD3C TCE floor around
−$34,845/day, which would meaningfully drag a 10-year spot-mean below the
TC-anchored equivalent.

VIE's methodology is **not publicly documented** (16 sources checked
including the VIE Investing Group, Catlin's and Mintzmyer's Seeking Alpha
author pages, X/Twitter accounts, VIE marketing pages, and YouTube — see
research agent findings 2026-06-04). The "raw Baltic spot arithmetic mean"
interpretation is **inferred** from the magnitude of the gap relative to
known spot-vs-TC structural differences, not confirmed by VIE disclosure.

### Methodological implication for the cycle ratio

The cycle-position ratio (METHODOLOGY §2.3) is `12M TC / 10y mean`. **For
the ratio to be physically meaningful, both numerator and denominator must
be unit-equivalent.** Our framework uses TC in both positions — internally
consistent.

If we replaced the denominator with VIE's spot-mean (~$25k for VLCC),
keeping the TC numerator ($111,500), the resulting ratio (4.40×) would
not represent "cycle position" in any defensible sense — it would be a
unit-mismatched number with no physical interpretation. **Switching to
VIE's denominator would break the metric**, not improve it.

### How to read VIE's numbers, then

- **Directional commentary** ("rates are elevated vs history") reads
  correctly under either baseline — both methodologies agree on direction.
- **Magnitude / multipliers** (282%, 482%, 652% vs 10y avg) **do not
  compose** with our cycle-position ratio. A name showing "+482% vs VIE 10y
  avg" is not interchangeable with a name showing "2.79× our cycle
  position." They are different metrics measuring different things.
- **VIE's "Vs. 10y Avg" column is best treated as their internal cycle
  reading**, useful as independent narrative confirmation of regime shifts,
  but NOT as a second-opinion calibration target for our framework's
  10-year means.

### What this changes for the framework

**Nothing structural.** Our 10-year means remain anchored where they are.
The VIE cross-check transitions from "potential calibration gap" status to
"documented methodology difference" status. See METHODOLOGY §10 (Caveats)
and LIMITATIONS.md for the canonical write-up. The vessel curves,
historical_tce_means.yaml values, and cycle-position calculations are
unchanged.

### Scope note

This reframe was prompted by VLCC specifically (the largest visible gap,
+58%). The same TC-vs-spot baseline distinction **likely explains the
Suezmax (+14%), Aframax (+15%), LR2 (+37%), and MR (+18%) gaps** as well,
but empirical confirmation per class is deferred. The +53% LNG gap is
separately and explicitly a deliberate spike-inclusive choice on our side
(see `historical_tce_means.yaml` LNGC comment) — orthogonal to the
TC-vs-spot framing.

---

## Source structure (what's on the VIE tab)

The Market Rates & Trends tab contains:

1. **Shipping Rate Tracker — weekly snapshots.** Multiple consecutive weeks
   (29 May, 22 May, etc.) of rate-level + W/W / M/M / Y/Y per class:
   Dry Bulk (BDI / Capesize / Panamax / Supramax), Containers (Harpex +
   per-TEU class), LPG (Clarksons VLGC), LNG Spot (Clarksons), Crude
   (BDTI + VLCC / Suezmax / Aframax), Clean (BCTI). Useful for: visibility
   on intra-quarter direction and spot-vs-spot trajectory.

2. **Average Market Rates / Expectations — per-quarter forward + historical
   panel.** For Q2-26, Q1-26, Q4-25 (and presumably earlier): "Live Est."
   rate-level per class plus % vs Q-1 (Y/Y), Q-1 (Q/Q), Avg Q (long-run
   quarter-average), and 10y Avg. **VIE's "Live Est." appears to be a
   spot QTD-average** ("realistic level for fixtures 'thus far' into the
   quarter" per VIE's own column header note); the "Vs. 10y Avg" column
   would then most naturally be spot QTD vs spot 10y mean — internally
   consistent with the methodology-difference framing above.

---

## Practical usage (revised)

Given the reframe, the appropriate use of VIE Market Rates & Trends within
our refresh workflow is:

- **Directional cross-check at quarter-end:** VIE's "vs 10y avg" deltas
  growing or shrinking quarter-over-quarter signal regime shifts that
  should also be visible in our cycle-position calculations. Same shift,
  different absolute baseline.
- **Spot-level visibility:** VIE's weekly trackers + Q-Live-Est give
  multi-week context on where spot has been clearing. Useful as a
  qualitative read on whether our point-in-time `spot_tce.yaml` is
  representative of the broader QTD environment.
- **Not used for:** numerical calibration of our 10y means; substitution
  into our cycle-position ratio denominator; any direct level comparison
  that crosses the TC/spot baseline boundary.

---

## Historical Context — original framing (2026-06-03, preserved for the record)

The original diagnostic (written same day as the source was first pulled)
treated the gap as a potential calibration target. The numerical findings
remain valid as data; the interpretation has been superseded by the
methodology-difference framing above. Preserved here so that anyone
reading the artifact later understands the investigation arc.

### Original cross-check table — VIE-implied 10-year means vs ours

Computing back from VIE Q2-26 Live Est and the "Vs. 10y Avg" delta:

```
VIE-implied 10y mean = Q2-26 Live Est ÷ (1 + delta/100)
```

| Class | VIE Q2-26 | VIE Vs 10y Avg | VIE-implied 10y mean | Our 10y mean | Δ (Ours − VIE) |
|---|---:|---:|---:|---:|---:|
| LNG (TFDE) | $48,213 | −13% | **$55,418** | LNGC $85,000 | **+$29,582 / +53%** (we higher) |
| VLCC | $147,358 | +482% | **$25,319** | $40,000 | **+$14,681 / +58%** (we higher) |
| Suezmax | $182,281 | +652% | **$24,239** | $27,747 | **+$3,508 / +14%** (we higher) |
| Aframax | $145,373 | +505% | **$24,028** | $27,600 | **+$3,572 / +15%** (we higher) |
| LR2 (clean) | $91,965 | +351% | **$20,392** | $28,000 | **+$7,608 / +37%** (we higher) |
| MR2 | $44,550 | +228% | **$13,582** | $16,000 | **+$2,418 / +18%** (we higher) |

### Original (superseded) per-class hypotheses

- **LNG (+53%):** Deliberate spike-inclusive choice on our side — see
  LNGC comment in `historical_tce_means.yaml`. **This interpretation
  remains valid** — the LNG gap is independent of the TC-vs-spot framing.
- **VLCC (+58%):** Originally hypothesised as Compass-vs-VIE-base-period
  difference. **Superseded** by the TC-vs-spot interpretation above.
- **Suezmax / Aframax / MR (+14-18%):** Originally hypothesised as
  source-methodology differences within reasonable bounds.
  **Superseded** by the TC-vs-spot interpretation — the smaller gaps
  for these classes are consistent with smaller historical spot-vs-TC
  spreads relative to VLCC's extreme cyclicality.
- **LR2 (+37%):** Originally hypothesised as defensible
  product-vs-crude-cycle distinction. **Likely also explained by
  TC-vs-spot**, but deferred for separate empirical confirmation.

### Original (now obsolete) spot vs QTD-average finding

The original artifact also flagged that VIE Q2-26 Live Est is QTD-average
and ours is point-in-time, with VIE values 21-188% higher. **This
observation remains accurate**, but its policy implication ("switching
sourcing would systematically raise tool FVs across crude") is now
secondary to the TC-vs-spot reframe — both are baseline-convention
choices that need to be evaluated jointly, not in isolation. Deferred.

### Original recommended integration path (superseded sections)

The original recommendations 1-4 (add to data_sources.yaml, §8.3 refresh
step, METHODOLOGY notes, optional automation) **all landed and stay
valid as workflow integration steps**. The recommendation to "investigate
VLCC anchor revisit" as the "highest-leverage open call" is **rescinded**
— that work block (B-1) is closed by the reframe rather than by
recalibration.
