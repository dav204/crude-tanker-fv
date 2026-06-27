I have confirmed the critical bug: dry_bulk and container classes currently fall through to the `crude` sleeve. The design is now fully grounded. Let me write the deliverable.

This is the engineering design. All file:line citations are against the current tree.

---

# Engineering Design — Multi-Sleeve Hybrid Support (CMBT: crude + dry_bulk + container)

## 0. Context and the load-bearing constraint

The 2-sleeve (INSW) and 3-sleeve (TEN) aggregators are hardcoded to crude/product/lng. Three facts shape every decision below:

1. **The sleeve-assignment predicate `carveout._sleeve_for` (`carveout.py:33-46`) has NO branch for dry_bulk or container classes — they all fall through to `return "crude"`.** I verified this empirically: `Cape`, `Pana`, `Supra-Ultra`, `Ctr-Feeder`, `Ctr-Intermediate`, `Ctr-Large` all currently return `sleeve="crude"`. This is the single most important thing to fix; without it a CMBT crude carve-out would silently swallow the entire fleet.
2. **`sleeve_values()` (`carveout.py:66-82`) is hardcoded to a 3-tuple `(crude, product, lng)`** and is the single denominator source of truth used by all three carve-outs. A 6-way split cannot be expressed in a 3-tuple.
3. **Scenario lists differ in length and horizon across sectors** (verified): crude=4/h8, dry_bulk=4/h8, containerships=**4**/h**10**, product=5/h8, lng=5/h8. CMBT's three sectors are crude(4,8) + dry_bulk(4,8) + container(4,10) — all 4-scenario, so the `min()` index-pairing in the aggregator yields 4 paired scenarios cleanly, but the **horizons differ (8 vs 8 vs 10)** and that is handled per-sleeve inside `run_scenarios` (each sleeve reads its own `doc["strip_horizon"]` at `scenarios.py:382`), so the aggregator never needs to reconcile horizons — it only sums per-share FVs.

The cleanest design is a **single parameterized `sector_carve_out(inputs, sector)` keyed on a sleeve-map**, plus an **N-sleeve aggregator over a list of `(report, share)`**, plus a **`MULTI_SLEEVE_TICKERS` registry** mapping a ticker to its ordered sleeve sectors.

---

## 1. CARVE-OUT GENERALIZATION

### 1.1 Generalize the sleeve taxonomy (`carveout.py:28-46`)

Replace the three flat class-sets with a **class→sector map** and make `_sleeve_for` sector-aware. New module-level constant:

```
CLASS_SECTOR = {
    "VLCC":"crude","Suezmax":"crude","Aframax":"crude","LR2":"crude",
    "MR":"product","LR1":"product","Handysize":"product","Handymax":"product",
    "LNGC":"lng","MGC":"lng",
    "Cape":"dry_bulk","Pana":"dry_bulk","Supra-Ultra":"dry_bulk",
    "Ctr-Feeder":"containerships","Ctr-Intermediate":"containerships","Ctr-Large":"containerships",
}
```

Note the LR1/LR2 asymmetry already baked into `_sleeve_for`: LR2 defaults crude, LR1 defaults product, both overridable by `vessel.sleeve`. Preserve that exactly — `CLASS_SECTOR` should keep `LR2:"crude"` and `LR1:"product"` as the class default, and an explicit `vessel.sleeve` still wins. The dual-use `crude_fraction` LR1 path (`_sleeve_fractions`, `carveout.py:49-63`) stays.

`_sleeve_for` becomes: if `vessel.sleeve` is explicitly set to a known sector, use it; else `CLASS_SECTOR.get(vessel.cls, "crude")`. **This is back-compatible** because the existing default `vessel.sleeve="crude"` (`schemas.py:34`) is the loader default — but the carve-out must distinguish "explicitly tagged crude" from "defaulted crude". The current code already relies on the class-default winning over the `"crude"` default-tag (see the comment at `carveout.py:38-40`); preserve that by treating `sleeve=="crude"` as "unset, defer to class" unless the class itself maps to crude. Cleanest: only honor `vessel.sleeve` overrides for the non-default sectors (`product`/`lng`/`dry_bulk`/`containerships`); `"crude"` always defers to class. That keeps every existing test green.

### 1.2 Generalize `sleeve_values` to an N-way split (`carveout.py:66-82`)

Replace the 3-tuple with a **dict keyed by sector**:

