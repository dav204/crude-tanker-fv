# TEN — full balance-sheet reconciliation, PRE-REGISTRATION (2026-07-15)

Ninth full reconciliation (Tsakos Energy Navigation), the first worked from the post-P0 queue
(`NAV_FIGURE_ESTIMATE_QUEUE` "structural/not-yet-worked" residue). Requested by the
portfolio-governance sizing analysis (`../portfolio-governance/analysis/2026-07-15-ten-ccec-trmd-sizing.md`
gate (ii): a TEN entry card is gated on this reconciliation; tranche-1 window ~mid-August, so waiting
for the H1 6-K [~September] has a real cost). **Reconciliation is analysis; any baseline re-ratify is
owner-gated and is NOT executed here.**

Sources (fetched 2026-07-15, archived `inputs/research_issuer/ten/`):
- **Q1-2026 6-K** ex-99.1 (EDGAR acc 0001193125-26-236934, filed 2026-05-22) — condensed Mar-31-2026
  balance-sheet data + subsequent events + NB program table.
- **FY2025 20-F** (acc 0001193125-26-144027, filed 2026-04-06) — audited Dec-31-2025 balance sheet,
  Note 3/leases detail (via financial-statement notes), Note 11 NCI, Note 12 commitments, Note 17
  subsequent events.
- TEN Data Kit (May 11, 2026) — already cited in the manifest; NOT needed for any balance-sheet figure
  after this reconciliation (every NAV-driving figure now traces to a filing).

## §0 — Vintage decision: reconcile NOW, at the Mar-31-2026 vintage

TEN files full detailed balance sheets semi-annually, but the premise that the Mar-31 balance sheet is
unavailable is **false**: the Q1-2026 6-K discloses a condensed consolidated balance sheet (Cash /
Other assets / Vessels,net / Advances for vessels under construction / Debt net / Other liabilities /
Equity) with Dec-31-2025 comparatives. Every NAV-driving aggregate is issuer-published at Mar-31.
The onboarding log (ten_log 2026-06-05 "Now-complete schema readiness") had ALREADY extracted these
exact figures — the YAML that got built used data-kit/roll-forward estimates instead. Waiting for the
H1 6-K would buy only composition detail (WC split, Ulysses completion accounting, the Arctic/Antarctic
repurchase execution) — all scheduled September-refresh work anyway. Decision: **reconcile now against
the Q1 6-K + FY2025 20-F; H1 refresh re-verifies in September.**

## §1 — Subsequent-events audit FIRST (the ASC/HAFN/TRMD discipline)

**20-F Note 17** (covers Jan-1 → Apr-6-2026, i.e., nearly all of Q1 — unusually useful):
- (b) **Jan-12-2026: MR `Delos T` DELIVERED** — Q1 event. Manifest already carries it (age 0.2) ✓.
- (h) **Feb-12-2026: MR `Dion` DELIVERED** — Q1 event. Manifest already carries it (age 0.1) ✓.
- (c) **Jan-22-2026: MOA SIGNED for the sale of VLCC `Ulysses`** — a **Q1 event**: at Mar-31 the vessel
  is sale-agreed (HFS). The manifest carries it as operating on-curve — the SB/ASC pattern in mirror
  (an in-quarter sale left on the curve). Correction below.
- (j) **Feb-25-2026: shipbuilding contract for +1 LNG carrier (Hull 3643, HHI)** — Q1 event; the
  manifest's 19-NB orderbook note already includes it ✓; its instalments are inside Mar-31 advances.
- (d,f,g,m,n,o) Q1 investments in bonds/debt securities totaling ~$36M — inside Mar-31 Other assets ✓
  (part of the WC composite move).

**Q1 6-K subsequent events** (post-Mar-31 — must stay OUT of the snapshot):
- **Apr-7-2026:** agreed to repurchase the two 2007-built SLB suezmaxes (Arctic + Antarctic) "at prices
  below current fair market value" — Q2 event; the pair returns to the owned fleet at the H1 refresh.
- **Apr-23-2026:** DP2 shuttle employment extensions (Brasil 2014 / Rio 2016) — already reflected as the
  APPROX $60k/d extension assumption in `shuttle_contracted_book`; unchanged here.
- **May-20-2026:** Ulysses sale COMPLETED, "about $83 million in free cash after repayment of existing
  debt" — Q2 cash event; the gain lands at H1. At Mar-31 the vessel is HFS at carrying value.

## §2 — Sourced figures ($K, 31-Mar-2026)

