"""Input loaders (METHODOLOGY.md section 4).

Reads the YAML files under ``inputs/`` into the dataclasses in ``schemas``.
Filenames are lower-cased (``dht.yaml``, ``dht_2026-Q1.yaml``); the ticker
argument is case-insensitive. Validation is intentionally light and lives only
at this boundary (required keys, class enum, non-negative age).
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

from .schemas import (
    BalanceSheet,
    CompanyInputs,
    CostStructure,
    DividendPolicy,
    FleetManifest,
    MarketData,
    Vessel,
    VesselValueCurve,
)

INPUTS_DIR = Path(__file__).resolve().parents[2] / "inputs"
ALLOWED_CLASSES = {"VLCC", "Suezmax", "Aframax", "LR2", "LR1", "MR", "Handymax", "Handysize", "LNGC", "MGC",
                   # dry_bulk classes added 2026-06-09 with SBLK onboarding (METHODOLOGY §11.7.1)
                   "Cape", "Pana", "Supra-Ultra",
                   # containerships classes added 2026-06-12 (METHODOLOGY §11.8.1):
                   # Feeder ≤2,000 TEU / Intermediate 2,000-5,500 / Large >5,500
                   "Ctr-Feeder", "Ctr-Intermediate", "Ctr-Large"}


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"input file not found: {path}")
    with open(path) as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"expected a YAML mapping at top level of {path}")
    return data


def _require(data: dict, key: str, path: Path):
    if key not in data or data[key] is None:
        raise ValueError(f"missing required key '{key}' in {path}")
    return data[key]


def load_fleet_manifest(ticker: str, inputs_dir: Path = INPUTS_DIR) -> FleetManifest:
    """Load ``inputs/fleet_manifests/{ticker}.yaml`` (section 4.1)."""
    path = inputs_dir / "fleet_manifests" / f"{ticker.lower()}.yaml"
    data = _read_yaml(path)

    vessels: list[Vessel] = []
    for raw in data.get("vessels") or []:
        cls = raw.get("class")
        if cls not in ALLOWED_CLASSES:
            raise ValueError(f"vessel {raw.get('id')!r}: unknown class {cls!r} in {path}")
        age = raw.get("age")
        if age is None or age < 0:
            raise ValueError(f"vessel {raw.get('id')!r}: age must be >= 0, got {age!r}")
        vessels.append(
            Vessel(
                id=raw["id"],
                cls=cls,
                dwt=raw["dwt"],
                age=age,
                scrubber=bool(raw.get("scrubber", False)),
                eco=bool(raw.get("eco", False)),
                charter_status=raw.get("charter_status", "spot"),
                charter_rate=raw.get("charter_rate"),
                charter_end=raw.get("charter_end"),
                yard=raw.get("yard"),
                count=int(raw.get("count", 1)),
                sleeve=raw.get("sleeve", "crude"),
                crude_fraction=raw.get("crude_fraction"),
            )
        )

    schedule = {
        cls: [float(x) for x in counts]
        for cls, counts in (data.get("fleet_schedule") or {}).items()
    }
    coverage = {
        cls: [float(x) for x in covs]
        for cls, covs in (data.get("coverage_schedule") or {}).items()
    }
    return FleetManifest(
        ticker=_require(data, "ticker", path),
        report_date=str(_require(data, "report_date", path)),
        vessels=vessels,
        spot_coverage_pct=data.get("spot_coverage_pct") or {},
        fleet_summary=data.get("fleet_summary") or {},
        fleet_schedule=schedule,
        coverage_schedule=coverage,
    )


def load_balance_sheet(
    ticker: str, quarter: str, inputs_dir: Path = INPUTS_DIR
) -> BalanceSheet:
    """Load ``inputs/balance_sheets/{ticker}_{quarter}.yaml`` (section 4.2)."""
    path = inputs_dir / "balance_sheets" / f"{ticker.lower()}_{quarter}.yaml"
    data = _read_yaml(path)
    fields = [
        "cash_and_equivalents",
        "working_capital_net",
        "total_debt",
        "lease_liabilities",
        "newbuild_capex_commitments",
        "newbuild_advances_paid",
        "diluted_shares_outstanding",
    ]
    return BalanceSheet(
        ticker=_require(data, "ticker", path),
        quarter=str(_require(data, "quarter", path)),
        crude_specific_debt=float(data.get("crude_specific_debt") or 0.0),
        product_specific_debt=float(data.get("product_specific_debt") or 0.0),
        preferred_equity=float(data.get("preferred_equity") or 0.0),
        shuttle_contracted_book=float(data.get("shuttle_contracted_book") or 0.0),
        governance_discount_pct=float(data.get("governance_discount_pct") or 0.0),
        **{f: float(_require(data, f, path)) for f in fields},
    )


def load_dividend_policy(ticker: str, inputs_dir: Path = INPUTS_DIR) -> DividendPolicy:
    """Load ``inputs/dividend_policies/{ticker}.yaml`` (section 4.3)."""
    path = inputs_dir / "dividend_policies" / f"{ticker.lower()}.yaml"
    data = _read_yaml(path)
    return DividendPolicy(
        ticker=_require(data, "ticker", path),
        policy_type=_require(data, "policy_type", path),
        payout_ratio=float(_require(data, "payout_ratio", path)),
        base_dividend_per_share=float(data.get("base_dividend_per_share") or 0.0),
        floor=float(data.get("floor") or 0.0),
    )


def load_cost_structure(ticker: str, inputs_dir: Path = INPUTS_DIR) -> CostStructure:
    """Load ``inputs/cost_structures/{ticker}.yaml`` (section 4.4)."""
    path = inputs_dir / "cost_structures" / f"{ticker.lower()}.yaml"
    data = _read_yaml(path)
    return CostStructure(
        ticker=_require(data, "ticker", path),
        opex_per_day={k: float(v) for k, v in (data.get("opex_per_day") or {}).items()},
        annual_G_and_A=float(data.get("annual_G_and_A") or 0.0),
        annual_interest_expense=float(data.get("annual_interest_expense") or 0.0),
        effective_tax_rate=float(data.get("effective_tax_rate") or 0.0),
    )


def load_market_data(inputs_dir: Path = INPUTS_DIR) -> MarketData:
    """Load the four files under ``inputs/market_data/`` (section 4.5).

    Only ``vessel_value_curves.yaml`` is required for NAV; the rate files are
    loaded leniently (classes with null values are skipped) so the templates
    don't break a NAV-only run.
    """
    md_dir = inputs_dir / "market_data"

    curves: dict[str, VesselValueCurve] = {}
    curves_doc = _read_yaml(md_dir / "vessel_value_curves.yaml")
    raw_curves = curves_doc.get("classes") or {}
    yard_discounts = {
        yard: float(pct)
        for yard, pct in (curves_doc.get("yard_discounts") or {}).items()
        if pct is not None
    }
    for cls, c in raw_curves.items():
        if not c or c.get("five_year_benchmark") is None:
            continue  # unfilled template entry
        curves[cls] = VesselValueCurve(
            cls=cls,
            dwt=c["dwt"],
            newbuild=float(c["newbuild"]),
            five_year_benchmark=float(c["five_year_benchmark"]),
            ten_year_benchmark=float(c["ten_year_benchmark"]),
            scrap_25yr=float(c["scrap_25yr"]),
            scrubber_premium=float(c.get("scrubber_premium") or 0.0),
            # NOTE: explicit 0.0 must be preserved (not coerced to default 0.05);
            # ``or`` would treat 0.0 as missing. LNGC / MR / LR1 set this to 0.
            eco_premium_pct=(
                float(c["eco_premium_pct"]) if c.get("eco_premium_pct") is not None else 0.05
            ),
        )

    def _scalar_map(filename: str, top_key: str) -> dict:
        data = _read_yaml(md_dir / filename).get(top_key) or {}
        return {k: float(v) for k, v in data.items() if v is not None}

    def _list_map(filename: str, top_key: str) -> dict:
        data = _read_yaml(md_dir / filename).get(top_key) or {}
        return {
            k: [float(x) for x in v]
            for k, v in data.items()
            if v and all(x is not None for x in v)
        }

    return MarketData(
        vessel_value_curves=curves,
        spot_tce=_scalar_map("spot_tce.yaml", "spot_tce"),
        ffa_forward_curve=_list_map("ffa_forward_curve.yaml", "ffa_forward_curve"),
        twelve_month_tc=_scalar_map("twelve_month_tc.yaml", "twelve_month_tc"),
        historical_tce_means=_scalar_map("historical_tce_means.yaml", "historical_tce_means"),
        yard_discounts=yard_discounts,
    )


def load_company_inputs(
    ticker: str, quarter: str, inputs_dir: Path = INPUTS_DIR
) -> CompanyInputs:
    """Load and bundle all per-company inputs for a run.

    Dividend policy and cost structure are optional at the NAV stage; if their
    files are missing, minimal placeholders are used so NAV can still run.
    """
    try:
        dividend_policy = load_dividend_policy(ticker, inputs_dir)
    except FileNotFoundError:
        dividend_policy = DividendPolicy(ticker=ticker, policy_type="unknown", payout_ratio=0.0)
    try:
        cost_structure = load_cost_structure(ticker, inputs_dir)
    except FileNotFoundError:
        cost_structure = CostStructure(ticker=ticker)

    return CompanyInputs(
        fleet=load_fleet_manifest(ticker, inputs_dir),
        balance_sheet=load_balance_sheet(ticker, quarter, inputs_dir),
        dividend_policy=dividend_policy,
        cost_structure=cost_structure,
        market_data=load_market_data(inputs_dir),
    )


def load_watchlist(inputs_dir: Path = INPUTS_DIR, live_prices: bool = False) -> dict[str, dict]:
    """Load ``inputs/watchlist.yaml`` -> {ticker: {current_price, analyst_target, as_of}}.

    Used by the report header, breakeven solve, and roll-up (section 7).

    ``live_prices=True`` (the pipeline CLI) overrides ``current_price``
    with the daily fetched close from ``prices_daily.yaml`` when fresh
    and unflagged; the watchlist static survives as ``as_of_price`` for
    vintage-matched consumers (broker NAV via consensus_pnav, consensus
    EPS via consensus_fwd_pe — both Pareto ratios tied to the as_of
    price). Default False keeps tests deterministic.
    """
    data = _read_yaml(inputs_dir / "watchlist.yaml")
    out: dict[str, dict] = {}
    for ticker, entry in data.items():
        if not isinstance(entry, dict):
            continue
        if entry.get("current_price") is None or entry.get("analyst_target") is None:
            continue  # not yet ready to value (e.g. target TBD)
        out[ticker] = {
            "current_price": float(entry["current_price"]),
            "analyst_target": float(entry["analyst_target"]),
            "consensus_pnav": (
                float(entry["consensus_pnav"]) if entry.get("consensus_pnav") is not None else None
            ),
            # Consensus 1-year-forward P/E (Pareto Shipping Daily). Feeds the
            # consensus-EPS cross-check (§9.11) — the earnings-leg analog of the
            # broker-NAV sweep. None for names without a published forward P/E.
            "consensus_fwd_pe": (
                float(entry["consensus_fwd_pe"]) if entry.get("consensus_fwd_pe") is not None else None
            ),
            # Sector layer (METHODOLOGY §11) — picks which scenario set to value
            # the name through. Defaults to crude so existing entries don't break.
            "sector": str(entry.get("sector") or "crude"),
            "as_of": entry.get("as_of"),
        }
        out[ticker]["as_of_price"] = out[ticker]["current_price"]

    if live_prices:
        from .price_refresh import is_fresh, load_daily_prices

        daily = load_daily_prices(inputs_dir)
        for ticker, entry in out.items():
            quote = daily.get(ticker)
            if quote is None:
                continue
            if quote.get("flag"):
                print(f"[watchlist] {ticker}: daily price flagged "
                      f"({quote['flag']}) — using static ${entry['current_price']}",
                      file=sys.stderr)
                continue
            if not is_fresh(quote["asof"]):
                print(f"[watchlist] {ticker}: daily price stale ({quote['asof']}) "
                      f"— using static ${entry['current_price']}", file=sys.stderr)
                continue
            entry["current_price"] = float(quote["price"])
            entry["price_as_of"] = quote["asof"]
    return out
