# Crude scenario reweight proposal — post-stand-down (§13.3 trigger)

**Date:** 2026-07-02 · **v2 (AMENDED same day) — Status: C-1 STOP, awaiting owner sign-off
on the leg recalibration question (§9 below). No inputs changed.**
**Trigger:** external audit F-2 (P0) + METHODOLOGY §13.3 owner-re-evaluation discipline.
The scenario file's own weight comment (Jun-9) says the 0.25/0.45 escalation/pre-MoU split
"hinges on the pending US response — revisit when it resolves." It has resolved.

**Review status (v3):** v1 APPROVED WITH CONDITIONS (2026-07-02 review); v2's C-1 audit
returned outcome (b); the review ADDENDUM answered **C-1 = (A)** (0.15-flare episodic
mixture adopted) and added two blocking items: **C-3** (multi-sleeve aggregation bug —
FIXED, ratified as its own gate layer, hybrids restated in §14) and **C-4** (product +
LNG reweight sections — drafted in §15, **owner sign-off on those weights is the one
open gate before the vintage runs**). §9 = C-1 audit; §10 = C-2 plan; §11 = W-1..W-4;
§12 = prepared YAML annotations; §13 = BRUT registration; §14 = C-3; §15 = C-4.

---

## 1. What changed in the world (dated evidence; web sweep 2026-07-02, citations in the
session research briefs — two of three briefs completed, see Provenance at bottom)

**Corrected timeline — the MoU is SIGNED, and §13.3's literal trigger fired June 17:**

- War began ~**Feb 28, 2026** (Brent pre-war reference $72.48); first ceasefire **Apr 8**
  (Pakistan-mediated), extended Apr 21; 60-day ceasefire conditions Jun 12; the
  **"Islamabad Memorandum" signed Jun 14/17** (Trump/Pezeshkian, witnessed by Pakistan;
  mediators Pakistan/Qatar/Saudi/Turkey/Egypt; full text via NPR Jun 18). Key term for
  shipping: **Hormuz toll-free for 60 days only** (to ~Aug 16) — Iran asserts a right to
  charge fees after; the toll question is UNRESOLVED and on the Doha agenda.
- **Late-June flare-up INSIDE the signed MoU:** Jun 25 container ship *Ever Lovely*
  attacked SE of Oman; Jun 26 CENTCOM strikes on missile/drone infra; Jun 27 tanker
  *Kiku* hit by an Iranian drone + US strikes near the strait; Jun 27–28 Iran struck US
  bases in Kuwait and Bahrain. The market re-priced war: VLCC TD3C re-spiked to
  ~$461k/day Jun 19 and BDTI peaked 2,227 Jun 23.
- **Stand-down Jun 28** — "Both sides will stand down for now and vessels can move
  freely" (US official, The Hill). A mutual freeze restoring MoU compliance, not a new
  agreement. Traffic picked up Jun 29; central-channel **mine status UNCONFIRMED**.
- **Doha technical talks Jun 30–Jul 2** (Witkoff/Kushner ↔ Deputy FM Gharibabadi;
  Qatar/Pakistan mediating; Oman delivered a separate strait proposal): agreed a
  dispute-resolution channel + ~$6B frozen-assets goods arrangement; Qatar: "positive
  progress"; Vance (Jul 1): "going well." Next round after the Khamenei funeral
  processions **Jul 4–9**. Corroborated in-repo: Pareto Shipping Daily **2 JUL 2026**
  (`inputs/research_pareto/2026/07/2026-07-02_…509255.pdf`, p.1): "Brent under further
  pressure (below $71/bbl) amid reports of positive peace talks between US and Iran."
- **The tape has fully round-tripped.** Brent closed $72.68 on **Jun 25** — explicitly
  "lowest since Feb 27, before the war started" (Al Jazeera) — vs the ~$112–120 March
  peak; $72.25 Jul 1. VLCC TD3C: record $423.7k Mar 2 → ~$461k Jun 19 → **$313k Jun 26
  (−33 % w/w, Baltic wk-26)** → ~$287k Jun 30 (Reuters/Maguire); Pareto 2-Jul prints
  TD22 $127.6k (−3.5 % d/d). BDTI 2,227 (Jun 23) → **1,864 (Jul 1)**, seven consecutive
  declines, now *below* late-May levels. June-30 equities: five names fell 15–22 % in one
  session (DHT/FRO/TNK/STNG/ASC — the F-1 band event).
- **Not resolved:** the post-day-60 toll regime; mine clearance; talks paused for the
  funeral; war-risk insurance level UNCONFIRMED (research brief did not complete). And
  the flare-up pattern has now escalated to direct strikes **twice** (March, late June).

## 2. The problem (audit F-2, verified — and worse than the audit knew)

