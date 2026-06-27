# CMBT (CMB.TECH NV) — multi-sleeve onboarding: methodology decision memo

> **CORRECTION (2026-06-26, same day):** this memo's "no clean broker NAV → APPROX,
> consensus_pnav 0.90, SANITY n/a" framing was **wrong** and is superseded. Pareto
> DOES publish a monthly CMB.TECH P/NAV + NAV/sh in the Shipping Daily (11-Jun-2026:
> price $14.90, **P/NAV 0.74x**, NAV ~$20/sh, fwd P/E 9.7x). CMBT is a **Pareto-anchored**
> name: broker NAV **$20.14**, tool NAV $15.26, **gap −24.2%, SANITY OK**, k_broker 1.14
> (inside the validated band). At the live close, scenario FV → **EV +11%, BUY**. The
> architecture / §15 / off-curve / engine sections below stand; only the
> reconcile-anchor framing (§6, §7) is corrected. See `decisions/cmbt_log.md`
> (2026-06-27 entry) + `outputs/pareto_mentions_cmbt.md`.

**Date:** 2026-06-26. **Status:** DECISION MEMO — awaiting owner sign-off before any
engine code is written (per the "methodology-decision-doc-first" rule for new
architectures, WORKFLOWS.md §"Onboarding a new sector"). The full §11.x prose for
METHODOLOGY.md is drafted only after approval.

**Companion artefacts** (raw, sourced, in `outputs/cmbt_onboarding/`):
`01_crude_fleet.md`, `02_drybulk_fleet.md`, `03_container_chem_offshore.md`,
`04_financials_nb_div.md`, `05_governance_s15.md`, `06_engine_design.md`.
All numbers below trace to SEC EDGAR primary sources (CIK 1604481): the **Q1-2026
6-K Ex-99.1** (filed 2026-05-19, period end 2026-03-31) and the **FY2025 20-F**
(filed 2026-04-21; per-vessel fleet table as of 2026-04-01, capex note as of
2025-12-31).

---

## 0. The decision in one paragraph

CMB.TECH (NYSE/Brussels: **CMBT**, ex-Euronav) is no longer a crude pure-play. After
the **Golden Ocean merger closed 20-Aug-2025** (0.95 exchange ratio, +95.95m shares),
it is a five-segment shipping conglomerate where **dry bulk is ~60% of vessel value**.
We onboard it as the watchlist's **first crude + dry_bulk + container multi-sleeve
hybrid** — all three sectors already have value curves and scenario sets in the engine —
with **chemical, offshore (Windcat), the 2 FSOs, the held-for-sale vessels, and the
multi-segment newbuild book held OFF-CURVE** at book / contracted / delivered-less-
commitment value (the established §11.5 / §11.6 / §3.1 precedents). It needs a one-time
**generalization of the carve-out + aggregator** (today hardcoded to crude/product/lng),
a §15 governance screen (**outcome: decline the haircut, carry with tripwires**), and it
ships **APPROX-anchored** (no clean broker NAV — joins the NAT/ASC/CCEC cohort).

---

## 1. Resolved facts (the inputs the marks depend on)

| Item | Value | Source / confidence |
|---|---|---|
| Shares outstanding (ex-treasury) — **NAV denominator** | **290,169,769** | 6-K, CONFIRMED |
| Shares issued incl. treasury | 315,977,647 | 6-K |
| Reporting currency | USD | — |
| Cash & equivalents | $194.6m (+ $8.3m ST investments) | 6-K, CONFIRMED |
| **Total interest-bearing debt (incl. leases)** | **$5,244.4m** | 6-K, CONFIRMED — *incl. the $200.3m current "Other notes" (unsecured 2026 retail/sustainability notes) the first fact-pack missed* |
| Net debt (cash only) | ~$5,049.8m | computed (no printed subtotal) |
| Total equity (book) | $2,941.3m → **$10.14/sh book** | 6-K |
| Goodwill (EXCLUDE from NAV) | $190.7m | 6-K — Golden Ocean acquisition goodwill, not a vessel asset |
| Vessels (carrying) / AUC | $6,441.5m / $759.8m | 6-K |
| Non-current assets held-for-sale | $137.5m | 6-K — Ilma, Ingrid (VLCC) + Sienna (Suezmax), agreed sale prices, deliver Q2-26 |
| `working_capital_net` (operating) | **+$169.4m** | 6-K (inventory + receivables + tax assets − payables − tax liab) |
| Dividend | $0.64/sh Q1 ($0.20 interim + $0.44 share-premium) ≈ 50% of net profit; **discretionary** policy (50–60% historical guide) | 6-K + transcript |
| Q1-26 net profit / EBITDA / backlog | $368.8m / $558.3m / **$3.26bn contract backlog** | 6-K |
| Price (snapshot, NOT the model input) | ~$16 NYSE | aggregators — live close comes from `prices_daily.yaml` |
| Broker NAV / P/NAV | **none clean** (Fearnley Buy, ~$12.43 PT Dec-25; "discount to NAV" qualitative) | → APPROX consensus_pnav |

