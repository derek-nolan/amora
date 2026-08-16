from pathlib import Path
import re


def load(path):
    return Path(path).read_text(encoding='utf-8')

def save(path, text):
    Path(path).write_text(text, encoding='utf-8')

def replace_exact(path, old, new, expected=1):
    text = load(path)
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{path}: expected {expected} occurrences, found {count}: {old[:120]!r}')
    save(path, text.replace(old, new))

def replace_regex(path, pattern, repl, expected=1, flags=re.S):
    text = load(path)
    text2, count = re.subn(pattern, repl, text, flags=flags)
    if count != expected:
        raise SystemExit(f'{path}: expected {expected} regex replacements, found {count}: {pattern[:120]!r}')
    save(path, text2)

# Campaign XI: remove two unsupported details while preserving the campaign-specific discovery.
replace_exact(
    'campaign-xi.html',
    '      calls the <strong>Thirteenth Seal</strong>. A later compendium describes it as a bronze\n      tablet bearing the glyph "Memory Through Loss." Its existence in Campaign XI is now\n      confirmed; its name does <em>not</em> make it one of the ancient Great Seals.</p>',
    '      calls the <strong>Thirteenth Seal</strong>. Its physical recovery in Campaign XI is now\n      confirmed; the surviving record does not securely establish what the name means, and it\n      does <em>not</em> make the object one of the ancient Great Seals.</p>'
)
replace_exact(
    'campaign-xi.html',
    '      <p><strong>The Thirteenth Seal.</strong> A half-melted bronze seal-tablet carrying\n      "Memory Through Loss" is physically recovered after the null-relic\'s destruction. That\n      resolves the old question of whether Campaign XI contained an object by this name. What\n      remains unresolved is what the name meant. It is a later Clause/Choir-era artefact in the\n      surviving record, not a thirteenth member of the ancient eight Great Seals.</p>',
    '      <p><strong>The Thirteenth Seal.</strong> A half-melted object identified in the\n      campaign record as the Thirteenth Seal is recovered after the null-relic\'s destruction.\n      That resolves the old question of whether Campaign XI contained an object by this name.\n      Its origin, function, and the meaning of the title remain unresolved; it is not evidence\n      for a thirteenth member of the ancient eight Great Seals.</p>'
)

# Canon Ledger: physical existence is now confirmed by the dedicated XI record, while interpretation stays open.
replace_regex(
    'canon-ledger.html',
    r'  <div class="ledger-entry">\n    <span class="tag open">Open</span>\n    <h3>Thirteenth Seal — unverified legacy reference</h3>.*?\n  </div>',
    '''  <div class="ledger-entry">\n    <span class="tag canon">Confirmed canon</span>\n    <h3>The Thirteenth Seal — object confirmed, meaning unresolved</h3>\n    <p>The dedicated final Campaign XI record confirms that, after the Null Relic is unmade\n    beneath Veylaris Rest, the party physically recovers a half-melted object identified as\n    the <strong>Thirteenth Seal</strong>. That supersedes this site's earlier assumption that\n    the name survived only in a later relic-continuity table. What it does <em>not</em> confirm\n    is a thirteenth ancient Great Seal: the recovered B16/B17 registry remains exactly eight\n    — Heart, Flame, Stone, Storm, Life, Shadow, Light, and Frost. The XI artefact's creator,\n    function, age, and reason for the name remain unresolved. It is therefore an attested\n    Campaign XI relic with disputed interpretation, not an addition to the ancient Seal\n    system. See <a href="campaign-xi.html">Campaign XI</a> and\n    <a href="relics.html#thirteenth-seal">Relics &amp; Artefacts</a>.</p>\n  </div>'''
)

# Relics: expose the XI object and soften Bastion Saren's disputed construction era.
replace_exact(
    'relics.html',
    '    <a href="#null-relic">Null Relic</a>\n',
    '    <a href="#null-relic">Null Relic</a>\n    <a href="#thirteenth-seal">Thirteenth Seal</a>\n'
)
replace_exact(
    'relics.html',
    '      <dt>Creator/origin</dt><dd>Ancient Choir-era fortress hidden in the Menge Expanse; once a ley-stabiliser.</dd>',
    '      <dt>Creator/origin</dt><dd>Ancient frozen relay fortress in the Menge Expanse; surviving records disagree on whether its construction predates the Dominion or belongs to the Choir era, so its exact origin remains unresolved.</dd>'
)
marker = '  <div class="relic-card" id="fragment-of-luminara">'
text = load('relics.html')
if text.count(marker) != 1:
    raise SystemExit('relics.html: fragment marker not unique')
