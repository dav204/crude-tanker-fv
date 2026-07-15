# Tanker forward-print ruling — `tanker_forward_print_lands` (DHT 6-K Jul-13)

Date: 2026-07-14 · Status: DRAFT — FOR OWNER SIGNATURE (curve promotion is human-only; nothing in this note changes an input until the §8 DECISION block is signed). Trigger: `tanker_forward_print_lands` (registered 2026-07-02, `inputs/reweight_triggers.yaml`), treated as FIRED 2026-07-14 on the DHT 6-K business update (filed Jul-13, sentinel-flagged Jul-14). Staging memo: `tanker_forward_print_2026-07-14.md` (options (i)/(ii) staged there; this note is self-contained). Companion method doc: `PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR.md` (Rider 3 — freeze before Jul-28).

## 1. What fired — letter vs spirit (and why it matters for the action)

The registered observable is "any tanker FFA or 1-year T/C forward print landing in the dailies/weeklies." What landed is a 3-year TC from an issuer 6-K (DHT Jaguar, $75,000/day, Sep-2026 start) plus Q3 QTD spot bookings ($139,700/day). Ruling on the semantics:

* Spirit: FIRED. The trigger's purpose clause is "the hold must not go stale silently." A term-market forward print now exists; the header's "no market forward print exists" is false as of Jul-13 and must change today (§6, Rider 1) regardless of the promotion timing.
* Letter: the registered action is not mechanically executable from this observable. The action reads "refresh the ffa_forward_curve + twelve_month_tc lines from the print" — but a 12M TC line cannot be set from a single 3-year fixture without a tenor-structure assumption, and the held complex spans VLCC/Suezmax/Aframax/LR2 + clean lines while the print speaks only to VLCC. Executing the registered action off this print would manufacture an anchor — the exact failure the Jul-02 option (i) rationale refused ("a re-anchor off a single spot print the week spot fell 33% would manufacture an anchor"). Deferral to a multi-name basis is therefore an application of the registered decision's logic, not an override of it.
* The original observable (FFA or 12M TC in the dailies/weeklies) stays armed through the deferral (§5, Rider 4): such a print IS mechanically executable and supersedes this ruling's timeline immediately.

## 2. The print, quantified against the held vintage

Held VLCC curve (2026-06-07 war vintage): front quarter $147.5k; Q5–Q8 average $125.0k; 12M average $155k.

