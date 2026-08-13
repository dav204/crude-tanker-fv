# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest.


**Current state (2026-08-09, Sunday EVE — SESSION HANDOFF).** Read this block, then start at
§NEXT BLOCK step 1 (tomorrow is INSW morning). **Suite 636 green + 15 xfailed · drift gate 0/0
· tree clean at db53188+ · producer ~9 commits ahead — NEEDS A PUSH (owner-gated).** The book
runs 2026-Q2 on the 8/07 price basis; every Q2 sheet is on file (the 14-name drain closed 8/08
with every pre-registered band HIT).

**THE 8/09 PROMOTION ROUND IS CLOSED (owner-authorized, three ratified/verified events):**
(1) **Marks-trail** (`decisions/marks_trail_triage_2026-08-09.md`): 28 in-window S&P prints —
war-tape VLCCs $120-130M @ 9-13y, Ellie Lady LR2 $47.5M @17, 5 PPMX incl. the first young node
(Pont Rouge @5), 11 Supra — plus 2 G5 revisions; **4 unnamed-print duplicates caught and
unwound** (the whole queued Pareto disposition was re-reports — new WORKFLOWS rule: sweep the
class file before promoting ANY unnamed print). DHT NAV +8.4%; SB EV +31% (TIGHT BUY
strengthened, PPMX evidence base now 10 prints); **k_broker pure-play premium COLLAPSED to
~1.00-1.04 → `TXN_PURE_PLAY_K_BAND` re-pinned (0.95, 1.15)** — partly pnav-vintage skew, the
REBASE IS NOW PRESSING (draft staged, see below). (2) **Dry-bulk FFA, 8/06 print**
(`ffa_promotion_2026-08-09.md`): tenor set rolled to Aug/Sep/Q4/Q1-27/Cal27 — 12M proxies
stepped DOWN on window COMPOSITION (Q1-trough entered; like-for-like Q4 FIRMED +4.3%): Cape
31,550 / Pana 18,300 / Supra 16,750; Smax Cal27 still cropped (held 2027-28 legs disclosed ~5%
rich vs the now-printed Q1-27). **SBLK BUY→HOLD band-mech = purely 12M-composition (ΔNAV 0.0)
→ FROZEN-FOR-OWNER-REVIEW** (one-word disposition owed; its Q3-coverage slide 62% @ $23,547
corroborates composition-not-weakness). (3) **Containers, MB W32**
(`container_mb_refresh_packet_2026-08-09.md`): Ctr-Large 12M 64,000 + feeder 10yr mark 29.5
(TC+VALUE joint; NAV-halt verified — MPCC +0.5% only); trigger re-armed 9/07.

