# CMBT 2026-Q2 pair — LANDING RECORD (2026-09-10)

Executes fork `cmbt_q2_c1_c2_c3` (inputs/forks.yaml; executable on 2026-09-10 under the
silence-executes ruling): **C-1 YES** (Donoussa, Stella, Brest, Brugge, Golden Myrtalia
off-curve; HFS 219,985k enters working capital at IFRS-5 carrying value) · **C-2 YES** (the
$100M FSO placeholder kept with its 109,937k secured loan inside total_debt) · **C-3 YES**
(governance_discount 0.0 holds; Note 23 litigation tripwire recorded — Bermuda appeal Nov-2026).
Pair written: inputs/balance_sheets/cmbt_2026-Q2.yaml + inputs/fleet_manifests/cmbt.yaml
(report_date 2026-Q2). Drafted and adversarially verified read-only first (WRITE WITH
CORRECTIONS, none corrupting; every NAV-moving figure re-read off the page image; the Q1 6-K
acc 0000919574-26-003591 fetched to settle the Newcastlemax count AT SOURCE).

## The one thing NOT executed by silence — Fork 3, registered instead

`newbuild_capex_commitments` is SUBTRACTED by the engine (nav.py:117). Booking the sourced
900,837k flips CMBT from advances-only to commitment-net: **−$3.10/share** (900,837k /
290,169,769). `newbuild_convention.yaml` says CMBT "must move to commitment-net (own pre-reg)"
— a methodology switch with its own ruling, not one of the three ruled forks. **Branch A
applied:** commitments 0 (the Q1 convention continues), the sourced figure carried as
provenance on the line. Registered as fork `cmbt_commitments_convention` (execute_after
2026-09-15, recommendation: move to commitment-net). Both readings below.

## PRE-REGISTRATION BAND (frozen before the regen)

Q1 NAV/share on HEAD curves: **$16.54** (reproduced to the cent by the verifier: 16.5394; fleet
8,068.8M; VLCC 635.5 / Suezmax 1,282.2 / Cape 4,835.6 / Pana 1,058.2 / Ctr 257.2).

**Branch A (applied): NAV/share $16.46, band $16.36–$16.56** (±$0.10 ≈ ±$29M, one mid-age
Suezmax mark). Movers: AUC −227,147k · HFS +219,985k less the five removed on-curve marks
(Donoussa 103.89M, Brest/Brugge 102.01M each, Stella 50.44M, Golden Myrtalia 35.58M) · the
seven H1 deliveries on-curve · CAPE_2026 recount 2→4 (+2 × 98.76M; the Q1 row over-counted two
phantom hulls, $0.68/share — an inherited Q1 error) · debt +208,900k · cash −43,026k · shares
unchanged. Fleet expected ≈ 8,184.7M (VLCC 701.3 / Suezmax 1,247.9 / Cape 4,933.2 / Pana ≈ Q1 /
Ctr ≈ Q1).

Commitment-net reading (fork 3 if ruled): **$13.36, band $13.26–$13.46** — differs by exactly
$3.104.

**A landing outside the band = HALT for input investigation, never output adjustment.** Order
of suspects: a curve/transaction print landed between HEAD and the regen (re-run
`--txn-comparison`, not this pair); a row not matching the loader's class parse; the HFS/AUC
double-count (a hull both on-curve and inside WC).

## Corrections folded from the verification

A. Sheet comment re-cut so the NB-context estimate regex sees the Note 12 img_027 token.
B. Fork 3 → registered (above). C. The "broker NAV $20.14" gate figure was uncited — Pareto
28 Aug 2026 gives 18.3 / 0.86 = 21.28; the HEAD scorecard row 22.5; SANITY OK either way
(16.46/22.5 = −27%). D. Q1 6-K (acc 0000919574-26-003591) cited in both files; "not staged"
removed. E. Sheet header says "executable ON 2026-09-10" (sentinel fires on execute_after ≤
today); forks.yaml status flips to executed with this commit. F. HFS basis = IFRS-5 carrying
per the ruling text "off-curve at HFS"; nav.py's own held_for_sale field is documented as
"agreed-sold vessels at contracted price" — the agreed-price reading (Brugge+Brest 224.0M,
Donoussa 123.7M derived) would add +$0.60/share; recorded, not applied. G. "REMOVED" → "RECOUNTED".

## Open items (owner)
- Fork 3 (above) — the recommendation executes 2026-09-15 unless answered.
- HFS basis (F): carrying vs agreed-price — a methodology note, +$0.60/share if changed.
- MB "Julie" identity (2,262 vs 2,207 TEU) — GSL, unrelated; settle at GSL's Q2 table.

---
# APPENDIX A — the drafted pair + band (agent, read-only)

I have everything I need; no further tool calls. All figures below trace to the packet (decisions/cmbt_q2_refresh_packet_2026-09-07.md, Appendices A–D) and were spot-checked against page images img_001, img_002, img_017, img_025, img_027, img_065–067, img_073; the band was computed in memory on HEAD's transaction-anchored curves (reproducing the scorecard's $16.54 exactly before applying the diff; nothing written, `git status` clean).

# CMBT 2026-Q2 pair — fork `cmbt_q2_c1_c2_c3` executed (C-1 YES · C-2 YES · C-3 YES)

**Two findings beyond the packet, both load-bearing, stated up front:**

1. **`newbuild_capex_commitments` is SUBTRACTED by the engine** (`nav.py:117`). Populating 900,837 as instructed is not a provenance note; it flips CMBT from advances-only to **commitment-net** (−$3.10/share) — the convention `newbuild_convention.yaml` says CMBT "must move to" (structural-exempt, clause 2). It is applied below as instructed; the Fork 3 Branch A alternative (0, figure carried as sourced provenance) is band-quoted alongside so the owner sees both numbers. Landing it XPASSes the strict-xfail in `tests/test_newbuild_convention.py` — `"CMBT"` must leave `OFF_CONVENTION_QUEUE` in the same commit.
2. **Fork 4 (Newcastlemax 42 vs 40) CLOSES on the report's own numbers, against the Q1 row, not the page.** Note 12 (img_025) lists exactly four H1 Newcastlemax deliveries and six remaining; the 20-F program was ten at Dec-25 (`02_drybulk_fleet.md:28-30`): 10 − 4 = 6 ✓, 36 + 4 = 40 ✓ = the 30-June page (img_073). The H1 timeline (img_065–069) shows no Q1 Newcastlemax delivery. So Mineral Malta / Mineral Europa — the Q1 row `CMBT_CAPE_2026 count: 2` — were NOT on the water at 30 June (nor at 31 March); the "38 (+8NB)" came from the Q1 6-K press-release paragraph (as-of PR date, the same trap as the 8/27 PR). Rows go to `count: 4`; summary = Σ rows = 129 = page. Third inherited Q1 error: 2 × $98.8M = $0.68/share over-counted at Q1 (and double-counted with AUC).

---

## 1. `inputs/balance_sheets/cmbt_2026-Q2.yaml`