Locked weights are Jun-9 POINT-IN-TIME: **escalation 0.25 / pre_mou_baseline 0.45 /
mou_base 0.18 / mou_bear 0.12** (`inputs/scenario_inputs.yaml:126/181/244/305`). Since
then the MoU signed (Jun 17), was violated (Jun 25–27), and compliance was restored with
talks progressing (Jun 28–Jul 2) — **§13.3's literal trigger ("the MoU signs") fired
June 17 and no re-evaluation was recorded.** The market now trades ~the MoU base case
while 70 % of the model's probability mass sits on war-continues paths. The errors
compound: prices moved to the MoU state (F-1 fixed, July-1 vintage recovered) while FVs
remain weighted pre-MoU — crude EV% systematically overstated, correlated across names.

## 3. Proposed weights

| Scenario | Locked (Jun-9) | **Proposed (Jul-2)** | Rationale |
|---|--:|--:|---|
| escalation | 0.25 | **0.10** | Tail is REAL, not residual: flare-ups reached direct US–Iran strikes twice (March; Jun 25–28, *inside* the signed MoU). Near-term re-ignition risks: the funeral pause, the day-60 toll cliff. So 0.10 (v1 level), not Set-D's 0.05. |
| pre_mou_baseline | 0.45 | **0.20** | Semantic shift, document in the YAML comment: with the MoU signed this leg now means **"MoU-ineffective"** — the framework exists on paper but Hormuz economics stay war-like (unilateral tolls after day 60, mines uncleared, recurring flare-ups). Jun 25–28 proved this path live. |
| mou_base | 0.18 | **0.45** | The market's central case: signed framework + stand-down + progressing Doha technical talks → three-phase normalization. |
| mou_bear | 0.12 | **0.25** | Framework holds but normalization disappoints — tolls imposed post-day-60, phased/partial reopening (v1 level). |

Anchor: the **v1 (pre-Jun-9) prior restored, adjusted for what June taught us** — the
escalation tail held at 0.10 (two observed escalation episodes), the MoU-ineffective leg
at 0.20 > v1's 0.15 (the toll cliff and mine question are real, dated, unresolved). It is
deliberately NOT a bespoke set: it reuses the family the robustness diagnostic brackets.
Keep the existing scenario KEYS (renaming `pre_mou_baseline` would churn the YAML and
history for no analytic gain); record the semantic shift in the weight comments.

## 4. What the proposal does to the crude book

Production path (txn-anchored marks, July-1 recovered prices), full run in
`outputs/weight_robustness_diagnostic.md` (Set E = this proposal):

| Ticker | Price | EV% locked | EV% proposed | Position locked → proposed |
|---|--:|--:|--:|---|
| DHT | $16.53 | −4.6 % | **−24.8 %** | HOLD → TRIM/SHORT* |
| ECO | $49.94 | −19.9 % | **−41.4 %** | TRIM/SHORT* → TRIM/SHORT* |
| FRO | $34.70 | −16.9 % | **−40.1 %** | TRIM/SHORT* → TRIM/SHORT* |
| INSW | $77.78 | −21.1 % | **−36.2 %** | TRIM/SHORT* → TRIM/SHORT* |
| TNK | $64.33 | +23.7 % | **+9.5 %** | BUY → BUY |
| NAT | $5.56 | −40.1 % | **−54.6 %** | TRIM/SHORT* → TRIM/SHORT* |
| TEN | $35.37 | +85.2 % | **+49.7 %** | BUY → BUY (§15 haircut applies downstream) |
| CMBT | $14.05 | +14.4 % | **−8.8 %** | BUY → TRIM/SHORT* |
| BRUT | $5.17 | +98.1 % | **−5.0 %** | BUY → HOLD — **the headline casualty**: the newbuild-torque vehicle's FV halves ($10.24→$4.91) without war rates |
| CAPT | $12.49 | +37.4 % | **−5.1 %** | BUY → TRIM/SHORT* |

\* Crude "rich/TRIM" reads remain **cycle position, not shorts** (§12 relabel registry
unchanged — DHT/ECO/FRO/INSW/NAT relabel; the registries are weight-independent).

**Read on the change:** the reweight removes ~all of the war-premium EV from the crude
book. TNK and TEN survive as BUYs on their own economics; the newbuild-heavy torque names
(BRUT, CAPT) and CMBT lose their margin entirely — which is exactly what a stand-down
*should* do to names whose upside was concentrated in the escalation/pre-MoU legs.
Drift-gate note: applying this produces large UNEXPLAINED EV rows + band flips on most of
the crude book by design; the annotation for every one is this document.

## 5. Weight-robustness (the §9.10 diagnostic, re-run 2026-07-02)

Fixed two bugs in `scripts/crude_weight_robustness.py` before trusting it (details §7):
ECO/FRO/INSW/NAT are **weight-robust TRIM** across all five sets; **DHT** flips
HOLD→TRIM everywhere except the (now-stale) war-weighted Set A; **TNK is the only
weight-driven BUY** (BUY under A/B/C, HOLD under bearish D, BUY under proposed E).
No crude long except TNK/TEN survives ANY defensible post-stand-down set.

