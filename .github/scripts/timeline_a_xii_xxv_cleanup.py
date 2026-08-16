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
        raise SystemExit(f'{path}: expected {expected} occurrences, found {count}: {old[:140]!r}')
    save(path, text.replace(old, new))


def replace_regex(path, pattern, repl, expected=1, flags=re.S):
    text = load(path)
    text2, count = re.subn(pattern, repl, text, flags=flags)
    if count != expected:
        raise SystemExit(f'{path}: expected {expected} regex replacements, found {count}: {pattern[:140]!r}')
    save(path, text2)


# XII — do not turn the Durreth surname into unsupported genealogy.
replace_exact(
    'campaign-xii.html',
    '''      <p><strong>The Durrel Line.</strong> Kael Durreth represents the Durrel name having
      drifted, over the roughly 850 years since Campaign X, into a new spelling — evidence
      that the line persists and continues producing consequential figures even as the name
      itself changes with time.</p>''',
    '''      <p><strong>The Durrel Line.</strong> The surviving Campaign XII material does not
      securely establish Kael Durreth as a blood descendant of the Durrels. His surname and
      the recurrence of familiar authority patterns make the comparison historically tempting,
      but resemblance is not genealogy. Until a lineage source proves otherwise, Kael remains
      a consequential Inheritance-era figure rather than a confirmed continuation of the Durrel
      bloodline.</p>'''
)

# XIII — preserve the source's mixed Choir/Dominion archaeology and remove an invented ordinal.
replace_exact(
    'campaign-xiii.html',
    '''      <p><strong>Magic.</strong> The Chain — revealed as a surviving Choir-era relic, the same
      technological lineage destroyed back in Campaign V — is severed from central command
      rather than destroyed outright. The leygrid stays active but ungoverned; the Chain
      persists as a neutral phenomenon, responsive to emotion but no longer obedient to
      command. This is the fifth recorded Severance in the record, and the first to leave the
      underlying structure intentionally intact rather than eliminating it.</p>''',
    '''      <p><strong>Magic.</strong> The Chain is tied by the campaign's evidence to surviving
      Choir-era relics and older Dominion-derived command technology, but the record does not
      prove one simple unbroken technological lineage back to Campaign V. Rian and Calen sever
      the Council's hierarchy rather than destroy the Chain itself. The leygrid stays active but
      ungoverned; the Chain persists as a neutral phenomenon, responsive to emotion but no longer
      obedient to central command. The sources call this a Severance, but do not securely number
      it within a universal sequence.</p>'''
)
replace_exact(
    'campaign-xiii.html',
    '''      <p>Rian Leth survives, his status afterward largely unknown but remembered publicly as
      a figure of reform and conscience. Calen Vorr survives and goes on to found a new
      doctrine of voluntary service. The Chain itself becomes autonomous and neutral,
      awaiting new interpretation rather than commanding anyone. The Council of Inheritance
      disbands entirely. In a quiet epilogue beyond the former central authority, Rian and
      Calen settle beside a forge and a river, teaching settlers that discipline isn't
      obedience and that silence can be its own kind of freedom — no collars, no hierarchies,
      only rhythm: hammer, breath, flame.</p>''',
    '''      <p>Rian Leth survives and, after the public reckoning, withdraws north with Calen
      Vorr rather than remaining at the centre of the new republic. Calen leads the Independent
      Sentinels through reconstruction before the pair settle beside a forge and a river,
      teaching that discipline is not obedience. The Chain itself becomes autonomous and
      neutral, awaiting new interpretation rather than commanding anyone. The Council of
      Inheritance disbands entirely. Their quiet epilogue leaves no collars and no hierarchy —
      only rhythm: hammer, breath, flame.</p>'''
)
replace_exact(
    'campaign-xiii.html',
    '''      <strong>Canon status:</strong> follows the fuller campaign summary: 7420–7425 ARV,
      with the Citadel of Inheritance at Tarenus Reclaimed and the Western Surge Frontier as
      a separate theatre. "Lira Durrel" and "Kael Durreth" appear as "Durell" / "Dureth" in
      some source passages — both are normalized here per the site's spelling decisions.''',
    '''      <strong>Canon status:</strong> follows the fuller campaign record. The played crisis
      runs through 7420–7421 ARV; later summaries extend the campaign entry through 7425 to
      include the reconstruction period in which the Quiet Republics, Forge Vale, and the
      post-Council settlement take shape. The site therefore retains 7420–7425 as the archival
      campaign window while distinguishing the core action from its epilogue. The Citadel of
      Inheritance at Tarenus Reclaimed and the Western Surge Frontier are separate theatres.
      "Lira Durrel" and "Kael Durreth" appear as "Durell" / "Dureth" in some source passages —
      both are normalized here per the site's spelling decisions.'''
)