```yaml
# CMB.TECH NV (CMBT) balance sheet snapshot — METHODOLOGY §4.2, §11.9. USD, as-of 2026-06-30.
# Source: H1-2026 half-year report, 6-K accession 0000919574-26-006193 (filed 2026-09-04), Ex-99.2
# = notes-bearing financial report (page images img_000-052), Ex-99.1 = narrative report
# (img_053-085). Citations are img_NNN + printed page + note. The staged .htm exhibits are
# image-only shells (0 figures) — the 86 page images were fetched from the EDGAR filing
# directory 2026-09-07 (decisions/cmbt_q2_refresh_packet_2026-09-07.md, App. A §0).
# ASSURANCE: the auditor's report (img_051, Antwerp 2 Sep 2026) is an ISRE 2410 REVIEW, not an
# audit ("we do not express an audit opinion") — every figure below is reviewed, not audited.
# Subsequent events (Note 26 img_049 p.50) audited FIRST and kept OUT: 14-Jul Windcat 65 CTV
# delivery (advances stay in AUC); 3-Aug Donoussa sale announcement (asset IN as HFS at 30 Jun
# per Note 8; the USD 74.3M gain is Q4-2026, OUT); 11-Aug Bristol sale announcement (OUT
# entirely — Bristol is an on-water Suezmax at 30 Jun, absent from Note 8). Outside Note 26:
# Note 6 img_015 says Brest/Brugge "have been delivered in the third quarter of 2026" (gain
# USD 100.2M, Q3) — IN at 30 Jun as HFS at carrying value, delivery + gain OUT.
# The 31-AUGUST fleet table (img_059) and its "18.28 USD" share price were NOT used anywhere.
# Executes fork cmbt_q2_c1_c2_c3 (inputs/forks.yaml, silence past 2026-09-10 = recommendation):
#   C-1 YES — the five held-for-sale hulls leave the on-curve manifest; HFS 219,985 enters
#             working_capital_net at IFRS-5 carrying value (see the HFS block).
#   C-2 YES — the FSO placeholder stays WITH its secured loan inside total_debt.
#   C-3 YES — governance_discount_pct stays 0.0; Note 23 tripwire recorded.
# PAIR: lands in ONE commit with inputs/fleet_manifests/cmbt.yaml report_date: 2026-Q2
# (pair guard, tests/test_quarter_coherence.py) and with newbuild_advances_paid falling
# 759,807 -> 532,660 as the seven H1 hulls go on-curve (else they are double-counted).

ticker: CMBT
quarter: 2026-Q2
source_url: https://www.sec.gov/Archives/edgar/data/1604481/000091957426006193/
retrieved_at: 2026-09-07
filing_period_end: 2026-06-30

# Cash 151,574 + short-term investments 8,271 (both liquid) = 159,845 — statement of
# financial position img_001 p.2 (Q1: 202,871). Cash-flow tie: 146,529 + 6,036 − 991 = 151,574
# (App. B §1). NOT included (known exclusion, Note 20 img_041 p.42): USD 51.4M cash security
# lodged with the High Court of Malaysia (realisation ~2 years) and the 19,029 ammonia-engine
# development advance — convention-consistent with Q1, disclosed here.
cash_and_equivalents: 159845000

# working_capital_net = operating WC + the OFF-CURVE segments at segment book (§11.9) + the
# Investments line + assets held for sale. All at 30 Jun 2026 unless stated. USD thousands:
#   operating WC (img_001/img_002, Q1 convention): inventory 120,674 + trade & other
#     receivables 415,688 + current tax assets 2,828 − trade & other payables 235,139
#     − current tax liabilities 2,807                                        = +301,244
#   + Bochem chemical vessels at segment book, Note 7 img_017 p.18 (Q1 used the
#     Dec-25 20-F value 276,374 — the staleness caveat is RETIRED; now 30-Jun)  = +312,680
#   + Windcat vessels at segment book, Note 7 img_017 (Dec-25: 196,542)         = +264,585
#   + Investments line, img_001 / Note 25 img_047 p.48 — RELABELLED: this is mostly
#     FVTPL equity stakes (Anglo-Eastern Univan 10% USD 45.0M, SwissMarine 15.92%
#     USD 44.8M = 89,825 non-current FVTPL, derived 154,217 − 64,392) plus
#     equity-accounted JVs 28,320 + associates 36,072 = 64,392 (Note 25 img_048).
#     The Q1 label "equity-accounted JV investments" was wrong; the whole-line
#     amount convention carries (Q1: 132,308). No FSO sits in the investees.      = +154,217
#   + assets held for sale at IFRS-5 CARRYING value, img_001 / Note 8 img_019 p.20 = +219,985
#       Included ONLY because C-1 moves all five hulls OFF the on-curve manifest in the
#       paired cmbt.yaml (else double-count, $0.758/share). Composition (Note 8 + Note 7):
#         Brugge + Brest (Suezmax 2023) "combined carrying value of USD 123.8 million"
#           — COMBINED figure, MoAs 12 Jun 2026, never split per hull            123,800
#         Donoussa (VLCC 2016) "carrying value of USD 49.4 million", Note 8       49,400
#         Golden Myrtalia (Capesize 2011) = Bocimar HFS column, Note 7 img_017,
#           the only Bocimar hull in Note 8 (segment-pinned)                      25,166
#         Stella (Suezmax 2011) RESIDUAL [DERIVED]: Euronav HFS 194,819 (Note 7)
#           − 123,800 − 49,400 = 21,619; cross-check Note 12 img_025 transfer
#           (173,196): 219,985 − 173,196 − 25,166 = 21,623 (±0.1M rounding)       21,619
#         foot: 123,800 + 49,400 + 25,166 + 21,619 = 219,985 = img_001 / Note 7 total
#       Basis note: carrying value (branch A of the packet's Fork 2), per the C-1 ruling
#       text "off-curve at HFS". The DHT precedent (dht_2026-Q2.yaml, Bauhinia) is
#       REALIZED net price; agreed-price basis here would be Brugge+Brest 224,000 (Note 8)
#       + Donoussa 123,700 [DERIVED 49.4 + 74.3 gain, Note 26] + the two no-MoA hulls at
#       carrying = 394,485 (+174,500 = +$0.601/share) — NOT applied, recorded for the owner.
#       Ilma / Ingrid (VLCC) + Sienna (Suezmax), the Q1 HFS line 137,513, were DELIVERED in
#       Q2 (Note 6 img_015: gain USD 98.2M; Note 8: Sienna 2 Jun 2026, USD 29.2M) — OUT.
#   TOTAL = 301,244 + 312,680 + 264,585 + 154,217 + 219,985 = 1,252,711 (Q1: 912,136)
# Goodwill 177,022 (img_001) EXCLUDED (not a vessel asset). FSO is NOT here (see
# shuttle_contracted_book). Full-statement cross-foots reproduce: non-current 7,908,869 +
# current 919,020 = 8,827,889 = equity 3,120,994 + 4,887,666 + 819,229 (img_001/img_002).
working_capital_net: 1252711000

# Total interest-bearing debt EXCL. IFRS-16 leases — img_002 p.3 face amounts, itemised and
# footed to Note 16 img_031 p.32 (identical Q1 convention: sale-and-leaseback book inside
# "other borrowings"):
#   bank loans        non-current 2,869,323 + current 195,082 = 3,064,405
#   other borrowings  non-current 1,998,055 + current 180,981 = 2,179,036
#   other notes       current                                =   203,619
#   total                                                    = 5,447,060   (Q1: 5,238,160; +208,900)
#   Note 16 grand total 5,452,661 = 5,447,060 + leases 5,601 (foots).
# C-2: the secured FSO loan (Note 16 img_032 p.33, "Secured FSO loan 161.1M", SOFR+2.05%,
# 2030, facility 110,619 fully drawn, carrying 109,937) is INSIDE this figure and stays
# paired with shuttle_contracted_book below — removing one side without the other
# mis-states NAV by ~$0.72/share (App. B Finding 2). Fleet-wide encumbrance: "All vessels
# financed with bank loans are subject to a mortgage" (Note 12 img_027 p.28).
total_debt: 5447060000

# IFRS-16 lease liabilities: non-current 4,014 + current 1,587 = 5,601 (img_002; Note 16
# img_031 total 5,601). Q1: 6,232.
lease_liabilities: 5601000

# Newbuild book (§3.1 / §9.6). CONVENTION CHANGE this quarter: advances-only -> COMMITMENT-NET
# (newbuild_convention.yaml structural_exempt: CMBT "must move to commitment-net"; the engine
# subtracts this field, nav.py). Remaining capital commitment at 30 Jun 2026 — Note 12
# "Capital commitment" img_027 p.28: "USD 0.9 billion (December 31, 2025: USD 1.6 billion)",
# itemised (USD k), both axes footed:
#   tankers 78,540 | dry bulk 283,559 | container 29,570 | chemical 334,250 |
#   offshore wind 166,361 | other 8,557 = 900,837
#   by year: 2026 514,697 | 2027 136,359 | 2028 169,181 | 2029 80,600 = 900,837
# The Q1 comment's "~$1.2bn" is RETIRED by this cited figure. The 25 hulls under construction
# (Note 12 img_025 p.26: 1 VLCC, 6 Newcastlemax, 6 chemical, 3 CSOV, 1 MPASV, 2 CTV,
# 2 coasters, 1 x 1,400 TEU, 2 bitumen, 1 harbour vessel; aggregate USD 526.0M = marine AUC
# 525,998, Note 7) are NOT on the curve: four of the six classes have no §9.9 fit and the
# dry-bulk / offshore lines are not split per hull, so the obligation is booked and the
# asset is not (clause 2). Cost of this convention vs Q1: −$3.10/share.
newbuild_capex_commitments: 900837000

# Assets under construction at 30 Jun 2026 — img_001 p.2 / Note 12 img_025 p.26 (Q1: 759,807;
# transfers out of AUC 986,032 as the eleven H1 hulls delivered; marine 525,998 + other
# 6,662 (Note 7 img_017: port vessels / R&D / H2 infra — $0.023/share, convention-consistent
# with Q1, now disclosed). Falls IN THE SAME COMMIT as Morini, Cap Grace, Cap Joseph and the
# four Newcastlemaxes go on-curve (cmbt.yaml). Basis caveat: img_002 footnote — prepayments
# were reclassified into AUC and comparatives re-presented (Note 12 opens at 739,373 on the
# new basis); whether the Q1 6-K's 759,807 is on the same basis is UNVERIFIED (App. B
# Finding 7) — settled by the Q1-2026 6-K (filed 2026-05-19, not staged).
newbuild_advances_paid: 532660000

# Shares outstanding ex-treasury = 315,977,647 issued − 25,807,878 treasury = 290,169,769
# (Note 15 img_030 p.31) — UNCHANGED vs Q1. Treasury shares (284,508) unchanged (img_002).
diluted_shares_outstanding: 290169769

# No preferred equity: the equity section (img_002 p.3) is share capital / premium /
# reserves / treasury / retained earnings only; no NCI line.
preferred_equity: 0.0

# §15 governance: C-3 — haircut stays DECLINED (0.0). The Q1 tripwire "GOGL Bermuda appraisal /
# FourWorld Antwerp outcomes" FIRED inside H1 (Note 23 img_045 p.46) and is recorded, not
# actioned, because both outcomes went the company's way so far: Antwerp 30 Mar 2026
# "rejected in full FourWorld's requests"; Bermuda 21 May 2026 rejected the USD 14.49/share
# immediate-cash claim, recourse limited to s.106(6) appraisal, court expects "no material
# delta" — UNDER APPEAL, pleaded NOVEMBER 2026 (the live tripwire: re-open this field at the
# appeal outcome). Oceania/Black Swan: judgment reserved to end-2026, final ~end-2028.
# Management: no provision ("not more likely than not that an outflow… will be required").
# Other Q1 tripwires (fee creep, distribution backsliding, P/NAV<0.85, audit-committee
# independence) unchanged. Rationale: outputs/cmbt_onboarding/05_governance_s15.md.
governance_discount_pct: 0.0

# Off-curve FSO sleeve (§11.6): FSO Africa + FSO Asia (2002). Ownership RESOLVED this quarter
# — CONSOLIDATED, not JV: (i) the secured FSO loan sits in consolidated bank loans, Note 16
# img_032; (ii) fleet page img_073 p.21 "FSO 2" marked owned; (iii) Note 25 img_047/048
# equity-accounted investees total only 64,392 with no FSO. The Q1 conditional "zero this if
# JV" therefore does NOT fire. Newly citable: FSO average TC rate USD 88,540/day H1-2026
# (img_074 p.22) — a rate without a term. External check: a lender fully drew 110,619 against
# the pair to 2030 (Note 16 img_032), so 100M reads conservative. The FSOs are NOT in the
# crude manifest (cmbt.yaml off_curve_note) — no double-count against Vessels.
# The VALUE itself remains UNSOURCED (no carrying value, counterparty or expiry disclosed):
# this line is the deliberate remaining figure-provenance flag that keeps "cmbt" in
# NAV_FIGURE_ESTIMATE_QUEUE (tests/test_manifest_provenance.py) — do not launder the marker.
# Settled by: the FY2025 20-F FSO service-contract term/expiry, or a segment PP&E split.
shuttle_contracted_book: 100000000   # APPROX placeholder, C-2 keep — paired with the 109,937 FSO loan in total_debt
```