## 6. §13.3 re-weight triggers going forward (audit recommendation — make it event-driven)

The existing §13.3 trigger ("the MoU signs") FIRED Jun 17 and was missed — dated
observables, so the next one can't be:

1. **Day-60 toll decision, ~Aug 16** (Jun 17 + 60d): Iran imposes fees → shift mass
   mou_base→mou_bear/pre_mou; toll-free extended/waived → pre_mou toward 0.
2. **Talks resumption after the Jul 4–9 funeral**: collapse or strikes resume → restore a
   Jun-9-shape risk-on set the same day.
3. **Mine-clearance confirmation / transit normalization** (UKMTO/JMIC advisories,
   war-risk premia — premia level currently UNCONFIRMED, add to the Saturday news-pull).
4. **Brent reopens > pre-war ($72.48) +$10/bbl sustained** — macro confirmation of 2.
5. **Quarterly staleness floor:** any weight set older than one quarter forces a §13.3
   review (this set went stale in 23 days; the floor is a backstop, not the standard).

## 7. Related fixes made while preparing this (committed separately)

- `scripts/crude_weight_robustness.py` ran on **un-anchored marks** (missing
  `_maybe_apply_transactions`, ~12 % high on every name since txn-anchoring went
  default-ON 2026-06-09) and on **static watchlist prices** (Set A column silently
  disagreed with the pipeline headline). Its "Set A (current locked)" was ALSO still the
  pre-Jun-9 v1 weights. All three fixed; header/cells now derive from the set dict; the
  hand-curated "Key findings" block (stale, F-8 pattern) now derives from the run.
- **F-5 rate refresh is ready to execute from the same source**: Pareto 2-Jul prints VLCC
  TD22 $127.6k / LR2 $89.0k / MR-East $35.6k vs `spot_tce.yaml`'s unrefreshed Jun-7 war
  values (VLCC $388.3k). Recommend refreshing `spot_tce` / `ffa_forward_curve` /
  `twelve_month_tc` from the 2-Jul daily **in the same commit as the reweight** so the
  scenario re-run lands on one coherent post-stand-down vintage (one drift-gate event,
  one cause).

## 8. Decision requested (v3 — crude fully approved; the open gate is C-4)

- [x] Crude weights 0.10/0.20/0.45/0.25 — approved (review 2026-07-02)
- [x] C-1 leg recalibration — **(A) adopted** (review addendum): 0.15-flare mixture
- [x] F-5 pairing + C-2 decomposition — approved; scope extended to product/LNG spot
- [x] C-3 aggregation fix — landed, ratified as its own gate layer, hybrids restated (§14)
- [ ] **OPEN — C-4 product + LNG weights (§15 menus): product (A) v2 restore
      0.15/0.25/0.45/0.15 (recommended); LNG (A) v3 restore 0.15/0.25/0.45/0.15
      (recommended).** On sign-off the ONE VINTAGE executes: scenario_inputs edits across
      crude/product/LNG (weights + §12 annotations + `semantics_changed` + recalibrated
      leg), §11.3/§11.5 lock-revision notes + lock-test re-pins, F-5 refresh (all
      sectors), pipeline re-run, C-2 table 4, per-name annotations (STNG/FLNG/TRMD flips
      per §15), `ratify_baseline.sh`, single commit, W-5 into brut_log.

---

## 9. C-1 parameter audit — the MoU-ineffective leg (BLOCKING; reviewer condition)

**Question:** does the pre_mou leg, calibrated for "war continues at current intensity,"
re-import war premium at 0.20 weight under its new "MoU-ineffective" meaning?

**Leg calibration (base point, front-12M value-weighted / ×10-yr mean):**

| Class | escalation | pre_mou | mou_base | mou_bear |
|---|--:|--:|--:|--:|
| VLCC | $337.5k (8.4×) | **$189.5k (4.7×)** | $84.9k (2.1×) | $65.3k (1.6×) |
| Suezmax | $148.8k (5.4×) | **$100.8k (3.6×)** | $47.9k (1.7×) | $41.0k (1.5×) |
| Aframax | $102.8k (2.8×) | **$69.5k (1.9×)** | $38.5k (1.1×) | $33.3k (0.9×) |
| LR2 | $191.3k (7.1×) | **$108.8k (4.0×)** | $48.3k (1.8×) | $32.8k (1.2×) |

**Finding: outcome (b).** The leg is 38–44 % below escalation (differentiated), but its
levels — VLCC 4.7× the 10-yr mean sustained for 12 months — are achievable only under
persistent physical disruption, which is precisely its OLD description ("Hormuz disruption
persists"). Under the new semantic (strait open, tolls after day 60, sporadic
fast-reverting flare-ups — the June episode spiked ~60 % and collapsed within ~10 days),
that time-average is not credible. Vessel multipliers derive from the same curves via the
elasticity, so they inherit the same bias; no separate multiplier issue found (no crude
leg carries a `vessel_scale_multiplier` override).

