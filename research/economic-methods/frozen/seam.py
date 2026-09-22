"""Deterministic producer seam. Events request reviews; they never authorize orders."""
import hashlib
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TEXT = ("confidence_tier", "position", "read_flag", "balance_sheet_vintage")
REQUIRED_NUM = ("fv", "price", "fv_low", "fv_high", "ev_pct_family_min", "ev_pct_family_max")


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def evaluate(doc, registry, previous=None, now=None):
    now = now or datetime.now(timezone.utc)
    previous = previous or {}
    events, states = [], {}

    def event(ticker, code, detail, value=None, severity="page", action=None):
        events.append({"id": ticker + ":" + code, "ticker": ticker, "code": code,
                       "detail": detail, "value": value, "severity": severity,
                       "action": action or "OWNER — open a valuation mini-review; no order is authorized"})

    if registry.get("version") != 1:
        event("SYSTEM", "REGISTRY_INVALID", "unsupported registry", severity="page")
        return {"events": events, "states": states}
    try:
        if doc["schema_version"] != "2.9":
            raise ValueError("unsupported schema")
        generated = datetime.fromisoformat(doc["generated_at"].replace("Z", "+00:00"))
        age = (now - generated).total_seconds()
        if not 0 <= age <= 72 * 3600:
            raise ValueError("surface is future-dated or older than 72h")
        if not isinstance(doc["names"], list):
            raise ValueError("names must be an array")
        names = {n["ticker"]: n for n in doc["names"]}
        if len(names) != len(doc["names"]):
            raise ValueError("duplicate names")
    except (KeyError, TypeError, ValueError, AttributeError) as exc:
        event("SYSTEM", "CONTRACT_INVALID", str(exc))
        return {"events": events, "states": states}
    for ticker, rule in registry["names"].items():
        row = names.get(ticker)
        if row is None:
            event(ticker, "DATA_UNAVAILABLE", "required ticker missing")
            states[ticker] = {"valid": False}
            continue
        missing = [k for k in REQUIRED_TEXT if not isinstance(row.get(k), str) or not row[k]]
        missing += [k for k in REQUIRED_NUM if isinstance(row.get(k), bool) or not isinstance(row.get(k), (int, float)) or not math.isfinite(row[k])]
        if type(row.get("weight_sign_stable")) is not bool:
            missing.append("weight_sign_stable")
        if row.get("confidence_tier") not in ("VALIDATED-TIGHT", "GOVERNED-WIDE", "PROVISIONAL"):
            missing.append("known confidence tier")
        if not (row.get("read_flag") == "robust" or str(row.get("read_flag")).startswith("flips (") or (not rule["read_flag_governed"] and row.get("read_flag") == "n/a")):
            missing.append("known read_flag")
        if not re.fullmatch(r"\d{4}-Q[1-4]", str(doc.get("quarter"))):
            missing.append("run quarter")
        if not re.fullmatch(r"\d{4}-Q[1-4]", str(row.get("balance_sheet_vintage"))):
            missing.append("valid balance sheet quarter")
        if row.get("void"):
            missing.append("non-void valuation")
        if not missing and (row["fv"] <= 0 or row["price"] <= 0 or row["fv_low"] > row["fv_high"] or row["ev_pct_family_min"] > row["ev_pct_family_max"]):
            missing.append("consistent numeric bounds")
        if missing:
            event(ticker, "DATA_UNAVAILABLE", "unknown/invalid: " + ", ".join(missing), sorted(missing))
            states[ticker] = {"valid": False}
            continue
        states[ticker] = {"valid": True, **{k: row[k] for k in (*REQUIRED_TEXT, *REQUIRED_NUM, "weight_sign_stable")}}
        baseline = rule["baseline"]
        for field in (("confidence_tier", "read_flag", "weight_sign_stable", "position") if rule["role"] == "holding" else ()):
            if field == "read_flag" and not rule["read_flag_governed"]:
                continue
            before = baseline.get(field)
            if before is None:
                event(ticker, "BASELINE_UNKNOWN_" + field, "review baseline not documented for " + field, field)
            elif row[field] != before:
                severity = "info" if field == "position" and row["fv_low"] <= row["price"] <= row["fv_high"] else "page"
                event(ticker, "CHANGED_" + field, f"{field}: {before} → {row[field]}", row[field], severity)
        base_fv = baseline.get("fv")
        if rule["role"] != "holding":
            pass
        elif base_fv is None:
            event(ticker, "BASELINE_UNKNOWN_fv", "weighted-FV review baseline is undocumented")
        elif abs(row["fv"] - base_fv) > abs(base_fv) * rule["fv_drift_pct"] / 100 + 1e-9:
            event(ticker, "FV_DRIFT", f"weighted FV {row['fv']} differs >{rule['fv_drift_pct']:g}% from reviewed {base_fv}", "outside")
        old = previous.get(ticker, {})
        for field in ("read_flag", "weight_sign_stable"):
            if (field != "read_flag" or rule["read_flag_governed"]) and field in old and old[field] != row[field]:
                event(ticker, "TRANSITION_" + field, f"{field}: {old[field]} → {row[field]}", row[field])
        if not row["weight_sign_stable"]:
            event(ticker, "VALUATION_CONVICTION_ZERO", "weight-family sign unstable; valuation cannot support sizing", False)
        elif rule["read_flag_governed"] and row["read_flag"] != "robust":
            event(ticker, "READ_CAP", "size to the weaker-basis read: " + row["read_flag"], row["read_flag"])
        if row["confidence_tier"] == "PROVISIONAL":
            event(ticker, "PROVISIONAL", "no deployment on this valuation anchor", "PROVISIONAL")
        elif row["confidence_tier"] == "GOVERNED-WIDE":
            event(ticker, "WIDE_CAP", "valuation-supported sizing is capped", "GOVERNED-WIDE", "info")
        lagging = row["balance_sheet_vintage"] != doc.get("quarter")
        if lagging:
            substantive = any(e["ticker"] == ticker and (e["code"].startswith("CHANGED_") or e["code"] == "FV_DRIFT") and e["severity"] == "page" for e in events)
            severity = "page" if rule["role"] == "candidate" or substantive else "info"
            event(ticker, "VINTAGE_LAGGING", f"balance sheet {row['balance_sheet_vintage']}; run {doc.get('quarter')}", row["balance_sheet_vintage"], severity)
        if rule["role"] == "candidate":
            gates = {"current_balance_sheet": not lagging, "buy": row["position"].startswith("BUY"),
                     "sign_stable": row["weight_sign_stable"]}
            if rule.get("minimum_family_upside") is not None:
                gates["family_min"] = row["ev_pct_family_min"] >= rule["minimum_family_upside"]
            if rule.get("required_tier"):
                gates["tier"] = row["confidence_tier"] == rule["required_tier"]
            for key, attestation in rule.get("attestations", {}).items():
                gates[key] = attestation["status"]
            states[ticker]["gates"] = gates
            prior_gates = rule.get("previous_gates", {})
            for key, value in gates.items():
                if key in prior_gates and prior_gates[key] != value:
                    event(ticker, "GATE_" + key, f"gate {key}: {prior_gates[key]} → {value}", value,
                          action=f"OWNER — re-present {ticker} as a fresh TRADE_PREREG; remaining gates still apply")
            if all(value is True for value in gates.values()):
                event(ticker, "CANDIDATE_REVIEW", "all recorded gates clear; fresh prereg required", True)
            else:
                event(ticker, "GATES_PENDING", "gates: " + json.dumps(gates, sort_keys=True), gates, "info")
            for key, attestation in rule.get("attestations", {}).items():
                if attestation.get("due") and now.date().isoformat() >= attestation["due"] and attestation["status"] is not True:
                    event(ticker, "VENUE_DUE_" + key, "gate resolving venue is due: " + key, attestation["due"])
    labels = []
    for ticker in registry["cycle_trigger"]["tickers"]:
        cycles = (names.get(ticker) or {}).get("cycles") or []
        values = [c for c in cycles if isinstance(c, dict) and c.get("sector") == "dry_bulk" and c.get("scope") == "company"] if isinstance(cycles, list) else []
        if len(values) != 1 or values[0].get("label") not in ("late-cycle/peak", "elevated", "mid-cycle", "below-mid", "trough") or not values[0].get("anchor_basis") or not isinstance(values[0].get("ratio"), (int, float)) or not math.isfinite(values[0]["ratio"]):
            event(ticker, "CYCLE_UNAVAILABLE", "current dry-bulk cycle unavailable; R-3 is UNKNOWN")
        else:
            labels.append(values[0]["label"])
    if len(labels) == 2 and all(label in ("below-mid", "trough") for label in labels):
        event("R-3", "CYCLE_TRIGGER", "SB and SBLK both below-mid or trough: mandatory charter re-read", True)
    return {"events": events, "states": states}


