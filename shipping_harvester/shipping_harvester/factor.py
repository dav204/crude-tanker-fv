"""Adapter: collapse the multi-broker marks panel onto your factor schema.

Produces, per quarter and vessel class:
    vessel_value_curves[class] = {newbuild, five_year_benchmark,
                                  ten_year_benchmark, scrap_25yr,
                                  scrubber_premium, eco_premium_pct}
    twelve_month_tc[class]
    spot_tce[class]

Two design points worth knowing:

1. Reconciliation. When several houses report the same class+field+quarter, a
   source-precedence policy picks the value, and the cross-broker spread is
   recorded regardless -- so you keep Weber's TC but still see that Xclusiv was
   12% off. Flip the policy to 'median'/'mean' for a consensus instead.

2. Segment-keying. Tanker and dry bulk share size names (Panamax, Handysize),
   but a coated Panamax tanker and a Panamax bulker are different vessels with
   different values. Weber is a tanker-only report, so its sizes resolve to
   tanker; the dry houses' Panamax/Handysize resolve to dry. Everything is keyed
   by (quarter, segment, class, field) so the two never reconcile together.

The vessel_value_curves dict is emitted with ALL of your schema keys present;
scrap_25yr is filled from demolition when a demolition parser exists (see
scrap_curve), and scrubber_premium / eco_premium_pct are left None because they
are your [S/J] judgment inputs, not harvested.
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass, field as dc_field, replace

import pandas as pd

from . import config, store


# --- field mapping: panel (kind, metric) -> your schema field ---------------
def _field_of(kind: str, metric: str) -> str | None:
    if kind == "vessel_value":
        return "vessel_value"
    if kind == "period_tc":
        return {"1yr_tc": "twelve_month_tc", "3yr_tc": "three_year_tc"}.get(metric)
    if kind == "spot_tce":
        return "spot_tce"
    if kind == "demolition":
        return "demolition"
    return None


# harvested anchor -> schema curve key
_ANCHOR_SCHEMA = {
    "newbuild": "newbuild",
    "five_year": "five_year_benchmark",
    "ten_year": "ten_year_benchmark",
    "scrap": "scrap_25yr",
}
# full curve shape, so emitted dicts match your schema exactly
_CURVE_KEYS = (
    "newbuild", "five_year_benchmark", "ten_year_benchmark", "scrap_25yr",
    "scrubber_premium", "eco_premium_pct",
)


# --- segment classification -------------------------------------------------
_TANKER = {"VLCC", "Suezmax", "Aframax", "LR2", "LR1", "MR", "MR2"}
_DRY = {"Capesize", "Newcastlemax", "Kamsarmax", "Ultramax", "Supramax",
        "Handysize", "Handymax", "Panamax"}   # Panamax/Handysize: dry by default
_GAS = {"LNGC", "VLGC", "MGC"}


def segment_of(vessel_class: str, broker: str) -> str:
    """tanker / dry / gas. Weber is a tanker-only report, so its sizes are
    tanker even when the name (Panamax, Handysize) also exists in dry."""
    if broker == "weber":
        return "tanker"
    if vessel_class in _GAS:
        return "gas"
    if vessel_class in _TANKER:
        return "tanker"
    if vessel_class in _DRY:
        return "dry"
    return "unknown"


# --- scrap: demolition $/ldt -> per-class scrap value ($m) -------------------
# Approx lightweight (ldt) by class; scrap_value_musd = $/ldt * ldt / 1e6.
# Inactive until a demolition parser (e.g. GMS) feeds $/ldt marks.
_LIGHTWEIGHT_LDT = {
    "VLCC": 42000, "Suezmax": 26000, "Aframax": 18000, "LR2": 18000,
    "LR1": 12000, "MR": 11000, "MR2": 11000,
    "Capesize": 22000, "Kamsarmax": 11000, "Ultramax": 10000,
    "Supramax": 9500, "Handysize": 7500, "Panamax": 10500,
}


def _demo_type(vessel_class: str) -> str | None:
    """Recycling type tag carried on a demolition mark's vessel_class."""
    v = (vessel_class or "").lower()
    if "tank" in v or v == "wet":
        return "tanker"
    if "dry" in v or "bulk" in v or "cargo" in v:
        return "dry"
    if "contain" in v:
        return "container"
    return None   # untyped (e.g. Allied's "*") -> generic bucket