Cross-foots relied on (all USD k): cash 151,574 + 8,271 = 159,845 · debt 3,064,405 + 2,179,036 + 203,619 = 5,447,060; + 5,601 = 5,452,661 (Note 16) · op WC 301,244 · WC total 1,252,711 · HFS 123,800 + 49,400 + 25,166 + 21,619 = 219,985 · commitments six rows / four columns = 900,837 · AUC 525,998 + 6,662 = 532,660 · shares 315,977,647 − 25,807,878 = 290,169,769 · statement 7,908,869 + 919,020 = 8,827,889 = 3,120,994 + 4,887,666 + 819,229.

---

## 2. `inputs/fleet_manifests/cmbt.yaml` (full file)

```yaml
# CMB.TECH NV (CMBT, ex-Euronav) fleet manifest — METHODOLOGY §4.1, §11.9
# First crude + dry_bulk + containerships MULTI-SLEEVE hybrid (MULTI_SLEEVE_TICKERS).
# Q2 REFRESH — snapshot AS-OF 2026-06-30 (H1-2026 report, 6-K acc 0000919574-26-006193 filed
# 2026-09-04; page-image citations img_NNN per decisions/cmbt_q2_refresh_packet_2026-09-07.md).
# Fleet basis = the 30-JUNE fleet page (img_073 p.21) + Note 6 / Note 8 / Note 12 — NOT the
# 31-August table (img_059) and NOT the 8/27 press-release paragraphs (both post-NAV-date).
# Onboarding sources (per-vessel built years / dwt): FY2025 20-F "Our Fleet" (filed 2026-04-21)
# via outputs/cmbt_onboarding/{01_crude_fleet,02_drybulk_fleet,03_container_chem_offshore}.md.
# Onboarded 2026-06-26; Q1 snapshot 2026-03-31; advanced to Q2 2026-09-10.
#
# SCOPE = the 129 ON-CURVE vessels on the water at 2026-06-30:
#   - Crude sleeve (sectors.crude):       4 VLCC + 15 Suezmax = 19   (Q1: 4 + 16 = 20)
#   - Dry bulk sleeve (sectors.dry_bulk): 76 Cape-class (40 Newcastlemax + 36 Capesize)
#                                         + 30 Pana-class (26 Kamsarmax + 4 Panamax) = 106
#   - Container sleeve (sectors.containerships): 4 Ctr-Large (6,000 TEU) = 4
# OFF-CURVE (held at the balance-sheet level, NOT in this manifest — §11.9):
#   - 2 FSO (consolidated; fleet page img_073) -> shuttle_contracted_book
#   - 8 Bochem chemical (img_073) -> working_capital_net at 30-Jun segment book (Note 7 img_017)
#   - Windcat CSOV/CTV fleet (img_073: 60 CTV + 3 CSOV incl. newbuildings & chartered; owned
#     count not restated in the H1 report) -> working_capital_net at 30-Jun segment book
#   - 5 HELD-FOR-SALE at 30 Jun (Note 8 img_019 p.20): Donoussa VLCC; Stella, Brest, Brugge
#     Suezmax; Golden Myrtalia Capesize -> working_capital_net at IFRS-5 carrying value (C-1).
#     Ilma / Ingrid VLCC + Sienna Suezmax (the Q1 HFS trio) DELIVERED to buyers in Q2
#     (Note 6 img_015, Note 8 img_019) — gone from both files.
#   - the 25-hull multi-segment newbuild book (Note 12 img_025) -> commitment-net on the sheet
#   See balance_sheets/cmbt_2026-Q2.yaml for each off-curve line + rationale.
#
# Q1 -> Q2 BRIDGE (each hull individually dated in the filing):
#   ADDS  Morini VLCC 10 Jun (img_068; Note 6 img_015); Cap Grace 8 Apr, Cap Joseph 27 Apr
#         (img_067; Note 6 img_015); Mineral Latvija 11 May (img_067), Mineral Eesti 28 May,
#         Mineral Magyar 8 Jun (img_068), Mineral Lietuva 29 Jun (img_069) — Note 12 img_025:
#         "four Newcastlemax vessels (…), three VLCCs (Eburones, Menapii and Morini), two
#         Suezmax vessels (Cap Grace and Cap Joseph)". Eburones (12 Jan, img_065) and Menapii
#         (23 Mar, img_066) were already Q1 rows — age roll only.
#   OFF-CURVE (C-1) Donoussa 49.4M (Note 8); Brest + Brugge 123.8M COMBINED (Note 8 — never
#         split per hull); Stella residual ~21.6M [DERIVED, Note 7 − Note 8]; Golden Myrtalia
#         25,166k (Bocimar HFS column, Note 7 img_017). Stella and Golden Myrtalia were HFS
#         "since December 31, 2025" (Note 8) — the Q1 manifest carried both on-curve
#         (inherited Q1 error, ~46.8M [DERIVED] double-count at Q1).
#   REMOVED  CMBT_CAPE_2026 count 2 -> 4: the Q1 row's two hulls (Mineral Malta / Mineral
#         Europa) were NOT delivered in H1 — Note 12 img_025 lists exactly four H1 Newcastlemax
#         deliveries and "six Newcastlemax bulk carriers" still under construction; the 20-F
#         program was 10 at Dec-25 (02_drybulk_fleet.md:28-30): 10 − 4 = 6, 36 + 4 = 40 = the
#         30-June page. The Q1 "38 (+8NB)" was the Q1 6-K press-release paragraph (as-of PR
#         date). Inherited Q1 error #3 (~2 x 98.8M on-curve + still in AUC). The only residual
#         UNVERIFIED point is WHY that paragraph said 38 — settled by the Q1-2026 6-K fleet
#         table (not staged); it cannot change the 30-June count, which is triple-cited.
#   STAYS  Bristol (Suezmax 2024): sale announced 11 Aug 2026 (Note 26 img_049), absent from
#         Note 8 -> on the water at 30 Jun, on-curve at age 2.5.
#   Count check vs img_073: Suezmax 18 = 16 + 2 -> 15 on-curve after 3 HFS; VLCC 5 = 4 + 1
#   -> 4 after Donoussa; Newcastlemax 40 (+6 NB); Capesize 37 -> 36 after Golden Myrtalia;
#   Kamsarmax 26 + Panamax 4; container 4 (+1 NB). Σ rows = 129 = fleet_summary.on_curve_total.
#
# Class mapping: Newcastlemax + Capesize -> "Cape" value class; Kamsarmax + Panamax -> "Pana";
# 6,000 TEU box -> "Ctr-Large". Dry bulk is grouped by built-year cohort (count) — valuation is
# by age, so a cohort is exact; the per-vessel rosters (names/yards) are in 02_drybulk_fleet.md.
# Ages = 2026.5 − built_year (Q2 convention, as dht.yaml / sb.yaml). eco = built ≥ 2015.
# Scrubber UNDISCLOSED in the SEC filings and in the H1 report (default false). Yard-quality
# discount (§9.4) NOT applied in v1 (China-heavy dry-bulk book; Q3 refinement) — NAV is the
# "without yard discount" leg. dwt on Cape/Pana rows is LOAD-BEARING (dwt_scaled, §11.7.10):
# the 2026 Newcastlemaxes are filing-stated 210,000 dwt (img_067-069), not rounded.

ticker: CMBT
report_date: 2026-Q2
vessels:
  # ============================================================
  # CRUDE SLEEVE — 19 vessels (4 VLCC + 15 Suezmax) at 2026-06-30
  # Held-for-sale Donoussa (VLCC), Stella / Brest / Brugge (Suezmax) are OFF-curve (C-1).
  # ============================================================
  # ---- VLCC (4): −Donoussa (HFS, Note 8 img_019 "carrying value of USD 49.4 million") +Morini ----
  - {id: CMBT_VLCC_Atrebates, class: VLCC, dwt: 319000, age: 1.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}
  - {id: CMBT_VLCC_Eburones,  class: VLCC, dwt: 319000, age: 0.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}   # dely 12 Jan 2026 (img_065; Note 6 img_015)
  - {id: CMBT_VLCC_Menapii,   class: VLCC, dwt: 319000, age: 0.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}   # dely 23 Mar 2026 (img_066; Note 6 img_015)
  - {id: CMBT_VLCC_Morini,    class: VLCC, dwt: 319000, age: 0.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}   # ADD Q2: dely 10 Jun 2026 "VLCC Morini (2026 – 319,000 dwt)" (img_068; Note 6 img_015; Note 12 img_025). charter_status UNVERIFIED (20-F rows unnamed; sisters spot, 01_crude_fleet.md:70-71) — inert with charter_rate null (dividend_strip.py:95), NAV-neutral
  # ---- Suezmax (15): +Cap Grace +Cap Joseph; −Brest −Brugge (Note 8 MoAs 12 Jun 2026, "combined
  #      carrying value of USD 123.8 million" — no per-hull split) −Stella (Note 8, HFS since 31 Dec 2025) ----
  - {id: CMBT_SUEZ_CapTheodora,    class: Suezmax, dwt: 158819, age: 18.5, scrubber: false, eco: false, charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_Fraternity,     class: Suezmax, dwt: 157714, age: 17.5, scrubber: false, eco: false, charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_CaptainMichael, class: Suezmax, dwt: 157648, age: 14.5, scrubber: false, eco: false, charter_status: spot, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_Maria,          class: Suezmax, dwt: 157523, age: 14.5, scrubber: false, eco: false, charter_status: spot, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_CapCorpusChristi, class: Suezmax, dwt: 156600, age: 8.5, scrubber: false, eco: true, charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_CapPembroke,    class: Suezmax, dwt: 158826, age: 8.5,  scrubber: false, eco: true,  charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_CapPortArthur,  class: Suezmax, dwt: 156600, age: 8.5,  scrubber: false, eco: true,  charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_CapQuebec,      class: Suezmax, dwt: 156600, age: 8.5,  scrubber: false, eco: true,  charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_Cedar,          class: Suezmax, dwt: 157310, age: 4.5,  scrubber: false, eco: true,  charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_Cypres,         class: Suezmax, dwt: 157310, age: 4.5,  scrubber: false, eco: true,  charter_status: spot, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_Bristol,        class: Suezmax, dwt: 156851, age: 2.5,  scrubber: false, eco: true,  charter_status: spot, charter_rate: null, count: 1}   # STAYS: sale announced 11 Aug 2026 (Note 26 img_049), not HFS at 30 Jun
  - {id: CMBT_SUEZ_Helios,         class: Suezmax, dwt: 156790, age: 2.5,  scrubber: false, eco: true,  charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_Orion,          class: Suezmax, dwt: 156790, age: 2.5,  scrubber: false, eco: true,  charter_status: spot, charter_rate: null, count: 1}
  - {id: CMBT_SUEZ_CapGrace,       class: Suezmax, dwt: 156000, age: 0.5,  scrubber: false, eco: true,  charter_status: time_charter, charter_rate: null, count: 1}   # ADD Q2: dely 8 Apr 2026 "Cap Grace (2026 – 156,000 dwt)" (img_067; Note 6 img_015). TC per 20-F Our Fleet + Q1-2026 6-K 1-yr extension to 10-yr w/ profit split (01_crude_fleet.md:92,94); rate undisclosed
  - {id: CMBT_SUEZ_CapJoseph,      class: Suezmax, dwt: 156000, age: 0.5,  scrubber: false, eco: true,  charter_status: time_charter, charter_rate: null, count: 1}   # ADD Q2: dely 27 Apr 2026 "Cap Joseph (2026 – 156,000 dwt)" (img_067; Note 6 img_015). TC as Cap Grace

  # ============================================================
  # DRY BULK SLEEVE — 106 vessels, grouped by built-year cohort
  #   Cape class (76) = 40 Newcastlemax + 36 Capesize   (fleet page img_073: NMax 40 (+6 NB), Capesize 37 − Golden Myrtalia HFS)
  #   Pana class (30) = 26 Kamsarmax + 4 Panamax        (img_073: 26 + 4)
  # ============================================================
  # ---- Cape class (76): NMax 210k + Capesize 180k ----
  - {id: CMBT_CAPE_2010, class: Cape, dwt: 180000, age: 16.5, scrubber: false, eco: false, charter_status: spot, count: 3}
  # CMBT_CAPE_2011 (count 1 = Golden Myrtalia, 177,979 dwt, sole 2011 Capesize, 02_drybulk_fleet.md:78) REMOVED (C-1):
  #   Note 8 img_019 "held for sale since December 31, 2025"; carrying 25,166k = Bocimar HFS column, Note 7 img_017.
  - {id: CMBT_CAPE_2013, class: Cape, dwt: 180000, age: 13.5, scrubber: false, eco: false, charter_status: spot, count: 1}
  - {id: CMBT_CAPE_2014, class: Cape, dwt: 181000, age: 12.5, scrubber: false, eco: false, charter_status: spot, count: 11}
  - {id: CMBT_CAPE_2015, class: Cape, dwt: 181000, age: 11.5, scrubber: false, eco: true,  charter_status: spot, count: 8}
  # 2016/2017 cohorts split NMax vs Capesize (dwt is load-bearing — §11.7.x dwt-scaling)
  - {id: CMBT_CAPE_2016_nmax, class: Cape, dwt: 211000, age: 10.5, scrubber: false, eco: true, charter_status: spot, count: 2}
  - {id: CMBT_CAPE_2016_cape, class: Cape, dwt: 181000, age: 10.5, scrubber: false, eco: true, charter_status: spot, count: 5}
  - {id: CMBT_CAPE_2017_nmax, class: Cape, dwt: 208000, age: 9.5,  scrubber: false, eco: true, charter_status: spot, count: 1}
  - {id: CMBT_CAPE_2017_cape, class: Cape, dwt: 181000, age: 9.5,  scrubber: false, eco: true, charter_status: spot, count: 3}
  - {id: CMBT_CAPE_2018, class: Cape, dwt: 180500, age: 8.5,  scrubber: false, eco: true,  charter_status: spot, count: 5}
  - {id: CMBT_CAPE_2019, class: Cape, dwt: 208400, age: 7.5,  scrubber: false, eco: true,  charter_status: spot, count: 2}
  - {id: CMBT_CAPE_2020, class: Cape, dwt: 209000, age: 6.5,  scrubber: false, eco: true,  charter_status: spot, count: 10}
  - {id: CMBT_CAPE_2021, class: Cape, dwt: 210000, age: 5.5,  scrubber: false, eco: true,  charter_status: spot, count: 3}
  - {id: CMBT_CAPE_2023, class: Cape, dwt: 210200, age: 3.5,  scrubber: false, eco: true,  charter_status: spot, count: 2}
  - {id: CMBT_CAPE_2024, class: Cape, dwt: 210000, age: 2.5,  scrubber: false, eco: true,  charter_status: spot, count: 8}
  - {id: CMBT_CAPE_2025, class: Cape, dwt: 210000, age: 1.5,  scrubber: false, eco: true,  charter_status: spot, count: 8}
  - {id: CMBT_CAPE_2026, class: Cape, dwt: 210000, age: 0.5,  scrubber: false, eco: true,  charter_status: spot, count: 4}
    # = Mineral Latvija 11 May (img_067), Mineral Eesti 28 May, Mineral Magyar 8 Jun (img_068), Mineral Lietuva 29 Jun
    # (img_069), each "(2026 – 210,000 dwt)"; Note 6 img_015; Note 12 img_025. Was count 2 (Malta/Europa) at Q1 —
    # NOT delivered in H1 per Note 12 (four H1 deliveries, six still under construction); see the header bridge.
  # ---- Pana class (30): Kamsarmax 82k + Panamax 74k — unchanged roster (img_073: 26 + 4), ages +0.25 ----
  - {id: CMBT_PANA_2011, class: Pana, dwt: 82188, age: 15.5, scrubber: false, eco: false, charter_status: spot, count: 2}
  - {id: CMBT_PANA_2012, class: Pana, dwt: 81500, age: 14.5, scrubber: false, eco: false, charter_status: spot, count: 3}
  - {id: CMBT_PANA_2013, class: Pana, dwt: 80000, age: 13.5, scrubber: false, eco: false, charter_status: spot, count: 3}
  - {id: CMBT_PANA_2014, class: Pana, dwt: 84970, age: 12.5, scrubber: false, eco: false, charter_status: spot, count: 1}
  - {id: CMBT_PANA_2015, class: Pana, dwt: 84978, age: 11.5, scrubber: false, eco: true,  charter_status: spot, count: 1}
  - {id: CMBT_PANA_2017, class: Pana, dwt: 74500, age: 9.5,  scrubber: false, eco: true,  charter_status: spot, count: 2}
  - {id: CMBT_PANA_2020, class: Pana, dwt: 81000, age: 6.5,  scrubber: false, eco: true,  charter_status: spot, count: 5}
  - {id: CMBT_PANA_2021, class: Pana, dwt: 80580, age: 5.5,  scrubber: false, eco: true,  charter_status: spot, count: 3}
  - {id: CMBT_PANA_2023, class: Pana, dwt: 84510, age: 3.5,  scrubber: false, eco: true,  charter_status: spot, count: 6}
  - {id: CMBT_PANA_2024, class: Pana, dwt: 84990, age: 2.5,  scrubber: false, eco: true,  charter_status: spot, count: 4}

  # ============================================================
  # CONTAINER SLEEVE — 4 vessels (6,000 TEU, Delphis), all 10-yr TC to CMA-CGM (img_073: post-panamax 4; +1 feeder NB off-curve)
  # ============================================================
  - {id: CMBT_CTR_MasaiMara, class: Ctr-Large, dwt: 80000, age: 3.5, scrubber: false, eco: true, charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_CTR_Zingaro,   class: Ctr-Large, dwt: 80000, age: 2.5, scrubber: false, eco: true, charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_CTR_Etosha,    class: Ctr-Large, dwt: 80000, age: 2.5, scrubber: false, eco: true, charter_status: time_charter, charter_rate: null, count: 1}
  - {id: CMBT_CTR_Dolomites, class: Ctr-Large, dwt: 80000, age: 2.5, scrubber: false, eco: true, charter_status: time_charter, charter_rate: null, count: 1}

# Share of fleet on spot, by class (not used by NAV; drives the single-point strip spot/TC
# blend). Values HELD at Q1; newest cover print = Q3-QTD fixed VLCC 83% / Suezmax 73% (8/27
# release, acc 0000919574-26-005821, pr827.txt) — strip-side update batched with the next
# strip refresh, not this NAV pair.
spot_coverage_pct:
  VLCC: 0.50
  Suezmax: 0.50
  Cape: 0.70
  Pana: 0.70
  Ctr-Large: 0.0

fleet_summary:
  on_curve_total: 129          # MUST equal Σ vessel-row counts (cross-foot gate): 4 + 15 + 76 + 30 + 4
  VLCC_count: 4
  Suezmax_count: 15
  Cape_count: 76               # 40 Newcastlemax + 36 Capesize (img_073: 40 (+6 NB) / 37 − 1 HFS)
  Pana_count: 30               # 26 Kamsarmax + 4 Panamax
  Ctr_Large_count: 4
  held_for_sale: 5             # Donoussa, Stella, Brest, Brugge, Golden Myrtalia — values on the sheet (Note 8 img_019 / Note 7 img_017)
  off_curve_note: "2 FSO + 8 chemical + Windcat CSOV/CTV fleet + 5 HFS (Donoussa, Stella, Brest, Brugge, Golden Myrtalia) held at the balance-sheet level (§11.9); Ilma/Ingrid/Sienna delivered Q2-2026"
```

