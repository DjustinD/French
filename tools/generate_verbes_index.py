import json
from pathlib import Path

VERB_DIR = Path('verbes')
verbs = []

for p in sorted(VERB_DIR.glob('*.json')):
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        infinitive = data.get('infinitive', p.stem)
        english = data.get('english', '')
        irregular = data.get('irregular', False)
        cefr = data.get('cefr', 'A1')
        
        verbs.append({
            'infinitive': infinitive,
            'english': english,
            'irregular': irregular,
            'cefr': cefr,
            'file': p.name
        })
    except Exception as e:
        print(f'ERROR reading {p}: {e}')

# Sort by CEFR then infinitive
cefr_order = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 4, 'C1': 5, 'C2': 6}
verbs.sort(key=lambda v: (cefr_order.get(v['cefr'], 99), v['infinitive']))

# Add order numbers
for i, v in enumerate(verbs, 1):
    v['order'] = i

output = {'verbs': verbs}
Path('verbes_français.json').write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Generated verbes_français.json with {len(verbs)} verbs')
print(f'CEFR distribution:')
from collections import Counter
cefr_count = Counter(v['cefr'] for v in verbs)
for level in sorted(cefr_count.keys(), key=lambda x: cefr_order.get(x, 99)):
    print(f'  {level}: {cefr_count[level]} verbs')
