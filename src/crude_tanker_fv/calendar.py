"""Dated contract construction and projection alignment. No wall-clock writes."""

import copy
import hashlib
import json
import math
import os
import re
from dataclasses import replace
from datetime import date

import yaml

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
VALUATION_DATE = None


def index(label):
    m = re.fullmatch(r"(\d{4})-Q([1-4])", label)
    if not m:
        raise ValueError("invalid calendar quarter: " + str(label))
    return int(m[1]) * 4 + int(m[2]) - 1


def label(number):
    return "%04d-Q%d" % (number // 4, number % 4 + 1)


def quarter(day):
    return label(day.year * 4 + (day.month - 1) // 3)


def keys(start, count):
    return [label(index(start) + i) for i in range(count)]


def scenario_key(period):
    return "q%s_%s" % (period[-1], period[:4])


def normalize(raw, printed):
    s = re.sub(r"[\s_/-]", "", raw.lower())
    m = re.fullmatch(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(\d{2}|\d{4})?", s)
    if m:
        month = MONTHS.index(m[1]) + 1
        year = (
            int(m[2]) + (2000 if len(m[2]) == 2 else 0)
            if m[2]
            else printed.year + (month < printed.month)
        )
        if not m[2] and (year * 12 + month) - (printed.year * 12 + printed.month) > 3:
            raise ValueError("ambiguous month year: " + raw)
        return "month", "%04d-%02d" % (year, month)
    m = re.fullmatch(r"q([1-4])(\d{2}|\d{4})?", s)
    if m:
        q = int(m[1])
        year = (
            int(m[2]) + (2000 if len(m[2]) == 2 else 0)
            if m[2]
            else printed.year + (q < (printed.month - 1) // 3 + 1)
        )
        return "quarter", "%04d-Q%d" % (year, q)
    m = re.fullmatch(r"cal(\d{2}|\d{4})", s)
    if m:
        return "year", str(int(m[1]) + (2000 if len(m[1]) == 2 else 0))
    raise ValueError("ambiguous contract label: " + raw)


def construct_panel(iso, panel, deltas):
    printed = date.fromisoformat(iso)
    start = quarter(printed)
    quotes = {}
    originals = {}
    for raw, value in panel.items():
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
            or value <= 0
            or int(value) != value
        ):
            raise ValueError("invalid contract rate: " + raw)
        kind, period = normalize(raw, printed)
        if (kind, period) in quotes and quotes[kind, period] != value:
            raise ValueError("conflicting quotes: " + period)
        quotes[kind, period] = int(value)
        originals.setdefault((kind, period), []).append(raw)
    months = {p: v for (k, p), v in quotes.items() if k == "month"}
    quarters = {p: v for (k, p), v in quotes.items() if k == "quarter"}
    annuals = {int(p): v for (k, p), v in quotes.items() if k == "year"}
    if len(months) != 2 or len(quarters) != 2 or len(annuals) != 1:
        raise ValueError(
            "incomplete required panel: two months, two quarters and one calendar year required"
        )
    month_numbers = sorted(int(m[:4]) * 12 + int(m[5:]) for m in months)
    print_number = printed.year * 12 + printed.month
    if month_numbers[1] != month_numbers[0] + 1 or month_numbers[0] not in (
        print_number,
        print_number + 1,
    ):
        raise ValueError("ambiguous or stale month assignments")
    ordered = sorted(quarters, key=index)
    if index(ordered[1]) != index(ordered[0]) + 1 or index(ordered[0]) not in (
        index(start),
        index(start) + 1,
    ):
        raise ValueError("ambiguous quarter year assignments: " + str(ordered))
    year = next(iter(annuals))
    if year not in (printed.year + 1, printed.year + 2) and not (
        year == printed.year and printed.month <= 3
    ):
        raise ValueError("ambiguous calendar-year assignment")
    rates = dict(quarters)
    provenance = {
        p: {"kind": "quoted", "original_labels": originals["quarter", p], "source_date": iso}
        for p in quarters
    }
    if start not in rates:
        required = [
            "%04d-%02d" % (printed.year, m)
            for m in range(printed.month, ((printed.month - 1) // 3 + 1) * 3 + 1)
        ]
        if not all(m in months for m in required):
            raise ValueError("incomplete remaining-quarter months: " + str(required))
        total = sum(months[m] for m in required)
        rates[start] = (total + len(required) // 2) // len(required)
        provenance[start] = {
            "kind": "derived",
            "method": "equal remaining-month mean; half-up integer",
            "months": required,
            "component_rates": {m: months[m] for m in required},
            "original_labels": [r for m in required for r in originals["month", m]],
            "source_date": iso,
        }
    yearkeys = keys("%d-Q1" % year, 4)
    unknown = [q for q in yearkeys if q not in rates]
    remaining = 4 * annuals[year] - sum(rates.get(q, 0) for q in yearkeys)
    if not unknown or remaining <= 0:
        raise ValueError("invalid calendar-year identity")
    base, rem = divmod(remaining, len(unknown))
    for n, q in enumerate(unknown):
        rates[q] = base + (n < rem)
        provenance[q] = {
            "kind": "derived",
            "method": "calendar-year residual; remainder to earliest unquoted quarters",
            "calendar_year": year,
            "calendar_rate": annuals[year],
            "original_labels": originals["year", str(year)],
            "source_date": iso,
        }
    tail = index(yearkeys[-1])
    for n, delta in enumerate(deltas, 1):
        q = label(tail + n)
        prev = label(tail + n - 1)
        if q not in rates:
            rates[q] = rates[prev] + delta
            provenance[q] = {
                "kind": "derived",
                "method": "ruled tail step",
                "delta": delta,
                "from": prev,
                "source_date": iso,
            }
    periods = keys(start, 8)
    for q in keys(start, max(8, tail + 3 - index(start))):
        if q not in rates:
            prev = label(index(q) - 1)
            if prev not in rates:
                raise ValueError("missing preceding rate for " + q)
            rates[q] = rates[prev]
            provenance[q] = {
                "kind": "derived",
                "method": "flat carry-forward",
                "from": prev,
                "source_date": iso,
            }
    if any(v <= 0 for v in rates.values()):
        raise ValueError("invalid nonpositive constructed rate")
    return {
        "periods": periods,
        "values": [rates[q] for q in periods],
        "nodes": [dict(provenance[q], period=q, rate=rates[q]) for q in periods],
        "quotes": [
            {
                "kind": k,
                "period": p,
                "rate": v,
                "original_labels": originals[k, p],
                "source_date": iso,
            }
            for (k, p), v in quotes.items()
        ],
        "proxy_quarters": ordered,
        "proxy": (sum(quarters[q] for q in ordered) + 1) // 2,
    }


def policy(inputs_dir):
    path = inputs_dir / "calendar_policy.yaml"
    if not path.exists():
        return {"version": 1, "enabled": False}
    doc = yaml.load(path.read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    if doc.get("version") != 1 or not isinstance(doc.get("enabled"), bool):
        raise ValueError("invalid calendar policy")
    return doc


def projection_start(inputs_dir):
    if not policy(inputs_dir)["enabled"]:
        return None
    from .loaders import run_timestamp

    return quarter(
        date.fromisoformat(
            str(VALUATION_DATE or os.environ.get("CRUDE_FV_VALUATION_DATE") or run_timestamp()[:10])
        )
    )


def align(inputs, inputs_dir, valuation_date=None, enabled=None):
    cfg = policy(inputs_dir)
    enabled = cfg["enabled"] if enabled is None else enabled
    if not enabled:
        return inputs
    from .loaders import run_timestamp

    day = date.fromisoformat(
        str(
            valuation_date
            or VALUATION_DATE
            or os.environ.get("CRUDE_FV_VALUATION_DATE")
            or run_timestamp()[:10]
        )
    )
    start = quarter(day)
    raw = yaml.load((inputs_dir / "market_data/ffa_forward_curve.yaml").read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    calendars = raw.get("calendar_nodes", {})
    curves = {}
    nodes = {}
    for cls, values in inputs.market_data.ffa_forward_curve.items():
        source = calendars.get(cls)
        if not source or len(source) != len(values):
            raise ValueError("missing calendar mapping for FFA " + cls)
        if any(
            row.get("rate") is not None and row["rate"] != value
            for row, value in zip(source, values)
        ):
            raise ValueError("FFA values changed without calendar provenance: " + cls)
        mapping = {row["period"]: dict(row, rate=rate) for row, rate in zip(source, values)}
        periods = [row["period"] for row in source]
        if periods != keys(periods[0], len(periods)):
            raise ValueError("non-contiguous FFA mapping for " + cls)
        horizon = 10 if cls.startswith("Ctr-") else 8
        projected = []
        for q in keys(start, horizon):
            if q in mapping:
                node = mapping[q]
            elif index(q) > index(periods[-1]):
                node = {
                    "period": q,
                    "rate": values[-1],
                    "kind": "derived",
                    "method": "flat carry-forward",
                    "from": periods[-1],
                    "source_date": source[-1].get("source_date"),
                }
            else:
                raise ValueError("missing FFA calendar period " + cls + " " + q)
            projected.append(node)
        curves[cls] = [r["rate"] for r in projected]
        nodes[cls] = projected
    origin = cfg.get("schedule_origins", {}).get(inputs.fleet.ticker)
    if not origin:
        raise ValueError("missing fleet/coverage calendar mapping for " + inputs.fleet.ticker)
    signature = hashlib.sha256(
        json.dumps(
            {"fleet": inputs.fleet.fleet_schedule, "coverage": inputs.fleet.coverage_schedule},
            sort_keys=True,
        ).encode()
    ).hexdigest()
    if cfg.get("schedule_fingerprints", {}).get(inputs.fleet.ticker) != signature:
        raise ValueError(
            "fleet/coverage schedules changed without a calendar mapping review: "
            + inputs.fleet.ticker
        )
    elapsed = index(start) - index(origin)
    if elapsed < 0:
        raise ValueError("live calendar precedes schedule origin; use explicit historical replay")
    fleet = {}
    coverage = {}
    extensions = []
    for cls, values in inputs.fleet.fleet_schedule.items():
        horizon = 10 if cls.startswith("Ctr-") else 8
        static = sum(v.count for v in inputs.fleet.vessels if v.cls == cls)
        fleet[cls] = [
            values[q] if q < len(values) else static for q in range(elapsed, elapsed + horizon)
        ]
        if elapsed + horizon > len(values):
            extensions.append(
                {"class": cls, "schedule": "fleet", "method": "existing static manifest extension"}
            )
    for cls, values in inputs.fleet.coverage_schedule.items():
        horizon = 10 if cls.startswith("Ctr-") else 8
        coverage[cls] = [
            values[q] if q < len(values) else values[-1] for q in range(elapsed, elapsed + horizon)
        ]
        if elapsed + horizon > len(values):
            extensions.append(
                {"class": cls, "schedule": "coverage", "method": "existing last-coverage extension"}
            )
    timeline = {
        "valuation_date": day.isoformat(),
        "projection_start_quarter": start,
        "schedule_origin": origin,
        "elapsed_quarters": elapsed,
        "cash_flow_convention": "full quarters; unchanged end-quarter discounting",
        "ffa_nodes": {
            cls: value
            for cls, value in nodes.items()
            if cls in {v.cls for v in inputs.fleet.vessels}
        },
        "schedule_extensions": extensions,
        "scenario_extensions": [],
    }
    return replace(
        inputs,
        market_data=replace(inputs.market_data, ffa_forward_curve=curves),
        fleet=replace(inputs.fleet, fleet_schedule=fleet, coverage_schedule=coverage),
        timeline=timeline,
    )


def align_scenarios(doc, timeline, classes):
    if not timeline:
        return doc
    doc = copy.deepcopy(doc)
    horizon = int(doc.get("strip_horizon", 8))
    for name, scenario in doc["scenarios"].items():
        for cls in classes:
            block = scenario[cls]
            dated = {
                index("%s-Q%s" % (k[3:], k[1])): k
                for k in block
                if re.fullmatch(r"q[1-4]_\d{4}", k)
            }
            if not dated:
                raise ValueError("missing scenario calendar mapping " + name + " " + cls)
            last = max(dated)
            for q in keys(timeline["projection_start_quarter"], horizon):
                key = scenario_key(q)
                if key in block:
                    continue
                if index(q) <= last:
                    raise ValueError(
                        "missing internal scenario calendar period " + name + " " + cls + " " + q
                    )
                block[key] = list(block[dated[last]])
                node = {
                    "scenario": name,
                    "class": cls,
                    "period": q,
                    "kind": "derived",
                    "method": "flat carry-forward",
                    "from": label(last),
                }
                if node not in timeline["scenario_extensions"]:
                    timeline["scenario_extensions"].append(node)
    return doc
