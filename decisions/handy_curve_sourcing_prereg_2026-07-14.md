# Handy-Bulk (dry-bulk Handysize) — Option B sourcing prereg + wiring record · 2026-07-14

**Authority:** owner ruling 2026-07-14 on `handy_curve_decision_2026-07-14.md` — **Option B**
("go with Option B, only realistic solution until when/if we get more transaction prints in the
future"). This doc is the pre-registered sourcing step that ruling authorizes: node set with
citations, predicted validation bands AHEAD of wiring, then the wiring inventory. Class is
**un-anchored** (§9.9 semantics: k_broker on Handy-heavy names reads broker-premium-over-OUR-curve,
LNGC/container regime) until the re-fit condition below arms.

**Evidence run:** 4-agent sweep 2026-07-14 (workflow `wf_bc3c20c5-68b`: AR2025 extraction / MB
dry weeklies 24-28 / Pareto archive re-read / single-threaded web bench) + the xclusiv harvester
cache (`shipping_harvester/data/marks/xclusiv/*.json`, 2021Q3→2026Q3).

## 0. Two corrections the sweep forced (recorded before any number)

1. **The decision doc's "one print" was product-tanker** — Baltic Sapphire/Swift sit in the
   2025-06-13 daily's "Tankers:" section (generic ref $30M en-bloc; the $17.4M generic is 15Y
   MRs). Dry-Handy prints in the Pareto archive: **zero**. Corrected in the decision doc same day.
2. **The xclusiv "Handysize" row is the BULK-carrier row** — it tabulates with Cape/Kamsarmax/
   Ultramax; its TC column is BHSI-38k gross earnings (17,014 × 0.95 = 16,163 = Pacific Basin's
   published NET print, exact); its NB (30.6-31.0) matches 2343's actual 40k-Handy contract
   ($29.8M/hull) while ASC's actual product-Handy NB contract is $44.9M/hull. **Consequence
   flagged (NOT acted on here): Thread-1A wired this bulk row to the PRODUCT Handysize curve**
   (age-0 $40M→$36M, `prompt_resale.Handysize`, basis_status `resale-uniform`, AGE0_BASIS
   `xclusiv-resale`). Live NAV impact today ≈ 0 (Thread-1A's own analysis: HAFN Handy age-18,
   ASC age-11 — age-0 touches only the 0-5yr leg; ASC's product-Handy NBs are excluded from the
   Q1 snapshot as subsequent events). **OWNER QUEUE ITEM: revert product Handysize age-0 to a
   product-sourced mark (or $40M pending-sourceable) as its own attributable step.** Until ruled,
   the product curve keeps asserting equality against a bulk number — documented here, dated.

## 1. The node set (wired values) — all at the committed xclusiv 2026-06-22 vintage

Vintage discipline: the whole dry family's age-0 basis is the committed
`xclusiv_age_curve.yaml` extract (2026-06-22); Handy-Bulk wires to the SAME vintage (its
"Handysize" row = the bulk row per §0.2). The Jul-06/Jul-13 issues + four independent brokers
corroborate levels stable-to-firmer — cross-check matrix below.

| Node | Wired | Primary source (2026-06-22 committed) | Independent corroboration (Jul-2026) |
|---|---|---|---|
| dwt baseline | 38,000 · dwt_scaled | xclusiv/MB/Compass assessment basis 38k | 2343 owned avg 35,390 dwt (AR2025 p.28) · PANL 38.7k |
| newbuild_contract | **$30.5M** | xclusiv NB (Chinese yard) 2026-06-22 | MB DBW 24-28: 30.5 · Compass W28: 31.0 · Intermodal: 31.0 · bancosta Jun-avg 30.4 · **2343's own Dec-2025 JNS contract $119.2M/4 = $29.8M per 40k hull (AR2025 p.17)** |
| age-0 (prompt resale) | **$36.0M** | xclusiv Resale 2026-06-22 (= `resale.Handysize`, bulk row; AGE0_BASIS `alias:Handysize`) | Compass W28 36.0 · xclusiv W27/W28 36.0 · AST 35.5@40k · MB 34.5 |
| five_year_benchmark | **$29.5M** | xclusiv 5yr 2026-06-22 (Japan-built basis) | Compass 30.0 · MB 30.0 · Intermodal 30.5@37k · **Baltic Exchange S&P assessment $29.4M (bancosta W27, 03-Jul)** |
| ten_year_benchmark | **$23.3M** | xclusiv 10yr 2026-06-22 | Compass 23.0 · AST 23.5@37k · xclusiv W27/W28 24.0 |
| scrap_25yr | **$4.5M** [ESTIMATE] | LDT convention ~8.5-9.5k t × ~$480/LDT (container-sector precedent); no dedicated Handy demo print classified | demolition prints refine via sp_scan queue |
| scrubber_premium | 0 | no sourced Handy scrubber premium (rare fitment; African Piper the only scrubber print) | conservative-0 convention |
| eco_premium_pct | 0.0 | not separately evidenced at desk (eco prints command premia — lives in future fit) | conservative-0 |