# XVII — restore surviving character texture; keep the dedicated dossier's exact murder account.
replace_exact(
    'campaign-xvii.html',
    '''        <li><span class="who">Lucen Marrin</span> <span class="pc-tag">PC</span> <span class="role">Rogue, thief, and reluctant agent of the Gray Woman's order — a survivor of the fallen grids turned blade for hire. Once a street survivor, later a symbol of justice by knife.</span></li>''',
    '''        <li><span class="who">Lucen Marrin</span> <span class="pc-tag">PC</span> <span class="role">Rogue, thief, part-time sex worker, and reluctant agent of the Gray Woman's order — a street survivor of the fallen grids turned blade for hire, later remembered as a symbol of justice by knife.</span></li>'''
)

# XVIII — thematic recurrence is supported; literal echo identity is not.
replace_exact(
    'campaign-xviii.html',
    '''      <p><strong>The Durrel Line.</strong> Auren and Kael are explicitly described as a
      Taren-echo dynamic in mortal form — another recurrence of the pattern through
      resonance rather than bloodline, this time resolved by voluntary self-sealing rather
      than Severance or death. Their bargain proves a hard truth the Archivist's Note states
      plainly: sometimes a city is safest when its keepers step outside of it entirely.</p>''',
    '''      <p><strong>The Durrel Pattern.</strong> Auren and Kael replay the old Heart/Veil and
      Crown/Consort dynamic — command and willing alignment becoming a civic engine — but the
      surviving campaign dossier does not identify either man as a literal Taren or Zethyr
      echo. Their resemblance is thematic and structural, not established reincarnation or
      bloodline. This time the pattern resolves through voluntary self-sealing rather than
      Severance or death.</p>'''
)

# XIX — source confirms a Severance, but not a universal ordinal count.
replace_exact(
    'campaign-xix.html',
    '''<p><strong>Magic.</strong> The Veil-like network dissolves without open war — the sixth recorded Severance.''',
    '''<p><strong>Magic.</strong> The Veil-like network dissolves without open war in another Severance; the surviving source does not assign it a secure universal ordinal.'''
)

