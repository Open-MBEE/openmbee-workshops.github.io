const { test } = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
function setup() {
  function element() {
    return { attrs: {}, events: {}, setAttribute(k, v) { this.attrs[k] = v; }, getAttribute(k) { return this.attrs[k]; }, addEventListener(k, fn) { this.events[k] = fn; }, focus() { this.focused = true; } };
  }
  const toggle = element(), group = element(), link = element();
  group.attrs['aria-expanded'] = 'false';
  group.parentElement = { contains: target => target === group || target === link };
  group.nextElementSibling = { querySelector: () => link };
  const open = new Set();
  const header = element();
  header.classList = { toggle(k) { if (open.has(k)) { open.delete(k); return false; } open.add(k); return true; }, remove: k => open.delete(k), contains: k => open.has(k) };
  header.querySelector = () => toggle;
  header.querySelectorAll = selector => selector === '.group-btn' ? [group] : [link];
  header.contains = target => [toggle, group, link].includes(target);
  const document = { querySelector: () => header, addEventListener() {} };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../navigation.js'), 'utf8'), { document, window: { location: { pathname: '/' } } });
  return { header, toggle, group, link };
}
test('disclosure exposes its controlled submenu and toggles on click', () => {
  const { group } = setup();
  assert.equal(group.attrs['aria-controls'], 'nav-group-0');
  group.events.click(); assert.equal(group.attrs['aria-expanded'], 'true');
  group.events.click(); assert.equal(group.attrs['aria-expanded'], 'false');
});
test('Arrow Down enters submenu; Escape closes it and returns focus', () => {
  const { header, group, link } = setup();
  header.events.keydown({ key: 'ArrowDown', target: group, preventDefault() {} });
  assert.equal(link.focused, true);
  header.events.keydown({ key: 'Escape', target: link });
  assert.equal(group.attrs['aria-expanded'], 'false');
  assert.equal(group.focused, true);
});
test('Escape closes mobile menu and returns focus to menu toggle', () => {
  const { header, toggle } = setup();
  toggle.events.click(); assert.equal(toggle.attrs['aria-expanded'], 'true');
  header.events.keydown({ key: 'Escape', target: toggle });
  assert.equal(toggle.attrs['aria-expanded'], 'false');
  assert.equal(toggle.focused, true);
});
