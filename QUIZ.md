# Quiz design (6 questions)

Every event carries tags: **format** (test / production / project / live), **judges** (yes/no), **team** (individual/team), **subjects** (one or more of 9), **prep** (low/medium/high), **level** (beginner/intermediate/advanced). Each answer option carries a points table per tag value (see `QUESTIONS` in template.html). Top 5 by score are shown; at most 2 virtual events; results scoring under 80% of the top pick are dropped once there are 3. Postsecondary-only events are hidden.

| # | Question | Options → points |
|---|---|---|
| 1 | Which of these sounds most like you? | Sit down and take a test → test +4, production +1 · Build something at a computer, on the clock → production +4, test +1 · Spend a few weeks making something, then show it off → project +4, live +1 · Get a scenario on the spot and present it → live +4, project +1 · Honestly, I'm not sure yet → 0 |
| 2 | Presenting in front of judges? | Love it → judges +3 · Nervous, but I'd do it → judges +1 · Fine either way → 0 · Hard pass → no-judges +3, judges −3 |
| 3 | Solo or team? | Solo → solo +3, team −3 · Team → team +3, solo −3 · Team, but only if I already have people → team +2 · Either → 0 |
| 4 | What are you into? (up to 3) | Money/investing/accounting · Business/management/office · Startups/pitching · Coding/networks/cyber · Games/animation/3D · Graphic design/video/photo/audio · Marketing/branding/social · Healthcare · Public speaking/interviews/career → +3 per matching subject |
| 5 | How much time before the conference? | Whatever it takes, I want to win → high +3, medium +1 · A solid few weekends → high +2, medium +2 · A few hours of studying or practicing → medium +3, low +1, high −2 · I'll study, but I don't want a whole project → low +2, medium +2, project-format −3 · Minimal, I'll wing it → low +3, medium −1, high −3 |
| 6 | Experience? | Total beginner → beginner +2, advanced −2 · Done some of this → intermediate +2 · Pretty good at this → intermediate +1, advanced +2 · Give me the hardest one → advanced +3, beginner −2 |

## Card depth
Each card has a "More about this event" section: what you actually make, what it's scored on, what a strong entry looks like, rough prep hours, and an examples list. Content lives in `details.py` (not from the PDF; summarized from how each event runs). `examples` is empty by default: add `{"title":..., "url":..., "note":...}` entries per event code to link your chapter's past entries.
