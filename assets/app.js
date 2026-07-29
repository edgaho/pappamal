/* Holm & Eventyr — tiny bit of state: night mode + text size.
   Both persist in localStorage so an iPad remembers how the kids like it. */

(function () {
  'use strict';

  var STORE_THEME = 'he:theme';
  var STORE_SIZE = 'he:storysize';
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
})();
