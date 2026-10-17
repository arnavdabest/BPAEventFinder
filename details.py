# Per-event depth shown under "More about this event". NOT from the PDF: written from the
# general shape of each BPA WSAP event. examples[] is for the chapter to fill with links to past entries.
D = {}
def d(code, make, look, strong, hours):
    D[code] = dict(make=make, look=look, strong=strong, hours=hours, examples=[])

# ---- Virtual ----
d("V01","A 1–3 minute promotional video or multimedia piece for a real client or cause set by BPA (a recent year used a local animal rescue), plus a short write-up of your process.","Clear message, clean editing, original footage/graphics, and citations for anything you didn't make yourself.","Looks like something the organization could actually post tomorrow: tight script, good audio, on-brand visuals, and a presenter who can explain every choice.","20–40 hours")
d("V02","Same deliverable as V01, split across a team: one person scripts, one shoots/edits, one handles graphics and the presentation.","Same as V01 plus how well the team divides work and presents together.","Every member speaks in the presentation and can answer judge questions about their part.","20–40 hours per person")
d("V03","A playable game built to that year's theme, with a design doc and a demo video, presented live online.","Does it run, is it fun, does it match the theme, and can you explain your design and code decisions?","A small polished game beats a big broken one. Winners usually have a clear core loop, a title screen, and no crashes during the demo.","40–80 hours")
d("V04","A working web app for a given scenario (think a booking system or inventory tool), with documentation and a live demo.","Functionality, usability, code quality, and that you can walk a judge through how it works.","A deployed link that works on a phone, real data validation, and a demo that doesn't rely on 'imagine this part works'.","40–80 hours")
d("V05","A mobile app prototype or build for a given scenario, demoed on-screen with a short design and testing write-up.","User experience, that the core features work, and your reasoning about who the user is.","Clean screens, a real flow from open to done, and evidence you tested it with actual people.","40–80 hours")
d("V06","A set of edited promotional photos for a given subject, with captions and a short explanation of technique.","Composition, lighting, editing restraint, and fit for the promotional purpose.","Consistent look across the set and a clear story about who the photos are for.","10–20 hours")
d("V07","Analysis of a provided cyber incident or forensic image: find what happened, document evidence, and present findings and recommendations.","Correct findings, a defensible method, a clear report, and sound recommendations.","A timeline of the attack, evidence for every claim, and plain-English recommendations a manager could act on.","20–40 hours")
d("V08","A full business plan for a new venture (market, product, financials) and a pitch to judges.","Feasibility, realistic numbers, market research, and how convincingly you pitch.","Real customer interviews or survey data, a believable first-year budget, and a pitch under time.","30–60 hours")
d("V09","An investment portfolio built for a described client, with your research and a strategy presentation.","Does the portfolio fit the client's goals and risk, is the reasoning sound, do you understand what you bought?","Clear risk reasoning, diversified holdings you can defend one by one, and a plan for what happens if markets drop.","20–40 hours")
d("V10","A brand identity package for a given organization: logo, colors, type, voice, and sample applications.","Originality, consistency, fit for the organization, and a clear rationale.","A one-page brand guide that someone else could follow, with mockups on real items (shirt, social post, sign).","20–40 hours")
d("V11","A short 2D animated piece on the year's theme, plus storyboard and process notes.","Storytelling, animation quality, sound, and originality.","Smooth motion, a beginning-middle-end in under 2 minutes, and original art.","40–80 hours")
d("V12","A social media campaign plan for a given organization: goals, audience, sample posts, calendar, and metrics.","Strategy fit, creative quality of the posts, and whether you measure the right things.","Platform-specific posts that look real, a posting calendar, and numbers for how you'd judge success.","20–40 hours")
d("V13","An esports-related project (event plan, team organization, or broadcast production) presented to judges.","Planning depth, budget realism, and production quality.","A complete event run-of-show with budget, sponsors, and a sample broadcast segment.","20–40 hours")
d("V14","Analysis of an ethical leadership scenario: your decision, the framework you used, and the impact on stakeholders.","Sound reasoning, awareness of all sides, and a clear presentation.","Names every stakeholder, weighs real tradeoffs, and lands on a decision you can defend under questioning.","10–20 hours")
d("V15","A digital portfolio (site or PDF) of your work and resume, then a virtual job interview with judges.","Professionalism, portfolio quality, and interview answers.","A clean portfolio site and practiced answers to the standard interview questions, with specific stories.","10–20 hours")
d("V16","An AI-based solution to a given problem: a working prototype or detailed design, with ethics and data considerations.","Does it solve the problem, is the AI use appropriate, and can you explain how it works and its limits?","A working demo, honest discussion of where it fails, and a clear data/ethics section.","40–80 hours")

