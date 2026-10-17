import json

# format keys:
#  test        = objective test (multiple choice / problems), no judges
#  production  = hands-on computer skills test at the conference (build a document/sheet/program), no judges
#  project     = pre-submitted project/portfolio + judged presentation with Q&A
#  live        = live judged event, little or no pre-work (case study, speech, interview)
# team: "individual" | "team"
# prep: how much work before the conference: low | medium | high
# division: S | PS | S|PS   (S = secondary/high school, PS = postsecondary)
# NOTE: description and teamSize are NOT in the PDF (it is a summary grid) -> from BPA WSAP knowledge, see flags.

E = []
def ev(code, name, cat, fmt, team, desc, prep, div="S|PS", size=None, flags=None, pres=None, judges=None):
    E.append(dict(code=code, name=name, category=cat, format=fmt, team=team,
                  teamSize=size, division=div, description=desc, prep=prep,
                  presentationMins=pres, judgesQMins=judges, flags=flags or []))

TEAM = "2–4 (typical BPA team size; not stated in PDF)"
V = "Virtual Events"
# ---------- Virtual ----------
ev("V01","Virtual Multimedia and Promotion Individual",V,"project","individual","Create a digital multimedia promotion (video/graphics/web) for a given topic and present it to judges online.","high",pres=10,judges=5)
ev("V02","Virtual Multimedia and Promotion Team",V,"project","team","Same as V01 but as a team: build a multimedia promotional package and present it online.","high",size=TEAM,pres=10,judges=5)
ev("V03","Virtual Game Development Team",V,"project","team","Design and build a playable game, then demo and defend it to judges online.","high",size=TEAM,pres=10,judges=5)
ev("V04","Virtual Web Application Team",V,"project","team","Build a working web application for a given scenario and present it online.","high",size=TEAM,pres=10,judges=5)
ev("V05","Virtual Mobile Applications",V,"project","team","Design and build a mobile app for a given scenario and present it online.","high",size=TEAM,pres=10,judges=5,flags=["PDF name has no 'Team'/'Individual' suffix; usually run as a team event – confirm"])
ev("V06","Virtual Promotional Photography",V,"project","individual","Shoot and edit a set of promotional photos for a given topic and present them online.","medium",pres=7,judges=5,flags=["PDF does not say individual vs team; assumed individual"])
ev("V07","Virtual Cybersecurity/Digital Forensics",V,"project","team","Investigate a simulated cyber incident, document findings, and present them online.","high",size=TEAM,pres=10,judges=5,flags=["PDF does not say individual vs team; assumed team"])
ev("V08","Virtual Start-up Enterprise Team",V,"project","team","Develop a business plan for a new start-up and pitch it to judges online.","high",size=TEAM,pres=10,judges=5)
ev("V09","Virtual Financial Portfolio Management Team",V,"project","team","Research and build an investment portfolio for a given client scenario and present your strategy online.","high",size=TEAM,pres=10,judges=5)
ev("V10","Virtual Branding Team",V,"project","team","Create a brand identity (logo, voice, guidelines) for a given organization and present it online.","high",size=TEAM,pres=10,judges=5)
ev("V11","Virtual 2D Animation Team",V,"project","team","Produce a short 2D animated piece on a given topic and present it online.","high",size=TEAM,pres=10,judges=5)
ev("V12","Virtual Social Media Marketing Campaign Team",V,"project","team","Plan and build a social media campaign for a given topic and present it online.","high",size=TEAM,pres=10,judges=5)
ev("V13","Virtual Esports Team",V,"project","team","Plan and run an esports event/organization project (management, marketing, production) and present it online.","high",size=TEAM,pres=10,judges=5,flags=["Exact deliverable not in PDF – confirm what the team submits"])
ev("V14","Virtual Ethical Leadership & Decision-Making Team",V,"project","team","Analyze an ethical leadership scenario, document your decision process, and present it online.","medium",size=TEAM,pres=10,judges=5)
ev("V15","Virtual Interview & Digital Portfolio Design",V,"project","individual","Build a digital career portfolio and complete a virtual job interview with judges.","medium",pres=10,judges=5)
ev("V16","Virtual Artificial Intelligence Team",V,"project","team","Design an AI-based solution for a given problem and present it online.","high",size=TEAM,pres=10,judges=5)

