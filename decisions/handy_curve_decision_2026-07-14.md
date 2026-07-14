# §9.9 dry-bulk Handysize curve decision — Stage-3 precondition (PANL D2 / 2343 coverage)

**Date:** 2026-07-14 (agent prep; decision reserved to the owner)
**Trigger:** Stage-3 intake — both governance dry-bulk funnel survivors carry Handysize dwt the
shipped fit family cannot mark: **2343 40.7%** (58 Handysize hulls, 2.2M of 5.4M owned dwt,
AR2025 p.7) and **PANL 23.5%** (14 hulls, 542,264 of 2,307,262 dwt, FY2025 10-K fleet table).
The PANL Gate-D PWE names this decision as the cure ("the shipped producer family lacks a Handy
fit (76.5%) — cure is a producer Handy-curve decision (§9.9)"); the Stage-2 verdicts direct:
*"decide it as part of onboarding, don't inherit it silently."*

**Status: OWNER DECISION PENDING — nothing wired.** No curve values are sourced in this doc
(sourcing is pre-registered onboarding work under the predict-bands-ahead discipline); this doc
inventories the comparable sample, frames the options against the §9.9 scope discipline, and
records a recommendation.

---

## 1. The comparable-sample hunt (performed 2026-07-14)

> **CORRECTION (2026-07-14, same day, post-ruling — the Option-B execution sweep re-read the
> source dailies):** the "one real print" below is MISCLASSIFIED. The 2025-06-13 daily's section
> is **"Tankers:"** — Baltic Sapphire/Baltic Swift are Handysize **PRODUCT tankers** (their
> generic reference was $30M en-bloc ≈ $15M each; the $17.4M generic attaches to 15Y **MRs** in
> the same bullet). The sp_scan Handy keyword matched tanker-section prose. **True dry-bulk
> Handysize print count from the Pareto archive: ZERO** — the sample was even thinner than this
> doc stated, which strengthens the Option-B conclusion and voids the "$17.1M ≈ $17.4M within
> 2%" corroboration claim. **Separately, the execution sweep found the print flow this doc
> thought absent: the MB Dry Bulk weekly reports ~3 dry-Handy S&P prints/week (16 prints across
> issues 24-28 alone, ages 8-23)** — the ruling's "when/if we get more transaction prints"
> branch is likely to arm within a quarter, not years. Sample inventory + re-fit arming
> condition now live in `handy_curve_sourcing_prereg_2026-07-14.md`. The Pareto-archive scan
> methodology below stands; only the classification of its single hit was wrong.

Full `sp_scan --full` rescan of the entire Pareto Shipping Daily archive (2024-09 → 2026-07-03,
the same archive that yielded 19-38 candidates per anchored class). The scanner's `Handy` class
keyword (`handymax|handysize`) has been live since the 2026-06-10 retro-harvest, so the result is
a true scarcity, not a scanner blind spot:

- **Handy candidate sentences: 2** (vs VLCC 34 · Suezmax 38 · MR 36 · Cape 22 · Supra-Ultra 19 ·
  Pana 14). One is generic-quote commentary, not a print. The single real print:
  - **2025-06-13 — 'Baltic Sapphire' + 'Baltic Swift'** (2009-10 built, Korea): **$34.25M
    en-bloc → ~$17.1M each, age ≈ 15-16**, no scrubbers. The same daily's sentence states the
    price "is in line with our **$17.4m generic quotes**" — the print corroborates Pareto's
    generic Handy quote at the old end **within ~2%**.
- The 2026-04-28 daily (commentary row) records Pareto raising small-ship (panamax, supramax,
  **handysize**) generic quotes — resale-to-20Y up ~$2M YTD — i.e. generic quote LEVELS exist
  and move, but Handy PRINTS rarely reach the dailies' S&P prose.

**Additional candidates surfaced by the Stage-2 packets (NOT classified here):**
- **PANL FY2025 10-K Note 9:** Strategic Spirit acquired Jun-2025 **$10.0M**, Strategic Vision
  Sep-2025 **$10.0M** (2012-built Handysize; year-end book $11.4M / $10.6M). **Provenance
  caveat:** Note 9 is the debt note — these read as sale-leaseback/financing-related
  acquisitions, likely option-strike-adjacent rather than clean arm's-length market prints (the
  BW Yushi precedent: option strikes are documentation-only, never fit). Classify from the
  filing text before any use.
- **PANL 10-Q Q1'26:** Bulk Xaymaca MOA 2026-02-27 $9.6M — a 2006 **Panamax** (pana.yaml
  candidate, not Handy).