def transitions(result, previous):
    old = previous.get("active", {})
    active = {e["id"]: {"value": e["value"], "severity": e["severity"]} for e in result["events"] if not e["code"].startswith("TRANSITION_")}
    changed = [e for e in result["events"] if e["severity"] == "page" and
               (e["code"].startswith("TRANSITION_") or old.get(e["id"]) != active.get(e["id"]))]
    for key in old.keys() - active.keys():
        if any(code in key for code in ("CONTRACT_INVALID", "DATA_UNAVAILABLE", "CYCLE_UNAVAILABLE", "PUBLICATION_HELD", "UNACCEPTED")):
            changed.append({"id": key + ":RECOVERED", "ticker": key.split(":")[0], "code": "RECOVERED",
                            "detail": key + " recovered", "severity": "info", "value": True,
                            "action": "No owner action; current data restored"})
    return changed, {"active": active, "states": result["states"]}


def render(result, publication_id="unknown"):
    lines = ["## Deterministic valuation checks", "", "Publication: " + publication_id]
    for event in result["events"]:
        lines.append(f"- [{event['severity']}] {event['ticker']} {event['code']}: {event['detail']} — ACTION: {event['action']}")
    if not result["events"]:
        lines.append("No valuation seam conditions triggered.")
    return "\n".join(lines) + "\n"


def check(envelope, registry=None, previous=None, now=None):
    registry = registry or json.loads((ROOT / "monitor/seam_registry.json").read_text())
    if envelope.get("validation") != "accepted":
        return {"events": [{"id": "SYSTEM:UNACCEPTED", "ticker": "SYSTEM", "code": "UNACCEPTED",
                            "detail": "accepted producer publication unavailable", "value": None,
                            "severity": "page", "action": "OWNER — restore producer publication"}], "states": {}}
    result = evaluate(envelope.get("scorecard"), registry, (previous or {}).get("states"), now)
    hold = envelope.get("publication_hold")
    if hold:
        result["events"].append({"id": "SYSTEM:PUBLICATION_HELD", "ticker": "SYSTEM", "code": "PUBLICATION_HELD",
                                 "detail": hold, "value": hold, "severity": "page",
                                 "action": "OWNER — resolve the producer publication blocker; previous accepted output retained"})
    return result
