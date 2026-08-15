(function() {
  var overlay = document.getElementById('site-search-overlay');
  var input = document.getElementById('site-search-input');
  var results = document.getElementById('site-search-results');
  var empty = document.getElementById('site-search-empty');
  var toggle = document.getElementById('site-search-toggle');
  if (!overlay || !input || !results || !toggle) return;

  var TAG_LABELS = { campaign: 'Campaign', character: 'Character', location: 'Location', lore: 'Lore', page: 'Page', faction: 'Faction', relic: 'Relic' };
  var FILTER_ORDER = ['campaign', 'character', 'location', 'faction', 'relic', 'lore', 'page'];
  var FILTER_LABELS = { campaign: 'Campaigns', character: 'Characters', location: 'Locations', faction: 'Factions', relic: 'Relics', lore: 'Lore', page: 'Pages' };
  var activeIndex = -1;
  var currentMatches = [];
  var activeFilter = 'all';

  // Build the filter chip row once and insert it between the input and the results list.
  var filterBar = document.createElement('div');
  filterBar.className = 'search-filters';
  filterBar.id = 'site-search-filters';
  var counts = { all: AMORA_SEARCH_INDEX.length };
  FILTER_ORDER.forEach(function(cat) { counts[cat] = 0; });
  AMORA_SEARCH_INDEX.forEach(function(e) { if (counts[e.c] !== undefined) counts[e.c]++; });

  function makeChip(cat, label) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'search-filter-chip' + (cat === 'all' ? ' active' : '');
    btn.setAttribute('data-cat', cat);
    btn.innerHTML = label + ' <span class="sf-count">' + counts[cat] + '</span>';
    btn.addEventListener('click', function() {
      if (activeFilter === cat) return;
      activeFilter = cat;
      filterBar.querySelectorAll('.search-filter-chip').forEach(function(el) { el.classList.remove('active'); });
      btn.classList.add('active');
      render(input.value);
      input.focus();
    });
    return btn;
  }
  filterBar.appendChild(makeChip('all', 'All'));
  FILTER_ORDER.forEach(function(cat) { filterBar.appendChild(makeChip(cat, FILTER_LABELS[cat])); });
  input.insertAdjacentElement('afterend', filterBar);

  function resetFilter() {
    activeFilter = 'all';
    filterBar.querySelectorAll('.search-filter-chip').forEach(function(el) {
      el.classList.toggle('active', el.getAttribute('data-cat') === 'all');
    });
  }

  function openSearch() {
    overlay.classList.add('open');
    input.value = '';
    resetFilter();
    input.focus();
    render('');
  }
  function closeSearch() {
    overlay.classList.remove('open');
  }
  function score(entry, q) {
    var t = entry.t.toLowerCase();
    var s = (entry.s || '').toLowerCase();
    if (t === q) return 100;
    if (t.startsWith(q)) return 80;
    if (t.indexOf(q) !== -1) return 60;
    if (s.indexOf(q) !== -1) return 30;
    return 0;
  }
  function renderList() {
    results.innerHTML = '';
    currentMatches.forEach(function(entry, i) {
      var a = document.createElement('a');
      a.className = 'search-result';
      a.href = entry.u;
      a.innerHTML = '<span class="sr-tag">' + (TAG_LABELS[entry.c] || '') + '</span>' +
        '<span class="sr-title">' + entry.t + '</span>' +
        (entry.s ? '<span class="sr-sub">' + entry.s + '</span>' : '');
      a.addEventListener('mouseenter', function() { setActive(i); });
      results.appendChild(a);
    });
  }
  function render(query) {
    var q = query.trim().toLowerCase();
    activeIndex = -1;
    var pool = activeFilter === 'all' ? AMORA_SEARCH_INDEX : AMORA_SEARCH_INDEX.filter(function(e) { return e.c === activeFilter; });

    if (!q) {
      if (activeFilter === 'all') {
        // No query and no filter: nothing to browse, matches the original empty-state behaviour.
        currentMatches = [];
        results.innerHTML = '';
        empty.style.display = 'none';
        return;
      }
      // A category chip is selected with no query yet: browse the whole category, alphabetically.
      currentMatches = pool.slice().sort(function(a, b) { return a.t.localeCompare(b.t); }).slice(0, 60);
      empty.style.display = currentMatches.length === 0 ? 'block' : 'none';
      renderList();
      return;
    }

    var scored = pool.map(function(e) { return { e: e, sc: score(e, q) }; })
      .filter(function(x) { return x.sc > 0; })
      .sort(function(a, b) { return b.sc - a.sc; })
      .slice(0, 40);
    currentMatches = scored.map(function(x) { return x.e; });
    empty.style.display = currentMatches.length === 0 ? 'block' : 'none';
    renderList();
  }
  function setActive(i) {
    var items = results.querySelectorAll('.search-result');
    items.forEach(function(el) { el.classList.remove('active'); });
    if (i >= 0 && i < items.length) {
      items[i].classList.add('active');
      items[i].scrollIntoView({ block: 'nearest' });
      activeIndex = i;
    }
  }

  toggle.addEventListener('click', openSearch);
  overlay.addEventListener('click', function(e) { if (e.target === overlay) closeSearch(); });
  input.addEventListener('input', function() { render(input.value); });
  input.addEventListener('keydown', function(e) {
    var items = results.querySelectorAll('.search-result');
    if (e.key === 'Escape') { closeSearch(); }
    else if (e.key === 'ArrowDown') { e.preventDefault(); setActive(Math.min(activeIndex + 1, items.length - 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(Math.max(activeIndex - 1, 0)); }
    else if (e.key === 'Enter') {
      if (activeIndex >= 0 && currentMatches[activeIndex]) {
        window.location.href = currentMatches[activeIndex].u;
      } else if (currentMatches.length > 0) {
        window.location.href = currentMatches[0].u;
      }
    }
  });
  document.addEventListener('keydown', function(e) {
    if ((e.key === '/' || (e.key === 'k' && (e.metaKey || e.ctrlKey))) && overlay && !overlay.classList.contains('open')) {
      var active = document.activeElement;
      var typing = active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA');
      if (!typing) { e.preventDefault(); openSearch(); }
    }
  });
})();
