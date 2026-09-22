"""Freeze research assumptions without evaluating changed fair values."""
import copy
import hashlib
import json
import math
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

from crude_tanker_fv import calendar
from crude_tanker_fv.carveout import sector_carve_out, sleeve_values_by_sector
from crude_tanker_fv.loaders import load_company_inputs, load_watchlist
from crude_tanker_fv.nav import compute_nav
from crude_tanker_fv.pipeline import _maybe_apply_transactions, HYBRID_TICKERS, THREE_SLEEVE_TICKERS, MULTI_SLEEVE_TICKERS
from crude_tanker_fv.scenarios import load_scenarios

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
calendar.VALUATION_DATE = "2026-09-22"

SOURCES = {
    "DHT": ("https://www.sec.gov/Archives/edgar/data/1331284/000095015726000847/ex99-1.htm", "2026-08-05", "ordinary income; 100%; remove unsupported nominal floor"),
    "SBLK": ("https://www.starbulk.com/gr/en/dividend-policy/", "2026-02-25", "100% operating cash less debt amortization, maintenance/upgrades and $2.1m/vessel cash deficit; $0.05 minimum"),
    "GNK": ("https://investors.gencoshipping.com/news/press-releases/news-details/2026/Genco-Shipping--Trading-Limited-Announces-Q2-2026-Financial-Results/default.aspx", "2026-08-05", "cash operating profit less voluntary reserve; Q3 target $19.5m"),
    "FRO": ("https://www.frontlineplc.cy/fro-second-quarter-and-six-months-2026-results/", "2026-08-28", "Q2 distribution equals adjusted EPS; future payout discretionary"),
    "ECO": ("https://www.sec.gov/Archives/edgar/data/1964954/000110465926090429/eco-20260630xex99d2.htm", "2026-08-04", "board discretion; retained 85% estimate is not an issuer formula"),
    "ASC": ("https://ardmoreshipping.investorroom.com/2026-04-29-Ardmore-Shipping-Provides-Update-on-Fleet-Investment%2C-Dividend-Policy%2C-and-Vessel-Sale", "2026-04-29", "two thirds adjusted earnings"),
    "HAFN": ("https://investor.hafnia.com/ir-news/news-details/2024/Hafnia-Limited--Increase-in-Quarterly-Dividend-Payout-Ratio-2024-RZ2rQvypGq/default.aspx", "2024-05-15", "net LTV ladder; 90% <=20%, 80% <=30%; issuer LTV must be reconciled"),
    "INSW": ("https://www.sec.gov/Archives/edgar/data/1679049/000110465926093033/tm2622617d1_ex99-1.htm", "2026-08-11", "current practice at least 85% adjusted income in combined distribution; not 70% plus a duplicated base"),
    "TNK": ("https://www.teekay.com/blog/2026/07/29/teekay-tankers-ltd-reports-second-quarter-2026-results-and-declares-dividend/", "2026-07-29", "fixed $0.25 quarterly; no automatic recurring special"),
    "STNG": ("https://www.scorpiotankers.com/scorpio-tankers-inc-announces-financial-results-for-the-second-quarter-of-2026-and-the-declaration-of-a-dividend/", "2026-07-29", "fixed $0.45; no assumed future buybacks"),
    "TRMD": ("https://www.torm.com/investor/share/distribution/default.aspx", "2026-09-22", "excess liquidity less per-vessel threshold and board discretionary reserve; not an EPS percentage"),
    "SB": ("https://www.sec.gov/Archives/edgar/data/1434754/000131786126000037/f072926sb6k.htm", "2026-07-28", "board-set $0.075 latest quarter; not a contractual 30% income formula"),
    "CCEC": ("https://ir.capitalcleanenergycarriers.com/press-releases", "2026-07-23", "$0.15 quarterly declaration; forward continuation assumption"),
    "FLNG": ("https://www.flexlng.com/flex-lng-second-quarter-2026-earnings-release/", "2026-08-26", "$0.75 declared; surplus cash policy; continuation is an assumption"),
    "GSL": ("https://www.globalshiplease.com/static-files/27597ccc-72ab-48f6-be44-6706626ea783", "2026-03-16", "2026 expected quarterly common distribution $0.625; preferred coupon 8.75%"),
    "BWLP": ("https://www.bwlpg.com/investor/dividends/", "2026-09-22", "shipping NPAT ladder 50/75/100%; net leverage <=30/20%; NCI is not preferred debt"),
    "LPG": ("https://dorianlpg.com/investors/stock-analysts/dividend-history/default.aspx", "2026-09-22", "irregular declared distributions; no mechanical forward payout formula"),
    "2343": ("https://www.pacificbasin.com/en/media/faq.php", "2026-09-22", "annual ordinary income ex-disposals 50%, up to100% when net cash; interim/final cadence"),
    "TEN": ("https://www.tenn.gr/earnings-releases/", "2026-09-22", "semiannual declarations; remove unsubstantiated extra 19% variable layer"),
    "CMBT": ("https://mfn.se/one/a/cmb-tech/cmb-tech-announces-q2-2026-results-04b1527a", "2026-08-27", "discretionary distribution includes share premium; joint sleeve dependence unresolved"),
    "CAPT": ("https://mfn.se/a/capital-tankers/capital-tankers-corp-board-of-directors-declares-dividend-of-nok-3-00-per-share", "2026-09-01", "NOK3 return of capital declared; construction-phase FCF and FX assumptions need review"),
    "BRUT": ("https://www.mfn.se/a/bruton-limited/bruton-limited-brut-results-for-the-six-months-ended-june-30-2026.iframe", "2026-08-13", "pre-delivery; existing zero distribution assumption retained, not a permanent policy"),
}