```
def sleeve_values(inputs) -> dict[str, float]:
    out = defaultdict(float)
    for v in inputs.fleet.vessels:
        value = vessel_market_value(v, md.vessel_value_curves[v.cls], yard_discounts) * v.count
        for sector, frac in _sleeve_fractions_by_sector(v).items():
            out[sector] += value * frac
    return dict(out)
```

`_sleeve_fractions_by_sector(v)` generalizes `_sleeve_fractions` (`carveout.py:49-63`): dual-use LR1 still splits `{crude:cf, product:1-cf}`; everything else is `{_sleeve_for(v): 1.0}`. The total denominator is `sum(out.values())`.

**Back-compat shim:** keep a thin `sleeve_values_3tuple(inputs)` returning `(d.get("crude",0), d.get("product",0), d.get("lng",0))` if you want to avoid touching the three legacy carve-outs' internals — OR (preferred) refactor the legacy carve-outs to consume the dict (see 1.4).

### 1.3 The parameterized `sector_carve_out(inputs, sector)`

A single function replacing the three near-identical bodies (`crude_carve_out` `carveout.py:108-166`, `product_carve_out` `:221-278`, `lng_carve_out` `:306-362`):

```
@dataclass
class SectorCarveOut:
    sector: str
    sleeve_inputs: CompanyInputs
    sleeve_share: float          # this sleeve's vessel value / whole-co vessel value
    sleeve_value: float
    all_values: dict[str, float] # full split, for the banner/aggregator
    def carved_price(self, whole_price): return whole_price * self.sleeve_share

def sector_carve_out(inputs, sector) -> SectorCarveOut:
    values = sleeve_values(inputs)
    total = sum(values.values()) or 1.0
    share = values.get(sector, 0.0) / total
    vessels = [replace(v, count=v.count*f, crude_fraction=None)
               for v in inputs.fleet.vessels
               for f in [_sleeve_fractions_by_sector(v).get(sector, 0.0)] if f > 0.0]
    bs = inputs.balance_sheet
    # vessel-secured debt: only crude/product have specific-debt fields today
    specific = _sector_specific_debt(bs, sector)        # crude->crude_specific_debt, product->product_specific_debt, else 0
    corporate = bs.total_debt - bs.crude_specific_debt - bs.product_specific_debt
    sleeve_debt = specific + corporate * share
    sleeve_bs = replace(bs,
        cash_and_equivalents=bs.cash_and_equivalents*share,
        working_capital_net=bs.working_capital_net*share,
        total_debt=sleeve_debt,
        lease_liabilities=bs.lease_liabilities*share,
        newbuild_capex_commitments=bs.newbuild_capex_commitments*share,
        newbuild_advances_paid=bs.newbuild_advances_paid*share,
        preferred_equity=bs.preferred_equity*share,
        shuttle_contracted_book=bs.shuttle_contracted_book*share,
        crude_specific_debt=0.0, product_specific_debt=0.0)
    sleeve_cost = replace(inputs.cost_structure,
        annual_G_and_A=inputs.cost_structure.annual_G_and_A*share,
        annual_interest_expense=inputs.cost_structure.annual_interest_expense*share)
    md = inputs.market_data
    if sector == "product":
        md = _remap_rates_for_product(md)               # carveout.py:184-204, unchanged
    return SectorCarveOut(sector, replace(inputs, fleet=replace(inputs.fleet, vessels=vessels),
                          balance_sheet=sleeve_bs, cost_structure=sleeve_cost, market_data=md),
                          share, values.get(sector,0.0), values)
```

**Sleeve-split predicate** (which classes → which sleeve), restated for CMBT:
- crude sleeve ← {VLCC, Suezmax, Aframax, LR2-default, LR1·crude_fraction}
- dry_bulk sleeve ← {Cape, Pana, Supra-Ultra} → class map `{"Cape":"cape","Pana":"pana","Supra-Ultra":"supra_ultra"}` (`scenarios.py:77-85`)
- containerships sleeve ← {Ctr-Feeder, Ctr-Intermediate, Ctr-Large} → class map `{"Ctr-Feeder":"ctr_feeder","Ctr-Intermediate":"ctr_intermediate","Ctr-Large":"ctr_large"}` (`scenarios.py:86-95`)

