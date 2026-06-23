# Test 1 — data contract (free broker-weekly path)

**Date:** 2026-06-22. **Companion to** `PRE_REGISTRATION_TEST1.md`. Defines
**exactly** what each historical vintage must contain so `run_engine_test1.py`
can compute a no-look-ahead EV%(i,q). Data path decided by the owner:
**free broker-weekly** (the vendored `shipping_harvester` crawling the
aggregators' WordPress archives — not a paid feed). This contract is the spec the
backfill must satisfy and the yardstick a future paid feed would be judged
against.

## Vintage layout (what the harness reads)

One directory per as-of quarter, a **partial mirror** of the live `inputs/` tree:

```
backtest/vintages/<YYYY-Qn>/
  watchlist.yaml                       # price + sector + (optional) consensus_pnav, as-of q
  scenario_inputs.yaml                 # derived neutral forward, keyed q{start}_… for THIS vintage
  fleet_manifests/<ticker>_<YYYY-Qn>.yaml
  balance_sheets/<ticker>_<YYYY-Qn>.yaml
  cost_structures/<ticker>_<YYYY-Qn>.yaml
  dividend_policies/<ticker>_<YYYY-Qn>.yaml
  market_data/
    vessel_value_curves.yaml           # PER-QUARTER — broker-weekly (the signal-sign-moving leg)
    twelve_month_tc.yaml               # PER-QUARTER — broker-weekly
    spot_tce.yaml                      # PER-QUARTER — broker-weekly
    ffa_forward_curve.yaml             # DERIVED (engine mean-reversion synthesis)
    historical_tce_means.yaml          # slow-moving, held
    transactions/<class>.yaml          # disclosed prints with print_date ≤ q only
```

The harness calls `run_scenarios_watchlist(quarter=q, asof_quarter=q,
inputs_dir=backtest/vintages/<q>)`. Files not present fall back to the live
`inputs/` copy **only** when this contract marks them "slow-roll / held"; the
per-quarter files are mandatory.

## Component spec — source, vintaging, no-look-ahead stamp

| Component | Free source | Per-quarter or slow-roll? | Public-date stamp (≤ q) |
|---|---|---|---|
| **price** (EV% denominator) | Sharadar SEP `close` at q-end (raw traded price, NOT adjclose) | per-quarter | trade date ≤ q |
| forward total return (dependent var, not an input) | Sharadar SEP `adjclose` | per-quarter | date ≤ q / ≤ q+1 |
| analyst_target | **not in free archives** → set = price (neutral) and DROP the target-relative reads | per-quarter | n/a |
| consensus_pnav (benchmark only) | Pareto archive (`inputs/research_pareto/`, 2024-08+) | where available | report_date ≤ q |
| **BS core** (cash, total_debt, shares, equity, G&A, interest, tax) | **Sharadar SF1** `datekey ≤ q` (reuse `loaders_sharadar`) | per-quarter (nearest-prior filing) | `datekey` ≤ q |
| BS shipping-specific (NB capex commitments, advances paid, lease split, sleeve debt) | 6-K/20-F parse | **slow-roll** nearest-prior filing | filed ≤ q |
| fleet manifest | issuer fleet list | **slow-roll** one base + disclosed deltas; ages rolled deterministically; `years_to_delivery` recomputed at q | filed ≤ q |
| cost structure (opex/day per class) | issuer / broker opex | **slow-roll** nearest-prior | filed ≤ q |
| dividend policy | issuer policy | **slow-roll** nearest-prior | filed ≤ q |
| **vessel_value_curves** (NB / 5yr / 10yr / scrap per class) | **broker weekly** — Allied (QuantumSea) + Xclusiv value tables (richest age splits); Intermodal/Bancosta backfill | **per-quarter** | issue `report_date` ≤ q |
| **twelve_month_tc** (per class) | **broker weekly** — Intermodal / Bancosta period-TC tables | **per-quarter** | `report_date` ≤ q |
| **spot_tce** (per class) | **broker weekly** — Weber / Intermodal spot | **per-quarter** | `report_date` ≤ q |
| ffa_forward_curve | **DERIVED** — engine mean-reversion synthesis from 12M TC + spot (the existing "constructed curve" path) | derived per vintage | n/a |
| historical_tce_means (through-cycle) | slow-moving — held, or recomputed from the value-house 10yr series | **held** | n/a |
| transactions/<class> | disclosed S&P prints | per-quarter **filter** of the live set to `print_date ≤ q` | print_date ≤ q |

**The only legs that move EV%'s *sign* per quarter are price + vessel marks +
TC** (the memo's finding). Everything marked slow-roll/held perturbs EV%
*magnitude* and is held at nearest-prior; the HOLD-band (|EV%|<10%) and NB-heavy
name-quarters where that could flip a sign are **flagged, not trusted** (per the
pre-registration), and reserved for targeted full reconstruction.

## The two derived legs (locked methodology, not knobs)

These depart from the live bespoke engine and so are pinned here:

1. **ffa_forward_curve** — synthesized, not sourced. Per class, a deterministic
   mean-reversion from the vintaged 12M-TC level toward that class's
   through-cycle mean over the strip horizon (the engine's existing constructed-
   curve mechanism). No separate FFA vintage is harvested.
2. **scenario_inputs.yaml (the scenario forward)** — the live escalation /
   pre_mou / mou_base / mou_bear set is a **2026-specific geopolitical
   construct** and is NOT back-projected. Historical vintages use a **neutral
   symmetric bracket** around the vintaged forward, locked as: per class, per
   strip quarter `q{start}…` (from `strip_start_from_asof`), `base` = the
   mean-reversion forward (leg 1); `low`/`high` = base × (1 ∓ 0.25); scenario
   weights base 0.50 / low 0.25 / high 0.25. This is the one deliberate
   departure of the historical engine from the live engine (pre-registration
   §caveats), fixed before any run so it is not a post-hoc choice.

## Slow-roll base & deterministic aging

Per name, author **one** base fleet/cost/dividend snapshot (the earliest
in-window issuer filing) and roll forward: vessel ages +0.25/quarter,
`years_to_delivery` −0.25/quarter (newbuilds cross to on-the-water at 0), apply
disclosed fleet deltas (sales/deliveries) at the quarter their filing is public.
BS core is refreshed per-quarter from Sharadar; BS shipping-specific rolls with
the base. This is the memo's "slow-roll" — it makes ~14 names × ~28 quarters
tractable without a per-quarter issuer census.

## Environment prerequisite (the binding execution gate)

The harvester is **Python 3.10+** (`shipping_harvester/.../models.py`
`@dataclass(slots=True)` → `TypeError` under this Mac's 3.9.6; confirmed
2026-06-22). The free-broker-weekly extraction therefore needs **one** of:
- a 3.10+ interpreter + the harvester's deps (the clean path), or
- a small **3.9 backport** of the harvester (drop `slots=True` — a pure perf
  hint, 3 sites in `models.py`; audit for other 3.10-only constructs).

Everything *downstream* of extraction (Sharadar BS, prices, the as-of engine, the
harness, the statistic) already runs in the repo's 3.9 venv. So this gate blocks
only the vessel-mark/TC vintage production, not the rest of the pipeline.

## Backfill execution order (free broker-weekly)

1. **Env**: stand up the 3.10+ harvester (or 3.9-backport).
2. **MVP first (2024-Q1→present, parsers already tuned):** crawl Allied/Xclusiv/
   Intermodal/Weber issues ≤ each quarter-end → `factor` adapter → the
   class-rename + `dwt`-injection shim (`Capesize`→`Cape`, etc.) → write
   `vessel_value_curves` / `twelve_month_tc` / `spot_tce` per vintage. Synthesize
   the derived legs. Pull Sharadar BS core per vintage. Slow-roll fleet/cost/div.
3. **Run** `run_engine_test1.py` over the MVP vintages → expect INCONCLUSIVE
   (the pre-stated MVP outcome); confirm the pipeline + measure real per-quarter
   assembly cost.
4. **Powered window (2018-Q3→2023):** per-era parser development for the value
   houses across the 2018–2023 format eras (the harvester's format-version
   dispatch scaffolds it; only 2024+ is tuned) + the Bancosta-2025-style OCR
   sub-path where `pdftotext` hits a font cipher. The 10yr anchor is the thinnest
   leg (only Allied & Xclusiv tabulate it). Sizing per the format-drift probe:
   ~2–4 weeks focused.

## What stays out of scope (no free-archive source)

LR2 value (folded into Aframax by every free house) → Aframax-proxy or
transactions; analyst targets → neutralized; pre-2024 Pareto P/NAV → the
naive-benchmark comparison is limited to 2024-08+.
