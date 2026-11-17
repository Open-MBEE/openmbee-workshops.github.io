/* Native disclosure buttons work the same way on desktop and mobile. */
(function () {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const toggle = header.querySelector('.nav-toggle');
  const groups = Array.from(header.querySelectorAll('.group-btn'));
  groups.forEach((button, index) => {
    const submenu = button.nextElementSibling;
    if (submenu) {
      submenu.id = 'nav-group-' + index;
      button.setAttribute('aria-controls', submenu.id);
    }
  });
  function closeGroups(except) {
    groups.forEach(button => {
      if (button !== except) button.setAttribute('aria-expanded', 'false');
    });
  }
  toggle.addEventListener('click', () => {
    const open = header.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    if (!open) closeGroups();
  });
  groups.forEach(button => button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') === 'true';
    closeGroups(button);
    button.setAttribute('aria-expanded', String(!open));
  }));
  header.addEventListener('keydown', event => {
    const group = groups.find(button => button.parentElement.contains(event.target));
    if (event.key === 'ArrowDown' && group) {
      event.preventDefault();
      closeGroups(group);
      group.setAttribute('aria-expanded', 'true');
      group.nextElementSibling.querySelector('a')?.focus();
    }
    if (event.key !== 'Escape') return;
    if (group && group.getAttribute('aria-expanded') === 'true') {
      group.setAttribute('aria-expanded', 'false');
      group.focus();
    } else if (header.classList.contains('open')) {
      closeGroups();
      header.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.focus();
    }
  });
  header.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    closeGroups();
    const mobileOpen = header.classList.contains('open');
    header.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    // An in-page link can otherwise leave focus in the now-hidden mobile menu.
    if (mobileOpen && link.hash && link.pathname === window.location.pathname) {
      const target = document.getElementById(link.hash.slice(1));
      if (target) {
        target.setAttribute('tabindex', '-1');
        target.focus();
      }
    }
  }));
  document.addEventListener('click', event => {
    if (!header.contains(event.target)) closeGroups();
  });
})();