Old-leg note (10yr→25yr linear, family convention): implies 15yr ≈ $17.0M vs broker 15yr quotes
$15.0M (xclusiv, 37k Japan) / $12.5M (AST, 32k) — the leg runs +13% above quotes at 15yr, within
the family's ±11% scatter on that leg (Supra +7%, Pana −11%) but at the high edge. 2343's fleet
(age ~13) prices on exactly this zone — the issuer-composite band check (§3) is the control.

## 2. Rates wiring

| Surface | Wired | Basis + source |
|---|---|---|
| `twelve_month_tc.Handy-Bulk` | **14,500** · as_of 2026-07-10 | MB Dry Bulk Weekly 28 (4-10 Jul): 1yr TC, 38k dwt modern Japanese, net of address comm — an EXPLICIT printed basis. Corroboration: Intermodal 1yr 13,500 @32k (≈14.4-15k dwt-scaled to 38k). NOT the xclusiv "tc" column (that is BHSI spot earnings, §0.2). No Handy FFA panel exists — refreshes on MB weekly, NOT the FFA OCR promote loop. |
| `historical_tce_means.Handy-Bulk` + `cycle_anchors.handy_bulk` | **12,850** | xclusiv BHSI-38k spot-earnings series median, 2024Q3→2026Q3 (9 obs: 12,730/10,427/11,052/11,449/15,130/13,432/12,842/17,014/16,960 → median 12,842). Same window-class as the family's 22-month archive medians → same `archive_22mo_median` token + the same "biased ELEVATED vs true long-run" §11.7.5 caveat. Cross-checks: 0.92 × supra anchor = 12,676; BHSI index avgs 2024/2025 (704/661 pts ≈ $12.7k/$11.9k at ~$18/pt) bracket it. Pareto dailies carry NO Handysize column (sweep-verified) — this is the honest substitute archive. |
| `spot_tce.Handy-Bulk` | **16,466** · as_of 2026-07-10 | BHSI 38k 7TC avg earnings, week-close 10-Jul-2026 (Baltic Exchange print via xclusiv W28 p.1; 13-Jul print 16,445 — HandyBulk republish — corroborates). Gross basis like the family's dry spot rows. |
| Scenario deck `handy_bulk` | **= supra_ultra × 0.90**, rounded to $10 | LOCKED derived basis. Observed spot/realized Handy÷Supra ratios cluster 0.87-0.92: BHSI/BSI 2025 avgs 10,580/11,630 = 0.910 (AR2025 p.20, net) · 2343 realized 1Q26 12,130/13,970 = 0.868 · wired anchors 12,850/13,930 = 0.9225. 0.90 = mid, slightly conservative. The MB 1-yr PERIOD ratio (14,500/19,250 = 0.75) is deliberately NOT the basis — strips model realized-TCE paths (spot-class), and the family strips are spot/FFA-derived. Identity is GUARD-TESTED (`test_handy_bulk_deck_is_supra_times_basis`) so any supra promotion that forgets handy REDS — the two surfaces cannot drift silently (the F-13/two-surfaces rule). |
| `class_routes.handy_bulk` | BHSI 38k (7TC composite) | minor-bulk/logs/parcelling basin; confidence low/very_low/very_low (no Handy FFA at any tenor). |
| `PARITY_BANDS` | ABSENT — deliberate | classes absent carry no registered band (unvalidated); registers at the P1a/P1b validation pass like the rest. |

Cycle read at wiring: 14,500 / 12,850 = **1.13×** (vs Supra 1.32×, Cape 1.49×) — Handy lags the
2026 dry rally in period space; coherent with MB's flat Handy 5yr through the 5 issues.

## 3. Predicted validation bands (registered AHEAD; computed below — the §9.9-style discipline)

**Band 1 — 2343 Handysize sleeve vs the issuer's own composite broker valuation
(vintage-matched).** AR2025 p.6 prints per-class composite values at 31-Dec-2025: Handysize 58
owned / avg 35,390 dwt / avg age 13 / **US$927.5M** (avg $15.99M/hull). Constructing the curve at
the CONTEMPORANEOUS Dec-2025 xclusiv nodes (2025Q4 cache 2025-12-22: resale 33.3 / 5yr 26.7 /
10yr 21.0; scrap 4.5) and valuing 58 hulls at age 13, dwt-scaled 35,390/38,000:
per-hull (21.0 − (21.0−4.5)/15×3) × 0.9313 = **$16.48M** → sleeve **$955.9M**.
**PREDICTED: within ±10% of $927.5M. COMPUTED: +3.1%. PASS.**
Same construction on the Supramax sleeve (xclusiv Ultramax 2025Q4: 10yr 24.6, scrap 6.5; 48
hulls, 58,790 dwt, age 13): $19.89M/hull → $954.9M vs issuer $1,013.8M = **−5.8%. PASS** —
the method lands inside ±10% on BOTH sleeves of the only issuer that publishes the answer.

**Band 2 — wired-vintage coherence.** At the wired 2026-06-22 nodes the same sleeve computes
$1,055M = +13.8% over the Dec-2025 composite; the gap must ≈ the observed 2026 YTD dry-value
rally. xclusiv Handy 10yr Dec→Jun/Jul: 21.0 → 23.3/24.0 = **+11-14%**; Pareto 2026-04-28: 5-yr
dry values "+~10% YTD". **PASS — the delta is the market move, not a construction artifact.**

