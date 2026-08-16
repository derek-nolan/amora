from pathlib import Path
p = Path('characters.html')
s = p.read_text(encoding='utf-8')
old = '<h3>Age of Inheritance / Arden & Caelen</h3>'
new = '<h3>Age of Inheritance</h3>'
if s.count(old) != 1:
    raise SystemExit(f'Expected one stale Campaign XII browser label, found {s.count(old)}')
p.write_text(s.replace(old, new), encoding='utf-8')