**Recalibration sketch (quantification only — NOT applied):** episodic-regime mixture,
`0.15 × escalation + 0.85 × mou_bear` per quarter/class/point — 15 % expected
time-in-flare-up (June datapoint: days-to-a-week per episode, two episodes in four
months), 85 % at the framework-holds-but-disappoints level (mou_bear: immediate P2, no P1
spike — the closest existing calibration to a tolled, mostly-open strait). Result: VLCC
front-12M **$106.1k (2.7× mean)** vs the current $189.5k.

**FV impact (both runs at the approved 0.10/0.20/0.45/0.25 weights, July-1 prices,
txn-anchored):**

| Ticker | EV% current leg | EV% recalibrated leg | ΔFV |
|---|--:|--:|--:|
| DHT | −24.8 % | −31.3 % | −8.7 % |
| ECO | −41.4 % | −48.5 % | −12.0 % |
| FRO | −40.1 % | −47.6 % | −12.6 % |
| INSW | −36.2 % | −39.6 % | −5.4 % |
| TNK | +9.5 % | **+5.1 %** | −4.0 % |
| NAT | −54.6 % | −59.5 % | −10.8 % |
| TEN | +49.7 % | +41.2 % | −5.7 % |
| CMBT | −8.8 % | −12.1 % | −3.6 % |
| BRUT | −5.0 % | **−39.7 %** | **−36.5 %** |
| CAPT | −5.1 % | −19.4 % | −15.1 % |

Material well beyond the weight decision: BRUT loses another third (FV $4.91 → $3.12);
TNK's BUY margin compresses to borderline (+5.1 %, the BUY band edge).

**Decision menu (owner):**

- **(A) RECOMMENDED — adopt the episodic-mixture recalibration** with flare-share 0.15 as
  the single documented tunable (a dated POINT-IN-TIME parameter with the June episode as
  its evidence). Cleanest semantics: every leg then describes a post-signature world.
- **(B) Keep the leg as-is** and accept that 0.20 weight carries some residual war-level
  premium — defensible only if the leg is re-read as "MoU collapses back to sustained
  disruption," which semantically overlaps escalation and double-counts that tail.
- **(C) Different flare-share** (0.10 → VLCC ~$92k; 0.25 → ~$133k) or hand-set curves —
  owner supplies the number, same mixture machinery.

## 10. C-2 decomposition (reviewer condition — attribution appendix)

Layer order (stated per rider 2): **aggregator fix → crude weights + leg → product
weights → LNG weights → rates.** For pure-plays the sector layers are trivial; for the
hybrids the per-sector cumulative attribution (rider 2, computed 2026-07-02 at July-1
prices, fixed aggregators):

| Ticker | C-3 base | + crude + leg | + product | + LNG |
|---|--:|--:|--:|--:|
| INSW | $60.19 (−22.6 %) | $49.28 (−36.6 %) | $48.00 (−38.3 %) | $48.00 (no LNG sleeve) |
| TEN | $64.35 (+81.9 %) | $52.16 (+47.5 %) | $51.18 (+44.7 %) | $50.92 (+44.0 %) |
| CMBT | $15.56 (+10.7 %) | $13.73 (−2.3 %) | — (no product sleeve) | — (no LNG sleeve) |

