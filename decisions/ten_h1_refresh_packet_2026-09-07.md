# TEN H1-2026 refresh — REPORT-DAY PACKET (prepared 2026-09-07 for Thursday 2026-09-10)

**Two premises corrected before anything else:**

1. **Pareto does not publish TEN.** A regex sweep over all 180 Pareto PDFs on disk returns
   zero Tsakos hits; `reconcile.py` already lists TEN in `APPROX_PNAV_TICKERS` and
   TICKER_NOTES.md:67 says so. The "89-day stale consensus pair" cannot be refreshed from
   Pareto — it is structurally APPROX (VIE-anchored). CLAUDE.md's exclusion list
   (NAT/ASC/CCEC/MPCC) is incomplete; TEN belongs on it.
2. **The notes-bearing 6-K will probably NOT land on 9/10.** Last year's H1 6-K (acc
   0001193125-25-225057, period 2025-06-30) was filed **2025-09-30** — three weeks after the
   results release. Expect a press release Thursday and the sheet-writable filing later. The
   edgar poll catches it; FILING-UNREADABLE now guards the image-only case.

**Price rebase — rule-determined, executes on report day, not before.** Watchlist row is
$37.14 / pnav 0.34 / fwd_pe 4.6 (as_of 2026-06-10). Last close 9/04 = $43.74 (+17.8%).
Option A (price only, WORKFLOWS.md:88-92) breaks the watchlist's own header rule (a price
never moves without pnav/fwd_pe from the same vintage) and lifts k_broker ≈1.25→1.47 — a
+0.22 second-difference that reds the drift gate. **Option B is the rule**: rebase to
preserve the anchor exactly as the 2026-06-10 fix did — price 43.74 · pnav 0.40 · fwd_pe
5.5 (43.74/8 EPS) — both still APPROX. If the H1 print resets NTM EPS, re-derive fwd_pe from
that. Valuation is unaffected either way (the pipeline values at the live close).

**Governance haircut in force:** 30% (§15 archetype; working band 30-36%; §15.7 review
2026-06-11). Tripwire at this refresh: pull the TCM related-party fees and add the
capitalized-fee drag per §15.7.

**Thirteen open items pre-filled** (Appendix A §2a): Ulysses cash/gain IN H1; Arctic +
Antarctic re-add as OWNED; WC composite re-derive; Mare Success NCI fork; shuttle extension
rate APPROX; LNG NB 19→20 with a new commitment figure; Anfield delivered July (subsequent
event); two 2006-built Suezmaxes sold 9/01 unnamed (NOT promotable; Alaska + Archangel
identity UNVERIFIED); data-kit Q2 deltas documented-not-applied; TCM fee-load; shares/
preferreds re-verify (F-3ASR 7/02 + Form 4s); $1.00 dividend confirm paid; data kit is
owner-supplied (tenn.gr WAF blocks the fetcher).

---
# APPENDIX A — report-day prep (verified USE WITH CORRECTIONS, none corrupting)

# TEN report-day prep (TRACK A) — prepared 2026-09-07, read-only

## 1. Consensus-pair rebase packet

**Premise check FAILED — Pareto does not publish a TEN row.** Walked every Shipping Daily on file: `inputs/research_pareto/2026/09/` holds 2026-09-01/02/03/04/07 (six PDFs incl. one CAPT company report); the 9/07 daily's share-price table lists 13 tanker names (Ardmore, Bruton, Capital Tankers, d'Amico, DHT, Frontline, Hafnia, INSW, NAT, OET, Scorpio, Teekay Tankers, TORM) and no Tsakos. A regex sweep (`Tsakos|\bTEN\b`) over all 180 PDFs under `inputs/research_pareto/2026/01..09/` returned **0 hits**; `inputs/market_data/pareto_share_prices.csv` (Jun-14 vintage) has 0 Tsakos rows; `inputs/research_pareto_other/` has no TEN report. The repo already records this: `TICKER_NOTES.md:67` "APPROX consensus_pnav (no Pareto; VIE anchor >1yr stale)"; `src/crude_tanker_fv/reconcile.py:69` `APPROX_PNAV_TICKERS = {"NAT","ASC","CCEC","TEN",…}`; `LIMITATIONS.md:313-320`. What would settle it: a Pareto daily or company report carrying a TEN P/NAV (none exists on disk), or an owner decision to adopt a different anchor (VIE).

