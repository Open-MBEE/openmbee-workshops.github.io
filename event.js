/* Progressive enhancement: all days stay readable without JavaScript. */
(function () {
  const controls = document.getElementById('agenda-controls');
  const days = Array.from(document.querySelectorAll('.agenda-day'));
  if (!controls || !days.length) return;
  const buttons = Array.from(controls.querySelectorAll('button[data-day]'));
  function select(id, announce) {
    if (id !== 'all' && !days.some(day => day.id === id)) return;
    days.forEach(day => { day.hidden = id !== 'all' && day.id !== id; });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.day === id)));
    if (announce) {
      const selected = buttons.find(button => button.dataset.day === id);
      document.getElementById('agenda-announcement').textContent = id === 'all' ? 'Showing all agenda days.' : 'Showing ' + selected.textContent + '.';
    }
  }
  controls.hidden = false;
  buttons.forEach(button => button.addEventListener('click', () => select(button.dataset.day, true)));
  function followHash() {
    const id = window.location.hash.slice(1);
    const day = days.find(day => day.id === id || day.contains(document.getElementById(id)));
    if (day) {
      select(day.id, false);
      day.scrollIntoView({ block: 'start' });
    }
  }
  window.addEventListener('hashchange', followHash);
  followHash();
})();