**VLCC count discrepancy RESOLVED: 4 on the water** (Donoussa 2016, Atrebates 2025,
Eburones 2026, Menapii 2026), +2 NB (2027). The "8" was the *disposed* fleet — Euronav
sold exactly 8 VLCCs in Q1/Q2-26 (six delivered, Ilma+Ingrid pending). Confirmed verbatim
in the 6-K fleet narrative and reconciled against the 20-F's 8-row table.

### Fleet composition at 2026-03-31 (on the water)

| Segment | On water | Model treatment | Engine class |
|---|---|---|---|
| **Crude — VLCC** | 4 (+2 NB) | on-curve, crude sleeve | `vlcc` |
| **Crude — Suezmax** | 18 (+2 Apr-delivered) | on-curve, crude sleeve | `suezmax` |
| Crude — FSO | 2 (2002) | **off-curve** (contracted-book) | — |
| **Dry bulk — Newcastlemax** | 38 (+8 NB) | on-curve, dry_bulk sleeve | `cape` |
| **Dry bulk — Capesize** | 37 | on-curve, dry_bulk sleeve | `cape` |
| **Dry bulk — Kamsarmax/Panamax** | 30 (26+4) | on-curve, dry_bulk sleeve | `pana` |
| **Container — 6,000 TEU (Delphis)** | 4 (+1 NB) | on-curve, container sleeve | `ctr_large` |
| Chemical — 25k stainless (Bochem) | 8 (+8 NB) | **off-curve** (working_capital_net, book) | — |
| Offshore — CSOV (Windcat) | 3 (+4 NB) | **off-curve** (book) | — |
| Offshore — CTV (Windcat) | **44 owned** + 15 JV (50%) (+NB) | **off-curve** (book vessels + equity-method JV stake) | — |

On-curve = **97 vessels** (4+18+75+4 wait: 4 VLCC + 18 Suez + 75 Cape-class + 30 Pana wait
— dry bulk on-curve is 105, container 4, crude 22). On-curve vessel count = 22 crude +
105 dry bulk + 4 container = **131 vessels**; off-curve = 2 FSO + 8 chemical + 47 owned
Windcat (+15 JV at 50%) + 3 HFS. Full per-vessel tables with built years/yards are in
`01_…`/`02_…`/`03_…`.

---

## 2. Sleeve architecture (the locked design)

CMBT = **3 on-curve sleeves** aggregated to a whole-company FV vs the tape price, exactly
the TEN §11.6 pattern but for a *different, non-hardcoded* sector combination:

```
whole-co FV  =  crude sleeve (sectors.crude, VLCC/Suezmax)
             +  dry_bulk sleeve (sectors.dry_bulk, Cape/Pana)
             +  container sleeve (sectors.containerships, ctr_large)
             +  off-curve corporate stack (FSO + chem + Windcat + HFS + NB book)
```

Carve-out splits the single manifest by vessel class → sleeve; balance-sheet items
pro-rate by sleeve **vessel-value share**; per-sleeve FVs sum (per-share, same shares
denominator) and compare to the **whole-company tape price**. Rough value shares
(order-of-magnitude marks): **crude ~25% / dry_bulk ~60% / container ~5%**, off-curve ~10%.

**Sleeve cycle positions differ and each carries its own** (crude late-cycle, dry bulk
its own Bulk-Set-A cycle, container its own) — the headline aggregates them, as TEN does.

---

## 3. Off-curve conventions (no new sector; reuse §11.5 / §11.6 / §3.1)

| Off-curve asset | Convention | Carried at | Precedent |
|---|---|---|---|
| **2 FSO** (2002, service contracts) | NPV of contracted cash flows | `shuttle_contracted_book` | §11.6 (TEN DP2 shuttle) |
| **8 chemical** (25k stainless) | segment book less liquidity haircut | `working_capital_net` | §11.5 (ASC chem-Handy residual) |
| **Windcat owned** (3 CSOV + 44 CTV) | segment book (vessels) | `working_capital_net` | offshore is §11 out-of-scope → off-curve at book |
| **Windcat JV** (15 CTV @ 50%) | equity-method carrying value | `working_capital_net` | the hulls are off the consolidated B/S; only the **$3.46m** equity stake represents them |
| **3 HFS** (Ilma, Ingrid, Sienna) | agreed sale prices | `working_capital_net` | DHT-Bauhinia / STNG-HFS precedent |
| **Newbuild book** (multi-segment, $759.8m AUC) | delivered-market **less** remaining commitment, PV-discounted `1.11^(−yrs)` | `newbuild_capex_commitments` + `newbuild_advances_paid` | §3.1 / §9.6 |
| **Goodwill** ($190.7m) | **excluded** | — | not a vessel asset |

