# TEN 2026-Q2 shadow build — 2026-09-18 (6-K-based; the H1-2026 filing landed 2026-09-17)

**What this is.** The results-landed SHADOW of the TEN Q2 pair, rebuilt on the STATUTORY
interim statements. The two drafts (`inputs/balance_sheets/ten_2026-Q2.yaml.draft`,
`inputs/fleet_manifests/ten.yaml.draft`) were rewritten from the H1-2026 6-K and valued by
`scripts/shadow_regen.sh TEN 2026-Q2` in a throwaway worktree of HEAD `e8e23cb`. Nothing live
was written; the live tree still values TEN on the 2026-Q1 pair.

**This SUPERSEDES the 2026-09-11 release-based shadow** (`decisions/ten_shadow_build_2026-09-11.md`,
commit `884cbfb`), which read WOULD-HOLD with six fields unverified. The 6-K landed 2026-09-17
(refresh-trigger recorded in `decisions/filings_triage_log.md` and `decisions/ten_log.md`
2026-09-18), so step 3 of the task — "skip if unchanged since" — does not apply: a new source
landed after the drafts' commit.

**VERDICT (one line, repeated at the end): WOULD-HOLD** — on TWO blocking items, not six.
`shuttle_contracted_book` (453,100 $K, about 16% of gross NAV) still rests on an APPROX
$60,000/day extension rate and an as-of-2026-03-31 strike, and the newly-CITED $2,233,409
newbuild commitment is an owner methodology fork that a shadow must not wire. One guard reds
(the pre-enumerated mechanical pin).

**Shadow headline:** NAV/sh 88.16 → **91.91** (+3.75); FV 61.8 → 64.32; EV% 17.6 → 22.4;
position BUY (undervalued) and tier GOVERNED-WIDE unchanged; balance_sheet_vintage 2026-Q1 →
2026-Q2. **The band is HIT** (§6). The bridge is verified against the run, not merely explained (§5).

---

## 1. Sources

| Source | Locator | Retrieved |
|---|---|---|
| **TEN H1-2026 interim financial statements, Form 6-K** (PRIMARY) | EDGAR accession **0001193125-26-394366**, filed **2026-09-17**, period ended 2026-06-30 (unaudited). Staged: `inputs/filings/TEN/0001193125-26-394366_6-K_d67788d6k.htm` (from `state/edgar_manifest.jsonl`, staged 2026-09-17T20:20Z) | 2026-09-18 |
| — R2 Consolidated Balance Sheets | `https://www.sec.gov/Archives/edgar/data/1166663/000119312526394366/R2.htm` | 2026-09-18 |
| — R3 Balance Sheets (Parenthetical) | `…/R3.htm` | 2026-09-18 |
| — R12 Right-of-use assets and lease liabilities [Note 4] | `…/R12.htm` | 2026-09-18 |
| — R13 Vessels [Note 5] | `…/R13.htm` | 2026-09-18 |
| — R20 Commitments and Contingencies | `…/R20.htm` | 2026-09-18 |
| — R24 Subsequent Events | `…/R24.htm` | 2026-09-18 |
| — R34 Transactions with Related Parties (Details Narrative) | `…/R34.htm` | 2026-09-18 |
| — R38 Vessels (Details Narrative) | `…/R38.htm` | 2026-09-18 |
| — FilingSummary.xml (R-number index) | `…/FilingSummary.xml` | 2026-09-18 |
| H1/Q2-2026 results release (secondary; superseded as authority) | GlobeNewswire 3359616, 2026-09-10; `inputs/research_issuer/ten/2026-09-10_ten_h1_2026_results_pr.txt` | on disk 2026-09-11 |
| Q1-2026 6-K ex 99.1 (comparatives / prior convention) | acc 0001193125-26-236934, filed 2026-05-22 | on disk since 2026-07-15 |
| FY2025 20-F (comparatives / prior convention) | acc 0001193125-26-144027, filed 2026-04-06 | on disk since 2026-07-15 |

