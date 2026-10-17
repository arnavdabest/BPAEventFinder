# BPA Event Matcher

A one-file quiz that recommends Business Professionals of America (BPA) competitive events. Students answer 10 quick questions and get 3–5 matched events with an explanation of why each fit, plus a browse-all list. No backend, no login, works on a phone.

**Live site:** enable GitHub Pages on this repo (Settings → Pages → Deploy from branch `main`, folder `/ (root)`) and it will be served at `https://arnavdabest.github.io/BPAEventFinder/`.

## How it works

- `index.html` is the whole app. Open it in any browser.
- Events come from the BPA Workplace Skills Assessment Program "Events at a Glance" table (Sept 2026 release). Each event is tagged with format, solo/team, subjects, prep level, experience level, whether you bring your own computer, and whether it has a certification component.
- Each quiz answer adds or subtracts points on events whose tags match. Results follow BPA entry rules: 2 main events with at least one solo, then alternates, then optional add-ons (virtual events and Open Concepts tests). Each card has a "why this matched you" line. Postsecondary-only events are hidden.
- Full question and scoring table: [QUIZ.md](QUIZ.md). Extracted event list with flags for rows to verify: [events.md](events.md).

## Editing

| What you want to change | Where |
|---|---|
| Event list, categories, descriptions | `build_events.py` (then run it to regenerate `events.json` / `events.md`) |
| "More about this event" text, prep hours, example links | `details.py` |
| Questions, answer options, point values | `QUESTIONS` in `template.html` |
| Styling and layout | `template.html` |

After any change, rebuild `index.html`:

```bash
python3 build.py
```

To add a link to a past entry on an event card, in `details.py`:

```python
D["430"]["examples"].append({"title": "2025 state 1st place video", "url": "https://...", "note": "2:10, shot on phones"})
```

## Caveats

- Descriptions, team sizes, and the "more about this event" content are summaries, not the official rubric. The official guidelines are behind the BPA member login at bpa.org.
- 11 events are flagged in `events.md` where the PDF was unclear (individual vs team, test vs hands-on).
