# WO5 / R4 — crude deck re-expression + Stage-A void dispositions (owner-scheduled)

**Status: DRAFT FOR RATIFICATION (prepped 2026-09-01 at owner go "prep the R4 work
order"; adversarially verified by a 3-lens panel — discipline / grounding / mechanism
simulation — and revised to their findings the same sitting).**

**The full owner surface in this WO (enumerated):** (1) the Phase-0 method fork ·
(2) the Phase-1 sequencing gate · (3-5) the three per-name void dispositions ·
(6) TNK's destination registry if freed (name-specific short vs §12 cycle-relabel) ·
(7) the B1 docket re-arm (or ruling, if taken) · (8) the ratify (owner runs
`ratify_baseline.sh`, owner commits) · (9) the push. Items 8-9 are owner ACTS by
standing law, not delegable.

**Authority:** the 2026-08-10 Stage-A halt, disposition B — owner-ruled "LAND + VOID"
(decisions/stage_a_halt_investigation_2026-08-10.md; RATIFY_LOG @ d510311: "BRUT/CAPT/TNK
BUY-ward flips VOIDed as deck-incoherence artifacts") → the 2026-08-16 C2 venue ruling
§R4: "Stage-A voids STAND … Deck re-expression is docketed as its own work order; the
retire/re-read executes there," carrying wf_8b0d1184 correction 2 ("one void name reads
BUY-ward at tape, not two") → the 2026-08-31 SCOPE word (brut_demerger_carry §RESIDUALS):
"the deck re-expression work order re-reads the LIVE 4-hull BRUT — not the historical
12-hull object" → scheduling go 2026-09-01 (owner, this sitting).

**What this buys:** a crude scenario deck whose de-escalation legs price REAL deltas
against the live rate base again — and, on that honest deck, the lawful per-name
disposition (retire / uphold / re-read) of the three Stage-A voids. **This WO authorizes
ZERO capital, changes NO scenario weight (the C2 vector 0.25/0.62/0.00/0.13 is frozen
input), moves NO tier, and implies no position.** A retired void produces a raw governed
surface read, not a trade.

**Read before starting — the one thing this must NOT become:** a license to make CAPT
actionable. The void and the read are separate machinery: even fully retired, CAPT's
read stays GOVERNED-WIDE · newbuild-heavy (read_blocked — §17 construction; no
`read_flag` while the NB share > 0.25, so the verdict cell prints the RAW un-deadbanded
band label with the W-frag caveat beside it) and WEIGHT-DRIVEN at the 9/01 sidecar
(+6.7% BUY Set A ↔ −21.2% TRIM conservative brackets — TO BE SUPERSEDED by the
post-re-expression sidecar before any ruling relies on it). The product is surface
honesty, plus the consumer's WIDE-capped sizing lane opening where the tier supports
it. Edge-cleared stays {SB} unless its own guard moves at owner word.

**Kill-switches (precedence stated):** the Stage-A addendum rule GOVERNS — **any flip
toward BUY on a NON-void name at the production regen = halt-and-investigate, even if
Phase 3 predicted it** (a predicted BUY-ward flip is still an owner eyeball, never
auto-accepted; Phase 3's "unpredicted = halt" is the floor, not the ceiling) · any
scenario WEIGHT question surfacing = finding to the owner, never in-scope work · Stage B
not disposed by 2026-09-05 → the sequencing gate returns to the owner · the drift gate
reds anything unexplained → stop, annotate, no bundling.

**Labor budget:** one sitting, honestly loaded: the re-derivation + guard + what-ifs +
freeze ≈ half; the production landing, ~9 crude/hybrid-row gate annotations (DHT FRO
ECO INSW TEN NAT TNK CAPT BRUT — every crude-sleeve name moves >2pp EV by design, each
needs its dated log annotation), five sidecar re-runs, and the three dispositions ≈ the
other half. NOT in budget: OMC anything, Stage B itself, the S&P promotion round.

---

## Existing assets (verified 2026-09-01 — do not rebuild)

- **The incoherence mechanism is fully diagnosed** (stage_a_halt_investigation §2-3):
  the deck's ABSOLUTE $/day scenario paths (2026-05-29 build, war-recalibrated 7/02)
  vs the Stage-A base (Jun-7 vintage RETIRED 8/10; VLCC 12M $105,700 Mount Horizon)
  make de-escalation legs near-no-ops — Pre-MoU Vessel× 0.82 → 0.96 against the new
  base; the de-escalation risk the weights exist to carry (0.57+0.05+0.13 at the 8/10
  diagnosis; 0.62+0.13 after C2 retired mou_base to zero) was silently absorbed into
  the base. The base's back half (VLCC Q5-8 $48.85k) already embeds the Jaguar term
  print's de-escalation.
- **The lawful retirement mechanism exists**: `POSITION_UNRELIABLE` registry
  (provenance.py:147-153) + the NAT de-void precedent (NAV_DERIVED_VOID emptied
  2026-06-30, registry kept as coverage). Pins that MOVE with a disposition:
  test_tier_semantics_amendment.py:156 (TNK-in-set — moves only at TNK's
  disposition). Guards to VERIFY-UNCHANGED (do not edit): :124 (BRUT/CAPT
  read_blocked hold GOVERNED-WIDE — stands because read_blocked stands), :137
  (edge-cleared == ["SB"] — stands unless reads move), test_scorecard.py:658-661
  (registry containment/disjointness). NOTE the registry comment's stale pointer
  ("RETIRES … at the crude_day60_toll_cliff re-derivation (2026-08-16)",
  provenance.py:152) — superseded by this docket; FIX the comment in the first
  disposition commit.
- **Re-pins/comments awaiting this WO** — the honest blast radius: pins that MOVE
  (crude-sleeve names only): test_scenarios.py:129 (`test_nav_flexes_with_scenario` —
  "the direction re-pins at the … deck re-derivation"), :169-174 (bear<base ordering —
  BINDS the re-derived `mou_base` curve: the zero-weight leg's CURVE must still be
  re-derived or this reds), :193 (FRO TRIM pin — likely green, direction TRIM-ward),
  :615 (INSW, crude sleeve), :1106-1107 (TEN, crude sleeve); adjacent deck-dependent
  checks to verify: test_eco.py:57-68, test_breakeven_sensitivity.py:79
  (render-only). Comment-ONLY cleanups (no number moves — the determinant-leg law
  predicts exactly 0.00 for pure-product names): test_scenarios.py:834 (HAFN — the
  stale "re-reads at the 8/16 deck re-derivation" note; the :828 band is the fresh
  8/31 Q2-refresh pin and must NOT move).
- **The §9.10 family sidecars are a MANDATORY consequential step**: editing
  sectors.crude changes the scenario_inputs.yaml sha → every family stamp lags →
  test_outputs_hygiene reds the committed scorecard. All FIVE sidecar scripts re-run
  after the landing, before the scorecard regen is committed (the a8e9914 precedent,
  bit twice in the 8/31-9/01 refresh arc).
- **read_flag law for reference** (tier amendment §3 + Addendum A §2;
  justified_pnav.py:181-198; hysteresis 2.0%; margins off the WATCHLIST VINTAGE, tape
  strobe on the delta layer only): it applies to NO name in this WO — TNK already
  carries live governed state (never read_blocked); CAPT/BRUT remain read_blocked
  (n/a) regardless of the void. Kept here so nobody re-derives it wrong mid-WO.
- **What-if isolation precedent**: the 7/22 B′ proposal's 3 isolated-worktree pipeline
  runs — predicted deltas computed OFF-TREE, frozen, then ONE production landing
  verifies. Runs never write governed state (B4).

## Phase 0 — methodology decision doc FIRST (owner fork)

Write `decisions/r4_deck_reexpression_method_2026-09-XX.md` before touching YAML.
The fork, with recommendation:

- **Fork A — structural: convert the crude scenario curves to RELATIVE multipliers on
  the live base.** Honors the Stage-A prereg §0 intent ("scenario *deltas* stay
  expressed relative to whatever base curve this re-anchor lands") permanently.
  COST: a scenario-engine change mid-season touching every crude fixture; a
  two-convention engine until the other five sectors migrate.
- **Fork B — one-time re-derivation: new ABSOLUTE per-quarter paths calibrated to the
  post-Stage-B base**, each leg's registered meaning re-expressed as a real spread
  (escalation = genuine upside tail; pre_mou_baseline ≈ the observed state ≈
  base-tracking; mou_bear = normalization-disappoints; `mou_base` re-derived TOO —
  zero weight, but its curve binds the :169-174 ordering guard and the fv_low/fv_high
  interval). COST: the bug class recurs at the NEXT re-anchor unless re-done.
- **Fork C (rider on B, recommended): B + a deck-coherence GUARD** — a test asserting
  each weighted crude scenario's implied Vessel×-vs-base spread stays inside
  registered bounds (red = the deck has gone no-op again). Guard over prose.

**REC: Fork B + C now; Fork A registered as the durable candidate for the post-season
refactor window (Q4), not ruled here.** Named sub-decision for the owner inside
Phase 0: `mou_bear` (weight 0.13) carries a premise the C2 record calls CONTRADICTED —
the re-expression gives the leg an honest curve meaning WITHOUT touching its weight
(compatible with the fee-collection watch's registered "→ mou_bear mass" action); if
the owner judges the leg unsalvageable, that is a weight question = OUT of this WO.
**Finding routed to the owner, not silently resolved:** whether the PRODUCT deck's
absolute curves need their own re-expression against the Stage-A base is an open
question this crude-scoped WO deliberately does not answer.

## Phase 1 — sequencing gate (owner word)

R4 executes on the SETTLED base. Pending events that move the same objects:

1. **Stage B (window closes 9/04)** — the ±10% class-bucket gate on the tanker 12M
   lines; the Suezmax bucket is expected to TRIP (direct prints 74.5-80k vs held
   58,050, ~25-28% low; VLCC 1yr MB 122.5k vs held 105.7k = +16% single-print
   caution). Executing R4 first would re-express against a base known to be
   mid-correction.
2. **CMBT 9/03** — balance-sheet wiring, not deck; safe to interleave before R4.
3. **The staged S&P promotion round** (10 rows incl. a Suezmax print; the VLCC print
   — Front Vefsna — rides the FRO refresh under the P1 pre-ruling, not this round) —
   moves the txn-anchored marks. Preferably ruled BEFORE R4 so Phase 3 freezes on
   settled marks; if deferred past R4, record the marks vintage used and arm the
   round as a NEW-eyeball trigger on the dispositions' recross watches.

**REC: execute R4 on 2026-09-04/05, immediately after the Stage B disposition (and
after CMBT), with the promotion round ruled either before it or explicitly after.**

## Phase 2 — author the re-expression, STAGED not landed

Per the Phase-0 ruling: derive the four crude scenario curve sets against the live
(post-Stage-B) base, with per-leg derivations documented in the Phase-0 doc's appendix
(per-leg provenance, the Vessel× spread each leg now implies — Stage-A-computation-
draft rigor). Author the Fork-C coherence guard. **Nothing lands: the candidate YAML +
guard are STAGED (draft file / uncommitted), no regen, no pin edits yet.** Weights:
byte untouched; `mou_base` stays retired-at-zero (its continuity guard at
test_scenarios:67) with its curve re-derived per Phase 0.

## Phase 3 — isolated what-ifs + THE FREEZE (before anything lands)

Isolated-worktree what-if runs (7/22 pattern) on the staged deck produce per-name
predicted EV/read for all 25 names. FREEZE, dated, in the Phase-0 doc: (a) the three
voids' predicted reads + bands; (b) per-name invariance expectations for the other 22
— **crude-sleeve names get predicted deltas; pure-product and non-tanker names get
EXACTLY 0.00 (the determinant-leg law: a frozen-leg name printing nonzero = HALT)**;
(c) the new values for every pin in the blast-radius list above; (d) the halt rules
(the kill-switch precedence governs). Calibration-only tape reads as of 2026-09-01
(NOT the frozen bands — those freeze post-Stage-B): CAPT +6.7% BUY-shaped · TNK −5.4%
TRIM-shaped · BRUT +3.6% HOLD-shaped, k 0.99.

## Phase 3b — the landing (ONE production event)

Land the deck + guard + pin moves (values from the freeze) in one commit; regen state
FIRST so the gate is awake (the 8/16 green-with-gate-asleep lesson); run the
production regen + verification loop; **re-run all FIVE §9.10 family sidecars** and
regen the scorecard so the family stamps are current; verify every frozen expectation
(bands, zero-deltas, pins) or halt; annotate the ~9 crude/hybrid drift-gate rows with
dated per-name log entries. The post-re-expression CRUDE SIDECAR now supersedes the
9/01 sidecar as the weight-robustness evidence for Phase 4.

## Phase 4 — the three dispositions (owner rules PER NAME; each its own commit)

Per name: decisions/ record of the ruling → provenance.py registry edit + dated
comment (fixing the stale :152 pointer in the first commit) → the name's moving pins
in the SAME commit → regen → gate annotation → the name's log entry.

- **CAPT — the one BUY-ward void at tape.** Question: does the re-expressed deck
  still print the BUY-ward read, now as signal? If YES and the owner retires the
  void: CAPT leaves POSITION_UNRELIABLE; the verdict cell renders the RAW
  un-deadbanded band label (no read_flag while read_blocked) with the weight-driven
  caveat beside it; read_blocked and GOVERNED-WIDE·newbuild-heavy STAND; consumer
  seam: the TRADE_PREREG #4 WIDE cap governs any sizing. **CAPT becomes the book's
  FIRST read_blocked-and-not-unreliable row — no test pins that rendering, and near
  the +5% EV edge the raw label can strobe BUY↔HOLD with no hysteresis: ADD a pin
  test for the rendering combination in the disposition commit, and note the strobe
  exposure in the ruling record.** Evidence inventory for the eyeball: the 9/01
  print (hairline +0.1% band BREACH, halt investigated, §5-breach-accepted — the
  at-contract, below-market acquisition +$1.71/sh filing-cited), k 1.17, the
  post-re-expression sidecar; AGAINST: weight-driven history, 20-of-33 forward
  book, the general crude-near-peak context (soft, not a record fact). If the
  re-expressed deck kills the BUY-ward read, the void retires WITH a HOLD/TRIM-shaped
  read — equally valid; the point is trustworthiness either way.
- **TNK — the artifact void.** wf_8b0d1184: its BUY-ward print was a stale-static
  sim artifact; at the 9/01 tape TNK is TRIM-shaped (−5.4%) at VALIDATED-TIGHT,
  robust. Retirement expectation: uncontroversial mechanically (move :156 with the
  commit) — **but freeing TNK flips the committed verdict prose silently: the
  named-shorts survey would print "Name-specific shorts: TNK" where the book has
  carried "not one is a name-specific short." That is a real escalation on the
  handoff surface and is an OWNER question (item 6): render freed-TNK as a
  name-specific short, or route it to POSITION_CYCLE_RELABEL beside its §12 crude
  peers (DHT/FRO/ECO/INSW/NAT). REC: cycle-relabel — TNK's rich read is the same
  late-cycle shape, not a name-specific short thesis; a genuine short call is a
  governance-side decision, not a rendering default.** No read machinery changes
  (TNK was never read_blocked; its read_flag state is live and governed already).
  Losing the :156 anchor RE-ARMS the B1 docket (POSITION_UNRELIABLE as an
  edge-cleared conjunct — currently moot: post-retirement no registry name is
  robust-cheap). **If the owner rules B1 YES at this sitting (item 7), that is its
  own commit: the scorecard longs filter + its definition prose + CLAUDE.md's
  edge-cleared one-liner + a BIND-guard test (the :137-145 test computes its own
  filter — production and test must be tied or they diverge silently). Consumer repo
  untouched (it consumes the exported position string).**
- **BRUT — re-reads, does not auto-retire (the 8/31 scope word).** The re-read
  object is the LIVE 4-hull entity (Vision ytd-0.02 §9.6 stand-in, Horizon fixed
  $105,700/day net from Nov, Frontier/Summit 2027; commitment $398.076M; cash
  $11.828M cited-with-known-unknown; debt $0; k 0.99, HOLD-shaped).
  Going-concern-unfinanced + §15 flags STAND regardless. A legitimate outcome is
  UPHOLD: the post-6/30 cash/debt known-unknown (July SLB draws + the $50M OMC
  contribution, undisclosed) resolves at the ~end-Sep uplisting prospectus or
  FY2026 — the owner may keep BRUT voided on that rider alone, with the disposition
  re-armed to the prospectus. NO OMC surface enters; the 12-hull-era numbers are
  dead artifacts.

## Phase 5 — gates & close (owner acts marked)

Full suite green with the gate AWAKE · `/reconcile` SANITY OK on the three names ·
drift gate rows all explained-or-ratified — **one ratify over the per-name-decomposed
causes (the 8/16 two-cause precedent), cause string naming this WO — the OWNER runs
`ratify_baseline.sh` and the OWNER commits (baseline file + RATIFY_LOG row in ONE
commit — the 8/31 half-commit lesson)** · RATIFY_LOG + CHANGELOG entries · PLAN.md
fact-3 rewritten (voids → dispositions) · **push = OWNER act**.

## Definition of done

Deck re-expressed per the Phase-0 ruling with the Fork-C coherence guard LIVE · the
blast-radius pins moved dated, the HAFN stale comment cleaned (no number move) · all
five family sidecars re-run and the scorecard stamps current · three dispositions
RULED and executed-or-upheld, each with its decisions/ record, registry edit, moving
pins, and log entry in one commit · TNK's destination registry ruled (item 6) ·
forward invariance verified against the Phase-3 frozen expectations (crude-sleeve
deltas in-band; pure-product/non-tanker EXACTLY 0.00), zero BUY-ward flips accepted
without owner eyeball · B1 ruled or explicitly re-armed with its trigger (item 7) ·
suite green gate-awake · ratified (owner) · pushed (owner) · PLAN/CHANGELOG updated.

## Non-goals / frozen

Scenario WEIGHTS (C2 vector) · every tier and tier-subreason · edge-cleared
membership except via item 7's own guarded commit at owner word · OMC
(release-capture watch only; onboarding = funnel decision) · CAPT option value
($253.7M stays excluded — we do not value optionality) · Stage B's disposition
(input, not subject) · the consumer repo's TRADE_PREREG mechanics · the PRODUCT
deck's own re-expression question (routed to the owner as a finding, Phase 0) · the
other sectors' decks. Any of these surfacing as *needed* is a finding to report to
the owner, not in-scope work.