**Reading mechanics — the FRO precedent of 2026-09-17 applied.** The staged primary document is a
1.3MB single-file inline-XBRL exhibit whose body is one ~94k-token line and is **unreadable by the
Read tool**. Every figure in this report was therefore read from the EDGAR **R-renderings of this
same accession**, fetched 2026-09-18. The `decisions/ten_log.md` 2026-09-18 arrival entry quotes the
same figures; **this build did not transcribe that entry** — each figure was re-fetched from the
R-rendering and independently re-footed (CLAUDE.md "absence isn't evidence" / open the original).

**Price basis:** the shadow values at HEAD's `prices_daily.yaml` vintage — **52.55 in BOTH
scorecard rows**, so no price drift sits inside any delta below.

## 2. Subsequent-events audit (done FIRST, per the snapshot rule)

The 6-K Subsequent Events note (R24) and Vessels note (R13) REPLACE the release prose as authority.

| Event | Verbatim / cited | 6/30 snapshot |
|---|---|---|
| Ulysses (2016-built VLCC) sale | R13: "On May 20, 2026, the Company sold its VLCC tanker *Ulysses,* for net proceeds of $106,427, realizing a gain of $37,870." | **IN** — before the snapshot. Proceeds inside Cash; carrying value has left the WC composite; no fleet row. NET only, no gross price → **not promotable**, no back-solve. |
| **Arctic + Antarctic repurchase** | R13: "On May 28, 2026 and June 11, 2026, the Company acquired the two suezmaxes *Arctic* (Argon Shipping Co.) and *Antarctic* (Alinda Enterprises Inc.), respectively (Note 4)." R12: repurchased "at a purchase price of $20,000 each, net of the seller's credit amount of $4,207.5 for each vessel"; RoU $48,362 and lease liability $39,999 derecognized, "recognized both vessels as fixed assets". | **IN — OWNED AT 6/30.** Both dates precede 2026-06-30. **This REVERSES the 2026-09-11 shadow's conservative OUT.** Rows re-added (§4). |
| Delos T + Dion MR deliveries | R13: delivered 2026-01-12 and 2026-02-12, "for an aggregate cost of $95,797". | **IN** — on-curve since Q1. Aggregate only, no per-vessel split → not promotable. |
| Anfield DP (DP2 shuttle) delivery | R24: delivered **2026-07-28**. | **OUT** — a newbuild at 6/30; instalments inside Advances 470,050; joins `shuttle_contracted_book` at Q3. |
| **Archangel sale** | R24: **2026-08-14**. | **OUT** — after the snapshot; owned at 6/30, row stays. |
| **Alaska sale** | R24: **2026-08-26**. | **OUT** — after the snapshot; owned at 6/30, row stays. |
| Held-for-sale at 6/30 | R2 carries **no vessels-held-for-sale caption**; R13 carries **no held-for-sale sentence**. | **NONE HFS at 6/30** — resolves the 9/11 judgment call **in its favour**, now cited (§9.4). |
| Series F preferred dividend | R24: $0.59375/share paid 2026-07-30. | **OUT** as cash. |
| Common dividend | R24: $1.00/share paid 2026-07-30, record date 2026-07-23. | **OUT** as cash — but **ACCRUED at 6/30**: dividends payable 30,126 inside the WC composite (§3). |
| Series E preferred dividend | R24: $0.57812/share paid 2026-08-28. | **OUT** as cash. |
| Second LNG carrier firm-up | R20 counts **two LNG carriers** among twenty hulls under construction at 6/30. | **RESOLVED — firm at or before 6/30.** The 9/11 draft's 19-hull orderbook was one short. No price disclosed. |
| Impairment review | R13: "As of June 30, 2026, and December 31, 2025, this review did not indicate an impairment charge." | No carrying-value haircut. |

R24 states the Company evaluated subsequent events other than those disclosed through the issuance
date; nothing else material is reported.

## 3. Sourced figures (sheet, $K unless stated)

