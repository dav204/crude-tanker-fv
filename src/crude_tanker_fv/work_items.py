"""Operational task projections from domain authorities, never financial decisions."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

from .runtime import atomic_json, commit_paths, locked

ROOT=Path(__file__).resolve().parents[2]
STATUSES={'ready','running','blocked','waiting','done','unknown'}
REQUIRED={'id','project','status','next_action','resolver','due','waiting_condition','blocking_decision_ids','evidence'}


def item(identity, project, status, action, resolver='agent', evidence=None, due=None, waiting=None, blockers=None, **extra):
    return dict(id=identity,project=project,status=status,next_action=action,resolver=resolver,
                due=due,waiting_condition=waiting,blocking_decision_ids=blockers or [],evidence=evidence or [],**extra)


def validate(doc):
    if not isinstance(doc,dict) or doc.get('version')!=1 or not isinstance(doc.get('items'),list):
        raise ValueError('missing or malformed versioned work-item registry')
    seen=set()
    for row in doc['items']:
        if not REQUIRED<=set(row) or row['status'] not in STATUSES or row['id'] in seen:
            raise ValueError('invalid or duplicate work item: '+str(row.get('id')))
        if row['resolver'] not in ('owner','agent','external') or not row['next_action']:
            raise ValueError('invalid resolver/action: '+row['id'])
        if not row['due'] and not row['waiting_condition'] and row['status']!='done':
            raise ValueError('work item needs due date or waiting condition: '+row['id'])
        if row['due']: date.fromisoformat(str(row['due']))
        if not isinstance(row['evidence'],list) or not isinstance(row['blocking_decision_ids'],list):
            raise ValueError('invalid evidence/blockers: '+row['id'])
        seen.add(row['id'])
    return doc


def reference(root, ref):
    project,path=ref.get('project','producer'),ref['path']
    base=root if project=='producer' else root.parent/'portfolio-governance'
    rel=Path(path)
    if project not in ('producer','governor') or rel.is_absolute() or '..' in rel.parts:
        raise ValueError('invalid evidence path')
    if ref.get('runtime'):
        raw=(base/rel).read_bytes()
    else:
        raw=subprocess.check_output(['git','show','HEAD:'+path],cwd=base,stderr=subprocess.DEVNULL)
    if ref.get('sha256') and hashlib.sha256(raw).hexdigest()!=ref['sha256']:
        raise ValueError('conflicting committed evidence: '+path)
    if ref.get('contains') and ref['contains'] not in raw.decode():
        raise ValueError('evidence does not support completion: '+path)
    return raw


def evidence(root,path,project='producer',contains=None):
    ref={'project':project,'path':path}
    if contains: ref['contains']=contains
    raw=reference(root,ref);ref['sha256']=hashlib.sha256(raw).hexdigest()
    return ref


def repair(identity,reason):
    return item('repair:'+identity,'producer','ready','Repair workflow evidence: '+reason,
                waiting='until valid evidence is recorded',details=reason,authority='repair')


def project(root=ROOT, today=None):
    today=today or date.today();issues=[]
    try:
        doc=validate(yaml.safe_load((root/'work_items.yaml').read_text()))
    except (OSError,ValueError,yaml.YAMLError) as exc:
        reason=str(exc)
        return {'version':1,'integration_enabled':True,'complete':False,'items':[
            item('registry:unknown','producer','unknown',reason,waiting='repair registry'),repair('registry',reason)]}
    rows={r['id']:dict(r) for r in doc['items'] if r.get('authority','manual')=='manual'}
    for row in list(rows.values()):
        try:
            if not row['evidence']:
                raise ValueError('missing cited evidence')
            for ref in row['evidence']: reference(root,ref)
            if row['status']!='done' and (today-date.fromisoformat(row.get('verified_at','1900-01-01'))).days>30:
                raise ValueError('status evidence older than 30 days')
        except (OSError,ValueError,subprocess.CalledProcessError) as exc:
            row['status']='unknown';row['evidence_error']=str(exc)
            rows['repair:'+row['id']]=repair(row['id'],str(exc))
    def add(row):
        row['authority']=row.get('authority','adapter');rows[row['id']]=row
    def failed(identity,exc):
        add(item(identity,'producer','unknown','Inspect unavailable authority: '+str(exc),waiting='authority repaired'))
        add(repair(identity,str(exc)))
    try:
        from .filings import queue, manifest
        q=queue(manifest(root),root/'state/filings_triaged.json')
        add(item('filings:pending','producer','ready' if q['pending_total'] else 'done',
                 'Drain all pending accessions; commit dispositions before acknowledging',
                 evidence=[{'project':'producer','path':'state/edgar_manifest.jsonl','runtime':True}],
                 waiting='all accessions dispositioned',pending_total=q['pending_total'],oldest_arrival=q['oldest_arrival'],invalid=q['invalid']))
        if q['invalid']: failed('filings:invalid',str(q['invalid']))
    except (OSError,ValueError,KeyError) as exc: failed('filings:pending',exc)
    for filename in ('forks.yaml','reweight_triggers.yaml'):
        try:
            data=yaml.safe_load(reference(root,{'path':'inputs/'+filename}))
            cards=data['forks'] if filename=='forks.yaml' else [dict(v,id=k) for k,v in data.items()]
            for card in cards:
                identity=('fork:' if filename=='forks.yaml' else 'trigger:')+card['id']
                status=card['status'];due=str(card.get('execute_after') or card.get('due') or '') or None
                done=status in ('executed','done','retired','closed')
                resolver='owner' if card.get('needs_code') and not done else 'agent'
                resolved='done' if done else ('blocked' if resolver=='owner' else ('ready' if due and due<=today.isoformat() else 'waiting'))
                add(item(identity,'producer',resolved,card.get('action') or card.get('recommendation') or 'Review trigger',resolver,
                         evidence=[{'project':'producer','path':'inputs/'+filename}],due=due,waiting='registered condition or ruling',
                         blockers=[identity] if resolver=='owner' else []))
        except (OSError,ValueError,KeyError,TypeError,subprocess.CalledProcessError) as exc: failed(filename,exc)
    try:
        gov=root.parent/'portfolio-governance'
        seam=json.loads((gov/'monitor/state/seam_latest.json').read_text())
        for event in seam['events']:
            if event.get('severity') not in ('page','blocked','unknown') and event['code'] not in ('GATES_PENDING','WIDE_CAP'): continue
            identity='governor:'+str(event.get('ticker','book'))+':'+event['code']
            add(item(identity,'governor','blocked',(event.get('detail') or event['code'])+'; '+(event.get('action') or 'Preserve binding restriction'),'owner',
                evidence=[{'project':'governor','path':'monitor/state/seam_latest.json','runtime':True}],
                waiting='explicit valuation mini-review or gate disposition',blockers=[identity],details=event))
    except (OSError,ValueError,KeyError) as exc: failed('governor:consumption',exc)
    # A structured shadow sidecar is required even when the narrative looks reassuring.
    latest={}
    for path in sorted((root/'decisions').glob('*_shadow_build_*.md')):
        latest[path.name.split('_shadow_build_')[0]]=path
    for ticker,path in latest.items():
        if rows.get('roadmap:ten-q2',{}).get('status')=='done' and ticker=='ten': continue
        try:
            side=path.with_suffix('.json');shadow=json.loads(reference(root,{'path':str(side.relative_to(root))}))
            if shadow.get('version')!=1 or not isinstance(shadow.get('blockers'),list): raise ValueError('invalid shadow blocker contract')
            reference(root,shadow['report_evidence'])
            for n,block in enumerate(shadow['blockers']):
                if block['resolver'] not in ('owner','agent','external') or not block['next_action']: raise ValueError('invalid shadow resolver')
                add(item('shadow:'+ticker+':'+str(block['id']),'producer','blocked',block['next_action'],block['resolver'],
                         evidence=[{'project':'producer','path':str(side.relative_to(root))}],waiting=block['condition'],
                         blockers=block.get('blocking_decision_ids',[])))
        except (OSError,ValueError,KeyError,subprocess.CalledProcessError) as exc: failed('shadow:'+ticker,exc)
    doc['items']=sorted(rows.values(),key=lambda r:r['id']);doc['complete']=not any(r['status']=='unknown' for r in rows.values())
    return validate(doc)


def queues(doc):
    def line(r):
        return f"{r['id']} [{r['status']}; resolver {r['resolver']}] — {r['next_action']}" + (f"; blockers: {', '.join(r['blocking_decision_ids'])}" if r['blocking_decision_ids'] else '')
    active=[r for r in doc['items'] if r['status']!='done']
    return ([line(r) for r in active if r['resolver']=='owner'],[line(r) for r in active if r['resolver']!='owner'])


def sync(root=ROOT):
    with locked(root/'state/work_items.lock'):
        doc=project(root)
        path=root/'work_items.yaml'
        previous=yaml.safe_load(path.read_text()) if path.exists() else None
        if previous!=doc:
            atomic_json(path,doc)
            commit_paths(root,['work_items.yaml'],'chore(workflow): synchronize operational task evidence')
        return doc


def record_shadow(report,blockers,root=ROOT):
    path=Path(report)
    if path.parent!=Path('decisions') or not re.fullmatch(r'[a-z0-9]+_shadow_build_\d{4}-\d{2}-\d{2}\.md',path.name):
        raise ValueError('shadow report must be a scoped dated decisions path')
    for block in blockers:
        if not {'id','resolver','next_action','condition','blocking_decision_ids'}<=set(block) or block['resolver'] not in ('owner','agent','external'):
            raise ValueError('invalid structured blocker')
    with locked(root/'state/work_items.lock'):
        ref=evidence(root,str(path))
        side=path.with_suffix('.json')
        atomic_json(root/side,{'version':1,'report_evidence':ref,'blockers':blockers})
        commit_paths(root,[str(side)],'shadow build: record structured blockers')


def receipts(root=ROOT):
    lines=[]
    patterns=[('producer execution',root,'state/operations/runs/*.json'),
              ('publication attempt',root,'state/publications/status.json'),
              ('governor landing',root.parent/'portfolio-governance','monitor/state/runs/*.json')]
    for title,base,pattern in patterns:
        paths=sorted(base.glob(pattern))
        if not paths: lines.append(title+': UNKNOWN — missing receipts');continue
        try:
            r=json.loads(paths[-1].read_text())
            lines.append(title+': '+str(r.get('status','unknown'))+'; '+str(paths[-1].relative_to(base))+'; stages '+json.dumps({k:r[k] for k in ('stages','generation','publication','consumer_check','persistence','smtp','healthcheck','job','checks') if k in r},sort_keys=True))
        except (OSError,ValueError) as exc: lines.append(title+': UNKNOWN — '+str(exc))
    for title,base,path in [('accepted publication',root,'state/publications/current.json'),('consumption',root.parent/'portfolio-governance','monitor/state/seam_latest.json')]:
        try:
            r=json.loads((base/path).read_text());lines.append(title+': '+str(r.get('publication_id',r.get('id','UNKNOWN'))))
        except (OSError,ValueError) as exc: lines.append(title+': UNKNOWN — '+str(exc))
    for title,base in [('producer',root/'state'),('governor',root.parent/'portfolio-governance/monitor/state')]:
        from .delivery import pending
        try:
            p=pending(base);lines.append(title+' delivery: '+str(len(p))+' unresolved exact-message receipt(s); SMTP accepted is not proof of inbox delivery')
        except (OSError,ValueError) as exc: lines.append(title+' delivery: UNKNOWN — '+str(exc))
    lines.append('Automation authority: graph.yaml and recorded rulings; authority is separate from observed execution/landing evidence.')
    return lines


def record(row, root=ROOT):
    row=dict(row, authority='manual', verified_at=date.today().isoformat())
    validate({'version':1,'items':[row]})
    if not row['evidence']: raise ValueError('cited evidence required')
    for ref in row['evidence']:
        if row['status']=='done' and ref.get('runtime'):
            raise ValueError('manual completion requires committed evidence')
        reference(root,ref)
    with locked(root/'state/work_items.lock'):
        doc=validate(yaml.safe_load((root/'work_items.yaml').read_text()))
        previous=next((r for r in doc['items'] if r['id']==row['id']),None)
        if previous and previous.get('authority','manual')!='manual':
            raise ValueError('update the domain authority; adapter facts cannot be overwritten')
        doc['items']=[r for r in doc['items'] if r['id']!=row['id']]+[row]
        validate(doc);atomic_json(root/'work_items.yaml',doc)
        commit_paths(root,['work_items.yaml'],'chore(workflow): record '+row['id'])


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('command',choices=['show','sync','shadow','record'])
    ap.add_argument('--report');args=ap.parse_args(argv)
    if args.command=='record': record(json.load(sys.stdin));return 0
    if args.command=='shadow': record_shadow(args.report,json.load(sys.stdin));return 0
    print(json.dumps(sync() if args.command=='sync' else project(),indent=2,default=str))
    return 0




def refresh_worker(root=ROOT):
    """Called only by the production worker; a rollback switch retains all evidence."""
    path=root/'work_items.yaml'
    settings=validate(yaml.safe_load(path.read_text()))
    if not settings.get('integration_enabled',False): return {'status':'disabled'}
    doc=sync(root)
    active={r['id']:{k:r.get(k) for k in ('status','resolver','next_action','blocking_decision_ids')}
            for r in doc['items'] if r['status'] in ('blocked','unknown') and (r['resolver']=='owner' or r['status']=='unknown')}
    observation=root/'state/work_items_observed.json'
    previous=json.loads(observation.read_text()) if observation.exists() else {}
    changes=[k for k,v in active.items() if previous.get(k)!=v]
    recovery=[k for k in previous if k not in active and (previous[k]['status']=='unknown' or k=='quarterly:scheduler-proof')]
    if changes or recovery:
        from .delivery import enqueue
        text='Operational task changes\n\n'+'\n'.join(k+': '+json.dumps(active[k],sort_keys=True) for k in changes)
        if recovery: text+='\nRecovered workflow conditions: '+', '.join(recovery)
        key=hashlib.sha256(json.dumps({'changes':{k:active[k] for k in changes},'recoveries':recovery},sort_keys=True).encode()).hexdigest()
        enqueue('[crude-fv] Workflow status changes',text,root/'state',key='work-items:'+key)
    atomic_json(observation,active)
    return {'status':'observed','changes':changes,'recoveries':recovery}


if __name__=='__main__': raise SystemExit(main())
