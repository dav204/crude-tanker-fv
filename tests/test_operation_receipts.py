import json
from crude_tanker_fv import operations, notify, delivery, sentinel
from crude_tanker_fv.runtime import atomic_json


def test_failed_stage_cannot_emit_success_healthcheck_after_mail_succeeds(tmp_path, monkeypatch):
    root=tmp_path/'producer'; gov=tmp_path/'governor'
    identity=operations.start(root)
    atomic_json(root/'state/publications/status.json',{'status':'held','reason':'generation failed'})
    monkeypatch.setattr(notify,'load_env_file',lambda *a:{})
    monkeypatch.setattr(delivery,'drain',lambda *a,**k:[])
    monkeypatch.setattr(delivery,'pending',lambda *a:[])
    calls=[]
    def ping(ok,state):
        calls.append(ok);atomic_json(state/'ping_status.json',{'status':'SENT' if ok else 'FAILED'})
    monkeypatch.setattr(sentinel,'_ping',ping)
    result=operations.finish(identity,{'checks':0,'generation':1,'publication':1},root,gov)
    assert result['status']=='failed' and calls==[False]
    assert result['consumer_check']=='not_published'
    assert json.loads((root/'state/operations/runs'/(identity+'.json')).read_text())==result


def test_duplicate_unchanged_holds_reuse_the_saved_notice(tmp_path, monkeypatch):
    root=tmp_path/'producer';gov=tmp_path/'governor'
    monkeypatch.setattr(notify,'load_env_file',lambda *a:{})
    for identity in ('old','new'):
        atomic_json(root/'state/publications/status.json',{'status':'held','publication_id':identity,'at':identity,'reason':'await annotation'})
        run=operations.start(root)
        operations.finish(run,{'checks':0,'publication':1},root,gov,ping=False)
    assert len(list((root/'state/delivery').glob('*.json')))==1
