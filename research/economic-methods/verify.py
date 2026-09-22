"""Read-only economic identities and shadow publication rejection evidence."""
import hashlib
import json
import math
import subprocess
import tempfile
from dataclasses import asdict
from pathlib import Path

from crude_tanker_fv import publication, drift_gate
from crude_tanker_fv.scorecard import handoff_coherence_flags
from crude_tanker_fv.scenarios import position_recommendation

STUDY=Path(__file__).resolve().parent
ROOT=STUDY.parents[1]
OUT=STUDY/'results'
METHODS=('legacy','cash','reference','risk','smooth','cash_reference','cash_reference_risk','combined','reference_risk_smooth')


def main():
    results={m:json.loads((OUT/(m+'.json')).read_text()) for m in METHODS}
    base=results['legacy']; cfg=json.loads((STUDY/'assumptions.json').read_text())
    checks={'full_book_names':len(base),'nav_invariance':True,'scenario_probabilities_unchanged':True,
            'cash_identity_rows':0,'handoff_coherence':{},'production_writes':False,'transports':'disabled'}
    funding={}; drifts={}
    frozen_rows={r['ticker']:r for r in json.loads((STUDY/'frozen/book_scorecard.json').read_text())['names']}
    prior=drift_gate.load_baseline(ROOT/'baselines/reconcile_baseline.yaml')
    generated=json.loads((OUT/'legacy_run_snapshot.json').read_text())['tickers']
    for method,rows in results.items():
        assert set(rows)==set(base)
        state={'tickers':{}}
        funding[method]={}
        for ticker,row in rows.items():
            if row['fv'] is None:continue
            assert row['nav']==base[ticker]['nav'], (method,ticker,'NAV changed')
            h=row['handoff']
            state['tickers'][ticker]=dict(h,k_broker=generated[ticker]['k_broker'],current_price=row['price'],
                position=position_recommendation(row['fv']/row['price']-1))
            assert row['price']==base[ticker]['price']
            all_ledgers=[]
            for sector,sleeve in row['sleeves'].items():
                original=base[ticker]['sleeves'][sector]['scenarios']['scenarios']
                scenarios=sleeve['scenarios']['scenarios']
                assert [(s['name'],s['weight']) for s in scenarios]==[(s['name'],s['weight']) for s in original]
                all_ledgers.append(('current:'+sector,sleeve['strip']['cash_bridge']))
                for scenario in scenarios:
                    detail=scenario.get('economic_research')
                    if detail:all_ledgers.append((sector+':'+scenario['name'],detail['strip']['cash_bridge']))
                if method=='reference':
                    assert math.isclose(row['fv'],base[ticker]['fv'],abs_tol=1e-8)
            for label,ledger in all_ledgers:
                for r in ledger:
                    expected=(r['opening_cash']+r['operating_cash_flow']-r['maintenance_capex']-r['newbuild_payment']+
                              r['sale_proceeds']+r['debt_draw']-r['debt_repayment']-r['lease_repayment']-
                              r['preferred_distribution']+r['equity_issuance']-r['buybacks']-r['common_distribution'])
                    assert math.isclose(expected,r['closing_cash'],abs_tol=1e-5), (method,ticker,label,r['period'])
                    assert math.isclose(r['operating_cash_flow'],r['accounting_income']+r['depreciation']+
                                        r['noncash_addback']-r['delta_working_capital'],abs_tol=1e-5)
                    checks['cash_identity_rows']+=1
                    if r['funding_gap'] or r['distribution_shortfall']:
                        funding[method].setdefault(ticker,[]).append(dict(case=label,period=r['period'],
                            funding_gap=r['funding_gap'],distribution_shortfall=r['distribution_shortfall']))
        doc=json.loads((OUT/(method+'_handoff.json')).read_text())
        flags=handoff_coherence_flags(doc)
        checks['handoff_coherence'][method]=flags
        assert not flags,(method,flags)
        # Empty evidence directory prevents unrelated historic annotations blessing a method move.
        with tempfile.TemporaryDirectory() as d:
            drifts[method]=[asdict(r) for r in drift_gate.evaluate(prior,state,decisions_dir=Path(d))]
        if method=='legacy':
            assert all(r['status']=='stable' for r in drifts[method]), 'legacy drift differs from committed baseline'
    checks['broker_second_difference']='unchanged versus reproduced legacy; broker multiplier comes from isolated production-path regeneration'
    checks['drift_annotations']='research attribution only; production baselines never ratified'
    with tempfile.TemporaryDirectory() as d:
        root=Path(d);(root/'outputs').mkdir()
        (root/'outputs/book_scorecard.json').write_bytes((OUT/'combined_handoff.json').read_bytes())
        for args in (['init','-q'],['add','outputs/book_scorecard.json'],
                     ['-c','user.name=Research Test','-c','user.email=research@localhost','commit','-qm','shadow fixture']):
            subprocess.run(['git',*args],cwd=root,check=True,capture_output=True)
        try:publication.validate(root)
        except ValueError as exc:
            assert 'not an accepted production publication' in str(exc)
            checks['real_committed_shadow_publication_validation']={'status':'HELD','reason':str(exc)}
        else:raise AssertionError('research publication accepted')
    manifest=json.loads((STUDY/'frozen/manifest.json').read_text())
    for rel,digest in manifest['files'].items():
        if rel.startswith(('inputs/','baselines/')):
            assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,rel
    checks['frozen_inputs_and_baselines_unchanged']=True
    (OUT/'identity_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    (OUT/'funding_exceptions.json').write_text(json.dumps(funding,indent=2)+'\n')
    (OUT/'drift_checks.json').write_text(json.dumps(drifts,indent=2)+'\n')
    print(json.dumps(checks,indent=2))


if __name__=='__main__':main()
