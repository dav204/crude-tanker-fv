# Marks-trail triage — staged weeklies 2026-07-20 → 08-07 + the queued dispositions (owner: "let's work on the marks/assessment promotion", 2026-08-09)

**2026-08-09. Sources swept (source list built from the STAGING TREE per the 7/28
lesson):** MB Tanker/Dry Bulk/Container/LNG W31 (7/30-31) + W32 (8/6-7) · banchero
files W30+W31 (= printed issues W29 14-21 Jul + W30 21-28 Jul) · intermodal files
W30+W31 (= issues W29 21-Jul + W30 28-Jul) · xclusiv 20-Jul + 27-Jul · advanced W31
(24-31 Jul) · fearnleys W30 (S&P BLANK — 3rd blank-as-staged issue; W29 still
never staged) + W31 (assessments only; **structural: Fearnleys prints NO named-
transaction S&P table — feed is assessment-grade for marks purposes**) · Pareto
dailies 8/03-8/07 (2 queue sentences) · plus the two queued dispositions: the
2026-08-09 sp_print disposition (4 prints, Pareto 7/20) and the stage-A-basis §3
TNK issuer prints (owner-gated 7/31, now authorized). Extraction: 8-agent workflow
over local PDFs, results archived in the session scratchpad.

**PROMOTION EXECUTED THIS RECORD** (owner authorization 2026-08-09) via the standard
prints-drift loop (re-run → transaction_anchor_comparison → annotate >2pp movers /
flips, every flip individually eyeballed).

## A. PROMOTE-LIST (exact per-vessel price · in mid-age window [3,17] · dedup vs the 7/18 + 7/28 batches)

Tanker:

| # | Class | Vessel | dwt | Built (age) | Price | Sources | Notes |
|---|---|---|---|---|---|---|---|
| 1 | VLCC | CELESTE NOVA | 318,510 | 2013 (13) | **$120.0M** | MB W32 exact | Zodiac→ADNOC; scrubber |
| 2 | VLCC | DONOUSSA | 299,999 | 2016 (10) | **$128.0M** | MB W32 exact; Advanced W31 $123M (older — newest-print-wins G5) | Euronav→"COPTCO" (as printed) |
| 3 | VLCC | SEAPASSION | 299,271 | 2017 (9) | **$130.0M** | MB W32 exact | Thenamaris→ADNOC; scrubber |
| 4 | VLCC | ~~TNK 2013-built~~ | | | | | **DEDUPE — NOT ADDED**: already in vlcc.yaml as TEEKAY SINGAPORE SPIRIT $84.5M (see §B-dedupe) |
| 5 | Suezmax | ~~TNK 2009-built~~ | | | | | **DEDUPE — NOT ADDED**: already suezmax.yaml's PRIMARY ANCHOR ($53.5M age-17, top row); caught by the round-trip guard (see §B-dedupe) |
| 6 | LR2 | ELLIE LADY | 109,999 | 2009 (17, edge) | **$47.5M** | xclusiv W31 + advanced W31 + banchero W31-file + intermodal W31-file — 4-source exact | eco, scrubber; Western Shipping→Trafigura. Distinct hull from Jag Lokesh (HHI 105,599, promoted 7/18) |
| 7 | LR2 | ~~Pareto-unnamed 2009 LR2~~ | | | | | **DEDUPE — NOT ADDED**: the Pareto 7/20 "$44M to a Greek buyer, drydock-due" IS JAG LOKESH (2009 HHI, $44.0M, Greek/Y-KNOT, promoted 7/18 from advanced W27) — a later re-report, not a new deal (see §B-dedupe) |
| 8 | MR | ~~Pareto-unnamed 2011 pumproom~~ | | | | | **HELD — NOT ADDED**: possible duplicate of HONESTY (2011 GSI, $25.1M exact, July, promoted 7/18); unnamed single-source vs a named exact print 10 days earlier — held per the ingestion-key lesson (see §B-dedupe) |

Dry bulk:

