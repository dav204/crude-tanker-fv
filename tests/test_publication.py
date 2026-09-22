import json
import subprocess
from datetime import datetime, timezone
from types import SimpleNamespace
import pytest
from crude_tanker_fv import publication, promote, loaders


def fixture(tmp_path, monkeypatch):
    root=tmp_path
    (root/'outputs').mkdir()
    subprocess.run(['git','init','-q'],cwd=root,check=True)
    subprocess.run(['git','config','user.name','Test'],cwd=root,check=True)
    subprocess.run(['git','config','user.email','test@localhost'],cwd=root,check=True)
    (root/'.gitignore').write_text('state/\n')
    subprocess.run(['git','add','.'],cwd=root,check=True)
    subprocess.run(['git','commit','-qm','source'],cwd=root,check=True)
    source=publication.git(root,'rev-parse','HEAD')
    doc={'schema_version':'2.9','source_commit':source,'generated_at':'2026-09-22T15:00:00+00:00','names':[{'ticker':'SB','void':False,'ev_pct':0,'position':'HOLD','cycles':[{'ratio':1.6,'label':'late-cycle/peak','anchor_basis':'tc'}]}]}
    (root/'outputs/book_scorecard.json').write_text(json.dumps(doc))
    subprocess.run(['git','add','.'],cwd=root,check=True)
    subprocess.run(['git','commit','-qm','output'],cwd=root,check=True)
    monkeypatch.setattr(promote,'evaluate_land',lambda *a:(SimpleNamespace(freeze_reasons=[]),''))
    monkeypatch.setattr(loaders,'load_watchlist',lambda *a:{'SB':{}})
    return root


def test_publication_is_immutable_and_held_run_keeps_previous(tmp_path,monkeypatch):
    root=fixture(tmp_path,monkeypatch); now=datetime(2026,9,22,18,tzinfo=timezone.utc)
    first=publication.publish(root,now)
    assert len(first['source_commit'])==40 and first['validation']=='accepted'
    assert publication.publish(root,now)==first
    pointer=(root/'state/publications/current.json').read_bytes()
    (root/'outputs/book_scorecard.json').write_text('{}')
    with pytest.raises(ValueError): publication.publish(root,now)
    assert (root/'state/publications/current.json').read_bytes()==pointer
    assert json.loads((root/'state/publications/status.json').read_text())['status']=='held'
