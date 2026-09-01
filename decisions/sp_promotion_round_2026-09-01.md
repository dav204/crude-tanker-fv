# S&P promotion round — 2026-09-01 (owner: "run the S&P promotion round with your recs")

**Scope as ratified:** the 10-row set staged at `marks_trail_triage_2026-08-31.md` §E
+ the staged 8/31 FFA print (`ffa_capture_review_2026-08-31.md`, Rider 4). Executed
BEFORE R4 per WO5's sequencing preference (marks settle before the Phase-3 freeze).

## HEAD re-sweep (the 8/31 lesson — run before promoting)

Manifest was STALE (the 8/31 + 9/01 dailies were on disk but unindexed — sp_scan
reads `_manifest.json`, rebuilt via `pareto_archive --build-manifest`; the incremental
"nothing to scan" was a false clean, caught by the absence-isn't-evidence check).
Post-rebuild scan of 8/31 + 9/01: **NO re-reports of any round vessel** — the dedupe
stands. Two NEW items surfaced (9/01 daily), routed not promoted:
- **Delta Tankers acquires a 2028-delivery Suezmax resale from DH Shipbuilding,
  $107M** ("Brokers are reporting") — a resale/forward-delivery print, NOT mid-age
  fit material; recorded as resale-level evidence beside the Bristol doc-row and the
  suezmax NB-order row (prompt-vs-forward spread coherent).
- **Suezmax 1Y TC "firm price achieved" at $74.5k/day** — the THIRD direct Suezmax
  12M print in the 74.5-80k family → Stage-B basis inventory (the bucket's trip is
  now triple-corroborated: Sea Topaz 80.0k, Monte Urbasa 74.5k, this 74.5k, MB
  assessment 77.5k, vs held 58,050).

## Leg 1 — transaction promotions (marks channel)

**Pana (+3 in-fit): #23 Presinge** 2015/age 11, $31.0M (MB W33 exact) · **#24 Bbg
Wuzhou** 2016/age 10, $29.0M, `distressed` flag RATIFIED (auction — the fit's +10%
uplift normalizes to ~$31.9M) · **#25 Efraim A** 2010/age 16, $20.0M (W34).
**Supra-Ultra (+5 in-fit, +1 doc): #32 unnamed 2019 NACKS ultramax** age 7, $34.5M
(Pareto 8/18; class-nominal 64k dwt, re-report watch armed — the #22 convention) ·
**#33 Amaryllis** age 13, $24.4M · **#34 African Wagtail** age 13, $20.2M · **#35
Marianna** age 16, $17.0M · **#36 FLC Happiness** age 17, $12.9M (window-edge,
inclusive — in-fit) · **#37 Harvest** age 18, $13.8M **DOC-ROW** (outside [3,17]).
**Suezmax (+1 doc): Bristol** 2024/age 2, $123.0M **DOC-ROW** (outside [3,17]
young-end; the fit-window check ruled it out of the regression — resale-level
corroboration only; resolves the 8/16 price-watch). **Fit unchanged for Suezmax
(n_used unmoved) → zero tanker NAV effect from this leg.**
**NOT promoted, standing blocks:** Front Vefsna $135.0M (the P1 leg — stays blocked
on issuer per-vessel disclosure per the FRO-refresh record; MB's attribution of half
an undisclosed aggregate does not clear the no-back-solve bar while the second hull
is unnamed) · the C-list aged prints (Suez Ice Supreme/Sonangol Namibe/Rui Fu Sheng
age 19, Minerva Xanthe age 20 + ice-premium flag, Hellstugutinden age 23, Princess
Eternity BBHP-financing, Jian Fa 22, scrap-region trio) — all outside-window or
attribute-flagged; the classes carry fresh in-window prints, nothing is gained by
edge rows. · The Kamsarmax trio's third (Japanese-built) leg: still unidentified,
watch rides.

## Leg 2 — FFA 31-Aug promote (rates channel, Rider 4)

**Month-end mapping variant RATIFIED with this round:** Aug rolled off → q1 = the
Sep tenor alone (no m2 to mean); everything else per the documented 13-Jul rule
(q2 = Qf exactly; 2027 decays to the Cal-27 identity exact; 2028 = committed
per-class deltas). Image-verified values (ffa_capture_review_2026-08-31.md):
Cape 45,250/44,475/30,125/Cal 33,300 · Pana 21,900/22,900/18,200/18,175 · Smax
19,875/20,933/16,000/16,125. 12M proxies: **Cape 37,300 (+5.3%) · Pana 20,550
(+4.9%) · Supra-Ultra 18,467 (+4.3%)**; Post-Panamax = Pana; Handy-Bulk ffa row
re-derived ×0.90 nearest-10 (guard-verified). as_of default → 2026-08-31 both rate
files; tanker Stage-A holds untouched. The scenario DECK is untouched (the ×0.90
deck identity keys on scenario_inputs, which this round does not edit).

## PREDICTED IMPACT (frozen BEFORE the regen — the 24-Aug lesson applied: the
## cycle-reweight channel is predicted UP FRONT this time)

- **Marks channel:** dry mid-age legs firm modestly (Pana age-10/11 prints at 29-32
  vs softer priors; Supra young-end 34.5 pulls the slope up). Movers: the dry five
  only (SBLK, GNK, CMDB, SB, 2343) — per-name band **|ΔNAV| ≤ 2.5%**, direction UP.
- **Rates channel:** dry 12M +4.3-5.3% lifts the dry cycle ratio ~1.47× → ~1.53×
  (elevated deepens) → **scenario EV fades ~1-1.5pp dry-book-wide while single-FV
  rises** — the exact mechanism the 24-Aug promote surfaced post-hoc, now
  pre-registered.
- **Combined per-name bands (the dry five): ΔNAV ∈ [0, +3%]; ΔEV ∈ [−3pp, +1pp].**
- **Forward invariance: every non-dry name delta EXACTLY 0.0** (no in-fit rows
  entered any tanker/product class; no tanker rate line moved).
- **Flip risk, pre-eyeballed:** CMDB (HOLD, post-G6) could print HOLD→T/S on the EV
  fade — the SAME direction as its G6-accepted flip, recross watch already armed;
  SBLK stays T/S; SB's BUY expected to HOLD-or-stay-BUY (single-FV up vs EV fade);
  GNK/2343 stay T/S. **Any flip toward BUY = halt-and-investigate** (standing rule).
- **Post-regen consequentials (mandatory):** all five §9.10 family sidecars re-run
  (dry family ranges shift with EV) before the scorecard regen commits; drift-gate
  rows annotated per name, dated; SBLK flip-margin pin expected to move ~±0.1-0.3pp
  (re-pin WITH the round, dated).

## Disposition

Inputs commit FIRST (this doc + 3 transaction files + 2 rate files + manifest/queue
churn), regen SECOND; gate rows annotated; the explained rows ride the owner's next
ratify (R4's Phase 5, or earlier at owner word). The spot_tce hold: UNCHANGED by
this round (its annotation stands — display-grade, rides the next owner sitting).