# XXIV — distinguish the Presence destroyed here from the separate Caelen-linked core revealed in XXV.
replace_exact(
    'campaign-xxiv.html',
    '''      <p>Somewhere in the Academy's older stonework, a fragmentary behavioural echo — not
      Dominion-made, not sentient, just a scrap of pattern left over from some earlier
      collapse — reacts to the rising power Zeth's early second-layer activation is putting
      out.''',
    '''      <p>Somewhere in the Academy's older stonework, a fragmentary behavioural echo — not
      a Dominion shard, not sentient, just a scrap of pattern drawn to Zeth's early
      second-layer activation — reacts to the rising power he is putting out.'''
)
replace_exact(
    'campaign-xxiv.html',
    '''      <p>Rather than let the Academy try to burn the leftover echo out by force, Zeth pulls
      Talren into a second-layer merge and approaches the fragment directly, meeting it in a
      controlled resonance fold instead of a fight. He dissolves it as a kindness, not a
      conquest — and with it, whatever remained of the Caelwick/Quiet Recursion shard logic
      in this era is gone for good.</p>''',
    '''      <p>Rather than let the Academy try to burn the leftover echo out by force, Zeth pulls
      Talren into a second-layer merge and approaches the Presence directly, meeting it in a
      controlled resonance fold instead of a fight. He dissolves this fragment completely as
      a kindness, not a conquest. At the time, the Academy has every reason to believe the
      last relevant residue is gone; Campaign XXV later proves that a separate Caelen-linked
      shard-core persisted inside a temporal fracture beyond the Presence encountered here.</p>'''
)
replace_exact(
    'campaign-xxiv.html',
    '''      <p>The Academy Council formally registers the world's first documented Living Dyad —
      a resonance category that is neither Dominion, nor Concord, nor ley-heir, and requires
      an entirely new classification: the Resonant Veil Lineage. It's the first time in the
      Academy's short history that its own rulebook has had to be rewritten around a single
      couple.</p>''',
    '''      <p>The Academy Council formally registers the world's first documented Living Dyad —
      a resonance category that is neither Dominion, nor Concord, nor ley-heir, and requires
      an entirely new classification. The campaign dossier calls that classification the
      <strong>Resonant Veil Lineage</strong>; here "lineage" is an Academy category for a new
      form of living resonance, not evidence that Zeth and Talren founded a hereditary
      bloodline. It's the first time in the Academy's short history that its own rulebook has
      had to be rewritten around a single couple.</p>'''
)
replace_exact(
    'campaign-xxiv.html',
    '''      <p><strong>Magic.</strong> Resonance is confirmed as a fundamentally new discipline —
      folds, drops, dyadic safety, emotional transparency, anchored consent — with a
      theorised third layer beyond anything the Academy, or Dominion records, ever mapped.
      Whatever remained of the shard logic that produced Caelen and the Quiet Recursion is
      now genuinely gone, not by force but by empathetic dissolution.</p>''',
    '''      <p><strong>Magic.</strong> Resonance is confirmed as a fundamentally new discipline —
      folds, drops, dyadic safety, emotional transparency, anchored consent — with a
      theorised third layer beyond anything the Academy, or Dominion records, ever mapped.
      The Presence encountered in this campaign is genuinely gone by empathetic dissolution.
      That does not erase every Caelen-linked remnant in existence: Campaign XXV later
      identifies a separate behavioural shard-core surviving inside the temporal fracture.</p>'''
)
replace_exact(
    'campaign-xxiv.html',
    '''      <strong>Canon status:</strong> follows the source account directly.''',
    '''      <strong>Canon status:</strong> follows the dedicated Campaign XXIV dossier, with
      one later-continuity clarification from Campaign XXV: Zeth destroys the Presence he
      encounters here, but that fragment is not the same remnant as the Caelen-linked
      shard-core later found inside the temporal fracture. "Resonant Veil Lineage" is kept
      as the Academy's period classification, not normalised into a hereditary bloodline.'''
)