**Band 3 — print-gap direction (documentation, not a gate).** The 17 dry-Handy prints below run
−8% to −30% under the wired curve mid-age (dwt-normalized) — the expected un-anchored signature
(broker quotes > transaction levels; every §9.9 dry fit moved its class DOWN). A future fit
should therefore LOWER 5yr/10yr toward prints; k_broker on Handy-heavy names will read HIGH
meanwhile. Stated now so nobody "fixes" it toward Pareto later.

## 4. The print sample (candidates, NOT classified, NOT fit — the re-fit fuel)

MB Dry Bulk Weekly issues 24-28 S&P tables (+ web-corroborated duplicates in Compass W28 /
Intermodal W27 / xclusiv W27-28 / bancosta W27 / AST W28), sub-45k bulkers, USD M:

| Vessel | dwt | Built | Price | Flags |
|---|---|---|---|---|
| Interlink Celerity + Solidity (en-bloc) | 40,112/40,098 | 2017 | 44.0 (22.0 ea) | eco |
| JNS Phoenix | 40,504 | 2025 | 34.1 | OHBS (Compass/AST Jul-13) |
| Atlantic Star | 37,065 | 2018 | 26.0 | eco, Oshima |
| African Piper | 34,365 | 2015 | 20.0 | eco + scrubber + logs |
| Darya Krishna | 34,000 | 2016 | 20.0 | AST commentary, late-Jun |
| Astro Propus | 38,271 | 2014 | 19.0 | Imabari |
| Dalarna | 35,958 | 2014 | 17.2 | eco |
| Tania | 37,188 | 2014 | 17.1 | eco, Ice 1C, DD due |
| Asahi Ocean | 32,085 | 2013 | 15.2 | semi-boxed |
| Maple Marina | 37,194 | 2012 | 14.3 | TC attached Sep/Dec-26 |
| Nordic Malmoe | 35,843 | 2012 | 13.7 | eco |
| Team View | 35,914 | 2011 | 13.7 | OHBS, surveys passed |
| Suzanna D | 37,205 | 2012 | 12.6 | |
| Lila Tochigi | 28,354 | 2014 | 12.5 | DD due |
| Beetle | 28,198 | 2012 | 12.6 | Imabari |
| Marina R | 37,785 | 2010 | 10.8 | TC attached 11/14mo |
| Woohyun Sky | 32,312 | 2010 | 10.5 | |
| Clacton/Eastbourne/Margate/Portsmouth (×4) | 40,000 | 2024 | 30.5 ea | May-26, AST commentary |
| Avra 1 | 32,597 | 2010 | 7.7 | logs |
| Sun Grace | 33,745 | 2004 | 7.4 | |
| Praetorius | 28,345 | 2008 | 8.6 | |
| HTK Lucky | 28,481 | 2003 | 6.0 | logs |

Per the never-auto-promote rule these are CANDIDATES: no `transactions/handy_bulk.yaml` is
created today (a transactions file with mis-classified rows silently moves a curve; human
classification per print — eco/gear/TC-attached/survey adjustments — is the §9.9 gate).

## 5. Re-fit trigger (registered at wiring, per the ruling's "when/if prints" branch)

`handy_bulk_txn_refit` in `reweight_triggers.yaml` — arming condition: **≥10 human-classified
in-window prints spanning ≥3 age nodes including at least one ≤6yr** (the age-4-7 hole is what
blocks a fit today; the MB flow at ~3 prints/week plausibly arms this by the Q3 refresh). On
fire: classify → `transactions/handy_bulk.yaml` → §9.9 fit → drift-gate loop → the class leaves
un-anchored semantics. Owner runs the promotion; the trigger only pages.

## 6. Wiring inventory (all landed this commit)

`vessel_value_curves.yaml` Handy-Bulk (nodes §1) · `scenario_inputs.yaml` (class_routes +
confidence + 4× handy_bulk scenario blocks ×0.90 + cycle_anchors.handy_bulk) ·
`historical_tce_means` / `twelve_month_tc` (+as_of) / `spot_tce` (+as_of) ·
`newbuild_contract_prices` (newbuild_contract + prompt_resale Handy-Bulk; invariant 30.5 < 36.0
holds) · `basis_status.yaml` Handy-Bulk resale-uniform · `loaders.ALLOWED_CLASSES` ·
`carveout.DRY_BULK_CLASSES` · `scenarios` dry map "Handy-Bulk"→"handy_bulk" ·
`AGE0_BASIS["Handy-Bulk"] = alias:Handysize` (reads the committed bulk row; §0.2 documents the
label) · `tests/test_handy_bulk_class.py` (statics lock · ×0.90 deck identity · routing/sleeve ·
gate-neutrality: no live watchlist manifest carries the class) · METHODOLOGY §11.7.11 ·
`reweight_triggers.yaml` trigger (§5). **Gate expectation: zero drift** — no watchlist name
routes Handy-Bulk; the suite's drift gate is the proof.
