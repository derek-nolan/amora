from pathlib import Path


def replace_exact(path, old, new, expected=1):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    found = text.count(old)
    if found != expected:
        raise SystemExit(f"{path}: expected {expected} occurrence(s), found {found}: {old[:100]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


# characters.html — propagate early Timeline A reconstruction decisions.
replace_exact(
    "characters.html",
    '<span class="date">7420–7421 ARV</span>',
    '<span class="date">7420–7425 ARV</span>',
)
replace_exact(
    "characters.html",
    '<span class="date">9650–9660 ARV</span>',
    '<span class="date">Shortly after XXI</span>',
)
replace_exact(
    "characters.html",
    "not by lineage — he's not descended from Tarenus Durrel, the order's original founder;\n    that blood runs through Taren.",
    "not by lineage — he's not descended from Tarenus Durrel, whose first permanent Heart\n    watch predates the later order; that blood runs through Taren.",
)
replace_exact(
    "characters.html",
    "Their marriage follows in month five, during an interlude in Evermere —\n    Zethyr takes the Durrel name at this marriage, not before — and it's here, unconsciously, that what later chronicles call the \"Chains of the Veil\"\n    begin forming between them, long before either recognises it as anything but love.",
    "Their marriage follows in month five, during an interlude in Evermere. The surviving\n    record does not securely preserve when Zethyr began using the Durrel surname; the\n    marriage is secure, the surname timing is not. It's here, unconsciously, that what\n    later chronicles call the \"Chains of the Veil\" begin forming between them, long before\n    either recognises it as anything but love.",
)
replace_exact(
    "characters.html",
    "a direct descendant of Tarenus Durrel, the order's original founder,",
    "a direct descendant of Tarenus Durrel, the first permanent Warden of Heart in his House,",
)
replace_exact(
    "characters.html",
    '<div class="aka">Magister of the Collegium Arcanum · Flamewarden (also recorded as Arienna Voss)</div>',
    '<div class="aka">Magister of the Collegium Arcanum · Flamewarden</div>',
)
replace_exact(
    "characters.html",
    "His creed, \"Through Law, Salvation,\" defines an entire age — and founds the Executor\n    office that becomes capital of the Wardens' Theocracy.",
    "His creed, \"Through Law, Salvation,\" defines an entire age — and helps establish the\n    Executor Office as the governing institution based at the Gate, capital of the Wardens'\n    Theocracy.",
)
replace_exact(
    "characters.html",
    '<div class="char-row" data-campaigns="viii"><span class="name">Alaric &amp; Lorian</span><span class="role">Paladin of Light and Scholar of Silence, married. Their household is where the Gate Codex\'s human cost actually shows — a marriage tested by living inside laws Sirian wrote to be fair but which get weaponised regardless.</span><span class="link"><a href="campaign-viii.html">VIII</a></span></div>\n',
    "",
)
replace_exact(
    "characters.html",
    '<div class="char-row" data-campaigns="x"><span class="name">Lior &amp; Iria</span><span class="role">Serik\'s closest civic allies through the Severing — co-rebels and moral equals rather than followers, serving as both his personal leverage and his reason for restraint whenever restraint is the harder choice.</span><span class="link"><a href="campaign-x.html">X</a></span></div>\n',
    "",
)
# Add the two reconstructed/provisional figures without pretending they are recovered original-play PCs.
replace_exact(
    "characters.html",
    '<div class="char-row" data-campaigns="xi"><span class="name">Verrin Mael</span>',
    '<div class="char-row" data-campaigns="ix"><span class="name">Jax (Reconstructed)</span><span class="role">A reconstructed digital Veilbearer consciousness recorded in later lineage material as Rhett Vale\'s co-discoverer of the Ring of Amora. Distinct from Campaign V\'s human Jax Korran; the Heartbearer/Veilbearer framing is archival interpretation, not literal reincarnation.</span><span class="link"><a href="campaign-ix.html">IX</a></span></div>\n<div class="char-row" data-campaigns="x"><span class="name">The Architect <span class="antagonist-tag">Reconstructed Antagonist</span></span><span class="role">A synthetic Veil-side figure preserved in a later continuum table as Serik Thorne\'s opposing test. Included as labelled editorial reconstruction rather than confirmed original-play cast; the exact final blow against the last Veil Shard remains unresolved.</span><span class="link"><a href="campaign-x.html">X</a></span></div>\n<div class="char-row" data-campaigns="xi"><span class="name">Verrin Mael</span>',
)

# search-index.js — remove unsupported alias and expose reconstructed figures.
replace_exact(
    "search-index.js",
    '"s": "Magister of the Collegium Arcanum · Flamewarden (also recorded as Arienna Voss)"',
    '"s": "Magister of the Collegium Arcanum · Flamewarden"',
)
replace_exact(
    "search-index.js",
    '];',
    ', {"t": "Jax (Reconstructed)", "s": "Timeline A · Campaign IX · reconstructed digital co-discoverer", "u": "campaign-ix.html", "c": "character"}, {"t": "The Architect", "s": "Timeline A · Campaign X · later-recorded synthetic antagonist", "u": "campaign-x.html", "c": "character"}];',
)

# canon-ledger.html — remove superseded Brevair/Voss claims and record reconstruction status cleanly.
replace_exact(
    "canon-ledger.html",
    "different starting relationship with Highever in each timeline (Timeline A: diplomatic,\n    becomes a crown ally; Timeline B: isolationist empire under Emperor Trainor Fell, not an\n    ally);",
    "original opening relationship with Highever (Brevair is already an isolationist,\n    expansionist empire under Emperor Trainor Fell while Highever rallies opposition; the\n    timelines diverge in what happens to that rivalry afterward);",
)
replace_exact(
    "canon-ledger.html",
    "Previously listed here as a site-invented choice between two unattested names. A\n    project-chat correction specifically identifies <strong>Lume</strong> as the name for\n    Campaign I's Flamewarden — this wasn't an arbitrary pick between equals after all.\n    Corrected across the site (Campaigns I–II, Characters, Atlas, Factions, Magic Codex);\n    Voss is retained everywhere as the recorded variant.",
    "The surviving early campaign material consistently identifies Campaign I's Flamewarden\n    as <strong>Arienna Lume</strong>. The previously displayed \"Arienna Voss\" variant could\n    not be substantiated during the deeper Campaign I reconstruction and is therefore\n    treated as later site/summary drift rather than a co-equal recorded name. Corrected\n    across the campaign and reference pages; Lume is the published form.",
)
replace_exact(
    "canon-ledger.html",
    "A separate, older continuum table\n    introduces \"the Architect\" — a provisional final synthetic Taren-echo said to test\n    Serik's refusal — without corroboration from any other source; this figure is\n    deliberately not added to the site as confirmed content. A further \"Burning Fall\"\n    account (Sirian and Alaric opening a remnant key, Lior and Jalen exposing an emperor\n    through records, Sevrin Mareth renouncing Elian, Lior breaking the shard beneath the\n    Collegium) survives in one older summary document but directly conflicts with the\n    accepted Serik/Lior/Iria campaign frame and isn't merged into it. Recorded here rather\n    than silently adopted or silently discarded.",
    "A separate, older continuum table introduces <strong>the Architect</strong> — a\n    provisional final synthetic Taren-echo said to test Serik's refusal. The reconstructed\n    Campaign X page now includes that figure <em>with the provenance visible</em>: an\n    editorial/archival reconstruction, not confirmed original-play cast. A further \"Burning\n    Fall\" account (Sirian and Alaric opening a remnant key, Lior and Jalen exposing an\n    emperor through records, Sevrin Mareth renouncing Elian, Lior breaking the shard beneath\n    the Collegium) survives in one older summary document but conflicts with the accepted\n    Serik-led campaign frame and is not silently merged into it. The exact physical hand\n    that destroys the final Veil Shard remains unresolved.",
)
# Add an explicit chronology-normalisation note before Normalised terminology.
replace_exact(
    "canon-ledger.html",
    '  <h2 style="text-transform:uppercase;letter-spacing:.1em;font-size:1rem;color:var(--vellum-dim);border-bottom:1px solid var(--hairline);padding-bottom:8px;margin-top:44px;">Normalised terminology</h2>',
    '  <div class="ledger-entry">\n    <span class="tag normalised">Normalised chronology</span>\n    <h3>Campaigns I–II: played months versus later ARV spans</h3>\n    <p>The surviving campaign-era chronology describes Campaign I as seven months and Campaign II as beginning in the eighth month, with the Dominion arc unfolding over roughly the following two years. Later summary documents normalised those campaigns to 0–27 ARV and 28–55 ARV. The site keeps those later spans in overview/reference tiles where useful for long-range chronology, while the reconstructed campaign pages explicitly distinguish them from the played month-by-month duration rather than pretending the two systems are identical.</p>\n  </div>\n\n  <h2 style="text-transform:uppercase;letter-spacing:.1em;font-size:1rem;color:var(--vellum-dim);border-bottom:1px solid var(--hairline);padding-bottom:8px;margin-top:44px;">Normalised terminology</h2>',
)

# atlas.html — restore the original expansionist Brevair opening state.
replace_exact(
    "atlas.html",
    "Home realm of the new Heartwarden order; diplomatic and scholarly ties to Brevair and Menge.",
    "Home realm of the revived Heartwarden order; Highever leads diplomatic opposition to expansionist Brevair while maintaining wider scholarly and religious links across Vanmere.",
)
replace_exact(
    "atlas.html",
    "Brevair's starting relationship with Highever is genuinely different\n    between the two timelines, not the same premise playing out two ways. Timeline A begins\n    diplomatically engaged and becomes a crown ally through the Heartwardens' work; Timeline\n    B begins as an isolationist, militarised rival under Emperor Trainor Fell.",
    "Brevair's opening state predates the Timeline A/B divergence: an isolationist,\n    expansionist empire under Emperor Trainor Fell, with Highever rallying opposition to its\n    attempts to destabilise neighbouring realms. The timelines diverge in what happens to\n    that rivalry afterward rather than beginning from opposite diplomatic premises.",
)
replace_exact(
    "atlas.html",
    "Becomes a crown ally to the new Heartwarden order.",
    "Expansionist rival under Emperor Trainor Fell; Highever rallies regional opposition while the Heartwarden crisis work unfolds.",
)

# factions.html — clean early-name drift and revival terminology.
replace_exact(
    "factions.html",
    "Timeline A, Campaign I, 0–27 ARV (founding); revived generations after an original lapse.",
    "Timeline A, Campaign I (later archive: 0–27 ARV); revived generations after an original lapse.",
)
replace_exact(
    "factions.html",
    '<dt>Founders</dt><dd><a href="campaign-i.html">Arienna Lume</a> (also recorded as Arienna Voss), Magister and Flamewarden, among the Heartwardens\' own founding ranks.</dd>',
    '<dt>Founders</dt><dd><a href="campaign-i.html">Arienna Lume</a>, Magister and Flamewarden, among the revived Heartwardens\' early ranks.</dd>',
)

print("Reference cleanup replacements applied successfully.")