# XXV — reconcile the older training-ground ending with later B1 play and clarify Timeline A's hinge.
replace_exact(
    'campaign-xxv.html',
    '''      <p>They land, hard, in the training yard at Silver Bastion in Highever — and hear two
      familiar names being called across the courtyard: Taren and Zethyr, mid-drill, neither
      one older than a teenager. It takes a moment for the six of them to understand what
      they're looking at. The future they came from is gone. The cycle has reset. And they
      are, somehow, alive at the true beginning of Amora's recorded history.</p>''',
    '''      <p>They are thrown bodily into Silver Bastion in Highever, during the training years
      of Taren and Zethyr Durrel. The older XXV dossier remembers the endpoint as the Bastion's
      training grounds; the later, played opening of Timeline B fixes the six travellers'
      arrival more precisely in the Heart chamber during early rites, with Taren and Zethyr
      still paladin candidates. The stable fact across both records is physical relocation to
      Silver Bastion before the events that once became Campaign I — not a return to the
      beginning of Amora's much older history.</p>'''
)
replace_exact(
    'campaign-xxv.html',
    '''      <p><strong>Geography.</strong> The Academy of Resonant Studies is the last location of
      Timeline A proper. The six arrive at Silver Bastion during the training years of Taren
      and Zethyr Durrel — the exact starting point of Campaign I, now revisited from the far
      end of the timeline.</p>''',
    '''      <p><strong>Geography.</strong> The Academy of Resonant Studies is Timeline A's final
      4CE theatre. The six are displaced to Silver Bastion during the training years of Taren
      and Zethyr Durrel, before the events later recorded as Campaign I. The exact landing
      point is source-layered: the older XXV dossier says the training grounds, while later
      Timeline B play places their arrival in the Heart chamber and therefore takes priority
      for the precise location.</p>'''
)
replace_exact(
    'campaign-xxv.html',
    '''      <p><strong>The Durrel Line.</strong> Timeline A ends here: Campaigns I through XXIV form
      a complete historical continuum, real but now sealed inside a closed temporal layer —
      "Timeline A, the Old Cycle," as later historians will call it. A new timeline begins
      the instant the six open their eyes in that training yard. Taren and Zethyr exist as
      teenagers, utterly unaware of the roles history already gave them once, and this moment
      becomes the opening of Timeline B — the Reforged Cycle.</p>''',
    '''      <p><strong>The Durrel Line.</strong> Campaigns I through XXIV form the pre-fracture
      historical continuum the six leave behind; Campaign XXV is itself the final Timeline A
      campaign, the hinge that closes that continuum and carries the six into Timeline B.
      Taren and Zethyr are still young paladin candidates, unaware of the roles the Old Cycle
      once gave them. Timeline B begins with their future no longer guaranteed.</p>'''
)
replace_exact(
    'campaign-xxv.html',
    '''      <p><strong>Institutions.</strong> The six become temporal refugees overnight — identity,
      magic adaptation, and sheer survival become the concerns that carry directly into what
      comes next. See <a href="campaign-b1.html">Campaign B1</a> for what happens the moment
      after this one ends.</p>''',
    '''      <p><strong>Institutions.</strong> The six become temporal refugees overnight — identity,
      magic adaptation, and sheer survival become the concerns that carry directly into what
      comes next. Their resonance vocabulary and techniques enter an era that has none of
      them. See <a href="campaign-b1.html">Campaign B1</a> for the later played account of
      their arrival and the first five days of the Reforged Cycle.</p>'''
)
replace_exact(
    'campaign-xxv.html',
    '''      <strong>Canon status:</strong> follows the source account directly. This is the hinge
      point of the entire chronicle — see Timeline B, Campaign B1, for what happens next.''',
    '''      <strong>Canon status:</strong> Campaign XXV remains the final Timeline A campaign and
      the hinge into Timeline B. The dedicated XXV dossier establishes physical displacement
      to Silver Bastion during Taren and Zethyr's training years; later Campaign B1 play fixes
      the precise arrival in the Heart chamber rather than the older dossier's training-ground
      image, so B1 takes priority on that detail. See Timeline B, Campaign B1, for the played
      continuation.'''
)