| Field | 2026-Q1 | 2026-Q2 draft | Citation, or the UNVERIFIED reason |
|---|---:|---:|---|
| `source_url` / `retrieved_at` / `filing_period_end` | — | 6-K primary-doc URL / 2026-09-18 / 2026-06-30 | The Q2-on ingest-provenance trio. |
| `cash_and_equivalents` | 321,416 | **466,143** | R2: "Cash and cash equivalents 463,989" + "Restricted cash 2,154". Same construction as the Q1 single "Cash" line. Dec-31 comparative 293,312 + 4,817 = 298,129 ties to the 20-F. |
| `working_capital_net` | 174,654 | **65,359** | R2 composite, **now decomposed at component level** (the 9/11 UNVERIFIED tag CLOSES): Other assets 286,240 = current (616,258 − 466,143 = 150,115) + non-current (342 + 1,700 + 15,233 + 91,270 + 27,580 = 136,125); Other liabilities 220,881 = current (440,197 − 250,376 = 189,821) + non-current (8,224 + 22,726 + 110 = 31,060). **Both foot exactly**; 286,240 − 220,881 = 65,359. |
| `total_debt` | 2,136,109 | **2,102,177** | R2: current portion 250,376 + "Long-Term Debt and Lease Obligation" 1,851,801. Dec-31 comparative 301,734 + 1,619,241 = 1,920,975 ties to the 20-F. |
| `lease_liabilities` | 0 | **0** | **Now verified, not assumed.** R12: the only operating lease at 6/30 is Sakura Princess, RoU **$1,700** — equal to R2's "Current portion of obligations under operating leases 1,700", so it nets to zero inside the composite. Arctic/Antarctic finance lease **derecognized** on repurchase (R12). |
| `newbuild_capex_commitments` | 0 | **0** | The LOCKED advances-only convention (OFF_CONVENTION_QUEUE). The remaining commitment is now CITED at **2,233,409** (R20) — an **owner fork**, not a sheet fix (§9.1). |
| `newbuild_advances_paid` | 442,740 | **470,050** | R2: "Advances for vessels under construction 470,050". Dec-31 comparative 301,868 ties to the 20-F. |
| `diluted_shares_outstanding` | 30,127,603 | **30,127,603** | **UNVERIFIED tag CLOSES.** R3 parenthetical: 30,805,776 issued / **30,127,603 outstanding** / 678,173 treasury, $5.00 par, 60,000,000 authorized — identical at Dec-31-2025, i.e. no H1 issuance or buyback. Issuer-stated at the snapshot date. |
| `preferred_equity` | 333,282 | **337,458** | E 4,745,947 + F 6,747,147 shares issued, both unchanged (R3) × $25.00 = 287,328; **NCI 50,130 taken DIRECTLY from R2** ("Non-controlling Interest 50,130"; 43,529 at Dec-31). **The distribution-leg UNVERIFIED tag CLOSES** — the 9/11 roll landed on the issuer's own figure; 45,954 is dead. 287,328 + 50,130 = 337,458. |
| `governance_discount_pct` | 0.30 | **0.30** | Judgmental HOLD. **The driver is now quantified for the first time** (R34) — see §9.2. Not moved in a shadow. |
| `shuttle_contracted_book` | 453,100 | **453,100** | **STILL UNVERIFIED — the binding blocker.** The 6-K carries no per-vessel shuttle day rates, so the Brasil/Rio **$60,000/day extension rate remains an APPROX** and the NPV is still struck as-of 2026-03-31 (§9.3). |
| `held_for_sale` | absent (0) | **absent (0)** | Now cited: no R2 caption, no R13 sentence (§9.4). |

Manifest header fields: `report_date` 2026-Q2; `on_curve_total` 56 → **58**; `crude_sleeve_count`
37 → **39**; `newbuild_orders_q2` 19 → **20**; `avg_age_crude` 9.55 → **10.05** (392.05 / 39);
`total_in_water_at_6_30` **63**; `spot_coverage_pct.Suezmax` 0.143 → **0.125**.

