# Reweight-trigger archive — done and retired cards (moved out of the live register 2026-09-02)

Owner ruling 2026-09-02 (prune ledger rows 53-61, F20 + F8): the live register keeps only ARMED cards
(23 → 10) so a sitting reads ~150 lines, not 539. Done cards are history; retired cards are listed with
their reason. `tests/test_refresh.py` pins the two 2026-07-02 checkpoints here. The YAML below is verbatim.

```yaml
# ---- DONE (archived 2026-09-02) ----
crude_mou_implementation_check:
  sector: crude
  due: 2026-07-17
  observable: >
    Islamabad Memorandum 30-day implementation deadlines (signed Jun-17-2026):
    blockade fully removed, Iranian demining complete, Hormuz traffic restored
    to pre-war proportionality. Check transit counts / UKMTO-JMIC advisories /
    war-risk premia. This checkpoint lands four weeks BEFORE the toll cliff.
  action: >
    Non-normalized traffic by the due date is direct evidence for the
    MoU-ineffective leg (shift mass pre_mou-ward); normalized traffic
    corroborates mou_base. Either way, record the check in decisions/.
  status: done   # CHECKED 2026-07-18 (due 7/17): FAILED all three observables — Jul-14
                 # naval blockade (reverse of removal), TSS mine area still published at
                 # Jul-16 (demining incomplete), transits ~8-11% of pre-crisis, war-risk
                 # ~8x. Pre-registered shift ALREADY LIVE via the 7/12 Jun-9 restore →
                 # closed PRO-FORMA, zero movement. Escalation-beyond-Jun-9 observation
                 # registered for the 7/22 round-3 watch + the Aug-16 toll-cliff reweight.
                 # decisions/mou_implementation_check_2026-07-18.md
  added: 2026-07-02

# ---- DONE (archived 2026-09-02) ----
crude_pause_talks_watch:
  sector: crude
  due: 2026-08-07   # RECORDED 2026-08-09 (2d late; drain-occupied 8/8) -> BRANCH 3
  observable: >
    Successor to crude_ceasefire_mediation_watch (B' executed 2026-07-31). The
    strike PAUSE (US, ~7/26-27, at Iran's request) + mediator-reported progress
    vs Iran's denial of bilateral talks (Oman-only channel). Does a ceasefire
    convene/take effect, do strikes resume, or does the ambiguous pause persist
    into the toll cliff?
  action: >
    Ceasefire convenes/takes effect -> re-normalization PROPOSAL to the owner
    (never unilateral; mou_bear is the landing zone, B' already holds it ~flat).
    Strikes resume -> record; B' stands (escalation mass untouched by design).
    Ambiguous pause persists -> record; the Aug-16 toll-cliff venue (9d later)
    does the full re-derivation regardless. LESSON ENCODED from the 7/29 check:
    this card names THREE branches, not two.
  status: done   # 2026-08-09: branch (3) AMBIGUOUS PAUSE PERSISTS — US pause holds,
                 # Oman framework close-not-convened, Iran conditions reopening, 8/8 ADNOC
                 # tanker hit = the in-pause vessel-attack pattern continuing. RECORD ONLY;
                 # B' stands; full re-derivation at crude_day60_toll_cliff 8/16.
                 # decisions/crude_pause_talks_watch_2026-08-09.md
  added: 2026-07-31

# ---- DONE (archived 2026-09-02) ----
crude_day60_toll_cliff:
  sector: crude+product
  due: 2026-08-16
  observable: >
    Islamabad Memorandum toll-free window expires (~Jun-17 + 60d; the released
    text makes Hormuz toll-free for 60 days only — Iran asserts a fee right
    after). Does Iran impose transit fees? Scope widened to PRODUCT (reviewer
    rider 1, 2026-07-02): MEG product flows are as toll-exposed as crude —
    fees would re-tilt refinery_squeeze/moderate_correction as well as the
    crude MoU legs.
  action: >
    PRE-REGISTERED RE-WEIGHT DATE REGARDLESS OF OUTCOME — mou_base's weight is
    conditional on this resolving benignly. Fees imposed: shift mou_base toward
    mou_bear/pre_mou AND revisit the product family the same day. Toll-free
    extended/waived: pre_mou toward 0. Rerun the §9.10 diagnostics, reweight,
    annotate, ratify.
  status: done   # 2026-08-16, owner venue ruling — decisions/crude_day60_toll_cliff_2026-08-16.md
  resolution: >
    NEITHER pre-registered branch fired. Fees: intent documented (PGSA "service
    fees", the UNCLOS-safe framing); collection NOT evidenced. Extension: not
    evidenced. Oman framework: not convened. The window expired into
    interdiction — UKMTO traffic 17% of the pre-conflict average, US naval
    blockade in force, Iran attacking the traffic it proposes to bill. R1: C2
    EXECUTED, crude 0.25/0.57/0.05/0.13 -> 0.25/0.62/0.00/0.13, mou_base retired
    to ZERO but retained as a leg (series continuity). R2: product revisit a
    recorded NO-OP, 7/14 shapes stand. R5: C3 (escalation tilt) DECLINED.
    Successors: hormuz_fee_collection_watch + escalation_pause_corroboration.
  added: 2026-07-02

# ---- DONE (archived 2026-09-02) ----
crude_doha_talks_resumption:
  sector: crude
  due: 2026-07-10
  observable: >
    Doha technical talks resume after the Khamenei funeral processions
    (Jul-4-9). Watch for collapse or any resumed strike.
  action: >
    Collapse or strikes: restore a Jun-9-shape risk-on weight set the SAME DAY.
    Progress: no reweight; update this trigger's due to the next round's date.
  status: done    # FIRED 2026-07-07/08 (strike leg: 3 vessels hit near Hormuz, US
                  # re-imposed MoU-lifted sanctions + CENTCOM retaliation, threat
                  # 'severe'); caught 2026-07-12 (watch-layer install gap — the
                  # sentinel's FIRST run surfaced it). RESOLVED 2026-07-12: the
                  # pre-registered restore EXECUTED at owner go — crude weights back
                  # to the Jun-9 shape 0.25/0.45/0.18/0.12. Record + per-name deltas:
                  # decisions/doha_check_2026-07-12.md. Follow-up round watched by
                  # crude_doha_round2_outcome below.
  added: 2026-07-02

# ---- DONE (archived 2026-09-02) ----
crude_doha_round2_outcome:
  sector: crude
  due: 2026-07-15
  observable: >
    The post-funeral Doha technical round (reported scheduled Tue Jul-14;
    timetable "unclear" amid the Jul-7/8 strikes + sanctions re-imposition).
    Did it convene, and with what outcome?
  action: >
    Any de-escalation outcome (round convenes + sanctions relief path or strike
    stand-down): NO pre-registered reweight — put a re-normalization proposal to
    the OWNER (the Jul-12 war tilt is the standing set; unwinding it is a new
    decision, per the Jul-2 stand-down precedent). Collapse/no-show or further
    strikes: weights already war-tilted — record the check, re-arm toward the
    next credible diplomatic date. Interplay: crude_mou_implementation_check
    (Jul-17) is largely pre-empted by the sanctions re-imposition — keep for the
    record; crude_day60_toll_cliff (Aug-16) stands.
  status: done   # 2026-07-14 EVE — NO-SHOW/STALL branch: no credible report the Jul-14
                 # round convened (freshest coverage Jul-10: timetable unclear, Iran
                 # reluctant amid ongoing strikes). No reweight owed; war tilt stands.
                 # Record: decisions/doha_round2_check_2026-07-15.md. Successor below.
  added: 2026-07-12

# ---- DONE (archived 2026-09-02) ----
crude_doha_round3_watch:
  sector: crude
  due: 2026-07-22
  observable: >
    Successor to crude_doha_round2_outcome (no-show recorded 2026-07-14): does a
    Doha/Switzerland technical round convene within the week, or does the path
    collapse into the toll-cliff track? Watch for a convening report, a formal
    talks-off statement, or strait/toll policy statements.
  action: >
    Same branch logic as round-2 (pre-registered 2026-07-12): de-escalation ->
    re-normalization PROPOSAL to the owner, never a unilateral reweight;
    no-show/strikes -> record + re-arm. The mid-Aug MoU expiry/toll window is
    covered separately by crude_day60_toll_cliff (Aug-16). NOTE: the staged
    Hormuz re-tilt ruling (hormuz_retilt_proposal_2026-07-13.md) is UNBLOCKED
    as of the round-2 no-show — owner decision cell, independent of this watch.
  status: done   # CHECKED 2026-07-22: COLLAPSE branch — no round convened; MoU declared
                 # "over" (Trump, ~Jul-12 Ankara) / "suspended" (Iran, Jul-18); 10th
                 # consecutive strike day Jul-21, US soldiers killed, Iran hit Kuwait,
                 # Brent $91; ≥9 ships attacked since Jul-6. No reweight (pre-registered
                 # branch); war tilt stands. Record:
                 # decisions/doha_round3_check_2026-07-22.md. Successor below.
  added: 2026-07-14

# ---- DONE (archived 2026-09-02) ----
crude_ceasefire_mediation_watch:
  sector: crude
  due: 2026-07-29
  observable: >
    Successor to crude_doha_round3_watch (collapse recorded 2026-07-22). The only
    live de-escalation thread: Iran has confirmed receiving mediation proposals and
    a possible 10-day ceasefire is reported under discussion (Jul-21). Does a
    ceasefire/mediation round convene or take effect, or does daily-strike tempo
    continue into the toll-cliff track?
  action: >
    RULED 2026-07-22 (owner: "Rule A - conditional B' pre-registered on the 7/29
    watch" — decisions/mou_scenario_reweight_proposal_2026-07-22.md): continued
    collapse-track (no ceasefire convened or in effect at this check) -> EXECUTE
    the FROZEN B' reweight (escalation .25 / pre_mou .57 / mou_base .05 /
    mou_bear .13) mechanically per the proposal's execution loop — CAPT HOLD->BUY
    flip eyeballed INDIVIDUALLY (halt-and-investigate rider), owner-aware ratify;
    mid-cluster landing accepted at the ruling. De-escalation (ceasefire takes
    effect / talks convene with a sanctions-relief path) -> the conditional is
    VOID; re-normalization PROPOSAL to the owner, never a unilateral reweight.
    Either branch: crude_day60_toll_cliff (Aug-16) stands as the venue for the
    full MoU-family re-derivation.
  status: done   # RULED + EXECUTED 2026-07-31 (owner: "Execute B'"): the letter governs the
                 # pause-without-talks third state. B' live (0.25/0.57/0.05/0.13, commit
                 # 6c508fb; regen at the 7/31 vintage, ratified 1d1cdb9; CAPT no-flip,
                 # TNK flip eyeballed price-led). Successor below; Aug-16 unchanged.   # CHECKED 2026-07-31 (2d late): the card's BINARY DOES NOT
                 # FIT — US paused strikes ~7/26-27 at Iran's request, mediators report
                 # progress, BUT Iran denies bilateral talks (Oman-only channel) and NO
                 # ceasefire is convened or in effect. By the card's letter the collapse
                 # branch is met (B' executes); the state is a third one the ruling did not
                 # contemplate. Agent rec = EXECUTE (B' retires dead-MoU mass, leaves
                 # escalation untouched — premise undisturbed by a pause). OWNER RULES.
                 # Record: decisions/ceasefire_mediation_check_2026-07-31.md
  added: 2026-07-22

# ---- RETIRED 2026-09-02: F8 — never observed in 9 weeks (0 decisions, 0 digests); the war-risk/transit line now rides the Saturday news-pull scheduled task (its SKILL.md) ----
crude_transit_normalization:
  sector: crude
  due: null
  observable: >
    Standing event-watch: mine-clearance confirmation / UKMTO-JMIC advisories
    lifted / war-risk insurance premia normalize. Premia level currently
    UNCONFIRMED (2026-07-02 research brief 403-blocked) — standing Saturday
    news-pull item until a level is on file.
  action: >
    Sustained normalization corroborates mou_base; renewed advisories or a
    premia spike is MoU-ineffective/escalation evidence.
  status: armed
  added: 2026-07-02

# ---- RETIRED 2026-09-02: F8 — same disposition as crude_transit_normalization ----
crude_brent_reopening:
  sector: crude
  due: null
  observable: >
    Standing event-watch: Brent sustained above pre-war ($72.48, Feb-27-2026
    reference) + $10/bbl — macro confirmation the stand-down is failing and
    war premium is rebuilding.
  action: >
    Same-day §13.3 review; risk-on reweight if corroborated by tanker rates.
  status: armed
  added: 2026-07-02

# ---- RETIRED 2026-09-02: F20 — only the 7/06 rebase was card-driven; the 42-day watchlist-vintage lane (STALE-INPUT) and the static guard page instead ----
all_sectors_consensus_pair_recapture:
  sector: all
  due: 2026-10-02
  observable: >
    Watchlist consensus vintages (as_of) are 23-72d old (BRUT worst) vs the
    14d freshness threshold — the pure sentinel + the Action issue carry the
    9-name list daily. The consensus pair (price + consensus_pnav + fwd_pe)
    is only valid AS A PAIR from one vintage (the TEN $44 lesson: a price
    never moves without rebasing consensus from the same daily).
  action: >
    Quarterly recapture as a packet procedure (WORKFLOWS §Consensus-pair
    recapture): ONE Pareto daily supplies price + P/NAV + fwd P/E for every
    covered name in the same sitting; APPROX names (NAT/ASC/CCEC) flagged not
    faked; watchlist as_of rebased together; gate annotated. On completion
    re-arm to the next quarter boundary and RESOLVE the threshold question
    (14d nag vs quarterly cadence) with a dated decision.
  status: armed
  added: 2026-07-03  # first sitting completed 2026-07-06 (4 days early, Pareto
                     # 3-Jul daily): 18 pairs rebased, TEN/SB/GSL/CMDB absent
                     # from that edition and left at their documented vintages;
                     # re-armed quarterly. decisions/consensus_recapture_2026-07-06.md

# ---- RETIRED 2026-09-02: F20 — an event-watch that FAILED silently (BWLP Q2 refreshed 8/31, twelve_month_tc VLGC still 63,615 of 2026-06-02); folded into lpg_v1_lock_rerun as a dated line ----
vlgc_realized_tce_refresh:
  sector: lpg
  due: null
  observable: >
    Standing event-watch (WO3 Phase 3, 2026-07-09): any new VLGC realized-TCE
    disclosure (Dorian / BW LPG quarterly reports — next cluster ~Aug-2026) or
    a fresh VLGC 1-yr TC fixture / broker TC assessment print. The VLGC 12M-TC
    line (63,615 realized, disclosure-cluster vintage 2026-06-02) and the
    derived base forward curve are HELD — the war-spiked vlgc_* spot dailies
    are never promoted (Phase-0 convention), and a held VALUE is invisible to
    the mtime staleness preflight (the tanker-hold lesson).
  action: >
    Refresh twelve_month_tc.VLGC (realized basis — NEVER a TC numerator over
    the realized anchor, the voided mixed-basis read) + re-derive the
    ffa_forward_curve VLGC row (absorption_base-path rule, or the observed
    term structure if fixtures land); watch the war-premium decay — the 1.59×
    cycle read is Hormuz-elevated; record in decisions/, gate-annotate any
    LPG-name move (none until Phase 4 validators onboard).
  status: armed
  added: 2026-07-09

# ---- RETIRED 2026-09-02: F20 — never fired, no ruling ordered it; folded into product_glut_arrival_timing (the merged 10/02 card) ----
all_sectors_quarterly_staleness_floor:
  sector: all
  due: 2026-10-02
  observable: >
    Any sector's locked weight set older than one quarter (roll this due
    forward to decision-date + 1 quarter on every reweight). Backstop, not the
    standard — the Jun-9 crude set went materially stale in 23 days.
  action: >
    Forced §13.3 review of every sector's weight vintage; record even a
    "reviewed, no change" outcome in decisions/.
  status: armed
  added: 2026-07-02

# ---- DONE (archived 2026-09-02) ----
drybulk_spot_daily_resumes:
  sector: dry_bulk
  due: 2026-09-01
  observable: >
    Pareto Shipping Daily resumes printing after the Jul/Aug seasonal silence
    (owner intel via RC 2026-07-12; silence_days:14 sentinel override expires
    ~Sep-1). First resumed daily carrying dry-bulk spot prints (Capesize VLSFO /
    Panamax "Average of key routes" rows).
  action: >
    Revert the spot_tce.yaml dry-bulk rows (Cape/Pana/Post-Panamax/Supra-Ultra)
    from the 13-Jul FFA front-month proxy basis back to the daily's spot
    prints, restamp their as_of from the same edition, and drop the proxy
    header note (decisions/ffa_promotion_2026-07-13.md surface 3). Supra keeps
    the FFA-proxy fallback ONLY on editions with no Smax spot row (the 2-Jul
    precedent). Diagnostic surface — no strip impact; annotate only if a band
    moves.
  status: done   # FIRED 2026-08-09 (8/7 daily prints Cape 42,313 / Pmax 20,473 /
                 # Umax 20,326, verified on the RENDERED page) → EXECUTED 2026-08-10
                 # in the Stage-A-day spot_tce promote: dry rows reverted to the
                 # daily's spot prints, FFA front-month proxy era ENDED. Retire —
                 # the daily column is back; normal spot_tce cadence resumes.
  added: 2026-07-13

```