# Chronology — the 1,000-year jump is between XXII and XXIII, not inside XXII.
replace_exact(
    'chronology.html',
    '''    history isn't a straight climb toward technology — it swings between medieval and
    futuristic states more than once (Ages of Machines and Inheritance push toward
    cyberpunk infrastructure well before the Third Cyberpunk Age proper, which then
    collapses back into the Age of Disconnection). The Fourth Cyberpunk Era (4CE),
    reached via Campaign XXII's 1,000-year jump, is the last and longest-lasting of
    these swings.</p>''',
    '''    history isn't a straight climb toward technology — it swings between medieval and
    futuristic states more than once (Ages of Machines and Inheritance push toward
    cyberpunk infrastructure well before the Third Cyberpunk Age proper, which then
    collapses back into the Age of Disconnection). Campaign XXII occurs shortly after the
    final Severance in that medieval drift; the 1,000-year gap falls between XXII and XXIII,
    and the Fourth Cyberpunk Era (4CE) is already in place when XXIII begins.</p>'''
)
replace_exact(
    'chronology.html',
    '''    <tr class="tl-a"><td class="num"><a href="campaign-xxii.html">XXII</a></td><td>The Shattered Quiet</td><td>4CE begins — 1,000-year jump</td><td>9650–9660 ARV</td><td>Arden and Caelen's shard-pattern imprint at Caelwick survives a thousand years of dormancy, opening the Fourth Cyberpunk Era.</td></tr>''',
    '''    <tr class="tl-a"><td class="num"><a href="campaign-xxii.html">XXII</a></td><td>The Shattered Quiet</td><td>Post-Severance medieval drift — pre-4CE</td><td>1 A.R. after the Severance / shortly after XXI</td><td>At Caelwick, Arden and Caelen accidentally create the tiny shard-pattern imprint that later survives a thousand years of dormancy. The jump itself occurs after this campaign.</td></tr>'''
)
replace_exact(
    'chronology.html',
    '''    <tr class="tl-a"><td class="num"><a href="campaign-xxiii.html">XXIII</a></td><td>The Quiet Recursion</td><td>4CE</td><td>9670–9680 ARV</td><td>The imprint reinstantiates Arden and Caelen a millennium later; Caelen dies, and Arden learns real consent from Rian.</td></tr>''',
    '''    <tr class="tl-a"><td class="num"><a href="campaign-xxiii.html">XXIII</a></td><td>The Quiet Recursion</td><td>4CE — 1,000-year jump complete</td><td>9670–9680 ARV</td><td>The Caelwick imprint reinstantiates Arden and Caelen in 4CE; the Rainshelf Rebels later assassinate Caelen at Spirefall, and Rian helps Arden rebuild autonomy.</td></tr>'''
)
replace_exact(
    'chronology.html',
    '''    { n: "XXII", title: "The Shattered Quiet", date: "9650–9660 ARV", href: "campaign-xxii.html", blurb: "Arden and Caelen's shard-pattern imprint opens the Fourth Cyberpunk Era.", arv: 9650 },''',
    '''    { n: "XXII", title: "The Shattered Quiet", date: "1 A.R. after XXI", href: "campaign-xxii.html", blurb: "Arden and Caelen accidentally leave the Caelwick imprint; the 1,000-year jump follows afterward.", arv: 8661 },'''
)
replace_exact(
    'chronology.html',
    '''    { n: "XXIII", title: "The Quiet Recursion", date: "9670–9680 ARV", href: "campaign-xxiii.html", blurb: "The imprint reinstantiates Arden and Caelen a millennium later.", arv: 9670 },''',
    '''    { n: "XXIII", title: "The Quiet Recursion", date: "9670–9680 ARV", href: "campaign-xxiii.html", blurb: "After the 1,000-year gap, the imprint reinstantiates Arden and Caelen in 4CE; Spirefall ends Caelen's life.", arv: 9670 },'''
)

# Atlas — align the geographic rows with the dedicated XXII source and XIII's reconstruction window.
replace_exact(
    'atlas.html',
    '''      <tr><td class="camp">XXII</td><td>9650–9660 ARV</td><td>Caelwick Frontier Post: a rainswept charter outpost (population ~2,400) built atop a collapsed Dominion scribe-vault, where the Arden/Caelen shard-pattern imprint first forms. Designated Fault-01: the Caelwick Node — the first identified Quiet Fault on the continent. The Under-Pump Galleries nearby are separately classed a Tier-2 Quiet Zone: no active arcane power, but architecture that still listens for command.</td></tr>''',
    '''      <tr><td class="camp">XXII</td><td>1 A.R. after the Severance / shortly after XXI</td><td>Caelwick Frontier Post: a rainswept charter outpost (population ~2,400) built atop a collapsed Dominion scribe-vault, where the Arden/Caelen shard-pattern imprint first forms. Designated Fault-01: the Caelwick Node — the first identified Quiet Fault on the continent. The Under-Pump Galleries nearby are separately classed a Tier-2 Quiet Zone: no active arcane power, but architecture that still listens for command. The 1,000-year jump to 4CE occurs after this campaign.</td></tr>'''
)
replace_exact(
    'atlas.html',
    '''      <tr><td class="camp">XIII</td><td>7420–7421 ARV</td><td>Becomes the Citadel of Inheritance; falls into the Free Citadel, a city of archives rather than edicts, after the Chain's Severance.</td></tr>''',
    '''      <tr><td class="camp">XIII</td><td>7420–7425 ARV</td><td>Becomes the Citadel of Inheritance; the core Chain crisis and Severance occur in 7420–7421, followed by reconstruction through 7425 as it becomes the Free Citadel, a city of archives rather than edicts.</td></tr>'''
)