def main():
    if (OUT / "assumptions.json").exists():
        raise SystemExit("freeze already exists; use a new dated study for amendments")
    watch = load_watchlist()
    config = dict(version=1, created_at=datetime.now(timezone.utc).isoformat(),
                  valuation_date=calendar.VALUATION_DATE, quarter="2026-Q2", companies={}, references={},
                  source_cutoff="2026-09-22", production_enabled=False,
                  risk_calibration=dict(risk_free=.0475, erp=.0414, cash_corrected_asset_beta=.71,
                    sector_scope="Transportation proxy for all six shipping sectors; sector peer calibration NOT established",
                    source_urls=["https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm",
                                 "https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html"],
                    source_dates=["2026-09-01", "2026-01-01"],
                    asset_rate_grid={"low":.0475+.61*.0356,"base":.0475+.71*.0414,"high":.0475+.81*.0605},
                    beta_range_basis="analyst +/-0.10 sensitivity, not statistical confidence limits",
                    erp_range_basis="published normalized-payout / adjusted trailing / ten-year average CF alternatives",
                    relevering="rE=[rA*(E+D+P-C)+rf*C-rD*D-rP*P]/E; E=clean NAV; no assumed tax shield",
                    cash_basis="gross claims, all carried cash at risk-free; operational minimum-cash treatment unresolved",
                    debt_basis="carried debt plus separate leases; expense/claim implied cost unless cited rate supplied"))
    for ticker, w in watch.items():
        ci,_ = _maybe_apply_transactions(load_company_inputs(ticker,"2026-Q2"), ROOT/"inputs", True)
        bs, pol = ci.balance_sheet, ci.dividend_policy
        nav = compute_nav(ci)
        hybrid = ticker in HYBRID_TICKERS or ticker in THREE_SLEEVE_TICKERS or ticker in MULTI_SLEEVE_TICKERS
        blocks = ["forward cash schedule requires issuer-level verification; analyst timing/cost ranges are not adoption evidence"]
        source = SOURCES.get(ticker)
        if not source:
            blocks.append("current policy primary-source recheck incomplete")
            source = (bs.source_url, str(bs.retrieved_at), "existing policy estimate retained pending current disclosure review")
        policy = dict(basis="earnings", ratio=pol.payout_ratio, base_dps=pol.base_dividend_per_share,
                      additive_base=pol.policy_type=="base_plus_variable")
        if ticker in ("CMDB","BRUT"):
            policy.update(basis="none",ratio=0,base_dps=0)
        elif ticker in ("CCEC","FLNG","GSL","STNG","TNK","SB","TEN"):
            policy.update(basis="fixed",ratio=0,base_dps={"CCEC":.15,"FLNG":.75,"GSL":.625,"STNG":.45,"TNK":.25,"SB":.075,"TEN":.375}[ticker])
            blocks.append("continuation of board-set dividend is a forecast, not a contractual payment")
        elif ticker=="DHT": policy.update(ratio=1,base_dps=0)
        elif ticker=="ASC": policy.update(ratio=2/3,base_dps=0)
        elif ticker=="SBLK": policy.update(basis="free_cash",ratio=1,base_dps=.05,minimum_cash_deficit=True)
        elif ticker=="GNK": policy.update(basis="operating_cash",ratio=1,base_dps=0)
        elif ticker=="TRMD": policy.update(basis="liquidity",ratio=1,base_dps=0)
        elif ticker=="INSW": policy.update(basis="earnings",ratio=.85,base_dps=.12,additive_base=False)
        elif ticker=="CAPT": policy.update(basis="free_cash",ratio=.35,base_dps=0)
        elif ticker=="2343": policy.update(basis="net_cash_earnings",net_cash_ratio=1,net_debt_ratio=.5,payment_quarters=[2,4])
        elif ticker in ("HAFN","BWLP"):
            policy.update(basis="leverage_earnings",tiers=[[.2,.9],[.3,.8],[.4,.6],[1e6,.5]] if ticker=="HAFN" else [[.2,1],[.3,.75],[1e6,.5]],inclusive_tiers=True)
            blocks.append("issuer net leverage/NLTV differs from independent NAV fleet proxy; reconcile before adoption")
        if ticker=="TEN": policy.update(payment_quarters=[2,4],base_period_multiplier=2)
        if hybrid: blocks.append("joint sector scenario mapping required for one issuer-level cash policy; no marginal-sleeve payout summation")
        if ticker in ("FRO","ECO","NAT","LPG","CMBT"):
            blocks.append("payout percentage is a discretionary forecast, not a binding formula")
        opening=dict(cash=bs.cash_and_equivalents,debt=bs.total_debt,leases=bs.lease_liabilities,
                     working_capital=bs.working_capital_net,commitments=bs.newbuild_capex_commitments,
                     advances=bs.newbuild_advances_paid,held_for_sale=bs.held_for_sale,fleet_value=nav.fleet_value)
        coupons={"SB":.08,"GSL":.0875}
        pref=coupons.get(ticker,0)*bs.preferred_equity
        if bs.preferred_equity and ticker not in coupons:
            blocks.append("preferred/NCI allocation and distributions require separate reconciliation")
        # Dated reported run rates; all other names carry an explicit proxy range.
        da={"DHT":27752000,"SBLK":79361000/2,"SB":28900000/2,"GNK":21000000}.get(ticker)
        da_basis="reported quarterly/H1 run-rate; GNK Q1; fleet changes still need a roll-forward"
        if da is None:
            da=sum(max(0,ci.market_data.vessel_value_curves[v.cls].newbuild-ci.market_data.vessel_value_curves[v.cls].scrap_25yr)*v.count/25/4 for v in ci.fleet.vessels if v.years_to_delivery<=0)
            da_basis="replacement-mark straight-line 25yr proxy; NOT reported book-cost depreciation"
            blocks.append("book-cost depreciation/amortization schedule not extracted; replacement-mark proxy is diagnostic only")
        debt=bs.total_debt+bs.lease_liabilities
        funding={"SB":.051,"HAFN":.048,"CAPT":.032}.get(ticker,ci.cost_structure.annual_interest_expense/debt if debt>0 else 0)
        risk={}
        for point,ra in config["risk_calibration"]["asset_rate_grid"].items():
            p_cost=pref if ticker in coupons else bs.preferred_equity*ra
            risk[point]=(ra*(nav.nav_total+debt+bs.preferred_equity-bs.cash_and_equivalents)+.0475*bs.cash_and_equivalents-funding*debt-p_cost)/nav.nav_total if nav.nav_total>0 else None
        sec=w.get("sector","crude")
        sectors = list(MULTI_SLEEVE_TICKERS[ticker]) if ticker in MULTI_SLEEVE_TICKERS else (["crude","product","lng"] if ticker in THREE_SLEEVE_TICKERS else ["crude","product"] if ticker in HYBRID_TICKERS else [sec])
        horizon=max(int(load_scenarios(sector=s).get("strip_horizon",8)) for s in sectors)
        periods=calendar.keys(ci.timeline["projection_start_quarter"],horizon)
        due={}
        nbs=[v for v in ci.fleet.vessels if v.years_to_delivery>0]
        nb_total=sum(v.count for v in nbs)
        if nbs:
            for v in nbs:
                index=max(0,math.ceil(v.years_to_delivery*4)-1-ci.timeline.get("elapsed_quarters",0))
                due[index]=due.get(index,0)+bs.newbuild_capex_commitments*v.count/nb_total
            blocks.append("remaining committed capex allocated by hull count at delivery; installment and financing dates unresolved")
        elif bs.newbuild_capex_commitments:
            blocks.append("commitments have no mapped delivery schedule; remain outstanding, not assumed paid")
        schedules,policies={},{}
        for point,mult in (("low",.5),("base",1),("high",1.5)):
            policies[point]=copy.deepcopy(policy)
            if ticker in ("FRO","ECO","NAT","LPG","CMBT"):
                policies[point]["ratio"]={"low":0,"base":policy["ratio"],"high":1}[point]
            if ticker=="CAPT": policies[point]["ratio"]={"low":.3,"base":.35,"high":.4}[point]
            schedules[point]={}
            debt_left=debt
            for i,period in enumerate(periods):
                repay=min(debt_left, {"FLNG":27000000,"INSW":14000000}.get(ticker, debt*{"low":0,"base":.0125,"high":.025}[point]))
                # Lease principal stays separate; these initial schedules repay carried debt only.
                repay=min(repay,bs.total_debt-sum(v["debt_repayment"] for v in schedules[point].values()))
                debt_left-=repay
                minimum=2.1e6*sum(v.count for v in ci.fleet.vessels if v.years_to_delivery<=i/4) if ticker=="SBLK" else 0
                row=dict(depreciation=da*mult,noncash_addback=0,delta_working_capital=0,
                         maintenance_capex=nav.fleet_value*{"low":0,"base":.0025,"high":.005}[point],
                         newbuild_payment=due.get(i,0),debt_draw=0,debt_repayment=repay,lease_repayment=0,
                         preferred_distribution=pref/4,sale_proceeds=0,sale_carrying_release=0,
                         advances_release=0,reserve=19.5e6*mult if ticker=="GNK" else 0,
                         minimum_cash=minimum,equity_issuance=0,buybacks=0)
                if ticker=="TRMD": row["reserve"]={"low":1e6,"base":2e6,"high":3e6}[point]*sum(v.count for v in ci.fleet.vessels)
                if ticker=="SB":
                    annual={2026:61.4e6,2027:81.5e6,2028:42.8e6,2029:91.5e6}
                    row["newbuild_payment"]=annual[int(period[:4])]/(2 if period.startswith("2026") else 4)
                    row["debt_repayment"]=113.7e6 if period=="2027-Q1" else 0
                schedules[point][period]=row
        company=dict(sector=sec,sectors=sectors,hybrid=hybrid,horizon=horizon,opening=opening,policy=policies,schedules=schedules,
                     source=dict(url=source[0],date=source[1],retrieved_at="2026-09-22",finding=source[2]),
                     depreciation_basis=da_basis,quarterly_depreciation=da,risk=risk,funding_cost=funding,
                     risk_blockers=["transportation beta proxy requires shipping-sector calibration", "funding-cost and cash-risk conventions require owner review"],
                     blockers=blocks,clean_nav=nav.nav_total,sector_asset_weights=sleeve_values_by_sector(ci))
        config["companies"][ticker]=company
        for sector in sectors:
            sleeve=sector_carve_out(ci,sector).sleeve_inputs if hybrid else ci
            classes=sorted({v.cls for v in sleeve.fleet.vessels})
            n=int(load_scenarios(sector=sector).get("strip_horizon",8))
            curves={c:sleeve.market_data.ffa_forward_curve[c][:n] for c in classes}
            if any(len(v)!=n for v in curves.values()): raise ValueError("incomplete reference curve")
            ref=dict(periods=calendar.keys(ci.timeline["projection_start_quarter"],n),
                     marks_hash=hashlib.sha256(json.dumps({c:asdict(sleeve.market_data.vessel_value_curves[c]) for c in classes},sort_keys=True).encode()).hexdigest(),
                     basis="proposed frozen current-mark/current-curve pair; NOT demonstrated historical strike-vintage pairing",
                     blockers=["historical vessel-mark/reference pairing not established; +/-10% reference-level sensitivity only"],
                     source_commit=json.loads((OUT/"frozen/manifest.json").read_text())["production_commit"],
                     source_dates=yaml.safe_load((ROOT/"inputs/market_data/ffa_forward_curve.yaml").read_text())["as_of"])
            for point,mult in (("low",.9),("base",1),("high",1.1)): ref[point]={c:[x*mult for x in vs] for c,vs in curves.items()}
            ref["reference_id"]=hashlib.sha256(json.dumps(ref,sort_keys=True,default=str).encode()).hexdigest()
            config["references"][ticker+":"+sector]=ref
    (OUT/"assumptions.json").write_text(json.dumps(config,indent=2,sort_keys=True,default=str)+"\n")


if __name__=="__main__": main()