card = '''  <div class="relic-card" id="thirteenth-seal">\n    <h2>The Thirteenth Seal <span class="confidence confirmed">Object confirmed</span></h2>\n    <p class="tagline">A confirmed Campaign XI artefact with an unresolved name.</p>\n    <dl class="relic-meta">\n      <dt>Timeline &amp; era</dt><dd>Timeline A, Campaign XI, c. 6550 ARV.</dd>\n      <dt>Discovery</dt><dd>Recovered as a half-melted object in the Lyricum anchor chamber after the Null Relic is unmade beneath Veylaris Rest.</dd>\n      <dt>Creator/origin</dt><dd>Unresolved.</dd>\n      <dt>Function</dt><dd>Unresolved.</dd>\n    </dl>\n    <p class="summary"><strong>What is confirmed:</strong> the dedicated final Campaign XI record physically places an object called the Thirteenth Seal in the party's discoveries after the Unmaking of the Quiet. The earlier site treatment that called the entire reference unverified is therefore superseded.</p>\n    <p class="summary"><strong>What is not confirmed:</strong> the title does not establish this as a thirteenth member of the ancient Great Seal network. Later Great-Seal archaeology fixes that registry at eight. Older compendia interpret the XI object as a post-Dominion attempt to bind the cycle or as "law without command," but those are interpretations rather than secure campaign facts.</p>\n    <p class="summary"><strong>Current status:</strong> exact custody after Campaign XI is not securely recorded. See <a href="campaign-xi.html">Campaign XI</a> and the <a href="canon-ledger.html">Canon Ledger</a>.</p>\n  </div>\n\n'''
text = text.replace(marker, card + marker)
save('relics.html', text)

# Factions: the Inquest is already operating during XI; XI intensifies its remit rather than founding it at the end.
replace_exact(
    'factions.html',
    '      <dt>Era</dt><dd>Timeline A, chartered by the close of Campaign XI, roughly 6550 ARV.</dd>',
    '      <dt>Era</dt><dd>Timeline A, already active during Campaign XI, roughly 6550 ARV; the campaign\'s ley disturbances and Witness signatures intensify its oversight.</dd>'
)
replace_exact(
    'factions.html',
    '      <dt>Doctrine</dt><dd>Chartered oversight of the Twelve Herald Houses\' descendant lineages — Witnesses, Editors, Recorders, Judges — each tracing back to a different facet of the old law.</dd>',
    '      <dt>Doctrine</dt><dd>State oversight of ley disturbances, forbidden Choir-tech, and harmonic inheritance. Campaign XI later ties that work to the Twelve Herald Houses\' descendant traditions — Witnesses, Editors, Recorders, Judges, and related offices.</dd>'
)

# Atlas: Bastion Saren is certain; its construction era is not.
replace_exact(
    'atlas.html',
    '<li><span class="locname">Bastion Saren</span><br><span class="locnote">Frozen pre-Dominion relay fortress; site of Clause XI\'s completion (Campaign <a href="campaign-xi.html" class="tl-a">XI</a>).</span></li>',
    '<li><span class="locname">Bastion Saren</span><br><span class="locnote">Ancient frozen relay fortress of disputed construction era; reawakened during Campaign <a href="campaign-xi.html" class="tl-a">XI</a> and central to the articulation of Clause XI.</span></li>'
)

# Chronology: propagate the reconstructed XI outcome and the already-settled XIII date.
replace_exact(
    'chronology.html',
    '<tr class="tl-a"><td class="num"><a href="campaign-xi.html">XI</a></td><td>Clause XI / The Null Relic</td><td>Age of Clause — First Cyberpunk Era</td><td>c. 6550 ARV</td><td>Riven Mareth forges Clause XI, the Breathing Law, and becomes Clause Zero rather than erasing or hoarding a dangerous relic\'s power.</td></tr>',
    '<tr class="tl-a"><td class="num"><a href="campaign-xi.html">XI</a></td><td>Clause XI / The Null Relic</td><td>Age of Clause — First Cyberpunk Era</td><td>c. 6550 ARV</td><td>Riven Mareth articulates Clause XI at Bastion Saren, orders the Null Relic unmade, and ultimately merges Clause Zero\'s mercy harmonic into the Twelve while remaining mortal and free.</td></tr>'
)
replace_exact('chronology.html', '7420–7421 ARV', '7420–7425 ARV', expected=2)
replace_exact(
    'chronology.html',
    '{ n: "XI", title: "Clause XI / The Null Relic", date: "c. 6550 ARV", href: "campaign-xi.html", blurb: "Riven Mareth forges Clause XI, the Breathing Law.", arv: 6550 }',
    '{ n: "XI", title: "Clause XI / The Null Relic", date: "c. 6550 ARV", href: "campaign-xi.html", blurb: "Riven Mareth articulates Clause XI, unmakes the Null Relic, and becomes the mortal Breath Between Laws.", arv: 6550 }'
)

# Search index: add the now-attested Campaign XI relic if not already present.
text = load('search-index.js')
entry = '{"t": "The Thirteenth Seal", "s": "Timeline A · Campaign XI · confirmed artefact, interpretation unresolved", "u": "relics.html#thirteenth-seal", "c": "relic"}'
if entry not in text:
    if not text.rstrip().endswith('];'):
        raise SystemExit('search-index.js: unexpected ending')
    stripped = text.rstrip()
    text = stripped[:-2] + ', ' + entry + '];\n'
    save('search-index.js', text)

print('Campaign XI reference cleanup applied successfully.')
