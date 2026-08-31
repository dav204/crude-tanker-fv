# CAPT H1-2026 report-day refresh — PRE-REGISTRATION (written 2026-08-31 EVE, before the print)

**Reports 2026-09-01 BEFORE the Euronext Growth Oslo open** (issuer scheduling release 8/26,
newsweb-staged; conference call 14:30 CET / 8:30 ET same day). Half-yearly reporter: the H1
print moves the sheet 31-Mar → **30-Jun**, one quarter. Frozen tonight per the standing
INSW/FLNG/TRMD pattern — the earnings train's last name.

## Basis (current committed state)

Price $16.46 (8/31 run) · PW FV $16.02 · EV −2.7% · band-state HOLD (BUY→HOLD at the 8/28
rebase, price-led) · **POSITION READ VOIDED — Stage-A void, POSITION_UNRELIABLE, the ONE
BUY-ward void at tape; NO VOID RETIRES AT THIS REFRESH (R4 only, scope ruled 8/31: the WO
re-reads live objects)** · tier GOVERNED-WIDE (§17 read-blocked, newbuild-heavy — a
construction fact) · NAV $15.48/sh · k_broker 1.26 (+41.5pp — the book's widest spread:
Pareto adds ~$204M option value + $14-18M/hull DF premium we deliberately exclude) · sheet
2026-Q1 (31-Mar): cash 405.0 + WC 13.0 − debt 217.0 − commitments 1,880.0; 133.7M diluted ·
fleet: 12 VLCC (1 on water — Aristotelis II; 7 deliver 2027, 4 in 2028) + 10 Suezmax +
4 Aframax (operating, avg 7.8y) + 4 LR2 (avg 0.5y); 13 options EXCLUDED from NAV.

## Predicted H1 drivers (knowable tonight)

- **The June VLCC acquisition is IN-SNAPSHOT** (June < 6/30; flagged unmodelled by the 8/16
  + 8/24 digests). AMBIGUITY REGISTERED: whether it is a NEW hull beyond the 12-committed
  program or an early/secondhand addition — the filing settles it; every figure (price,
  financing, delivery) must be filing-cited on entry. Expected ≈ NAV-neutral if bought at
  market (§9.6/§3.1), but it moves fleet counts, commitments, and debt.
- **Installments are NAV-NEUTRAL by construction** (cash↓ commitment↓ together); facility
  draws likewise (cash↑ debt↑). Expect cash well below 405 and commitments well below
  1,880 — the WALK must tie, not the levels.
- **PV unwind on the NB book**: one quarter closer to delivery ≈ +2%-class on the
  PV-discounted NB marks ≈ **+$0.30-0.45/sh**.
- **Operating cash**: small fleet (1 VLCC + 4 Aframax + young LR2s/Suez as delivered)
  earning war rates ≈ **+$0.15-0.30/sh** net.
- **Aging** on operating hulls only ≈ **−$0.10/sh** (the age-0 NB book doesn't age).
- No dividend assumed (pre-full-operation profile); a maiden declaration = news, flagged
  not absorbed.

## Registered band

**Point NAV ≈ $16.00/sh; band [14.70, 17.30] (±8%).** Landing outside → HALT and
investigate the INPUT (the June acquisition's booking, a missed draw/delivery, a basis
change) before accepting.

## Halt/verification conditions

1. **Subsequent-events note FIRST** — EXPECTED there and OUT of the 6/30 snapshot: the
   **8/06 LR2 delivery + $50.0M senior secured facility** and the **8/13 Suezmax delivery
   + $67.5M sale-and-leaseback**. A 6/30 sheet carrying either is a halt (mis-dated
   booking or our misread).
2. **THE ECO SLB TRAP, registered on the first only**: the $67.5M SLB books into
   BORROWINGS as a financial liability — never as debt AND a separate operating-lease
   line (the ECO precedent). The $50M senior-secured is ordinary mortgage debt — do not
   read it as an SLB. Neither enters THIS snapshot; the trap arms for the note-reading
   now and the FY sheet later.
3. Pair lands together: `capt_2026-Q2.yaml` (provenance trio, machine-readable) +
   manifest `report_date` bump + ages +0.5 in ONE commit; commit FIRST, regen SECOND.
4. **Forward invariance: the other 24 names delta exactly 0.0.**
5. **Void discipline: POSITION_UNRELIABLE holds through this refresh regardless of what
   the band prints.** A BUY-ward band print is recorded and eyeballed but is NOT a read
   and NOT actionable — no void retires outside R4. (The ADDENDUM halt rule for flips
   toward BUY applies to the OTHER 24 names at the invariance check.)
6. **Stage-B basis capture**: CAPT fixes newbuilds forward (the BRUT pattern) — any
   VLCC/Suezmax/LR2 term-rate disclosures in the H1 report are Stage-B class-bucket
   evidence; extract BEFORE Stage B's bucket re-check runs.
7. Watchlist pair stays at the 8/28 vintage (kr 150.4 / 0.72 / 25.5) — no mixing at the
   refresh; the P/E 25.5 sits in the verified collapsing-estimate class (8/09 + 8/18
   render checks), not an artifact.
8. `prices_daily.yaml` reverted before the regen if the evening cron has dirtied it
   (standing rule).
