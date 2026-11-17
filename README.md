# OpenMBEE workshops website

Static HTML site for workshops.openmbee.org. No package dependencies are required; checked-in HTML works without a server. Open `index.html` in a browser for local review.

## Editing

- `index.html`: event overview and registration guidance.
- `iw-workshop.html`: OpenMBEE sessions at INCOSE IW.
- `caltech-program.html`: generated Caltech workshop and JPL reception page.
- `data/caltech-2027.json`: event, registration, speaker, venue, and session data.
- `templates/caltech-program.html`: page shell and shared site navigation.
- `scripts/render_event.py`: dependency-free static page generator.
- `event.css` and `event.js`: Caltech presentation and progressive day selection.
- `sponsors.html`: supporting organizations.
- `proposal.css`: shared presentation overrides.
- `brand/`: existing brand assets.

Registration links open external Google Forms; form settings and questions must be maintained separately. Keep navigation labels, dates, and registration destinations consistent across all pages.

## Review before publishing

Confirm fees, deadlines, JPL access requirements, whether separate INCOSE registration is needed, and whether Caltech or reception-only attendance is available independently. The copy does not establish these policies.

After editing event data or the template, run `python3 scripts/render_event.py` and commit the generated HTML with its sources. `published` means a session appears in the public program, not that its detailed timing is confirmed; `tentative` timings and `tba` slots come from the draft wiki. Keep source URLs and the checked date current. All three days are visible without JavaScript; day buttons enhance the existing day anchor links.

Run `python3 scripts/render_event.py --check`, `node --test tests/event.test.cjs`, and `git diff --check`. Also check local links, keyboard navigation, zoom, contrast, and desktop and mobile layouts before publishing. Automated logic checks do not establish WCAG conformance. `CNAME` contains the existing custom domain; retain it when publishing through the repository's GitHub Pages setup.
