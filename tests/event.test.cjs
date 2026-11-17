const { test } = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
function setup(hash = '') {
  const days = ['03', '04', '05'].map(d => ({ id: 'day-2027-02-' + d, hidden: false, contains: () => false, scrollIntoView() { this.scrolled = true; } }));
  const buttons = [...days.map(d => ({ dataset: { day: d.id }, textContent: d.id })), { dataset: { day: 'all' }, textContent: 'All days' }];
  buttons.forEach(b => { b.setAttribute = (k, v) => { b[k] = v; }; b.addEventListener = (_, fn) => { b.click = fn; }; });
  const announcement = {};
  const dayLinks = { hidden: false };
  const controls = { hidden: true, querySelectorAll: () => buttons };
  const window = { location: { hash }, addEventListener: (_, fn) => { window.hashchange = fn; } };
  const document = { getElementById: id => id === 'agenda-controls' ? controls : id === 'agenda-announcement' ? announcement : id === 'agenda-day-links' ? dayLinks : days.find(d => d.id === id), querySelectorAll: () => days };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../event.js'), 'utf8'), { document, window });
  return { days, buttons, announcement, window, controls, dayLinks };
}
test('starts with all days visible and exposes native day buttons', () => {
  const { days, controls, buttons } = setup();
  assert.equal(controls.hidden, false);
  assert.ok(days.every(d => !d.hidden));
  assert.equal(buttons[3]['aria-pressed'], undefined); // Initial state is in static HTML.
});
test('selecting a day hides others and announces it; all days restores them', () => {
  const { days, buttons, announcement } = setup();
  buttons[1].click();
  assert.deepEqual(days.map(d => d.hidden), [true, false, true]);
  assert.equal(buttons[1]['aria-pressed'], 'true');
  assert.match(announcement.textContent, /2027-02-04/);
  buttons[3].click();
  assert.ok(days.every(d => !d.hidden));
});
test('deep links and hash navigation reveal and scroll to the requested day', () => {
  const { days, window } = setup('#day-2027-02-05');
  assert.equal(days[2].hidden, false);
  assert.equal(days[2].scrolled, true);
  window.location.hash = '#day-2027-02-03';
  window.hashchange();
  assert.deepEqual(days.map(d => d.hidden), [false, true, true]);
});

test('enhancement replaces fallback day links with a single day control group', () => {
  const { controls, dayLinks } = setup();
  assert.equal(controls.hidden, false);
  assert.equal(dayLinks.hidden, true);
});
