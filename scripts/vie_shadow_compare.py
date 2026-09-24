"""Reproduce broker-availability ablation in disposable clones, without transports."""
import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('nav_per_share', 'fv', 'blend_fv', 'fv_low', 'fv_high', 'position',
          'cycles', 'sleeves', 'weight_sign_stable', 'read_flag', 'ev_pct_family_min', 'ev_pct_family_max')


def run():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--governor', type=Path, required=True)
    args = ap.parse_args()
    frozen = json.loads((ROOT/'research/vie-exit/frozen_baseline.json').read_text())
    base = json.loads(subprocess.check_output(['git','show',frozen['production_commit']+':outputs/book_scorecard.json'],cwd=ROOT))
    result = {'version':1,'production_baseline':frozen,'runs':{},'limitations':[
        'No licensed replacement FFA observations; FFA full-book experiment blocked.',
        'Broker absence exposes legacy k_broker=1.0 snapshot fallback; research marks broker checks unavailable. Production removal not authorised.'
    ]}
    spec=importlib.util.spec_from_file_location('shadow_seam',args.governor/'monitor/seam.py')
    seam=importlib.util.module_from_spec(spec); spec.loader.exec_module(seam)
    registry=json.loads((args.governor/'monitor/seam_registry.json').read_text())
    workspace=Path(tempfile.mkdtemp(prefix='vie-book-',dir='/private/tmp'))
    for mode in ['available','unavailable']:
        target=workspace/mode
        subprocess.run(['git','clone','--shared','--quiet',str(ROOT),str(target)],check=True)
        (target/'.venv').symlink_to((ROOT/'.venv').resolve(),target_is_directory=True)
        with (target/'.git/info/exclude').open('a') as exclude:
            exclude.write('\n.venv\n')
        (target/'state').mkdir(exist_ok=True)
        (target/'state/last_run.json').write_text(json.dumps({'quarter':base['quarter'],'tickers':{},
            'run_at':base['generated_at'],'input_file_hashes':{}}))
        # Research bookkeeping and engine code do not replace the frozen economic inputs.
        subprocess.run(['git','checkout',frozen['production_commit'],'--','inputs','outputs','baselines','decisions'],cwd=target,check=True)
        if mode=='unavailable':
            p=target/'inputs/watchlist.yaml'; data=yaml.safe_load(p.read_text())
            for row in data.values():
                if isinstance(row,dict): row['consensus_pnav']=None
            p.write_text(yaml.safe_dump(data,sort_keys=False))
            (target/'outputs/broker_nav_sweep.md').unlink(missing_ok=True)
        subprocess.run(['git','add','inputs','outputs','baselines','decisions'],cwd=target,check=True)
        subprocess.run(['git','commit','--allow-empty','-qm','research: frozen broker availability '+mode],cwd=target,check=True)
        env=dict(os.environ,PYTHONPATH=str(target/'src'))
        log=workspace/(mode+'.log')
        with log.open('w') as out:
            for name in ['crude_weight_robustness','dry_bulk_weight_comparison','lng_weight_comparison','lpg_weight_comparison','product_weight_comparison']:
                subprocess.run([str(target/'.venv/bin/python'),'scripts/'+name+'.py'],cwd=target,env=env,stdout=out,stderr=out,check=True)
            subprocess.run([str(target/'.venv/bin/python'),'-m','crude_tanker_fv.pipeline',base['quarter'],
                            '--valuation-date',base['valuation_date']],cwd=target,env=env,stdout=out,stderr=out,check=True)
        card=json.loads((target/'outputs/book_scorecard.json').read_text())
        subprocess.run(['git','add','outputs','decisions'],cwd=target,check=True)
        subprocess.run(['git','commit','-qm','research: shadow outputs'],cwd=target,check=True)
        code='''import json
from crude_tanker_fv.publication import validate, ROOT
try:
 validate(ROOT)
 print(json.dumps({'status':'passed'}))
except (ValueError, KeyError) as e:
 print(json.dumps({'status':'held','reason':str(e)}))
'''
        validation=subprocess.check_output([str(target/'.venv/bin/python'),'-c',code],cwd=target,env=env,text=True)
        diagnostics={r['ticker']:{'broker_nav':r['broker_nav'],'broker_reference':r['broker_reference'],
                    'sanity':r['sanity'],'research_broker_check':'UNAVAILABLE' if r['broker_nav'] is None else 'archived_vintage_only'} for r in card['names']}
        result['runs'][mode]={'workspace':str(target),'log':str(log),'publication_validator':json.loads(validation.splitlines()[-1]),
                             'governor':seam.evaluate(card,registry),'diagnostics':diagnostics,
                             'scorecard':card}
    before={r['ticker']:r for r in result['runs']['available']['scorecard']['names']}
    after={r['ticker']:r for r in result['runs']['unavailable']['scorecard']['names']}
    old={r['ticker']:r for r in base['names']}
    if before.keys()!=after.keys() or before.keys()!=old.keys(): raise ValueError('full-book coverage changed')
    result['comparison']=[dict(ticker=t, before={k:before[t].get(k) for k in FIELDS},
                               after={k:after[t].get(k) for k in FIELDS},
                               changed=[k for k in FIELDS if before[t].get(k)!=after[t].get(k)],
                               baseline_changed=[k for k in FIELDS if old[t].get(k)!=before[t].get(k)]) for t in sorted(before)]
    output=ROOT/'research/vie-exit/broker_ablation.json'
    output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'output':str(output),'names':len(before),
                      'economic_changes':[r['ticker'] for r in result['comparison'] if r['changed']],
                      'baseline_changes':[r['ticker'] for r in result['comparison'] if r['baseline_changed']]}))


if __name__=='__main__':
    run()
