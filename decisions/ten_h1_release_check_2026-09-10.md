# TEN H1-2026 release check — 2026-09-10 (report day; the 6-K has not landed)

**Source:** GlobeNewswire 3359616, "TEN, Ltd. Reports Profits for the First Half and Second
Quarter of 2026", 2026-09-10 09:15 ET. Not on EDGAR (the H1-2025 6-K lagged three weeks). The
rendered page could not be saved by curl (HTTP/2 stream error; HTTP/1.1 hung) — every figure
below came through three section-scoped fetches and was re-fetched verbatim by the verifier;
the Dec-31-2025 comparatives tie digit-for-digit to the on-disk Q1 ex991. **Save the rendered
page before any sheet write.** Verdict: USE WITH CORRECTIONS, nothing corrupting as written.

## The pair is NOT writable from the release — it waits for the 6-K

Release-sourceable with the provenance trio (source_url = the GlobeNewswire URL, retrieved_at
2026-09-10, filing_period_end 2026-06-30): cash 466,143k · working-capital composite 65,359k
(Other assets 286,240 − Other liabilities 220,881; the Q1 construction) · total_debt 2,102,177k
("Debt and other financial liabilities, net of deferred finance costs") · newbuild advances
470,050k. NOT sourceable: diluted_shares_outstanding (the release gives only the weighted
average 29,972,103; the Q1 sheet carries issued-less-treasury 30,127,603 — the gap is
restricted stock), the Mare Success NCI roll (45,954 + 4,176 Q2 NCI = 50,130 ASSUMES no Q2
distribution — unverified), the lease population (Arctic/Antarctic repurchase completion is
not in the release), the debt schedule (Anfield draw, Tenergy SL). The MANIFEST cannot be
built at all (no fleet table); the pair guard requires both in one commit. Sentinel posture:
STALE-BALANCE-SHEET TEN stands until the 6-K; FILING-LANDED pages when it stages.

## Subsequent events (audited first) — IN / OUT of 30 June

