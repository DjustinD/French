import json
from pathlib import Path
p = Path('verbes')
errors = []
for f in sorted(p.glob('*.json')):
    try:
        with open(f, encoding='utf-8') as fh:
            json.load(fh)
    except Exception as e:
        errors.append((str(f), str(e)))
print('checked', len(list(p.glob('*.json'))), 'files')
if errors:
    print('errors:')
    for e in errors:
        print(e)
else:
    print('no syntax errors')
