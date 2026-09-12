# TEN 2026-Q2 shadow build — 2026-09-11 (release-based; the H1 6-K has not landed)

**What this is.** The results-landed SHADOW of the TEN Q2 pair: the two drafts
(`inputs/balance_sheets/ten_2026-Q2.yaml.draft`, `inputs/fleet_manifests/ten.yaml.draft`)
were corrected for every verifier issue in the handoff, then valued by
`scripts/shadow_regen.sh TEN 2026-Q2` in a throwaway worktree of HEAD `5576846`.
Nothing live was written; no git command was run by this stage. The live tree
still values TEN on the 2026-Q1 pair.

**VERDICT (one line, repeated at the end): WOULD-HOLD** — NAV-moving fields are still
carried UNVERIFIED (Arctic/Antarctic ownership at 6/30, Alaska/Archangel held-for-sale
status at 6/30, diluted shares, the NCI distribution leg, the shuttle NPV), one guard reds
(mechanically), and there is no pre-registered band to hit.

**Shadow headline:** NAV/sh 88.16 → **89.61** (+1.45); FV 61.8 → 62.75; EV% 38.2 → 40.3;
position BUY (undervalued) and tier GOVERNED-WIDE unchanged; balance_sheet_vintage
2026-Q1 → 2026-Q2. The bridge is verified, not just explained (§5).

---

## 1. Sources

| Source | Locator | Saved path | Retrieved |
|---|---|---|---|
| TEN H1/Q2 2026 results release, "TEN, Ltd. Reports Profits for the First Half and Second Quarter of 2026" | GlobeNewswire 3359616, 2026-09-10 09:15 ET; `source_url` on the sheet | `inputs/research_issuer/ten/2026-09-10_ten_h1_2026_results_pr.txt` (rendered-page text; file header "RETRIEVED: 2026-09-11 10:00 ET") | 2026-09-11 (saved page); first transcribed 2026-09-10 from three WebFetch pulls (`decisions/ten_h1_release_check_2026-09-10.md` Appendix B, every figure re-fetched verbatim; Dec-31-2025 comparatives tie digit-for-digit to the on-disk Q1 ex 99.1). `retrieved_at: 2026-09-11` on the sheet (both verifier lenses). |
| Q1 2026 6-K ex 99.1 | EDGAR acc 0001193125-26-236934, filed 2026-05-22 | `inputs/research_issuer/ten/ten_q1_2026_ex991.htm` | on disk since 2026-07-15 |
| FY2025 20-F | EDGAR acc 0001193125-26-144027, filed 2026-04-06 | `inputs/research_issuer/ten/ten_20f_fy2025.htm` | on disk since 2026-07-15 |
| 9/01 sale PR (two 2006-built Suezmaxes) | GlobeNewswire 3354219, 2026-09-01 | NOT saved (WebFetch small-model extraction only) | 2026-09-11 |

**The H1 2026 6-K is NOT on EDGAR as of 2026-09-11.** Read directly from
`data.sec.gov/submissions/CIK0001166663.json` on 2026-09-11: most recent 6-K filed
2026-05-22 (acc 0001193125-26-236934, the Q1 report); no 6-K on or after 2026-05-23; newest
filing of any kind is a Form 4 filed 2026-08-17 (before it: Form 144 2026-08-14, Form 4
2026-07-16, Form 144 2026-07-14, Form 4 2026-07-10, F-3ASR 2026-07-02 acc
0001193125-26-294484). `state/edgar_poll.json` for the CIK agrees (last_polled
2026-09-11T23:20Z; newest seen accession 0001193125-26-236934). H1-2025 precedent: the 6-K
for the period ended 2025-06-30 was filed 2025-09-30 (acc 0001193125-25-225057), so expect
late September / early October. **This shadow is therefore RELEASE-BASED**: the release's
BALANCE SHEET DATA table is the source for every figure it prints; everything else keeps
the 2026-Q1 sheet value and is marked `UNVERIFIED (shadow)` with the note that resolves it.

