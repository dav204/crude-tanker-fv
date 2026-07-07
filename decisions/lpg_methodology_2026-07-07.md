# LPG/VLGC sector — methodology decision doc (WO3 Phase 0) — DRAFT FOR RATIFICATION

**Authority:** WO3_LPG_ONBOARDING.md · charter Part-B verdict `fd0277f` (50% LPG, VLGC-first).
**Status:** DRAFT. Phase 1+ (any YAML) does NOT begin until the owner ratifies the forks below.
This is the methodology-doc-first gate (WORKFLOWS §Onboarding-a-sector); it records DECISIONS,
so open forks are a decision *request*, not a spec. Prospective home: METHODOLOGY §11.10.

**Charter guardrail carried verbatim (B-4):** the LPG half was chosen partly for low infra cost
("under the streetlight") — *"the allocation should not be read as a supply call on VLGCs."* The
market cells are adverse (~30% orderbook, avg age 11.7y, no scrappage lever). The engine reads the
sector honestly; it does not justify the allocation.

---

## Evidence base (sourced 2026-07-06/07; the sourcing agent stalled and was salvaged — figures below are the recovered, cited cells)

- **Current 1-yr TC (the live anchor):** BW LPG Q1-2026 call (2026-06-02): **BW Pampero fixed
  1-yr TC at "high $60,000/day"**, Aug delivery. Multi-year term structure BACKWARDATED: BW Brage
  (5-yr) + BW Gemini (3-yr) both "low $40,000/day" — long-dated sits below 1-yr, the classic
  rate-spike shape.
- **FY2026 coverage:** BW LPG "42% of portfolio with fixed rate TC and FFA hedges at $44,800 and
  $48,100/day"; Q2-2026 guidance ~$81,000/day for 85% of available days (spot-heavy).
- **Spot context (why spot ≠ TC anchor):** Baltic **BLPG1 = Ras Tanura–Chiba VLGC route**; early
  Jul-2026 print $262.50/mt → **TCE $264,164/day** — a Hormuz-crisis spike, not a normal level.
  Fearnleys W23 (2026-06-03) VLGC 84k spot ~$5.09M/month. Clarksons: 2025 MEG-Japan spot TCE avg
  **$49,669/day** (+18% YoY); 2026 opened $73,631/day, fell 30% to ~$48,000 by mid-March.
  *The daily `vlgc_*` spot columns are index-spot and currently war-distorted — NOT a TC anchor.*
- **Demand drivers (the scenario axis):** (1) **US LPG export buildout** — Enterprise +~300k bpd
  (end-2026), Energy Transfer Nederland +55k bpd LPG (H1-2027), Targa Galena Park (Q3-2027),
  MPLX/Oneok Texas City (2028) — structurally long ton-miles. (2) **China PDH demand SOFT** —
  utilization ~69-72% (Jul-Nov 2025), "cautious outlook", propane demand rising only "slightly"
  2026-27 — the demand sink is weak. (3) **Panama transit constrained** — LoTSA 2.0 (Jan-2026),
  auction slots spiked to $4M (May-2026, Hormuz reroute) — episodic ton-mile lengthener.

---

## The five Phase-0 decisions

### 1. Sector definition & scope — PROPOSED (low-fork)
- v1 values **VLGC only** (~78-93k cbm). NVGS (midsize/ethane) and GASS (small pressurized) are
  OUT of v1 — different classes/trades; census-note, don't onboard.
- Both v1 validators (Dorian, BW LPG) are pure-VLGC fleets, so **MGC is NOT needed** for v1 (the
  existing `sectors.lng.*.mgc` class stays where it is; LPG v1 carries one class, VLGC).
- **Fork 1 (minor):** confirm VLGC-only, or include MGC now for future NVGS/Exmar coverage.
  *Recommend VLGC-only — smallest honest surface, matches both validators.*