| Field | Model (basis) | **Sourced** | Citation |
|---|---|---|---|
| `cash_and_equivalents` | 321,416 ✓ | **321,416** | 6-K BS "Cash" — verified exact |
| `working_capital_net` | 28,000 (20-F Dec-31 roll-forward, "minimal Q1 movement" assumed) | **174,654** | 6-K BS composite: Other assets 331,398 − Other liabilities 156,744. Basis VALIDATED at Dec-31: 197,009 − 169,101 = 27,908 ≈ the prior 28,000 — same construction, so the +146.7M is a real Q1 swing (Ulysses HFS reclass into Other assets, ~$36M securities investments [20-F Note 17 d/g/m/n/o], EUA/trade receivables, seller's credits $12.8M), not a basis artifact |
| `total_debt` | 2,148,200 (data kit "expected outstanding") | **2,136,109** | 6-K BS "Debt and other financial liabilities, net of deferred finance costs" (incl. Tenergy SL financing) — BS carrying convention per TRMD precedent |
| `lease_liabilities` | 0 ✓ | **0** | RoU = obligation for the 3 op-leases (20-F: $7,770 current at Dec-31), nets inside the WC composite |
| `newbuild_capex_commitments` | 0 (convention) | **0** | Convention unchanged (delivered-value = contract-price, §11.6/§3.1 conservative read). Corroboration: 20-F Note 12 = $1,968,298 remaining for 20 hulls at Dec-31; Mar-31 = 19 pending (2 MR delivered, 1 LNG added) |
| `newbuild_advances_paid` | ~400,000 `[EST between 301.9 (20-F) and 430 (data kit)]` | **442,740** | 6-K BS "Advances for vessels under construction" — the $128M-range estimate resolves to an issuer print $42.7M ABOVE the booked value |
| `preferred_equity` | 287,328 | **333,282** | 287,328 preferred (E 4,745,947 + F 6,747,147 × $25.00, 20-F share counts verified by the $6.75M/q dividend) **+ 45,954 NCI** (20-F BS Non-controlling interest 43,529 at Dec-31 + Q1 attrib income 2,425 per 6-K; Note 11: 49% of Mare Success S.A. [Selini/Salamina/Byzantion/Bosporos] held by Polaris/Flopec; zero distributions in FY2025). NCI-via-`preferred_equity` = the BWLP ratified convention |
| `held_for_sale` | 0 | **0 (deliberate)** | Ulysses HFS carrying value sits INSIDE the WC composite (Other assets) — counted once, at carrying, conservative vs both the curve mark and the contracted price. Gain recognized at H1 |
| `diluted_shares_outstanding` | 30,127,603 ✓ | **30,127,603** | 20-F: 30,805,776 issued − 678,173 treasury; no Q1 buyback/issuance disclosed (6-K wtd-avg 29,971,603 is the EPS denominator, not EOP) |

## §3 — Manifest corrections (ownership, AS-OF 2026-03-31)

The 20-F proves TEN does **not own** four manifest vessels curve-marked as owned steel:

| Vessel | Fact | Citation | Txn-anchored mark removed | Base mark removed |
|---|---|---|---|---|
| `TEN_VLCC_Ulysses` | Sale MOA signed Jan-22-2026 → HFS at Mar-31 (carrying value inside WC composite) | 20-F Note 17(c); 6-K subs. events (completion May-20) | $97.6M | $117.1M |
| `TEN_SUEZ_Arctic` | SLB Jun-21-2021 (pair net sale price $52,304), ASC 842 TRUE SALE op lease to ~Jun-2026; RoU-not-vessel on the audited BS | 20-F leases note; BS RoU $4,329 | $34.9M | $38.9M |
| `TEN_SUEZ_Antarctic` | same SLB pair — the YAML note "Antarctic expired during Q1" is WRONG (wtd-avg remaining term 0.48y at Dec-31 → ~Jun-2026) | same | $35.6M | $39.8M |
| `TEN_AFRA_SakuraP` | SLB Dec-21-2020 ($24,527), extended Sep-19-2025 to ~Dec-2026; TRUE SALE op lease | 20-F leases note; BS RoU $3,441 | $30.1M | $33.0M |

Convention precedent: chartered-in/leased-in steel is NEVER in NAV (2343 chartered-in book excluded;
CMDB CBI platform "P&L-only, never in the manifest"). TEN retains: the lease-period economics (net ≈ 0
via RoU/obligation inside the composite), the seller's credits ($12.8M ST receivables — inside the
composite ✓), and the below-FMV repurchase rights (Arctic+Antarctic exercise agreed Apr-7 → the pair
RE-ENTERS the owned fleet at the H1 refresh, likely with a below-FMV gain — pre-flagged so the
round-trip does not read as churn). Fleet cross-foot after correction: 56 on-curve owned + 4 shuttle
off-curve + 3 chartered-in (excluded) + 1 HFS (excluded) = **64 operated = the 6-K/data-kit count** ✓.
Sleeve effects: crude 41 → 37 (2 VLCC + 14 conv Suezmax + 21 Aframax); product/LNG untouched;
spot fractions recomputed (Suezmax 2/14 = 0.143, Aframax 3/21 = 0.143, VLCC 0.00 unchanged).

## §4 — PRE-REGISTERED PREDICTION (committed BEFORE recompute)