| # | Class | Vessel | dwt | Built (age) | Price | Sources | Notes |
|---|---|---|---|---|---|---|---|
| 9 | Cape | ORANGE TIGER | 181,395 | 2011 (15) | **$36.5M** | MB W32 exact | Daishin Senpaku→Greek |
| 10 | Cape | AANYA | 179,628 | 2012 (14) | **$36.9M** | MB W32 exact; banchero W31-file $37.5 (older — newest wins) | the AASHNA sister (7/28 §H: "remains on market") — now SOLD; Adani |
| 11 | Cape | ATTIKOS | 178,929 | 2012 (14) | **$37.5M** | Advanced W31 exact | scrubber; Sungdong — distinct hull from AASHNA (HHIC 179,523) |
| 12 | PPMX | OCEAN RHEA | 92,648 | 2011 (15) | **$15.25M** | MB W29 exact (7/28 §I3 upgrade, promote-grade) | seller Wei Xu, buyer Chinese; the clean PPMX print |
| 13 | PPMX | ANGLO MARIE LOUISE | 114,674 | 2011 (15) | **$19.70M** | MB W32 exact | scrubber; Anglo International |
| 14 | PPMX | ANGLO JESSICA | 114,664 | 2010 (16) | **$18.25M** | MB W32 exact | scrubber |
| 15 | PPMX | ANGLO ALEXANDRIA | 114,248 | 2011 (15) | **$19.70M** | MB W32 exact | scrubber. Rows 13-15: 114k "post-panamax" hulls — dwt-scaled fit carries the size; class basin assignment flagged for the ppmx refit review |
| 16 | PPMX | PONT ROUGE | 99,992 | 2021 (5) | **$36.0M** | advanced W31 + intermodal W31-file exact | eco; **Q4-2026 FORWARD delivery → standard flag** (the 7/28 §H Oldendorff precedent: forward ≠ prompt premium); first young PPMX print — `ppmx_txn_refit` young-age condition now 1 of 2 |
| 17 | Pana | YARRA | 78,184 | 2015 (11) | **$28.5M** | MB exact + intermodal W31-file exact (banchero "mid 28") — 7/28 hold upgraded | eco; Chinese buyer |
| 18 | Pana | AQUAVITA AIM | 82,192 | 2019 (7) | **$38.2M** | MB W32 exact | eco; European buyer; age 7 = inside the G1 7-16 fit band (not young-flagged) |
| 19 | Pana | ROYAL HOPE | 81,011 | 2015 (11) | **$30.8M** | MB W32 exact | eco; Tokei Kaiun |
| 20 | Pana | VELOS JASPER | 82,030 | 2012 (14) | **$23.5M** | MB W32 exact | scrubber; SS/DD due |
| 21 | Pana | MONT FORT | 82,113 | 2012 (14) | **$22.0M** | MB W32 + intermodal W31-file + advanced W31 exact | scrubber; **TC ATTACHED → quality_flag tc_attached** |
| 22 | Supra-Ultra | AMIS WISDOM VI | 61,456 | 2011 (15) | **$22.3M** | MB exact 22.30 + xclusiv W31 22.3 ("basis SS/DD passed"); intermodal 22.0 variance recorded — 7/28 hold upgraded | banchero narrative "91,456 dwt Kamsarmax" is its own transposition (its table prints 61,456; 2-house-confirmed) |
| 23 | Supra-Ultra | AMIS WISDOM II | 61,611 | 2010 (16) | **$22.0M** | xclusiv W31 exact | basis delivery SS/DD passed |
| 24 | Supra-Ultra | ST PAUL | 57,982 | 2010 (16) | **$16.5M** | MB W31 exact (advanced "Mid 16", xclusiv "MID 16") | Ship Finance Maritime→Vietnamese |
| 25 | Supra-Ultra | UNITED HALO | 55,848 | 2012 (14) | **$19.0M** | intermodal W31-file exact "each" + banchero 19 — 7/28 hold upgraded | en-bloc pair; **built-year conflict** banchero 2010 vs intermodal + 7/28 record 2012 → 2012 (2-1), conflict annotated |
| 26 | Supra-Ultra | VENUS HALO | 55,848 | 2012 (14) | **$19.0M** | as #25 | en-bloc pair |
| 27 | Supra-Ultra | AGIOS NEKTARIOS I | 56,722 | 2010 (16) | **$13.3M** | advanced W31 exact | Chinese-built (Jiangsu) — yard spread vs #24 real |
| 28 | Supra-Ultra | EBURY TRADER | 56,603 | 2011 (15) | **$13.1M** | MB W32 exact | SS/DD due; Chinese-built; Lomar→Chinese |
| 29 | Supra-Ultra | LILA FROSTBURG | 56,425 | 2013 (13) | **$16.8M** | MB W32 exact (advanced "High 16") | eco |
| 30 | Supra-Ultra | NIKOS N | 53,815 | 2011 (15) | **$15.0M** | MB W32 exact (advanced "Low 15") | Am Nomikos |
| 31 | Supra-Ultra | VIVA ECLIPSE | 54,279 | 2009 (17, edge) | **$11.75M** | MB W32 exact | Unity Navigation→Chinese |
| 32 | Supra-Ultra | LIANSON HERMES | 53,507 | 2009 (17, edge) | **$13.0M** | banchero W31-file + advanced W31 exact | Indian buyers |

## B-dedupe. UNNAMED-PRINT DUPLICATES CAUGHT (post-first-run correction, 2026-08-09)

The first pass ADDED four rows that dedupe review + the suezmax round-trip guard then
killed; all four were removed before the final ratify, and the dedupe went the other
way on the two queued Ultramax prints:

