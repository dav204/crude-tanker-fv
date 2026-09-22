from datetime import date
from dataclasses import replace
import copy
import json
from pathlib import Path

import pytest
import yaml

from crude_tanker_fv import calendar as cal, ffa_promote as fp
from crude_tanker_fv.loaders import INPUTS_DIR, load_company_inputs
from crude_tanker_fv.pipeline import _load_all_sectors, _maybe_apply_transactions, _run_scenarios_for_ticker
from crude_tanker_fv.loaders import load_watchlist
from crude_tanker_fv.nav import compute_nav


@pytest.mark.parametrize('stamp,panel,start,front,proxy',[
 ('2026-09-21',{'sep':10000,'oct':99999,'q4':12000,'q1':11000,'cal27':10000},'2026-Q3',10000,11500),
 ('2026-10-05',{'oct':99999,'nov':99999,'q4':12000,'q1':11000,'cal27':10000},'2026-Q4',12000,11500),
 ('2026-11-05',{'nov':10000,'dec':12000,'q1':11000,'q2':10000,'cal27':10000},'2026-Q4',11000,10500),
 ('2026-12-05',{'dec':10000,'jan':99999,'q1':11000,'q2':10000,'cal27':10000},'2026-Q4',10000,10500),
 ('2026-12-28',{'dec':10000,'jan':99999,'q1':11000,'q2':10000,'cal28':10000},'2026-Q4',10000,10500),
 ('2027-01-05',{'jan':99999,'feb':99999,'q1':12000,'q2':11000,'cal28':10000},'2027-Q1',12000,11500),
])
def test_dated_panels(stamp,panel,start,front,proxy):
    result=cal.construct_panel(stamp,panel,(-500,-500))
    assert result['periods'][0]==start and result['values'][0]==front and result['proxy']==proxy
    mapped={n['period']:n for n in result['nodes']}
    for quote in result['quotes']:
        if quote['kind']=='quarter' and quote['period'] in mapped:
            assert mapped[quote['period']]['rate']==quote['rate']
            assert mapped[quote['period']]['kind']=='quoted'
        if quote['kind']=='year':
            periods=cal.keys(quote['period']+'-Q1',4)
            if all(p in mapped for p in periods): assert sum(mapped[p]['rate'] for p in periods)==4*quote['rate']
    assert all(n['kind'] in ('derived','quoted') and n['source_date']==stamp for n in result['nodes'])


@pytest.mark.parametrize('panel',[
 {'oct':1,'nov':2,'q1':3,'q2':4,'cal27':5},
 {'sep':1,'oct':2,'q4':3,'q4-26':4,'q1':5,'cal27':6},
 {'sep':1,'q4':2,'q1':3,'cal27':4},
 {'sep':1,'oct':2,'q4':3,'q2':4,'cal27':5},
 {'sep':1,'oct':2,'q4':3,'q1':999,'cal27':5},
 {'sep':1,'oct':2,'q4':float('nan'),'q1':4,'cal27':5},
])
def test_bad_panels_freeze(panel):
    with pytest.raises(ValueError): cal.construct_panel('2026-09-21',panel,(-500,-500))


def test_ambiguous_years_and_rollover():
    assert cal.normalize('Jan-27',date(2026,12,1))==('month','2027-01')
    assert cal.normalize('Q1',date(2026,12,1))==('quarter','2027-Q1')
    with pytest.raises(ValueError): cal.normalize('Feb',date(2026,3,1))


def test_september_replay_committed_nodes():
    db=json.loads((INPUTS_DIR.parent/'state/ffa_ocr_curves.json').read_text())
    built=fp.construct('2026-09-21',db['2026-09-21'])
    raw=yaml.safe_load((INPUTS_DIR/'market_data/ffa_forward_curve.yaml').read_text())
    for cls,curve in built['curves'].items(): assert raw['ffa_forward_curve'][cls]==curve


def test_alignment_all_sectors_and_hybrids():
    watch=load_watchlist(INPUTS_DIR);docs=_load_all_sectors(INPUTS_DIR)
    for ticker,entry in watch.items():
        original=load_company_inputs(ticker,'2026-Q2',calendar_enabled=False)
        shifted=cal.align(original,INPUTS_DIR,'2026-10-01',True)
        assert compute_nav(original)==compute_nav(shifted)
        assert shifted.timeline['projection_start_quarter']=='2026-Q4'
        for cls,values in original.fleet.coverage_schedule.items(): assert shifted.fleet.coverage_schedule[cls][0]==values[1]
        for cls,values in original.fleet.fleet_schedule.items(): assert shifted.fleet.fleet_schedule[cls][0]==values[1]
        shifted,_=_maybe_apply_transactions(shifted,INPUTS_DIR,True)
        result,_,_=_run_scenarios_for_ticker(ticker,shifted,entry['current_price'],entry['analyst_target'],docs,watch)
        assert result.probability_weighted_fv>0
        assert shifted.timeline['scenario_extensions']
        assert all(n['kind']=='derived' for n in shifted.timeline['scenario_extensions'])


def test_missing_scenario_period_blocks():
    doc={'scenarios':{'one':{'a':{'q3_2026':[1,1,1],'q1_2027':[2,2,2]}}}}
    with pytest.raises(ValueError,match='internal scenario'): cal.align_scenarios(doc,{'projection_start_quarter':'2026-Q4','scenario_extensions':[]},{'a'})