**Balance-sheet pro-rating rules** (unchanged from the established pattern, `carveout.py:130-158`):
- *Vessel-secured debt* → its own sleeve directly. Today only `crude_specific_debt`/`product_specific_debt` exist (`schemas.py:82-83`). **dry_bulk and container have NO specific-debt field.** Recommendation: do NOT add `dry_bulk_specific_debt`/`container_specific_debt` fields unless CMBT actually discloses ship-mortgage tranches by segment. CMB.TECH finances largely at the corporate/Hemen-style level; treat its debt as corporate and let it pro-rate by value share. If a future disclosure splits mortgages by segment, add fields then (schema is additive, default 0.0).
- *Everything else* (cash, WC, leases, newbuild commitments/advances, preferred, shuttle_contracted_book, governance_discount_pct) → pro-rate by `share`. Note `governance_discount_pct` is a scalar that applies identically to each sleeve (it is NOT scaled — `replace` leaves it as-is, which is correct per `schemas.py:108`).

### 1.4 Back-compat for the three existing carve-outs

Two options:
- **(A) Keep `crude_carve_out`/`product_carve_out`/`lng_carve_out` as thin wrappers** that call `sector_carve_out` and adapt the return into the legacy `CarveOut`/`ProductCarveOut`/`LngCarveOut` dataclasses (`carveout.py:85-96, 207-218, 291-303`). This preserves every import in `pipeline.py:21` and every test in `test_carveout.py` verbatim. **Recommended** — lowest blast radius.
- (B) Migrate all callers to `sector_carve_out`. More churn, touches `pipeline.py:263-264, 277, 348-352` and ~12 tests. Defer.

Pick **(A)**. The legacy dataclasses' `.crude_value`/`.product_value`/`.lng_value` accessors map onto `all_values`.

---

## 2. N-SLEEVE AGGREGATOR

Generalize `_aggregate_three_sleeve_report` (`pipeline.py:157-220`) into:

```
def _aggregate_multi_sleeve_report(
    sleeves: list[tuple[ScenarioReport, float]],   # ordered [(report, share), ...]
    *, ticker, whole_price, whole_target, sectors: list[str],
) -> ScenarioReport:
    reports = [r for r, _ in sleeves]
    shares  = [s for _, s in sleeves]
    n = min(len(r.scenarios) for r in reports)     # min-length index pairing
    agg = []
    for i in range(n):
        cells = [r.scenarios[i] for r in reports]
        lead = cells[0]                            # first sleeve carries display name/weight/cycle
        agg.append(ScenarioFV(
            name=lead.name, weight=lead.weight,
            fair_value=sum(c.fair_value for c in cells),
            fair_value_low=sum(c.fair_value_low for c in cells),
            fair_value_high=sum(c.fair_value_high for c in cells),
            nav_per_share=sum(c.nav_per_share for c in cells),
            vessel_scale=lead.vessel_scale,        # lead sleeve, informational
            divstrip_npv=sum(c.divstrip_npv for c in cells),
            cycle_position=lead.cycle_position,
            w_nav=lead.w_nav,
            assumed_tce=sum(c.assumed_tce * sh for c, sh in zip(cells, shares)),  # value-weighted
        ))
    total_w = sum(s.weight for s in agg)
    pw_fv = sum(s.weight * s.fair_value for s in agg) / total_w
    ev = pw_fv - whole_price
    basis = _multi_sleeve_basis(sectors, shares)
    return ScenarioReport(
        ticker=ticker, current_price=whole_price, analyst_target=whole_target,
        base_nav_per_share=sum(r.base_nav_per_share for r in reports),
        breakeven_tce=reports[0].breakeven_tce,    # lead-sleeve proxy (same convention as today)
        scenarios=agg, probability_weighted_fv=pw_fv,
        upside_best=max(s.fair_value for s in agg) - whole_price,
        downside_worst=min(s.fair_value for s in agg) - whole_price,
        expected_value_vs_current=ev,
        position_recommendation=position_recommendation(ev / whole_price * 100.0),
        basis=basis, sector=reports[0].sector)
```

Make `_aggregate_three_sleeve_report` and `_aggregate_hybrid_report` thin wrappers over this (or leave them and have the multi-sleeve path use the new one). **Keep both old functions** so `test_three_sleeve_aggregator_sums_per_scenario` (`test_carveout.py:177-225`) stays green — or update that test to call the generalized one and assert the same arithmetic.

**Handling the enumerated concerns:**

