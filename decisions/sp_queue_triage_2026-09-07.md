# S&P print queue triage — 2026-09-07 (verified SAFE TO USE)

**Four unreviewed candidates, none promotable, no draft rows.** The queue closes with the
owner's one command, `sp_scan --mark-reviewed` (it writes the scan state under
`transactions/`, an ask-tier surface — the auto-mode classifier blocked the agent from
running it). Run it before the next 13:07 UTC ingest chain, or re-read the queue first so a
fresh 9/08 hit is not acked blind. It marks reviewed = cumulative (232), does not scan, does
not advance the cursor, and touches no transactions YAML; the FLEET-TRANSACTION flag clears.

| # | Candidate | Disposition | Reason |
|---|---|---|---|
| 1 | 9/01 VLCC | OUT-OF-SCOPE | false key — the "$95,000/day" CAPT rate clause, not a sale |
| 2 | 9/01 Suezmax 2028 resale | OUT-OF-SCOPE, already dispositioned 9/01 | routed to resale-level evidence (sp_promotion_round_2026-09-01.md); never acked |
| 3 | 9/02 VLGC | OUT-OF-SCOPE + DUPLICATE | newbuild orders, no per-vessel split; hulls already recorded |
| 4 | 9/07 VLCC prompt resale ~$200m | RUMOUR | unnamed hull, "talk"/"rumours", buyer unnamed ("entities from Iraq"), Hormuz premium-distorted |

---
# Triage detail (verified)

# Track B — S&P print queue triage (2026-09-07)

## Why the file shows 1 line but the report counts 4

`outputs/sp_print_candidates.md` is rewritten on every scan (`run_scan` → `output_path.write_text`, `src/crude_tanker_fv/sp_scan.py` ~L336), so it holds only the latest run's hits: line 3 "Scanned 1 reports (2026-09-07 → 2026-09-07); 1 candidate sentences". The "4" is the sentinel's `candidates_cumulative − candidates_reviewed` = 232 − 228 (`inputs/market_data/transactions/_scan_state.json` L63-64; `sentinel.py` L504-510; `outputs/weekly_report_2026-09-07.md` L23). Counter trail: 228 after the 8/31 `--mark-reviewed` (commit 27ee3bf) → 230 (0f506ce, 9/01 scan, 2 hits) → 231 (c1c03f0, 9/02 scan, 1 hit) → 232 (working tree, 9/07 scan, 1 hit). The 9/03 and 9/04 dailies were scanned with 0 hits (`state/rocketchat_ingest.log` L18052-18109); I re-verified by running the pure `extract_sp_candidates()` on both PDFs → `[]` (no state written). The three older unreviewed sentences are recovered from `git show 0f506ce:outputs/sp_print_candidates.md` (L10, L14) and `git show HEAD:outputs/sp_print_candidates.md` (L10).

## Triage table

| # | Candidate (scan date · keyed class) | Class | Disposition | Reason |
|---|---|---|---|---|
| 1 | 9/01 · VLCC | (false key: the "$95,000/day" CAPT rate clause) | OUT-OF-SCOPE / already dispositioned | Same sentence as #2; VLCC keyword fires on a rate remark, not a sale |
| 2 | 9/01 · Suezmax | Suezmax, 2028 delivery (age 0) | OUT-OF-SCOPE (resale evidence) — already dispositioned 9/01, not acked | `decisions/sp_promotion_round_2026-09-01.md` L14-17 routed it to resale-level evidence; recorded in `suezmax.yaml` L198 (Bristol doc-row notes). Reviewed counter never advanced |
| 3 | 9/02 · VLGC | VLGC | OUT-OF-SCOPE (newbuild orders) + DUPLICATE (aggregate of filed per-vessel figures) | No per-vessel split in the sentence; the hulls are already recorded (below) |
| 4 | 9/07 · VLCC | VLCC prompt resale (age 0) | RUMOUR | Unnamed hull, "talk"/"rumours", ~$200m, premium-distorted (Hormuz delivery); buyer unnamed ("entities from Iraq") |

**Promotable: none. Draft rows: none.**

## Per-candidate detail

