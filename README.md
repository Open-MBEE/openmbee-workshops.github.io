# OpenMBEE workshops website

Static HTML for workshops.openmbee.org, published through this repository's GitHub Pages setup. No build step or package installation is required.

## Content and editing

- `index.html`: workshop overview, event tiles with registration links, and brief keynote/activity highlights.
- `iw-workshop.html`: IW overview, registration, brief session highlights, and links to the full IW wiki program.
- `caltech-program.html`: Caltech and reception registration, keynote/activity highlights, and links to the full workshop wiki program.
- `sponsors.html`: workshop supporters, logos, and community categories awaiting announcements.
- `brand/brand.css`: shared OpenMBEE brand styling; page layout styles also live in each HTML file.
- `navigation.js`: shared desktop/mobile menus and keyboard interactions.
- `brand/` and `OMBEE2027/`: logos and announcement artwork.

Maintain the detailed program exclusively on the wiki:

- [INCOSE IW OpenMBEE program](https://github.com/Open-MBEE/openmbee-workshops.github.io/wiki/INCOSE-IW-2027-OpenMBEE-Workshop)
- [Caltech workshop and JPL reception program](https://github.com/Open-MBEE/openmbee-workshops.github.io/wiki/OpenMBEE-Workshop-2027)

Edit HTML directly. Keep only brief keynote/activity highlights on the website; do not copy session-by-session schedules, draft timing tables, or pending agenda slots into the pages. There is no program JSON, template, or page-generation workflow.

Preserve the registration links inside the homepage event tiles and their existing wording. IW and Caltech have separate Google Forms, and the JPL reception requires its own registration for advance visitor checking. Check forms for current availability and requirements. Confirm fees, deadlines, access instructions, and any separate INCOSE registration requirements with the organizers before publishing policy claims. Form settings must be maintained separately.

The opening reception is February 3 at JPL; the Caltech workshop is February 4–5. Planned OpenMBEE IW sessions are January 30 and February 1, within the wider January 30–February 2 International Workshop. Consult the wiki for changes.

## Validation

Run `node --test tests/navigation.test.cjs` and `git diff --check`. Check local links, registration destinations, desktop/mobile navigation, keyboard focus, and page layout before publishing. The navigation tests exercise behavior with a simulated DOM; they do not replace browser or accessibility review.

Keep `CNAME`, `.nojekyll`, and the existing GitHub Pages configuration when publishing.

## Sponsors and community

`sponsors.html` is the single page for workshop support and community participation. It lists the five organizations carried over from the existing sponsors page, preserving the NumFOCUS sponsored-project note. Additional community categories say “To be announced” until participation is confirmed. Logo source URLs are recorded in `brand/partners/sources.json`.
