# Per-ticker quick-refs — Tanker FV tool

Split out of CLAUDE.md (2026-06-22) to keep the operating rulebook short.
Full notes live in METHODOLOGY §6; consult this when working a specific name.

(One-liners; full notes live in METHODOLOGY §6. Prices/EVs quoted here
are the vintage at which the note was written — read the latest
`outputs/delta_report.md` for live position + FV; don't "fix" a
quick-ref price unless the note itself is being updated.)

- **DHT** — pure VLCC, single-class methodology validator. If DHT is weird,
  the methodology has a bug.
- **FRO** — LR2 classification choice (crude vs product) is open (§9.3).
  Trust the report counts, not the fleet page.
- **ECO** — all-spot, modern fleet; sale-leaseback in borrowings; TLS chain
  fails WebFetch.
- **NAT** — §12 archetype: high-payout pure-play; tool reads "rich" at peak
  (treat tool FV as NAV floor). APPROX consensus_pnav. **Reconciled 2026-06-30
  (de-voided):** NAV $2.79; fleet 16 operating + 2 held-for-sale booked at the
  $65M contracted price (`held_for_sale` field); 2 Suezmax NB (H2-2028) PARKED
  at $0 — NAT discloses the order but not the price (only a Pareto LOI), so §9.6
  on-curve is unauthorized → `NEWBUILD_PRICE_PENDING`, tier GOVERNED-WIDE·newbuild-
  indeterminate. Un-park onto the curve only when NAT files a contract price.
  See nat_log + decisions/nat_reconciliation_prereg_2026-06-30.md.