**#1/#2 — 9/01 daily** (`inputs/research_pareto/2026/09/2026-09-01_…527926.pdf` p1), verbatim: "Brokers are reporting that Delta Tankers of Greece has acquired a 2028 suezmax from DH Shipbuilding for $107m. Unclear who the seller is, but we note that companies like Exmar, Atlas Maritime, NAT and Swiss Maritime all have suezmax orders at the yard matching that delivery date." A forward-delivery resale, seller unknown, no hull name; age 0 sits outside the [3,17] fit window (`suezmax.yaml` L161-179 convention: `newbuild_resale`, `in_fit: false`). The 9/01 round already recorded it as resale-level evidence beside Bristol (`suezmax.yaml` L198: "Sits beside the 9/01 Pareto print (Delta Tankers acquires a 2028-delivery Suezmax resale from DH Shipbuilding at $107M)") and routed the same sentence's "1Y TC at $74.5k/day" to Stage-B inventory (decision doc L18-21). Nothing further to do; only the ack is owed.

**#3 — 9/02 daily** (`…2026-09-02_…528191.pdf` p1), verbatim: "This would be Dorian's second newbuild order this year; having ordered a single 90k VLGC from Hyundai Heavy in June. Delivery for that ship will be in July 2029 and the company paid a price of $115m • Dorian has sold four VLGCs this year (2014-15 built), for total proceeds of almost ~$340m." Preceding bullet: Hanwha 3× 88k cbm VLGCs "said to be paying $116m per vessel … Delivery will be around 2030". Two parts: (i) the $115m/$116m figures are yard contracts, not S&P — the transactions files touch only mid-age anchors (`_template.yaml` L3-5); (ii) "four VLGCs … ~$340m" is an aggregate with no per-vessel split → no back-solve (CLAUDE.md 2026-06-09). The underlying hulls are already in the repo: Cobra $81.9M net in `vlgc.yaml` L60-76 (in fit); Constellation $85.6M net and Corsair $80.8M recorded as owner-gated marks-trail candidates in `decisions/lpg_log.md` L1080-1084, deferred to the Nov-13 `lpg_v1_lock_rerun` (L2280); Clermont "no agreed price disclosed" (L1075). Note VLGC IS a fitted class — the 9th §9.9 class (`METHODOLOGY.md` L2424) — so the task's list of 8 is one short; but the LPG re-fit is owner-gated, so no queue action lands in `vlgc.yaml` today.

**#4 — 9/07 daily** (`…2026-09-07_…528948.pdf` p1), verbatim: "Rumours of a ~$200m resale deal for a VLCC were out on Thursday, and this morning Tradewinds is also suggesting that this may be a Dynacom vessel (Procopiou) acquired by 'entities from Iraq'. Dynacom has 2x VLCCs to be delivered from New Times and CSS Tianjin over the next month or so – reported to have a yard price of ~$115m each. According to the reports, the deal is said to involve vessel delivery on the inside of Hormuz, which obviously requires a premium". Buyer is NOT named — only "entities from Iraq" (TradeWinds-attributed, in quotes); Dynacom is the suggested SELLER ("may be"), not confirmed; hull unnamed; price is "talk". Even a firm print would be age-0 (`newbuild_resale`, outside the window — cf. `vlcc.yaml` L111-117) with a `prompt_premium`/`in_fit: false` treatment (`_template.yaml` L23-26): it can document, never set the curve. The 9/03 (Thursday) daily has no mention (keyword sweep of that PDF: none). Pareto's own read: "The last 'clean' resale transaction was ~$163m paid by Trafigura back in May … We currently use $175m in our NAVs … we do not believe it's completely relevant". Side find: no Trafigura ~$163m May resale row exists in `vlcc.yaml` (grep) — UNVERIFIED whether the May daily names the hull; settle by grepping `inputs/research_pareto/2026/05/` for "Trafigura" before treating it as a doc-row candidate.

What would firm #4 into a doc-row (still `in_fit: false`): a named hull, a confirmed buyer/seller, a dated firm price from a broker weekly (MB/xclusiv) or issuer disclosure. Until then it stays a watch item (already carried as W1 in `outputs/news_digest_2026-09-07.md` L449-459).

## `sp_scan --mark-reviewed` semantics (`sp_scan.py` L548-559, L248-257) — not run