**STAGE A: COMPUTED + RULED, WIRES TOMORROW (8/10) AFTER THE INSW PRE-MARKET PRINT.**
`decisions/stage_a_computation_draft_2026-08-09.md` carries the §§1-4 construction, the §5
scoreboard (VLCC front 179.65k BREACH-HIGH + term-implied 48.85k BREACH-LOW, both traced to
ECO's verified $206.6k QTD print, tape-corroborated), and the FOUR OWNER RULINGS: wait-for-INSW
· breaches ACCEPTED post-investigation · VLCC 12M = Mount Horizon $105,700 single-print (BRUT
is all-VLCC) · LR2_clean term = §4-letter 28,000 flagged. The INSW refresh itself is
PRE-REGISTERED (`decisions/insw_q2_prereg_2026-08-09.md`: point $56.30, band [51.50, 61.00],
forward-invariance + subsequent-events-first + the Q3-QTD-extraction step that feeds §6).

**STAGED FOR THE OWNER'S WORD:** `inputs/watchlist_rebase_2026-08-07.yaml.draft` — the full
consensus-pair transcription from the 8/7 Pareto daily (16 pareto-basis + 4 approx names;
kr-quoted rows flagged for FX at promote). Promoting it retires the k-vintage-skew test debt.

**2026-08-13 PM UPDATE (July-hole audit — owner-directed backfill executed).**
Result: **NOTHING TO BACKFILL — attribution corrected** (full record: brut_log 8/13 PM
entry). The 7/03→7/14 Pareto gap is SOURCE-QUIET (Pareto's Jul/Aug cadence; the 7/12
seasonal note in `rocketchat_sources.yaml` covered it): full RC history walk (uncapped,
since 7/01, 2,379 msgs) = zero Pareto posts in the window while the sibling FFA lane
ingested daily; archive == channel exactly for 7/01→8/13. The "harvester outage" was the
weekly broker-marks lane (revived 8/11) — a deep 40-page HSN+CapitalLink recrawl
recovered NO July weeklies either (mirror-side non-publication; W33 banchero/fearnleys
picked up; allied dead in 2026). So the BRUT-miss remediation rests on the surviving
causes: untriaged name-text + NO ISSUER CHANNEL (NewsWeb) — the latter is now the
load-bearing gap. **Full-window `--names all` sweep executed** (issues 7/14→8/13, manifest
rebuilt to 8/13): 15 decision logs triaged. **TWO OPEN PRINT FLAGS (not promoted):**
FRO 2×2017-built VLCCs (8/04, "extreme prices", NO price disclosed yet — watch MB
W33/W34 + FRO Q2) · CMBT 'Bristol' 2024 suezmax (8/11, $57m Q4 gain, beyond the 8/07
print cursor — expect in the Sat 8/15 queue). **HEADS-UP for tonight: OET trades ex-div
$5.25 Oslo 8/13 / NY 8/14** — don't read the price drop as drift; the staged 8/07
watchlist-rebase draft pre-dates the ex-date. No prints promoted, no regen run
(prices_daily untouched by this work). NOTE the interaction with the 8b ARCHIVE-GAP
check landed in parallel (block below): its flagged July/early-Aug Pareto holes are this
same verified cadence — accepted-gap entries for `inputs/archive_gaps.yaml` are now
evidence-backed by the RC walk.

**2026-08-13 PM — WATCHDOG REMEDIATION (owner-directed after the BRUT miss).**
Root cause of the 5-week blindness was NOT a crash: `/news-pull`'s agent half ran
TWICE (6/10, 6/21), its orchestration was **deferred by owner 2026-06-14 under the
crude-edge freeze**, the freeze lifted 6/21 and the deferral was never re-docketed —
while the MECHANICAL job sharing its name reported `outcome=ok` every Saturday.
THREE FIXES LANDED (commit 40a3496 + this one, suite 639 green):
(1) **ARCHIVE-GAP (8b)** — every prior staleness check read the NEWEST artifact
(alive-now) and was blind to a hole BEHIND the head. Now counts missing business
days; accepted publication holidays go in `inputs/archive_gaps.yaml`. Live tree
shows **5 gaps**, incl. the 6-day July hole that hid the BRUT release (plus
7/15-19, 7/21-27, 7/29-8/02 — previously unknown). News read from a gap window is
UNSUPPORTED, not absent.
(2) **AGENT-TASK-DUE (8c)** — check 6 sees jobs with plists, check 8 sees feeds
with artifacts; a duty living as a slash command was invisible to both.
`inputs/agent_duties.yaml` now registers such duties.
(3) **SCHEDULED the sweep** — Claude scheduled-task `crude-fv-weekly-news-pull`,
**Sat 09:03** (after the 08:00 chain). Closes the 6/14 deferral. The digest's age
IS its heartbeat: if the task dies, 8c flags it. Prompt carries the absence-isn't-
evidence rule (must state window + sources searched, never a bare "nothing found")
and an archive-gap check. **OWNER: click "Run now" once** to pre-approve its tools
— an unapproved tool prompt at 09:03 Saturday aborts the run silently (the exact
failure that killed the governance monitor's 8/07 run).
(4) Check 6 also now flags **3 consecutive `skipped-*` runs** (a skip writes a
FRESH heartbeat by design, so a job standing down forever looked healthy — a
forgotten PAUSE would silence all six jobs with six green hearts), and the weekly
limit tightened 9d→8d.
**URGENT, OWNER-ONLY — THE PAGER IS OFF:** `~/.config/crude-tanker-fv.env:8-10`
still has `CRUDE_FV_HEALTHCHECK_URL` **commented out from the 2026-07-13 drill
whose own restore date was 7/15** — 29 days. `state/sentinel_cron.log`:
**PING-SENT 0 / PING-SKIPPED 30**. The ping is the ONLY mechanism that pages on
ABSENCE, so with it off the sentinel is an unwatched watcher — this is why all
four deaths went unseen, and why the 8/09 allowlist-matcher fix didn't restore it.
Uncomment that line. Also open from the sweep: `pareto_research silence_days: 14`
is 7× loose (its premise retired 8/09 when `drybulk_spot_daily_resumes` fired) on
the book's most fragile single-sender feed · `inputs/overlays.yaml` has 3 overlays
scoped to the RETIRED Jun-9 weights and `retire_trigger` is read by no code · 2
zombie `ctxprobe` launchd jobs still firing 6 weeks past a 7-day window · two
sentinel tags (`EARNINGS-UNCONFIRMED`, `EARNINGS-SWEEP-STALE`) unrouted so they
page every run, the latter with a trailing-colon bug in the tag itself.

**2026-08-13 AM UPDATE (Thursday — BRUT report day).** H1 IS OUT (Pareto 8/13 daily
covers it) and the owner-requested AGM/feed check surfaced a **MISSED 5-WEEK
STRUCTURAL CHAIN** (full record: brut_log 2026-08-13 entry): issuer release
**7/07** — Vision DELIVERED 7/08 on a 3+1+1y index-linked TC ($95k/d fixed 9mo),
sale-leaseback signed for the 4 NTS hulls (85-90% of cost, 15y BB ~5.6%),
**DEMERGER announced** (BRUT keeps 4×2026-27 as a monthly-dividend cashflow co;
8×2028-29 demerge to a new Euronext Growth listing by END-AUG; BRUT uplists by
end-Sep), interim CEO Svensen. 8/13 daily: demerger on schedule, rump "fully
financed" subject to completion (83% capex outstanding 8/12), **Horizon joins
MID-NOV-26 at $106k/d** (manifest says Jan-27 — re-date at the pair; ≈ the ruled
$105.7k print, Rider-4 corroboration). **AGM 8/12 results:** routine slate + share
premium −$226.04M → contributed surplus eff. 8/12 (the dividend plumbing). Why
missed: 7/03→7/14 archive hole (CORRECTED 8/13 PM: source-quiet — no dailies existed;
see the PM block above) + the 8/06 daily's BRUT paragraph untriaged at the FFA sitting
→ dated rule added to WORKFLOWS §Report-day refresh; backfill CLOSED (nothing to pull). **The frozen prereg band
[8.50,10.00] still governs the mechanical 6/30 pair** (all of the above is
post-6/30 subsequent events; routing already correct). **OWNER WORDS NOW OPEN:**
run the H1 refresh per the prereg · demerger modeling (structural split, own
decision doc — compounds with 8/16) · §15 tier/flag call at the refresh
(financing-clarity event has arrived, by restructuring).

**2026-08-12 UPDATE (Wednesday).** BRUT H1 PREREG WRITTEN + FROZEN
(`decisions/brut_h1_prereg_2026-08-12.md`): point $9.68 note-gross / $8.87 note-net
(the ledger fork is BIMODAL — (cash − commitments) is deposit-invariant, so the 7/01
double-conservative corner un-double-counts by +$0.81/sh iff Note-15's CIMC $499.0M
was gross), band **[8.50, 10.00]**, halt-outside; Rider-4 hooks named (Mount Horizon
IS the live VLCC 12M single-print; Vision's index-linked TC); §15 screen +
cash-flag resolution + expected gate-row/ratify pre-registered; **position stays
VOID through the print — 8/16 is the only un-void venue.** Report 8/13, no stated
time (Euronext calendar; watch newsweb from the open). **AGM was today 8/12** —
outcomes route to the §15 screen; any pre-print AGM news amends the prereg dated,
pre-print only. Feeds silent on Q2 placements (brokers through W33, dailies through
8/12; BRUT kr 59.6 −0.7% today). **PANL B3 TRANSCRIPT SWEEP EXECUTED** (the other
Wed item): Q2'26 PR + call coverage + **FULL TRANSCRIPT (published 8/11 eve,
swept 8/12) — ALL ABSENT** on the COA/spot split, rendered-source-verified
(keyword census 0 across affreightment/COA/spot/voyage); prior-call premise
REFUTED — Q1'26 (Fool) + Q2'25 (Investing.com) transcripts carry zero COA-cover
characterization. Recorded as a dated ADDENDUM in the governance packet
(funnels/drybulk_2026H2/panl.md); B3 stays PASS-WITH-EXCEPTION; the packet's
"if absent → owner sends the staged IR query" condition FIRED and **the owner SENT
the IR query same-day (8/12) — B3 is now WAITING-ON-IR; watch the reply ahead of
next week's Stage-3 seed.** Q3 QTD bookings from the call:
4,873 days @ $20,258 (+14% premium, as-of 8/10) + 2,200 charter-in days @
~$17,537 — seed-relevant color.
NOTE for 8/16 context: today's daily reports fresh
attacks on vessels in BOTH the Red Sea and Gulf of Oman (day after Maersk/Hapag
announced a Gemini-service Suez return); Brent ~$90 — the toll-cliff branch state
is moving, not settling.

**2026-08-11 EOD UPDATE (Tuesday triage sitting — HANDOFF CURRENT).** Suite green ·
gate 0/0 · both repos pushed. Done today: **Diana SPA TERMINATED** (SBLK 6-K 8/11 —
zombie treatment vindicated, zero NAV impact, watch retired; governance-favorable) ·
**CCEC AGM slate CLEAN** (DiFiore in; proxy read — two routine proposals, no
related-party items; NOT the F-2 observable, that is PANL's slate) · **harvester
REVIVED** (Sat 8/8 launchd firing missed while the machine slept; manually kicked, all
five broker feeds backfilled W32 + xclusiv W33 — marks-trail feed restocked) · drift
absorbed · PANL Q2 skimmed (NI $10.2M/$0.16, cash $105.7M).
**THE WEEK FROM HERE:** (1) **Wed 8/12:** BRUT AGM watch · WRITE BRUT'S PREREG BAND
before Thursday (the INSW pattern) · sweep the PANL Q2 CALL TRANSCRIPT (call was Tue
8:00 ET) for the B3 spot-split — if absent, the owner sends the staged IR query
(funnels/drybulk_2026H2/panl_b3_ir_query_draft.md). (2) **Thu 8/13:** BRUT H1
refresh (pair flow, band-checked) + Rider-4 check (any BRUT 12M/FFA print supersedes
for its classes). (3) **Fri 8/14:** governance monitor + the healthchecks validation
(green check or a page by ~11pm; step-7b makes ping status a log fact). (4) **Sat
8/16 — THE CRITICAL DATE:** crude_day60_toll_cliff = the pre-registered crude+product
reweight on the toll outcome + the scenario-deck re-expression against the landed
Stage-A base (un-voids BRUT/CAPT/TNK; every tanker scenario read is
suspect-optimistic until then). (5) **Next week:** the PANL SEED (Stage-3 producer
onboarding — own block; the Handy-curve §9.9 ruling made explicitly at onboarding;
E2 completes at reconciliation) · TRMD 8/26 + Stage B. **CI NOTE (8/11 EVE):** sentinel-lite sat RED for 10+ runs unnoticed (unpinned ruff
drifted ahead of local — 461 phantom violations; FIXED: ruff==0.15.21 pinned, 8 real
violations cleaned, actions bumped). THE PATTERN (healthchecks, now CI): watchdogs
failing silently. **Handoff item: give the local sentinel a CI-status lane** (one
`gh run list` check — red CI on main = a sentinel line in the morning email).
**Owner words open:**
watchlist rebase promote (draft + checklist staged — retires the k-skew debt) · TEN
alternative-anchor · SBLK GTC riding (line $31.30, tape ~$28.4, ex-div re-read 8/19).

**2026-08-10 EOD UPDATE — STAGE A LANDED (commits d510311/1a6086d/7c991a5, pushed).**
INSW band-HIT ($54.64 in [51.50,61.00]; ER carried NO QTD bookings — basis closed on the
8/09 values); all four rulings executed; the Jun-7 war vintage is RETIRED. **THE HALT
FIRED AND WAS DISPOSED (B):** three flips toward BUY (BRUT +44.3pp / CAPT +17.8 / TNK
+5.0) = the war-calibrated ABSOLUTE scenario deck double-counting the Jaguar
de-escalation now embedded in the base (decisions/stage_a_halt_investigation_
2026-08-10.md) — CAPT/TNK joined BRUT in POSITION_UNRELIABLE, retiring at the 8/16
re-derivation. **8/16 IS NOW THE CRITICAL DATE (double duty): the pre-registered
toll-cliff crude+product reweight + the deck re-expression against the landed base**
(un-voids the three reads; every tanker scenario band re-pins there — they carry
dated deck-lift re-pins from today). Handysize 12M split from the MR war-identity
(donor Handymax). SBLK leg-2 GTC LIVE at $31.30 (governance, instruction id 100).
Remaining calendar: **BRUT 8/13** (Rider-4 watch) · **Fri 8/14** healthchecks
validation (green check or a page by ~11pm — prompt hardened both copies) · **8/16**
· TRMD 8/26 + Stage B (the 7th-TIGHT gate chain). Owner words open: watchlist rebase
promote (draft staged; retires the k-skew debt — clean to run any day now that Stage A
is down) · TEN alternative-anchor docket item.

**NEXT BLOCK — theme: STAGE A LANDS, then the date-driven tail.** _(written 8/09;
step 1 DONE per the update above)_
(1) **Mon 8/10 pre-market:** INSW Q2 refresh per the frozen prereg (pair flow, band-checked) →
extract Q3 QTD bookings + fixtures → stage_a_basis §6 update → RECOMPUTE the §2 medians/§5
checks → **wire Stage A** per the rulings + the §4 riders (DHT Jaguar coverage 0.55→0.52 ·
spot_tce promotion incl. LNGC 65,000 from MB W32 · C-2 rerun) → ADDENDUM flip inventory (TRMD
BUY toward the +5 boundary is EXPECTED-direction; ANY flip toward BUY = halt-and-investigate)
→ one ratify citing the prereg → re-arm the trigger. PANL reports 8/10 after close (seed
decision = owner's). (2) **Owner words pending:** watchlist rebase promote (draft
staged, checklist in-file) · SBLK leg-2 (governance; producer FV $31.28 ≈ the proposed
$31.30 line, ex-div ~8/21) · **TEN alternative-anchor decision** (the roster pin
codifies TEN as never-Pareto-recapturable — the $44-lesson name; guard
test_ten_untabled_is_tracked_not_fine keeps it visibly tracked, but the real fix is an
alternative anchor [VIE? company-implied?] or an accepted explicit-staleness stance). (3) **Wed 8/13:**
BRUT H1 (Rider 4 alert: any BRUT 12M/FFA print supersedes for its classes). (4) **Sat 8/16:**
`crude_day60_toll_cliff` — the pre-registered crude+product re-derivation venue (regardless of
Hormuz outcome; branch state at 8/09: ambiguous pause persists, Oman channel live). (5) **Stage
B window 8/26→9/04** (TRMD 8/26 · CMBT 8/27 · HAFN 8/28 · FRO 8/31): ±10% class-bucket gate;
the LR2_clean-term war-ratio distortion corrects HERE; TRMD 7th-TIGHT candidacy at the
post-Stage-A anchor round. Standing docket unchanged: Compass feed build · WF Artemis
G3-retroactivity · Diana SPA zombie watch · 2343 commitments true-up at the full Interim.

**PRIOR WEEK (2026-08-03) — theme: UNBLOCK THE Q2 CLUSTER, THEN DRAIN IT — DONE IN FULL.**
The transition mechanism ruled+shipped 8/08 (pair guard + preflight + vintage disclosure,
schema 2.7); SB/TNK/ASC re-run as the first coherent block (all bands hit, TNK back to
VALIDATED-TIGHT); the 11-name backlog drained by report date (every prereg band HIT, zero
unexplained gate rows); `crude_pause_talks_watch` recorded (branch 3); the 8/09 promotion
round + Stage A prep closed the week (this block above).

**PRIOR WEEK (2026-07-27) — theme: THE Q2 CLUSTER LANDS + the 7/29 quad-day.** Calendar-driven:
(1) **Mon 7/28** — GNK/Diana tender outcome PR expected (census recorded 7/26, gnk_log;
extension #3 / lapse / amended terms all live — the announcement un-pins GNK's tape);
ASC/SB report windows open (EARNINGS-UNCONFIRMED — run the date sweep). (2) **Tue 7/29,
the quad-day** — Hynix Q2 print + call 9am Seoul (governance G1–G5 restore gate; G4 already
1-of-4) · CCEC Q2 (the governance t2 print-gate venue) · TNK after close (call 7/30) ·
`crude_ceasefire_mediation_watch` due — **collapse-track week ⇒ B′ EXECUTES mechanically
(pre-registered 7/22 ruling; CAPT flip individual eyeball; mid-cluster landing accepted at
ruling)**, ceasefire ⇒ conditional VOIDS, owner proposal. (3) **Wed 7/30** — STNG Q2
pre-market (call 8:00 ET); LPG window. (4) **Per landed print:** report-day refresh flow,
subsequent-events note FIRST (DHT Impala/Bauhinia = the standing example: post-Q2 events do
NOT enter Q2 snapshots); fold ASC's pre-booked ~+1.9% Handysize correction; capture
STNG/ASC/TNK term-rate disclosures as **Stage-A cluster-basis prints**
(PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR §6 — Stage A ≤8/15 UNCONDITIONAL). (5) **Owner
items:** SBLK trim decision (governance-side, mini-review staged; a pre-set take-profit
fired — sizing is the consumer repo's business) · the Palun channel ask (Smax Cal27
row) · push both repos. **Definition of done:** every landed print reconciled-or-queued with its log entry;
7/29 watch recorded (B′ executed or voided); gate 0 unexplained at close; Stage-A basis
inventory grows with each term-rate disclosure.

**PRIOR WEEK (2026-07-20) — theme: Q2 intake + Stage-A basis accumulation.** The sprint is
calendar-driven: (1) **7/22** — Doha round-3 watch (record either way; the MoU-check evidence
leans collapse-track) + the Hynix Q2 print (governance executes its print-gated restore on
G1–G5); (2) **7/24** — tender census (gnk_log branch-c); (3) **from 7/28** — the Q2 early
cluster lands: run the report-day refresh flow per name (subsequent-events note FIRST), fold
ASC's pre-booked ~+1.9% Handysize correction, watch STNG/ASC/TNK term-rate disclosures as
**Stage-A cluster-basis prints** (PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR §6); (4) owner
items — batch price-vintage ratify · marks-trail triage (weeklies staged through 7/14, newest
promoted print 6/30) · baltic_indexes staleness disposition (probe verdict in the Week-close
audit). **Definition of done:** every landed Q2 print reconciled-or-queued with its log entry;
round-3 + census recorded; drift gate 0 unexplained at close; Stage-A basis inventory started.

**PENDING OWNER DECISIONS (do not act unilaterally; recorded 2026-07-08, extended 2026-07-14):**
-3. **2026-07-22 — MoU-scenario reweight: RULED SAME DAY (owner: "Rule A - conditional B′
   pre-registered on the 7/29 watch") — no longer pending; now SCHEDULED WORK:** no reweight
   now (weights stand at the Jun-9 shape; interim bias known-conservative). **B′
   (0.25/0.57/0.05/0.13) FROZEN + PRE-REGISTERED on `crude_ceasefire_mediation_watch` (due
   7/29):** continued collapse-track at the check → B′ EXECUTES mechanically (execution loop
   in the proposal; **CAPT HOLD→BUY eyeballed individually** — halt-and-investigate rider;
   mid-cluster landing accepted); ceasefire → conditional VOID, de-escalation proposal to
   owner. Aug-16 toll-cliff venue stands either way for the full MoU-family re-derivation;
   the B escalation-bump variant is NOT pre-registered. What-if basis: 3 isolated-worktree
   pipeline runs @ ac216cf (crude FVs +0.5-2% under B′, ΔNAV 0.0, non-crude byte-identical).
   Full doc: `decisions/mou_scenario_reweight_proposal_2026-07-22.md`.
-2. **2026-07-14 EVE — tanker forward re-anchor (trigger `tanker_forward_print_lands`
   FIRED, stays red until ruled) — STILL OPEN:** DHT's Jul-13 business update delivered a
   REAL term print — 3-yr VLCC TC $75,000/day (Jaguar, Sep-26 start) ~46% below the held
   war-vintage curve average, plus Q3 bookings corroborating the curve FRONT ($139.7k spot
   QTD). Options (i-continue ~3wks to the Q2 cluster / ii shape re-anchor / iii 12M-TC-only)
   in `decisions/tanker_forward_print_2026-07-14.md`; agent rec = (i-continue).
   **RULED + SIGNED 2026-07-15 (owner: "sign as specified") — (i-continue), two-stage,
   Riders 1-4; NO LONGER PENDING, now SCHEDULED WORK:** the prereg is FROZEN (incl. the
   pre-freeze TRMD addendum); §6 annotations applied verbatim; trigger
   `fired-ruled-deferred` with the AMBER-deferred sentinel treatment IMPLEMENTED in
   refresh.py (WARN with the Stage-A date every run; ESCALATES red past the deadline —
   guard-tested). **Diary: Stage A promotion ≤ 2026-08-15 UNCONDITIONAL** (cluster basis
   per PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR.md §6, else the DHT-print fallback §7;
   batch the DHT Jaguar coverage update — dht_log §7 entry); **Stage B window
   2026-08-26→09-04** band-gated ±10%; Rider 4 keeps a dailies/weeklies FFA/12M print
   promoting immediately at any time. Stage-A eyeball inventory incl. TRMD's
   post-re-tilt BUY (ruling ADDENDUM); any flip toward BUY = halt-and-investigate.
   **RESOLVED same evening — the Hormuz re-tilt RULING: RESTORE BOTH, EXECUTED @ fb00ede +
   ratify (owner verbatim: "all three are affected by hormuz, so should all move together
   coherently").** LNG v4 + product war shapes live; TRMD HOLD→BUY + STNG TRIM→HOLD
   (ruled-FV flips, eyeballed); ASC boundary did NOT fire (+4.0%); CCEC extends to +60% EV;
   the Jun-9→Jul-2→Jul-12 coherence gap is CLOSED — all three Hormuz sectors price one
   state again. Round-3 watch due Jul-22; the Jul-17 MoU check stays pro-forma.
-1. **ALL FOUR METHODOLOGY DECISIONS RULED 2026-07-15 (owner: "Proceed as recommended")
   — no longer pending; now executed or scheduled:** **D-M5 EXECUTED @ 41464fa** (fv_low/
   fv_high scenario-min/max interval in the Verdict + book_scorecard.json schema 2.4;
   drift-gate interval flip-triage LIVE: band-mech auto-classified inside the interval,
   band-EXIT keeps the eyeball — the Stage-A expected flips triage by rule). **D-M2
   Option B RULED, execution POST-STAGE-A** (per-sector asset r_a + relever by debt/NAV;
   sweep memo gates adoption; flat-r sensitivity column one quarter; B′ = container-refresh
   rider). **D-M3 prereg FROZEN** (`PRE_REGISTRATION_CYCLE_PARITY_DENOMINATOR.md`; A/B
   RUNS post-Stage-A; kill condition honest re newbuild_contract coverage). **D-M4 RULED
   piecewise-linear; open decision 9.1 CLOSED as ruled** (cycle.py note; adoption in ONE
   D1 round with D-M3's outcome ~late Aug; deltas eyeballed under the D-M5 rule).
   Sequencing principle: one FV-moving event in flight at a time — Stage A (≤ Aug-15)
   first, then D-M2 sweep, then the D1 round. Memo's mechanical items were already
   executed (M-1 attribution block; §2.3 provenance table); M-6a/b ride the next
   quarterly anchor refresh. **Thread-1A product-Handysize queue item CLOSED 2026-07-15**
   (owner "Execute"): age-0 re-sourced 36→44.9M on the ASC issuer-contract basis, xclusiv
   row renamed Handy-Bulk, zero live movement verified — decisions/
   product_handysize_resource_2026-07-15.md; the ASC Q2 NB entry books the ~+1.9%-NAV
   correction at the refresh, attributed there.
0. **RESOLVED 2026-07-13 — baseline ratify EXECUTED (owner: "accept all four + ratify").**
   The 14 UNEXPLAINED decomposed to three owner-traceable causes (Jul-12 war-tilt regen
   [owner-executed] + Jul-10→13 price vintage + the 13-Jul FFA promotion; ΔNAV 0.0% on every
   row). All four flips eyeballed INDIVIDUALLY: **BRUT** T/S→BUY +56.1pp = war-tilt FV-side,
   handoff already voids the read (PROVISIONAL, sign-unstable −63.4/+11.2, "not actionable") ·
   **CAPT** T/S→HOLD +24pp = pre-approved in the 7/12 doha_check table · **ASC** BUY→HOLD =
   shallow price-crossing (+7% tape; NOTE the staged product re-tilt [Jul-15 ruling] may flip
   it back — NEW eyeball then) · **GNK** HOLD→T/S = price-led pre-FFA + FFA deepening,
   sign-stable, tender-pinned (census Jul-24). STNG/GSL recross watch: quiet. Baseline
   re-ratified @ 1f6f2f2 (RATIFY_LOG 2026-07-13T17:30Z — pages the governance monitor);
   **drift gate 0 UNEXPLAINED, suite 569 fully green.**
1. **RESOLVED 2026-07-10 — committed-price re-ratify EXECUTED (owner: "accept both").** The 12
   EV%-only price-vintage drifts (ΔNAV 0.0% on every name) were accepted and the baseline
   re-ratified at the 2026-07-10T20:34 state (adds LPG/BWLP; `test_committed_baseline_covers_live_state`
   green). Both band flips were eyeballed INDIVIDUALLY per the don't-batch-accept rule and accepted
   as price-mechanical: **GSL BUY→HOLD** (shallow crossing, unheld, Q2 FV rebuild due — gsl_log
   2026-07-10) and **STNG HOLD→TRIM/SHORT** (accepted as a PRICE-POSITION ARTIFACT, NOT a short
   thesis — PROVISIONAL·off-curve/handoff-NO/⚠sign-flips + the known +$9.6/sh un-wired §9.6 leg;
   stng_log 2026-07-10). The k_broker +0.07 was the same price event seen through the pinned
   Jul-3 P/NAV. Watch item: if either name recrosses its boundary on a later vintage, that is a
   NEW eyeball, not noise.
1b. **RESOLVED 2026-07-10 — v1 lock ruling: OPTION (a), the WO3 letter (owner: "let's go with (a)").**
   The 0/2 lock miss (LPG −20.4% / BWLP −17.2%, consistent direction — txn-anchored curve vs
   Pareto's May-2026 raised quotes, k_broker ~1.2) is ACCEPTED AS DOCUMENTED: the sector holds
   **PROVISIONAL·v1-lock-miss** (`SECTOR_V1_UNLOCKED{"lpg"}`, handoff NO, consumer reads
   flag-don't-pass). **This closes WO3 Phase 5 on the "miss documented" branch of its
   definition-of-done — the charter's LPG half is DELIVERED** (honest validation surface: 2 names,
   SANITY-OK, weight-robust, PROVISIONAL — charter B-4 explicitly blesses this outcome). Re-run
   path REGISTERED: trigger `lpg_v1_lock_rerun` (due 2026-11-13, sentinel-paged) — trio per-vessel
   splits → §9.9 re-fit → re-run the lock → back to the owner; precedent context: dry bulk's v1
   lock was 1/2 FAIL-with-explanation (no cap, pre-WO3-letter), containers N/A-by-construction
   (GOVERNED-WIDE·structural-class cap). A rough re-fit sketch says the gaps land ~−15%/−12% —
   possibly STILL outside ±10% on the residual broker premium; if so, the GOVERNED-WIDE question
   returns WITH evidence as a logged amendment, not blind loosening. The BWLP
   **NCI-via-preferred_equity convention — RESOLVED 2026-07-13 (owner: "ratify with riders a
   and b")**: the $199.0M NAV-basis derivation ratified as wired (shown decision-neutral: book
   NCI would still miss the lock); rider (a) = curve↔NCI agreement guard `tests/test_bwlp_nci.py`
   (a VLGC re-fit now REDS until the YAML is re-derived — the Nov-13 lock re-run will trip it
   by design); rider (b) = the India strip-attribution leak (~10% of shipping EPS over-attributed
   to common, ≈+0.7% FV, offset by above-tier actual payouts) documented in LIMITATIONS.md §3.
   Record: bwlp_log 2026-07-13 entry.
2. **Owner install checklist — COMPLETE 2026-07-13** (residual cleared: uuid ping URL re-copied,
   sentinel **PING-SENT** 09:52 ET — the dead-man is ARMED; receipts seeded in
   decisions/wo2_acceptance_receipts.yaml; the three Phase-0 drills are owner-timed). (detail + fix log in
   `decisions/owner_install_checklist_2026-07-08.md`): all 8 launchd rows LIVE (D-2 CLOSED), email
   channel verified (test mail SENT after the agent scrubbed NBSPs from the pasted app password),
   GitHub secret set, governance healthcheck wired (next Fri monitor → PING-SENT). **RESIDUAL: the
   crude sentinel's ping URL is the wrong link type (HTTP 400, 4-segment path, not the plain
   uuid form) — owner re-copies it, then sentinel re-run for the PING-SENT receipt.** First live
   sentinel run 2026-07-12 exercised all check families; bonus catches: BWLP Oslo symbol fixed
   (BWLPG.OL, was 404) — feed 24/24; pareto_research 5-business-day silence flagged (see below).
3. **WO2 residue:** Phase-0 acceptance demonstrations + drill 2.5 UNBLOCKED once the ping URL
   residual clears; acceptance window Jul-28→Aug-6 (`close_acceptance.py` ready), task #32
   web-agent watchdog (interim single-threaded rule below).
3b. **Sentinel first-run finds (2026-07-12) — ALL THREE RESOLVED SAME NIGHT:** (i) the doha
   trigger check found the STRIKE leg had FIRED Jul-7/8 (3 vessels hit near Hormuz, US re-imposed
   the MoU-lifted sanctions + CENTCOM retaliation, threat 'severe') → **the pre-registered
   Jun-9-war-tilt restore EXECUTED at owner go 2026-07-12** (crude 0.25/0.45/0.18/0.12; test
   re-pins; decisions/doha_check_2026-07-12.md; follow-up trigger `crude_doha_round2_outcome` due
   Jul-15; NOTE the Jul-17 MoU check is largely pre-empted). **LNG/product NOT re-tilted — the
   trigger was crude-only; a Qatari LNG carrier was among the vessels hit, so the LNG-Hormuz
   re-tilt question (Jun-9 v4 shape) is FLAGGED as a new owner decision, not pre-registered.
   → PROPOSAL PREPARED 2026-07-13 (owner: "prep it"): decisions/hormuz_retilt_proposal_2026-07-13.md
   — restore shapes for BOTH remaining Jun-9 legs (LNG v4 + product war), scratch per-name deltas
   (STNG flips HOLD→BUY, TRMD +11.3% FV, CCEC extends to +66% EV; dry bulk/containers/LPG/crude
   untouched, no held name affected), test re-pin inventory, three-option decision cell. RULING
   STAGED for the round-2 outcome (trigger due Jul-15) — one coherent call, not churn.**
   (ii) pareto_research silence = SEASONAL (owner intel via RC: no daily printing Jul/Aug) —
   silence_days: 14 override until ~Sep-1; prices never depended on it (Yahoo feed 24/24 after
   the BWLPG.OL fix). (iii) the LPG/BWLP price jumps land in the post-reweight regen + ratify.

**STAGE-3 INTAKE (governance dry-bulk funnel, cycle closed 2026-07-13 — `../portfolio-governance/
funnels/drybulk_2026H2/stage2_verdicts_2026-07-13.md`): PREP LANDED 2026-07-14; onboarding proper
still owner-scheduled (competes with the Q2-refresh block).** What landed:
- **HKEX light-adapter (F-3) DELIVERED** — `hkex_poll.py` (edgar_poll invariants: politeness/quiet
  bootstrap/staging-only; arrivals land in `state/edgar_manifest.jsonl` with `source: "hkexnews"`,
  so sentinel FILING-LANDED + draft queue work unchanged), 8 tests incl. the stockId 7703 pin,
  rides the hourly edgar-poll launchd row; live-verified (bootstrap 56 filings, watermark
  2026-06-30 = the June Monthly Return). **2343's conditional Gate-D PASS is now unconditional**;
  governance register F-3 updated. Fetch mechanics in WORKFLOWS.md §Data-sources.
- **§9.9 Handy-curve decision RULED + EXECUTED 2026-07-14 (owner: Option B, verbatim in the
  decision doc) — the Handy-Bulk class is WIRED (§11.7.11), gate-neutral.** Record chain:
  `decisions/handy_curve_decision_2026-07-14.md` (ruling + a same-day CORRECTION: the "one
  archive print" was a PRODUCT-tanker pair — true dry-Handy Pareto-archive count is ZERO) →
  `handy_curve_sourcing_prereg_2026-07-14.md` (4-agent sweep `wf_bc3c20c5-68b`; nodes =
  xclusiv 2026-06-22 committed vintage [the BULK Handysize row], 5-broker corroboration ±4%,
  2343's own JNS contract $29.8M ≈ the $30.5M NB node; bands REGISTERED AND PASSED — the
  Dec-2025-vintage construction reproduces 2343's issuer-published Handy composite to +3.1%).
  Wired: Handy-Bulk curve (38k dwt-scaled, 36.0/29.5/23.3/4.5) + handy_bulk scenario deck
  (= supra_ultra × 0.90 LOCKED, identity guard-tested — re-derive BOTH on any supra promotion)
  + 12M TC 14.5k (MB DBW28, own cadence, NO FFA panel) + anchor 12.85k + BHSI spot + routing/
  sleeve/AGE0_BASIS(alias:Handysize)/basis_status + `tests/test_handy_bulk_class.py` (incl. a
  gate-neutrality test to DELETE at onboarding). **Re-fit path armed:** trigger
  `handy_bulk_txn_refit` (≥10 classified in-window prints, ≥3 age nodes incl. ≤6yr) — the MB
  Dry Bulk weekly runs ~3 sub-45k prints/week (22-print candidate table in prereg §4), so
  Option A may arm by the Q3 refresh; promotion is owner-run, never auto.
- **NEW OWNER QUEUE ITEM (flagged 2026-07-14, prereg §0.2 — NOT acted on):** Thread-1A wired
  the xclusiv BULK Handysize row ($36M) to the PRODUCT-tanker Handysize age-0 (ASC's actual
  product-Handy NB contract is $44.9M; the row's TC column is BHSI = bulk). Live NAV impact
  ≈ 0 today (age-0 touches 0-5yr only; no young product-Handy on the books; ASC's NBs are
  subsequent-event-excluded) but the product curve's basis label is wrong — needs its own
  attributable re-source ruling. Flags left in basis_status/newbuild_contract_prices/AGE0_BASIS.
- **Onboarding scaffolds:** data_sources.yaml entries ("2343" quoted-key + PANL; PANL CIK
  0001606909 VERIFIED vs company_tickers.json 2026-07-14, pinned in test_edgar_poll); earnings
  calendar seeds (PANL Q2 10-Q ~Aug-4/14, 2343 Interim ~Jul-27/Aug-14 — both UNVETTED estimates,
  inert for the sentinel until watchlisted, but they arm the pollers' in-window cadence); Pareto
  share-price table carries NEITHER name → both consensus pairs will be APPROX per §11.7.2
  (CMDB/SB precedent; re-verify on the newest daily at pair capture); PANL B3 IR-query DRAFT
  staged governance-side (`funnels/drybulk_2026H2/panl_b3_ir_query_draft.md` — owner sends).
- **2343 ONBOARDED 2026-07-14 (owner: "onboard 2343 before q2") — PROVISIONAL-at-birth read:
  GOVERNED-WIDE·pending-anchor · HOLD (EV −3.2% live) · SANITY −2.0% (n/a-APPROX,
  issuer-composite basis) · k_broker 1.03 · handoff-ready.** All four PRE-REGISTERED bands
  passed (decisions/2343_log.md — NAV/sh $0.39 vs band 0.36-0.44; no re-tuning). 25th name,
  first HKEX/HKD listing (yahoo_symbol 2343.HK enters the daily feed tonight; STATIC-FALLBACK
  flagged until then), first Handy-Bulk carrier (58 hulls = 51%; UNANCHORED_VALUE_CLASS_CAP
  holds the tier until handy_bulk_txn_refit). Snapshot = 31-Dec-2025 audited (semi-annual
  reporter — known one-quarter vintage lag vs the book, manifest header; next BS at the ~Aug
  Interim = the F-1 orderbook re-test + post-April NB conversion ingest). Carried-at-birth
  limits: 35-Supramax scrubber aggregate as documented conservative omission (~2.5% NAV,
  ECO-NB pattern, not queued); chartered-in book (13 LT + ~134 ST) excluded with full $82M
  operated-book G&A charged (CMDB/CBI convention); bareboat mini-cape rate unmodeled.
  **Baseline RATIFIED at owner go 2026-07-14T16:41Z** (RATIFY_LOG @ 0aa4fba; review page
  `decisions/ratify_review_2026-07-14.md`; cause: 2343 onboarding + the 7/14 price vintage —
  2343 `new` + 10 EV%-only rows all ΔNAV +0.0%, incl. two shallow price-band flips eyeballed
  individually: CMDB BUY→HOLD / SBLK BUY→HOLD, recross watches armed). **Suite fully green
  584 + 16 xfailed, drift 0 UNEXPLAINED; pushed.** External audit same day
  (`outputs/EXTERNAL_AUDIT_2026-07-14.md` — clean, nothing above P2; N-1..N-7 dispositioned,
  see CHANGELOG 2026-07-14 audit entry).
- **PANL: onboarding DEFERRED (owner 2026-07-14) — potentially after the Q2-refresh block.**
  Owner sends the B3 IR query (draft staged governance-side). When scheduled: four-YAML
  sourcing (subsequent-events-note-first; SSI-merger vessel cohort + Note-9 SLB structures +
  NBHC 2/3 VIE), §15 screen (SSI 29% bloc + F-2 wrapper watch), E2 breakeven completion at
  reconciliation, Handy sleeve (23.5% dwt) on the §11.7.11 curve, update the
  test_handy_bulk_routed_only_by_2343 pin deliberately.
  Timing note: 2343's Interim (~Aug) publishes the post-April commitments figure (governance F-1
  orderbook re-test) — onboarding off the AR2025 snapshot before it is legitimate (AS-OF
  discipline) but the F-1 re-test lands mid-reconciliation either way.

**NEXT BIG BLOCK — WO3 Phase 5 (the lock ruling — OWNER) + the Q2-refresh LPG carry-forwards.**
**Phase 4 LANDED 2026-07-10** (both validators onboarded + reconciled SANITY=OK; the two designed
reds at HEAD are the baseline-ratify + the committed-scorecard vintage — both resolve at owner
decision #1/#1b). Q2-refresh carry-forwards created by Phase 4: **Dorian** — Cobra LEAVES the
fleet (sold 5/6), the Corsair+2×2015 trio goes `held_for_sale` ($256M; per-vessel splits →
transactions/vlgc.yaml re-fit, the lock's re-run path), FQ1 report ~Jul-30/Aug-6; **BWLP** — the
8×90'cbm Panamax-VLGC order (~$940M, deliveries 2029→Q2-2030) goes §9.6 on-curve with its first
instalment, Q2 report ~Aug-25/28, NCI re-derivation if the curve moved, R-2 orderbook re-read
(order adds 8 hulls toward the 38% void bar). Phases 1-3 history: (Phase 1
2026-07-08: `sectors.lpg` + §9.10 family. Phase 2 2026-07-09: VLGC marks — §9.9 txn-ANCHORED, 9th
fitted class: 7 in-window prints, age-10 $80.3M strong / age-5 $92.3M extrapolated-FLAGGED-WIDE;
curve NB $117.5M NB-parity age-0 [AGE0_BASIS exception, basis_status pending-sourceable] / 5yr
$92M / 10yr $80M / age-25 $42M; record `decisions/vlgc_marks_2026-07-09.md`. Phase 3 2026-07-09:
`twelve_month_tc.VLGC` 63,615 REALIZED basis [ratified — never a TC numerator over the realized
anchor; cycle 1.59× war-elevated] + `ffa_forward_curve.VLGC` = absorption_base path under a
documented rule [war-spiked dailies NOT promoted] + standing trigger `vlgc_realized_tce_refresh`;
END-TO-END verified on a synthetic pure-VLGC name — no engine gaps left. **Pre-Phase-4 hardening
2026-07-09, owner review — all four findings closed:** age-5 WIDE flag machine-readable
[`MARK_WIDE_NODES` → `mark_wide_nodes` in the JSON, schema 2.3]; the synthetic e2e committed as
`tests/test_lpg_sector.py` incl. the ffa==absorption_base identity; realized-basis numerator pinned
[`rate_basis` stamp + basis-agreement test]; METHODOLOGY §11.10 written — pointers live).
**Phase 4 =
`/add-ticker` Dorian LPG (CIK 1596993) + BW LPG (CIK 1649313)** — CIKs **VERIFIED 2026-07-09**
against SEC company_tickers.json (LPG → 1596993 "DORIAN LPG LTD."; BWLP → 1649313 "BW LPG Ltd" —
exact match both, the FLNG/CCEC/INSW wrong-CIK class ruled out); per-vessel manifests with every NAV-moving
figure cited (figure-provenance rule; audit the subsequent-events note FIRST); balance sheets from
the latest filings (Dorian 10-K FY-end Mar-31; BWLP 20-F + Q1-2026); same-vintage consensus pairs
(Pareto prints BWLP 1.02 / LPG 1.01); §15 screen on the BW-Group bloc (no pre-assumed haircut).
Names land PROVISIONAL by definition until reconciled. Phase 5 lock: ≥70% of validators within
±10% of broker NAV at lock-time (2 validators ⇒ both, or document the miss and hold PROVISIONAL).
Kill-switches live: R-2 VLGC orderbook >38% voids the half; R-5 charter expires 2026-12-26.

**WO3 ISSUED 2026-07-06 — LPG/VLGC sector onboarding (charter-funded):** see `WO3_LPG_ONBOARDING.md`.
Consumer-side authority: portfolio-governance sector charter (verdict `fd0277f`) — 50% of the cycle's
validation labor; VLGC-first (Dorian LPG + BWLP validators); NOT a supply call (charter B-4); kill-switches:
VLGC orderbook >38% voids the half, charter expires 2026-12-26. Phase 0 (methodology decision doc) first.
**WO3 PHASE 1 LANDED 2026-07-08:** `sectors.lpg` in scenario_inputs.yaml (4 scenarios, LPG Set A
(US-export-arb) 0.15/0.35/0.35/0.15; VLGC 8q curves, PW front-4 $48.6k = 1.22× anchor, PW end-strip
$34.3k below mean — overhang tilt priced); anchor $40k realized-TCE `as_of 2026-07-07` under NEW basis
token `realized_tce_10yr_mean` (4th basis, MIXED-ANCHOR-BASIS-tripping, pinned by
`test_lpg_realized_tce_basis_does_not_compose_with_tc_means`); routing wired (VLGC→vlgc, VLGC-only);
§9.10 family from birth (`scripts/lpg_weight_comparison.py`, Set B arb-bull / Set C deep-overhang
brackets; sidecar block registered, names populate at Phase 4); locks
`test_lpg_locked_weights_and_anchor`. Gate-neutral (zero LPG names; delta 0 material; drift gate 0
UNEXPLAINED). **Also fixed en route:** the sidecar merge's pre-namespacing whitelist would have wiped
all other families' weight_sets on the first post-WO4 merge (scorecard.py; now key-shape detection +
`test_sidecar_merge_preserves_all_other_families`); all four legacy families re-stamped against the new
scenario_inputs sha — no `ev_sign_stable`/position changes. The verification pipeline run surfaced the
KNOWN pending-decision-#1 price drift as 4 EV%-only gate rows (CAPT/CMDB/GSL/MPCC) — ANNOTATED as
explain-not-accept in their logs; re-ratify + the GSL band call stay with the owner.

**WO4 ISSUED 2026-07-07 — dry-bulk weight-robustness family (§9.10) extension (charter-funded):** see
`WO4_DRYBULK_WEIGHT_FAMILY.md`. Consumer-side authority: same charter (verdict `fd0277f`) — the dry-bulk
deepening half; unblocks the consumer's Gate E (drybulk rubric commit `f54e797`), whose "sign-flip at desk
depth = FAIL" reads `weight_sign_stable`. Write `scripts/dry_bulk_weight_comparison.py` (mirror crude) +
a `test_dry_bulk_locked_weights` pin; the scorecard seam already emits the family fields — dry bulk is null
only for lack of a sidecar entry. DIAGNOSTIC ONLY: Bulk Set A stays locked; §11.7.10 dwt-scaling /
Post-Panamax / FFA-OCR are frozen. Kill-switches: dry-bulk orderbook >16% voids the half, charter expires 2026-12-26.
**WO4 LANDED 2026-07-07** (`scripts/dry_bulk_weight_comparison.py` + `test_dry_bulk_locked_weights_position`):
sidecar `outputs/weight_robustness.yaml` carries a current-SHA dry_bulk block (SBLK/GNK/CMDB/SB
`ev_sign_stable` all True) — the field Gate E reads; seam emits it to `book_scorecard.json` on regen.
Findings: SB/CMDB weight-robust BUY; SBLK sign-stable-positive but label position-driven (BUY→HOLD at the
property-drag bracket); GNK sign-stable-negative. Bulk Set A byte-locked, gate-neutral. **Standing thread
made concrete:** the WO4 regen surfaced pre-existing committed-price drift (FVs byte-identical; only EV%
denominators moved vs the Jul-6 book — CMDB EV +6.0pp, **GSL band BUY→HOLD**) — the overdue daily
price-refresh re-ratify, deliberately NOT bundled into WO4; needs its own owner-aware re-ratify (GSL flip
is position-relevant).

**Follow-ups from the 2026-07-02 review chain (non-blocking):** (1) drift-gate CLI needs
`state/last_run.json` — add a from-inputs recompute mode so a clean clone can run the gate
(clean-clone verifiability is an audit-noted strength); (2) tanker forward curves held at the
Jun-7 vintage pending a market print (trigger `tanker_forward_print_lands`; scorecard Rate-basis
header discloses); (3) LNG comparison script shares the missing-anchoring pattern (harmless —
no LNGC txn fits — but align it when next touched); (4) the drift gate's
`decision_log_annotated_since` matches only the literal `**Decision:**` prefix
(drift_gate.py:203) — dated prefixes like `**Decision (2026-07-02, …):**` are invisible to
it (caught at the vintage re-pin, 2026-07-02); widen the matcher + add a test.

**WO2 BOARD — web-research agent watchdog failure (owner-flagged 2026-07-07, NOW A KNOWN FAILURE MODE,
3× occurrences):** parallel web-heavy source agents (WebSearch/WebFetch fleets) have stalled on the
stream watchdog three times — the standalone VLGC sourcing agent, then the 3-agent VLGC-anchor
workflow (both source phases), each salvageable by hand from the frozen jsonl but costing a manual
synthesis pass every time. This is producer-tooling debt, not an incident: the fetchers (price/RC/
harvester/edgar) get FETCH-FAILED-class heartbeat-and-restart, but the RESEARCH agents don't. Fix =
give web-research sweeps the same watchdog-and-auto-restart, OR a hard rule that source sweeps run
SINGLE-THREADED (one web agent at a time, no parallel() fleets of fetch-heavy agents). **INTERIM RULE
adopted 2026-07-07 until the fix lands: no parallel() fleets of web-fetch-heavy agents — run source
sweeps single-threaded, or accept the salvage tax knowingly.** "Salvageable by hand each time" is
exactly the load-bearing manual step the automation push exists to retire.

**The P0 reconciliation queue (`NAV_FIGURE_ESTIMATE_QUEUE ∩ PROVISIONAL`) is CLEARED —
EIGHT names done: NAT/SB/ASC/BRUT/ECO/HAFN/STNG/TRMD.** EIGHT P0 names worked this arc: **NAT DE-VOIDED** (2026-06-30, NAV $2.07→$2.79,
GOVERNED-WIDE·newbuild-indeterminate), **SB corrected** (date-mix + CAPT blanket-scrubber bug; NAV
$10.47→$10.12, ~0.63×), **ASC reconciled** (April-2026 newbuild wrongly loaded as a −$88.8M Q1
commitment [subsequent event] + phantom `Ardmore_Patriot` removed + chem-Handies → cited 20-F
carrying-value floor; NAV $15.96→$17.80, PROVISIONAL → GOVERNED-WIDE, BUY +5.2%), and **BRUT traced**
(2026-07-01 — a DIFFERENT outcome: the reconciliation VALIDATES the model [commitment $1,373.1M ≈ Pareto
$1,370M; debt $0; shares 61.9M all now issuer-traced] but BRUT STAYS PROVISIONAL — cash booked at a $66M
conservative floor keeps it flagged `cash-pending-H1-report`; also fixed a fabricated governance block +
flagged going-concern doubt; NAV $9.40→$8.80; NOT actionable — going-concern-doubtful, max-torque), and
**ECO cleared to VALIDATED-TIGHT** (2026-07-01 — the first TIGHT of the arc; figures all verified vs the
Q1-2026 6-K, the 2 Suezmax NBs wired on-curve §9.6 + 16 scrubbers verified; the value-flag guard caught a
peer-default and the NBs were booked scrubber=false; NAV $34.56→$34.35 [sub-threshold]. But ECO is
validated-but-RICH [rich · cycle position, ~1.39× NAV] — NOT a new long), and **HAFN reconciled**
(2026-07-01 — the most consequential: an ASC-pattern 3-Apr-2026 subsequent-event newbuild removed [+$365M],
debt/lease corrected to the Note-2/4 split [−$46M], the TORM stake to Hafnia's own lower-of-cost NAV basis
[−$118M; precedent: marketable stakes take the issuer's method], and operating WC held at a conservative
pool-gross-up floor [precedent: pool receivables are custodial, not NAV-economic]; NAV $5.22→$5.57, stays
PROVISIONAL·pool-gross-up-pending, rich · cycle position — NOT actionable; price-refresh isolated out), and
**STNG reconciled** (2026-07-01 — the most TANGLED: two large errors pointing OPPOSITE ways that nearly
cancelled, so the model reported a plausible-but-wrong NAV. `total_debt` $789.1M DOUBLE-COUNTED the $200M
2030 notes [→$589.1M, +$200M]; the $395M held-for-sale line double-counted 6 operating-manifest MRs AND
listed the wrong hulls [→ real March 8-vessel agreement $305M, fleet MR 41→35 / on-curve 87→81, −$280M];
plus opWC $207.8M→$163.3M [omitted accrued] and NB advances $90M[est]→$69.069M. NAV $83.87→$80.97 base /
$80.35→$77.47 headline, BUY→HOLD; leaves `NAV_FIGURE_ESTIMATE_QUEUE`, stays PROVISIONAL·off-curve. FLAGGED
separately: the 10-vessel NB [incl. 2 VLCC — first crude exposure] off-curve carries a −$504M commitment
drag; §9.6 on-curve wiring would add ~+$481M NAV [~+$9.6/sh] — a cross-sector methodology decision, deferred),
and **TRMD reconciled** (2026-07-02 — the estimate-heaviest name [six `[ESTIMATE]` figures] and the FIRST of
the arc to move NAV materially UP. Two errors SUPPRESSED NAV: `newbuild_capex_commitments` $360M→$31.2M [the
$360M bundled 6 MR resales bought AFTER quarter-end — the ASC/HAFN subsequent-event pattern a THIRD time; only
the 2 Q1 resales remain], and `working_capital_net` $110M[est]→$254.9M [sourced: $249.6M trade rec + $82.5M
bunker inv]. Plus debt $1,089.6M→$1,081.8M, leases $5M→$0 [SLB bought out], advances $50M→$0 on-curve. All
6-K-verified by an 8-agent workflow. Owner forks [all completeness]: WC operating $254.9M; the 2 MR resales
wired ON-CURVE §9.6 [in-sector, clean — leaves `OFF_CONVENTION_QUEUE`]; scrubbers corrected to the disclosed
85 [FY2025 20-F — leaves `OPERATING_SCRUBBER_QUEUE`, `{TRMD:85}`]. NAV $26.74→$31.65 base / $25.43→$30.34
headline, HOLD→BUY +17-22%; k_broker 1.17→1.03 [TIGHTEST spread in the book; headline ≈ TORM's own NAV $29.7].
→ GOVERNED-WIDE·basis-pending [product nav_basis pending-sourceable, not TIGHT]. **This CLEARS the P0 queue.**).
CLAUDE.md was also restructured to a lean ~3.8k-token router with a build-enforced size cap. These
hardened **provenance + handoff + hygiene**, not the thesis — SB stays cheap on every version of its numbers.

**THE consolidated handoff output is `outputs/book_scorecard.md`** (2026-06-30). One file,
two sections: a **Verdict** table on top (per name: confidence tier · FV vs current price ·
upside · position · NAV/sh · broker NAV · gap · SANITY · handoff-ready) and the **Validation
matrix** (per-gate detail) below. This is the single surface a downstream sizing decision
reads — it replaces hand-joining three sources (scorecard / reconcile / decision logs). The
Verdict's price/NAV/position come from the **scenario whole-company spine** (so hybrids INSW
/ CMBT show the whole, not a sleeve — regression-tested); the single-point FV from the
CompanyReport. Generated by the pipeline (`run_scorecard_xref` with the in-scope reports).

Three owner-directed label corrections make the verdict un-misreadable (verified per name +
adversarially, registered in `provenance.py`): (1) a **cycle-rich position is relabeled** away
from "TRIM/SHORT" to "rich · cycle position (not a short)" — a NAV-relative §12 read is not a
trade signal (crude AND product near peak; MPCC → "unreliable read"); **all 8 of the book's
TRIM/SHORT positions are cycle/unreliable/void — not one is a name-specific short**; (2) the
tier cell carries a **sub-reason = resolution path** (`structural-class` / `newbuild-heavy` /
`pending-anchor` / `mixed` / `read-flips` / `void` / `uncited-figure` / `off-curve`) so
GOVERNED-WIDE / PROVISIONAL aren't junk drawers; (3) NAT's derived NAV + gap WERE voided (they
rested on the contradicted $17M-advance figure) — **NAT was DE-VOIDED 2026-06-30** by the P0
reconciliation (advance sourced to $0, whole balance sheet re-sourced); the void-rendering path is
retained as coverage for the next contradicted-figure name (`NAV_DERIVED_VOID` now empty). The verdict header states the **opportunity-set finding**:
of 22 names the validated-actionable-long surface is **2 (SB, SBLK)** — the tool refusing to
manufacture conviction, not a gap.

The xfail-strict guard queues ARE the visible work queue — `provenance.py` is their single
source of truth (imported by both the guards and the tier, so they can't drift):
1. **§9.6 newbuild on-curve convention** (`test_newbuild_convention`) — newbuilds valued at
   delivered-market PV − remaining commitment, advances→0. SB/SBLK/DHT/CAPT are on-curve;
   `OFF_CONVENTION_QUEUE` (CMBT/STNG/TEN — 3; NAT parked, ASC+HAFN April-2026 subsequent-event NBs,
   ECO/TRMD on-curve via years_to_delivery [ECO 2 Suezmax NBs; TRMD 2 MR resales 2026-07-02]) is the
   remaining xfail-strict queue. CCEC/CMBT are STRUCTURAL (Group-B, commitment-net not on-curve).
2. **Operating-scrubber provenance gradient** (`test_scrubber_provenance`) — contradicted→hard-
   fail; untraced-newbuild→hard-fail; untraced-operating→xfail-strict. `OPERATING_SCRUBBER_VERIFIED
   = {CAPT:5, SB:20, ECO:16, TRMD:85}` (TRMD → FY2025 20-F "installed scrubbers on 85 of our vessels"
   = all 22 LR2 + all 63 MR, 2026-07-02); `OPERATING_SCRUBBER_QUEUE` = 8 names.
3. **NAV-figure provenance** (`test_manifest_provenance`) — field-GENERAL: any figure in the NAV
   equation (debt/cash/leases/commitment/advances/preferred/shuttle/working-capital) that rests
   on an estimate marker (a tilde, `[ESTIMATE]`, `approx`) without a citation is a red. Plus the
   claims half: a `(confirmed)`/`verified` assertion must cite a source. `NAV_FIGURE_ESTIMATE_QUEUE`
   = brut/cmbt/flng/hafn (4; nat/asc/stng left; trmd left 2026-07-02; **ten left 2026-07-15 — FULL
   reconciliation vs the Q1-2026 6-K condensed BS + FY2025 20-F, pre-registered bands HIT [headline
   $88.76→$87.35 vs predicted $87.34]: advances $442.74M cited, WC composite $174.65M, debt $2,136.1M,
   +$45.95M Mare Success NCI netted, 4 not-owned hulls out of the manifest [Ulysses HFS + 3 true-sale
   SLBs — Arctic/Antarctic re-add owned at H1]; decisions/ten_reconciliation_prereg_2026-07-15.md;
   **four §6 forks RULED + baseline RE-RATIFIED 2026-07-15 (owner: "proceed as recommended.
   TEN-only baseline ratify." — RATIFY_LOG @ 6145378, zero number movement; H1 revisits:
   Ulysses gain/cash · Arctic/Antarctic re-add · WC components) — the TEN recon arc is CLOSED**). The P0 reconciliation queue [figure-queue ∩ PROVISIONAL]
   is CLEARED: brut + hafn were reconciled but stay in the figure-queue via a DELIBERATE conservative
   `[ESTIMATE]` floor (brut cash-pending, hafn pool-gross-up); cmbt/flng are structural/not-yet-worked.
   "Present but uncited" fails like "absent".

**Confidence tier (governance handoff, `provenance.confidence_tier`)** — read from the existing
validation state, NOT a new model: **VALIDATED-TIGHT** (5: DHT, FRO, SB, SBLK, **ECO** — TNK LEFT 2026-07-31 at its Q2 refresh → GOVERNED-WIDE·read-flips, label fragility at fair value, figures all trace — traced +
robust two-basis; ECO cleared 2026-07-01 via the §9.6 on-curve fix + scrubber verification, but is
validated-but-RICH [rich · cycle position], NOT a new long), **GOVERNED-WIDE** (13 — traces but
structural-unavailable input, read flips, or newbuild parked/absent: **NAT** `newbuild-indeterminate`;
**ASC** `structural-class`; **TRMD** `basis-pending` — cleared 2026-07-02, all figures sourced + all 3 queues
cleared, but product nav_basis is `pending-sourceable` [**LR1 the LAST non-uniform class** after the
2026-07-15 MR clear — **LR1 RULED 2026-07-15: contract-floor + resale-corroborated; TRMD →
VALIDATED-TIGHT scheduled at the post-Stage-A anchor round** (`PRE_REGISTRATION_LR1_CONTRACT_FLOOR.md`,
boundary checkpoints registered)], so GOVERNED-WIDE not TIGHT until that round; BUY, k_broker 1.03 —
the tightest tool↔broker spread in the book), **PROVISIONAL**
(3: **STNG** `off-curve` — all figures now sourced to the Q1-2026 6-K [2026-07-01 rebuild], but the 10-vessel
NB stays off the §9.6 curve; + **BRUT** `cash-pending` — 4/5 issuer-traced, cash flagged pending the H1-2026
report; + **HAFN** `pool-gross-up-pending` — all figures sourced/decided except operating WC, held at a
conservative floor because pool custodial receivables can't be netted from the filing; **NOT handoff-ready,
flag don't pass**). APPROX-pnav does NOT demote a robust name
(SB's two-basis corroboration substitutes for the missing broker check); an immaterial uncited
operating-scrubber surface does not either (materiality-gated at 10% of NAV). Emitted in the
scorecard Verdict + the `/add-ticker` handoff (a PROVISIONAL name may not hand off a governed FV).

**A NEW AGENT: read CLAUDE.md, then this file.** The **reconciliation queue** (below) that was the lead
thread — clearing PROVISIONAL names to handoff-ready — is now **CLEARED (2026-07-02: all EIGHT done,
NAT+SB+ASC+BRUT+ECO+HAFN+STNG+TRMD).** The next open work is the remaining `OFF_CONVENTION_QUEUE`
(CMBT / STNG's 10-hull NB [thread-(d) gate CLEARED 2026-07-15, wiring queues post-Stage-A] / TEN) onto
the §9.6 curve, and the **P1 product-basis thread (P1c)** — **2026-07-15 state: MR CLEARED to
resale-uniform** (xclusiv resumed the MR2 line 07-13; TEN +0.07% the sole move, 0 unexplained —
`decisions/mr_secondhand_resumption_2026-07-15.md`), and **LR1 RULED the same evening** (owner:
"taxonomy (b) + contract-floor, post-Stage-A") — execution prereg FROZEN
(`PRE_REGISTRATION_LR1_CONTRACT_FLOOR.md`): **TRMD → VALIDATED-TIGHT is now SCHEDULED WORK at the
post-Stage-A anchor round** (with the extract-refresh rider; INSW +$7.80M / TEN +$1.17M predicted,
TRMD+HAFN exact-zero controls); Handysize/Handymax stay structurally uncovered (no broker line —
07-15 sweep re-confirmed; neither qualifies for the new scoped `resale-corroborated` status).
Per-change chronology in `CHANGELOG.md`; per-name detail in `decisions/<t>_log.md`.

## Recent arc — convention + provenance + handoff + hygiene (2026-06-29 → 07-01)

- **§9.6 newbuild convention standardized** (SB/SBLK first, then DHT/CAPT) — newbuilds were
  inconsistently valued book-wide; the 3-clause guard + per-name pre-registered sourcing put the
  worked names on-curve and made the rest a visible xfail-strict queue.
- **Provenance turned from attention-dependent to ENFORCED.** Four catches (xclusiv resale mislabel
  → crude age-0 → DHT scrubber `(confirmed)` → NAT newbuild figure the cash flow contradicts) →
  the field-GENERAL guard: any NAV-moving manifest field must trace to a citation; a tilde/`[ESTIMATE]`
  is a red. Two more instances landed on the SB audit (below), both now guarded.
- **NAT reconciled + DE-VOIDED** (2026-06-30) — advance $17M→$0 (contradicted), newbuild parked at
  $0 (undisclosed price), fleet 18→16 + a `held_for_sale` field; NAV $2.07→$2.79,
  GOVERNED-WIDE·newbuild-indeterminate. (Was HALTED-as-VOID; the reconciliation cleared it.)
- **SB corrected** (2026-07-01) — an audit of the headline actionable name found a date-mix (the
  manifest was the June-12 fleet on the 3/31 balance sheet: Katerina double-counted, Michalis H the
  one HFS, Xenia/Ped.Commander mis-bucketed) AND the CAPT blanket-scrubber bug (29 flagged vs 20
  disclosed). NAV $10.47→$10.12 (still ~0.63×); scrubber set traced to the 20-F → cleared to
  OPERATING_SCRUBBER_VERIFIED. Two new CLAUDE.md rules + the post-mortem in CHANGELOG.
- **CLAUDE.md restructured to a lean router** (2026-07-01, 357→189 lines / ~6.2k→~3.8k tokens) —
  gotchas compressed to one-liners, runbook/fetch-mechanics/week-close migrated to WORKFLOWS.md;
  the compounding-knowledge habit made self-limiting with a build-enforced size cap
  (`tests/test_docs_stay_lean.py`). Verified lossless by an independent audit.
- **Confidence tier + consolidated Verdict output** — the handoff surface above.

## Open threads (prioritized — start here)

**P0 — reconciliation queue: clear PROVISIONAL → handoff-ready (owner-directed, START HERE).**
The PROVISIONAL names each carry a NAV-driving figure that is uncited or off the §9.6 curve;
each clears ONLY by sourcing the figure to a citation in a **full balance-sheet reconciliation**
(newbuild commitment + debt + cash + working capital), NOT a single-figure plug. Discipline:
pre-register the predicted bands AHEAD, commit, then recompute; halt on a miss and investigate
the INPUT; never source mid-recompute.
   - **NAT — DONE (2026-06-30).** Full reconciliation vs the FY2025 20-F (acc 0001140361-26-017809)
     + Q1-2026 6-K (acc 0000919574-26-003779): advance $17M→$0 (contradicted); commitment PARKED at
     $0 (firm price undisclosed by NAT — only a Pareto LOI; §9.6 on-curve unauthorized); operating
     fleet 18→16 + a new `held_for_sale` field ($65M contracted). NAV $2.07→$2.79, de-voided,
     GOVERNED-WIDE·newbuild-indeterminate. Reusable pattern: `held_for_sale` model field +
     `NEWBUILD_PRICE_PENDING` (park-at-$0-pending-filed-price → GOVERNED-WIDE not TIGHT). Record:
     `decisions/nat_reconciliation_prereg_2026-06-30.md` (commits df2c616 pre-reg, b44c3c4 fix).
   - **ASC — DONE (2026-07-01).** Full reconciliation vs the Q1-2026 6-K (acc 0001104659-26-056715),
     FY2025 20-F (acc 0001104659-26-024690), 2013 order 6-K (acc 0000919574-13-005339): the 2×40,500 DWT
     Handysize newbuild EXCLUDED from Q1 (signed **April-2026** = subsequent event; was a −$88.8M
     commitment-only drag + §9.6 violation); phantom `Ardmore_Patriot` removed (0 mentions in 6-K/20-F);
     4 chem-Handies re-marked to a cited **20-F carrying-value floor** (~$18.3M/hull); HFS Engineer →
     `held_for_sale` field ($35.5M). NAV $15.96→$17.80, PROVISIONAL → GOVERNED-WIDE·structural-class,
     BUY +5.2% but §12 cycle-position. Newbuild to go on-curve in Q2 (§9.6, issuer $44.9M/ship). Record:
     `decisions/asc_reconciliation_prereg_2026-07-01.md` (commits 48b3956 recon, cfc904e re-ratify).
     LESSON (owner): **audit the subsequent-events note FIRST** — it's where post-quarter events leak
     into a Q1 snapshot (ASC's newbuild; the SB fleet-table version).
   - **BRUT — DONE (2026-07-01), a DIFFERENT outcome: the reconciliation VALIDATES the model, and BRUT
     stays PROVISIONAL (does NOT clear).** Workflow-sourced (9 agents) to the FY2025 Annual Report
     (`inputs/research_issuer/2025_brut_annual_report.pdf`) + the Euronext admission doc. The Pareto
     estimates were ACCURATE: commitment $1,373.1M (Note 10 $661.7M + Note 15 Jan $236.0M + CIMC $499.0M
     − $23.6M) ≈ prior $1,370M; debt $0; shares 61,923,808 — 4 figures now TRACE to the issuer. Cash
     booked at the **$66M conservative FLOOR** (owner: not the $116M point, not Pareto's $100M; the
     Mar-2026 CIMC ~$50M execution deposit likely hit Q1) → NAV $9.40→$8.80. **Cash keeps BRUT
     PROVISIONAL** — new sub-reason **`cash-pending-H1-report`** (a WAITING state, resolves at H1-2026
     2026-08-13; re-ratify AGAIN then). Also fixed a **FABRICATED governance** block (no Goodwood/Koch;
     managers 2020 Bulkers+Himalaya, Trøim-sponsored, Magni zero-fee) + recorded the **going-concern
     doubt** as the §15/risk headline. NOT actionable (going-concern-doubtful, max-torque, resale-level-
     provisional). Record: `decisions/brut_reconciliation_prereg_2026-07-01.md`. Baseline re-ratify
     (BRUT-only) pending — owner. **NEW PATTERN: a reconciliation can VALIDATE + still not clear** (sourced
     except one figure with a known resolution date → `cash-pending`, distinct from `void`/`uncited`).
   - **ECO — DONE (2026-07-01), → VALIDATED-TIGHT (first TIGHT of the arc), the CLEANEST (no forks).**
     ECO (Okeanis) was PROVISIONAL only on `OFF_CONVENTION` (2 Suezmax NBs at delivered market with no
     `years_to_delivery`). ALL figures verified vs the Q1-2026 6-K (acc 0001104659-26-060273): debt $683.1M
     (incl. SLB), cash $176.5M, advances $39.74M → commitment $158.86M, NBs $99.3M each (Tigani May-26, Vous
     Jul-26), shares 39,044,655, 8 VLCC + 8 Suezmax (no phantoms). FIX: split the NB row + set years_to_delivery
     (0.12 / 0.29) → on-curve, leaves `OFF_CONVENTION_QUEUE`; verified 16 on-water scrubbers → leaves
     `OPERATING_SCRUBBER_QUEUE` (`{ECO:16}`). PROVENANCE CATCH: the value-flag guard blocked defaulting
     scrubber=true on the NBs (6-Ks' scrubber statements are existing-fleet-scoped — the SB trap), so the NBs are
     booked **scrubber=false** (conservative, `newbuild_specs.yaml`). NAV $34.56→$34.35 (−0.6%, sub-threshold —
     gate stable, no re-ratify needed). Record: `decisions/eco_reconciliation_prereg_2026-07-01.md`. **ECO is
     validated-but-RICH (rich · cycle position, ~1.39× NAV) — NOT a new actionable long.**
   - **HAFN — DONE (2026-07-01), the MOST consequential (multiple errors + genuine forks); stays PROVISIONAL.**
     Workflow-sourced (12 agents) + independent read vs the Q1-2026 6-K (acc 0001140361-26-022910). Recurring
     theme: **balance-sheet-literal ≠ NAV-economic**, three times. (1) The 8 MR HHI newbuild EXCLUDED from Q1 —
     signed **3-Apr-2026** (Note 7 subsequent event) → the −$405M commitment + $40M phantom advance was the ASC
     double-anachronism (+$365M; HAFN leaves `OFF_CONVENTION_QUEUE`). (2) `total_debt` $943.5M→$953.9M (Note 2/4
     bank borrowings) + `lease_liabilities` $35.9M→$71.6M (model dropped the $35.7M SLB) (−$46M). (3) TORM 13.97%
     stake → **$277.2M lower-of-cost** (Hafnia's OWN NAV method, comparability to its $8.09 NAV — NOT $395M market;
     **precedent: a marketable stake in NAV takes the issuer's disclosed method, not fair value**). (4) operating
     WC — the gross balance-sheet $335.9M carries **pool custodial gross-up** (Hafnia runs the world's largest
     product pool; the $670M receivables aren't NAV-economic); booked at a conservative **$85.7M floor** →
     `pool-gross-up-pending` (**precedent: pool receivables are custodial, not NAV-economic**). (5) shares → 505.3M.
     NAV $5.22→$5.57 headline; SANITY OK. Incidental daily price-refresh (5 names, EV-only) REVERTED to isolate the
     commit. HAFN stays PROVISIONAL·pool-gross-up-pending, rich · cycle position — NOT actionable. Record:
     `decisions/hafn_reconciliation_prereg_2026-07-01.md`. Baseline re-ratify (HAFN-only) pending — owner.
   - **STNG — DONE (2026-07-01), the MOST TANGLED (two large offsetting errors); leaves the figure queue,
     stays PROVISIONAL·off-curve.** Owner-directed FULL per-vessel rebuild vs the Q1-2026 6-K (acc
     0001483934-26-000042). Two errors pointing OPPOSITE ways nearly cancelled, so a half-fix would report a
     wildly wrong intermediate: (1) `total_debt` $789.1M **double-counted the $200M 2030 notes** — STNG's own
     "Gross debt outstanding 3/31 $589,056K" (bank $389.1M + notes $200M; ties to net cash $395.3M) → $589.1M
     (+$200M). (2) The $395M held-for-sale line **double-counted 6 operating-manifest MRs AND listed wrong hulls**
     (it counted operating LR2s Broadway/Condotti/Winnie/Lauren + the Q1-CLOSED STI Lavender); the real 3/31 HFS
     is the March 8-vessel agreement **$305M** (Solidarity LR2 + 7 MRs; $215M carrying). Removed the 6 double-counted
     MRs from the fleet (**MR 41→35, on-curve 87→81**) + re-booked HFS via a new `held_for_sale` field (−$280M net).
     Also: opWC $207.8M→**$163.3M** (omitted $44.6M accrued), NB advances $90M[est]→**$69.069M** (BS "Vessels under
     construction"), cash $984.321M, shares 50,025,865, leases 0 — all 6-K-verified. **NAV $83.87→$80.97 base /
     $80.35→$77.47 headline, BUY→HOLD** (in the pre-reg band); SANITY OK (−28.3% to broker $108, documented spread).
     STNG **leaves `NAV_FIGURE_ESTIMATE_QUEUE`** (advances sourced) but **stays `OFF_CONVENTION_QUEUE` →
     PROVISIONAL·off-curve**. Record: `decisions/stng_reconciliation_prereg_2026-07-01.md`.
     **§9.6 NEWBUILD — DEFERRED as its own pre-registered step (owner decision 2026-07-01), NOT wired with the
     rebuild.** The 10-vessel NB (2 MR + 4 LR2 + **2 VLCC**) off-curve is a −$504M commitment drag; full on-curve
     wiring would add **~+$481M NAV (~+$9.6/sh → base ~$90.6)** and flip the read toward BUY. Deferred because it is
     a reconciliation-sized methodology move, not a flag-flip, and it must NOT be bundled with a data correction
     (attributable-step discipline) or import unresolved crude-level uncertainty onto a product name:
       · **The 2 VLCC portion is BLOCKED on thread (d)** — STNG's VLCCs would mark on the CRUDE age-0 curve, whose
         RESALE-basis level is itself provisional (thread (d), `curve.newbuild` basis inconsistency). Wiring them now
         imports that quarantined crude-level uncertainty onto STNG's clean product NAV. **Thread (d) now gates the
         VLCC portion of STNG too — not just the crude names / BRUT.**
       · **Likely future structure (pre-register separately):** wire the **6 product hulls (2 MR + 4 LR2) on-curve**
         (within-sector, settled product curve; ~+$7/sh) and **park the 2 VLCCs off-curve pending thread (d)**.
         Source per-hull delivered marks + the delivery schedule, predict bands AHEAD, gate the move as its OWN
         attributable re-ratify (a +$7–9.6/sh headline move cannot be a footnote).
       · **Classification:** even fully wired at ~$90.6 (a deep nominal BUY vs price $75.60), the cheapness would rest
         partly on the provisional VLCC resale mark → **GOVERNED-WIDE at best, not TIGHT**. So the §9.6 wiring does
         NOT manufacture a clean tight long either — same arc finding. Baseline re-ratify (STNG-only) pending — owner.
   - **TRMD — DONE (2026-07-02), the estimate-heaviest name + the FIRST of the arc to move NAV materially UP;
     leaves ALL THREE queues → GOVERNED-WIDE·basis-pending, handoff-ready BUY.** Full balance-sheet sourcing to
     the Q1-2026 6-K (acc 0000919574-26-003082), independently confirmed by an 8-agent verification workflow (5
     extractors + 3 adversarial verifiers, all verdicts agree). Two errors SUPPRESSED NAV: (1)
     `newbuild_capex_commitments` $360M→**$31.2M** (Note 10 "Second-hand vessels commitments") — the $360M bundled
     the **6 MR resales bought "after the end of the quarter"** (subsequent event, the ASC/HAFN pattern a THIRD
     time); only the 2 Q1-agreed resales (Dehradun/Dapitan) remain. (2) `working_capital_net` $110M[est]→**$254.9M**
     (sourced: $249.6M trade rec + $82.5M bunker inv at a record-rate quarter-end). Also debt $1,089.6M→$1,081.8M,
     leases $5M→$0 (SLB bought out — the $10M ROU is inside borrowings), advances $50M→$0 (on-curve). **Owner forks
     (all completeness, 2026-07-02):** WC operating $254.9M; the **2 MR resales wired ON-CURVE §9.6** (age-11 MRs,
     years_to_delivery 0.12 — in-sector, near-immediate, no cross-sector blocker unlike STNG → leaves
     `OFF_CONVENTION_QUEUE`); scrubbers corrected to the disclosed **85** (FY2025 20-F "installed scrubbers on 85 of
     our vessels" = all 22 LR2 + all 63 MR → leaves `OPERATING_SCRUBBER_QUEUE`, `{TRMD:85}`; the 2 resale hulls
     scrubber=FALSE, no NB statement). NAV $26.74→**$31.65** base / $25.43→**$30.34** headline (in the pre-reg band);
     HOLD→**BUY** +17-22%; **k_broker 1.17→1.03** — the TIGHTEST tool↔broker spread in the book (headline ≈ TORM's
     OWN disclosed NAV $29.7 — a triple corroboration). → **GOVERNED-WIDE·basis-pending** (NOT TIGHT: product
     nav_basis `pending-sourceable`, thread P1c — a book-wide product limitation, not TRMD-specific). Record:
     `decisions/trmd_reconciliation_prereg_2026-07-01.md`. Baseline re-ratify (TRMD-only) pending — owner.
   - **P0 RECONCILIATION QUEUE CLEARED (2026-07-02)** — all 8 `NAV_FIGURE_ESTIMATE_QUEUE ∩ PROVISIONAL` names
     done. Remaining reconciliation-style work: the `OFF_CONVENTION_QUEUE` fixable names (CMBT / STNG's own NB
     [gated on thread (d) for the VLCC portion] / TEN) onto the §9.6 curve, and the **P1 product-basis thread
     (P1c)** — sourcing the product LR1/Handysize/Handymax `newbuild_contract` marks would move the product names
     (TRMD/ASC/STNG) from `basis-pending`/`pending-sourceable` toward `resale-uniform` and unlock VALIDATED-TIGHT.

**P1 normal-rate / justified-leg follow-ons** (the §18 layer is diagnostic-only; these
harden it and the OTHER names — none affect the durable SB-cheap finding, which rests on the
§5b-independent historical floor 0.733). All data-gated routes were pre-registered to defer:

   a. **§18.5b orderbook validation** — the parity "under-ordered" signal (dry-bulk −24%) is
      PROVISIONAL until validated against an INDEPENDENTLY observed orderbook-to-fleet ratio
      per sector (run per sector, crude included). Until then the parity column is a hypothesis
      with a test attached, not a result. This is what makes parity trustworthy or rejects it.
   b. **§18.5a Baltic mean-reversion data** — the historical_mean basis is v1 = current
      `historical_tce_means` (unvalidated); upgrade to a true $/day realized mean (BCI 5TC /
      BPI 4TC / BSI 10TC / New ConTex) and run the registered ≥70%-of-≥12q mean-reversion gate.
   c. **Product LR1 / Handysize / Handymax marks (P1c)** — **PARTIALLY LANDED 2026-07-15;
      LR1 RULED same evening.** **MR: CLEARED to resale-uniform** (xclusiv RESUMED the MR2
      secondhand line 2026-07-13, Resale $55.0M; the $54M exception confirmed −1.8%, age-0
      re-anchored to the resumed line; TEN +0.07% the sole mover, drift gate 0 UNEXPLAINED,
      no re-ratify — `decisions/mr_secondhand_resumption_2026-07-15.md`). **LR1: RULED
      2026-07-15 (owner verbatim: "rule the LR1 fork — taxonomy (b) + contract-floor,
      post-Stage-A")** — fork (i) contract-floor (age-0 → dated xclusiv Panamax-tanker NB
      ~$61.0M; 5yr → dated intermodal ~$60.0M; marks re-dated at execution) + the NEW scoped
      `resale-corroborated` status (uniform-equivalent per-name iff all the name's hulls in
      the class are age ≥10; INSW's young hulls keep it honestly pending). Execution prereg
      FROZEN `PRE_REGISTRATION_LR1_CONTRACT_FLOOR.md`: post-Stage-A anchor round (with the
      mr_secondhand §5 extract-refresh rider), predicted INSW +$7.80M / TEN +$1.17M /
      TRMD+HAFN exact zero (compute_nav-verified), **TRMD → VALIDATED-TIGHT at that round**
      (boundary checkpoints: 8.7%-of-fleet cap check + the W-frag sign-stability eyeball).
      **Handysize/Handymax:** no broker tabulates product secondhand (07-15 sweep
      re-confirmed); Handysize sits on the issuer-contract floor (07-15 re-source), Handymax
      needs a chem-specialist source; NEITHER qualifies for resale-corroborated (the status
      self-limits — no dated second-house 5yr exists for either). `newbuild_contract` LR1
      stays OMITTED (parity would be contract-vs-contract degenerate — prereg §2).
   d. **NAV-layer thread — RESOLVED + SIGNED 2026-07-15 (owner: "sign thread (d) as
      confirmed") — CLOSED.** The basis
      inconsistency was closed by Thread 1 + Amendment B (2026-06-29, all wired classes on the
      dated xclusiv Resale line); the remaining LEVEL-currency question is now CONFIRMED on the
      2026-07-13 xclusiv print (every crude class within the Thread-1B ±2%; VLCC exact, passing
      the BRUT ±0.5% carve-out; advanced W28 corroborates independently) —
      `decisions/thread_d_crude_level_confirmation_2026-07-15.md`. **Consequence: STNG's 2-VLCC
      §9.6 portion is UN-GATED in principle** — the 10-hull wiring becomes its own pre-registered,
      owner-ruled step, queued post-Stage-A (one FV-moving event at a time); even fully wired STNG
      classifies GOVERNED-WIDE at best (Handymax basis pending). The Suezmax +1.49% /
      Supra-Ultra +1.16% drift vs the 07-13 issue rides the post-Stage-A anchor-refresh rider
      (mr_secondhand_resumption §5).
   e. **P3 presentation guards** (no number changes): suppress the non-composable LNG/container
      medians from the headline vector; "rich-near-peak" caveat on crude; §15 governance dual-read
      for TEN/CMDB (clean-NAV-justified ≠ haircut basis). Lowest-stakes; timebox.

Older dry-bulk refinement threads (now DONE by P2): Post-Panamax sub-class split + SB charter
rates — landed this push-block; removed from this list.
2. **CMBT open items** (in `cmbt_log.md`): verify FSO owned-vs-JV (zero `shuttle_contracted_book`
   if the FSOs are inside the equity-JV line); apply the §9.4 yard-quality discount to the
   China-heavy dry-bulk book (v1 is the "without discount" leg); confirm the NMax newbuild
   level vs a current NB quote; G&A/interest are Q1-annualised estimates; chemical/Windcat
   segment books are Dec-2025 vintage; `consensus_fwd_pe` APPROX (Q1 EPS one-off-gain-distorted).
3. **SB open items** (in `sb_log.md`): refresh `consensus_pnav` if a VIE SB NAV is obtained
   (currently P/BV common-book proxy); confirm the finance-lease current/non-current split,
   the exact €950/day + €5.0M mgmt-fee figures, and the buyback authorization from the raw 20-F.
4. **GNK/Diana tender — EXTENDED to 2026-07-24** (checks fired: Jun-26 → extended to Jul-10;
   Jul-13 scheduled check → extended AGAIN to Jul-24, 29.7% tendered, branch-(c) muddle —
   gnk_log 2026-07-13). GNK stays a normal on-curve name; SBLK's conditional 16-vessel purchase
   inactive; consumer P-1 PENDING holds. Next outcome check 2026-07-24.

## Standing operational threads (carry forward)

### Q2-refresh carry-forwards (earnings calendar + preflight §0 drive timing)
- **Early cluster Jul-28 → Aug-6:** STNG/ASC/TNK/CCEC, then ECO/GNK/GSL/CMDB/DHT/INSW/SBLK.
  Now also **CMBT** (ex-Euronav reports ~mid-Aug; H1 basis) and **SB** (early-Aug 6-K) join the
  dry-bulk refresh cycle.
- **BRUT (H1, Aug-13):** first issuer report vs the Pareto-estimate balance sheet; §15 screen.
- **CAPT (Q2):** verify the Jun-16 sponsor VLCC deal terms (§15 tripwire).
- **MPCC (Aug-26):** issuer fleet list → built years + NB delivery quarters; sale prints.
- **GSL (Aug-4/6):** Series B prefs post-ATM; the Jun-26 $917M NB order (apply §9.6).
- **TEN (Sep, H1):** TCM fee-load (§15 anchor); ten_log Q2 kit deltas. **CMDB:** Astros sale.

### Standing threads
- **Daily price-refresh re-ratify pending (deferred 2026-06-30).** The 2026-06-30 close refresh
  moved 9 names' EV vs the baseline (ΔNAV 0% — pure price), incl. two price-driven BAND FLIPS
  (DHT TRIM/SHORT→HOLD +3.8pp, FLNG HOLD→BUY +4.6pp). It was kept OUT of the NAT reconciliation
  commit (owner: don't launder market drift through a sourcing commit) and reverted from the tree
  to isolate NAT. Handle as its OWN deliberate re-ratify on the next refresh: accept the 7 pure-EV
  drifts as routine, but **eyeball whether the DHT/FLNG flips are trivial boundary-crossings or real
  position signals before absorbing them** — don't batch-accept a band flip.
- **FFA feed LIVE again — the "DORMANT since 2026-06-12" note was STALE (probed 2026-07-10 at
  owner prompt).** Ground truth from the archive + curves.json: the poster genuinely went quiet
  Jun-13→Jun-21 (zero images — the dormancy call was right when made), RESUMED Jun-22, near-daily
  parses since (the Jul-2 promotion already used the resumed feed). The OCR leg separately broke
  Jul-4→Jul-6 (launchd bare-PATH/tesseract, fixed 1dba1d1) and now runs daily at 07:00 via the
  ingest wrapper — today's widget parsed clean, staleness alarm quiet (0 days). **PENDING OWNER
  PROMOTION (human-only):** the pipeline dry-bulk curve sits at the Jul-2 vintage while the Jul-10
  parse reads Cape Qn +9.2% / Qf +4.5% / Cal27 +2.5% (Pana +3.3/+5.8/+2.9) — a MATERIAL front-end
  move on the held-name sector (SB/SBLK strips); promote via the normal promote→rerun→drift loop.
  LESSON for the WO2 install: the sentinel's source-silence check (cadence keys already in
  rocketchat_sources.yaml) would have paged the go-quiet AND cleared on resume — stale prose notes
  like this one retire when checklist item 4 lands.
- **Weekly /news-pull** — Saturday cadence AUTO-RESUMES tomorrow (Jul-11 08:00): the Jul-4 failure
  was the same launchd-PATH bug, fixed 1dba1d1; the five harvest steps before ffa_ocr completed
  even on Jul-4, so nothing was lost.
- **OWNER ACTION pending:** ratify-or-revise the A1 horizon (10 strip quarters = end-2028).
- **MB weeklies:** container current-rate refresh (owner-gated); Pana anchor flagged
  structurally low; LNG weekly not yet delivered.
- **Hormuz weight-revisit trigger** — standing (trigger NOT met).
- **Deferred by owner:** /news-pull agent-half orchestration; Task-3 weight adjuster;
  demand-destruction overlay; FFA Stage 2.

### Methodology-soundness remediation — Tier-4 backlog (manage/document; owner judgment)
Per `outputs/METHODOLOGY_AUDIT_2026-06-22.md` §A–G: cycle step-band vs logistic (C-1);
cross-sector anchor commensurability (C-2); marks statistical thinness / age-5 extrapolation
(B-1/B-2); k_broker band vs live (B-3); the 11% rate calibration (B-4); §15 haircut derivation
rule (E-1); data staleness (frozen container feed + APPROX names, F). Phase 2 drift gate is
DONE; **standing care: at each quarterly refresh expect the gate to flag legitimate moves —
annotate the material ones, then `./scripts/ratify_baseline.sh "<Qx refresh>"` to re-anchor.**

## Backtest (reference, not a gate)
`backtest/REPORT.md`: no statistically demonstrated cross-sectional edge. Test 1 (engine EV%,
Nq 23, IC −0.020, INCONCLUSIVE) and the powered P/B-proxy tests (Amendment-2 N=31 / Amendment-3
N=72, both exclude a moderate within-sector value premium on a book proxy) do NOT gate
development. **Test 2** (time-series reversion to fair value, in-sample IC +0.234, p 0.018) is a
HYPOTHESIS — pre-registered out-of-sample/multi-cycle confirmation runs at +8q (~end-2028) or on
a paid feed. Net: not a name-ranker (Test 1 null), plausibly a cycle/value timer (Test 2), unproven.

## Verification gate (run before any handoff / Week-close)
- `PYTHONPATH=src .venv/bin/python -m pytest -q` — main suite, **440 passed / 25 xfailed** at
  2026-07-01 (includes the Phase 2 drift gate, which can legitimately go red on accepted drift —
  annotate + re-ratify; and the xfail-strict provenance queues — an xfail CLEARING is the work).
- `PYTHONPATH=. .venv/bin/python -m pytest backtest/ -q` — backtest (**13**; separate).
- (optional) `cd shipping_harvester && PYTHONPATH=. ../.venv310/bin/python -m pytest -q` — **57**.
- `python -m crude_tanker_fv.pipeline 2026-Q1` runs clean.
- `python -m crude_tanker_fv.reconcile --all` — SANITY all OK/n-a-APPROX; annotate >2pp drift.
- Clean git state; push `origin main`. `.venv310/`, `shipping_harvester/data/`,
  `backtest/vintages/*/` are gitignored by design. NOTE: every pipeline run auto-prepends a
  model-state entry to ALL `decisions/<t>_log.md` and regenerates `outputs/*` — commit that
  churn deliberately (it is expected, mostly "+0.0pp no material moves").