(The aggregator-fix layer sits ABOVE these as its own ratified line: committed → C-3
base is §14's first two columns.) The final **rates layer** lands at execution with the
F-5 refresh:

4. **New weights + new rates — EXECUTED 2026-07-02 (vintage run).** Rate-effects
   (scenario PW FV, new-rates run minus old-rates eval): **every tanker name exactly
   $0.00** — the held tanker forwards make the understatement caveat literal — and the
   dry-bulk names small and mixed from the 2-Jul FFA promotion (SB **+$0.14**,
   SBLK −$0.18, GNK −$0.49, CMDB −$0.09, CMBT dry-sleeve **−$0.39**). Completed
   decompositions: **BRUT $10.24 → $3.12** = fix $0.00 / crude weights −$5.33 / leg
   −$1.79 / product+LNG $0.00 / rates $0.00. **CMBT $16.07 → $13.34** = fix −$0.51 /
   crude+leg −$1.83 / rates −$0.39 — and the rates nudge is what carried CMBT across
   the −5 % TRIM line (−2.3 % → −5.05 %): a **boundary-cross, not signal** (annotated
   in cmbt_log; the W-frag ⚠ already flags the name as weight/boundary-sensitive).
   **CAVEAT (reviewer condition): the TANKER rate-effect is UNDERSTATED pending a
   market forward print** — tanker ffa_forward_curve / 12M-TC lines held at the
   2026-06-07 vintage (owner decision, option (i)); standing trigger
   `tanker_forward_print_lands` re-runs this layer when a print lands; the scorecard's
   Rate-basis header discloses the hold.

## 11. Completed work items (review conditions W-1..W-4 + sequencing)

- **Sequencing (F-3/F-8):** both were already fixed and committed BEFORE this proposal —
  F-3 in `9526968` (exact-zero sentinel at the solver — stricter than the review's
  $1,000/day floor suggestion, it detects the unbracketed solve exactly; regression test
  asserts no rendered ratio > 100×; plus a committed-outputs guard in
  `tests/test_outputs_hygiene.py`), F-8 in `428bf29` (verdict prose fully derived from
  rows; a forced non-registry short must be NAMED by the prose — test-locked). The
  regenerated vintage cannot re-print either defect.
- **W-1 (fragility flag): DONE.** The §9.10 diagnostic now covers all 10 crude-exposed
  names and writes a machine-readable sidecar (`outputs/weight_robustness.yaml`,
  EV-sign-stability per the review's definition); the scorecard verdict carries a
  **W-frag** column and the JSON handoff a `weight_sign_stable` field. Under the CURRENT
  locked weights it flags **BRUT / CAPT / CMBT (⚠ sign flips)** and clears
  DHT/ECO/FRO/INSW/NAT/TNK/TEN — i.e., it would have flagged all three names before any
  reweight, which was the point.
- **W-2 (look-back on the broken diagnostic): affected-decisions list is EMPTY.** The
  only decision citing §9.10 output is FRO's exit rationale (decisions/fro_log.md:1246),
  dated Jun 2–4 — BEFORE txn-anchoring went default-ON (Jun 9) broke the script. No
  decision in the Jun 9 – Jul 2 window cites `weight_robustness` or its outputs (grep of
  decisions/, PLAN, CHANGELOG). Additionally, the FIXED rerun reproduces both pre-window
  verdicts (FRO weight-robust TRIM; TNK weight-driven), so no cited conclusion inverts.
  The LNG comparison script shares the missing-anchoring pattern but LNGC/MGC have no
  transaction fits (anchoring is a no-op) — LNG diagnostics unaffected.
- **W-3 (dry-bulk war-vintage sweep): checked, clean.** Cape $38k / Pana $20.5k /
  Supra-Ultra $19.5k spot and the 12M TC entries are Jun-9 vintage but NOT war-premium
  levels — dry bulk never carried the war trade (BDI FELL through June, 2,916 → 2,562;
  Cape input ≈ the Baltic ~34–36k seasonal level), and the Jul-2 Pareto has dry bulk
  FIRMING ("FFA curve markedly higher"). No bunker/fuel assumptions live in
  cost_structures (TCE is net of voyage costs). Refresh the dry-bulk lines opportunistically
  in the F-5 pass; no contamination flag. SB/SBLK value curves are transaction-anchored
  off bulker prints, which did not reprice on the war.
- **W-4 (F-1 fix mechanism): STRUCTURAL, not manual.** Commit `8f29467`: true prior-day
  close from the daily bars (the band was silently a ~5-session window), the ≥3-name
  market-event circuit breaker (prices APPLIED + review marker, loader passes them
  through), fallback reasons recorded on the entry, and the scorecard price-basis header
  (`428bf29`). All test-locked (`tests/test_price_refresh.py`,
  `test_price_basis_header_announces_static_fallbacks`). The July-1 log reconstruction
  was only the recovery of the one discarded vintage; the next sector-wide day is handled
  in code.
- **Triggers → YAML: DONE.** `inputs/reweight_triggers.yaml` (six triggers incl. the
  reviewer's ~Jul-17 MoU 30-day implementation checkpoint and the ~Aug-16 toll cliff as a
  pre-registered reweight date), surfaced by the refresh preflight
  (`refresh.check_reweight_triggers`, red on due/overdue/FIRED — test-locked);
  METHODOLOGY §13.3 now points at the file and says prose triggers are unwatched;
  war-risk insurance premia added as a STANDING Saturday news-pull item.

## 12. Prepared YAML annotations (reviewer's three requirements — land with the run)

To be written into `inputs/scenario_inputs.yaml` on approval, verbatim modulo formatting:

- **escalation:** "Weight 0.10 (Jul-2-2026 POINT-IN-TIME; was 0.25 Jun-9). Why 0.10 and
  not 0.15 despite two direct-strike episodes inside the signed MoU: both episodes
  MEAN-REVERTED WITHIN DAYS (TD3C ~$461k Jun-19 → ~$287k Jun-30); scenario weights price
  persistent states over the valuation horizon, not event frequency — fast-reverting
  flare-ups inside a holding framework are evidence for the MoU-ineffective leg (raised
  to 0.20 over v1's 0.15 for exactly that reason), not for sustained war economics."
- **pre_mou_baseline:** "Weight 0.20 (Jul-2-2026 POINT-IN-TIME; was 0.45 Jun-9).
  SEMANTIC SHIFT: with the Islamabad Memorandum signed Jun-17 this leg now means
  MOU-INEFFECTIVE — framework on paper, war-like strait economics in practice (tolls
  after day 60, mines, recurring fast-reverting flare-ups)." Plus the machine-readable
  field on the scenario entry: `semantics_changed: 2026-07-02` (backtests must detect
  the break without reading comments).
- **mou_base:** "Weight 0.45 (Jul-2-2026 POINT-IN-TIME; was 0.18 Jun-9). CONDITIONAL:
  assumes the day-60 toll cliff (~Aug-16) resolves benignly; Aug-16 is a PRE-REGISTERED
  re-weight date regardless of outcome (inputs/reweight_triggers.yaml
  crude_day60_toll_cliff). Not unconditional confidence with a known binary inside the
  horizon."
- **mou_bear:** "Weight 0.25 (Jul-2-2026 POINT-IN-TIME; was 0.12 Jun-9). Framework holds
  but normalization disappoints — tolls imposed post-day-60, phased/partial reopening."

**Product family (C-4 (A) + rider 1 — the annotation carries v2's own provenance):**

- **All four product weights:** "Restored to the v2 lock (0.15/0.25/0.45/0.15,
  Jul-2-2026 POINT-IN-TIME; was 0.25/0.30/0.30/0.15 Jun-9). THE RESTORE REMOVES THE
  JUN-9 HORMUZ-TRANSIT LAYER ONLY: v2 itself (locked 2026-06-03) was calibrated DURING
  the crisis on observed-tightness evidence (Iran-crisis rate spike, >2× historic clean
  earnings, stockpile-replenishment phase), so crisis-era empirical tightness remains in
  the curves — some genuinely persistent (the inventory drawdown was real; replenishment
  is a live cargo-mile driver), some may fade with normalization. Residual triggers:
  `crude_day60_toll_cliff` (scope widened to product — MEG product flows equally
  toll-exposed) and `product_glut_arrival_timing` (the family's central live
  uncertainty: 2026 tight vs 2027 glut arrival), both in reweight_triggers.yaml."

**LNG family (C-4 (A) — no rider):**

- **All four LNG weights:** "Restored to the v3 Set B-revised lock (0.15/0.25/0.45/0.15,
  Jul-2-2026 POINT-IN-TIME; was 0.25/0.25/0.38/0.12 Jun-9). v3 already prices the Ras
  Laffan supply damage (§14 — Trains 4&6 offline, NOT resolved by the stand-down); the
  Jun-9 tilt added only a Hormuz-TRANSIT layer ('Qatar LNG transits Hormuz'), and only
  the transit layer resolved. §11.3 revision note + lock-test re-pins land with this."

## 13. W-5 — BRUT registration text (pre-drafted; lands in brut_log with the run)

> The reweight demonstrates a MODEL-INTERNAL fact: BRUT's modeled margin was concentrated
> in scenarios a model update removed (EV +98 % → −5 % on weights alone; → −40 % with the
> recalibrated leg). It is NOT out-of-sample proof the tier system beat the market: on
> Jun-30 BRUT fell ~7.5 % while the crude five fell 15–22 % — the market was never
> carrying the war premium the model was. The 0.61× P/NAV was the market correctly
> pricing scenario-dependence and going-concern risk, and the reweight moved the model
> TOWARD a price the tape had already set. What worked was the GOVERNANCE LAYER:
> PROVISIONAL ⛔ (cash-pending) + POSITION_UNRELIABLE prevented the model from fighting a
> correct tape. Same lesson as the null-IC finding, in miniature: a deep discount to
> model NAV is not, by itself, opportunity.

## 14. C-3 — multi-sleeve aggregation fix + hybrid restatement (review addendum, blocking)

**The bug (verified, worse than a one-name issue):** all three hybrid aggregators
(`_aggregate_hybrid_report` / `_aggregate_three_sleeve_report` /
`_aggregate_multi_sleeve_report`) paired sleeve scenario ladders by index and applied the
FIRST sleeve's (crude's) probability weights to every sleeve. The 2-sleeve aggregator's
own comment recorded the load-bearing assumption — "currently-identical weights at each
index" — which the Jun-9 crude reweight silently broke. Since Jun-9, INSW's product
sleeve, TEN's product+LNG sleeves, and CMBT's dry-bulk sleeve (72.7 % of vessel value)
were all probability-weighted by the Hormuz state.

**The fix (landed 2026-07-02):** one aggregation core; headline PW FV = Σ of each
sleeve's OWN probability-weighted FV ("cross-sector independence assumed; rank-1 pairing
removed"); display rows stay index-paired as an illustrative slice; upside/downside are
independence envelopes. Regression-tested: a two-sleeve name with a worthless crude
sleeve is INVARIANT under a crude-only reweight (the old form moved it), and the old
INSW identity test was rewritten to assert the per-sleeve identity *plus* that a
product-weight change now moves the whole-co FV (its old invariance WAS the bug).
Gate event ratified as its own layer for C-2 attribution: **CMBT −3.6pp / TEN −3.2pp /
INSW −1.5pp EV, ΔNAV 0.0 % all names, no band flips** (annotated in cmbt/ten logs).

**Restated hybrid stacks (each layer separately attributable):**

| Ticker | committed (pre-fix) | + C-3 fix | + crude reweight | + leg (A) | full vintage (§15) |
|---|--:|--:|--:|--:|--:|
| CMBT | +14.4 % BUY | +10.7 % BUY | +0.9 % HOLD | −2.3 % HOLD | −2.3 % HOLD |
| TEN | +85.2 % BUY | +81.9 % BUY | +56.0 % BUY | +47.5 % BUY | +44.0 % BUY |
| INSW | −21.1 % TRIM* | −22.6 % TRIM* | −33.2 % TRIM* | −36.6 % TRIM* | −38.3 % TRIM* |

**Owner-estimate reconciliation (required by the addendum):** the owner's CMBT
Δ-estimate is CONFIRMED — the crude-reweight impact is **−$1.38/sh** vs the estimated
−$1.2–1.5/sh. The EV landing (+0.9 % vs the estimated +4–7 %) differs because the
estimate started from the PRE-FIX baseline: the C-3 fix itself first takes CMBT
+14.4 % → +10.7 % (the dry-bulk sleeve de-inflates at locked weights too), and the
reweight then lands +0.9 %. Two stacked effects; the per-effect magnitudes match.

**Narrative correction (executed throughout this doc):** the reweight clears **two**
war-premium false-BUYs — **BRUT and CAPT**, genuinely crude. **CMBT comes off that
list**: its downgrade was majority aggregation artifact; the residual is a marginal
HOLD-band straddle. Its W-frag flag remains **⚠ sign flips** after re-derivation but the
range is now shallow (+10.7 % to −2.7 % across the family, vs +14.4 % to −17.3 %
pre-fix); TEN and INSW are now weight-ROBUST.

## 15. C-4 — product + LNG reweight (review addendum; owner sign-off = the open gate)

The Jun-9 reweight war-tilted three sectors; the strait has reopened; one coherent
vintage reweights all three (deferral would need a dated trigger + cause — not proposed).

**Product** (all four names quantified at July-1 prices, txn-anchored, fixed aggregators):

| Weights | refinery_squeeze | moderate_correction | glut_base | demand_softening |
|---|--:|--:|--:|--:|
| current Jun-9 | 0.25 | 0.30 | 0.30 | 0.15 |
| **(A) v2 restore (recommended)** | **0.15** | **0.25** | **0.45** | **0.15** |
| (B) bear bracket (shown for robustness) | 0.10 | 0.20 | 0.50 | 0.20 |

The Jun-9 comments' own logic reverses: refinery_squeeze was raised on "MEG product flows
directly affected by Hormuz contestation" (resolved); glut_base was trimmed because "glut
still arrives once SoH reopens" (it has reopened). Straight v2 restoration; the toll
cliff caveat rides the same `crude_day60_toll_cliff` trigger (product flows are equally
exposed — noted in the trigger's observable at execution).

| Ticker | current | (A) v2 restore | (B) bear | Read |
|---|--:|--:|--:|---|
| **STNG** | +10.9 % BUY | **+2.0 % HOLD ⟵ FLIP** | −4.1 % HOLD | **Surfaced prominently: this retracts this morning's price-driven HOLD→BUY flip** — that flip was real at the tape but weight-dependent; PROVISIONAL·off-curve ⛔ regardless. |
| ASC | +18.1 % BUY | +14.2 % BUY | +11.2 % BUY | **Survives** — ASC's BUY is weight-robust across the family. |
| HAFN | −5.1 % TRIM | −14.5 % TRIM | −20.9 % TRIM | Deepens (cycle-relabeled, not a short). |
| **TRMD** | +21.5 % BUY | **+9.1 % BUY** | +0.8 % HOLD | **The one-day-old reconciliation BUY SURVIVES the restore** (margin compresses 22→9 %); only the bear bracket takes it to HOLD. |

**LNG:**

| Weights | tight_resurgence | moderate_tightening | glut_base | glut_intensifies |
|---|--:|--:|--:|--:|
| current Jun-9 | 0.25 | 0.25 | 0.38 | 0.12 |
| **(A) v3 restore (recommended)** | **0.15** | **0.25** | **0.45** | **0.15** |
| (B) bear bracket | 0.10 | 0.20 | 0.50 | 0.20 |

Cleaner logic than product: **v3 Set B-revised already embeds the Ras Laffan supply
tightness (§14 — NOT resolved by the stand-down; Trains 4&6 still offline)**; Jun-9
added only a Hormuz-TRANSIT layer on top ("Qatar LNG transits Hormuz"), and only that
layer is resolved. Restore v3 exactly.

| Ticker | current | (A) v3 restore | (B) bear | Read |
|---|--:|--:|--:|---|
| **FLNG** | +7.2 % BUY | **+2.0 % HOLD ⟵ FLIP** | −2.6 % HOLD | The marginal BUY the review flagged — retracts to HOLD. (History: FLNG was TRIM under v3, lifted to HOLD/BUY by the Jun-9 tilt; the restore lands it HOLD, consistent.) |
| CCEC | +65.6 % BUY | +54.5 % BUY | +44.4 % BUY | Survives everywhere — but remains the §9.10/§13 weight-driven torque BUY; the W-frag/tier flags carry that trust qualifier to the governance seam. |

**Lock discipline:** LNG Set B-revised and Product Set B v2 are LOCKED families —
executing this requires a §11.3 / §11.5 revision note and **re-pinning the lock tests**,
which anticipate exactly this: `test_flng_v3_set_b_revised_fv_band` /
`test_flng_v3_locked_weights_position` / `test_ccec_position_under_locked_weights` carry
"re-pin on weight settle (post-Hormuz resolution)" instructions in their own comments.
(`scripts/product_weight_comparison.py` also received the same txn-anchoring fix as the
crude diagnostic; the LNG script is unaffected — LNGC/MGC carry no transaction fits.)

**Full-vintage table (crude E + leg A + product v2 + LNG v3), all 16 scenario-run names,
six flips:**

| Ticker | current (all locked) | full vintage | |
|---|--:|--:|---|
| DHT | −4.6 % HOLD | −31.3 % TRIM* | ⟵ flip (cycle-relabeled) |
| ECO | −19.9 % TRIM* | −48.5 % TRIM* | |
| FRO | −16.9 % TRIM* | −47.6 % TRIM* | |
| TNK | +23.7 % BUY | +5.1 % BUY | barely holds the band edge |
| NAT | −40.1 % TRIM* | −59.5 % TRIM* | |
| STNG | +10.9 % BUY | +2.0 % HOLD | ⟵ flip |
| ASC | +18.1 % BUY | +14.2 % BUY | |
| HAFN | −5.1 % TRIM* | −14.5 % TRIM* | |
| TRMD | +21.5 % BUY | +9.1 % BUY | survives |
| FLNG | +7.2 % BUY | +2.0 % HOLD | ⟵ flip |
| CCEC | +65.6 % BUY | +54.5 % BUY | |
| INSW | −22.6 % TRIM* | −38.3 % TRIM* | |
| TEN | +81.9 % BUY | +44.0 % BUY | §15 haircut downstream |
| CMBT | +10.7 % BUY | −2.3 % HOLD | ⟵ flip (§14 stack) |
| BRUT | +98.1 % BUY | −39.7 % TRIM | ⟵ flip — war-premium false-BUY cleared |
| CAPT | +37.4 % BUY | −19.4 % TRIM | ⟵ flip — war-premium false-BUY cleared |

\* cycle-position / unreliable-read relabels apply as registered (weight-independent).

**Post-vintage actionable-long surface:** SB, SBLK (dry bulk, untouched) + ASC (+14.2 %,
weight-robust) + TRMD (+9.1 %) + TNK (+5.1 %, band edge) + TEN (+44 %, APPROX/governed)
+ CCEC (+54.5 %, weight-driven — W-frag/tier carry the trust qualifier). The book's long
surface rotates from crude-war names to product/dry-bulk value — which is what a
stand-down SHOULD do. (Sizing is the governance repo's field; this surface states worth
and trust only — reviewer correction 2026-07-02.)

**F-5 scope extension (per the addendum):** the same rate refresh covers LR2/MR product
spot and LNG spot inputs — all carry the 2026-06-07 war vintage.

---

**Provenance.** World-state: 3-agent web sweep 2026-07-02 (Topic 1 stand-down/diplomacy and
Topic 2 oil/rates briefs completed with per-claim citations — Wikipedia "Islamabad
Memorandum"/"2026 Strait of Hormuz crisis" fetched 2026-07-02, Al Jazeera 2026-06-25/07-02,
Baltic wk-26 via thedcn.com.au, Reuters/Maguire via MarineLink 2026-06-30, Capital.com
2026-06-30, StockQ BDTI table; Topic 3 Hormuz-insurance brief DID NOT COMPLETE, sources
403-blocked — war-risk premia UNCONFIRMED). In-repo corroboration: Pareto Shipping Daily
2026-07-01/02 PDFs, `baltic_indexes_daily.csv`, the June-30 `prices_daily.yaml` band event.
Numbers in §4/§5: production scenario engine, txn-anchored, July-1 recovered prices.