**Dry-sleeve cross-foot — which side changed and why:** the ROWS changed (`CMBT_CAPE_2026` 2 → 4, not 6) and the summary follows Σ rows = 129 / Cape 76, which equals the 30-June page. The packet's draft encoded 42 in rows over a 40 summary; the verification proposed 131/78 "because 40 has no per-hull support". It does: the 20-F names the ten 2026-build hulls, Note 12 names the four delivered and counts six remaining, and the H1 timeline carries no Q1 Newcastlemax delivery. The unsupported figure was the Q1 row's Malta/Europa, which rested only on a press-release paragraph.

---

## 3. Pre-registration band for the regen

Basis: HEAD scorecard (`outputs/book_scorecard.json`, source_commit 0e6c518, balance_sheet_vintage 2026-Q1) NAV/share **$16.54** (NAV total 4,799.2M; in-memory reproduction 16.5394 on the transaction-anchored curves, by-class fleet values identical to `outputs/cmbt_fv_report.md`). Shares 290,169,769 unchanged. Curves, prices and weights do not enter NAV; the regen's fresh price vintage is NAV-invariant.

| Mover | USD M | $/share |
|---|---:|---:|
| Five HFS hulls off-curve at their Q1 marks (Donoussa 103.89, Brest 102.01, Brugge 102.01, Stella 50.44, Golden Myrtalia 35.58) | −393.9 | −1.358 |
| Malta/Europa removed (2 × 98.76 at age 0.25) | −197.5 | −0.681 |
| Adds at age 0.5: Morini 178.13, Cap Grace 117.25, Cap Joseph 117.25, 4 NMax × 97.68 = 390.72 | +803.4 | +2.769 |
| Age roll +0.25 on the 122 surviving hulls | −96.0 | −0.331 |
| **Fleet net** (8,068.8 → 8,184.7) | **+115.9** | **+0.399** |
| cash 202.871 → 159.845 | −43.0 | −0.148 |
| working capital 912.136 → 1,252.711 (HFS +219.985, Q1 HFS trio −137.513, op WC +131.845, Bochem +36.306, Windcat +68.043, Investments +21.909) | +340.6 | +1.174 |
| debt 5,238.160 → 5,447.060 | −208.9 | −0.720 |
| leases 6.232 → 5.601 | +0.6 | +0.002 |
| AUC 759.807 → 532.660 | −227.1 | −0.783 |
| commitments 0 → 900.837 | −900.8 | −3.104 |
| **Balance-sheet net** | **−1,038.7** | **−3.580** |
| **ΔNAV** | **−922.8** | **−3.180** |