- **Differing scenario-list lengths** — `min(len(r.scenarios))` over all sleeves, identical to `pipeline.py:173`. For CMBT all three are 4, so n=4. If a sleeve had 5 (e.g. a future product addition), the 5th is dropped — same semantics as the documented INSW `structural_decline` drop (`pipeline.py:115-118`). **Add an explicit guard/log if `n < max(len)`** so a silent scenario drop is visible (the existing code drops silently).
- **Differing per-sector strip horizons (8/8/10)** — **not the aggregator's concern.** Each sleeve's `run_scenarios` already reads `doc["strip_horizon"]` (`scenarios.py:382`) and builds its own `qkeys`/strip internally. The aggregator only sums per-share FVs that have already been computed at the right horizon. The container sleeve's 10-quarter strip and the crude sleeve's 8-quarter strip both reduce to a per-share FV before they reach the aggregator. **This is already correct — no change needed.** Just document it in the basis/banner.
- **Weighted `assumed_tce`** — value-weighted by sleeve share, exactly as `pipeline.py:190-192`, generalized to `zip(cells, shares)`.
- **Basis banner** — `_multi_sleeve_basis(["crude","dry_bulk","containerships"], shares)` produces e.g. `WHOLE-COMPANY 3-SLEEVE = crude (X%) + dry_bulk (Y%) + containerships (Z%) AGGREGATED (METHODOLOGY §11.x). Off-curve segments (chemical/offshore/FSO/newbuild book) sit at the corporate level and flow through NAV uniformly. Compared to the WHOLE-COMPANY tape price.` The string must still start with `WHOLE-COMPANY` so `render_scenario_markdown` (`scenarios.py:549-554`) and the roll-up basis detection (`scenarios.py:671`) tag it `[WHOLE-CO]`.

---

## 3. ROUTING / REGISTRATION

### 3.1 Registry

Add a `MULTI_SLEEVE_TICKERS` mapping ticker → ordered sleeve sectors (`pipeline.py`, near `:51-57`):

```
MULTI_SLEEVE_TICKERS: dict[str, list[str]] = {
    "CMBT": ["crude", "dry_bulk", "containerships"],
}
```

Keep `HYBRID_TICKERS` (INSW) and `THREE_SLEEVE_TICKERS` (TEN) as-is for back-compat, OR express them through the same map (`"INSW":["crude","product"]`, `"TEN":["crude","product","lng"]`) and derive the legacy sets from the map's keys. **Recommended:** make `MULTI_SLEEVE_TICKERS` the single source of truth and derive:
```
HYBRID_TICKERS = {t for t,s in MULTI_SLEEVE_TICKERS.items() if len(s)==2}      # back-compat
THREE_SLEEVE_TICKERS = {t for t,s in MULTI_SLEEVE_TICKERS.items() if t=="TEN"} # keep literal if INSW/TEN semantics must not drift
```
But this risks subtly changing the `ticker in HYBRID_TICKERS` checks scattered across `_write_broker_sweep`, `run_scenarios_watchlist`, etc. (search shows ~10 sites). **Safer minimal diff: leave INSW/TEN literal sets untouched, add `MULTI_SLEEVE_TICKERS` for genuinely new (≥3 heterogeneous or non-crude/product/lng) names, and have `_run_scenarios_for_ticker` check all three sets.** The `hybrid=` flags in `BrokerSweepRow`/`TxnComparisonRow` should become `multi_sleeve = ticker in (HYBRID_TICKERS | THREE_SLEEVE_TICKERS | MULTI_SLEEVE_TICKERS.keys())`.

### 3.2 `_run_scenarios_for_ticker` wiring (`pipeline.py:223-296`)

Add a multi-sleeve branch. The cleanest generalization of the whole function body:

```
sleeve_sectors = MULTI_SLEEVE_TICKERS.get(ticker)
if sleeve_sectors is None and ticker not in HYBRID_TICKERS and ticker not in THREE_SLEEVE_TICKERS:
    ... existing pure-play routing (pipeline.py:241-259) unchanged ...

# Map legacy hybrids onto the generic path:
sleeve_sectors = sleeve_sectors or (["crude","product","lng"] if ticker in THREE_SLEEVE_TICKERS
                                    else ["crude","product"])
sleeves = []
for sec in sleeve_sectors:
    carve = sector_carve_out(ci, sec)
    cmap = _class_map_for_sector(sec)          # crude->default crude map; product->PRODUCT_SCENARIO_CLASS_MAP;
                                                # dry_bulk/containerships->SCENARIO_CLASS_MAP_BY_SECTOR[sec]; lng->default
    r = run_scenarios(carve.sleeve_inputs, carve.carved_price(whole_price),
                      carve.carved_price(whole_target), sector_docs[sec],
                      scenario_class_map=cmap, asof_quarter=asof_quarter)
    sleeves.append((r, carve.sleeve_share, sec))
headline = _aggregate_multi_sleeve_report(
    [(r,s) for r,s,_ in sleeves], ticker=ticker, whole_price=whole_price,
    whole_target=whole_target, sectors=[sec for *_,sec in sleeves])
```

