/* Pappamål — tiny bit of state: night mode + text size.
   Both persist in localStorage so an iPad remembers how the kids like it. */

(function () {
  'use strict';

  var STORE_THEME = 'pm:theme';
  var STORE_SIZE = 'pm:storysize';
  var MIN = 18, MAX = 30, STEP = 2, DEFAULT = 21;

  var root = document.documentElement;

  /* ---- theme -------------------------------------------------------- */

  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    var btn = document.querySelector('[data-theme-toggle]');
    if (btn) {
      var night = theme === 'night';
      btn.textContent = night ? '☀ Dag' : '☾ Kveld';
      btn.setAttribute('aria-label', night ? 'Bytt til dagmodus' : 'Bytt til kveldsmodus');
    }
  }

  var stored = null;
  try { stored = localStorage.getItem(STORE_THEME); } catch (e) {}
  applyTheme(stored || (window.matchMedia &&
    window.matchMedia('(prefers-color-scheme: dark)').matches ? 'night' : 'day'));

  document.addEventListener('click', function (ev) {
    var toggle = ev.target.closest('[data-theme-toggle]');
    if (!toggle) return;
    var next = root.getAttribute('data-theme') === 'night' ? 'day' : 'night';
    applyTheme(next);
    try { localStorage.setItem(STORE_THEME, next); } catch (e) {}
  });

  /* ---- text size ---------------------------------------------------- */

  function applySize(px) {
    root.style.setProperty('--story-size', px + 'px');
    var minus = document.querySelector('[data-size="-"]');
    var plus = document.querySelector('[data-size="+"]');
    if (minus) minus.disabled = px <= MIN;
    if (plus) plus.disabled = px >= MAX;
  }

  var size = DEFAULT;
  try {
    var raw = parseInt(localStorage.getItem(STORE_SIZE), 10);
    if (raw >= MIN && raw <= MAX) size = raw;
  } catch (e) {}
  applySize(size);

  document.addEventListener('click', function (ev) {
    var btn = ev.target.closest('[data-size]');
    if (!btn) return;
    size = Math.min(MAX, Math.max(MIN, size + (btn.dataset.size === '+' ? STEP : -STEP)));
    applySize(size);
    try { localStorage.setItem(STORE_SIZE, String(size)); } catch (e) {}
  });

  /* ---- lest ---------------------------------------------------------- */

  var STORE_LEST = 'pm:lest';

  function kanLagre() {
    try {
      localStorage.setItem('pm:probe', '1');
      localStorage.removeItem('pm:probe');
      return true;
    } catch (e) { return false; }
  }

  function lesteNa() {
    try { return JSON.parse(localStorage.getItem(STORE_LEST)) || {}; }
    catch (e) { return {}; }
  }

  function lagreLeste(lest) {
    try { localStorage.setItem(STORE_LEST, JSON.stringify(lest)); } catch (e) {}
  }

  function tegnKnapp(btn, lest) {
    var er = !!lest[btn.dataset.lest];
    btn.setAttribute('aria-pressed', er ? 'true' : 'false');
    btn.querySelector('.lest-tekst').textContent = er ? 'Lest' : 'Marker som lest';
  }

  function merkKort(lest) {
    var kort = document.querySelectorAll('.story-card[data-slug]');
    for (var i = 0; i < kort.length; i++) {
      var er = !!lest[kort[i].dataset.slug];
      kort[i].classList.toggle('er-lest', er);
      var merke = kort[i].querySelector('.lest-merke-tekst');
      if (er && !merke) {
        merke = document.createElement('span');
        merke.className = 'visually-hidden lest-merke-tekst';
        merke.textContent = ' — lest';
        kort[i].querySelector('h3').appendChild(merke);
      } else if (!er && merke) {
        merke.parentNode.removeChild(merke);
      }
    }
  }

  var knapper = document.querySelectorAll('[data-lest]');

  if (!kanLagre()) {
    /* En knapp som ikke husker er verre enn ingen knapp. */
    for (var k = 0; k < knapper.length; k++) knapper[k].hidden = true;
  } else {
    var lest = lesteNa();
    for (var j = 0; j < knapper.length; j++) tegnKnapp(knapper[j], lest);
    merkKort(lest);

    document.addEventListener('click', function (ev) {
      var btn = ev.target.closest('[data-lest]');
      if (!btn) return;
      var slug = btn.dataset.lest;
      var na = lesteNa();
      if (na[slug]) { delete na[slug]; } else { na[slug] = new Date().toISOString(); }
      lagreLeste(na);
      tegnKnapp(btn, na);
      merkKort(na);
    });
  }
})();
