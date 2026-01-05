import json
from pathlib import Path
from collections import OrderedDict

mapping = {
  'aimer':'A1','aller':'A1','apprendre':'A2','arriver':'A1','attendre':'A1','avoir':'A1',
  'boire':'A1','choisir':'A2','commencer':'A1','comprendre':'A2','connaître':'A2','courir':'A2',
  'croire':'A2','demander':'A1','dessiner':'A2','devoir':'A2','dire':'A1','donner':'A1',
  'entendre':'A1','être':'A1','écrire':'A2','fermer':'A1','faire':'A1','laisser':'A2',
  'lire':'A1','manger':'A1','mettre':'A1','offrir':'A2','ouvrir':'A1','parler':'A1',
  'partir':'A1','passer':'A1','penser':'A2','perdre':'A2','pouvoir':'A1','prendre':'A1',
  'regarder':'A1','rencontrer':'A2','rendre':'A2','rester':'A1','répondre':'A2','savoir':'A2',
  'sembler':'A2','sortir':'A1','suivre':'B1','tenir':'B1','tomber':'A1','travailler':'A2',
  'trouver':'A1','venir':'A1','vivre':'B1','voir':'A1','vouloir':'A1','écrire':'A2'
}

VERB_DIR = Path('verbes')
changed = []
for p in sorted(VERB_DIR.glob('*.json')):
    name = p.stem
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        print('SKIP (read error):', p, e)
        continue
    cefr_val = mapping.get(name, 'A1')
    # Insert/replace 'cefr' right after 'english'
    if isinstance(data, dict):
        new = OrderedDict()
        for k,v in data.items():
            if k == 'cefr':  # Skip existing cefr, we'll add it after english
                continue
            new[k]=v
            if k=='english':
                new['cefr']=cefr_val
        data = new
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        changed.append((p.name,cefr_val))

print('Updated', len(changed), 'files')
for c in changed:
    print(c[0], '->', c[1])