**Segment book values available** (FY2025 20-F segment B/S, auditable): Delphis vessels
$210.5m; Bochem vessels $276.4m (+$62.1m AUC); Windcat vessels $196.5m (+$160.1m AUC,
+$3.46m JV). These give a defensible off-curve floor.

**Newbuild book — the one segment that needs a judgment.** $759.8m advances paid sit in
AUC; ~$1.2bn remaining commitment (end-April, $184m unfunded). Newbuilds whose class has
a curve **and** deliver inside a sleeve's strip horizon enter that sleeve's fleet schedule;
those delivering past the horizon (most of the book) carry only the balance-sheet lines.
**Ammonia/hydrogen-spec newbuilds with no value curve → contracted/advances value, no
hot-market markup** (the conservative §11.6 NB-shuttle analog). The "ammonia-ready"
premium is NOT marked up — consistent with declining to speculate on the decarbonization bet.

---

## 4. §15 governance — DECLINE the haircut, carry with tripwires

Full screen in `05_governance_s15.md`. Saverys/CMB NV control = 56.56% economic /
61.59% voting (single share class, no loyalty voting; the voting>economic gap is just the
treasury-share mechanical effect). The §15 gate (multi-year median P/NAV ≥ 0.85) is
**effectively N/A** — <1yr of clean post-rebrand history. On the evidence:

- **Fee load immaterial** — CMB NV auxiliary services (cost-plus +5%) + shipping services
  (1.25% of revenue) + office lease ≈ **$15.2m/yr ≈ 0.18–0.21% of GAV**, independent-
  committee-reviewed. Not the TEN-archetype external-manager drain.
- **Distributions pro-minority** — the large 2022-23 specials went pari-passu; the cut was
  a *funded capital-allocation pivot*, not a starve; payouts resumed at 50% of net profit.
- **Natural experiment favourable** — through the 2021-24 Euronav saga minorities got the
  **same $18.43 the controller paid the exiting Frontline block** (court-tested, US +
  Brussels blocks rejected).
- **No structural extraction mechanism.**

**`governance_discount_pct = 0`.** The genuine risk is *strategy/agency drift* (capital
sunk into a hydrogen/ammonia bet, related-party drop-downs), which we express through
**conservative newbuild/off-curve marks**, not a governance multiplier. Recorded in
`decisions/cmbt_log.md`.

**Tripwires (any one → re-open the haircut):** (1) GOGL Bermuda appraisal settles above
merger value, or FourWorld Antwerp claim succeeds; (2) related-party fee creep off
cost-plus; (3) distribution backsliding below ~50% through the next down-leg; (4) multi-year
median P/NAV settles <0.85 alongside any of 1–3; (5) erosion of the independent Audit &
Risk Committee majority.

---

## 5. Engine generalization (the only locked-code change; design in `06_engine_design.md`)

The design surfaced a **latent bug**: `carveout._sleeve_for` has no branch for dry_bulk or
container classes — they all fall through to `return "crude"`, so a crude carve-out of a
CMBT-shaped fleet would silently swallow Capes and boxships. The generalization fixes it.

**Minimal, surgical, back-compatible diff** (full file:line list in the design doc):

- **`carveout.py`** — add a `CLASS_SECTOR` map; make `_sleeve_for` sector-aware (preserving
  the LR2→crude / LR1→product defaults and "explicit `crude` defers to class"); change
  `sleeve_values` to return a `dict[sector→value]` (N-way, not a 3-tuple); add a
  parameterized `sector_carve_out(inputs, sector)`; **convert the three legacy
  `crude/product/lng_carve_out` into thin wrappers** over it (keeps every `test_carveout.py`
  import + assertion green).