- **TNK Suezmax $53.5M** — already suezmax.yaml's PRIMARY ANCHOR since the Q2-ER
  subsequent-events promotion (the stage_a_basis §3 "owner-gated" pointer was STALE
  for this print). Guard `test_load_suezmax_yaml_round_trip` caught the double-add.
- **TNK VLCC $84.5M** — already in vlcc.yaml as TEEKAY SINGAPORE SPIRIT (age-13).
- **Pareto 7/20 "LR2 2009 $44M Greek, drydock-due" = JAG LOKESH** (promoted 7/18) —
  same hull/price/buyer-nationality; the queued disposition row was a re-report.
- **Pareto 7/20 "MR 2011 pumproom $27.0M"** — HELD as possible duplicate of HONESTY
  (2011, July, $25.1M exact); not promoted.
- Queued "**Ultramax 2020 $36.5M**" = **WF ARTEMIS** (promoted 7/18; the §H Compass
  identity) — no action. Queued "**Ultramax 2016 $30.7M**" ≈ **WOOYANG BELOS**
  (promoted 7/28 @ $30.0 banchero exact) — treated as the same deal at source
  variance (Pareto 30.7 vs banchero 30.0; newest/exact stands at 30.0, variance
  recorded here).
- **Net: the entire 2026-08-09 sp_print disposition queue resolves to ZERO new rows**
  — all four sentences were re-reports of already-promoted deals (or held). The
  promotion's real content is the W31/W32 broker-weekly + MB batch (#1-3, 6, 9-32
  = 28 rows) and the two §B revisions.
- **LESSON (candidate CLAUDE.md rule): before promoting an UNNAMED broker print,
  sweep the class file for same-age/same-built prints within ±10% price in the
  trailing ~6 weeks — unnamed prints are re-report magnets.**

## B. REVISIONS to already-promoted rows (G5 standing rule: newest print wins)