The 9/01 PR, fetched today because its wording bears on the held-for-sale question, reads
(per the WebFetch extraction, not a saved page): *"TEN announced today the sale of two
2006-built Suezmax tankers. This transaction will release in excess of $100 million to the
company's cash reserves."* It carries neither "agreed" nor "concluded" and no agreement /
MOA date. This ties to the digest's "in excess of $100 million" (release check, repo
citations) and is now recorded in both drafts' reason (i). The ten_log entry for it is still
owed (outside this stage's edit list).

Other repo inputs used: `decisions/ten_log.md` 2026-06-11 entry (Jun-5 data-kit deltas;
bareboat rates Arctic/Antarctic $13,870/day, Sakura Princess $10,500/day);
`decisions/ten_reconciliation_prereg_2026-07-15.md` (the Q1 construction; the removed-hull
marks); `decisions/ten_h1_refresh_packet_2026-09-07.md`;
`decisions/ten_h1_release_check_2026-09-10.md`. Price: the shadow values at HEAD's
`prices_daily.yaml` vintage — 44.71 in BOTH scorecard rows, so no price drift sits inside
the deltas (the working-tree `prices_daily.yaml` modification is not in the worktree).

## 2. Subsequent-events audit (done first, per the snapshot rule)

| Event | Verbatim (release 2026-09-10 unless noted) | 6/30 snapshot |
|---|---|---|
| Ulysses (2016-built VLCC) sale | Q1 6-K ex 99.1 SUBSEQUENT EVENTS: "On May 20, 2026, the Company completed the sale of a 10-year-old VLCC to third party interests. From the sale, TEN generated about $83 million in free cash after repayment of existing debt." Identity: 20-F Note 17(c) "On January 22, 2026, the Company signed a memorandum of agreement for the sale of the VLCC Ulysses" + release CORPORATE STRATEGY "The sale of the 2016-built VLCC Ulysses". Release STATEMENT OF OPERATIONS "Gain on sale of vessels (37,870)" Q2 and H1; "(inclusive of $38 million capital gains)". | **IN** — cash and gain inside 6/30; carrying value has LEFT Other assets; no row. Gross price not disclosed (not promotable). |
| Anfield DP (DP2 shuttle) delivery | SUBSEQUENT EVENTS: "on July 28, 2026, TEN took delivery of the DP2 suezmax shuttle tanker Anfield DP from Samsung Heavy Industries Co., Ltd in South Korea, the third in a series of 12 DP2 shuttle tankers under construction at that yard. The vessel commenced a 10-year employment to a US oil major, with charter options to extend the charter until the vessel's 20th year anniversary. Assuming charterers employ the vessel to the maximum duration, the expected gross revenues should approach $500 million." | **OUT** — a newbuild at 6/30; instalments inside Advances 470,050; joins `shuttle_contracted_book` at Q3. $500M is a max-duration envelope, not a rate. |
| Alaska + Archangel (2006-built Suezmaxes) sale | SUBSEQUENT EVENTS: "As part of its ongoing fleet renewal program, in August 2026 TEN concluded the sale of two 2006-built suezmax tankers, the Alaska and Archangel, for net proceeds of $100 million." 9/01 PR: "announced today the sale ... in excess of $100 million" (no date). | **OUT as a sale** — owned at 6/30, rows stay. **Held-for-sale AT 6/30: OPEN** (judgment call §9.1; on-curve taken = the non-conservative side, exposure bounded). Aggregate + net, never split — not promotable. |
| July 2026 common dividend | CORPORATE AFFAIRS: "In July 2026, TEN distributed to common shareholders a second semi-annual dividend, amounting to $1.00 per share, following a $0.50 per share payment in February 2026." | **OUT** as cash; whether a payable sat inside Other liabilities 220,881 at 6/30 is not disclosed (6-K item). |
| Series E call intent | "become redeemable at the election of the Company on May 28, 2027 ... This disclosure does not constitute a notice of redemption" | **OUT** — E outstanding at 6/30 (H1 "Effect of preferred dividends (13,500)" = 118,649 × 9.25%/2 + 168,679 × 9.50%/2, ties). |
| LNG newbuild row 26 firm-up | NB table row 26 "TBN \| LNG Carrier \| Q1 2029 \| Under Construction \| TBA" (Q1 ex 99.1 row 26 = "Optional Vessel"); contract undated in the release; MB LNG Weekly 29 dated 2026-07-16 (ten_log). | **OUT / UNVERIFIED** — not counted in the 6/30 orderbook; no price (NEWBUILD_PRICE_PENDING if the 6-K is silent). |
| November 2026 dividend announcement | "intends to announce the first semi-annual dividend payment of 2027 in November 2026" | **OUT**. |
| Arctic + Antarctic repurchase (agreed Apr-7-2026) | Q1 6-K ex 99.1 SUBSEQUENT EVENTS: "On April 7, 2026, TEN agreed to repurchase two of its 2007-built suezmax tankers, currently operating under five-year leases at prices below current fair market value." 20-F leases note: "On June 21, 2021, the Company commenced a new five-year sale and leaseback agreement for each of the two suezmaxes, Arctic and Antarctic. The agreed net sale price was $52,304." (weighted-average remaining term 0.48 years at Dec-31-2025). Release: no "Arctic" / "Antarctic" / "repurchase" text. | **UNVERIFIED — completion undated.** The SLB term ended 2026-06-21, before the snapshot; the pair was still operated at 6/30 (release dwt 7,702k = the Jun-5 kit's 63 hulls including them). Kept OUT as the CONSERVATIVE DEFAULT, not a prior state (§9.2). |
| Brasil 2014 / Rio 2016 extensions (Apr-23-2026) | Q1 6-K: "employment extension of up to five years for two 2013-built DP2 Shuttle tankers, in direct continuation of their existing charters" | Pre-quarter agreement, rate undisclosed → the $60k/day APPROX in the shuttle book is unchanged. |

## 3. Sourced figures (sheet, $K unless stated)

| Field | 2026-Q1 value | 2026-Q2 draft | Citation, or the UNVERIFIED reason |
|---|---:|---:|---|
| `source_url` / `retrieved_at` / `filing_period_end` | — (Q1 sheet pre-dates the trio) | GlobeNewswire 3359616 URL / 2026-09-11 / 2026-06-30 | The trio the Q2-on guard requires; retrieved_at = the saved-page date (§1). |
| `cash_and_equivalents` | 321,416 | **466,143** | Release BALANCE SHEET DATA, June 30, 2026: "Cash 466,143"; prose tie "$466.1 million, $168.0 million higher than the end of December 2025" (466,143 − 298,129 = 168,014). |
| `working_capital_net` | 174,654 (331,398 − 156,744) | **65,359** | Same composite construction: "Other assets 286,240" − "Other liabilities 220,881". Δ −109,295 explained at NO component level (Ulysses HFS carrying value left Other assets; Other liabilities +64,137 undisclosed). **UNVERIFIED at component level** → 6-K interim balance sheet. |
| `total_debt` | 2,136,109 | **2,102,177** | Release "Debt and other financial liabilities, net of deferred finance costs 2,102,177" (the same BS-carrying line the Q1 sheet cites; Dec-31-2025 comparative 1,920,975 ties to the 20-F). Schedule / Anfield draw / Tenergy SL split → 6-K Note 7. |
| `lease_liabilities` | 0 | **0** | Convention (RoU = obligation nets inside the composite). Arctic/Antarctic population at 6/30 **UNVERIFIED** → 6-K leases note (§9.2). |
| `newbuild_capex_commitments` | 0 | **0** | Convention (delivered-value = contract-price, advances-only, OFF_CONVENTION). LNG row 26 commitment date/price **UNVERIFIED** → 6-K. |
| `newbuild_advances_paid` | 442,740 | **470,050** | Release "Advances for vessels under construction 470,050" (Dec-31-2025 comparative 301,868 ties to the 20-F). Includes Anfield DP instalments (delivered after 6/30). |
| `diluted_shares_outstanding` | 30,127,603 | **30,127,603** | **UNVERIFIED**: the release prints only the EPS denominator "Weighted average number of shares, basic and diluted 29,972,103" (excludes non-vested restricted stock, "(684)" allocation); Q1 ex 99.1 printed 29,971,603 on the same basis against 30,127,603 outstanding. Awaits the 6-K cover / equity note (or the F-3ASR of 2026-07-02). No buyback or issuance disclosed. |
| `preferred_equity` | 333,282 (287,328 + NCI 45,954) | **337,458** (287,328 + NCI 50,130) | E+F liquidation 287,328 re-tied by "Effect of preferred dividends (6,750)" / "(13,500)". NCI ROLLED on the Q1 construction: 43,529 (20-F audited) + 2,425 (Q1 6-K) + 4,176 (release "Less: Net income attributable to the noncontrolling interest (4,176)" Q2; "(6,601)" H1 = 2,425 + 4,176, ties). **UNVERIFIED on the distribution leg** (zero Q2 distributions to Polaris is the Q1 sheet's basis, not a release statement) → 6-K NCI note. Judgment call: the roll is the conservative side (−$0.14/sh vs holding 45,954). |
| `governance_discount_pct` | 0.30 | **0.30** | Judgmental HOLD inside the §15.7 band 30-36% (release check §6: no fee figure, no buyback, payout $1.50 on H1-annualised EPS 14.24 = 10.5%; Series E call intent leans the other way). Revisit at the 6-K related-party note / November dividend. |
| `shuttle_contracted_book` | 453,100 | **453,100** | **UNVERIFIED**: Brasil/Rio extension rate still undisclosed (the $60k/day APPROX stands); NPV struck as-of 2026-03-31 and not re-struck — about $5M (about $0.15/sh) of Q2 contracted margin now sits in both Cash and the NPV (non-conservative). Re-strike at the live land; Anfield DP joins at Q3. |
| `held_for_sale` | absent (0, deliberate) | **absent (0)** | Ulysses sold; Alaska + Archangel on-curve (HFS status **UNVERIFIED**, §9.1); under the flip the carrying value sits inside the composite, not here. |

Manifest header fields: `report_date` 2026-Q1 → **2026-Q2**; `fleet_summary.on_curve_total` 56
(unchanged); avg ages re-footed (crude 9.55, product 13.67, LNG 7.05); `total_in_water_at_6_30`
63 (the release's printed 64.0 is contradicted by its own dwt 7,702k and 63.5 average — no hull
added on the printed count).

## 4. Fleet changes (2026-Q1 manifest → 2026-Q2 draft)

- **Rows: the same 56 hulls** (2 VLCC / 14 conventional Suezmax / 21 Aframax / 4 LR2 / 9 LR1 /
  2 MR / 2 Handysize / 2 LNGC) — no sourced addition or removal dated inside Q2. The release
  carries no per-vessel fleet table (nor did the H1-2025 6-K), so no row is a sourced 6/30 hull
  list; every age is the Q1 age + 0.25 (91/365 y).
- **Ulysses**: already out of the on-curve fleet at Q1 (HFS); now gone from the WC composite too.
- **Anfield DP**: delivered 2026-07-28 — not a row (newbuild at 6/30; no Shuttle class on a curve).
- **Arctic + Antarctic (2007-built Suezmaxes)**: NO rows — the CONSERVATIVE DEFAULT, not a prior
  state (SLB term ended 2026-06-21; repurchase agreed 2026-04-07; completion in no source on
  disk). Re-add pre-enumerated: 56 → 58, crude 37 → 39, Suezmax 14 → 16, direction +.
- **Alaska + Archangel (2006-built)**: rows STAY on-curve (owned at 6/30; sold August 2026).
  Row-level tag added: held-for-sale status at 6/30 UNVERIFIED (shadow).
- **Employment / coverage**: Q1 values carried (attribution, not provenance — the Jun-5 kit
  deltas are as-of-snapshot facts the guard would accept); direction stated per row (Archangel
  102,000 overstates the Suezmax TC leg; Sola TS understated by $1,000/day); Euro / Spyros K /
  Asahi Princess tagged with their 20-F charter expiries (May-26 / Jun-26 / Jun-26). Suezmax
  spot fraction re-derives to 0.214 at the live land; the inherited Aframax 0.143 vs the rows'
  0.095 is load-bearing in the strip (coverage 0.857 vs 0.905).
- **Fleet value by class, committed run vs draft** (reproduced with the engine's txn-anchored
  curves via a read-only library call; the live manifest reproduces the committed report's
  3,733.3 total): VLCC 233.5 → 231.3 · Suezmax 1,015.0 → 1,000.5 · Aframax 1,425.6 → 1,407.1 ·
  LR2 229.0 → 225.4 · LR1 250.6 → 245.5 · MR 109.5 → 108.6 · Handysize 26.9 → 26.2 · LNGC
  443.2 → 440.2 · **total 3,733.4 → 3,684.8 ($M), −48.6 = −$1.61/sh** — the 91-day age roll,
  nothing else.

## 5. Shadow vs committed (copied from the SHADOW-JSON block; HEAD 5576846, manifest_used: draft)

| Field | Committed (live) | Shadow | Delta |
|---|---:|---:|---:|
| `nav_per_share` | 88.16 | **89.61** | **+1.45** (+1.6%) |
| `fv` | 61.8 | 62.75 | +0.95 |
| `ev_pct` | 38.2 | 40.3 | +2.1pp |
| `position` | BUY (undervalued) | BUY (undervalued) | unchanged |
| `confidence_tier` | GOVERNED-WIDE (subreason mixed) | GOVERNED-WIDE (subreason mixed) | unchanged |
| `balance_sheet_vintage` | 2026-Q1 | 2026-Q2 | advanced |
| `blend_fv` | 59.49 | 60.47 | +0.98 |
| `gap_pct` (vs broker NAV 109.05) | −19.2 | −17.8 | +1.4pp |
| `fv_low` / `fv_high` | 45.87 / 82.53 | 46.97 / 83.25 | +1.10 / +0.72 |
| sleeves (crude / product / lng $/sh) | 41.39 / 12.67 / 7.74 | 42.11 / 12.77 / 7.87 | +0.72 / +0.10 / +0.13 |
| `price` | 44.71 | 44.71 | none (same vintage) |
| `weight_sign_stable`, `ev_pct_family_min/max` | true, 21.3 / 38.2 | null, null / null | the weight-family sidecars are not regenerated inside the shadow worktree (`scripts/regen.sh` runs them; the shadow runs the pipeline alone) — mechanical, not a build defect |

**NAV bridge, verified against the run (CLAUDE.md 2026-08-08: verify the run's own breakdown).**
Balance-sheet legs ($K): cash +144,727 · WC −109,295 · debt −33,932 (adds +33,932) · advances
+27,310 · preferred/NCI −4,176 → **+92,498 = +$3.07/sh**. Age roll (§4): **−$1.61/sh**.
Predicted 88.16 + 3.07 − 1.61 = **89.62 vs observed 89.61** (rounding). Shadow NAV total
≈ 2,699.7 $M = draft fleet 3,684.8 + (466.1 + 65.4 − 2,102.2 + 470.1 + 453.1 − 337.5).

Drift-gate reading for the live land: NAV +1.6%, EV% +2.1pp — over the 2pp EV% annotation
threshold (this document is the annotation); no band flip (BUY unchanged); k_broker on its
second difference unaffected (broker NAV 109.05 carried).

## 6. Band check

**No pre-registered band.** The packet (`decisions/ten_h1_refresh_packet_2026-09-07.md` and the
release check §7) records "No prereg band — the pair is not writable". Nothing to HIT or MISS.
The owner-present build must pre-register one BEFORE the 6-K lands; on this shadow's
construction the arithmetic anchor is NAV/sh 89.61 with the open-item envelope in §9 (roughly
87.4 – 92.0 depending on the Arctic/Antarctic and Alaska/Archangel rulings).

## 7. Guard verdicts (shadow worktree; `-k "TEN or ten or coherence or provenance"` over
`tests/test_quarter_coherence.py`, `tests/test_manifest_provenance.py`, `tests/test_scrubber_provenance.py`)

```
[shadow] guards: 1 failed, 27 passed, 9 xfailed in 6.05s
[shadow] FAILED tests/test_quarter_coherence.py::test_balance_sheet_basis_summary_lagging_and_current
```

- The one red is the pre-enumerated pin: `tests/test_quarter_coherence.py:238-246` asserts
  `s["lagging"] == {"TEN": "2026-Q1"}` — TEN is pinned as the Q1-lagging specimen "until its H1
  sheet lands". With the draft resolving as `ten_2026-Q2.yaml` the lagging set becomes `{}`.
  Mechanical, not a build defect; the live land must rotate the pin (as CMBT's was on
  2026-09-10). The live tree is untouched.
- Pipeline: no `STALE-PRICE` / `STROBE` / `Traceback` / `Error` lines were printed by the script's
  filter; the SHADOW-JSON block printed (it only prints after a successful pipeline run). The
  wrapper's exit-code capture showed blank because `PIPESTATUS` is bash-only under this zsh
  shell — not a script failure.
- Pre-run self-check (read-only, in the working tree): both drafts parse; manifest rows sum to
  56 = `on_curve_total`; the provenance guard's regexes (CLAIM_RE; NAV-figure estimate markers in
  newbuild / other-NAV context) replicated over both drafts find no new red; 287,328 + 50,130 =
  337,458 ✓.
- The full pytest suite was NOT run (not permitted in this stage); 9 xfails are the queue
  xfails, expected.

## 8. Verifier issues — applied / left open

Applied to the drafts (handoff numbering; both files where the text was mirrored):

1. source/MINOR — reason (ii) (Vessels, net bridge) replaced with the NON-DISCRIMINATING
   wording in the sheet header and the manifest cohort block; the ">$100M of additions"
   sentence deleted; the call now rests on (i) and (iii).
2. source/MINOR — Arctic/Antarctic circumstantial lines (Charter hire 2,646 vs 3,386 vs 3,321;
   Vessels, net +10,118 net of 46,295 D&A; Q2 D&A vs Q1 44,147; investing +3,763) added verbatim
   to the sheet `lease_liabilities` comment and the manifest cohort comment, labelled
   inference-not-disclosure; the re-add pre-enumerated with direction (+).
3. source/MINOR + snapshot/MINOR — `retrieved_at` → 2026-09-11 (saved-page date), comment
   keeps the 2026-09-10 first-transcription pointer.
4. source/MINOR — reason (i) rewritten: no MOA date on disk; 9/01 PR locator (GlobeNewswire
   3354219, earnings-calendar basis, text not on disk, ten_log owed); the 9/10 release quote.
   The 9/01 PR was then fetched (§1): "announced today the sale", no agreement date — recorded
   in both drafts.
5. source/MINOR (process) — not a draft defect; recorded here for the git-owning stage (§8
   left-open); the test pin was pre-enumerated and fired exactly as predicted (§7).
6. snapshot/BLOCKING — Arctic/Antarctic: rows kept OUT; the manifest header, cohort comment and
   the sheet lease comment rewritten as "CONSERVATIVE DEFAULT, NOT a prior state" with the 20-F
   leases-note quote (commenced June 21, 2021, five-year → ended 2026-06-21), the Q1 6-K
   repurchase quote, the dwt tie and the Antarctic TC-to-Dec-26 fact; indicators listed as
   inference; the 58-hull sensitivity sized (§9.2, analytic on the engine curve — a pipeline
   run was not permitted here); the owner fork is OWED (forks.yaml is outside this stage's list).
7. snapshot/BLOCKING — Alaska/Archangel HFS: each row now carries "UNVERIFIED (shadow):
   held-for-sale status at 6/30 — awaits 6-K vessels-held-for-sale / subsequent-events note (MOA
   date)"; reason (i) restated on ASC 360-10-45-9 with the Note 17(c) "precedent" attribution
   dropped (Note 17(c) only records the Ulysses MOA; the HFS-at-Mar-31 treatment was the Q1
   prereg's inference); ON-CURVE stated as the non-conservative side; exposure bounded (§9.1);
   the 54-hull flip sized.
8. snapshot/MINOR — Euro / Spyros K / Asahi Princess rows tagged with the 20-F expiries
   (May-26 / Jun-26 / Jun-26) and "Jun-5 kit showed no delta".
9. snapshot/MINOR — Alaska/Archangel rate direction stated on each row (spot-indexed per the
   kit; Archangel 102,000 overstates the TC leg); Sola TS $26,651 named an as-of-snapshot fact
   (kept for attribution only); live-land actions listed; Suezmax 0.214 re-derivation and the
   load-bearing Aframax 0.143-vs-0.095 note added at `spot_coverage_pct`.
10. snapshot/MINOR — `preferred_equity` ROLLED to 337,458,000 (NCI 50,130) on the Q1
    construction, release-cited; distribution leg UNVERIFIED; recorded as a judgment call
    (conservative side).
11. snapshot/MINOR — `shuttle_contracted_book` comment now states the NPV as-of (2026-03-31),
    the about-$17M collected margin, the about-$5M net overlap, non-conservative, re-strike at
    the live land.
12. snapshot/MINOR — Ulysses citation chain (Q1 6-K "a 10-year-old VLCC" + 20-F Note 17(c) +
    release "2016-built VLCC Ulysses") applied in the sheet header, the cash comment, the
    manifest header and the VLCC block.
13. schema/CORRUPTING — Arctic/Antarctic "probable wrong OUT". **The issue text arrived
    TRUNCATED in the handoff (cut at "Th"; no fix section received).** It disagrees with the
    snapshot lens (BLOCKING: keep OUT) and the source lens (MINOR: keep OUT). Per the stage rule
    the CONSERVATIVE reading was taken — OUT understates NAV (cash is already net of any
    repurchase price paid; the marks are missing) — and it is recorded as a judgment call
    (§9.2). Every indicator the schema lens cites (SLB end date, the dwt tie, the charter-hire
    step at the logged bareboat rates) is now in both drafts, and the re-add is pre-enumerated
    as the likeliest 6-K resolution with direction +.

Left open (outside this stage's edit list or its permissions):

- **Git:** both drafts are untracked; the shadow script's header expects them committed, and any
  auto-land lane needing a clean tree will refuse. The git-owning stage commits the two drafts +
  this document.
- **forks.yaml:** the Arctic/Antarctic ownership question as an owner fork (§9.2).
- **ten_log:** entries for the 9/01 sale PR and the 9/10 release (owed since the release check).
- **Saved page for the 9/01 PR** (WebFetch extraction only).
- **Sensitivities as pipeline runs** (analytic here, engine-curve exact for the fleet leg but
  without the blend / strip recomputation).
- **Full pytest**, the test-pin rotation, the prereg band, the kit deltas and the coverage
  re-derive — all live-land work.

## 9. Judgment calls the owner-present build must rule on

**9.1 (FIRST) Alaska + Archangel — held-for-sale at 2026-06-30?**
Shadow takes NOT HFS → on-curve (rows in; carrying value NOT inside the composite). This is the
NON-conservative side. Evidence: no MOA / "held for sale" text in the release or the 9/01 PR;
no agreement date anywhere on disk; the 9/10 release says only "in August 2026 TEN concluded
the sale"; the Vessels, net bridge cannot discriminate (a reclass would move only the
undisclosed carrying value, and the unidentified Q2 additions have another named candidate).
Under ASC 360-10-45-9 a signed MOA normally meets the criteria — TEN discloses no policy; the
Ulysses HFS-at-Mar-31 treatment was itself an inference. **If flipped** (rows out, composite
unchanged, `held_for_sale` stays 0): the two marks at 20.35 / 20.45 years on the txn-anchored
Suezmax curve (10-yr $70.6M → scrap $13.0M at 25) are $30.9M + $30.5M = **$61.3M = −$2.04/sh**
(base curve $67.1M = −$2.23/sh); the 20-F carrying basis is lower still (repurchased
Jul-19 / Aug-22-2024 at $21,000K each net of the $5,900K seller's credit; finance-lease
liability remeasured $43,316K incl. the $11,800K credit). Resolves at the 6-K
vessels-held-for-sale note / subsequent-events MOA date.

**9.2 Arctic + Antarctic — owned at 2026-06-30?**
Shadow keeps them OUT (chartered-in, excluded) as the conservative default. The five-year SLB
commenced 2021-06-21 (20-F) and so ended 2026-06-21, before the snapshot; the repurchase was
agreed 2026-04-07 (Q1 6-K); the pair was still operated at 6/30 (dwt tie); the release's
charter-hire step (Q2 2,646 vs Q1 3,386, fitting the pair on hire about 60 of 91 days at
$13,870/day each), the Vessels, net +10,118 net of D&A, the D&A rise with Ulysses gone and Q2
investing of +3,763 after the VLCC proceeds all point the same way — but none is a citation for
ownership. **If re-added** (56 → 58; crude 37 → 39; Suezmax 14 → 16; `lease_liabilities` stays
0; cash already net of the price): two 2007-built Suezmaxes at 19.0–19.5 years on the
txn-anchored curve mark $34.1–36.0M each → pair $68.2–72.1M = **+$2.26 to +$2.39/sh** (base
curve at 19.25y: $77.4M = +$2.57/sh). Likeliest 6-K resolution; direction +. Also check 6-K
Note 7 for repurchase financing. **Owner fork owed** (forks.yaml). One verifier lens rated the
OUT "probable wrong" (CORRUPTING, text truncated in the handoff); two lenses said keep OUT.

**9.3 NCI roll** — 50,130 (rolled, conservative, Q1 construction) vs 45,954 (held): ±$0.14/sh.
The 6-K NCI note / Mare Success distributions settle it.

**9.4 `diluted_shares_outstanding`** — 30,127,603 carried from the 20-F; the release prints only
the weighted average 29,972,103. 6-K cover / equity note / F-3ASR 2026-07-02.

**9.5 Shuttle book re-strike** — NPV as-of 2026-03-31 carried to a 6/30 snapshot: about $5M
(about $0.15/sh) overlap with Cash, non-conservative; ages inside the breakdown not rolled;
Brasil/Rio rate still APPROX $60k/day; Anfield DP joins at Q3.

**9.6 Kit deltas + spot coverage (strip leg only)** — apply Sola TS 26651, Dimitris P TC 40000,
Alaska/Archangel `charter_status: spot`; Suezmax coverage 0.214; re-derive Aframax (inherited
0.143 vs rows 0.095 is load-bearing). Attribution: land as its own leg, not inside the
balance-sheet swap.

**9.7 LNG newbuild row 26** — contract date and price (MB LNG Weekly 29 dated 2026-07-16 →
post-quarter if it holds); NEWBUILD_PRICE_PENDING park if the 6-K is silent.

**9.8 Governance 0.30** — HOLD inside the 30-36% band; revisit at the 6-K related-party note /
the November dividend announcement.

**9.9 `retrieved_at` convention** — the saved-page date (2026-09-11) was taken over the
first-transcription date (2026-09-10) on both verifiers' reading; if the owner prefers the
DHT-style build date, say so in the sheet comment.

**9.10 Mechanics before the 6-K land** — rotate the `test_balance_sheet_basis_summary_lagging_and_current`
pin; pre-register the band (§6); commit the drafts; regenerate the weight-family sidecars
(`scripts/regen.sh`); annotate the +2.1pp EV% move (this document).

Open-item envelope on NAV/sh 89.61: −2.04 (9.1 flip) −0.15 (9.5) ±0.14 (9.3) … +2.39 (9.2
re-add) → roughly **87.4 – 92.0**; position BUY and tier GOVERNED-WIDE are insensitive across it.

---

**VERDICT: WOULD-HOLD** — NAV-moving fields still carried UNVERIFIED (Arctic/Antarctic ownership
at 6/30 with OUT uncited against contrary indicators; Alaska/Archangel held-for-sale status at
6/30 on the non-conservative side; diluted shares; the NCI distribution leg; the shuttle NPV);
one guard red (the lagging-specimen pin, mechanical); no pre-registered band to hit; drafts
untracked. The release-sourced fields (cash, WC composite, debt, advances, NCI income) are
clean and the bridge verifies — the pair lands on the 6-K, not on the release.