# ---------- Financial Services ----------
F = "Finance"
ev("100","Fundamental Accounting",F,"test","individual","Take a 90-minute test on beginning accounting: journal entries, ledgers, and basic financial statements.","medium",div="S",pres=90)
ev("105","College Accounting",F,"test","individual","College-level accounting test (postsecondary only).","medium",div="PS",pres=90)
ev("110","Advanced Accounting",F,"test","individual","Take a 90-minute test on advanced accounting topics like adjusting entries, depreciation, and corporate accounting.","medium",div="S",pres=90)
ev("115","Advanced College Accounting",F,"test","individual","Advanced college accounting test (postsecondary only).","medium",div="PS",pres=90)
ev("125","Payroll Accounting",F,"test","individual","Take a 60-minute test on calculating wages, withholdings, and payroll records.","medium",pres=60)
ev("135","Managerial Accounting",F,"test","individual","Managerial/cost accounting test (postsecondary only).","medium",div="PS",pres=90)
ev("145","Banking and Finance",F,"test","individual","Take a 60-minute test on how banks, credit, loans, and financial institutions work.","low",pres=60)
ev("150","Financial Analyst Team",F,"project","team","Analyze a real company's financials as a team and give a 30-minute presentation with 10 minutes of judges' questions.","high",size=TEAM,pres=30,judges=10)
ev("155","Economic Trends Research Individual",F,"project","individual","Research a current economic topic, write a report, and present it to judges.","high",div="S",pres=7,judges=5)
ev("160","Economic Trends Research Team",F,"project","team","Same as 155 but as a team: research an economic topic and present findings.","high",div="S",size=TEAM,pres=7,judges=5)
ev("165","Personal Financial Management",F,"test","individual","Take a 60-minute test on budgeting, saving, credit, insurance, and investing for your own life.","low",pres=60)
ev("190","Financial Services Concepts (Open)",F,"test","individual","Open-entry 60-minute general finance concepts test, no entry limit.","low",pres=60)

# ---------- Management & Entrepreneurship ----------
M = "Business Admin & Management"
ev("200","Integrated Office Applications",M,"production","individual","At a computer, complete a 90-minute set of tasks that combine Word, Excel, and other Office apps.","medium",pres=90)
ev("205","Fundamental Spreadsheet Applications",M,"production","individual","At a computer, build spreadsheets with basic formulas and formatting in 90 minutes.","medium",pres=90)
ev("210","Advanced Spreadsheet Applications",M,"production","individual","At a computer, build spreadsheets using advanced functions, charts, and data tools in 90 minutes.","medium",pres=90)
ev("215","Database Applications",M,"production","individual","At a computer, create tables, queries, forms, and reports in a database program in 90 minutes.","medium",pres=90)
ev("220","Legal Office Procedures",M,"production","individual","Complete legal-office tasks (documents, terminology, procedures) in a 60-minute test.","medium",pres=60,flags=["Could be objective test or production; PDF only shows 10/10 setup + 60 min"])
ev("225","Administrative Support Team",M,"production","team","As a team, split up and produce a set of office documents (letters, reports, spreadsheets) in 90 minutes.","medium",size=TEAM,pres=90)
ev("230","Admin. Support Research Project",M,"project","individual","Research an office/administrative topic, write a report, and present it to judges.","high",div="S",pres=7,judges=5,flags=["PDF does not say individual vs team; assumed individual"])
ev("235","Business Law and Ethics",M,"test","individual","Take a 60-minute test on contracts, business law basics, and ethical issues.","low",pres=60)
ev("240","Entrepreneurship",M,"project","individual","Write a business plan for your own venture and pitch it to judges in 5–7 minutes.","high",pres=7,judges=5)
ev("245","Small Business Strategy Team",M,"live","team","Receive a small-business case at the conference, then as a team present a strategy for 30 minutes with 10 minutes of questions.","medium",size=TEAM,pres=30,judges=10,flags=["Assumed case given on-site; PDF shows 5-min setup and no pre-submission columns"])
ev("250","Parliamentary Procedure Team",M,"live","team","Run a mock business meeting using Robert's Rules of Order in front of judges.","high",div="S",size="5–8 (typical for this event; not stated in PDF)",pres=15,judges=5)
ev("290","Management & Entrepreneurship Concepts",M,"test","individual","Open-entry 60-minute test on general management and entrepreneurship concepts.","low",pres=60)
ev("291","Parliamentary Procedure Concepts",M,"test","individual","Open-entry 60-minute test on parliamentary procedure rules.","low",pres=60)
ev("292","Project Management Concepts",M,"test","individual","Open-entry 60-minute test on how projects are planned, scheduled, and managed.","low",pres=60)
ev("293","Meeting and Event Planning Concepts",M,"test","individual","Open-entry 60-minute test on planning meetings and events.","low",pres=60)