def scrap_curve(panel: pd.DataFrame,
                market_priority=("bangladesh", "india", "pakistan", "turkey")):
    """Map demolition $/ldt marks -> {(quarter, segment, class): scrap_musd}.

    GMS quotes $/ldt per market AND per type (dry vs tanker), so we use the
    tanker price for tanker classes and the dry price for dry classes, picking a
    market by priority. Untyped marks (e.g. Allied's market-only "*") fall into a
    generic bucket used when a type-specific price is missing. Returns {} when
    there are no demolition marks."""
    out: dict[tuple, float] = {}
    if panel.empty or "kind" not in panel:
        return out
    demo = panel[panel["kind"] == "demolition"]
    if demo.empty:
        return out

    for quarter, q_rows in demo.groupby("quarter"):
        buckets: dict[str, dict[str, float]] = {"dry": {}, "tanker": {}, "generic": {}}
        for _, r in q_rows.iterrows():
            t = _demo_type(r["vessel_class"]) or "generic"
            if t == "container":
                continue
            mkt = (r["note"] or "").lower()
            if mkt:
                buckets[t][mkt] = float(r["value"])

        def pick(t: str) -> float | None:
            for mkt in market_priority:
                if mkt in buckets[t]:
                    return buckets[t][mkt]
            if buckets[t]:
                return next(iter(buckets[t].values()))
            for mkt in market_priority:           # fall back to generic/untyped
                if mkt in buckets["generic"]:
                    return buckets["generic"][mkt]
            return next(iter(buckets["generic"].values()), None)

        dry_p, tanker_p = pick("dry"), pick("tanker")
        for cls, ldt in _LIGHTWEIGHT_LDT.items():
            if cls in _TANKER:
                price, seg = tanker_p, "tanker"
            else:
                price, seg = dry_p, "dry"
            if price is None:
                price = tanker_p if tanker_p is not None else dry_p
            if price is not None:
                out[(quarter, seg, cls)] = round(price * ldt / 1e6, 2)
    return out


# --- resolution policy ------------------------------------------------------
@dataclass(frozen=True)
class ResolutionPolicy:
    # (field, segment) -> ordered broker preference. First present wins.
    precedence: dict = dc_field(default_factory=dict)
    # global fallback order when a (field, segment) pair isn't listed
    fallback: tuple = ("allied", "intermodal", "xclusiv", "weber")
    mode: str = "precedence"        # "precedence" | "median" | "mean"
    spread_warn_pct: float = 0.10   # flag groups whose cross-broker spread exceeds this

    def order_for(self, field: str, segment: str) -> tuple:
        return tuple(self.precedence.get((field, segment), self.fallback))


DEFAULT_POLICY = ResolutionPolicy(
    precedence={
        # value: Xclusiv is the primary house (rich resale/5/10/15yr, all eras 2021+);
        # Allied is the FALLBACK so it only wins where Xclusiv is absent — i.e. the
        # Wayback-recovered 2019-2020 quarters. (Allied-first would let spotty/stale
        # HSN Allied issues override the Xclusiv spine for 2022Q4+.)
        ("vessel_value", "dry"): ("xclusiv", "allied", "intermodal"),
        ("vessel_value", "tanker"): ("xclusiv", "allied", "intermodal"),
        # TC: Intermodal is the designated period-TC source (clean table, all eras
        # 2021+); Allied is the fallback for the 2019-2020 quarters where Intermodal
        # isn't on HSN; Xclusiv prose is a cross-check.
        ("twelve_month_tc", "tanker"): ("intermodal", "weber", "xclusiv", "allied"),
        ("twelve_month_tc", "dry"): ("intermodal", "xclusiv", "allied"),
        ("spot_tce", "tanker"): ("weber", "xclusiv", "intermodal"),
        ("spot_tce", "dry"): ("xclusiv", "intermodal", "weber"),
        ("demolition", "tanker"): ("gms", "allied", "intermodal"),
        ("demolition", "dry"): ("gms", "allied", "intermodal"),
    },
)


# --- core -------------------------------------------------------------------
def _normalise(panel: pd.DataFrame) -> pd.DataFrame:
    df = panel.copy()
    df["field"] = [_field_of(k, m) for k, m in zip(df["kind"], df["metric"])]
    df = df[df["field"].notna()].copy()
    df["segment"] = [segment_of(c, b) for c, b in zip(df["vessel_class"], df["broker"])]
    if "age_anchor" not in df:
        df["age_anchor"] = None
    return df