- Reads `_scan_state.json`, takes `candidates_cumulative` (currently 232) and merge-writes `candidates_reviewed: 232`, preserving `last_scanned_report_date` (2026-09-07), `tanker_period_signals`, and stamping `updated_at`. Prints "marked reviewed at 232 cumulative candidates".
- Does NOT scan, NOT advance the cursor, NOT touch `outputs/sp_print_candidates.md` or any transactions YAML. Local-only.
- Effect: sentinel check #10 computes unreviewed = 232 − 232 = 0 → the FLEET-TRANSACTION flag (weekly report L23/L64) clears.
- Timing caveat: it acks whatever the cumulative count is at run time. The ingest chain runs ~13:07 UTC daily (`state/automation_runs.log`); run the ack before tomorrow's chain, or re-read the queue first, so a fresh 9/08 hit is not acked unseen.
- Both `_scan_state.json` and the queue file are already uncommitted automation-state changes (`git status`: M); the ack rides the same routine `commit_drift.sh` absorb (`scripts/commit_drift.sh` L4, L62).

Owner's one command (from repo root): `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.sp_scan --mark-reviewed`
---
# Verification

**VERDICT: SAFE TO USE** — every load-bearing citation checks out; the triage dispositions (no promotions, no draft rows) are correct; no rumour is dressed as a print and nothing age-0 is routed onto a curve. Corrections below are cosmetic, none corrupting.

## 1. Citation spot-checks (12)

| # | Claim | Result |
|---|---|---|
| 1 | Queue file rewritten each run, `sp_scan.py` ~L336 | VERIFIED (actual `output_path.write_text` at **L343**; "~" covers it) |
| 2 | `_scan_state.json` L63-64: cumulative 232 / reviewed 228 | VERIFIED (`"candidates_cumulative": 232`, `"candidates_reviewed": 228`) |
| 3 | `sentinel.py` L504-510 unreviewed = total − reviewed → FLEET-TRANSACTION | VERIFIED |
| 4 | Counter trail 228 (27ee3bf) → 230 (0f506ce) → 231 (c1c03f0) → 232 (tree) | VERIFIED via `git show <c>:_scan_state.json` (HEAD 217cef5 also 231/228) |
| 5 | Older sentences at `0f506ce:…sp_print_candidates.md` L10/L14 and `HEAD:…` L10 | VERIFIED — L10/L14 are the merged CAPT+Delta sentence keyed VLCC and Suezmax; HEAD L10 is the Dorian VLGC sentence |
| 6 | 9/03 and 9/04 scans → 0 hits (`rocketchat_ingest.log` L18052-18109) | VERIFIED: "scanned 1 reports -> 0 candidates … cursor advanced to 2026-09-03" and same for 09-04 |
| 7 | 9/01 PDF verbatim (Delta Tankers / DH Shipbuilding / $107m / Exmar, Atlas, NAT, Swiss Maritime) | VERIFIED (pypdf, `…527926.pdf` p1) |
| 8 | 9/02 PDF verbatim (Hyundai 90k VLGC, July 2029, $115m; four VLGCs 2014-15 built, ~$340m; Hanwha 3× 88k cbm $116m, ~2030) | VERIFIED (`…528191.pdf`) |
| 9 | 9/07 PDF verbatim (Rumours ~$200m … Dynacom … 'entities from Iraq' … New Times / CSS Tianjin ~$115m … inside Hormuz; Trafigura ~$163m May; $175m in NAVs; "not completely relevant") | VERIFIED (`…528948.pdf`) |
| 10 | 9/03 daily contains no mention | VERIFIED — 0 hits for Dynacom / resale / $200m / Iraq / Procopiou / Hormuz in `…528520.pdf` |
| 11 | `suezmax.yaml` L161-179 `newbuild_resale` convention; L198 Bristol note "Sits beside the 9/01 Pareto print … $107M" | VERIFIED |
| 12 | `lpg_log.md` L1075 Clermont "no agreed price disclosed"; L1080-1084 Cobra $81.9M / Constellation $85.6M / Corsair $80.8M owner-gated; L2280 `lpg_v1_lock_rerun` Nov-13; `vlgc.yaml` L60-76 Cobra $81.9M filed net; `METHODOLOGY.md` L2424 "9th §9.9 class"; `_template.yaml` L3-5 mid-age-only + L23-26 prompt_premium/newbuild_resale; `vlcc.yaml` L111-117 FRO NB resale `in_fit: false`; `decisions/sp_promotion_round_2026-09-01.md` L14-21; weekly report L23 "4 unreviewed" + L64 FLEET-TRANSACTION: 1; `news_digest` L449-459 W1; `commit_drift.sh` L4 | ALL VERIFIED (drift list `scripts/drift_files.txt` L11/L13 carries both S&P state files — the "rides commit_drift" claim holds) |