# ---- Finance ----
d("150","A full financial analysis of a publicly traded company assigned ahead of time, delivered as a 30-minute team presentation.","Ratio analysis, trend interpretation, a recommendation, and depth in the 10-minute Q&A.","Reads like an analyst report: ratios vs. competitors, a clear buy/hold/sell call, and every member able to defend the numbers.","40–60 hours per team")
d("155","A research paper on a current economic topic and a 7-minute presentation to judges.","Research quality, correct economics, citations, and presentation.","Uses real data (FRED, BLS), explains cause and effect, and has a clean slide deck.","20–30 hours")
d("160","Same as 155, as a team paper and presentation.","Same as 155 plus teamwork in the presentation.","Everyone presents, one voice in the paper.","20–30 hours per person")

# ---- Business admin ----
d("230","A research report on an office/administrative topic (for example remote work policy) and a 7-minute presentation.","Research quality, document formatting, and presentation.","Properly formatted report using BPA style, with a practical recommendation.","15–25 hours")
d("240","A written business plan for your own venture idea and a 5–7 minute pitch to judges.","Feasibility, financials, market research, and your pitch.","A plan with real numbers and a pitch you could give to an actual investor without notes.","30–50 hours")
d("245","A small-business case handed to you at the conference, then a 30-minute strategy presentation with 10 minutes of questions.","Analysis, practical recommendations, and how the team handles tough questions.","Teams that practiced on past cases beforehand and have a structure (situation, options, recommendation, risks).","10–20 hours practicing cases")
d("250","A mock business meeting run under Robert's Rules of Order, judged on correctness and flow.","Correct procedure, handling of motions, and team coordination.","Teams that drill weekly; every member knows the motions cold.","30–60 hours of team practice")

# ---- IT ----
d("325","A network design for a given scenario, presented in 30 minutes with diagrams, equipment lists, costs, and security.","Technical soundness, cost realism, and clarity of the design.","Proper diagrams, a bill of materials with real prices, and a security section.","30–50 hours per team")
d("365","A complete website for a given client scenario, built before the conference and presented to judges.","Design, functionality, accessibility, and your process.","Mobile-friendly, fast, every link works, and a short demo that highlights the hardest part you built.","40–80 hours per team")

# ---- Design/media ----
d("410","A promotional graphic design piece (poster, logo set, or similar) for the year's theme, presented in 6 minutes.","Originality, print readiness, and design principles.","Print-ready files, a clear concept, and a rationale for every design choice.","15–30 hours")
d("420","A digital media production (video or interactive piece) on the theme, presented in 10 minutes.","Technical quality, creativity, and theme fit.","Original footage, clean audio, and a story.","20–40 hours")
d("425","3D models built to the theme, shown with renders and a short presentation.","Modeling quality, texturing, and process.","Multiple polished renders plus wireframes that prove you built it.","20–40 hours")
d("430","A short video on the theme, shot and edited by the team.","Story, camera work, editing, and audio.","Looks like something a real brand could use; everyone on the team had a clear job.","20–40 hours per person")
d("440","A 3D animated short on the theme.","Animation quality, story, and technical skill.","Smooth animation, rendered lighting, and a complete story under the time limit.","40–80 hours per person")
d("445","A broadcast news segment (anchors, packages, graphics) produced by the team.","Journalism quality, production value, and on-air presence.","A real newsroom feel: lower-thirds, b-roll, and interviews.","20–40 hours per person")
d("450","A podcast episode on the theme, with show notes.","Audio quality, content, structure, and editing.","Clean audio, a tight format, and a topic that's actually interesting.","15–30 hours per person")
d("455","A UX design for an app or site: research, wireframes, prototype, and testing results.","User research, usability, and design rationale.","Clickable prototype plus evidence from real user tests.","20–40 hours per person")
d("460","A visual design package (graphics, layouts, branding) for the theme.","Design principles, consistency, and creativity.","Consistent system across several pieces with a clear concept.","20–40 hours per person")