def _resolve_group(rows: pd.DataFrame, order: tuple, mode: str, warn: float) -> dict:
    # one value per broker (latest report_date if a broker somehow repeats)
    by_broker: dict[str, tuple[float, str]] = {}
    for _, r in rows.sort_values("report_date").iterrows():
        by_broker[r["broker"]] = (float(r["value"]), r["report_date"])
    brokers = list(by_broker)
    values = [v for v, _ in by_broker.values()]
    med = statistics.median(values)
    vmin, vmax = min(values), max(values)
    spread = (vmax - vmin) / med if med else 0.0

    if mode == "median":
        value, source, rdate = statistics.median(values), f"consensus:median({len(values)})", max(d for _, d in by_broker.values())
    elif mode == "mean":
        value, source, rdate = statistics.fmean(values), f"consensus:mean({len(values)})", max(d for _, d in by_broker.values())
    else:
        chosen = next((b for b in order if b in by_broker), None) or sorted(brokers)[0]
        value, source, rdate = by_broker[chosen][0], chosen, by_broker[chosen][1]

    return {
        "value": round(value, 4),
        "source": source,
        "n_sources": len(brokers),
        "sources": ",".join(sorted(brokers)),
        "value_min": vmin,
        "value_max": vmax,
        "spread_pct": round(spread, 4),
        "disagreement": spread > warn,
        "report_date": rdate,
    }


def to_factor_marks(panel: pd.DataFrame, policy: ResolutionPolicy = DEFAULT_POLICY) -> pd.DataFrame:
    """Resolve the panel to one row per (quarter, segment, class, field[, anchor])."""
    if panel.empty:
        return pd.DataFrame()
    df = _normalise(panel)
    # demolition is per-market, not per-class -> handled by scrap_curve/to_schema_dict
    df = df[df["field"] != "demolition"]
    keys = ["quarter", "segment", "vessel_class", "field", "age_anchor"]
    records = []
    for (quarter, segment, vclass, field, anchor), rows in df.groupby(
        keys, dropna=False
    ):
        order = policy.order_for(field, segment)
        res = _resolve_group(rows, order, policy.mode, policy.spread_warn_pct)
        records.append({
            "quarter": quarter, "segment": segment, "vessel_class": vclass,
            "field": field, "anchor": anchor,
            "unit": rows["unit"].iloc[0], **res,
        })
    out = pd.DataFrame(records)
    if not out.empty:
        out = out.sort_values(["quarter", "segment", "field", "vessel_class"]).reset_index(drop=True)
    return out


def disagreements(resolved: pd.DataFrame) -> pd.DataFrame:
    """Rows where two houses materially disagree -- feed your sanity gating."""
    if resolved.empty:
        return resolved
    cols = ["quarter", "segment", "vessel_class", "field", "anchor",
            "value", "value_min", "value_max", "spread_pct", "sources"]
    return resolved[resolved["disagreement"]][cols].reset_index(drop=True)


# --- schema-shaped output ---------------------------------------------------
def to_schema_dict(resolved: pd.DataFrame, panel: pd.DataFrame | None = None) -> dict:
    """Nested dict matching your named schema:
    {quarter: {segment: {vessel_value_curves: {class: {...}},
                         twelve_month_tc: {class: v}, spot_tce: {class: v}}}}.
    """
    scrap = scrap_curve(panel) if panel is not None else {}
    out: dict = {}
    if resolved.empty:
        return out

    for _, r in resolved.iterrows():
        q, seg, cls, fld = r["quarter"], r["segment"], r["vessel_class"], r["field"]
        node = out.setdefault(q, {}).setdefault(seg, {})
        if fld == "vessel_value":
            curve = node.setdefault("vessel_value_curves", {}).setdefault(
                cls, {k: None for k in _CURVE_KEYS}
            )
            schema_key = _ANCHOR_SCHEMA.get(r["anchor"])
            if schema_key:
                curve[schema_key] = r["value"]
        elif fld in ("twelve_month_tc", "spot_tce"):
            node.setdefault(fld, {})[cls] = r["value"]
        # three_year_tc / demolition are kept in `resolved` but not the schema dict

    # fold in scrap_25yr from demolition, but only for classes that actually
    # appear in the resolved panel (avoid phantom class entries from scrap alone)
    tracked = {(r["quarter"], r["segment"], r["vessel_class"])
               for _, r in resolved.iterrows()}
    for (q, seg, cls), scrap_musd in scrap.items():
        if (q, seg, cls) not in tracked:
            continue
        curve = (out.setdefault(q, {}).setdefault(seg, {})
                 .setdefault("vessel_value_curves", {})
                 .setdefault(cls, {k: None for k in _CURVE_KEYS}))
        curve["scrap_25yr"] = scrap_musd
    return out


# --- convenience ------------------------------------------------------------
def load_and_resolve(policy: ResolutionPolicy = DEFAULT_POLICY):
    """Read the stored panel and resolve it. Returns (resolved_df, panel_df)."""
    panel = store.build_panel(write=False)
    return to_factor_marks(panel, policy), panel