- **CAPT EUGENE** (Supra, promoted 7/28 #14 @ $16.8M advanced): MB W31 **16.60** + xclusiv
  W31 **16.6** — two newer exacts → corrected to **$16.6M**, revision annotated on the row.
- **CMB JORDAENS** (Ultra, promoted 7/28 #7 @ $35.2M xclusiv, in_fit false / prompt_premium):
  MB W31 **35.50** + advanced W31 **35.5** → corrected to **$35.5M**. ALSO seller per MB =
  "Nova", per advanced p1 prose = **Keiyo Kisen** — neither corroborates the 7/28 "CMB-complex
  disposal (ex-Bocimar)" cell; the cmbt_log disposal note is now UNSUPPORTED by the two
  newest sources → cmbt_log gets a correction footnote (query, not assertion). Excluded
  from fit either way (flag unchanged).
- **SEACON TOKYO** (7/28 #8 @41.6): MB W31 prints **41.60 exact** (buyer Obe Ships — a
  FOURTH house corroboration; xclusiv W31 "MID 41"). No change.
- **AASHNA** (7/28 #1 @37.5): banchero W30-file tables it at 37.5 (dwt 179,253 = its own
  transposition, again). No change; corroboration count +1.

## C. HOLDS (unchanged or new)

- **HEROIC** (Cape 2010): banchero W30-file confirms "market sources indicating $32.8M" —
  still indication-tier. HOLD stands.
- **INDUS PROSPERITY** (PPMX 2011, $11.5M): banchero W31-file "Reported in bad conditions"
  vs Compass 7/28 "SS/DD due, NOT poor" — condition dispute persists; the owner-ruled hold
  (PPMX fit-thinness, borrowed distress-uplift) STANDS.
- **HL BALIKPAPAN** (PPMX 114,531/2012), **ALGERIA PROSPERITY** (VLCC 2012), **CALYPSO**
  (LR2 2021): prices UNDISCLOSED — no print.
- **DELTA 4-ship VLCC en-bloc → ADNOC $472.0M** (Angelica/Amazon/Glory/Apollonia,
  2012/2015/2012/2015): en-bloc WITHOUT per-vessel split → documented, never back-solved
  (house rule). Context: implies ~$118M/hull average against #1-3 singles at 120-130.
- **VLCC gain-only sentence** (Pareto 8/03: "$74.4m gain... delivered Q4, buyer
  undisclosed"): NO PRICE → not promotable; identification pending (seller sold "6x VLCCs
  and 2x capes in Q1" per the sentence — watch for the named disclosure).

## D. Out-of-window / out-of-scope (recorded)

- VELOS EMERALD (LR2-size dirty 115,042/2008, $50.0M xclusiv W31) — age 18, outside [3,17].
  LEVEL context: aged war-market tanker bid, sits ABOVE the 2009 prints #6-7.
- IVESTOS 8 (Pana 75,239/2008 $11.7M) · FRANCESCO/"G.B." CORRADO (77,061/2008 $15.0M,
  MB W32 + advanced same deal, name variants) · BLUE DIAMOND (53,521/2008 $11.0M) ·
  LIBERATOR (28,414/2006 $6.7M) — all age ≥18, outside window.
- StSt/chem (off-curve classes): FG ROTTERDAM 22.7/"mid-high 22s" · DING HENG 39 18.3 ·
  CNC DREAM 11.5 · EVA HONGKONG (2017) 30.0 — documented only.
- TORM MR NEWBUILD ORDER (Pareto 8/05): "$46M per ship scrubber-fitted" — age-0 leg,
  out-of-window by design; corroborates the MR NB anchor ($49.5M prompt resale / $45-46
  order tape); TRMD-relevant (first TORM order since 2018), noted for trmd_log at the
  8/26 refresh.
- MB W32 tanker fixture MARINA AMAN (19.7k chem, 50-100 days) — out of scope.

## E. Handy-Bulk tally (NOT fitted — accumulates toward `handy_bulk_txn_refit`)

Three new in-window prints: **AFRICAN HARRIER** 37,707/2014 **$20.1M** (advanced +
intermodal W31-file + MB W31 3-source exact; eco, MUR) · **NEW JOURNEY** 36,371/2015
**$19.8M** (MB W32 exact; eco, Hsin Chien) · **SAKURA DREAM** 38,213/2013 **$18.5M**
(advanced W31 exact; Nov-Dec'26 FORWARD delivery noted). Ages 12/11/13 — the **≤6yr
age-node condition remains UNMET** (count advances; arming still short). Level note:
the 2014-15 Japanese Handies at 19.8-20.1 print ~35% above the 2013 SAKURA forward-dely
— recency-checked, all three are eco Imabari/Shikoku-class quality.

## F. Cross-check notes (assessment feeds, no promotion path)

- **Container S&P** (feeds the §11.8 MB-assessment cross-check, not a txn-anchor class):
  MONTPELLIER 2,824-TEU/2006 "xs $27M" + APOLLO TRADER 1,118-TEU/2003 $11.0M (advanced
  W31) · FITZ ROY 1,740-TEU/2011 "mid/high $20s" narrative (MB W32) — Fitz Roy sits
  consistent with MB's own 1,700-TEU ladder (10yr 29.5 / 15yr 23.5 at W32).
- **LNG**: METHANE MICKIE HARPER 170k/2010 TFDE ~$79M rumoured Excelerate (MB W31) —
  to the mb_lng_crosscheck file at the next FLNG/CCEC review; MB 145K-15yr assessment
  27.0 vs this 2010 (16y) 170k print at ~79 — the assessed ladder covers smaller/older
  tonnage; not comparable rungs, recorded verbatim.
- **Fearnleys W31 asset ladder** (5yr/10yr): VLCC 140/110 · Suez 103/85.5 · Afra-LR2
  80/70 · Cape 74/59 · Kmax 38.5/31 · Umax 38/30 · Handy 30.5/23. vs MB W32 5yr: VLCC
  152, Suez 100, Afra 82, LR2 84, Cape 71 — the I2 lesson again (houses ±8% apart on
  VLCC 5yr); class-varying, spec-confounded; no doctrine change.

## G. Execution + eyeball registrations (before the loop runs)

1. Rows #1-32 appended to `transactions/{vlcc,suezmax,lr2,mr,cape,pana,post_panamax,
   supra_ultra}.yaml` with per-row provenance; revisions per §B applied in place.
2. Direction eyeball, registered BEFORE the run: tanker prints (VLCC 120-130 at ages
   9-13; LR2 44-47.5 at the age-17 edge; Suez 53.5 realized at 17) sit ABOVE the held
   curves — expect UP pressure on VLCC/Suezmax/LR2 mid-age anchors (war tape). Dry
   prints are mid-age-heavy at near-curve levels (Cape ~36.5-37.5 at 14-15; Kmax
   22-30.8 at 11-14) — expect small moves; PPMX gains 5 prints incl. its first young
   node (fit re-runs mechanically; the MARK_WIDE_NODES band re-derive WAITS for
   `ppmx_txn_refit` — young condition 1 of 2 met).
3. Any position flip: individually eyeballed (house rule). SB (PPMX 42.7% of levered
   NAV, the lone TIGHT BUY): band-invariance test per the 7/18 ruling — a band-edge
   that flips the read = cap territory; otherwise flag-not-cap stands.
4. TNK #4-5 close the stage-A-basis §3 owner gate; the OCEAN RHEA/AMIS/YARRA §I3
   upgrades close the 7/28 "next triage batch" pointer.
5. `date:` fields carry the print's SOURCE-ISSUE date (sentinel newest-promoted-print
   basis); TNK #4 carries 2026-02-15 (month-precision, noted on the row).