Balance-sheet deltas ($K): WC **+146,654** · debt **+12,091** · advances **+42,740** · NCI **−45,954**
= +155,531. Manifest steel removed: **−198,200** (txn-anchored) / **−228,800** (base).

- Net headline (txn-anchored): −42,669 ÷ 30,127,603 sh = **−$1.42/sh**.
  **Headline NAV/sh $88.76 → predicted ~$87.34 (band $86.8 – $87.9).**
- Net base: −73,269 ÷ 30,127,603 = **−$2.43/sh**.
  **Base NAV/sh $97.01 → predicted ~$94.58 (band $94.0 – $95.2).**
- Scenario PW FV: expected DOWN somewhat more than NAV (the strip loses Ulysses' $138k/d TC + three
  older hulls' earnings; partially offset by the +$201.5M asset-side lift). Position expected
  **BUY intact** (EV point ~+38-44% at the $39.75 vintage price); k_broker ~1.22 → ~1.20. No band flip
  predicted; any flip = halt-and-investigate.
- **The STNG lesson applies:** the net is small (−1.6% headline) ONLY because large opposing errors
  nearly cancel (+$201.5M of understated assets vs −$244.2M of steel-not-owned + NCI). The point of the
  reconciliation is figure integrity, not the net — the prior NAV was plausible-but-wrong.

## §5 — Queue consequences (predicted)

- **`NAV_FIGURE_ESTIMATE_QUEUE`: ten LEAVES** — every NAV-equation figure now cites a filing (the
  advances tilde-estimate, the WC roll-forward assumption, and the data-kit debt figure all resolve).
- **`OFF_CONVENTION_QUEUE`: TEN STAYS** — the 19-hull NB program remains on the documented
  delivered=contract convention, not §9.6 on-curve. The §9.6 wiring (3 VLCC + 5 LR1 + 1 LNG could go
  on-curve; the 10 DP2 shuttles have no observable resale market) is a separate owner methodology
  decision (STNG precedent — deferred, cross-sector).
- **`OPERATING_SCRUBBER_QUEUE`: TEN STAYS** — TEN publishes no fleet-wide scrubber aggregate in the
  20-F/6-K (data-kit per-vessel callouts only; NB-program "Scrubber Fitted" tags cover Delos T/Dion).
  Nothing to cross-foot against; documented, not cleared.

## §6 — OPEN FORKS — **ALL FOUR RULED 2026-07-15 (owner verbatim: "rule the four forks —
proceed as recommended. TEN-only baseline ratify.")** Each recommended option is the treatment
already wired by the reconciliation, so the ruling ratifies with ZERO number movement:
NCI = booked $45,954K via preferred_equity (BWLP convention) · Ulysses = carrying-inside-WC
(gain + ~$83M cash land at H1) · SLB steel = excluded (ASC 842 true-sale; keep-at-curve would
be a NEW convention) · WC = Mar-31 composite (component re-derive at H1, TRMD-fork-1 style).
H1 (~September) re-visits: Ulysses gain/cash · Arctic/Antarctic re-add owned · WC components.

1. **NCI basis.** Book $45,954 via `preferred_equity` (recommended — cited, BWLP convention) vs a
   NAV-basis derivation (49% × Mare-Success-level curve marks + sub cash − sub debt — NOT derivable:
   sub-level debt/cash undisclosed) vs a later BWLP-rider-(a)-style agreement guard. Booked figure ≈
   book equity; the 4 hulls are old (ages 17-19), so book-vs-curve divergence is bounded.
2. **Ulysses HFS value.** Carrying-inside-WC-composite (recommended — fully cited, conservative;
   the sale gain + $83M cash land at H1) vs curve mark $97.6M (REJECTED — violates HFS-at-contract)
   vs an estimated contract price (REJECTED — uncited figure, guard red by design).
3. **SLB steel exclusion.** Exclude (recommended — ASC 842 true-sale fact + house chartered-in
   convention) vs keep-at-curve under an "economic retention via repurchase options" thesis — that
   would be a NEW convention requiring its own owner ruling; nothing in the current book supports it.
4. **WC composite basis.** Composite Other-assets − Other-liabilities (recommended; the only citable
   Mar-31 construction) vs component build (available only at H1; re-derive then, TRMD-fork-1 style).

## §7 — HALT criteria

- Recomputed headline NAV/sh outside **$86.8 – $87.9**, or base outside **$94.0 – $95.2** → HALT,
  investigate the INPUT (the WC composite and the removed-marks set are the biggest movers).
- `/reconcile TEN` SANITY ≠ OK → HALT.
- Any guard red beyond the enumerated changes (manifest cross-foot updated in the same commit,
  figure-queue exit, drift-gate rows annotated in ten_log) → HALT.
- Any position band flip (BUY → anything) → HALT (also pre-flagged Stage-A-adjacent; TEN is in the
  sizing analysis's gate stack).

Baseline re-ratify after verification: **owner-gated, NOT executed by this reconciliation.**