- **`pipeline.py`** — add `MULTI_SLEEVE_TICKERS = {"CMBT": ["crude","dry_bulk","containerships"]}`;
  add `_aggregate_multi_sleeve_report(list[(report,share)])` (generalizes
  `_aggregate_three_sleeve_report`, min-length scenario pairing — all three are 4-scenario
  so n=4 cleanly; per-sleeve strip horizons 8/8/10 are handled *inside* each sleeve's
  `run_scenarios`, so the aggregator only sums per-share FVs); a `_class_map_for_sector`
  resolver; wire `_run_scenarios_for_ticker` through the generic sleeve-loop; a
  `_append_multi_sleeve_breakdown`; widen the whole-co labelers to treat MULTI_SLEEVE names
  as `[WHOLE-CO]`. Single-point `value_company` follows the TEN precedent (un-carved
  detail report; the scenario report is the headline).
- **`scenarios.py`** — **no change** (dry_bulk + container class maps and container
  `strip_horizon:10` already exist).
- **New tests** — N-sleeve split invariant (would have caught the `_sleeve_for` bug),
  aggregator arithmetic, horizon-mix, MULTI_SLEEVE routing/labeling, CMBT SANITY +
  aggregation invariant, off-curve attachment.

Legacy INSW (2-sleeve) and TEN (3-sleeve) paths are left untouched; the generic path serves
the genuinely new combination. Verification: full pytest must stay ≥315 green (the gate
includes the drift gate), `/reconcile CMBT` SANITY=OK, drift gate clean → ratify baseline.

---

## 6. Rough NAV sanity sketch (order-of-magnitude — NOT the engine output)

Hand marks (crude-class transaction curves are higher; this is a floor check): crude
on-curve ~$1.5bn, dry_bulk ~$4.4–4.9bn, container ~$0.36bn → on-curve ~$6.3–6.8bn; off-curve
(chem $0.28bn + Windcat $0.20bn + FSO ~$0.15bn + HFS $0.14bn + NB-net ~$0.6bn) ~$1.4bn;
+ cash $0.19bn + WC $0.17bn − debt $5.24bn − goodwill excluded ≈ **$2.8–3.3bn equity ≈
$9.5–11.5/sh asset NAV**. That sits **at/below book ($10.14) and well below price (~$16)**
→ the tool likely reads CMBT **fairly-valued-to-modestly-expensive on NAV**, with the
dividend strip (backed by the $3.26bn backlog + strong current crude/bulk rates) supplying
the gap to price. Notably this does **not** obviously confirm the broker "deep discount to
NAV" narrative — the divergence is itself a tool output (the call), per the project
philosophy. Real marks come from the age-curve engine post-build.

---

## 7. Reconcile posture & open items

- **consensus_pnav = APPROX** (no clean broker NAV; Pareto coverage unconfirmed). Reconcile
  **Job A (±50% broker-NAV bug gate) cannot anchor cleanly** — CMBT is tracked on
  self-consistency like NAT/ASC/CCEC. The Pareto name-sweep (`sp_scan --names CMBT`, alias
  Euronav/CMB.TECH/Saverys) runs at onboarding and may surface a Pareto NAV statement.
- **Toolchain fix (flagged by 3/6 agents):** `scripts/fetch_pdf.py` `USER_AGENT="Mozilla/5.0"`
  **403s on SEC EDGAR** — SEC's fair-access policy requires a contact-bearing UA. The working
  path was `curl -A "crude-tanker-fv research <email>"`. **Recommend** updating the UA so the
  allowlisted path works for the CMBT report-day refresh (and every SEC filer). Small,
  surgical, empirically validated.
- **Per-vessel gaps:** scrubber fitment is undisclosed in SEC filings for the whole fleet
  (would need Clarksons/VesselsValue); per-hull NB contract prices/advances are not broken
  out (only aggregate $ per segment). Neither blocks the build.
- **Yard-quality discount (§9.4):** the 3 newest VLCCs + the own-built Newcastlemax series
  are Chinese (Qingdao Beihai) → modern top-tier Chinese ~5% haircut; the older Capesize
  book spans SWS / NTS / Japanese yards — apply per-yard tiers in the manifest.

---

## 8. Build sequence (post-approval)

1. **(CHECKPOINT — this memo)** owner signs off architecture + §15 + off-curve conventions.
2. Engine generalization (carve-out + aggregator + routing) + new tests → pytest green.
3. `/add-ticker CMBT --sector crude` scaffold → fill the multi-segment manifest (per-vessel
   from `01/02/03`), balance sheet (corporate debt, off-curve lines, NB book), cost, dividend.
4. Pareto name-sweep + watchlist row (APPROX consensus_pnav) + close `decisions/cmbt_log.md`.
5. Pipeline + `/reconcile CMBT` (SANITY=OK) + drift gate → ratify baseline.
6. Week-close docs: METHODOLOGY §11.x prose, CLAUDE.md MULTI_SLEEVE note, TICKER_NOTES,
   LIMITATIONS (chemical/offshore still off-curve).
