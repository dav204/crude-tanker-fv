# INSW Q2-2026 report-day refresh — PRE-REGISTRATION (written 2026-08-09 EVE, before the print)

**Reports 2026-08-10 BEFORE market open (Business Wire date-PR 7/24; call 9:00 ET).**
Frozen tonight so tomorrow's refresh is band-checked from the moment the 10-Q lands.
Sequence per the Stage-A D-4 ruling: **this refresh runs FIRST on the held Jun-7 curves
(pair flow), THEN the Stage-A wiring** — so this band is curve-invariant by construction
(pure sheet + aging effect; the curve re-anchor is a separate, later regen).

## Basis (current committed state)

NAV $53.88/sh (whole-co, post-marks baseline db53188) · EV −39.8% · position
"rich · cycle (not a short)" (§12 relabel) · sheet vintage 2026-Q1 (cash 376.8 + WC
229.3 − debt 602.1 − leases 8.0; 49.7M diluted; product NB commitments excluded from
the crude carve-out by convention; product_specific_debt 43.0).

## Predicted Q2 drivers (knowable tonight)

- **Cash/WC build POSITIVE and large**: Q2 was the record war quarter (peer realized:
  TNK Suez $109k / VLCC $123k; DHT $90.8k blended). INSW's spot-heavy crude sleeve at
  those levels ≈ +$120–200M net of interest, drydock, and the June-paid combined
  dividend → **+$2.4–4.0/sh**.
- **Uniform ~0.5y aging**: ≈ −1.3–1.7% of ~$2.7B GAV → **−$0.7–0.9/sh**.
- **Debt**: scheduled amortization ~$14M/q (NAV-neutral vs cash); possible ECA draw if
  an LR1 newbuild delivered in Q2 (roughly NAV-neutral at delivery under §9.6; moves
  the hull to operating + product-secured debt up).
- **Unknowable until the note**: vessel sales/purchases (subsequent-events note FIRST —
  the standing discipline), buybacks (INSW has a standing authorization), the
  supplemental-dividend declaration.

## Registered band

**Point NAV ≈ $56.30/sh; band [51.50, 61.00] (±8%).** Landing outside → HALT and
investigate the INPUT (a missed sale, a buyback, a basis change) before accepting.

## Halt/verification conditions (all standing rules, restated so the run can't skip them)

1. Subsequent-events note read FIRST; post-Q2 events do NOT enter the Q2 snapshot.
2. Pair lands together: `insw_2026-Q2.yaml` (provenance trio) + manifest `report_date`
   bump in ONE commit; both halves verified in the run's own fv_report breakdown.
3. **Forward invariance: the other 24 names delta exactly 0.0** at the pair regen.
4. Issuer-report S&P sweep (per filing): any disclosed per-vessel sale → marks
   candidate (NOTE: the pending-ID Pareto 8/03 gain-only VLCC sentence — if INSW's
   10-Q discloses a VLCC sale with a Q4 delivery and ~$74.4M gain, that identifies it;
   promote on the named terms, not the sentence).
5. **Q3 QTD bookings extracted → stage_a_basis §6 update BEFORE the Stage-A wiring**
   (the whole point of D-4): expect VLCC/Suez/Afra-LR1 bookings with booked-day shares;
   Aframax comes off single-print; LR1 possibly gains its first direct front print.
6. No flip predicted (a +4% NAV ≈ +2pp EV, far from any boundary). Any flip → eyeball;
   any flip toward BUY → halt-and-investigate (the Stage-A ADDENDUM rule is armed the
   same morning).
7. Watchlist consensus legs: price/pnav/fwd_pe stay the current vintage (the rebase is
   staged separately as a draft — do NOT mix vintages at this refresh).