# ---------- Digital Technology ----------
T = "IT & Computer Science"
ev("300","Computer Network Technology",T,"test","individual","Take a 60-minute test on how networks, cabling, and protocols work (CompTIA Network+ style).","medium",pres=60)
ev("305","Device Configuration and Troubleshooting",T,"test","individual","Take a 60-minute test on setting up and fixing PCs and devices (CompTIA A+ style).","medium",pres=60)
ev("310","Server Administration Using Microsoft®",T,"test","individual","Take a 60-minute test on managing Windows servers.","medium",pres=60)
ev("315","Network Administration Using Cisco®",T,"test","individual","Take a 60-minute test on configuring and managing Cisco network gear.","medium",pres=60)
ev("320","Computer Security",T,"test","individual","Take a 60-minute test on cybersecurity concepts, threats, and defenses.","medium",pres=60)
ev("325","Network Design Team",T,"project","team","As a team, design a network for a given scenario and present it to judges for 30 minutes with 10 minutes of questions.","high",size=TEAM,pres=30,judges=10,flags=["PDF unclear whether scenario is pre-released or given on-site"])
ev("330","C# Programming",T,"production","individual","At a computer, write a working C# program to a given spec in 90 minutes.","medium",pres=90)
ev("335","C++ Programming",T,"production","individual","At a computer, write a working C++ program to a given spec in 90 minutes.","medium",pres=90)
ev("340","Java Programming",T,"production","individual","At a computer, write a working Java program to a given spec in 90 minutes.","medium",pres=90)
ev("345","SQL Database Fundamentals",T,"test","individual","Take a 60-minute test on SQL queries and relational database basics.","medium",pres=60)
ev("350","Linux Operating System Fundamentals",T,"test","individual","Take a 60-minute test on Linux commands, files, and system basics.","medium",pres=60)
ev("355","Python Programming",T,"production","individual","At a computer, write a working Python program to a given spec in 90 minutes.","medium",pres=90)
ev("360","HTML and CSS Coding",T,"production","individual","At a computer, hand-code a web page with HTML and CSS to a given spec in 90 minutes.","medium",pres=90)
ev("365","Website Design and Development Team",T,"project","team","Build a full website for a given client scenario ahead of time, then present it to judges.","high",size=TEAM,pres=10,judges=5)
ev("390","Digital Technology Concepts (Open)",T,"test","individual","Open-entry 60-minute test on general IT concepts.","low",pres=60)
ev("391","Computer Programming Concepts (Open)",T,"test","individual","Open-entry 60-minute test on general programming concepts (no coding).","low",pres=60)