**Prediction (as instructed, commitments booked): NAV/share $16.54 → $13.36, DOWN 19.2%; band $13.26–$13.46 (±$0.10 ≈ ±$29M, the size of one mid-age Suezmax mark).** Fleet by class expected: VLCC 701.3 / Suezmax 1,247.9 / Cape 4,933.2 / Pana 1,045.9 / Ctr-Large 256.5; NAV total 3,876.4M.
Alternative if the owner keeps Fork 3 Branch A (commitments 0, figure as provenance only): **$16.46, band $16.36–$16.56** (ΔNAV −$0.076; NAV total 4,777.3M). The two readings differ by exactly 900,837k / 290,169,769 = $3.104.

Gate consequences to expect and annotate in `decisions/cmbt_log.md` BEFORE the regen: ΔNAV −19.2pp (drift gate UNEXPLAINED unless annotated), sleeve shares still dry-bulk-dominant (Cape+Pana ≈ 73% of fleet value — `test_cmbt` dominance holds), the SANITY ±50% band vs broker NAV $20.14 holds at either reading (−34% / −18%).

**A landing outside the band = HALT for input investigation, never output adjustment.** Candidates, in order: a curve/transaction print landed between HEAD and the regen (re-run `--txn-comparison`, not this pair); a row not matching this file (diff the manifest against §2); the sheet loaded at the wrong vintage (pair guard / `balance_sheet_vintage` in the scorecard must read 2026-Q2). Nothing here licenses touching marks or the sheet to land inside the band.