## 4. Fleet changes (2026-Q1 manifest → 2026-Q2 draft)

- **Rows: 56 → 58.** Arctic and Antarctic **RE-ADDED** as owned steel on the R13 acquisition dates —
  exactly the re-add the 9/11 draft pre-enumerated (56 → 58, crude 37 → 39, Suezmax 14 → 16,
  direction +). Ages are the pre-removal rows (Antarctic 19.0 / Arctic 19.2, verified to be on the
  same 2026-03-31 vintage — commit `4e0a9f3` removed the rows without re-dating any hull) rolled
  +0.25 to 19.25 / 19.45. dwt 163,216 both (pre-removal row); **not NAV-moving** — crude classes are
  flat-per-class, not `dwt_scaled` (§11.7.10-11).
- **Valuation basis for the pair: ON-CURVE at the txn-anchored Suezmax mark, NOT at the $20,000
  repurchase price.** The repurchase was explicitly "at prices below current fair market value"
  (Q1 6-K), so it is a bargain exercise, not a market print — §9.9 does not admit it, and it is
  **not promotable** to the S&P queue.
- **Alaska + Archangel: rows STAY on-curve**, now on three cited legs (sale dates 2026-08-14 /
  2026-08-26 after the snapshot; no R2 HFS caption; no R13 HFS sentence). The −$2.04/sh
  double-count flip the 9/11 draft sized does **not** fire.
- **Ulysses**: no row (sold 2026-05-20); its carrying value is now out of the WC composite too.
- **Anfield DP**: not a row (newbuild at 6/30).
- **Chartered-in population at 6/30 is Sakura Princess ALONE** — Arctic and Antarctic have left it.
- **Fleet cross-foot now ties exactly.** 58 owned on-curve + 4 shuttle off-curve + 1 chartered-in =
  **63 operated**, matching the June-5 data kit's 63 in-water hulls / 7,701,519 DWT, the release's
  "Dwt at end of period 7,702" (thousands) and its "Average number of vessels during period 63.5".
  The 9/11 shadow could only assert this tie; with the pair owned rather than chartered-in it
  closes. The release's printed "Number of vessels at end of period 64.0" remains contradicted by
  its own dwt and average series — **no hull is added on the printed count**.
- **Employment: Q1 values carried throughout, UNVERIFIED (shadow).** The 6-K has no fleet or
  employment table of any kind. Kit deltas (ten_log 2026-06-11) deliberately NOT applied — this is
  an ATTRIBUTION choice, so a strip-only change does not fold into the balance-sheet-swap bridge.
- **`spot_coverage_pct.Suezmax` 0.143 → 0.125** — 2 of 16 spot (Dimitris P, Decathlon). This is not
  an invented figure: **0.125 on 16 hulls is exactly the value this file carried before the
  2026-07-15 reconciliation removed the pair** (commit `4e0a9f3`), so the re-add restores the
  sourced value. Live land: 0.188 once the kit deltas are applied.

## 5. Shadow vs committed (from the SHADOW-JSON block; HEAD `e8e23cb`, `manifest_used: draft`)

| Field | Committed (live) | Shadow | Delta |
|---|---:|---:|---:|
| `nav_per_share` | 88.16 | **91.91** | **+3.75** (+4.3%) |
| `fv` | 61.8 | **64.32** | +2.52 |
| `ev_pct` | 17.6 | **22.4** | **+4.8pp** |
| `position` | BUY (undervalued) | BUY (undervalued) | unchanged |
| `confidence_tier` | GOVERNED-WIDE (subreason mixed) | GOVERNED-WIDE (subreason mixed) | unchanged |
| `balance_sheet_vintage` | 2026-Q1 | **2026-Q2** | advanced |
| `blend_fv` | 59.49 | 62.06 | +2.57 |
| `gap_pct` (vs broker NAV 128.17) | −31.2 | −28.3 | +2.9pp |
| `fv_low` / `fv_high` | 45.87 / 82.53 | 48.31 / 85.19 | +2.44 / +2.66 |
| sleeves (crude / product / lng $/sh) | 41.39 / 12.67 / 7.74 | 43.56 / 12.84 / 7.92 | +2.17 / +0.17 / +0.18 |
| `price` | 52.55 | 52.55 | none (same vintage) |
| `sanity` | n-a | n-a | TEN carries APPROX P/NAV (Pareto publishes no TEN row); tool NAV 91.91 vs broker 128.17 = −28.3%, well inside ±50% |
| `weight_sign_stable`, `ev_pct_family_min/max` | true, 3.2 / 17.6 | null, null / null | the weight-family sidecars are not regenerated inside the shadow worktree (`scripts/regen.sh` runs them; the shadow runs the pipeline alone) — mechanical, not a build defect |

