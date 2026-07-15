# P1c — MR secondhand line RESUMED: age-0 → xclusiv Resale, basis → resale-uniform

**Frozen ahead of the wiring (commit precedes recompute).** Thread-1A registered the
MR sourcing path as "allied or advanced weekly … verifies the $54M and clears the
`unverified-no-current-xclusiv-line` flag." What actually landed is better: **xclusiv
itself resumed the MR2 secondhand table** — the exception's cause (xclusiv dropped MR
secondhand after 2023Q4) no longer exists.

## 0. The finding (dated)

xclusiv weekly **2026-07-13** (in-repo `shipping_harvester/data/pdfs/xclusiv/
2026W29_f76ec738.pdf`, parsed `data/marks/xclusiv/2026Q3.json`) prints a full MR2
secondhand line: **Resale 55.0 / 5yr 50.0 / 10yr 40.0 / 15yr 28.0**. Same footnote
basis as the locked extract ("Resale prices refer to prompt delivery ex yard") —
label-verified against the 5-Year row (no row-slip).

Level check vs the wired mark: $54M vs $55.0M = **−1.8%, inside ±2%** — the repo's
$54M was sound (as the 2023 allied/advanced corroboration suggested). But
`resale-uniform` is defined as *age-0 == the dated xclusiv Resale line*
(`test_curve_age0_equals_xclusiv_resale`), so clearing the flag wires **55.0**, not 54.

**Cross-broker divergence (recorded, not blended):** advanced W28 (2026-07-10) prints
MR 52k Resale **60** — +9% over xclusiv, while the two houses' 5yr agree (50.5 vs
50.0); the whole spread is in the Resale/5yr uplift (1.19× vs 1.10×). xclusiv is the
locked source of record (Amendment B); the advanced print is a footnote divergence,
same treatment as VIE/MB.

## 1. The wiring (this step, and only this)

- `inputs/market_data/xclusiv_age_curve.yaml`: add `MR: 55.0` to `resale:` (+ 5yr/10yr
  documentation rows), **per-row dated 2026-07-13** — a deliberate mixed-vintage row in
  the 2026-06-22 extract, annotated in place (precedent: the file already carries per-row
  dated annotations; full-file vintage coherence is restored by the §5 rider).
- `inputs/market_data/vessel_value_curves.yaml`: MR `newbuild` 54.0M → **55.0M**.
- `inputs/market_data/newbuild_contract_prices.yaml`: `prompt_resale` MR 54.0M → **55.0M**
  (single-source invariant `test_curve_age0_equals_prompt_resale`).
- `inputs/market_data/basis_status.yaml`: MR `unverified-no-current-xclusiv-line` →
  **`resale-uniform`**.
- `tests/test_thread1_resale_anchor.py`: `XCLUSIV_WIRED` += MR; `AGE0_BASIS["MR"]` →
  `xclusiv-resale`; the `test_basis_status_covers_curve_classes` MR special-case assert
  flips to resale-uniform (the "never silently resale-uniform" guard is satisfied by THIS
  dated record — the flip is loud, not silent).
- NOT touched: `newbuild_contract` (parity layer — its MR 52.0 is a 2026-06-22 xclusiv
  CONTRACT mark; the 2026-07-13 issue prints MR2 NB 53.0 — rides §5); the xclusiv extract's
  other rows (06-22 vintage holds); mid-age production anchors (MR is a §9.9 fitted class —
  transaction prints govern, this file's 5yr/10yr rows are documentation).

## 2. Predicted outcome (committed AHEAD; honor a miss)

Age-0 +$1.0M moves only on-curve MR tonnage with age < 5 (sensitivity 1−age/5).
Book-wide scan (all 25 manifests, 2026-07-15):

- **TEN is the ONLY mover: +$1.94M NAV** — 2 young MRs (ages 0.1 / 0.2; factors
  0.98 + 0.96). On 30,127,603 shares = **+$0.064/sh, NAV 88.70 → ~88.77 (+0.07%)**.
  Far under the 2pp drift bar; EV +44.9% BUY — no band-flip risk.
- **Every other name 0.0 exactly:** TRMD's 2 resale MRs are age-11 (10yr+ segment —
  age-0-insensitive; ytd 0.12 only PV-discounts); STNG's NB MRs are OFF-curve (parked,
  §9.6 deferral); HAFN's 8 HHI MR NBs are post-Q1 subsequent events (excluded);
  all other MR tonnage ≥ age 5 (transaction-anchored mid-age).
- **Zero nav_basis composite changes / zero tier moves:** every MR holder keeps ≥1
  other non-uniform class — TRMD (LR1), STNG (Handymax), ASC (Handysize), HAFN
  (Handysize+LR1), INSW (LR1), TEN (LNGC structural + LR1 + Handysize). Only
  `nav_basis_detail` shrinks (the MR item leaves 6 names' flag lists).
- Suite green (incl. the two deliberate test edits); drift gate 0 UNEXPLAINED
  (TEN's +0.07% is sub-threshold); **no re-ratify needed**.

**Halt conditions:** any name other than TEN moves; TEN moves outside +$1.8–2.1M;
any band flip; any tier/nav_basis composite change. Halt → investigate the input,
never widen a band.

## 3. What this buys (P1c ledger)

MR was one of the two classes keeping **TRMD** off resale-uniform. After this step
**LR1 is TRMD's last basis blocker** (and INSW's only one) — see
`decisions/lr1_level_evidence_2026-07-15.md` for the dated LR1 evidence + the owner
fork. TRMD's path to VALIDATED-TIGHT is now exactly one class wide.

## 4. Sequencing

NAV-effect +0.07% on one name, no flips, no tier moves — this is routine dated-source
maintenance, not an FV-moving event in the Stage-A sense (2026-07-15 ruling). Executed
now; the §5 rider queues.

## 5. Deferred rider — full extract refresh to the 2026-07-13 issue (post-Stage-A)

The 2026-07-13 issue also moves: Suezmax Resale 114.3→116.0 (+1.49%), Supra-Ultra
43.0→43.5 (+1.16%); NB rows Aframax 75→78, Suezmax 88→90 (contract table), MR2 52→53,
Panamax(LR1) NB 61.0 (new line — feeds the LR1 packet). Quantified movers (all
sub-2pp): CAPT ~+$16–17M (10 young Suezmax), ECO ~+$6–7M PV'd (4), CMBT ~+$4M (7 young,
partial factors), TEN ~+$4.6M (3 young Suezmax), 2343 ~+$1.5M PV'd (4 Ultra NBs),
GNK ~+$0.2M. Deferred to the next anchor-refresh cycle per the one-FV-moving-event
sequencing; restores single-issue vintage coherence for the whole extract.

## OUTCOME (fill at the gate)

- [ ] pipeline + suite + drift gate results vs §2