**Current watchlist row** (`inputs/watchlist.yaml:128-149`): `current_price: 37.14` (NYSE close 10 Jun 2026), `consensus_pnav: 0.34` APPROX ("rebased from 0.40 with the $44→$37.14 price fix to PRESERVE the implied broker NAV anchor (~$110, VIE-stale)"), `consensus_fwd_pe: 4.6` APPROX ("Price $37.14 / EPS $8 = 4.6x"), `as_of: 2026-06-10` — 89 days stale. Implied broker NAV = 37.14 / 0.34 = **$109.24/sh** (ties to ten_log:3737 "broker NAV $109.24").

**Latest price** (`inputs/market_data/prices_daily.yaml:151-156`): `TEN: asof '2026-09-04T20:00:02+00:00', price: 43.74, prev_close: 43.28, day_change_pct: 1.06`. Note 9/07 is Labor Day (9/07 daily p.1: "US markets closed today for Labor Day"), so 9/04 is the last close. Drift vs watchlist: 43.74 / 37.14 − 1 = **+17.8%**.

**Rebase options (owner decision, not executable by me):**
- (A) WORKFLOWS.md:88-92 step 4 rule for APPROX names: "refresh the price leg only, keep the APPROX flags" → `current_price 43.74`, `as_of 2026-09-04`. Side effect: reconcile's broker NAV = 43.74/0.34 = **$128.65** (+17.8%), a pure artifact of the stale pnav.
- (B) The 2026-06-10 precedent (ten_log:3730-3736) preserved the anchor by rebasing pnav: 43.74/109.24 = **0.40**; fwd_pe on the same EPS basis 43.74/8 = **5.5**. Both stay APPROX. If the H1 print resets NTM EPS, re-derive fwd_pe from that instead of the $8 guidance (watchlist:145-148).
- Valuation is unaffected either way: the pipeline values at the live close (watchlist header lines 11-16; ten_log 9/01 auto entries show "Current price: $42.52" from prices_daily).

## 2. Report-day checklist (pre-filled)

**Event:** `inputs/earnings_calendar.yaml:198-207` — CONFIRMED, GlobeNewswire 3348799 (2026-08-20): "prior to the open of the market in New York on Thursday, September 10, 2026"; call 10:00 ET; `disclosure_type: 6-K (H1 report)`.