---

## 4. Open items (one line each)

- **Fork 3 was never in `inputs/forks.yaml`** — the −$3.10/share commitment-net switch is executed on the orchestrator's instruction, not a silence ruling; owner to confirm or revert to Branch A (0) at the regen.
- Landing commit must also carry: `tests/test_cmbt.py` (load `"2026-Q2"`; Suezmax 15, Cape 76, total 129), `tests/test_quarter_coherence.py:244-247` (CMBT leaves the lagging pin; TEN remains), `tests/test_newbuild_convention.py` (`"CMBT"` out of `OFF_CONVENTION_QUEUE`) and the `newbuild_convention.yaml` CMBT reason text; a fresh price vintage committed ALONE first (CLAUDE.md 2026-07-26 rule).
- `shuttle_contracted_book` 100,000,000 remains an uncited placeholder (C-2 keeps it; `cmbt` stays in `NAV_FIGURE_ESTIMATE_QUEUE`) — settled by the FY2025 20-F FSO contract term/expiry.
- Stella carrying value is a residual (~21.6M [DERIVED]); Brest/Brugge have no per-hull split — settled by the FY2026 20-F Note 8 per-vessel HFS table.
- Why the Q1 6-K press release said "38 (+8NB)" when the reviewed H1 notes imply 36 at 31 March — settled by the Q1-2026 6-K fleet table (filed 2026-05-19, not staged); same document settles the AUC reclassification basis (App. B Finding 7).
- Morini charter status (drafted spot) — settled by the FY2026 20-F "Our Fleet"; inert with `charter_rate: null`.
- Windcat owned-vessel count at 30 June (Q1 "47") not restated in the H1 report — the segment book is used, so NAV-neutral; settled by the FY2026 20-F.
- Filing fetcher silently stages image-only exhibits as empty shells (App. A §0) — fix before the next image-rendered CMBT filing.
- Three inherited Q1 mis-scopes to log (Stella + Golden Myrtalia HFS since Dec-25, ~46.8M; Malta/Europa undelivered, ~197.5M; both double-counted against Q1 AUC/HFS) — a Q1 re-ratification cause, not a Q2 input.
---
# APPENDIX B — verification