# ---------- Arts, Entertainment & Design ----------
D = "Digital Media & Design"
ev("400","Fundamental Desktop Publishing",D,"production","individual","At a computer, lay out a flyer/newsletter-style document to spec in 90 minutes.","medium",pres=90)
ev("405","Advanced Desktop Publishing",D,"production","individual","At a computer, produce a more complex multi-page publication to spec in 90 minutes.","medium",pres=90)
ev("410","Graphic Design Promotion",D,"project","individual","Design a promotional graphic (poster/logo set) for a given topic ahead of time and present it to judges.","high",pres=6,judges=5)
ev("420","Digital Media Production",D,"project","individual","Produce a digital media piece (video/interactive) on a given topic and present it to judges.","high",pres=10,judges=5)
ev("425","3D Computer Modeling",D,"project","individual","Build 3D models for a given topic ahead of time and present them to judges.","high",div="S",pres=6,judges=5)
ev("430","Video Production Team",D,"project","team","As a team, shoot and edit a video on a given topic and present it to judges.","high",size=TEAM,pres=6,judges=5)
ev("440","3D Computer Animation Team",D,"project","team","As a team, create a 3D animated short on a given topic and present it to judges.","high",div="S",size=TEAM,pres=6,judges=5)
ev("445","Broadcast News Production Team",D,"project","team","As a team, produce a news broadcast segment and present it to judges.","high",size=TEAM,pres=6,judges=5)
ev("450","Podcast Production Team",D,"project","team","As a team, record and edit a podcast episode on a given topic and present it to judges.","high",size=TEAM,pres=6,judges=5)
ev("455","User Experience Design Team",D,"project","team","As a team, design the user experience/interface for an app or site and present it to judges.","high",size=TEAM,pres=6,judges=5)
ev("460","Visual Design Team",D,"project","team","As a team, create a visual design package (graphics/branding) and present it to judges.","high",size=TEAM,pres=6,judges=5)
ev("490","Arts, Communication, & Design Concepts (Open)",D,"test","individual","Open-entry 60-minute test on design, media, and communication concepts.","low",pres=60)

# ---------- Marketing & Sales ----------
K = "Marketing & Sales"
ev("500","Global Marketing Strategy Team",K,"project","team","As a team, build a marketing plan to take a product into a foreign market and present it to judges.","high",div="S",size=TEAM,pres=10,judges=5)
ev("505","Sports Media Marketing Team",K,"project","team","As a team, create a sports marketing/media campaign and present it to judges.","high",size=TEAM,pres=10,judges=5)
ev("510","Industry Pitch Team",K,"project","team","As a team, develop and deliver a 7-minute pitch for a product or idea to judges.","high",size=TEAM,pres=7,judges=5)
ev("590","Marketing & Sales Concepts (Open)",K,"test","individual","Open-entry 60-minute test on marketing and sales concepts.","low",pres=60)

# ---------- Healthcare & Human Services ----------
H = "Health Administration"
ev("600","Medical Coding",H,"test","individual","Take a 60-minute test assigning diagnosis/procedure codes (ICD/CPT) to medical scenarios.","medium",pres=60)
ev("605","Health Insurance and Medical Billing",H,"test","individual","Take a 60-minute test on insurance claims, billing, and reimbursement.","medium",pres=60)
ev("610","Health Administration Procedures",H,"test","individual","Take a 60-minute test on running a medical office: records, scheduling, regulations.","medium",pres=60)
ev("615","Health Trends Research Presentation",H,"project","individual","Research a current healthcare trend, write a report, and present it to judges.","high",pres=10,judges=5,flags=["PDF does not say individual vs team; assumed individual"])
ev("690","Healthcare & Human Services Concepts",H,"test","individual","Open-entry 60-minute test on healthcare and human services concepts.","low",pres=60)