**Return-tuple back-compat:** the public signature returns `(headline, crude_sleeve, product_sleeve)` (`pipeline.py:227`). For CMBT there is no product sleeve; return `(headline, crude_r, None)` (crude is sleeve[0]). The only consumer of the 2nd/3rd slot is `run_scenarios_watchlist` `:572-573` (`_append_hybrid_breakdown` for INSW only) — gated on `ticker in HYBRID_TICKERS`, so CMBT won't hit it. **Add a generalized `_append_multi_sleeve_breakdown`** (analog of `_append_hybrid_breakdown` `:436-467`) that takes the full sleeve list, gated on `ticker in MULTI_SLEEVE_TICKERS`. This needs the full per-sleeve report list, so widen the return to either a 4th element (list of `(report,share,sector)`) or a dedicated accessor; cleanest is to return the sleeve list as a new optional 4th tuple element and update the three call sites (`pipeline.py:567, 620, 791`) to unpack `*_` for the tail.

**Class-map resolver `_class_map_for_sector`** centralizes the routing currently inline at `pipeline.py:251-256` and `:271`:
```
def _class_map_for_sector(sector):
    if sector == "product": return PRODUCT_SCENARIO_CLASS_MAP
    if sector in ("dry_bulk","containerships"): return SCENARIO_CLASS_MAP_BY_SECTOR[sector]
    return None   # crude/lng use the module default
```

### 3.3 `value_company` single-point path (`pipeline.py:325-428`)