### 2. Cycle-anchor basis — **THE REAL FORK** (blocks Phase 1)
The book is TC-anchored, not spot-scaled (§10). A VLGC needs a **12M-TC series + a 10-yr mean**.
- **Current 12M-TC anchor: ~$60,000/day** is cleanly sourced (BW Pampero, arm's-length, Aug-2026).
- **10-yr mean: `INSUFFICIENT`** — the sourcing agent did not retrieve a citable 10-yr TC average
  before it stalled. What exists: 2025 full-year spot TCE avg $49,669 (one year, spot not TC);
  MGC 10-yr mean $20k on file (VLGC runs ~2-2.5×). A real long-run number lives in BW LPG / Dorian
  annual-report BLPG1 history charts — not yet pulled.
- **Fork 2 — owner picks the path:**
  - **(a) Source it first** — one targeted pass on BW LPG's + Dorian's annual reports / investor
    decks for a stated or chart-derived 10-yr VLGC earnings mean, cited, before any YAML. (~1
    session; cleanest; delays Phase 1 slightly.)
  - **(b) Documented proxy now** — anchor the 10-yr mean to the **2025 full-year $49,669 spot avg**
    as a conservative "recent-normal" (the exact move the container sector made: FY-average table,
    not the boom-distorted spot archive; §11.8.5 precedent), flagged as proxy, tightened in Q3.
    Note this reads current $60k TC as ~1.2× — "elevated", not peak — which is defensible and
    consistent with the backwardated term structure.
  - *Recommend (b) to keep WO3 moving, with a §11.10 note to upgrade to a broker 10-yr print when
    one surfaces — same discipline as the tanker-forward HOLD.*

### 3. Demand-scenario axis — PROPOSED (fork on weights only)
LPG is a demand-story sector; the axis is **US-export ton-mile growth × China-PDH absorption**,
with the fleet's ~30% orderbook as the supply overhang every scenario carries. Proposed four
scenarios (driver names, NOT a dry-bulk China clone):
1. **arb_wide** — US export capacity ramps into firm Asian PDH pull; ton-miles + Panama premium
   outrun deliveries. (bull)
2. **absorption_base** — exports grow but China PDH stays ~70% utilized; fleet growth roughly
   matches demand. (base)
3. **overhang** — the 30% orderbook delivers into soft PDH margins; rates normalize toward the
   10-yr mean. (bear)
4. **arb_collapse** — US-Asia arb closes (tariff/price) + Panama normalizes; ton-mile give-back.
   (tail)
- **Fork 3:** ratify the four scenario names + the initial **"LPG Set A (US-export-arb)"** weight
  vector. I have NOT proposed weights — that's a §11.x weight decision and wants your call given
  the sector is explicitly a non-supply-call allocation. *Suggest starting near dry-bulk-style
  0.20/0.40/0.25/0.15 and letting the weight-robustness family (shipped from birth) show
  fragility, rather than me picking a vector.*

### 4. Charter-book convention — PROPOSED (low-fork)
VLGC owners carry real TC cover (BW LPG 42% FY2026). Adopt the **§11.8.6 coverage-schedule
convention** used for containers/dry-bulk: per-vessel charter status + rate in the manifest drives
a coverage-dampened scenario spread. Spot→TC dampening applies the current-$60k-TC anchor, not the
war-spiked BLPG1 spot. **Fork 4 (minor):** confirm reuse of the §11.8.6 machinery vs a bespoke LPG
variant. *Recommend reuse — it generalized cleanly across two sectors already.*

### 5. Governance screen (§15) — PROPOSED (low-fork)
- **BW LPG:** BW Group controls a bloc → standard §15 governance/value-trap screen at blend +
  strip terminal (not compute_nav), stored per-name with rationale. Not a haircut by default —
  a screen; apply only if the structure impairs minority realisation.
- **Dorian:** widely-held, no controller → no §15 flag expected.
- **Fork 5 (minor):** confirm no §15 haircut is pre-assumed for either — the screen is judgmental
  and gets written per-name after reading the filings.

---

## What ratification unblocks
Forks 1/3/4/5 are confirm-or-adjust; **Fork 2 is the one that gates Phase 1** (the whole marks +
cycle layer keys off the 10-yr basis). On ratification: Phase 1 (sectors.lpg + weight family) →
Phase 2 (VLGC marks; the §9.9 sample from decisions/sec99_print_hunt_2026-07-06.md is v1-provisional
grade — 10-yr node strong, 5-yr flagged wide, un-anchored fallback documented) → Phase 3 (promote
`vlgc_*` under a tenor rule) → Phase 4 (Dorian CIK 1596993 + BW LPG CIK 1649313, CIKs to be
re-verified vs company_tickers.json per the FLNG/CCEC/INSW lesson) → Phase 5 (v1 lock ≥70%/±10%).

**Kill-switches live:** R-2 (VLGC orderbook >38% units → LPG half VOID); R-5 (charter expires
2026-12-26).