- **INSW** — mark-driven (k_broker 1.52 post txn-anchor flip, ~1.6 at live
  prices; was 1.37 pre-flip); hybrid crude+product carve-out. Pareto
  BUY→HOLD 2026-05-18 (valuation-driven, TP raised). LR1 = its only
  non-uniform class; the ruled contract-floor wiring books INSW **+$7.80M**
  at the post-Stage-A round (registered — don't read it as drift).
- **TNK** — Atlantic-skewed; Aframax transaction anchor; both mark-driven
  AND weight-driven.
- **FLNG** — tool above broker (k_broker 0.87); mature TC-heavy book.
- **CCEC** — BUY, **sign-stable across the §9.10 family since the 7/14 LNG
  re-tilt** (point +58.3 / family-min +38.0 — was "weight-driven"); tier
  GOVERNED-WIDE·structural-class; large NB orderbook (Group-B commitment-net);
  high scenario torque. APPROX consensus_pnav. Q2 window 7/29–8/06.
- **ASC** — first product validator; off-curve chemical-Handy residual.
  APPROX consensus_pnav.
- **STNG** — multi-class product; buyback channel invisible to strip.
  PROVISIONAL·off-curve: the 10-hull §9.6 NB wiring (~+$9.6/sh) is UN-GATED
  since thread (d) signed 7/15 — its own post-Stage-A prereg; GOVERNED-WIDE
  at best even wired (Handymax basis).
- **HAFN** — IFRS reporting + pool operator; largest product fleet.
- **TRMD** — first full 3-class product. Fully reconciled 2026-07-02 (all 3
  queues cleared, k 1.03 — the book's tightest tool↔broker spread). **P1c arc
  2026-07-15: MR cleared to resale-uniform → LR1 is TRMD's LAST basis blocker;
  LR1 contract-floor + `resale-corroborated` RULED (frozen) → VALIDATED-TIGHT
  (the 7th) scheduled at the post-Stage-A anchor round** (TRMD an exact-zero
  control in that wiring). ⚠ weight-sign-unstable (family −10.1/+8.4); its
  post-re-tilt BUY sits in the Stage-A expected-flips inventory.
- **TEN** — three-sleeve crude+product+LNG (`THREE_SLEEVE_TICKERS`); DP2
  shuttle off-curve at contracted book (§11.6); **first §15 case**
  (governance/value-trap haircut at 30%). **RECONCILED 2026-07-15
  (data-integrity, the SB-precedent restate):** headline NAV **$87.35**
  (was 88.76; bands hit), PW FV $56.46, BUY (EV +42% at $39.75) — every
  NAV figure now 6-K/20-F-CITED (advances $442.74M, WC $174.65M composite,
  debt $2,136.1M, +$45.95M Mare Success NCI via preferred_equity); 4
  not-owned hulls OUT (Ulysses HFS; Arctic/Antarctic/Sakura true-sale
  SLBs). Forks ruled, TEN-only baseline ratified; **left
  `NAV_FIGURE_ESTIMATE_QUEUE`** (stays OFF_CONVENTION + SCRUBBER queues).
  APPROX consensus_pnav (no Pareto; VIE anchor >1yr stale). H1 (~Sep):
  Ulysses gain + ~$83M cash; Arctic/Antarctic RE-ADD owned (pre-flagged —
  not churn); WC components; §15 TCM fee-load tripwire. Onboarded
  2026-06-06; see ten_log + the 2026-07-15 recon prereg.
- **SBLK** — first dry-bulk validator (Cape 31 / Pana 46 / Supra-Ultra 58
  post-Eagle-Bulk fleet, §11.7.1 class collapse); mark-driven (k_broker
  1.27 at v1, 1.27 post-transaction-anchor — the recalibration shifted
  the gap by 0.6pp, confirming the −21% spread is methodological, not a
  curve artefact). Cape was understated (+18%/+12% at 5/10yr), Supra-Ultra
  overstated (−10%/−13%), Pana roughly calibrated. Transaction sample:
  Pareto Shipping Daily archive + SBLK Q1 2026 6-K Star Stonington
  ($19.6M). Tool HOLD at live prices (band-edge; was TRIM/SHORT at the
  Jun-5 static — see sblk_log 2026-06-11), broker BUY. §15.7-screened
  OUT (self-managed, ~100% payout). Onboarded + transaction-anchored
  2026-06-09. GNK (k 1.04 on identical curves) isolates SBLK's gap as
  name-specific — likely the 46-vessel Pana book on the thinnest fit.
- **GNK** — second dry-bulk validator; VALIDATES the transaction-anchored
  dry-bulk curves (k_broker 1.04, gap −5.2% — within the v1 ±10% bar on
  the same marks where SBLK reads −21%). No Pana exposure (19 Cape /
  25 Supra-Ultra at Mar-31). US domestic issuer — 10-Q not 6-K; per-vessel
  employment table lives in the 10-Q MD&A. **LIVE DEAL (updated 2026-07-18):
  Diana lost the Jun-18 proxy fight (pill ratified, hostile path blocked) but
  did NOT withdraw — the $24.80 tender was EXTENDED to **2026-07-24** (Form 425
  7/13; 29.7% of non-Diana shares tendered, the branch-(c) muddle). Position is
  **HOLD** at the 7/18 state (TRIM/SHORT→HOLD band-mech on the 7/18 spot
  re-proxy; the earlier HOLD→TRIM/SHORT was price-led + FFA, tender-pinned) —
  NOT a BUY; the pre-2026-07 "hold BUY as event-contingent" guidance is
  RETIRED. Census check 7/24: on a lapse with no deal, drop the overlay and
  expect reversion toward the pre-bid 0.66-0.75× Pareto-NAV regime. See
  gnk_log 2026-07-13/18.**
  No §15 haircut (event risk ≠ realisation impairment). v1 lock outcome:
  1/2 (50%) FAIL-with-explanation — the miss is the documented SBLK case;
  no curve tuning per the back-solve rule. Onboarded 2026-06-09/10.
- **CMDB** — third dry-bulk validator, APPROX-anchored (zero Pareto/VIE
  coverage; consensus_pnav 0.62 is a P/BV proxy — spinoff book ≈ recent
  fair value). 29 owned old bulkers at Mar-31 (6 Cape / 7 Pana / 16
  Supra-Ultra); the ~20-vessel CBI chartered-in trading platform is
  P&L-ONLY, never in the manifest. Tool asset NAV $32.23 = book +15.8%.
  **Second §15 case — 30% governance haircut (owner decision 2026-06-10,
  TEN-equivalent: related-party fees $21.6M/yr, no payout, family
  control, 0.6× P/BV).** Post-haircut PW FV $19.82 vs price $17.25 →
  mild BUY (+14.9% EV); pre-haircut read +64%. No external anchor to
  triangulate the 30% (unlike TEN's VIE check) — revisit on any payout
  initiation. Consolidated EPS includes the trading platform → §9.11
  xref reads structurally hot. Watch Q2 for the Astros price (clean
  age-8 Ultramax print). **2026-07-18: HOLD→BUY band-mech (EV +6.8%) on the
  ratified 13-Jul spot re-proxy application; tier GOVERNED-WIDE·read-flips.**
  Onboarded 2026-06-10; Week 2 closed.

- **SB** — 4th dry-bulk validator (Safe Bulkers, NYSE:SB); the book's **lone
  VALIDATED-TIGHT BUY** (SBLK sits HOLD/band-edge since 7/13; re-flipped
  band-mech BUY 7/18 on the spot re-proxy — eyeball-free per D-M5). Cheap on both bases (~0.63× P/NAV);
  APPROX consensus_pnav (P/BV proxy, no Pareto). Hajioannou-controlled; §15
  DECLINED (market-rate mgmt fees, pari-passu dividends). Onboarded 2026-06-27.
  **AUDIT-CORRECTED 2026-07-01 (data-integrity, not a market move):** NAV
  $10.47→$10.12. Two errors vs the 6-K/20-F — (1) date-mixing (manifest was the
  2026-06-12 fleet on the 3/31 balance sheet): Katerina is a NEWBUILD at 3/31 (was
  double-counted), Michalis H (2012 Cape) is the ONE 3/31 HFS, Xenia + Pedhoulas
  Commander are operating (sales agreed May); (2) the CAPT blanket-scrubber bug —
  29 flagged vs 20 disclosed, corrected to the 20-F set (only Pedhoulas Rose among
  the Kamsarmax). **CLEARED to OPERATING_SCRUBBER_VERIFIED{SB:20}** — tightens the
  VALIDATED-TIGHT read. Fleet at 3/31 = 44 operating + 1 HFS + 8 NB. See
  sb_reconciliation_prereg_2026-07-01.md + the CLAUDE.md rules it added.

- **CAPT** — 17th name, first Oslo/NOK listing (watchlist carries USD;
  `yahoo_symbol: CAPT.OL` — bare CAPT on Yahoo is the wrong issuer).
  Marinakis ~75%; 30 firm vessels, 21 NB through mid-28 (heaviest §3.1/
  §9.6 delivered-market-less-commitment user); 13 options at cost
  EXCLUDED from NAV. Tightest first reconcile on record: −2.6% vs real
  Pareto pnav (k_broker 1.04) — validates NB convention + txn-anchored
  crude curves. BUY, EV +38.8% — deepest-discount crude name. §15
  deep-dived vs the full Euronext admission doc (archived
  `inputs/research_issuer/`) and NOT applied: single share class, fees
  ~0.4% of GAV/yr (vs CMDB ~4%), transfers at broker marks, pays ~50%
  from quarter one; BUT blank-check preferreds + written-consent
  control + no board committees + Crude Carriers fold-in precedent =
  SIX named tripwires in capt_log (option-funding dilution, preferred
  issuance, payout walk-back, sponsor merger proposal, fee escalation,
  Q1-27 NB-debt landing). Breakeven solve reads $0/day (net-cash
  + NB-heavy; cosmetic). Onboarded 2026-06-11 from archived Pareto
  initiation + Q1 review. **UPDATE 2026-06-22:** Q1 issuer report confirmed
  the build (broker-sourced caveat CLEARED); the §9.6 time-to-delivery
  discount then rolled out across the NB cohorts (now on exact Q1-release
  delivery dates) → NAV $15.03, gap **−17.5%, k_broker 1.17** — the tool is
  now more conservative on NB timing than Pareto (the −2.6%/k-1.04 above was
  the pre-§9.6 onboarding read). BUY held (EV +22.4%). **2026-07-18: band now HOLD (EV −1.9% at the 7/17 tape; the war-tilt/price path since 7/12 — see the 7/13 doha_check pre-approval); no longer the deepest-discount crude name.** See capt_log.

- **BRUT** — 20th name, the CAPT natural-experiment comp. Pure-play VLCC
  newbuild vehicle (Trøim-sponsored: Drew Holdings 48.15% at the Nov-2024
  admission, since diluted by four issuances, current % unresolved; managers
  2020 Bulkers Management + Himalaya Shipping, Magni support at zero fee —
  the prior "Koch 26% / dispersed" block was FABRICATED, corrected 2026-07-01),
  Oslo Growth/NOK (`yahoo_symbol: BRUT.OL`). 12 firm VLCC NB
  (8 NTS 300k + 4 CIMC 319k), **0 on the water** — first delivers Jul-2026,
  last Q3-2029. The name that **resolved §9.6**: raw delivered-less-commitment
  NAV was +116% vs Pareto (SANITY=FAIL — the $175M VLCC mark on a 100%-NB book,
  "max torque"); the time-to-delivery PV discount lands it at +30.6% (OK), NAV
  $9.40, BUY (EV +97%) — **since relabeled: NAV $8.80 (cash floor 2026-07-01),
  position prints "unreliable read (not actionable)" (`POSITION_UNRELIABLE`);
  binding flags cash-pending-H1 + going-concern (§15) per the 2026-07-15
  thread-(d) close.** Real Pareto coverage (NOT APPROX; 0.75× NAV). Pre-
  operational max-torque + ~75% LTV (equity-raise/dilution risk); §15:
  going-concern is the headline risk (haircut judgment pending the prospectus). Half-yearly reporter —
  H1-2026 (Aug-13) confirms the Pareto-estimate financials. Onboarded 2026-06-22.

- **MPCC** — 1st containerships validator (Oslo/NOK; `yahoo_symbol:
  MPCC.OL`). 51 on-water (21 feeder / 30 intermediate, ~129k TEU) + 15
  OWNED NB rows at the CAPT §3.1 net-of-commitment convention ($633.7M
  commitments; Uthalden JV pair excluded both sides). Coverage 99/69/41%
  of 2026/27/28 days fixed → coverage_schedule; ~50%-of-adj-profit
  dividend (policy_type variable). NAV $2.27, TRIM EV −29.6% at NOK
  26.42 (since relabeled "unreliable read" — `POSITION_UNRELIABLE`, method
  mismatch) (= USD $2.78 carried in the watchlist, CAPT NOK machinery).
  APPROX anchor = company-implied NAV NOK ~25.5 (Jul-25, stale);
  Pareto covers on EV/EBITDA only (HOLD TP NOK 25). §15.7 DECLINED
  (fees 0.6%/yr GAV, payout channel wide open). KNOWN SOFT: cohort age
  ESTIMATES (deck has no built years) + NB delivery quarters — refine at
  Q2 (reports 2026-08-26). §11.8.5(b) marks-tilt ledger row ACTIVE; its
  3 disclosed sale prints show tool old-age marks 0-33% BELOW realized
  (deliberate, conservative). Onboarded 2026-06-12.
- **GSL** — 2nd containerships validator, the charter-book stress test.
  71 vessels (0 feeder / 30 intermediate / 41 large; 18.2-yr
  TEU-weighted), full per-vessel charter table from the 6-K PR;
  coverage_schedule computed at mid-redelivery cross-foots disclosed
  100%/86%. Coverage dampening visible: scenario FV spread only ±10%.
  NAV $38.59 (prefs $109M subtracted), TRIM EV −18.5% at $38.99 (2026-07-18:
  band now HOLD, EV −1.7% — price-led); tool
  fleet 22% BELOW cost book (§11.8.5(b) row). APPROX = P/B proxy, WEAK.
  §15.7 dimension-6 charter-affiliation pass DECLINED: CMA CGM equity
  ZERO since 2022-08-05, 13/71 vessels (#2 behind Maersk 24) — tripwires
  incl. the Jun-26 $917M NB order's undisclosed charterers (Q2 check).
  NB order is POST-snapshot — Q2 item. Onboarded 2026-06-12.

- **CMBT** — CMB.TECH conglomerate, first multi-sleeve §11.9 case (crude +
  dry-bulk + chemical/Windcat legs); GOVERNED-WIDE·structural-class,
  TRIM/SHORT. Governance-repo history: held ~7%, EXITED 2026-07-06
  (reallocation, falsifier not fired). Open items in cmbt_log (FSO
  owned-vs-JV, §9.4 yard discount, NMax NB level). Onboarded 2026-06-27.
- **2343** — Pacific Basin, 25th name, 1st HKEX, 1st Handy-Bulk carrier
  (§11.7.11; 40.7% Handy). GOVERNED-WIDE·pending-anchor via
  `UNANCHORED_VALUE_CLASS_CAP` (empties at the `handy_bulk_txn_refit`
  §9.9 fit — the cleanest TIGHT path after TRMD). HOLD; NAV $0.39;
  issuer-composite APPROX anchor (AR publishes per-class broker values —
  the strongest APPROX basis). Chartered-in trading book P&L-ONLY (the
  CMDB/CBI convention — now cited as precedent by the TEN recon). Interim
  ~Aug (window 7/27–8/14, unvetted): F-1 orderbook re-test + post-April
  NB conversion. Onboarded 2026-07-14.
- **LPG** — Dorian, VLGC validator #1 (WO3 Phase 4). PROVISIONAL·
  v1-lock-miss (sector cap `SECTOR_V1_UNLOCKED`; re-run 11/13) —
  handoff NO regardless of per-name state. Rich · cycle position
  relabel (§12 late-cycle). mark_wide VLGC@five_year (extrapolated age-5
  node). US domestic filer (10-K/8-K). $1.00 irregular dividend declared
  7/16 (record 7/27) — the §12 payout archetype; FQ1-FY27 window 7/30–8/06.
- **BWLP** — BW LPG, VLGC validator #2. PROVISIONAL·v1-lock-miss (same
  sector cap). NCI-via-preferred_equity $199.0M RATIFIED 2026-07-13 with
  riders (BW India listed sub; guard `test_bwlp_nci.py`; India strip-leak
  documented LIMITATIONS §3). Product Services trading arm pre-announced
  Q2 net −$31M (7/16 6-K; ≈−1.3% NAV, flows at the Q2 refresh — results
  date CONFIRMED **2026-08-28**). Onboarded 2026-07-10.