**NAV bridge, verified against the run** (CLAUDE.md 2026-08-08: verify the run's own breakdown; a
satisfying explanation is not a verified one). Balance-sheet legs ($K): cash **+144,727** · WC
**−109,295** · debt −33,932 (adds **+33,932**) · advances **+27,310** · preferred/NCI **−4,176** →
**+92,498 = +$3.07/sh**. Age roll on the 56 carried hulls (§4 of the 9/11 shadow, unchanged):
**−$1.61/sh**. Arctic + Antarctic re-add: the residual is **+$2.29/sh = $69.0M for the pair**, which
lands inside the 9/11 pre-enumeration of $68.2–72.1M (+$2.26 to +$2.39/sh) — the two hulls at
19.25 / 19.45 years on the txn-anchored Suezmax curve.
**88.16 + 3.07 − 1.61 + 2.29 = 91.91 vs observed 91.91** ✓ exact.

Drift-gate reading for the live land: NAV +4.3%, EV% **+4.8pp** — over the 2pp annotation threshold,
**and this document is the annotation**. No band flip (BUY unchanged), tier unchanged. `gap_pct`
moves +2.9pp on a level basis; k_broker on its **second difference** is what the gate reads, and a
one-off vintage advance of this kind is a level move, not an acceleration.

## 6. Band check — **HIT**

