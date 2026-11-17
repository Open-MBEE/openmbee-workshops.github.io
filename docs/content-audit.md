# Content audit — November 17, 2026

Compared the branch with upstream `main` at `bfc85315baf57f5cacf70e9bd6b412152eb5f52d`. The GitHub API reported that same SHA as current `main` during this audit. Also read the live Caltech page, Caltech registration form, reception form, and both planning agendas.

Sources:

- [Original repository](https://github.com/Open-MBEE/openmbee-workshops.github.io/tree/bfc85315baf57f5cacf70e9bd6b412152eb5f52d)
- [Caltech program](https://workshops.openmbee.org/caltech-program.html)
- [Caltech planning agenda](https://github.com/Open-MBEE/openmbee-workshops.github.io/wiki/OpenMBEE-Workshop-2027)
- [IW planning agenda](https://github.com/Open-MBEE/openmbee-workshops.github.io/wiki/INCOSE-IW-2027-OpenMBEE-Workshop)
- [Caltech registration](https://forms.gle/PBHnLteSZcqWZSSEA)
- [JPL reception registration](https://forms.gle/hupXadCrkBWYFYsJ6)

## Verified preservation and additions

- All five sponsor names match the original: Caltech CTME, Planetary Utilities, Dynamical Systems Group, Cognition, and NumFOCUS. The NumFOCUS sponsored-project acknowledgement is retained.
- Nicholas LeGrand, Ed Seidewitz, and Adam Wade retain their original names and role descriptions. No new speakers or sponsors were added.
- All original external link destinations, including the three registration forms, are retained on their respective pages. Sponsor website links are additions verified in the earlier sponsor-link change.
- All 26 session dates and start/end time pairs in the structured Caltech data match the current draft wiki. TBA slots remain pending; the agenda explicitly warns that timings are provisional. Break and lunch entries describe draft schedule slots, not a promise of catering.
- The Caltech form lists February 4 and 5; the wiki places the reception at JPL on February 3. The IW draft lists January 30 and February 1; the wider IW dates remain January 30–February 2 as in the original website.
- Newcomer and practitioner audience wording is supported by the Caltech form's introduction. Activity descriptions paraphrase the original program and planning wiki, without adding a promised deliverable.
- Original focus areas, origins at ESO/JPL/NASA/Boeing, workshop history alongside the JPL MBSE Symposium, SysML/Python context, and community mission are retained. Copy is reorganized and shortened, not verbatim throughout.
- `CNAME`, `LICENSE`, `.nojekyll`, `brand/`, and original flyer assets are unchanged.

## Corrections made during audit

- Fixed the IW page's lingering “February 3–5 at Caltech” sentence to distinguish February 3 at JPL from February 4–5 at Caltech.
- Clarified that reception starts at 6:00 PM PST and Nicholas LeGrand's keynote at 6:30 PM PST.
- Restored community resource links removed during navigation simplification.
- Restored the four original workshop focus areas, named JPL venue, and shortened historical context.
- Changed logistics wording to distinguish information absent from this page from claims about what organizers have or have not finalized.

## Deliberate differences and limits

The original “registration and call for participation open” banner is replaced with a series heading. No new submission process or deadline was invented; a current call for participation needs organizer confirmation before being advertised.

The original calls the venue “JPL Van Karman”; that wording is retained as source-provided, not independently certified as the official venue spelling. The reception form says “Bon Karman”; the discrepancy is tracked in issue #17.

Fees, deadlines, access/eligibility rules, independent attendance, and any separate INCOSE registration requirement remain unconfirmed. No forms were submitted or edited during this audit. Source consistency checks do not constitute organizer approval or a visual/accessibility audit.

## Checks run

- Compared all 26 structured session date/time ranges with freshly retrieved wiki Markdown; verified every TBA slot remains pending.
- Checked original external URL preservation per page; exact sponsor names, acknowledgement, speaker roles, and focus areas; unchanged domain/license/assets.
- Checked local anchor IDs and references.
- `python3 scripts/render_event.py --check`
- `node --test tests/*.test.cjs` — seven tests passed.
- `git diff --check`
