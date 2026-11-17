#!/usr/bin/env python3
"""Generate the static Caltech event page. Standard library only."""
import argparse
import json
from datetime import datetime
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def h(value):
    return escape(str(value), quote=True)

def time_label(value):
    return datetime.strptime(value, '%H:%M').strftime('%I:%M %p').lstrip('0')

def render(event):
    speakers = event['speakers']
    venues = event['venues']
    def register(option):
        if option['status'] != 'open':
            return '<p>Registration ' + h(option['status']) + '</p>'
        return f'<a class="event-button" href="{h(option["url"])}" target="_blank" rel="noopener noreferrer">Register for the {"workshop" if option["id"] == "workshop" else "JPL reception"}</a>'
    options = ''.join(f'<article class="registration-option"><p class="event-kicker">{h(o["dates"])}</p><h3>{h(o["title"])}</h3><p>{h(o["description"])}</p>{register(o)}<p class="event-note">{h(o["relationship"])}</p></article>' for o in event['registrationOptions'])
    speaker_html = ''.join(f'<article class="speaker"><span class="speaker-initials" aria-hidden="true">{h(s["initials"])}</span><div><p class="event-kicker">{h(s["date"])}</p><h3>{h(s["name"])}</h3><p>{h(s["role"])}</p></div></article>' for s in speakers.values())
    days, links = [], []
    for day in event['days']:
        ident = 'day-' + day['date']
        links.append(f'<a href="#{ident}">{h(day["short"])}</a>')
        rows = []
        for session in (s for s in event['sessions'] if s['date'] == day['date']):
            names = ' · '.join(speakers[s]['name'] for s in session['speakerIds'])
            detail = f'<p class="session-meta">{h(names + " · " if names else "")}{h(venues[session["venueId"]]["name"])}</p>'
            if session.get('description'):
                detail += f'<details class="session-details"><summary>About this activity</summary><p>{h(session["description"])}</p></details>'
            status = 'Topic pending · draft slot' if session['status'] == 'tba' else 'Draft timing' if session['status'] == 'tentative' else 'Published session · draft timing'
            rows.append(f'<li class="agenda-row {"agenda-pending" if session["status"] == "tba" else ""}"><div class="session-time"><time datetime="{h(session["date"])}T{h(session["startTime"])}:00-08:00">{time_label(session["startTime"])}</time><span>– {time_label(session["endTime"])}</span></div><div class="session-content"><span class="session-type">{h(session["type"].capitalize())}</span><h4>{h(session["title"])}</h4>{detail}<p class="session-status">{status}</p></div></li>')
        days.append(f'<section class="agenda-day" id="{ident}" aria-labelledby="{ident}-heading"><h3 id="{ident}-heading">{h(day["label"])}</h3><p class="event-note">{h(venues[day["venueId"]]["name"])} · All times PST</p><ol class="agenda-list">{"".join(rows)}</ol></section>')
    return f'''<main class="event-shell" id="main-content">
<header class="event-hero"><div><p class="event-kicker">OpenMBEE Workshop 2027 · In person</p><h1>{h(event['theme'])}</h1><p class="event-subtitle">{h(event['title'])}</p><p class="event-lede">Join systems engineers, researchers, and open-source developers for keynotes, technical demonstrations, collaborative discussions, and hands-on modeling.</p><dl class="event-facts"><div><dt>Workshop</dt><dd>February 4–5 · Caltech, Pasadena</dd></div><div><dt>Opening evening</dt><dd>February 3 · JPL</dd></div><div><dt>Time zone</dt><dd>Pacific Standard Time (UTC−8)</dd></div></dl><nav class="event-sections" aria-label="On this page"><a href="#overview">Overview</a><a href="#speakers">Speakers</a><a href="#agenda">Agenda</a><a href="#attend">Attend</a></nav></div><aside class="hero-registration" aria-labelledby="registration-title"><h2 id="registration-title">Join the workshop</h2><p>Two forms. Choose the activities you plan to attend.</p>{''.join(f'<div class="hero-option"><h3>{h(o["title"])}</h3><p>{h(o["dates"])}</p>{register(o)}</div>' for o in event['registrationOptions'])}<p class="event-note">Registration opens in Google Forms. The reception requires separate registration and advance visitor checking.</p></aside></header>
<section class="event-section" id="overview"><h2>What to expect</h2><p class="event-lede">New to SysML v2, applying it in your work, or building open-source tools? Bring your questions and experience to the conversation.</p><dl class="expect-list"><div><dt>Keynotes & talks</dt><dd>Perspectives on SysML v2 and open-source systems engineering.</dd></div><div><dt>Technical demos</dt><dd>Projects, implementations, and modeling practices.</dd></div><div><dt>Open Space</dt><dd>Participant-led topics and collaborative discussions.</dd></div><div><dt>Hackathon</dt><dd>Hands-on collaboration and shared community outcomes.</dd></div></dl></section>
<section class="event-section" id="speakers"><p class="event-kicker">Published keynote program</p><h2>Featured speakers</h2><div class="speaker-grid">{speaker_html}</div></section>
<section class="event-section" id="agenda"><div class="section-heading"><h2>Workshop agenda</h2><span class="program-status">Program evolving</span></div><p class="agenda-intro">Browse the program by day. Keynote speakers and community activities appear in the published program; detailed timings come from the draft planning agenda and may change. Unannounced talks are marked as pending.</p><nav class="day-links" aria-label="Jump to an agenda day">{''.join(links)}</nav><div id="agenda-controls" class="agenda-controls" hidden><span class="event-note">Show a day</span>{''.join(f'<button type="button" data-day="day-{h(d["date"])}" aria-controls="day-{h(d["date"])}" aria-pressed="false">{h(d["short"])}</button>' for d in event['days'])}<button type="button" data-day="all" aria-pressed="true">All days</button><p class="sr-only" id="agenda-announcement" role="status" aria-live="polite"></p></div>{''.join(days)}<p class="planning-link">Technical session topics and speakers are still being finalized. <a href="{h(event['sources']['planning'])}" target="_blank" rel="noopener noreferrer">View the full draft planning agenda →</a></p></section>
<section class="event-section" id="participate"><h2>Take part in the community</h2><div class="participation-grid"><article><h3>Open Space</h3><p>Propose a topic, join a discussion, and share what your group explored.</p></article><article><h3>Fishbowl discussion</h3><p>Listen to the conversation and join in as perspectives and questions develop.</p></article><article><h3>Hackathon</h3><p>Work with other participants and share outcomes in the closing outbrief. Activity details are still being developed.</p></article></div></section>
<section class="event-section" id="attend"><h2>Attend and participate</h2><p>Register for the Caltech workshop and, if you plan to join the opening evening, complete the separate JPL reception form.</p><div class="registration-grid">{options}</div></section>
<section class="event-section event-resources" id="resources"><h2>Plan your visit</h2><details><summary>Where are the activities?</summary><p>The February 4–5 workshop is at Caltech in Pasadena, California. The February 3 reception and opening keynote are at JPL. Detailed arrival, room, parking, and access information is still to be announced.</p></details><details><summary>What do I need for the JPL reception?</summary><p>Complete the separate reception registration form. Advance visitor checking is required; consult the form for the information requested. Access deadlines and detailed arrival instructions are still to be announced.</p></details><details><summary>What should I prepare?</summary><p>Participants with different levels of SysML v2 experience are welcome. Laptop, software setup, and activity prerequisites are still to be announced.</p></details><details><summary>What is still being finalized?</summary><p>Technical session topics, fees, registration deadlines, attendance policies, and travel logistics need organizer confirmation. Check the program and registration forms for updates before making arrangements.</p></details><details><summary>How does this relate to INCOSE IW?</summary><p>The workshop follows INCOSE IW in Torrance. <a href="iw-workshop.html">Explore the OpenMBEE IW sessions</a>. Whether separate INCOSE registration is required, and policies for attending the Caltech workshop or reception independently, need organizer confirmation.</p></details><ul class="resource-links"><li><a href="{h(event['sources']['planning'])}">Workshop planning wiki</a></li><li><a href="https://github.com/Open-MBEE">OpenMBEE on GitHub</a></li><li><a href="https://openmbee.org">OpenMBEE community</a></li></ul></section>
<footer class="event-footer"><a href="index.html">All OpenMBEE workshop events →</a><p>Program sources checked {h(event['sources']['checked'])}. Schedule subject to change.</p></footer></main>'''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if generated HTML is stale')
    args = parser.parse_args()
    event = json.loads((ROOT / 'data/caltech-2027.json').read_text())
    result = (ROOT / 'templates/caltech-program.html').read_text().replace('<!-- EVENT_CONTENT -->', render(event))
    output = ROOT / 'caltech-program.html'
    if args.check:
        if output.read_text() != result:
            raise SystemExit('Generated page is stale: run python3 scripts/render_event.py')
        print('Generated event page is up to date')
    else:
        output.write_text(result)
        print('Generated caltech-program.html')

if __name__ == '__main__':
    main()