The band was pre-registered **before this build**, in `decisions/ten_log.md` 2026-09-18 (the
arrival entry, written on the filing's landing and explicitly ahead of any sheet build): *"The
open-item envelope on the shadow's 89.61 narrows from roughly 87.4–92.0 to roughly **91.7–92.0** on
the two resolutions above, before the commitment question; BUY and GOVERNED-WIDE are insensitive
across it."*

**Observed NAV/sh 91.91 — inside [91.7, 92.0].** HIT, by +0.21 off the low edge and −0.09 off the
high edge. Position **BUY** and tier **GOVERNED-WIDE** are unchanged, as pre-registered. This is
also a hit against the finer arithmetic prediction (89.61 + 2.26…2.39 = 91.87…92.00).

## 7. Guard verdicts (shadow worktree)

```
[shadow] guards: 1 failed, 27 passed, 9 xfailed in 20.84s
[shadow] FAILED tests/test_quarter_coherence.py::test_balance_sheet_basis_summary_lagging_and_current
```

- The single red is the **pre-enumerated mechanical pin**: `tests/test_quarter_coherence.py`
  asserts `s["lagging"] == {"TEN": "2026-Q1"}` — TEN is pinned as the Q1-lagging specimen "until its
  H1 sheet lands". With the draft resolving as `ten_2026-Q2.yaml` the lagging set becomes `{}`.
  **Not a build defect**; the live land must rotate the pin (as CMBT's was on 2026-09-10). The live
  tree is untouched.
- **Two provenance guards red on the first pass and were FIXED, not suppressed** — recorded because
  the fix is the point:
  - `test_manifest_provenance.py::test_no_unbacked_verification_claims` — the line
    "convention unchanged, and now VERIFIED rather than assumed" carried a bare claim word with no
    same-line citation (the guard is **per-line**; my first fix put the accession on the *following*
    line and still red). Resolved by putting the citation on the claim's own line.
  - `test_manifest_provenance.py::test_every_estimate_flagged_nav_figure_is_queued` — the
    related-party line "$228.1M. R34 also discloses ESTIMATED FUTURE MANAGEMENT FEES PAYABLE of"
    tripped MONEY + `payable` context + `ESTIMATED` keyword with no same-line citation, which would
    have demanded TEN re-enter `NAV_FIGURE_ESTIMATE_QUEUE` (it left 2026-07-15). Resolved by citing
    the note and period on that line. **TEN stays out of the figure queue.**
- Pipeline ran clean (the only `[shadow] pipeline:` line is the unrelated READ-FLIP STROBE for CMDB
  and GNK); the SHADOW-JSON block printed, which only happens after a successful pipeline run.
- The full pytest suite was NOT run (outside this task's shell allowlist); the 9 xfails are the
  standing queue xfails.

## 8. What the 6-K closed, relative to the 2026-09-11 shadow

| 9/11 open item | Status 2026-09-18 |
|---|---|
| Arctic/Antarctic ownership at 6/30 | **RESOLVED — owned** (R13 dates), *against* the conservative default. Per-vessel price cited off the R12 note prose. |
| Alaska/Archangel held-for-sale at 6/30 | **RESOLVED — not HFS** (R24 dates + no R2 caption + no R13 sentence). The non-conservative call was right. |
| `diluted_shares_outstanding` | **RESOLVED** — issuer-stated 30,127,603 (R3). |
| NCI distribution leg | **RESOLVED** — 50,130 taken straight off R2. |
| `working_capital_net` at component level | **RESOLVED** — both composites decompose exactly. |
| Second LNG carrier firm at 6/30? | **RESOLVED — yes** (R20: twenty hulls, two LNG). Price still undisclosed. |
| Newbuild remaining commitment | **CITED** at 2,233,409 (R20) — and thereby promoted from an absence to an **owner fork** (§9.1). |
| Shuttle book re-strike / extension rate | **STILL OPEN** — the 6-K has no shuttle rates (§9.3). |
| Per-vessel employment at 6/30 | **STILL OPEN** — no fleet table in the 6-K (data kit is the resolution path). |

## 9. Judgment calls the owner-present build must rule on

**9.1 (FIRST, and the largest) `newbuild_capex_commitments` — 0, or net the $2,233,409?**
R20 now CITES, for the first time, a remaining contracted commitment of **$2,233,409** on twenty
hulls (228,339 rest-of-2026 / 723,029 2027 / 1,127,374 2028 / 154,667 2029 — the legs sum exactly),
against advances of 470,050. That is roughly **$74/share of gross obligation** on 30,127,603 shares
which this NAV does not net. The sheet keeps **0** because that is the locked advances-only
OFF_CONVENTION the name has always carried, and moving it inside a shadow would silently swing NAV
by the single largest leg on the name. This is the TEN instance of the GSL/CMBT/BWLP commitment-net
question under §3.1/§9.6 (newbuilds at delivered market LESS remaining commitment). **Not sized
here** — a sensitivity needs a run with the convention switched, which is live-land work.
Note the CLAUDE.md gate is now satisfied on its own terms: §9.6 wiring requires the name's
commitment/advance to be OUT of `NAV_FIGURE_ESTIMATE_QUEUE`, and this filing sources the figure.

**9.2 `governance_discount_pct` 0.30 — the §15 driver is quantified for the first time.**
The 9/11 shadow recorded "the release carries no related-party fee figure". R34 now supplies them
for H1-2026 ($K): Tsakos Energy Management fees **14,659** (H1-2025: 10,217, **+43.5%**), of which
supervisory services 2,171; **incentive awards 5,000** (H1-2025: 3,000, +66.7%); Tsakos Shipping
and Trading chartering commission **6,602** at a stated **1.25%** rate, technical services 1,034,
delivery commission 250; Argosy Insurance **9,036**; AirMania Travel **3,432** — about **40,013 of
H1 related-party outflow**, roughly **$80M annualised**, against H1 net income of $228.1M. R34 also
discloses contracted future management fees of 13,843 (2026) / 27,702 (2027) / 29,136 (2028) /
30,114 (2029) / 30,108 (2030) / 119,521 (2031-2035) ≈ **250,424** committed to the manager.
The §15.7 working band is **30-36%**. This evidence points to the **upper half**, but the haircut is
judgmental and **a shadow does not move a judgmental NAV lever** — 0.30 is held so the owner rules on
a clean comparison. Revisit with the November 2026 dividend announcement.

**9.3 `shuttle_contracted_book` 453,100 — THE BINDING BLOCKER.**
The 6-K has no per-vessel shuttle day rates, so (a) the Brasil 2014 / Rio 2016 **$60,000/day
extension rate is still an APPROX** of the "increased rate" disclosed in the Q1 6-K subsequent
events (2026-04-23) — a `~`-grade input on a **$453.1M** NAV leg, about 16% of gross NAV, and per
CLAUDE.md an APPROX is a RED not data; and (b) the NPV is struck **as-of 2026-03-31 and not
re-struck at 6/30**, so about $17M of Q2 contracted margin sits in both Cash 466,143 and this NPV;
net of the 11% unwind the overlap is about **$5M ≈ $0.15/sh, NON-CONSERVATIVE**. Resolution path is
the **monthly data kit**, not the 6-K. Anfield DP joins the book at Q3.

**9.4 Alaska + Archangel HFS — resolved, but the owner should ratify the reasoning.** The 9/11
shadow took the non-conservative side on a judgment call; the 6-K corroborates it on three
independent legs (§2). Recorded so the precedent is explicit rather than lucky.

**9.5 Arctic + Antarctic valuation basis.** On-curve at the txn-anchored mark, NOT at the $20,000
below-FMV repurchase price; not promotable to the S&P queue. Confirm the owner agrees a bargain
repurchase is not a §9.9 print.

**9.6 Kit deltas + spot coverage (strip leg only).** Apply Sola TS 26,651, Dimitris P TC 40,000,
Alaska/Archangel `charter_status: spot`; Suezmax coverage 0.125 → 0.188; re-derive Aframax (the
inherited 0.143 vs the rows' 0.095 is load-bearing in the strip). Land as its own leg, not inside
the balance-sheet swap.

**9.7 Second LNG carrier** — firm at 6/30 (R20) but no per-vessel price disclosed →
NEWBUILD_PRICE_PENDING stands on that hull.

**9.8 Presentation, not value: the debt-securities book.** 106,413 (15,143 short-term
held-to-maturity + 91,270 non-current, up from 25,233 at Dec-31) sits **inside** the WC composite
rather than beside cash. In NAV at the same amount either way; flagged because the composite hid it.

**9.9 Mechanics before the live land** — rotate the
`test_balance_sheet_basis_summary_lagging_and_current` pin; regenerate the weight-family sidecars
(`scripts/regen.sh`); annotate the +4.8pp EV% move (this document); register the §9.1 commitment
fork in `inputs/forks.yaml` (a shadow may not write it).

---

**VERDICT: WOULD-HOLD** — on two items, down from six. (1) `shuttle_contracted_book` is still an
uncited APPROX on about 16% of gross NAV and is struck at the wrong date (§9.3); (2) the newly-cited
$2,233,409 newbuild commitment is an owner methodology fork that a shadow must not wire (§9.1). One
guard reds and it is the pre-enumerated mechanical pin. **Everything the 6-K could settle, it
settled**: cash, the working-capital composite at component level, debt, advances, shares, NCI,
lease population, the orderbook count, held-for-sale status, and the Arctic/Antarctic ownership
question — the last of which went *against* the 9/11 shadow's conservative default, which is the
result worth keeping from this exercise. The band pre-registered on the filing's arrival was **HIT**
(91.91 in [91.7, 92.0]) and the bridge reconciles to the cent.