* Front: corroborated. Q3 QTD bookings $139.7k vs held front $147.5k — within ~5%.
* Back: repriced hard. A $75k flat 3-year TC from Sep-2026, decomposed strip-consistently (year-1 average ~$105k decaying off the $139.7k front), forces years 2–3 to ~$60k — i.e. the term market prices the held Q5–Q8 window 40–55% below vintage depending on decomposition convention (staging memo's ~46% is mid-range).
* Shape: the favorable one. The error concentrates in the most-discounted, most-coverage-dampened strip quarters — exactly the shape the Jul-02 option (ii) anticipated.

## 3. Waiting cost: bounded AND direction-safe (the load-bearing finding)

Promotion can only move tanker-family FVs down. Ceiling worked on the most peak-weighted name (DHT, committed 2026-Q1 report: spot exposure 0.55, w_earn 0.30, r 11%): a full promote-now reshape (front held, back marked to the term-consistent path) moves FV ≈ −3.4% ($14.95 → ~$14.4; Model FV −23% → ~−26%).

Walking the live scorecard (2026-07-14 vintage):

* Deep-rich names get richer, no verdict moves: DHT −23%, ECO −41%, FRO −38%, INSW −39%, NAT −55%, HAFN −23%.
* Near-edge HOLDs can only drift toward TRIM — the cheap error direction: TNK +3%, ASC +3%, TRMD −1%, CAPT −1%.
* The only crude BUY, TEN +45%, absorbs a 3–4% overhang without approaching a flip.

The costly error class — a false BUY held on an inflated FV — is not live anywhere in the book. The full cost of deferral is therefore scorecard honesty, which Rider 1 converts from silent to disclosed-and-quantified.

## 4. Calendar correction to the staging premise (material)

The staging framing of "~3 weeks to the Q2 cluster" is only the cluster's start. Per `decisions/earnings_calendar_vet_2026-07-03.md`: STNG/ASC/SB land Jul-28/29, ECO Aug-4, SBLK Aug-5, TNK ~Aug-5, BRUT Aug-13 — but FRO is confirmed Aug-31, TRMD Aug-26, HAFN Aug-28, CMBT Aug-27. A single re-anchor waiting for the full family holds the war vintage ~7 weeks, not 3. The ruling therefore adopts a two-stage design (§5.2): the vintage retires no later than Aug-15 on the names landed by then (every major class is covered: VLCC via DHT/ECO/INSW, Suezmax via INSW/NAT/ECO, Aframax via INSW/TNK, LR2/MR via STNG/ASC), and the late tail true-up runs only if it moves a class median beyond a registered band.

## 5. THE RULING — (i-continue), two-stage, four riders

(i-continue): the Jun-7 tanker forward hold continues to the Q2-cluster re-anchor. Rationale: one coherent multi-name, multi-class re-anchor beats a single-fixture reshape (§1) plus a second reshape at the cluster; the deferral cost is bounded and direction-safe (§3); the interim state is disclosed and quantified (Rider 1).

1. Rider 1 — header truth, today. The "no market forward print exists" language in `ffa_forward_curve.yaml` vintage_notes (line ~54), the `twelve_month_tc.yaml` header, and the trigger's observable text is replaced with the §6 prepared annotations before any other action. This is unconditional and independent of signature timing on the rest.
2. Rider 2 — hard exit, two stages, unconditional fallback.
   * Stage A: promote from cluster disclosures no later than 2026-08-15, using everything landed by Aug-14 close, per the pre-registered method. If the registered minimum basis (PRE_REG §6) is not met by then, promote on the DHT print alone with the registered tenor decomposition, documented as such. No extension exists in any state of the world; the Jun-7 vintage does not survive past Aug-15.
   * Stage B: true-up window 2026-08-26 → 2026-09-04 (FRO/TRMD/HAFN/CMBT tail). Executes only if any class median moves >±10% vs the Stage-A anchor (PRE_REG §6); otherwise record-no-change in decisions/ and stand down.
3. Rider 3 — method frozen before results. `PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR.md` is signed and committed before 2026-07-28 (first cluster prints). If it is not frozen by Jul-27 EOD, Stage A executes on the DHT-print fallback at Aug-15 — the re-anchor may not be method-shaped by results already seen.
4. Rider 4 — the registered observable stays armed. Any tanker FFA or 12M TC print landing in the dailies/weeklies before Stage A promotes immediately under the trigger's original action (it is mechanically executable), superseding the Stage-A date. Stage-B logic then applies unchanged.

## 6. Prepared annotations (paste-ready on signature)

`inputs/market_data/ffa_forward_curve.yaml` — replace the vintage_notes hold text:

```
HELD at the 2026-06-07 vintage — TERM PRINT EXISTS (DHT 6-K 2026-07-13: 3-yr VLCC
TC $75k/day Sep-26 start; Q3 QTD bookings $139.7k corroborate the front within ~5%;
back-half implied 40-55% below this vintage). Promotion deferred to the Q2-cluster
re-anchor by owner ruling 2026-07-14 (decisions/tanker_forward_print_ruling_2026-07-14.md):
Stage A no later than 2026-08-15 (unconditional — DHT-print fallback if cluster basis
insufficient), Stage B true-up ≤2026-09-04 band-gated. Estimated strip overhang while
held: −3 to −4% FV on peak-weighted crude, direction-safe (can only make rich names
richer; no false-BUY exposure — ruling §3). Method: PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR.md.
```

`inputs/market_data/twelve_month_tc.yaml` — same replacement in the header comment, plus: `# NOTE: the DHT 3-yr fixture is NOT a 12M TC print; this line stays held per ruling §1 (letter) until Stage A or a dailies/weeklies 12M print (Rider 4).`

`inputs/reweight_triggers.yaml` — `tanker_forward_print_lands`: set `status: fired-ruled-deferred` with `ruled: 2026-07-14`, `stage_a_deadline: 2026-08-15`, `stage_b_window: 2026-08-26..2026-09-04`, `ruling: decisions/tanker_forward_print_ruling_2026-07-14.md`; observable and action text retained verbatim (Rider 4 keeps the original mechanics live). Sentinel treatment: the fired/red surfaces as AMBER-deferred with the Stage-A date, so it keeps appearing in `--pure` output without demanding daily re-triage.

## 7. Separate thread — the Jaguar fixture as a DHT company input

Independent of the curve question, the fixture is a disclosed 3-yr charter starting inside DHT's strip horizon: it changes DHT's own `spot_coverage` / disclosed-charter-rate blend (and at $75k vs the ~$84k implied current charter rate, nudges DHT's strip down through the coverage channel regardless of curve promotion). Batched into the Stage-A regen as a normal company-input update with the 6-K as provenance — recorded on `decisions/dht_log.md` now so it cannot be lost, executed with Stage A so there is one DHT regen, not two.

## 8. DECISION block (owner)

* ☐ RULE (i-continue) as specified — two-stage, Riders 1–4, dates as written (Stage A ≤ 2026-08-15; Stage B window 2026-08-26..09-04; band ±10%)
* ☐ RULE (i-continue), dates amended to: Stage A ≤ ________ · Stage B ≤ ________ · band ±____%
* ☐ RULE (ii-promote now) on the DHT print with the registered tenor decomposition (rejects §1 letter-analysis; single-fixture anchor accepted as documented assumption)
* ☐ Other: ________________

Signature/date: ________________ · On signature: apply §6 annotations, append RATIFY_LOG-style entry to decisions/dht_log.md (§7), commit ruling + prereg together.

Provenance: DHT 6-K filed 2026-07-13 (sentinel flag 2026-07-14); held-vintage figures from committed `outputs/dht_fv_report.md` (2026-Q1, commit `1d3db14`); verdict positions from `outputs/book_scorecard.md` (2026-07-14 vintage); earnings dates from `decisions/earnings_calendar_vet_2026-07-03.md`; trigger text from `inputs/reweight_triggers.yaml` @ `d1c702e`. Drafted by the external reviewer (same session as EXTERNAL_AUDIT_2026-07-14 / methodology_review_memo_2026-07-14); all promotion authority remains owner-only.

---

## ADDENDUM (2026-07-15, agent verification pass — DECISION UNCHANGED, STILL UNSIGNED)

Committed as drafted by the external reviewer; verification before signature found the
arithmetic and calendar claims EXACT (held-curve front 147.5 / Q5-Q8 avg 125.0 / 12M avg
155.0 recompute from the live YAML; FRO Aug-31, TRMD Aug-26, HAFN Aug-28, CMBT Aug-27 all
match the vetted calendar) and ONE material vintage correction:

**§3's scorecard walk predates the same-evening Hormuz re-tilt** (RESTORE BOTH, executed
fb00ede + ratified b87f832 ~2h after this draft's scorecard snapshot). Post-re-tilt:
TRMD is **BUY +8.4%** (draft: "TRMD −1%" near-edge HOLD), STNG is HOLD −1.0% (was TRIM),
ASC +4.0 / TNK +1.3 / CAPT −1.9. Consequence: the §3 claim "a false BUY held on an
inflated FV is not live anywhere in the book" is now QUALIFIED — TRMD's BUY sits at
+8.4% and its clean-product strip lines (MR/LR2_clean, inside the held complex) would
trim at Stage A; a −3-4% strip trim brings it toward the +5% boundary. This does NOT
overturn the direction-safety finding (the trim direction remains toward-boundary, never
signal-creating; TRMD's BUY rests primarily on its NAV leg — k_broker 1.03, the book's
tightest) but TRMD joins the Stage-A expected-flip eyeball inventory explicitly. The
deferral-vs-promote trade is unchanged in substance; the owner signs with this caveat
on the record. Interim truth-fix (the separable Rider-1 core) applied 2026-07-15 in
ruling-NEUTRAL wording — the YAML headers now state a term print EXISTS and this ruling
awaits signature; the §6 verbatim annotations (which assert the ruling) apply at
signature, not before.