- **2343 AR2025:** eight older-vessel 2025 disposals "at historically healthy prices" (p.20) —
  per-vessel splits not extracted at desk depth; the AR notes + HKEX announcements are the
  richest untapped Handy-print source (2343 is one of the world's largest Handy owners). The
  HKEX adapter (landed 2026-07-14) makes these pollable going forward.
- **MB Shipbrokers Dry Bulk weekly** (direct subscription since 2026-06-11, S&P section per
  issue) — a standing hunting ground the archive scan does NOT cover; only ~5 issues on disk so
  far.

**Desk verdict on the sample:** effectively **one price point at one age** (an en-bloc pair at
age 15-16). The fit minimum elsewhere in §9.9 is n≥2 in-window (LR2 at n=1 = fallback-to-proxy);
the VLGC fit used n=7 and still flagged its extrapolated node WIDE. **A transaction-anchored
Handy fit is not supportable today.**

## 2. What the class needs regardless of option (engine inventory)

A dry-bulk Handysize class does not exist anywhere in the engine — this is NOT the product-tanker
`Handysize` (37-40k product hulls, ASC): distinct market, distinct curve, distinct rates. Wiring
any option means:
- `vessel_value_curves.yaml`: new dry-bulk class (working name **`handy_bulk`**, baseline 38k
  dwt — PANL fleet avg 38.7k, 2343 37.9k), dwt-scaled per §11.7.10.
- `scenario_inputs.yaml` dry-bulk `class_routes`: + handy_bulk; scenario TCE deck for the class
  (no Handy FFA panel exists in the OCR widget — Cape/Pmax/Smax only; the honest v1 rate surface
  is a BHSI-basis deck derived off the Supra deck with a documented BHSI/BSI basis, or issuer
  cover disclosures; 2343's AR cites BHSI-38k 2025 avg $10,580 net, and the Pacific Basin IR page
  republishes weekly BHSI/BSI — already used by the Stage-2 packets).
- `historical_tce_means.yaml` / `twelve_month_tc.yaml`: dry-Handy entries (current `Handysize`
  rows there are PRODUCT).
- §9.10 weight-family: handy_bulk flows into the dry-bulk sidecar automatically once routed.
- A `transactions/handy_bulk.yaml` is created ONLY under Option A (fit); under Option B the
  class runs un-anchored (LNGC/container semantics) and the Baltic pair print lives in the
  decision record as a validation cross-check, not a fit input.

## 3. Options

**A. Transaction-anchored fit now — NOT SUPPORTABLE.** n≈1 effective print, single age node,
no slope information. Fails the §9.9 comparable-sample bar (the rule exists precisely for this).

**B. Static broker-quote curve, explicitly NOT txn-anchored (LNGC/container precedent) —
RECOMMENDED.** Source curve nodes from broker generic quotes (Pareto dry-bulk generic quote
tables in the dailies; MB Dry Bulk weekly price assessments; the Clarksons benchmarks 2343's own
AR cites), each node cited per the figure-provenance rule; validate the old end against the
Baltic pair print ($17.1M vs $17.4M generic — already within 2%); flag the class
`basis: broker-generic, not transaction-anchored` so k_broker on Handy-heavy names reads on the
un-anchored semantics (the §9.9 two-regime rule already handles mixed books via class-level
basis). Standing re-fit path: the sp_scan Handy keyword + the MB dry weekly + 2343's own
disposal flow accumulate prints; re-visit the fit when ≥2 age-diverse in-window prints exist
(register a trigger at wiring time, owner-ratified).
*Consequence for the funnel read:* rubric-as-written D2 coverage becomes ~100% (both names),
but the TXN-ANCHORED family stays 3 classes — Handy-heavy names carry a documented un-anchored
sleeve, which caps them at **GOVERNED-WIDE·pending-anchor** rather than VALIDATED-TIGHT until a
real fit lands. Honest, and consistent with "PROVISIONAL by definition until reconciled."

**C. Proxy under Supra-Ultra dwt-scaling — REJECTED as primary.** Linear dwt-scaling across the
class boundary (38k on a 62k baseline → 0.61×) is exactly the §11.7.10 failure mode in mirror
(small-bulk $/dwt runs at a premium to linear; the Pana curve's old-Post-Panamax overvaluation
is the cautionary instance). Useful only as a sanity BRACKET on Option B's sourced nodes.

**D. Leave Handysize unmarked — REJECTED.** Unlike LNG (where the whole sector runs on its own
static curve), an unmarked class means 40.7% of 2343's dwt carries NO mark — no NAV can be
computed for the name at all. Not an available outcome if 2343 onboards; choosing D means
descoping 2343 from Stage-3 (a governance-side call, not a producer one).

## 4. Recommendation (agent's read — the decision is the owner's)

**Option B**, wired as its own pre-registered onboarding step BEFORE either name's
reconciliation: source the node set with citations, predict the curve's implied 2343/PANL fleet
marks vs the AR2025 broker-composite ($1,958.3M owned-fleet value — an issuer-published
validation surface the crude sectors never had) AHEAD of computing, then run the standard gate
loop. The 2343 broker-composite cross-check is the strongest argument this static curve can be
honest: it gives the un-anchored class an independent aggregate validator at birth.

**Owner decision:** [ ] Option A · [x] **Option B** · [ ] Option C · [ ] Option D ·
[ ] other/amend: ____
**Rationale (owner, verbatim 2026-07-14):** "go with Option B, only realistic solution until
when/if we get more transaction prints in the future."
**Execution:** sourcing prereg + wiring proceed as the doc's own pre-registered step —
`decisions/handy_curve_sourcing_prereg_2026-07-14.md` (bands ahead of wiring), re-fit trigger
registered at wiring. Class stays un-anchored until the print sample supports a §9.9 fit.

---
*Records touched if B is ratified: vessel_value_curves.yaml + scenario_inputs.yaml +
historical_tce_means.yaml + twelve_month_tc.yaml (+ their lock tests), a
`decisions/handy_curve_sourcing_prereg_<date>.md` with predicted bands, and a re-fit trigger in
reweight_triggers.yaml. None touched today.*
