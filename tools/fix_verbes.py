import json
from pathlib import Path
import re
from collections import OrderedDict

VERB_DIR = Path('verbes')

def clean_form(form):
    if not isinstance(form, str):
        return form
    # remove parenthetical groups like (e), (s), (e)(s)
    form = re.sub(r"\([^)]*\)", "", form)
    # keep only before slash
    if '/' in form:
        form = form.split('/')[0]
    # normalize spaces
    form = re.sub(r"\s+", " ", form).strip()
    return form


def process_file(p: Path):
    text = p.read_text(encoding='utf-8')
    data = json.loads(text)
    infinitive = data.get('infinitive', p.stem)

    # ensure cefr exists; default to A1
    if 'cefr' not in data:
        # reconstruct dict to place cefr after english
        new = OrderedDict()
        for k, v in data.items():
            if k == 'english':
                new[k] = v
                new['cefr'] = 'A1'
            else:
                if k not in new:
                    new[k] = v
        data = new
    # capture simple present and future simple forms for mapping
    conjugations = data.get('conjugations', {})
    pres_simple = {}
    futur_simple = {}
    try:
        pres_simple = conjugations.get('présent', {}).get('aspects', {}).get('simple', {}).get('forms', {})
    except Exception:
        pres_simple = {}
    try:
        futur_simple = conjugations.get('futur', {}).get('aspects', {}).get('simple', {}).get('forms', {})
    except Exception:
        futur_simple = {}

    # iterate all conjugation tenses/aspects
    for tense_key, tense_val in list(conjugations.items()):
        if not isinstance(tense_val, dict):
            continue
        aspects = tense_val.get('aspects', {})
        for aspect_key, aspect_val in aspects.items():
            forms = aspect_val.get('forms', {})
            for person, form_entry in forms.items():
                if not isinstance(form_entry, dict):
                    continue
                form = form_entry.get('form')
                if not form:
                    continue
                orig = form
                cleaned = clean_form(form)
                replaced = False
                # if was continuous, map from présent simple
                if 'continu' in aspect_key or 'continu' in aspect_val.get('name','').lower():
                    alt = pres_simple.get(person, {}).get('form')
                    if alt:
                        cleaned = clean_form(alt)
                        replaced = True
                # if proche (futur proche), map from futur simple
                if not replaced and ('proche' in aspect_key or 'proche' in aspect_val.get('name','').lower()):
                    alt = futur_simple.get(person, {}).get('form')
                    if alt:
                        cleaned = clean_form(alt)
                        replaced = True
                # if cleaned still contains the infinitive (e.g., 'vais arriver' -> contains infinitive), try map
                if not replaced and infinitive and (infinitive in orig):
                    alt = futur_simple.get(person, {}).get('form') or pres_simple.get(person, {}).get('form')
                    if alt:
                        cleaned = clean_form(alt)
                        replaced = True
                # final fallback: cleaned (removed parentheses/slashes)
                form_entry['form'] = cleaned
    # write back
    Path(p).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    return p.name


def main():
    verbs = sorted(VERB_DIR.glob('*.json'))
    changed = []
    for v in verbs:
        try:
            name = process_file(v)
            changed.append(name)
        except Exception as e:
            print('ERROR', v, e)
    print('Updated', len(changed), 'files')
    for c in changed:
        print(' -', c)

if __name__ == '__main__':
    main()