**(a) Open items / forks flagged for the H1 refresh**
1. **Ulysses (VLCC)** — HFS at carrying value inside the WC composite at Mar-31 (`ten_2026-Q1.yaml:25-27`, manifest:54-56); sale completed May-20 → "gain + ~$83M free cash land at the H1 refresh". Watch for a gross price: ten_log:3687-3691 "No gross price disclosed → NOT promotable … Watch the Q2 6-K for the gross figure" (a 2016-built VLCC print).
2. **Arctic + Antarctic** — chartered-in SLBs excluded at Q1; "repurchase agreed Apr-7-2026 → re-add as OWNED at the H1 refresh" (manifest:19-22, 78-81; prereg §3 line 81). Check debt for the repurchase financing.
3. **WC composite** ($174.654M, Other assets − Other liabilities, sheet:19-35) — "component re-derive at H1, TRMD-fork-1 style" (prereg §6 lines 121-122, 135).
4. **Mare Success NCI** $45.954M book via `preferred_equity` (sheet:90-98) — "NAV-basis derivation not disclosed-derivable … owner fork prereg §6.1".
5. **Shuttle extension rates** — "$60k/day … APPROX of 'increased rate' disclosed in the Q1 6-K subsequent events (April 23, 2026)" (sheet:144-147); `shuttle_contracted_book: 453100000`.
6. **New LNG newbuild** (ten_log:1481-1490, MB LNG Weekly 29): "expect the NB program to read 19→20 hulls with a NEW commitment figure (price from the H1 6-K, else NEWBUILD_PRICE_PENDING park)".
7. **Anfield (DP2 shuttle) delivered July 2026** (`outputs/news_digest_2026-09-07.md:294`) — post-Jun-30 subsequent event; at delivery it is off-curve at contracted book (§11.6), advances fall, Anfield debt ($111.8M agreed / $44.7M drawn, ten_log:3701-3703) draws.
8. **Two 2006-built Suezmaxes sold, announced 9/01** (digest M5, lines 283-322): "in excess of $100 million", no names, no price → "NOT promotable" (digest:442-444). The manifest's 2006 cohort is Alaska + Archangel (manifest:83-84) — identity UNVERIFIED until named. Post-Jun-30 → subsequent-events note only, not the Jun-30 snapshot.
9. **Data-kit Q2 deltas, documented not applied** (ten_log:3676-3696): Sola TS $25,651→$26,651; Dimitris P spot→TC $40k min; Alaska + Archangel rolled to spot-indexed TCs; Hercules I $140k "until … Hormuz is resolved", expiry Nov-26.
10. **§15 TCM fee-load tripwire** — "pull the TCM fees from the 20-F related-party note at the Q2 refresh and add the capitalized-fee-drag number per §15.7" (ten_log:2352-2356).
11. **Shares/preferreds** — 30,127,603 diluted at Dec-31 (sheet:78-80); Series E 4,745,947 / Series F 6,747,147 (sheet:84-87). EDGAR shows an F-3ASR shelf 2026-07-02 and Form 4s 7/10, 7/16, 8/17 (submissions JSON, fetched 9/07) — re-verify the count.
12. **Dividend** — $1.00 second semi-annual "declared for July 2026" (`dividend_policies/ten.yaml:6-8`); confirm paid.
13. **Data kit** — last reconciled kit is Jun-5 (ten_log:3637); tenn.gr WAF blocks agent fetch ("the WAF 403s the fetch service", ten_log:3639-3641; digest:288 "tenn.gr itself returned an empty body twice") → owner-supplied PDF.

**(b) Governance discount in force:** `governance_discount_pct: 0.30` (`ten_2026-Q1.yaml:129`). Rationale lines 101-128: first §15 case; controlled-shareholder structure + TCM related-party fees; ~19% payout ($1.50 vs ~$8 EPS); no buyback, $2.4B NB orderbook; family-held preferred slugs; "30% NAV haircut chosen to bring tool PW FV into the neighborhood of VIE Bullish $51.50"; applied at blend + strip terminal, not to `compute_nav`. §15.7 review 2026-06-11 (ten_log:2338-2360): "HOLD 30%, working band 30-36%", VIE-implied 36.3%, market ~53%.

**(c) Known gotchas:** ten_log:3716-3750 — "the 2026-06-05 watchlist entry read the Q1 6-K prose '~$44' as a live Jun-5 price … ~16% too high"; fix rebased pnav 0.40→0.34 and fwd_pe 5.5→4.6 so broker NAV stayed ~$110; process fix = `prices_daily.yaml`. Also: the manifest header's "14 conventional Suezmax" arithmetic slip that dropped two 2025 hulls (ten_log:3645-3658) — count hulls against the report; SEC Archives return 403 to an undeclared UA — use `edgar_poll.USER_AGENT` (`edgar_poll.py:52`).

