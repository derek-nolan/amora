(function() {
  var overlay = document.getElementById('site-search-overlay');
  var input = document.getElementById('site-search-input');
  var results = document.getElementById('site-search-results');
  var empty = document.getElementById('site-search-empty');
  var toggle = document.getElementById('site-search-toggle');
  if (!overlay || !input || !results || !toggle) return;

  var TAG_LABELS = { campaign: 'Campaign', character: 'Character', location: 'Location', lore: 'Lore', page: 'Page', faction: 'Faction', relic: 'Relic' };
  var activeIndex = -1;
  var currentMatches = [];

  function openSearch() {
    overlay.classList.add('open');
    input.value = '';
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
  function render(query) {
    var q = query.trim().toLowerCase();
    results.innerHTML = '';
    activeIndex = -1;
    if (!q) {
      currentMatches = [];
      empty.style.display = 'none';
      return;
    }
    var scored = AMORA_SEARCH_INDEX.map(function(e) { return { e: e, sc: score(e, q) }; })
      .filter(function(x) { return x.sc > 0; })
      .sort(function(a, b) { return b.sc - a.sc; })
      .slice(0, 40);
    currentMatches = scored.map(function(x) { return x.e; });
    if (currentMatches.length === 0) {
      empty.style.display = 'block';
      return;
    }
    empty.style.display = 'none';
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
