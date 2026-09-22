"""Frozen-input calendar effect decomposition; does not publish or change inputs."""
import copy
import json
from dataclasses import replace
from pathlib import Path

from crude_tanker_fv import calendar
from crude_tanker_fv.loaders import INPUTS_DIR, load_company_inputs, load_watchlist
from crude_tanker_fv.pipeline import _load_all_sectors, _maybe_apply_transactions, _run_scenarios_for_ticker
from crude_tanker_fv.nav import compute_nav


def measure():
    watch=load_watchlist(INPUTS_DIR,live_prices=True);docs=_load_all_sectors(INPUTS_DIR)
    rows=[]
    from crude_tanker_fv.ffa_promote import construct
    source=json.loads((INPUTS_DIR.parent/'state/ffa_ocr_curves.json').read_text())['2026-09-21']['curves']
    october=construct('2026-10-01',{'curves':{p:{'oct':v['sep'],'nov':v['oct'],'q4':v['q4'],'q1':v['q1'],'cal27':v['cal27']} for p,v in source.items()}})
    for ticker,entry in watch.items():
        original=load_company_inputs(ticker,'2026-Q2',calendar_enabled=False)
        original,_=_maybe_apply_transactions(original,INPUTS_DIR,True)
        def value(ci,scenarios):
            r,_,_=_run_scenarios_for_ticker(ticker,ci,entry['current_price'],entry['analyst_target'],scenarios,watch)
            return {'fv':r.probability_weighted_fv,'position':r.position_recommendation,
                    'nav':compute_nav(ci).nav_per_share,'fv_low':min(s.fair_value for s in r.scenarios),
                    'fv_high':max(s.fair_value for s in r.scenarios),'sleeves':r.sleeve_fvs}
        base=value(original,docs)
        for stamp in ('2026-09-22','2026-10-01','2027-01-01'):
            aligned=calendar.align(original,INPUTS_DIR,stamp,True)
            result=value(aligned,docs)
            constructed=None
            if stamp=='2026-10-01':
                md=replace(aligned.market_data, ffa_forward_curve=dict(aligned.market_data.ffa_forward_curve,**october['curves']),
                           twelve_month_tc=dict(aligned.market_data.twelve_month_tc,**october['twelve_month']))
                constructed=value(replace(aligned,market_data=md),docs)
            elapsed=aligned.timeline['elapsed_quarters']
            # Attribution counterfactual only: retain the old terminal calendar by shortening
            # each sleeve's strip. Production always retains the ruled 8/10-quarter horizon.
            short=copy.deepcopy(docs)
            for doc in short.values(): doc['strip_horizon']=int(doc.get('strip_horizon',8))-elapsed
            without_extension=value(aligned,short) if elapsed else result
            rows.append({'ticker':ticker,'valuation_date':stamp,'price':entry['current_price'],
                         'baseline':base,'aligned':result,'construction_effect_september':0.0,
                         'timeline_to_old_terminal_delta':without_extension['fv']-base['fv'],
                         'tail_and_terminal_extension_delta':result['fv']-without_extension['fv'],
                         'total_fv_delta':result['fv']-base['fv'],'october_construction_delta':constructed['fv']-result['fv'] if constructed else None,'timeline':aligned.timeline})
    return rows


if __name__=='__main__':
    rows=measure();out=Path('outputs/calendar_comparison_2026-09-22.json');out.write_text(json.dumps(rows,indent=2)+'\n')
    lines=['# Full-book calendar comparison — 2026-09-22','',
      'Frozen committed prices and determinants. October/January are constant-source sensitivity cases, not new quotes or forecasts. September construction replay is exact. Independent NAV is held unchanged. All production sectors retain their 8/10-quarter horizons.', '',
      'Attribution: timeline-to-old-terminal uses a shorter diagnostic strip to isolate calendar advancement; tail/terminal extension is the difference when restoring the unchanged production horizon. The reference-forward average includes the labelled carried nodes in both aligned cases. This is an ordered decomposition, not a claim that effects are independent. No shorter horizon is activated.','',
      '| Date | Name | Prior FV | Calendar FV | Total Δ | Timeline Δ | Tail/terminal Δ | Position |','|---|---|--:|--:|--:|--:|--:|---|']
    for r in rows:
        lines.append('| %s | %s | %.4f | %.4f | %+.4f | %+.4f | %+.4f | %s → %s |' % (r['valuation_date'],r['ticker'],r['baseline']['fv'],r['aligned']['fv'],r['total_fv_delta'],r['timeline_to_old_terminal_delta'],r['tail_and_terminal_extension_delta'],r['baseline']['position'],r['aligned']['position']))
    lines += ['', 'October construction-only replay relabels the September source month columns to October/November while preserving quoted Q4, Q1 and Cal27 rates. These are synthetic labels, not observed October data. All 25 construction-only deltas: ' + str({r['ticker']:round(r['october_construction_delta'],8) for r in rows if r['october_construction_delta'] is not None})]
    Path('decisions/calendar_comparison_2026-09-22.md').write_text('\n'.join(lines)+'\n')
    print('comparison:',len(rows),'name/date rows; September maximum delta',max(abs(r['total_fv_delta']) for r in rows if r['valuation_date']=='2026-09-22'))