**(d) What the H1 6-K must carry / its format:** Sheet writability needs the provenance trio `source_url` / `retrieved_at` / `filing_period_end` (`tests/test_quarter_coherence.py:187`; example `dht_2026-Q2.yaml:13-15`), condensed BS lines (cash, Other assets/liabilities, "Debt and other financial liabilities, net", advances), Subsequent Events note, debt schedule, plus the manifest `report_date` bump in the same commit (pair guard; `scripts/check_snapshot_advance.py`). **There is no `inputs/filings/TEN/` directory** (ls confirms; `inputs/filings/_manifest.json` lists none). Proxies: on disk, `inputs/research_issuer/ten/ten_q1_2026_ex991.htm` = 95,796 bytes, **1 `<img>` (logo), 12 tables, 16,202 text chars** — text HTML, but no Subsequent-Events heading and no fleet table. Fetched from EDGAR 9/07: the H1-2025 6-K (acc 0001193125-25-225057, filed **2025-09-30**, reportDate 2025-06-30, `d79040d6k.htm`) = 1,400,564 bytes, **0 `<img>`, 73 tables, 147,568 text chars**, inline XBRL, with "7. Long-term debt and other financial liabilities … Loans $1,683,624", "16. Subsequent Events", "Advances for vessels under construction 279,247"; H1-2024 (acc 0001193125-24-234389, filed **2024-10-08**) same shape (0 img, 79 tables). No per-vessel fleet table ("Fleet": 0 hits; vessel names appear only in loan notes) — hull-level detail comes from the PR/data kit. **Cadence warning:** no 6-K was filed between 2025-06-25 and 2025-09-30, so the 9/10 results release is not furnished on EDGAR that day; the condensed statements historically land ~3-4 weeks later. Pull the GlobeNewswire/tenn.gr PR on 9/10; expect the 6-K late Sept/early Oct.

**(e) Filings since 8/31:** `state/edgar_manifest.jsonl` (99 rows, 25 tickers) has **zero TEN rows**; EDGAR submissions JSON (fetched 9/07): newest TEN filing 2026-08-17 (Form 4), last 6-K 2026-05-22 — **nothing since 8/31**. The digest's "configured-but-unpolled" read (digest:296-303) is not supported by config: `edgar_poll.covered_ciks` reads `data_sources.yaml:201` (CIK 0001166663) and `RELEVANT_FORMS` (`edgar_poll.py:53-54`) excludes Form 4/144/F-3ASR; the poller's first manifest row is 2026-07-14, after TEN's last 6-K. Whether a TEN poll actually ran is UNVERIFIED (a `--dry-run` would settle it).
---
# APPENDIX B — verification

**VERDICT: USE WITH CORRECTIONS** — no corrupting error found; the premise (no Pareto TEN row), the price/vintage facts, the EDGAR facts and every recomputable number check out. Corrections are citation drift, one wrong claim about the ex991 proxy, one "UNVERIFIED" that the repo already settles, and one missed consequence of rebase option (A).

## 1. Citation spot-checks (12)