## 2. Recomputation
- 232 − 228 = **4** unreviewed: correct, and matches the weekly report's count.
- `--mark-reviewed` path (`sp_scan.py` L554-559): reads `candidates_cumulative` (232), calls `save_scan_state(last_scanned_report_date, extra={"candidates_reviewed": 232})`; `save_scan_state` (L248-256) does `prior.update(extra)` then stamps `updated_at` — `tanker_period_signals` preserved, no scan, no queue-file/YAML write. Post-ack unreviewed = 0. Confirmed by code read.

## 3. Snapshot integrity
- No price, pnav, fwd_pe or NAV figure is moved or proposed. No resale/NB figure is routed onto any fit (both age-0 items are explicitly `in_fit: false`-class). The ~$200m is treated as talk, buyer unnamed, seller "may be" — correctly NOT a print. The Dorian "~$340m" is correctly refused as an aggregate (no back-solve). Not a CMBT/TEN track; img_059 not touched.

## 4. Corrections (all RECOVERABLE, none change a disposition)
1. **Ingest-chain timing "~13:07 UTC daily"** is imprecise: `state/automation_runs.log` shows rocketchat-ingest at 14:09 (9/03), 14:08 (9/04), 13:07 **and** 14:00 (9/07). Say "13:00-14:10 UTC"; the operational advice (ack before tomorrow's chain, or re-read the queue first) stands.
2. **Trafigura ~$163m May resale — I ran the suggested settle-check**: 18 May Shipping Daily PDFs in `inputs/research_pareto/2026/05/`, **zero** "Trafigura" hits. The Pareto claim is therefore not sourced in the repo (only `vlcc.yaml` L90 has a Trafigura row — a 2019-built at ~$103M, different vessel). Remains UNVERIFIED; a broker weekly (MB/Compass) or TradeWinds item naming the hull would settle it. Not a doc-row candidate today. Note the 9/07 text also says "for a vessel delivering in Q3" (omitted from the write-up; immaterial).
3. **L-number nit**: write_text is L343 not ~L336; `--mark-reviewed` arg is L548-551, handler L554-559.

## 5. What it missed (bearing on the deliverable, not the S&P queue)
- **9/07 daily, same page: SBLK Athens dual-listing, offering up to 4.4m shares (vs ~112m) at max $29.52, ~9% discount, ~0.89x Pareto NAV; "price range announced tomorrow"** (`…528948.pdf` p1, verbatim). Not an S&P print — but it is a share-count/NAV-per-share event for a name with a pinned flip margin (SBLK −8.48 per the 9/01 close). Out of Track SP scope; should be handed to whichever track owns SBLK before the 9/08 range print.
- My independent sale-verb sweep of 9/02-9/07 found no S&P print the regex dropped (9/03 KCC block sale and 9/04 Diana-sells-GNK-shares are equity trades, correctly 0 hits). Pareto 9/02 also notes "recent VLGCs sold have been ~10% above our generic quotes" — sentiment only, nothing promotable.

## 6. Bottom line
Dispositions #1-#4 stand. The owner's single command is correct as written and is the only state change owed; nothing else in this triage should touch a transactions YAML.
---
# Addendum 2026-09-10 — the fifth candidate (9/09 daily), dispositioned before the ack

| # | Candidate | Disposition | Reason |
|---|---|---|---|
| 5 | 9/09 · MR, Japanese-built 2018, "$45.5m to Greek buyers with a drydock due before YE"; Pareto "We had her at $31.6m" | UNNAMED — watch, not promotable | no hull name, buyer unnamed; a firm print needs the hull + a dated broker weekly (MB/xclusiv) or issuer disclosure. The $45.5m vs Pareto's $31.6m gap is itself the note: MR mid-age prints running well above broker marks — cross-check at the next MR curve read, never a curve input on an unnamed hull |

Ack runs after this addendum: cumulative 233 → reviewed 233.