# Characters — propagate Lucen's surviving background detail and remove an unsupported suicide staging claim.
replace_exact(
    'characters.html',
    '''<div class="aka">Rogue, Thief · Blade for the Gray Woman's Order</div>
<p class="summary">A survivor of the fallen Concord grids turned blade for hire — once
    a street survivor, later a symbol of justice by knife.''',
    '''<div class="aka">Rogue, Thief, Part-Time Sex Worker · Blade for the Gray Woman's Order</div>
<p class="summary">A survivor of the fallen Concord grids turned blade for hire — once
    a street survivor and part-time sex worker, later a symbol of justice by knife.'''
)
replace_exact(
    'characters.html',
    '''    through fear and donation in equal measure. Captured and secretly executed by Lucen
    once her network falls, her death is staged as suicide specifically to deny the Gray
    Woman the public spectacle she'd demanded — a final act of control exercised over her''',
    '''    through fear and donation in equal measure. Captured and secretly executed by Lucen
    once her network falls, she is found dead in her cell with her throat cut in prayer
    position. Lucen keeps the hand behind the killing secret, denying the Gray Woman the
    public spectacle she'd demanded — a final act of control exercised over her'''
)

# Search propagation for Lucen.
replace_exact(
    'search-index.js',
    '''{"t": "Lucen Marrin", "s": "Rogue, Thief · Blade for the Gray Woman's Order", "u": "characters.html#lucen-marrin", "c": "character"}''',
    '''{"t": "Lucen Marrin", "s": "Rogue, Thief, Part-Time Sex Worker · Blade for the Gray Woman's Order", "u": "characters.html#lucen-marrin", "c": "character"}'''
)

# Canon Ledger — correct the XII shorthand and record the late-Timeline-A source-priority decisions.
replace_exact(
    'canon-ledger.html',
    '''    chronology corrects this. This site follows the fuller version: Kael Durreth, Evren Thalos,
    Seraphine, Jalen/Joren, and Cassius are the Age of Inheritance cast. Arden and Caelen enter
    later, in the Shattered Quiet/4CE arc (Campaigns XXII onward).</p>''',
    '''    chronology corrects this. This site follows the fuller version: Kael Durreth, Evren Thalos,
    Seraphine, Jalen/Joren, and Cassius are the Age of Inheritance cast. Arden and Caelen enter
    much later in Campaign XXII, <em>The Shattered Quiet</em>; the 1,000-year jump to 4CE occurs
    between XXII and XXIII rather than inside XII or XXII.</p>'''
)
ledger_marker = '''  <div class="ledger-entry">
    <span class="tag canon">Confirmed canon</span>
    <h3>Tempest Divide and Sundering Tempest are two separate events</h3>'''
ledger_entry = '''  <div class="ledger-entry">
    <span class="tag canon">Confirmed canon</span>
    <h3>Late Timeline A source priority — Campaigns XXII–XXV</h3>
    <p>The dedicated late-Timeline-A records settle several points that older compact summaries
    compress or contradict. <strong>XXII</strong> takes place one year after Talen Marric's
    Severance in the post-network medieval drift; Arden and Caelen leave the Caelwick imprint
    there, and the roughly 1,000-year gap falls <em>between</em> XXII and XXIII.
    <strong>XXIII</strong> is the 4CE reinstantiation era, with the corrected final account of
    Spirefall — Caelen is deliberately assassinated by the Rainshelf Rebels with a single
    analogue round, not killed by conflicting grid protocols. <strong>XXIV</strong> destroys
    the specific fragment called the Presence; <strong>XXV</strong> later reveals that a
    separate Caelen-linked behavioural shard-core had survived inside the temporal fracture,
    so those two remnants are not the same object. Campaign XXV is itself the final Timeline A
    campaign: I–XXIV are the pre-fracture continuum it closes, while XXV is the hinge that
    carries the six travellers into Timeline B.</p>
    <p><strong>Arrival-location source conflict:</strong> the older XXV dossier pictures the six
    arriving at Silver Bastion's training grounds. Later played Timeline B material in
    Campaign B1 places their actual arrival in the Heart chamber during early rites, while
    Taren and Zethyr are still paladin candidates. Both agree on physical arrival at Silver
    Bastion during the pair's training years; B1 takes priority for the precise room.</p>
  </div>

'''
text = load('canon-ledger.html')
if ledger_entry not in text:
    if text.count(ledger_marker) != 1:
        raise SystemExit('canon-ledger.html: insertion marker not unique')
    text = text.replace(ledger_marker, ledger_entry + ledger_marker)
    save('canon-ledger.html', text)

print('Late Timeline A XII–XXV reconstruction cleanup applied successfully.')