1. **Pareto premise — VERIFIED.** `inputs/research_pareto/2026/09/` holds exactly the six PDFs named; `pdftotext` of the 9/07 daily: line 49 "US markets closed today for Labor Day"; share-price table rows Ardmore, Bruton, Capital Tankers, d'Amico, DHT, Frontline, Hafnia, NAT, OET, Scorpio, Teekay Tankers, TORM — no Tsakos. Case-sensitive `Tsakos|\bTEN\b` over all 180 PDFs under `2026/`: **0 hits** (case-insensitive gets 6, all the English word "ten"). `pareto_share_prices.csv`: 0 Tsakos rows, max `report_date` 2026-06-11. Caveat: the sweep was 2026-only; `ten_log.md:3751-3765` records 5 Pareto free-text mentions 2025-01→2026-06 (one a Mar-2025 Suezmax disposal print, promoted) — none a P/NAV, so the conclusion stands. Its cited source `outputs/pareto_mentions_ten.md` **does not exist on disk** (ugrep: no such file).
2. **Watchlist row 128-149 — VERIFIED** verbatim (37.14 / 0.34 / 4.6 / as_of 2026-06-10; APPROX comments as quoted).
3. **prices_daily.yaml:151-156 — VERIFIED** (asof 2026-09-04T20:00:02Z, 43.74, prev 43.28, +1.06). `state/price_refresh.log` shows the 9/07 12:54Z refresh ran; TEN row unchanged = consistent with Labor Day close.
4. **earnings_calendar.yaml:198-207 — VERIFIED** (GlobeNewswire 3348799, 9/10 pre-open, 10:00 ET, `6-K (H1 report)`).
5. **`TICKER_NOTES.md:67` — WRONG line, correct text at :69.** `reconcile.py:69` VERIFIED; `LIMITATIONS.md:313-320` VERIFIED.
6. **`ten_log:3687-3691` (Ulysses "No gross price disclosed") — WRONG line; text is at 3677-3681.** `ten_log:3701-3703` (Anfield $111.8M/$44.7M) — WRONG, it is line 3699. `3716-3750` price-error entry VERIFIED (lines drift by ≤2). `2338-2360`, `1481-1490`, `3637-3658`, `3676-3696` VERIFIED.
7. **Sheet `ten_2026-Q1.yaml` — VERIFIED**: 19-35 WC composite (331,398−156,744=174,654 ✓), 76 advances 442,740,000 (comment :62 "Resolves the prior ~$400M [ESTIMATE]" — the log's 3701-3705 open flag is closed, no `[ESTIMATE]` red remains), 78-80 shares, 84-87 E/F, 90-98 NCI, 99 preferred_equity 333,282,000, 101-128 rationale, 129 `governance_discount_pct: 0.30`, 144-147 $60k APPROX.
8. **Manifest — VERIFIED**: 19-22 Arctic/Antarctic SLB + Apr-7 repurchase, 54-56 Ulysses removal, 78-84 cohort note + Alaska (age 20.1) / Archangel (20.2); `report_date: 2026-Q1` at :48. Prereg :81 / :121-122 / :135 VERIFIED.
9. **Digest 283-322 / 288 / 294 / 296-303 / 442-444 — VERIFIED** verbatim.
10. **`tests/test_quarter_coherence.py:187` — VERIFIED** (trio required for keys ≥ "2026-Q2"); `dht_2026-Q2.yaml:13-15` VERIFIED; `data_sources.yaml:201` CIK 0001166663 VERIFIED; `edgar_poll.py:52-54` UA + RELEVANT_FORMS VERIFIED (no Form 4/144/F-3ASR).
11. **EDGAR (re-fetched 9/07, declared UA) — VERIFIED**: newest 2026-08-17 Form 4; F-3ASR 2026-07-02; Form 4s 7/10, 7/16, 8/17; last 6-K 2026-05-22; nothing since 8/31. H1-2025 6-K acc 0001193125-25-225057 filed 2025-09-30 reportDate 2025-06-30; **no 6-K between 2025-06-25 and 2025-09-30** ✓; H1-2024 filed 2024-10-08 ✓. (H1-2025 byte/table counts not re-fetched — low stakes, unverified by me.)
12. **ex991 proxy — PARTLY WRONG.** Size 95,796 / 1 img / 12 tables / 16,204 text chars ✓. But **"no Subsequent-Events heading" is WRONG**: the file carries a "SUBSEQUENT EVENTS" section (Apr-7 repurchase of "two of its 2007-built suezmax tankers"; Apr-23 extension of "two 2013-built DP2 Shuttle tankers … at an increased rate … commence … second half of 2028 … more than $200 million in gross revenues"; May-20 sale of "a 10-year-old VLCC … about $83 million in free cash"). "No fleet table" ✓ (12 "fleet" hits are all prose). RECOVERABLE — and useful: the ex991 is the *source* for items 2, 5 and 12.

## 2. Recomputations (all tie)

43.74/37.14−1 = +17.77% ✓ · 37.14/0.34 = 109.24 ✓ · 43.74/0.34 = 128.65 ✓ · 43.74/109.24 = 0.400 ✓ · 43.74/8 = 5.47 ✓ · 4,745,947×25 + 6,747,147×25 = 287,327K ✓, +45,954 = 333,282K ✓ · shuttle 104.8+104.2+121.5+122.6 = 453.1 ✓ · 1−51.50/80.79 = 36.3% ✓ · 37.99/80.79 = 0.47 ✓ · 1.50/8 = 19% ✓. New bound the work could have drawn: ">$200M gross over up to 5 yrs × 2 hulls" ⇒ ≥ 200/(2×5×365×0.983) ≈ **$55.7k/day floor** at full term (higher if shorter) — the $60k APPROX is inside the disclosed envelope.

## 3. Snapshot integrity

- **Price/pnav/fwd_pe same vintage?** Currently yes — all three are 2026-06-10 derivations (none from a Pareto daily). **Option (A) breaks that pairing**: a 9/04 price against 6/10-vintage pnav/fwd_pe is exactly what `watchlist.yaml:11-16` forbids ("never the price alone"), while `WORKFLOWS.md:90-91` carves APPROX names out. The two rules conflict for TEN; the packet presents both options but does not name the conflict. Owner call.
- **MISSED consequence of (A)**: broker NAV $109.24→$128.65 against an unchanged tool NAV ($87.35, TICKER_NOTES:62) moves k_broker ≈1.25→1.47 — a **~+0.22 jump that will very likely red the drift gate (>0.05 second-difference)** and force a log annotation or ratify, for a number the packet itself calls an artifact. Option (B) is gate-neutral. Say so before the owner picks. (A `drift_gate` dry run against a scratch copy would confirm; not run here.)
- Post-Jun-30 items (Anfield July delivery, 9/01 two-Suezmax sale, Ulysses cash lands *in* H1 since May-20 < Jun-30) are routed correctly. Note Ulysses cash/gain is IN the Jun-30 statements, not a subsequent event — the packet's item 1 has this right.
- CMBT img_059 — not applicable to this track.
- No rumour dressed as a print; the 9/01 sale is correctly held NOT promotable.

## 4. What it missed

1. **"Whether a TEN poll actually ran is UNVERIFIED" — it is verifiable on disk and the answer is YES.** `state/edgar_poll.json["0001166663"]`: `bootstrapped: true`, `last_polled: 2026-09-07T13:08:42Z`, `watermark: 2026-05-22`, `seen_accessions` include 0001193125-26-236934 (the 5/22 6-K). The digest's "configured-but-unpolled" (digest:296-303) is refuted by state, not just config. Zero manifest rows = zero relevant forms since the poller's first run (ts min 2026-07-14T14:20Z), which EDGAR confirms. Also: the manifest's 25 tickers = 24 watchlist names + **PANL** (non-watchlist); TEN is the one watchlist name absent — the digest's arithmetic, not the packet's, but worth stating precisely.
2. **2006-cohort identity can be tightened by elimination**: the manifest's only Suezmaxes aged ≥19 are Alaska/Archangel; Arctic/Antarctic are 2007-built per the ex991. Unless the manifest ages are wrong, the 9/01 pair is Alaska + Archangel — still name it UNVERIFIED until the PR/6-K names them, but the checklist should pre-load their charter (data-kit: rolled to spot-indexed, ten_log:3686-3689) and dwt (163,250 / 163,216) so the exit is one edit.
3. **NB-count cross-foot**: the 9/01 PR's "26-vessel programme, 7 delivered" ⇒ 19 outstanding post-Anfield = Jun-5 kit's 19 − Anfield + 1 new LNG. That corroborates item 6, but whether the LNG hull sits in the Jun-30 snapshot depends on its contract date (MB Weekly 29 is dated 7/16) — the packet's "19→20 at H1" should be conditional on that date.
4. **`PLAN.md:140` already dockets "TEN alternative-anchor" as an open owner word** — the rebase packet is that decision; cite it so the owner sees it is not new.
5. **9/01 sale is not in `ten_log.md`** (no "3354219"/"2006-built" entry; only the digest) — the checklist should say the log entry is owed at the H1 refresh.
6. `outputs/pareto_mentions_ten.md` cited by ten_log:3753 is missing from disk — a broken provenance pointer for the promoted Mar-2025 print (not this track's deliverable, but flag it).

## 5. Error classification

| Item | Status | Class |
|---|---|---|
| ten_log 3687-3691 / 3701-3703, TICKER_NOTES:67 | wrong lines (true text at 3677-3681 / 3699 / :69) | RECOVERABLE |
| ex991 "no Subsequent-Events heading" | WRONG — section exists | RECOVERABLE (helps) |
| TEN poll "UNVERIFIED" | settled by `state/edgar_poll.json` | RECOVERABLE |
| Option (A) drift-gate consequence | omitted | RECOVERABLE, but decision-bearing |
| Watchlist-header vs WORKFLOWS conflict for APPROX names | unnamed | RECOVERABLE |
| All prices, dates, EDGAR facts, recomputed figures | VERIFIED | — |

Nothing here corrupts the deliverable; apply the six corrections and it is usable on 9/10.