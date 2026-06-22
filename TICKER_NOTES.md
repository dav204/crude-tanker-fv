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
- **NAT** — §12 archetype: high-payout pure-play; tool reads as "rich" at
  peak. Treat tool FV as NAV floor. APPROX consensus_pnav.
- **INSW** — mark-driven (k_broker 1.52 post txn-anchor flip, ~1.6 at live
  prices; was 1.37 pre-flip); hybrid crude+product carve-out. Pareto
  BUY→HOLD 2026-05-18 (valuation-driven, TP raised).
- **TNK** — Atlantic-skewed; Aframax transaction anchor; both mark-driven
  AND weight-driven.
- **FLNG** — tool above broker (k_broker 0.87); mature TC-heavy book.
- **CCEC** — weight-driven BUY; large NB orderbook; high scenario torque.
  APPROX consensus_pnav.
- **ASC** — first product validator; off-curve chemical-Handy residual.
  APPROX consensus_pnav.
- **STNG** — multi-class product; buyback channel invisible to strip.
- **HAFN** — IFRS reporting + pool operator; largest product fleet.
- **TRMD** — first full 3-class product.
- **TEN** — three-sleeve crude+product+LNG (`THREE_SLEEVE_TICKERS`); DP2
  shuttle off-curve at contracted book (§11.6); **first §15 case**
  (governance/value-trap haircut at 30%). Txn-anchored NAV $88.13 (asset
  NAV $95.95 un-anchored), post-haircut PW FV $62.56 vs price $37.99 →
  BUY (EV +64.7%). APPROX consensus_pnav (no Pareto coverage; VIE-stale
  anchor). Onboarded 2026-06-06; June-5 data-kit reconcile 2026-06-11
  added two Suezmaxes the build omitted (Dr Irene Tsakos, Silia T) —
  NAV +9.1%, see ten_log. H1 reporter: Q2 events (Ulysses sale, charter
  rolls) land at the SEPTEMBER refresh.
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
  employment table lives in the 10-Q MD&A. **LIVE DEAL (updated 2026-06-21):
  Diana LOST the Jun-18 proxy fight — all 6 Genco nominees re-elected, pill
  ratified, hostile path now structurally blocked. Diana did NOT withdraw:
  $24.80 all-cash tender still live to Jun-26 + non-binding $27.34 cash+stock
  under board review. Price de-rating below the cash leg (~$23.66). Framing
  migrating deal-arb → NAV-discount but still event-contingent until Jun-26;
  hold BUY as event-contingent, not a clean NAV-discount signal. On a tender
  lapse with no deal, drop the overlay and expect reversion toward the pre-bid
  0.66-0.75× Pareto-NAV regime. See gnk_log 2026-06-21.**
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
  age-8 Ultramax print). Onboarded 2026-06-10; Week 2 closed.

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
  the pre-§9.6 onboarding read). BUY held (EV +22.4%). See capt_log.

- **BRUT** — 20th name, the CAPT natural-experiment comp. Pure-play VLCC
  newbuild vehicle (Trøim/Magni; Koch 26% / Trøim 20% / float 54%; NO >50%
  controller), Oslo Growth/NOK (`yahoo_symbol: BRUT.OL`). 12 firm VLCC NB
  (8 NTS 300k + 4 CIMC 319k), **0 on the water** — first delivers Jul-2026,
  last Q3-2029. The name that **resolved §9.6**: raw delivered-less-commitment
  NAV was +116% vs Pareto (SANITY=FAIL — the $175M VLCC mark on a 100%-NB book,
  "max torque"); the time-to-delivery PV discount lands it at +30.6% (OK), NAV
  $9.40, BUY (EV +97%). Real Pareto coverage (NOT APPROX; 0.75× NAV). Pre-
  operational max-torque + ~75% LTV (equity-raise/dilution risk); §15 partial
  (provisional 0%, fee/control pending the prospectus). Half-yearly reporter —
  H1-2026 (Aug-13) confirms the Pareto-estimate financials. Onboarded 2026-06-22.

- **MPCC** — 1st containerships validator (Oslo/NOK; `yahoo_symbol:
  MPCC.OL`). 51 on-water (21 feeder / 30 intermediate, ~129k TEU) + 15
  OWNED NB rows at the CAPT §3.1 net-of-commitment convention ($633.7M
  commitments; Uthalden JV pair excluded both sides). Coverage 99/69/41%
  of 2026/27/28 days fixed → coverage_schedule; ~50%-of-adj-profit
  dividend (policy_type variable). NAV $2.27, TRIM EV −29.6% at NOK
  26.42 (= USD $2.78 carried in the watchlist, CAPT NOK machinery).
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
  NAV $38.59 (prefs $109M subtracted), TRIM EV −18.5% at $38.99; tool
  fleet 22% BELOW cost book (§11.8.5(b) row). APPROX = P/B proxy, WEAK.
  §15.7 dimension-6 charter-affiliation pass DECLINED: CMA CGM equity
  ZERO since 2022-08-05, 13/71 vessels (#2 behind Maersk 24) — tripwires
  incl. the Jun-26 $917M NB order's undisclosed charterers (Q2 check).
  NB order is POST-snapshot — Q2 item. Onboarded 2026-06-12.
