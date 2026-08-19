# FLNG Q2-2026 report-day refresh — PRE-REGISTRATION (written 2026-08-18, before the print)

**Reports 2026-08-19 ~07:00 CEST (~01:00 ET) — issuer invitation on flexlng.com, confirmed
2026-08-18; webcast 15:00 CEST.** PLAN carried FLNG at 8/28 with "early-release risk stands" —
the risk FIRED: FLNG is the earnings train's FIRST print, nine days early. Band frozen today
so tomorrow's refresh is band-checked from the moment the 6-K lands (INSW/BRUT pattern).

## Basis (current committed state)

NAV $28.45/sh · PW FV $30.67 · EV −0.4% · position HOLD (fairly valued) · tier
GOVERNED-WIDE · structural-class (LNGC = structural-unavailable §17 basis; no txn-anchored
fit — no marks candidacy expected from this print) · k_broker 0.87 · sheet vintage 2026-Q1
(cash 389.1 + WC 56.0 − debt 1,821.0; 54,092,376 diluted; no NB commitments) · 13×174k cbm
LNGC, ~91% of 2026 fleet days fixed, FY26 TCE guidance $73–78k/day · in
`NAV_FIGURE_ESTIMATE_QUEUE` (WC "other current liabilities assumed small ~$10M" is an
uncited assumption — see §Queue below).

## Predicted Q2 drivers (knowable tonight)

- **Cash ≈ FLAT, ± small.** The fleet is TC-fixed: Q2 revenue ≈ 13 hulls × ~91d × ~$75k
  ≈ $85–90M; less opex (~$18M), interest on $1.82B (~$27M), G&A → operating cash
  ≈ +$38–43M. The Q1 dividend paid in Q2 ≈ $0.75 × 54.09M = $40.6M. Net ≈ **−$3M to +$3M
  ≈ ±$0.05/sh** — the fixed-floor >100% payout is DESIGNED to bleed the cash pile slowly.
- **Scheduled amortization** ~$27M/q: NAV-neutral (cash↓ debt↓ together); only a
  refinancing/balloon event moves the net.
- **Uniform ~0.5y aging**: ≈ −1.3–1.7% of ~$2.9B GAV → **−$0.7–0.9/sh** (INSW convention).
- **Unknowable until the note**: vessel S&P (none signalled; no NBs on the books),
  new charters/extensions (backlog 54–81y — extensions are the upside surprise class),
  any newbuild ORDER (would be the first — §9.6 + R-2-style orderbook question, new).

## Registered band

**Point NAV ≈ $27.6/sh; band [25.40, 29.80] (±8%).** Landing outside → HALT and
investigate the INPUT (a missed S&P event, a refinancing, a basis change) before accepting.

## Halt/verification conditions (standing rules restated so the run can't skip them)

1. **Subsequent-events note FIRST**; post-Q2 events do NOT enter the Q2 snapshot.
2. Pair lands together: `flng_2026-Q2.yaml` (provenance trio) + manifest `report_date`
   bump in ONE commit; both halves verified in the run's own fv_report breakdown.
3. **Forward invariance: the other 24 names delta exactly 0.0** at the pair regen.
4. **Queue discipline:** the Q1 sheet's `working_capital_net` carries an assumed ~$10M
   other-current-liabilities plug (FLNG is in `NAV_FIGURE_ESTIMATE_QUEUE`). The Q2 6-K
   condensed BS is the chance to source the WC components; if disclosed, cite them and
   FLNG leaves the queue — if not, the conservative construction stays, documented.
5. **Dividend strip check:** expect the 20th consecutive $0.75 ordinary declaration.
   A cut/raise/special is THESIS news (the strip is half the tool's FLNG value) →
   owner flag, not a silent absorb. Policy YAML only moves on a declared change.
6. **TC disclosures → context, not Stage-B basis** (Stage B's ±10% class-bucket gate is
   tanker classes; LNGC has no fitted class). Capture fresh TCE guidance / backlog years
   in the log entry; `structural-unavailable` basis stands.
7. **No flip predicted** (EV −0.4% at the $30.80 tape, scenario band 20.36–39.36).
   The +$2.4 FV-vs-price gap means a band-mech flip HOLD↔BUY-side is possible on the
   print-day tape move alone — any flip → eyeball; **any flip toward BUY →
   halt-and-investigate** (ADDENDUM rule, standing).
8. Watchlist consensus legs: the 8/18 whole-book rebase may land the same day — the
   band above is NAV-side and price/vintage-invariant by construction; do not read a
   consensus-pair move as a band event. Sequence: refresh (pair flow) and rebase stay
   SEPARATE commits regardless of order.
9. `prices_daily.yaml` reverted before any regen (standing rule; it was reverted to the
   ratified 8/14 vintage this morning).
