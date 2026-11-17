# OpenMBEE workshops website

Static HTML site for workshops.openmbee.org. No dependencies or build step are required. Open `index.html` in a browser for local review.

## Editing

- `index.html`: event overview and registration guidance.
- `iw-workshop.html`: OpenMBEE sessions at INCOSE IW.
- `caltech-program.html`: Caltech workshop and JPL reception program.
- `sponsors.html`: supporting organizations.
- `proposal.css`: shared presentation overrides.
- `brand/`: existing brand assets.

Registration links open external Google Forms; form settings and questions must be maintained separately. Keep navigation labels, dates, and registration destinations consistent across all pages.

## Review before publishing

Confirm fees, deadlines, JPL access requirements, whether separate INCOSE registration is needed, and whether Caltech or reception-only attendance is available independently. The copy does not establish these policies.

Check local links, keyboard navigation, and desktop and mobile layouts. No automated test suite or build tooling is configured. `CNAME` contains the existing custom domain; retain it when publishing through the repository's GitHub Pages setup.
