"""Reproduce shadow economic experiments; never invoke publication or delivery."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from dataclasses import asdict, replace
from datetime import datetime, timezone
from pathlib import Path

import yaml

from crude_tanker_fv import calendar
from crude_tanker_fv.loaders import load_company_inputs, load_watchlist, INPUTS_DIR
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.cycle import compute_cycle
from crude_tanker_fv.dividend_strip import compute_dividend_strip
from crude_tanker_fv.blend import blend_fair_value
from crude_tanker_fv.carveout import sector_carve_out
from crude_tanker_fv.pipeline import _maybe_apply_transactions, _run_scenarios_for_ticker
from crude_tanker_fv.scenarios import load_scenarios, run_scenarios, SCENARIO_CLASS_MAP_BY_SECTOR
from crude_tanker_fv.research_context import experiment, discount_rate
from crude_tanker_fv.normal_rates import normal_rate_table
from crude_tanker_fv.justified_pnav import (normalized_annual_eps, evaluate, _newbuild_value_share,
    _read_from, _robust_from, flip_margin_pct, govern_read_flag)

ROOT=Path(__file__).resolve().parents[2]
STUDY=Path(__file__).resolve().parent


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def contract_differences(rows,old):
    fields=("fv", "nav_per_share", "fv_low", "fv_high", "position", "read_flag", "weight_sign_stable", "ev_pct_family_min", "ev_pct_family_max", "blend_fv", "sleeves", "cycles", "robust", "flip_margin_pct")
    diff={t:{k:[old[t].get(k),r.get("handoff",{}).get(k)] for k in fields if old[t].get(k)!=r.get("handoff",{}).get(k)} for t,r in rows.items()}
    return {t:v for t,v in diff.items() if v}


def diagnostics(ci,price,doc,prior,parity):
    nav=compute_nav(ci).nav_per_share
    r=discount_rate(ci.fleet.ticker,.11)
    g=float(doc.get("g",.01))
    out={}
    for basis,anchors in (("parity",parity),("history",ci.market_data.historical_tce_means)):
        eps,missing=normalized_annual_eps(ci,nav,anchors)
        res=evaluate(nav,price,eps,bool(missing),bool(ci.cost_structure.opex_per_day),_newbuild_value_share(ci),r,g)
        out[basis]={**asdict(res),"normalized_annual_eps":eps,"read":_read_from(res.justified_pnav,res.pnav_mkt,res.flag)}
    robust=_robust_from(out["parity"]["read"],out["history"]["read"])
    margin=flip_margin_pct(nav,out["parity"]["justified_pnav"],out["history"]["justified_pnav"],price)
    out.update(discount_rate=r,read_flag=govern_read_flag(robust,margin,prior),flip_margin_pct=margin,
               robust=robust,earnings_basis="legacy_pre_depreciation_proxy; accounting EPS is separately versioned in cash strips")
    return out


def evaluate_name(ticker,ci,company,old,docs,watch,weight_sets,parity):
    price=watch[ticker]["current_price"]
    report,_,_=_run_scenarios_for_ticker(ticker,ci,price,price,docs,watch)
    nav=compute_nav(ci)
    sleeves={}
    for sector in company["sectors"]:
        sleeve=sector_carve_out(ci,sector).sleeve_inputs if company["hybrid"] else ci
        cyc=compute_cycle(sleeve)
        h=int(docs[sector].get("strip_horizon",8))
        strip=compute_dividend_strip(sleeve,compute_nav(sleeve).nav_per_share,strip_horizon=h,terminal_multiple=cyc.terminal_multiple)
        sr=run_scenarios(sleeve,price,price,docs[sector],scenario_class_map=SCENARIO_CLASS_MAP_BY_SECTOR[sector])
        fvs={s.name:s.fair_value for s in sr.scenarios}
        family={name:sum(w*fvs[k] for k,w in weights.items())/sum(weights.values()) for name,weights in weight_sets.get(sector,{}).items()}
        sleeves[sector]=dict(cycle=asdict(cyc),strip=asdict(strip),scenarios=asdict(sr),family_fv=family,
                            blend_fv=blend_fair_value(compute_nav(sleeve),strip,cyc).fair_value_per_share)
    fv=report.probability_weighted_fv
    from crude_tanker_fv.scorecard import valuation_index, _verdict_position
    valuation=valuation_index([], [report], [])[ticker]
    interval_low,interval_high=valuation.fv_low,valuation.fv_high
    # The lead-sector family follows the existing registered marginal-family convention.
    lead=company["sectors"][0]
    other=sum(v["scenarios"]["probability_weighted_fv"] for k,v in sleeves.items() if k!=lead)
    family=[v+other for v in sleeves[lead]["family_fv"].values()]
    family_ev=[100*(v/price-1) for v in family]
    row=copy.deepcopy(old)
    position=_verdict_position(ticker, report.position_recommendation)
    row.update(fv=round(fv,2),ev_pct=round(100*(fv/price-1),1),fv_low=round(interval_low,2),fv_high=round(interval_high,2),
               nav_per_share=round(nav.nav_per_share,2),position=position,
               weight_sign_stable=((min(family_ev)>0)==(max(family_ev)>0) and 0 not in (min(family_ev),max(family_ev))) if family_ev else None,
               ev_pct_family_min=round(min(family_ev),1) if family_ev else None,
               ev_pct_family_max=round(max(family_ev),1) if family_ev else None)
    row["cycles"]=[dict(sector=s,scope="sleeve" if company["hybrid"] else "company",ratio=v["cycle"]["cycle_position"],
                       label=v["cycle"]["band_label"],anchor_basis=old["cycles"][i]["anchor_basis"])
                   for i,(s,v) in enumerate(sleeves.items())]
    diag=diagnostics(ci,watch[ticker]["as_of_price"],docs[company["sector"]],old["read_flag"],parity)
    from crude_tanker_fv.pipeline import HYBRID_TICKERS
    point_inputs=sector_carve_out(ci,"crude").sleeve_inputs if ticker in HYBRID_TICKERS else ci
    point_cycle=compute_cycle(point_inputs)
    point_nav=compute_nav(point_inputs)
    point_strip=compute_dividend_strip(point_inputs,point_nav.nav_per_share,
        strip_horizon=int(docs[company["sector"]].get("strip_horizon",8)),terminal_multiple=point_cycle.terminal_multiple)
    row.update(read_flag=diag["read_flag"],robust=diag["robust"],
        flip_margin_pct=round(diag["flip_margin_pct"],2) if diag["flip_margin_pct"] is not None else None,
        blend_fv=round(blend_fair_value(point_nav,point_strip,point_cycle).fair_value_per_share,2),
        sleeves=[dict(sleeve=s,sector=s,fv_contribution_per_share=round(v,2)) for s,v in report.sleeve_fvs.items()] if report.sleeve_fvs else None)
    return dict(status="computed_provisional",ticker=ticker,fv=fv,nav=nav.nav_per_share,price=price,
                handoff=row,sleeves=sleeves,diagnostics=diag,discount_rate=discount_rate(ticker,.11),
                earnings_basis=next(iter(sleeves.values()))["strip"]["earnings_basis"])


def parity_audit(config,inputs):
    classes=sorted({v.cls for ci in inputs.values() for v in ci.fleet.vessels})
    rates=normal_rate_table("2026-Q2",classes)
    available={c:r.parity for c,r in rates.items() if r.parity is not None}
    share=len(available)/len(classes)
    vintages=[]
    production_commit=json.loads((STUDY/"frozen/manifest.json").read_text())["production_commit"]
    for name,cutoff in (("2026-Q1 report dates",None),("2026-06-07 war vintage","2026-06-07T23:59:59Z"),("latest post-Stage-A","2026-09-22T23:59:59Z")):
        commit=subprocess.check_output(["git","rev-list","-1","--before="+cutoff,production_commit],cwd=ROOT,text=True).strip() if cutoff else None
        vintages.append(dict(vintage=name,commit_candidate=commit or None,
                             evaluation="not eligible: full-book class-coverage kill condition" if share<.8 else "blocked: historical dated-source validation required",
                             historical_values="not backfilled from later observations"))
    return dict(status="VOID" if share<.8 else "BLOCKED",class_coverage=share,required_coverage=.8,
                coverage_basis="calculable current classes: upper bound on fully dated source coverage; historical gates not run after kill",
                classes=classes,available_classes=sorted(available),missing_classes=sorted(set(classes)-set(available)),
                latest_parity=available,vintages=vintages,band_stability=None,lock_time_reconciliation=None,
                decision="retain historical denominators; no scoped post-hoc adoption",research_fv=None)


def main():
    if os.environ.get("PYTHONHASHSEED") != "0":
        os.execve(sys.executable, [sys.executable] + sys.argv, dict(os.environ, PYTHONHASHSEED="0"))
    ap=argparse.ArgumentParser();ap.add_argument("--baseline-only",action="store_true");args=ap.parse_args()
    if ROOT.resolve()==Path("/Users/dan_personal/Projects/crude-tanker-fv"):
        raise SystemExit("research runner refuses production checkout")
    for rel,expected in json.loads((STUDY/"preregistration_hashes.json").read_text()).items():
        if sha(STUDY/rel)!=expected:raise SystemExit("preregistration changed: "+rel)
    cfg=json.loads((STUDY/"assumptions.json").read_text())
    calendar.VALUATION_DATE=cfg["valuation_date"]
    baseline=json.loads((STUDY/"frozen/book_scorecard.json").read_text())
    old={r["ticker"]:r for r in baseline["names"]}
    from unittest.mock import patch
    from crude_tanker_fv.price_refresh import is_fresh
    frozen_time=datetime.fromisoformat(baseline["generated_at"].replace("Z","+00:00"))
    with patch("crude_tanker_fv.price_refresh.is_fresh",side_effect=lambda stamp:is_fresh(stamp,now=frozen_time)):
        watch=load_watchlist(live_prices=True)
    docs={s:load_scenarios(sector=s) for s in {v.get("sector","crude") for v in watch.values()}}
    weights=yaml.safe_load((ROOT/"outputs/weight_robustness.yaml").read_text())["weight_sets"]
    inputs={t:_maybe_apply_transactions(load_company_inputs(t,"2026-Q2"),INPUTS_DIR,True)[0] for t in watch}
    parity={c:r.parity for c,r in normal_rate_table("2026-Q2",sorted({v.cls for ci in inputs.values() for v in ci.fleet.vessels})).items() if r.parity is not None}
    experiments={"legacy":[]}
    if not args.baseline_only:
        experiments.update(cash=["cash"],reference=["reference"],risk=["risk"],smooth=["smooth"],
                           cash_reference=["cash","reference"],cash_reference_risk=["cash","reference","risk"],combined=["cash","reference","risk","smooth"],
                           reference_risk_smooth=["reference","risk","smooth"])
    results={}
    out=STUDY/"results";out.mkdir(exist_ok=True)
    for name,methods in experiments.items():
        rows={}
        for ticker,ci in inputs.items():
            try:
                with experiment(cfg,methods):
                    rows[ticker]=evaluate_name(ticker,ci,cfg["companies"][ticker],old[ticker],docs,watch,weights,parity)
            except ValueError as exc:
                rows[ticker]=dict(ticker=ticker,status="unavailable",fv=None,reason=str(exc))
            print(name,ticker,rows[ticker]["status"],flush=True)
        results[name]=rows
        (out/(name+".json")).write_text(json.dumps(rows,indent=2,allow_nan=False)+"\n")
        if name=="legacy" and contract_differences(rows,old):
            raise SystemExit("legacy handoff differs; changed-method evaluations not started")
    mismatches={t:dict(reproduced=r["fv"],committed=old[t]["fv"]) for t,r in results["legacy"].items() if r["fv"] is None or round(r["fv"],2)!=old[t]["fv"]}
    (out/"baseline_reproduction.json").write_text(json.dumps(dict(matched=not mismatches,mismatches=mismatches),indent=2)+"\n")
    semantic_diff=contract_differences(results["legacy"],old)
    (out/"handoff_reproduction.json").write_text(json.dumps(semantic_diff,indent=2)+"\n")
    if semantic_diff:raise SystemExit("baseline handoff semantics differ; inspect before consumer comparisons")
    if mismatches:raise SystemExit("baseline reproduction differs; inspect before interpreting changed valuations")
    if args.baseline_only:return
    sensitivity={}
    for method in ("cash","reference","risk"):
        sensitivity[method]={}
        for point in ("low","high"):
            sensitivity[method][point]={}
            for ticker,ci in inputs.items():
                try:
                    with experiment(cfg,[method],point):
                        sr,_,_=_run_scenarios_for_ticker(ticker,ci,old[ticker]["price"],old[ticker]["price"],docs,watch)
                    value=sr.probability_weighted_fv
                    sensitivity[method][point][ticker]=dict(fv=value)
                except ValueError as exc:sensitivity[method][point][ticker]=dict(fv=None,reason=str(exc))
    (out/"sensitivity.json").write_text(json.dumps(sensitivity,indent=2,allow_nan=False)+"\n")
    (out/"parity.json").write_text(json.dumps(parity_audit(cfg,inputs),indent=2)+"\n")
    spec=importlib.util.spec_from_file_location("frozen_seam",STUDY/"frozen/seam.py");seam=importlib.util.module_from_spec(spec);spec.loader.exec_module(seam)
    registry=json.loads((STUDY/"frozen/seam_registry.json").read_text())
    events={}
    now=datetime.fromisoformat(baseline["generated_at"].replace("Z","+00:00"))
    for name,rows in results.items():
        doc=copy.deepcopy(baseline);doc["names"]=[]
        doc["economic_research"]={"schema_version":"economic-research-1", "method":name,
                                  "adoption_status":"OWNER_REVIEW_REQUIRED", "production_enabled":False,
                                  "assumptions_sha256":sha(STUDY/"assumptions.json")}
        for t,row in rows.items():
            h=copy.deepcopy(row.get("handoff",old[t]))
            if row["status"]=="unavailable":h.update(fv=None,fv_low=None,fv_high=None,read_flag=None,weight_sign_stable=None,
                blend_fv=None,sleeves=None,ev_pct=None,position=None,ev_pct_family_min=None,ev_pct_family_max=None,handoff_ready=False)
            doc["names"].append(h)
        events[name]=seam.check(dict(validation="accepted",publication_id=seam.fingerprint(doc),
                                    content_hash=seam.fingerprint(doc),scorecard=doc),registry,now=now)
        events[name]["transport"]="shadow envelope fixture only; no publication, state consumption or notifications"
        (out/(name+"_handoff.json")).write_text(json.dumps(doc,indent=2,allow_nan=False)+"\n")
    (out/"governor_events.json").write_text(json.dumps(events,indent=2,allow_nan=False)+"\n")
    comparison={}
    for t,base in results["legacy"].items():
        vals={n:rs[t]["fv"] for n,rs in results.items()}
        deltas={n:(v-base["fv"] if v is not None else None) for n,v in vals.items()}
        interaction=deltas["combined"]-sum(deltas[n] for n in ("cash","reference","risk","smooth")) if deltas["combined"] is not None else None
        comparison[t]=dict(fv=vals,delta=deltas,interaction=interaction,price=old[t]["price"],
                           blockers=cfg["companies"][t]["blockers"]+cfg["companies"][t]["risk_blockers"],
                           adoption="DEFER pending owner review and material input closure")
    (out/"comparison.json").write_text(json.dumps(comparison,indent=2,allow_nan=False)+"\n")
    from crude_tanker_fv.cash_bridge import consolidate
    hybrids={}
    for ticker,company in cfg["companies"].items():
        if not company["hybrid"]:continue
        ci=inputs[ticker];sleeves=results["legacy"][ticker]["sleeves"]
        horizon=min(len(v["strip"]["eps_by_quarter"]) for v in sleeves.values())
        periods=calendar.keys(ci.timeline["projection_start_quarter"],horizon)
        tax=ci.cost_structure.effective_tax_rate;shares=ci.balance_sheet.diluted_shares_outstanding
        operations={s:{p:(eps*shares/(1-tax) if eps>0 else eps*shares) for p,eps in zip(periods,v["strip"]["eps_by_quarter"])} for s,v in sleeves.items()}
        ledger=consolidate(company["opening"],periods,operations,tax,shares,company["policy"]["base"],company["schedules"]["base"],ci.cost_structure.annual_interest_expense/4,company["funding_cost"])
        hybrids[ticker]=dict(basis="current-market common-period issuer bridge, NOT scenario-weighted FV",periods=periods,
                            ledger=ledger,unmodelled_longer_sleeve_periods=company["horizon"]-horizon,
                            blockers=company["blockers"],scenario_weighted_fv=None)
    (out/"hybrid_current_cash.json").write_text(json.dumps(hybrids,indent=2,allow_nan=False)+"\n")


if __name__=="__main__":main()