# ---------- Career Ready Skills ----------
C = "Communication & Career Skills"
ev("700","Fundamental Word Processing",C,"production","individual","At a computer, type and format basic business documents (letters, memos) in 60 minutes.","low",pres=60)
ev("705","Intermediate Word Processing",C,"production","individual","At a computer, format more complex documents (tables, reports) in 60 minutes.","medium",pres=60)
ev("710","Advanced Word Processing",C,"production","individual","At a computer, produce advanced multi-part business documents in 90 minutes.","medium",pres=90)
ev("715","Essential Workplace Skills",C,"test","individual","Take a 90-minute test on basic workplace skills: communication, teamwork, professionalism.","low",pres=90,flags=["10/10 setup suggests computer-based; could include production tasks"])
ev("720","Advanced Workplace Skills",C,"test","individual","Take a 90-minute test on advanced workplace scenarios and professional judgment.","low",pres=90,flags=["10/10 setup suggests computer-based; could include production tasks"])
ev("725","Interview Skills",C,"live","individual","Submit a resume/application, then do a 15-minute mock job interview with judges.","low",judges=15)
ev("730","Advanced Interview Skills",C,"live","individual","Higher-level mock interview (15 minutes with judges) for a professional-level position.","low",judges=15)
ev("735","Extemporaneous Speech",C,"live","individual","Get a business topic on the spot, prep for 10 minutes, then give a 2–4 minute speech.","low",div="S",pres=4)
ev("740","Contemporary Issues",C,"live","individual","Postsecondary only: prep 10 minutes, then speak on a current issue for 3–5 minutes.","low",div="PS",pres=5)
ev("745","Human Resource Management",C,"live","individual","Get an HR case on-site, prep 20 minutes, then present your solution (3–5 min) and answer judges' questions.","low",pres=5,judges=3)
ev("750","Ethics and Professionalism",C,"live","individual","Get an ethics case on-site, prep 20 minutes, then present your position (5–7 min) and answer judges' questions.","low",pres=7,judges=3)
ev("755","Prepared Speech",C,"project","individual","Write a 5–7 minute speech on a business/BPA topic ahead of time and deliver it to judges.","medium",pres=7)
ev("760","Presentation Individual",C,"project","individual","Prepare a 7–10 minute slideshow presentation on a given topic and deliver it with judges' questions.","medium",pres=10,judges=5)
ev("790","Career Ready Skills Concepts",C,"test","individual","Open-entry 60-minute test on general career-readiness concepts.","low",pres=60)

json.dump(E, open("events.json","w"), indent=1)

FMT = {"test":"Objective test","production":"Hands-on computer test","project":"Pre-submitted project + judged presentation","live":"Live judged (on-site prep)"}
lines = ["# BPA Events – extracted list", "",
 "Source: Events-at-a-Glance.pdf (WSAP Initial Release 1.0, Sept 2026). The PDF is a summary grid only: it gives times, judges' Q&A, division and entry limits. **Descriptions and team sizes are NOT in the PDF** and come from general BPA knowledge – treat them as drafts.", "",
 "Format key: Objective test = sit a test, no judges. Hands-on computer test = build something at a computer during the conference, no judges. Pre-submitted project = build it before the conference, then present to judges. Live judged = little/no pre-work, you perform on-site.", "",
 "Division: S = high school only, PS = postsecondary only, S|PS = both.", ""]
cat=None
for e in E:
    if e["category"]!=cat:
        cat=e["category"]; lines += ["", f"## {cat}", "", "| # | Event | Format | Solo/Team | Div | Prep | What you do | Flags |", "|---|---|---|---|---|---|---|---|"]
    team = "Team" + (f" ({e['teamSize'].split(' ')[0]})" if e["teamSize"] else "") if e["team"]=="team" else "Solo"
    lines.append(f"| {e['code']} | {e['name']} | {FMT[e['format']]} | {team} | {e['division']} | {e['prep']} | {e['description']} | {'; '.join(e['flags'])} |")
open("events.md","w").write("\n".join(lines)+"\n")
print(len(E), "events")
from collections import Counter
print(Counter(e["format"] for e in E)); print(Counter(e["team"] for e in E)); print(Counter(e["division"] for e in E))
print(sum(1 for e in E if e["flags"]), "flagged")