**VERDICT: WRITE WITH CORRECTIONS** — both files are sound as drafted (every NAV-moving figure re-read off the page image; all cross-foots reproduce; the band reproduces to the cent on HEAD curves; Fork 4 now settles AT SOURCE in the work's favour). The corrections are to four comment/packet lines and the landing checklist; none is CORRUPTING. One item (Fork 3, −$3.10/share) needs the owner's word, not silence, before the regen.

## Verification done (sources opened by me)

- Page images read: img_001, 002, 015, 017, 019, 025, 027, 030, 031, 032, 049, 059, 065–069, 073 (`scratchpad/pages/`).
- Q1-2026 6-K fetched from EDGAR (acc **0000919574-26-003591**, `d12164570_ex99-1.htm`, filed 2026-05-19) — the document the work called "not staged".
- Draft yamls loaded through the repo's own loaders (`load_fleet_manifest` / `load_balance_sheet` on a scratch copy) and valued with `compute_nav` after `_maybe_apply_transactions` on HEAD inputs; `git status` clean before and after.

## (1) Sheet — every field cited, matches the packet, cross-foots

| Field | Draft | Image check |
|---|---|---|
| cash 159,845 | 151,574 + 8,271 | img_001 ✓ |
| operating WC 301,244 | 120,674 + 415,688 + 2,828 − 235,139 − 2,807 | img_001/002 ✓ (recomputed) |
| Bochem 312,680 / Windcat 264,585 / HFS 194,819 + 25,166 = 219,985 / AUC 525,998 + 6,662 = 532,660 | Note 7 | img_017 ✓ |
| Investments 154,217 | statement line | img_001 ✓ |
| WC total 1,252,711 | Σ five components | recomputed ✓ |
| debt 5,447,060 | 2,869,323 + 195,082 + 1,998,055 + 180,981 + 203,619; + 5,601 = 5,452,661 | img_002 + img_031 ✓ |
| commitments 900,837 | six rows AND four year-columns both foot | img_027 ✓ |
| AUC 532,660; transfers 986,113/(986,032); HFS transfer (173,196) | Note 12 | img_025 ✓ |
| shares 290,169,769 = 315,977,647 − 25,807,878 | Note 15 | img_030 ✓ |
| preferred 0 | equity section | img_002 ✓ |
| FSO loan 109,937 (facility 110,619 drawn, SOFR+2.05%, 2030) | Note 16 | img_032 ✓ |
| Note 8 (Donoussa 49.4M; Brugge+Brest 224.0/123.8/100.2 combined; Stella + Golden Myrtalia "since December 31, 2025"; Sienna 2 Jun, 29.2M) | | img_019 ✓ verbatim |
| Note 26 (14 Jul Windcat 65; 3 Aug Donoussa 74.3M Q4; 11 Aug Bristol 56.9M Q4) | | img_049 ✓ verbatim; Bristol absent from Note 8 ✓ |
| Note 6 Brest/Brugge "delivered in the third quarter of 2026" | | img_015 ✓ |

Provenance regexes run over the draft text (`tests/test_manifest_provenance.py` regexes): no unbacked `confirmed/verified` claim in either file ✓; the sheet flags on exactly two lines — the intended `shuttle_contracted_book` APPROX line and **one unintended line** (Finding A).

## (2) Off-curve moves — individually sourced vs aggregate

- Donoussa 49,400: individually sourced (Note 8, img_019). ✓
- Golden Myrtalia 25,166: segment-pinned (Bocimar HFS column, img_017; sole Bocimar hull in Note 8). ✓
- **Brugge + Brest 123,800: kept COMBINED, never split** — the hard-failure check passes. ✓
- Stella 21,619: residual, flagged `[DERIVED]`, ±0.1M cross-check to the Note 12 transfer (219,985 − 173,196 − 25,166 = 21,623). ✓ (Nit: App. C said "never write it at thousand precision"; the sheet lists 21,619 with the ±0.1M note — acceptable, RECOVERABLE.)
- Foot 123,800 + 49,400 + 25,166 + 21,619 = 219,985 = img_001. ✓

## (3) Manifest

- Loader-parsed counts: VLCC 4 / Suezmax 15 / Cape 76 / Pana 30 / Ctr-Large 4 = **129** = `on_curve_total`. ✓ Suezmax roster = 13 survivors + Cap Grace + Cap Joseph; VLCC = Atrebates, Eburones, Menapii, Morini. ✓
- Ages: every surviving row = Q1 + 0.25; adds at 0.5 (2026.5 − 2026); Bristol 2.5. ✓ Filing-stated dwt for the seven adds (img_067/068/069: 156,000 / 319,000 / 210,000). ✓
- `report_date: 2026-Q2` paired with `quarter: 2026-Q2`; `load_company_inputs` pair guard passes on the scratch pair. ✓ `scripts/check_snapshot_advance.py` will not fire (report_date line changes). ✓
- img_059 (31 Aug: 46 NMax / 16 Suezmax / 6 VLCC / 18.28 USD) — none of those figures appears in either file. ✓
- **Dry cross-foot resolved on the correct side — now CONFIRMED at source, not by inference.** The Q1 6-K (acc 0000919574-26-003591, ex99-1) says verbatim "Bocimar has 38 (+8NB) Newcastlemaxes on the water (average age 3.2y)", but **its own delivery table lists Mineral Latvija (11 May 2026) as the only Newcastlemax delivery and names no Mineral Malta / Mineral Europa**. So the "38" is unsupported by the same document's table. H1 Note 12 (four H1 deliveries, "six Newcastlemax bulk carriers" under construction, img_025/027), the 30-June page (40 + 6, img_073) and the H1 timeline (no Q1 NMax on img_065/066) all give 36 → 40. Rows = 4 is right; 131/78 (App. D) would have been the error. The work may now cite the Q1 6-K accession and drop "not staged" (Finding D).

## (4) Pre-registration band — reproduced exactly

HEAD Q1: **16.5394**; fleet 8,068.8; by-class VLCC 635.5 / Suezmax 1,282.2 / Cape 4,835.6 / Pana 1,058.2 / Ctr 257.2 (= `outputs/cmbt_fv_report.md`). Q1 marks: Donoussa 103.89, Brest/Brugge 102.01, Stella 50.44, Golden Myrtalia 35.58, CAPE_2026 98.76 each. Q2 draft on HEAD curves: **13.3592** (fleet 8,184.7; VLCC 701.3 / Suezmax 1,247.9 / Cape 4,933.2 / Pana 1,045.9 / Ctr 256.5); Morini 178.13, Cap Grace/Joseph 117.25, NMax 97.68; survivor age-roll −96.0M on 122 hulls. Branch A (commitments 0): **16.4637**. Sleeve shares crude 0.238 / dry_bulk 0.731 / containerships 0.031 (`test_cmbt` dominance holds). Every number in the work's table is CONFIRMED; band $13.26–$13.46 (or $16.36–$16.56) stands.

## (5) Q1 carry-forward — nothing silently vanished

All ten Q1 sheet fields present with a Q2 value and rationale; `spot_coverage_pct`, `fleet_summary`, `off_curve_note` carried. The Q1 "15 Windcat JV CTVs" is inside the Investments-line convention (disclosed). One thing the Q1 6-K now proves in the work's favour: its 31-Mar "Non-current assets held for sale 137,513" is the **carrying** balance (necessarily incl. Stella + Golden Myrtalia), so the Q1 sheet's "at agreed price" label was wrong and Q2's carrying basis is continuity with what Q1 actually did.

## Findings

**A. Sheet line 104 trips the NB-context estimate regex (RECOVERABLE, fix before writing).** `# The Q1 comment's "~$1.2bn" is RETIRED by this cited figure. The 25 hulls under construction` — contains "under construction" + "~" + money and no `CITATION_RE` token (`test_manifest_provenance.py:110-135`; confirmed by running the regex). Harmless today (cmbt is queued for the FSO APPROX anyway) but it would keep `cmbt` xfail-red after the FSO line is sourced, so the queue could never clear by sourcing. Corrected line:
`# The Q1 comment's "~$1.2bn" is RETIRED by the Note 12 img_027 figure above. The 25 hulls under construction`

**B. Fork 3 (commitments 900,837 booked, −$3.10/share) has no ruling (RECOVERABLE, owner-word-gated).** Not in `inputs/forks.yaml`; the registry's own text (`inputs/market_data/newbuild_convention.yaml` CMBT: "must move to commitment-net (own pre-reg)"; GSL entry: "joins CMBT's pending commitment-net pre-reg (owner fork)") expects a CMBT pre-reg + owner fork that does not exist. The number is fully cited and both bands are quoted, so the file is safe either way — but landing it on "orchestrator's instruction" contradicts the "silence executes" doctrine, which only covers forks in the registry. Either the owner says the word (then remove `"CMBT"` from `OFF_CONVENTION_QUEUE`, update the CMBT and GSL registry reasons) or land Branch A (`newbuild_capex_commitments: 0`, 900,837 in the comment) at $16.46 ± 0.10.

**C. Uncited gate figure (RECOVERABLE).** The §3 gate line's "broker NAV $20.14" traces to nothing: `inputs/watchlist.yaml:293-298` (Pareto 28 Aug 2026: price 18.3 / pnav 0.86 → 21.28) and the HEAD scorecard row (`broker_nav: 22.5` = 19.35/0.86). SANITY still OK at either reading (13.36/22.5 = −41%; 16.46/22.5 = −27%). Replace $20.14 with the scorecard's 22.5.

**D. Tighten two UNVERIFIED caveats with the Q1 6-K now in hand (RECOVERABLE, improves the file).** (i) Manifest bridge: cite acc 0000919574-26-003591 for the "38 (+8NB)" sentence and its Latvija-only delivery table; delete "not staged". (ii) Sheet AUC caveat (App. B Finding 7): the Q1 6-K's Dec-25 AUC comparative is 738,298 vs the H1 re-presented Jan-1 739,373 — the prepayment reclassification is ≤1.1M at the opening balance, so 759,807 → 532,660 is on essentially the same basis. Replace "UNVERIFIED … not staged" with that sourced comparison.

**E. Landing checklist omissions (RECOVERABLE).** (i) `inputs/forks.yaml` `cmbt_q2_c1_c2_c3` status → `executed` citing the commit, same commit (policy header, forks.yaml:1-4). (ii) The sheet header's "silence past 2026-09-10" mis-phrases the rule: `sentinel.py:363-364` fires on `execute_after <= today`, i.e. executable ON 2026-09-10 — reword to "on/after 2026-09-10". (iii) `newbuild_convention.yaml` GSL reason text goes stale if B lands.

**F. HFS basis is under-determined by the ruling text (RECOVERABLE, flag only).** "off-curve at HFS" was read as IFRS-5 carrying. Note `nav.py:72/121` defines the schema's own `held_for_sale` field as "agreed-sold vessels at contracted price (§4.2)" (LPG Clermont trio at realisable, `test_lpg.py:49`; DHT Bauhinia at realized net, `dht_2026-Q2.yaml:19-29`). Brugge + Brest had a signed MoA (12 Jun) **before** the NAV date → a contracted 224.0M exists at 30 Jun; carrying understates them by 100.2M (**$0.345/share**). Donoussa (MoA 15 Jul) and Stella / Golden Myrtalia (no MoA) have carrying as their only citable basis. §4.2-consistent line: HFS 320,185 → NAV +$0.345 vs the draft. The draft's choice is disclosed, conservative and continuous with Q1's actual (carrying) practice — the owner's call, not a defect.

**G. Nits (RECOVERABLE).** "REMOVED CMBT_CAPE_2026 count 2 -> 4" heading reads as a removal of the row; it is a recount. Golden Myrtalia Q1 dwt 180,000 vs filing 177,979 is mooted by removal.

Nothing found is CORRUPTING. Files not touched; `git status` clean.