# ---- Marketing ----
d("500","A marketing plan to take a product into a foreign market, presented in 10 minutes.","Market research, cultural fit, and strategy.","Real country data, a pricing and channel plan, and a confident presentation.","20–40 hours per team")
d("505","A sports media marketing campaign for a given scenario.","Strategy, creative, and presentation.","Campaign creative that looks real plus a measurable plan.","20–40 hours per team")
d("510","A 7-minute pitch for a product or idea to judges acting as industry decision-makers.","Persuasiveness, business sense, and delivery.","Rehearsed to the second, with a demo or visual that makes the idea tangible.","15–30 hours per team")

# ---- Health ----
d("615","A research report on a current healthcare trend and a 7–10 minute presentation.","Research quality, accuracy, and presentation.","Cites real studies, explains why the trend matters, and has clean slides.","15–30 hours")

# ---- Career skills ----
d("725","Submit a resume and application, then a 15-minute mock job interview with judges.","Professionalism, answers, and how you present yourself.","Specific stories for every common question and a polished resume.","5–10 hours")
d("730","A higher-level mock interview for a professional role, 15 minutes with judges.","Same as 725 at a higher bar.","Industry-specific answers and confident follow-ups.","5–10 hours")
d("735","You draw a business topic, prep for 10 minutes, then give a 2–4 minute speech.","Organization, delivery, and content on the fly.","People who practice with random topics weekly; a simple structure (point, three reasons, close).","5–10 hours practicing")
d("745","You get an HR case on-site, prep 20 minutes, then present a solution (3–5 min) and answer questions.","Sound HR reasoning, legality, and clarity.","Knows the basics of employment law and gives a decision with a rationale.","5–15 hours")
d("750","You get an ethics case on-site, prep 20 minutes, then present your position (5–7 min) and answer questions.","Ethical reasoning, stakeholder awareness, and delivery.","Names the stakeholders, weighs options, and makes a clear call.","5–15 hours")
d("755","A 5–7 minute speech on a business/BPA-related topic, written and rehearsed in advance.","Content, organization, and delivery.","Memorized, timed, with one memorable story.","10–20 hours")
d("760","A 7–10 minute slide presentation on an assigned topic, with 5 minutes of judges' questions.","Content, slide design, delivery, and Q&A.","Clean slides, a confident delivery without reading, and prepared answers for likely questions.","10–20 hours")

# ---- Generic templates for tests / production events ----
TEST = dict(
 make="A timed multiple-choice (sometimes short-problem) test on this subject. No judges, no project.",
 look="Score on the test. Ties are rare but can be broken on specific sections.",
 strong="People who studied the event's topic outline from the guidelines and took a few practice tests.",
 hours="5–15 hours of studying")
PROD = dict(
 make="A hands-on test at a computer: you are given tasks or a spec and produce the actual files in the time limit.",
 look="Accuracy, correct formatting to the spec, and finishing the tasks.",
 strong="People who practiced with past-year style tasks and know the software's shortcuts.",
 hours="10–25 hours of practice")
OVERRIDE = {
 "100": dict(make="A 90-minute test with accounting problems: journal entries, ledgers, and a basic financial statement."),
 "110": dict(make="A 90-minute test with harder accounting problems: adjustments, depreciation, corporate transactions."),
 "125": dict(make="A 60-minute test calculating wages, overtime, withholdings, and payroll records."),
 "165": dict(make="A 60-minute test on real-life money: budgets, credit, loans, insurance, taxes, investing basics.", hours="3–8 hours of studying"),
 "600": dict(make="A 60-minute test assigning ICD-10 and CPT codes to medical scenarios.", strong="People who worked through a coding workbook; you need the code books or reference allowed."),
 "330": dict(make="Write a working C# program to a given spec in 90 minutes, on a computer."),
 "335": dict(make="Write a working C++ program to a given spec in 90 minutes, on a computer."),
 "340": dict(make="Write a working Java program to a given spec in 90 minutes, on a computer."),
 "355": dict(make="Write a working Python program to a given spec in 90 minutes, on a computer."),
 "360": dict(make="Hand-code a web page in HTML and CSS to a given spec in 90 minutes."),
 "225": dict(make="As a team, split a packet of office tasks (letters, spreadsheets, reports) and produce them in 90 minutes.", hours="10–25 hours of team practice"),
}