Ulysses (VLCC, sold May 20): IN — "Gain on sale of vessels (37,870)" in Q2/H1, no gross price.
Anfield DP (delivered 28 July, 10-year charter to a US oil major, "expected gross revenues
should approach $500 million" at maximum duration — an envelope, not a rate): OUT; its advances
sit inside 470,050. Alaska + Archangel (2006 Suezmaxes) "concluded ... in August 2026 ... net
proceeds of $100 million": OUT as a sale; an AGGREGATE, net, never split. **Open question for
the 6-K build (verifier): were they held-for-sale AT 30 June (MOA date)?** If so they are
off-curve at carrying value in the Q2 manifest, not on-curve — applying "keep in" without
checking would be CORRUPTING. July $1.00 dividend: OUT as cash (payable at 6/30 not disclosed).
Series E call intent for 28 May 2027: OUT. LNG NB #26 firm-up: contract date unverifiable here.

## Price rebase — option B, applied on the anchors of record

`prices_daily.yaml` 9/09 close: TEN 44.32 (no price typed from prose). Anchors of the
2026-06-10 fix carried forward unchanged: implied broker NAV 109.24 (= 37.14 / 0.34) → pnav
44.32 / 109.24 = 0.4057 → **0.41**; fwd P/E on the same $8 EPS basis → 44.32 / 8 = **5.5**.
Alternatives recorded, not applied (an anchor choice, not a rounding one): the "$110" anchor
the watchlist prose names gives 0.40; annualising the H1 EPS ($7.12, gains-inclusive) is not
an NTM figure — the $8 guidance basis stays until the 6-K or a data kit resets NTM. Both
remain APPROX (Pareto publishes no TEN row). Valuation unaffected (the pipeline values at the
live close); only the surface's TEN broker-NAV fields move on the next regen.

## The 13 packet items — what the release settled

Ulysses gain IN, no gross price (still not promotable) · Arctic/Antarctic NOT in the release
(completion unverified; "Vessels, net" +10,118 across a quarter of 46,295 depreciation is
consistent with additions, not evidence) · WC composite 65,359 writable, its components wait ·
Mare Success NCI roll unverified · shuttle extension rate still undisclosed · LNG #26 no
price (NEWBUILD_PRICE_PENDING park if the 6-K is silent) · Anfield OUT, debt draw → Note 7 ·
Alaska + Archangel named, $100M net aggregate · data-kit deltas still owner-supplied · TCM
fees: footnote definitions only (§15 tripwire: nothing moves the 30% haircut; the working band
30-36% stands; "$3.6 billion in minimum contracted revenue", up from $3.5bn) · shares:
weighted average only · dividend: $1.50 paid in 2026, next announced November · fleet: 64.0
vessels / 7,702k dwt at 30 June vs 64.0 / 8,003k at 31 March — the dwt drop is Ulysses out,
Anfield not yet in; 81 pro-forma = 64 + 19 NB − 2 sold.

## Corrections folded from the verification

$500M over 20 years is $68.5k/day, not $137k (the work's slip; not written anywhere) · the
Alaska/Archangel HFS-at-6/30 question flagged above · the 64.0 count settled by the dwt
bridge · pnav anchor choice stated · fwd_pe basis stated · "4 fields" vs "six numbers"
wording (cosmetic).

---
# APPENDIX A — the release check (agent, read-only)

# TEN H1-2026 report-day packet — run against the 2026-09-10 release (READ-ONLY)

**Source:** GlobeNewswire 3359616, "TEN, Ltd. Reports Profits for the First Half and Second Quarter of 2026", 2026-09-10 09:15 ET. No saved copy exists (`inputs/research_issuer/ten/` holds only the 20-F and the Q1 ex991). Raw curl failed (HTTP/2 `INTERNAL_ERROR`; HTTP/1.1 hung), so all release text below came through WebFetch in three section-scoped pulls. Fidelity check: every Dec-31-2025 comparative in the fetched balance sheet ties digit-for-digit to the on-disk Q1 ex991 (298,129 / 197,009 / 3,156,075 / 301,868 / 3,953,081 / 1,920,975 / 169,101 / 1,863,005), and the fetched EPS recomputes exactly (131,866k / 29,972,103 = 4.40; 213,534k / 29,972,103 = 7.12). Owner should still save the rendered page to the packet path before any sheet write. Not yet on EDGAR (consistent with the 2025 three-week lag). Release content treated as data.

## 1. Subsequent-events audit (post-30-June) — IN / OUT of the 30-June snapshot

| Event | Verbatim (section) | Snapshot |
|---|---|---|
| Anfield delivery + 10-yr charter | SUBSEQUENT EVENTS: "on July 28, 2026, TEN took delivery of the DP2 suezmax shuttle tanker *Anfield DP* from Samsung Heavy Industries Co., Ltd in South Korea, the third in a series of 12 DP2 shuttle tankers under construction at that yard. The vessel commenced a 10-year employment to a US oil major, with charter options to extend the charter until the vessel's 20th year anniversary. Assuming charterers employ the vessel to the maximum duration, the expected gross revenues should approach $500 million." | **OUT.** At 6/30 Anfield is still a NB: its advances sit inside "Advances for vessels under construction 470,050". No day rate disclosed ($500M is a max-duration envelope, not a rate). |
| Alaska + Archangel sale | SUBSEQUENT EVENTS: "in August 2026 TEN concluded the sale of two 2006-built suezmax tankers, the *Alaska* and *Archangel*, for net proceeds of $100 million." | **OUT.** Both hulls remain owned at 6/30. "Net proceeds" — an aggregate, no gross, no split. |
| Ulysses sale | CORPORATE STRATEGY: "The sale of the 2016-built VLCC *Ulysses* and the two 2006-built suezmax tankers *Alaska* and *Archangel*, are a testament to that approach." Income statement: "Gain on sale of vessels (37,870)" in both Q2 and H1 columns; narrative "(inclusive of $38 million capital gains)". | **IN** (closed May 20). Gain and cash are in the 6/30 statements. No gross price. |
| July dividend | CORPORATE AFFAIRS – COMMON STOCK DIVIDEND: "In July 2026, TEN distributed to common shareholders a second semi-annual dividend, amounting to $1.00 per share, following a $0.50 per share payment in February 2026. A total distribution of $1.50 per share in 2026." | **OUT as cash** (paid July). Whether it sat as a payable inside "Other liabilities 220,881" at 6/30 is NOT disclosed — 6-K item. |
| Series E call | CORPORATE AFFAIRS – SERIES E: "become redeemable at the election of the Company on May 28, 2027, and the Company currently expects that it may elect to redeem, all or a portion of … This disclosure does not constitute a notice of redemption". | OUT (2027 intent). Series E still outstanding at 6/30 (H1 "Effect of preferred dividends (13,500)" = E+F at $25 par exactly, by recompute: 118,649×9.25%/2 + 168,679×9.5%/2 = 13,500). |
| LNG NB order (MB Weekly 29, 7/16) | Not in prose. NB table row 26: "TBN | LNG Carrier | Q1 2029 | Under Construction | TBA" — the Q1 ex991 had this row as "Optional Vessel". | **Contract date UNVERIFIED** from the release; if MB's 7/16 date holds, OUT of 6/30. No price. |
| Arctic + Antarctic repurchase (agreed Apr-7) | Fetcher reports NOT PRESENT: "Arctic", "Antarctic", "repurchase", "leaseback". | **Completion UNVERIFIED.** Circumstantial only: "Vessels, net" rose 3,145,164 → 3,155,282 (+10,118) across a quarter carrying 46,295 depreciation and no NB delivery — consistent with ~$56M of additions, but not evidence. 6-K item. |
| Dividend timing | "intends to announce the first semi-annual dividend payment of 2027 in November 2026." | OUT. |

Also NOT PRESENT per the fetcher: Hercules, Series F, Tsakos Columbia / management fee (except the footnote definitions), buyback, Mare Success, commitment, Hormuz.

## 2. Writable now vs waits for the 6-K

**BALANCE SHEET DATA (In Thousands of U.S. Dollars), June 30, 2026 column, verbatim:** Cash 466,143 · Other assets 286,240 · Vessels, net 3,155,282 · Advances for vessels under construction 470,050 · Total assets 4,377,715 · Debt and other financial liabilities, net of deferred finance costs 2,102,177 · Other liabilities 220,881 · Stockholders' equity 2,054,657 · Total liabilities and stockholders' equity 4,377,715. Narrative cross-checks: "Total bank debt as of June 30, 2026 was $2.0 billion from $1.8 billion at December 31, 2025"; "TEN's cash balances increased to $466.1 million, $168.0 million higher than the end of December 2025"; "Weighted average shares 29,972,103" (basic and diluted, Q2 and H1).

Mapping to the ten fields of `ten_2026-Q1.yaml`:

| Field | Q1 value | Release-sourceable? | Note |
|---|---|---|---|
| `cash_and_equivalents` | 321,416,000 | **YES** → 466,143,000 | "Cash 466,143". Same line the Q1 sheet cites. |
| `working_capital_net` | 174,654,000 (331,398−156,744) | **YES as composite** → 65,359,000 (286,240 − 220,881) | Identical construction, same labels. Δ −109,295: Ulysses HFS carrying value left Other assets; Other liabilities +64,137 (July $1.00 dividend payable? NB payables?) — **component re-derive waits for 6-K** (item 3). The composite is writable; the explanation is not. |
| `total_debt` | 2,136,109,000 | **YES** → 2,102,177,000 | Same BS-carrying line (TRMD precedent). Δ −33,932 despite NB drawdowns (Ulysses debt repaid). Debt schedule / Anfield draw / Tenergy SL split → 6-K Note 7. |
| `lease_liabilities` | 0 | Unchanged by convention | Whether Arctic/Antarctic left the op-lease population → 6-K leases note. |
| `newbuild_capex_commitments` | 0 | Convention unchanged | But the LNG #26 firm-up (and any new price) is a NEW commitment figure — NEWBUILD_PRICE_PENDING park if the 6-K is silent. |
| `newbuild_advances_paid` | 442,740,000 | **YES** → 470,050,000 | "Advances for vessels under construction 470,050". Includes Anfield (IN at 6/30). |
| `diluted_shares_outstanding` | 30,127,603 (issued − treasury, 20-F) | **NO** | Release gives only the *weighted average* 29,972,103 (restricted stock excluded — "Income allocated to non-vested restricted stock (684)"). Q1 ex991 showed 29,971,603 on the same basis vs the sheet's 30,127,603, a 155,500 gap = restricted shares. Outstanding count at 6/30 → 6-K cover / equity note / F-3ASR 7/02. |
| `preferred_equity` | 333,282,000 (287,328 + 45,954 NCI) | **Partly** | E+F liquidation 287,328 re-confirmed by the 13,500 dividend tie. NCI: "Net income attributable to noncontrolling interest (4,176)" Q2, "(6,601)" H1; Q1 2,425 + 4,176 = 6,601 ties exactly. Book roll-forward 45,954 + 4,176 = 50,130 **assumes no Q2 distribution to Polaris — UNVERIFIED** → 6-K. |
| `governance_discount_pct` | 0.30 | Judgmental, see §6 | — |
| `shuttle_contracted_book` | 453,100,000 | **NO change from release** | Brasil/Rio extension rate still undisclosed; Anfield joins the off-curve book only at the Q3 refresh (delivered 7/28). |

**Verdict: the pair is NOT coherently writable from the release alone.** Sheet: 4 of 10 fields sourceable with the trio `source_url: https://www.globenewswire.com/news-release/2026/09/10/3359616/0/en/ten-ltd-reports-profits-for-the-first-half-and-second-quarter-of-2026.html`, `retrieved_at: 2026-09-10`, `filing_period_end: 2026-06-30`; but `diluted_shares_outstanding`, the NCI roll and the lease population need the 6-K. Manifest: the pair guard requires the `report_date: 2026-Q2` bump in the same commit, and the manifest cannot be built (no fleet table; Arctic/Antarctic ownership at 6/30 unknown; see §4). **Draft only a PARTIAL pre-fill** with the six release-sourced numbers above and every other line marked `[6-K PENDING]`; do not stage as `.yaml`.

## 3. The 13 packet items

1. **Ulysses cash/gain IN H1** — SETTLED: "Gain on sale of vessels (37,870)"; sale named in CORPORATE STRATEGY. Gross price NOT disclosed → still not promotable.
2. **Arctic + Antarctic re-add OWNED** — NOT SETTLED: terms absent from release (fetcher NOT PRESENT). 6-K leases/vessels note.
3. **WC composite re-derive** — composite WRITABLE (65,359); components WAIT.
4. **Mare Success NCI** — Q2 attributable 4,176 SETTLED; distributions/NAV-basis WAIT (owner fork unchanged).
5. **Shuttle extension rate** — NOT SETTLED; only Anfield's "$500 million" max-duration envelope (~$137k/day over 20 yrs at 100% — an envelope, not a rate; do not write).
6. **LNG NB 19→20** — CORROBORATED: NB table row 26 now "Under Construction" (Q1: "Optional Vessel"); row 25 named "NY KNICKS"; 26 − 7 delivered = 19 outstanding = 9 shuttle + 5 LR1 + 3 VLCC + 2 LNG. Price/contract date NOT disclosed → NEWBUILD_PRICE_PENDING.
7. **Anfield delivered** — SETTLED as post-quarter (7/28), 10-yr + options to 20th anniversary. Debt draw → 6-K.
8. **Two 2006 Suezmaxes** — IDENTITY SETTLED: "Alaska and Archangel … net proceeds of $100 million" (August). Aggregate, net, no split → not promotable; log entry owed.
9. **Data-kit Q2 deltas** — NOT SETTLED (no per-vessel employment in release); apply from the kit at the manifest write, cite the kit.
10. **TCM fee-load** — NOT in release (only the footnote that overhead "include[s] Management fees"). Available now from the 20-F on disk: "We paid Tsakos Energy Management aggregate management fees of $20.6 million in 2025, $19.9 million in 2024 and $19.5 million in 2023"; "Management fees, including those paid to third-party managers, totaled $23.3 million in 2025". H1 "Vessel overhead costs per ship per day $2,370" (vs $2,063). Compute the §15.7 drag from the 20-F, not the release.
11. **Shares/preferreds** — weighted avg 29,972,103 (+ vs 29,661,103 prior-year); E+F both outstanding (13,500 tie); Series E call intent 5/28/2027 is NEW. Outstanding count WAITS.
12. **$1.00 dividend paid** — SETTLED: "In July 2026, TEN distributed … $1.00 per share".
13. **Data kit** — not superseded; owner-supplied.

## 4. Fleet at 30 June

FLEET DATA, verbatim: "Number of vessels at end of period 64.0" (Q2 2026) vs 63.0 (Q2 2025); "Average number of vessels during period 63.5"; "Dwt at end of period (thousands) 7,702"; "Average age of fleet (years) 10.5". ABOUT TEN LTD.: "TEN's diversified pro-forma energy fleet currently consists of 81 vessels, totaling approx. 10.5 million dwt."

Reconciliation: Q1 manifest = 64 operated (56 owned on-curve + 4 shuttle + 3 chartered-in + 1 HFS Ulysses) + 19 NB. Expected 6/30: 64 − Ulysses = **63**, yet the release prints **64.0**. The Jun-5 kit's "63 in-water vessels, 7,701,519 DWT" matches the release's 7,702k dwt exactly, so the release's 64 is a counting-basis question (chartered-in included? a hull the kit omits?) — **UNRESOLVED without the 6-K fleet list**. Pro-forma 81 = 64 + 19 NB − 2 sold (Anfield's delivery is count-neutral) — ties. A Q2 manifest bump needs from the 6-K: (a) whether Arctic/Antarctic were owned at 6/30 (re-add as OWNED with their 2021 SLB carrying basis vs repurchase price), (b) confirmation Alaska/Archangel were still owned (yes per August sale — keep in, spot-indexed TCs per the kit), (c) Ulysses out of the WC composite, (d) per-vessel employment, (e) the 64-count decomposition. Ulysses gross price: **NOT disclosed** (only the $37,870k gain, single line; H1-2025 comparative gain 3,553). Alaska + Archangel: **are** the manifest's 2006 cohort (ages 20.1/20.2 at 3/31; release "2006-built"); "$100 million" is net and aggregate — **per-vessel split NOT disclosed; do not back-solve.** They stay in the Q2 manifest and leave at Q3.

## 5. Price rebase (option B, rule-determined)

`prices_daily.yaml:151-156`: `TEN: asof '2026-09-09T20:00:02+00:00', price: 44.32, prev_close: 43.52, day_change_pct: 1.84`. Anchor 37.14 / 0.34 = 109.24. **pnav = 44.32 / 109.24 = 0.4057 → 0.41** at the watchlist's 2-dp precision (implied broker NAV 108.10; 0.40 would imply 110.80 — state the rounding choice in the comment). **fwd_pe on the packet's $8 basis = 44.32 / 8 = 5.54 → 5.5.** Release-derived alternatives (run-rate, my arithmetic on release figures): H1 EPS 7.12 × 2 = 14.24 → **3.11x**; Q2 4.40 × 4 = 17.60 → 2.52x; ex the one-off gain (37,870k / 29,972,103 = $1.26/sh): H1 (7.12 − 1.26) × 2 = 11.71 → **3.78x**; Q2 (4.40 − 1.26) × 4 = 12.55 → 3.53x. The release gives no NTM guidance; recommend the ex-gain H1 run-rate 3.8x as the APPROX fwd_pe (comment: "H1-26 EPS 7.12 less $1.26/sh Ulysses gain, annualised; not a broker print"), with 5.5 recorded as the superseded $8-basis figure. Note the watchlist's "mgmt-guided Q2 $2.37" was beaten by $4.40 ($3.14 ex-gain). Both stay APPROX; `as_of: 2026-09-09`; valuation unaffected (pipeline already values at 44.32: 9/10 auto run "Current price: $44.32 … NAV / share: $88.16 … k_broker 1.34").

## 6. Governance §15 tripwire (band 30-36%)

Release: no related-party fee figure (footnotes only); no buyback; NB commitments not quantified ("26 vessels under construction, seven of which already delivered"; "$3.6 billion in minimum contracted revenue" — up from the 9/01 release's "$3.5bn"); preferreds: 13,500 H1 unchanged, plus the new Series E call intent (May 28, 2027 — would retire $118.6M of 9.25% paper, mildly positive for common). Payout: $1.50 on H1-annualised 14.24 EPS = **10.5%** (vs the 19% in the sheet rationale) — the payout-ratio driver has *worsened*, "increasingly reward its shareholders" is intent only. Net: nothing moves the haircut out of band; the case for the upper half (33-36%) strengthens on payout, the Series E call intent leans the other way. **HOLD 30% pending the 6-K fee note; revisit at the November dividend announcement.**

## 7. Prereg band / sentinel posture

**No prereg band** — the pair is not writable (§2). 6-K notes that unblock it: (1) Note 7 "Long-term debt and other financial liabilities" (schedule, Anfield draw, Tenergy SL); (2) Leases note (Arctic/Antarctic repurchase completion + lease population); (3) Vessels / Vessels held for sale note (Ulysses gross, Q2 additions); (4) Noncontrolling interest / Mare Success distributions; (5) Subsequent Events (LNG order date + price, Alaska/Archangel terms); (6) Equity note or cover share count; (7) Related-party (TCM) fees for §15.7; (8) any fleet list (last year: none — plan on the data kit). **Posture:** leave the edgar poll armed (CIK 0001166663 is bootstrapped, watermark 2026-05-22); FILING-LANDED pages ticker·form·accession on arrival (`sentinel.py:740-762`), expected late Sept/early Oct per the 2025 lag. Meanwhile stage the partial pre-fill as a draft, write the owed ten_log entries (9/01 sale + this release), and rebase the watchlist vintage per §5 as its own commit.
---
# APPENDIX B — verification

**VERDICT: USE WITH CORRECTIONS** — every quoted release figure re-fetched and verified verbatim; no price typed from prose (44.32 traces to `prices_daily.yaml:151-156`, verified); no corrupting error *as written* (nothing staged). Two arithmetic/derivation slips, one missed cross-check that settles the 64.0 puzzle, and one unflagged double-count trap in the manifest plan.

## 1. Figures (3 independent WebFetch pulls, 2026-09-10 ~13:00 ET; page still not saved to disk — `inputs/research_issuer/ten/` holds only the 20-F + Q1 ex991)

- **Balance sheet, June 30 2026 column — all VERIFIED verbatim:** Cash 466,143 · Other assets 286,240 · Vessels, net 3,155,282 · Advances 470,050 · Total assets 4,377,715 · Debt and other financial liabilities, net of deferred finance costs 2,102,177 · Other liabilities 220,881 · Stockholders' equity 2,054,657. Dec-31 comparatives tie digit-for-digit to on-disk Q1 ex991 (independently re-checked).
- **Income statement — VERIFIED:** Gain on sale of vessels (37,870) Q2 and H1; H1-2025 comparative (3,553); NCI (4,176)/(6,601); preferred (6,750)/(13,500); restricted stock (684)/(1,108); net to common 131,866/213,534; EPS $4.40/$7.12; weighted average 29,972,103 vs 29,661,103. Recomputes tie (131,866/29,972.103 = 4.3996; 213,534/… = 7.1245).
- **Narrative — VERIFIED verbatim:** "Total bank debt as of June 30, 2026 was $2.0 billion from $1.8 billion at December 31, 2025" (FIRST HALF); "TEN's cash balances increased to $466.1 million, $168.0 million higher than the end of December 2025" (FIRST HALF); Q2 "(inclusive of $38 million capital gains)" (Q2 SUMMARY — the H1 paragraph says "(including $38 million in capital gains)"); Anfield sentence incl. "third in a series of 12", "20th year anniversary", "$500 million" (SUBSEQUENT EVENTS); "in August 2026 TEN concluded the sale of two 2006-built suezmax tankers, the Alaska and Archangel, for net proceeds of $100 million" (SUBSEQUENT EVENTS); Series E May 28, 2027 + "does not constitute a notice of redemption" (CORPORATE AFFAIRS – SERIES E); "$1.00 per share … $1.50 per share in 2026" + "intends to announce the first semi-annual dividend payment of 2027 in November 2026" (COMMON STOCK DIVIDEND); "26 vessels under construction, seven of which already delivered"; "$3.6 billion in minimum contracted revenue"; "81 vessels, totaling approx. 10.5 million dwt"; NB row 25 "NY KNICKS", row 26 "TBN | LNG Carrier | Q1 2029 | Under Construction" (Q1 ex991 row 26 = "Optional Vessel" — VERIFIED on disk).
- **FLEET DATA — VERIFIED:** 64.0 / 63.5 / 7,702 / 10.5 (label is "Average age of fleet at end of period (Years)" — trivial paraphrase).
- **Fetcher NOT-PRESENT list** (Arctic, Antarctic, Hercules, repurchase, leaseback, buyback, Series F, Mare Success, Tsakos Columbia, Hormuz, commitment) — reproduced by my own fetch, but this is fetcher absence on both sides; the rendered page has still not been opened by anyone. Save it before any write.
- **Repo citations VERIFIED:** prices_daily 44.32/43.52/1.84 asof 2026-09-09; 9/10 03:39Z auto run ($44.32, NAV $88.16, k_broker 1.34) at ten_log:15-30; 20-F "$20.6 million in 2025, $19.9 million in 2024 and $19.5 million in 2023" and "Management fees, including those paid to third-party managers, totaled $23.3 million in 2025"; digest:291 "in excess of $100 million", :293 "$3.5bn"; MB LNG Weekly 29 (2026-07-16) at ten_log:1518-1524; Q1 ex991 weighted avg 29,971,603 and Vessels, net 3,145,164; `sentinel.py:736-762` FILING-LANDED; `test_quarter_coherence.py:186-189` trio; `state/edgar_poll.json` watermark 2026-05-22 (last_polled 2026-09-10T17:20Z); `NAV_FIGURE_ESTIMATE_QUEUE = {"cmbt","hafn"}` (ten out) — figure-provenance queue clear.
- **Computed figures, all recomputed correct:** 0.4057, 108.10, 110.80, 5.54, 3.11x, 2.52x, $1.2635, 11.71, 3.78x, 12.55, 3.53x, 13,499.8, 65,359, −109,295, +64,137, −33,932, +10,118, 10.5%, 50,130, 6,601 tie, 81 = 64+19−2.
- **WRONG (computed):** §3 item 5 "~$137k/day over 20 yrs at 100%" — $500M/(20×365) = **$68.5k/day**; $137k/day is the 10-year figure. Not written anywhere → RECOVERABLE.

## 2. Subsequent events
IN/OUT calls all correct (Ulysses IN; Anfield, Alaska/Archangel sale, July $1.00, Series E intent, Nov-26 announcement OUT; LNG contract date and Arctic/Antarctic completion unverifiable from the release). Nothing post-6/30 missed. **Missed pre-6/30 question:** the Alaska/Archangel MOA date. The 9/01 PR announced a sale that "concluded" in August; if the MOA was signed before 6/30, the pair was **held-for-sale at 6/30** — carried inside Other assets (the Ulysses precedent, `ten_2026-Q1.yaml:25-27`) and OUT of Vessels, net. §4(b) "keep in, spot-indexed TCs" would then double-count them (on-curve in the manifest AND in the WC composite). Release is silent → 6-K Vessels-held-for-sale note decides. RECOVERABLE now (manifest not staged); **CORRUPTING if (b) is applied as written.**

## 3. Writable-vs-waits
Correct: the four release-sourced fields (cash, WC composite, total_debt, advances) are verbatim BS lines with identical labels to the Q1 sheet; shares/NCI roll/leases correctly held. "$100 million" is kept aggregate and net, never split — correct. Minor: §2 says "4 of 10 fields" then "six release-sourced numbers" — reconcile the count. Note the WC composite writable-now claim inherits finding 2: if Alaska/Archangel are HFS inside Other assets 286,240, the composite is still numerically right but its manifest counterpart changes.

## 4. The 13 items
All statuses hold, with: item 5 arithmetic (finding 1); item 8 add "HFS-at-6/30 status UNVERIFIED" (finding 2); item 9 the release's own numbers settle the count question the work left open — Q1 ex991 FLEET DATA prints **64.0 vessels / 8,003k dwt** at Mar-31; the H1 release prints **64.0 / 7,702k** at Jun-30: Δdwt = −301k ≈ one VLCC (Ulysses 299,999+) with no addition, and both average-vessel figures (63.5 Q2 and H1) are consistent only with 63 at end (64 all quarter would print Q2 avg 64.0). The 64.0 end-count is internally inconsistent with the release's own dwt/average series — expect **63 owned/operated at 6/30**, per the kit. RECOVERABLE, resolves the "UNRESOLVED" in §4.

## 5. Price rebase / governance
No prose-typed price. Two derivation notes, both RECOVERABLE: (a) pnav 0.41 uses the back-solved anchor 109.24; the watchlist comment of record says "37.14/110 = 0.34" — on the $110 anchor 44.32/110 = 0.403 → **0.40**, so 0.40 vs 0.41 is an anchor choice, not a rounding choice; present both. (b) fwd_pe 3.8x annualises H1 ex-gain — the release carries no NTM guidance, and Q2 TCE $46,100 is a spike quarter; the packet's "re-derive from the reset NTM EPS" condition is not met by an annualisation. Owner call; label as run-rate, not NTM. §6 HOLD 30% is sound; payout 10.5% is on gain-inclusive EPS (ex-gain 1.50/11.71 = 12.8%) — same conclusion.

## Error classification
| Finding | Class |
|---|---|
| $137k/day (should be $68.5k/day) | RECOVERABLE (not written) |
| Alaska/Archangel HFS-at-6/30 unflagged; "keep in" | RECOVERABLE now; CORRUPTING if applied |
| 64.0 vs 63 settled by dwt 8,003→7,702 + averages | RECOVERABLE (improves) |
| pnav anchor 109.24 vs 110 → 0.41 vs 0.40 | RECOVERABLE, owner choice |
| fwd_pe annualisation ≠ NTM | RECOVERABLE, owner choice |
| "4 fields" vs "six numbers" | RECOVERABLE, cosmetic |
| All release figures, subsequent-events routing, aggregate handling, repo citations | VERIFIED |