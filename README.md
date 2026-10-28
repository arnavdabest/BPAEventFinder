# BPA Event Matcher

A one-file quiz that recommends Business Professionals of America (BPA) competitive events. Students answer 10 quick questions and get 3–5 matched events with an explanation of why each fit, plus a browse-all list. No backend, no login, works on a phone.

**Live site:** https://bpaeventfinder.vercel.app (Vercel Hobby, free) with anonymous analytics in Supabase (free tier).

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

## Hosting and analytics ($0)

- **Vercel** serves the static site and two serverless functions in `api/`:
  - `api/track.js` receives batched events from the page and writes them to Supabase. Env vars: `SUPABASE_URL`, `SUPABASE_KEY` (the publishable key).
  - `api/forget.js` powers "Delete my data" on `/privacy`.
  - `api/keepalive.js` runs once a day (Vercel Cron, protected by `CRON_SECRET`): keeps the free Supabase project awake and deletes data older than 2 years.
- **Supabase** stores the data. Run `supabase/schema.sql`, then `supabase/hardening.sql`, in the SQL Editor. RLS lets the public key insert rows but never read them, so the data is only visible in your Supabase dashboard.
- The page doesn't send anything when opened as a local file, when the browser sends Global Privacy Control or Do Not Track, or after the visitor opts out on `/privacy`.
- Legal pages: `privacy.html`, `terms.html`, `support.html` (support goes to GitHub Issues).

### Security

- `build.py` writes `vercel.json` with a Content-Security-Policy that only allows the page's own script (by hash), plus anti-framing and other headers. Always rebuild before deploying.
- `api/_guard.js`: POST only, same-origin only, per-IP rate limit, strict input validation and size caps.
- Database (`hardening.sql`): the public key can only insert; rows can't be read, changed, or deleted from outside the dashboard. Only known event types and small payloads are accepted, and each session is capped at 400 events.

### What gets tracked

| Type | Data |
|---|---|
| `session_start` | visit number, referrer, UTM tags, timezone, language, device, OS, browser, screen/viewport size, dark mode, touch; country + state from Vercel's edge |
| `question_view` / `answer` | every question shown and answered, the answer text, ms spent, whether it changed and from what |
| `option_toggle` | each multi-select click in order, including trying to pick more than the max |
| `back`, `home_click`, `start_over`, `page_hidden` | where people back up or leave the quiz |
| `quiz_complete` | all answers as text, interests, classes, the main / alternate / add-on picks with scores and "why", top 10 scores, total time |
| `detail_open` / `detail_close` | which event cards people open, from where (results or browse-all), and how long they read |
| `link_click`, `browse_all` | outbound links and browse-all usage |

No names, emails, or IP addresses are stored. Ready-made views: `v_completed_quizzes`, `v_interest_popularity`, `v_answer_breakdown`, `v_funnel`, `v_question_time`, `v_recommended_events`, `v_event_interest`, `v_daily`, `v_traffic_sources`.

## Caveats

- Descriptions, team sizes, and the "more about this event" content are summaries, not the official rubric. The official guidelines are behind the BPA member login at bpa.org.
- 11 events are flagged in `events.md` where the PDF was unclear (individual vs team, test vs hands-on).