Today the single-point detail report only carves the **crude** sleeve and only for `HYBRID_TICKERS` (`:348-352`); **TEN (3-sleeve) is NOT carved at single-point level** — it values the whole company on the crude class map, which works only because TEN's non-crude classes are routed by `compute_nav` regardless. For CMBT the single-point report has two viable options:
- **(A) Mirror TEN: leave `value_company` un-carved for CMBT** (don't add it to the `HYBRID_TICKERS` carve at `:348`). The single-point FV report then runs whole-company NAV (correct — `compute_nav` handles all classes) but the dividend strip uses the **crude** scenario forwards by default, which is wrong for a fleet that's majority non-crude. TEN gets away with this because its scenario/strip headline lives in the scenario report, and the single-point report is explicitly the "detail" report. **Acceptable but flag it.**
- **(B) Make the single-point report multi-sleeve too** — more work, out of scope for v1. Defer.

**Recommendation:** match the TEN precedent (option A) and lean on the scenario report as the CMBT headline. Add a `note` in `value_company` for `MULTI_SLEEVE_TICKERS` saying the single-point strip is crude-sleeve-only and the whole-co view lives in the scenario report (mirror the TEN handling). Critically, ensure the single-point strip horizon is sane: `run_watchlist` passes `horizons.get(sector,8)` (`pipeline.py:497-500,511`), and CMBT's watchlist `sector:` will be `crude` (its lead) → horizon 8, fine.

---

## 4. OFF-CURVE ATTACHMENT (chemical, offshore/Windcat, FSO, multi-segment newbuild book)

CMB.TECH carries segments with **no sector in the engine**: 8× 25k chemical tankers, Windcat offshore/CTV/CSOV, 2× FSO, and a large multi-segment newbuild book (Newcastlemax/VLCC/container/ammonia). The established precedent is explicit (METHODOLOGY §11.5 ASC chemical residual at `working_capital_net:447,469`; §11.6 TEN shuttle at `shuttle_contracted_book:530-531`; §3.1/§9.6 newbuild-at-market).

**Recommended conventions, in priority order:**

1. **Multi-segment newbuild book → `newbuild_capex_commitments` + `newbuild_advances_paid`** (`schemas.py:77-78`), valued **newbuild-at-delivered-market less remaining commitment, PV-discounted** per §9.6 / the CLAUDE.md rule (`1.11^(−years_to_delivery)`). Newbuilds whose class HAS a curve (VLCC, Newcastlemax≈Cape-proxy, container) and that deliver **inside** a sleeve's strip horizon should enter that sleeve's `fleet_schedule` (`schemas.py` fleet_schedule; §3.1:197) so the strip captures forward earnings. Newbuilds delivering **past** the horizon (most of CMBT's book) carry **only the balance-sheet lines** — no scenario impact, exactly the STNG VLCC-NB precedent (`METHODOLOGY:470`). Ammonia/H2 newbuilds with no curve → off-curve at contracted value or advances-paid (see 4.4).

2. **Chemical (8× 25k) → `working_capital_net`** as a §11.5 chemical-Handy residual (ASC precedent, `:447`). Carry at recent S&P/broker value less a liquidity discount. These are too small/specialized for the product Handysize curve. This is a flat NAV add, pro-rated across sleeves by the carve-out (`share`), which is acceptable since it's a corporate-stack residual — OR attach it to whichever sleeve is least wrong (none is a natural home; corporate-stack pro-rate is cleanest and matches `working_capital_net` treatment at `carveout.py:136`).

3. **FSO (2) → `shuttle_contracted_book`** if on long contracts (NPV of contracted cash flows, the §11.6 off-curve-at-contracted-book convention, `:530-531`), else `working_capital_net` at residual value. FSOs are contract-anchored assets exactly like TEN's DP2 shuttles — `shuttle_contracted_book` is the right line. **Recommendation: rename the field's *semantics* in docs to "contracted-book off-curve sleeve" (the schema name stays `shuttle_contracted_book` to avoid a migration), and put the FSO NPV here.** The carve-out already pro-rates it as a corporate-stack item (`carveout.py:148`).

4. **Windcat offshore/CTV → `working_capital_net`** (or `shuttle_contracted_book` if its CSOV charters are long and disclosed) at an EV estimate. No offshore sector exists and onboarding one is out of scope (CLAUDE.md "Offshore" listed out-of-scope, `METHODOLOGY:48`). Carry as an off-curve corporate-stack residual with a documented EV mark and a liquidity haircut.

**Cleanest single convention:** two off-curve buckets, both already in the schema and both already pro-rated by every carve-out:
- **`shuttle_contracted_book`** for *contract-anchored* off-curve assets (FSO, long-charter CSOV) — carried at NPV of contracted cash flows.
- **`working_capital_net`** for *spot/residual* off-curve assets (8× chem, short-charter Windcat) — carried at EV-less-haircut.
- **newbuild lines** for the orderbook.

This requires **zero schema changes** and reuses the exact §11.5/§11.6 precedents. Document each mark with its rationale in `decisions/cmbt_log.md` (the §11.6 discipline). The one judgment call to surface to the owner: whether off-curve marks should pro-rate across sleeves (current carve-out behavior) or attach to a single sleeve — pro-rating is the path of least resistance and is defensible since these are genuinely corporate-stack/cross-segment.

---

## 5. TEST IMPACT

### 5.1 Existing tests that exercise the carve-out/aggregator

- **`tests/test_carveout.py`** (the whole file): `test_crude_share_by_vessel_value`, `test_balance_sheet_allocated_pro_rata`, `test_vessel_specific_debt_allocated_directly`, `test_preferred_equity_pro_rated_by_sleeve`, `test_three_sleeve_carve_outs_sum_to_one` (`:125-136`), `test_three_sleeve_corporate_stack_aggregates_to_whole_co` (`:139-162`), `test_three_sleeve_fleet_split_is_clean` (`:165-174`), `test_three_sleeve_aggregator_sums_per_scenario` (`:177-225`), `test_dual_use_lr1_split`, `test_product_carve_out_complements_crude`, `test_whole_company_nav_aggregation_invariant`, `test_product_rate_remap_uses_clean_variants`, `test_insw_outputs_are_clearly_labeled_v2_whole_company`.
- **`tests/test_nav.py`**, **`tests/test_scenarios.py`** — touch sleeve/carve paths.
- The **drift gate** (`tests/test_drift_gate.py`) and **`tests/test_containerships_sector.py`** exercise the container sector independently.

### 5.2 What could break

- **`sleeve_values` return-type change (3-tuple → dict)** breaks any caller that unpacks `crude_v, product_v, lng_v = sleeve_values(...)`. Only the three carve-out bodies do this today (`carveout.py:120,236,320`). Wrapping them (option 1.4-A) keeps `test_carveout.py:51-94, 272-303` green.
- **`_sleeve_for` sector-awareness change** — risk that an existing crude/product/lng vessel re-routes. Mitigated by keeping the LR2/LR1 class defaults and the "crude defers to class" rule. The `test_dual_use_lr1_split` (`:241-263`) and `test_three_sleeve_fleet_split_is_clean` (`:165-174`) are the canaries — they must stay green unchanged.
- **`_aggregate_three_sleeve_report` refactor** — if it becomes a wrapper, `test_three_sleeve_aggregator_sums_per_scenario` (`:177-225`) and its `"3-SLEEVE" in headline.basis` assert (`:225`) must still pass. Keep the 3-sleeve basis string containing `"3-SLEEVE"`.
- **Return-arity change** if `_run_scenarios_for_ticker` grows a 4th tuple element — must update all three unpack sites (`pipeline.py:567, 620, 791`).
- Nothing in `value_company` breaks if CMBT follows the TEN single-point precedent (un-carved).

### 5.3 New tests a CMBT build needs

1. **`tests/test_carveout.py` — N-sleeve split invariant (synthetic CMBT):** a fixture `_crude_bulk_ctr_hybrid()` (VLCC + Cape + Ctr-Large), assert `sum of the three sector shares == 1.0`, each sleeve's fleet contains only its own classes (`{"VLCC"}`, `{"Cape"}`, `{"Ctr-Large"}` — this is the test that would have caught the `_sleeve_for` fall-through bug), and corporate-stack items (cash/debt/preferred/shuttle_contracted_book/WC) re-aggregate to whole-co. Direct analog of `:125-162`.
2. **N-sleeve aggregator arithmetic:** analog of `test_three_sleeve_aggregator_sums_per_scenario` (`:177-225`) over a 3-element sleeve list with the new `_aggregate_multi_sleeve_report`; assert per-scenario FV sums, PW FV, base-NAV sum, and `"crude"+"dry_bulk"+"containerships"` all appear in `basis`.
3. **Horizon-mix invariant:** assert that aggregating an 8-quarter crude sleeve with a 10-quarter container sleeve produces a finite headline and that the container sleeve's `run_scenarios` used horizon 10 (assert via the container sleeve report's strip, or via a `strip_horizon` echo). Guards the "differing horizons" concern.
4. **`MULTI_SLEEVE_TICKERS` routing / output labeling:** analog of `test_insw_outputs_are_clearly_labeled_v2_whole_company` (`:323-383`) — once CMBT YAML inputs exist, assert `cmbt_scenarios.md` carries `[WHOLE-CO]` and `WHOLE-COMPANY`, the scenario roll-up row reads `WHOLE-COMPANY (hybrid aggregation)`, broker sweep / txn comparison flag it `(WHOLE-CO)`.
5. **Locked-weights / calibration-lock test (per CLAUDE.md "Reconciliation job B"):** CMBT is a new *multi-sleeve* configuration, not a new sector — but dry_bulk×container×crude composition needs a SANITY+calibration assertion. New `tests/test_cmbt.py` (scaffolded by `/add-ticker`) asserting `/reconcile CMBT` → SANITY=OK (tool NAV within ±50% of broker NAV) and the whole-co NAV/share ≈ sum of sleeve NAVs (the aggregation invariant, analog of `test_whole_company_nav_aggregation_invariant` `:295-303`).
6. **Off-curve attachment test:** assert that populating `shuttle_contracted_book` (FSO) + `working_capital_net` (chem/Windcat) + newbuild lines flows additively into whole-co NAV and pro-rates across all three sleeves (sum-to-whole-co).
7. **Drift gate:** after CMBT lands, ratify the baseline (`./scripts/ratify_baseline.sh`) and add CMBT to `baselines/reconcile_baseline.yaml` so `tests/test_drift_gate.py` covers it.

---

## 6. MINIMAL DIFF SHAPE

Surgical change list, in dependency order:

**`src/crude_tanker_fv/carveout.py`**
- Add `CLASS_SECTOR` constant after `:30`; keep `CRUDE_CLASSES/PRODUCT_CLASSES/LNG_CLASSES` (referenced) or derive them from it.
- Generalize `_sleeve_for` (`:33-46`) to be sector-aware via `CLASS_SECTOR`, preserving "crude defers to class" and LR2/LR1 defaults.
- Add `_sleeve_fractions_by_sector(v) -> dict[str,float]` generalizing `_sleeve_fractions` (`:49-63`).
- Change `sleeve_values` (`:66-82`) to return `dict[str,float]`; add a `sleeve_values_3tuple` shim if not refactoring legacy bodies.
- Add `SectorCarveOut` dataclass + `sector_carve_out(inputs, sector)` (new, modeled on `:108-166`) + `_sector_specific_debt(bs, sector)` helper.
- Convert `crude_carve_out`/`product_carve_out`/`lng_carve_out` (`:108,221,306`) to thin wrappers over `sector_carve_out` (preserves the legacy return dataclasses and all `test_carveout.py` imports).

**`src/crude_tanker_fv/pipeline.py`**
- Add `MULTI_SLEEVE_TICKERS` near `:57`.
- Add `_multi_sleeve_basis(sectors, shares)` and `_class_map_for_sector(sector)` helpers.
- Add `_aggregate_multi_sleeve_report(...)` (new, modeled on `_aggregate_three_sleeve_report` `:157-220`); make `_aggregate_three_sleeve_report` and `_aggregate_hybrid_report` (`:96-154`) thin wrappers OR leave them and route CMBT through the new one.
- Rewrite the carve/aggregate block of `_run_scenarios_for_ticker` (`:261-296`) to the generic sleeve-loop; keep the pure-play branch (`:241-259`) and the `(headline, crude_r, product_r[, sleeves])` return shape (widen tuple, update unpack at `:567, 620, 791`).
- Add `_append_multi_sleeve_breakdown(...)` (analog of `_append_hybrid_breakdown` `:436-467`); call it in `run_scenarios_watchlist` (`:572-573`) gated on `ticker in MULTI_SLEEVE_TICKERS`.
- Widen the `hybrid=` flags in `BrokerSweepRow`/`TxnComparisonRow` construction (`:669, 834`) and the `_write_*` labelers (`:716-724, 745, 883, 909`) to treat `MULTI_SLEEVE_TICKERS` names as whole-co.
- In `value_company` (`:348`): do **NOT** add CMBT to the crude-only carve (follow TEN precedent); add a `notes` line for multi-sleeve names pointing to the scenario report as headline.

**`src/crude_tanker_fv/scenarios.py`** — **no engine change required.** The dry_bulk and containerships class maps and the container `strip_horizon:10` already exist (`:77-95`, `:382`). Only confirm `SCENARIO_CLASS_MAP_BY_SECTOR` is importable where `_class_map_for_sector` needs it (it is, `:52`).

**`inputs/`** — CMBT YAML artefacts via `/add-ticker`: `fleet_manifests/cmbt.yaml` (vessels tagged with explicit `sleeve:` for any ambiguous class, off-curve segments NOT as vessels), `balance_sheets/cmbt_2026-Q1.yaml` (corporate debt, `shuttle_contracted_book` for FSO, `working_capital_net` for chem/Windcat, newbuild lines), `cost_structures/cmbt.yaml`, `dividend_policies/cmbt.yaml`, and a `watchlist.yaml` row with `sector: crude` (lead) + `consensus_pnav` (likely APPROX).

**`tests/test_cmbt.py`** (new, scaffolded) + the 6-7 new tests in §5.3. **`baselines/reconcile_baseline.yaml`** re-ratified post-onboarding.

**Docs (week-close):** a new METHODOLOGY §11.x for the multi-sleeve generalization (cite §11.5 chem residual, §11.6 contracted-book, §3.1/§9.6 newbuild-at-market), CLAUDE.md `MULTI_SLEEVE_TICKERS` note alongside `HYBRID_TICKERS`/`THREE_SLEEVE_TICKERS`, and `decisions/cmbt_log.md`.

---

### The one bug this design exists to fix

`carveout._sleeve_for` (`src/crude_tanker_fv/carveout.py:33-46`) returns `"crude"` for every dry_bulk and container class today (verified empirically). Until `CLASS_SECTOR` routing lands, any crude carve-out of a CMBT-shaped fleet silently pulls Capes and container ships into the crude sleeve. The N-sleeve split-invariant test (§5.3 item 1) is the regression guard.

Key files: `/Users/dan_personal/Projects/crude-tanker-fv/src/crude_tanker_fv/carveout.py`, `/Users/dan_personal/Projects/crude-tanker-fv/src/crude_tanker_fv/pipeline.py`, `/Users/dan_personal/Projects/crude-tanker-fv/src/crude_tanker_fv/scenarios.py`, `/Users/dan_personal/Projects/crude-tanker-fv/src/crude_tanker_fv/schemas.py`, `/Users/dan_personal/Projects/crude-tanker-fv/tests/test_carveout.py`.