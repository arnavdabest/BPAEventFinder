"""Builds index.html from events.json + details.py + template.html. Run: python3 build.py"""
import json
from details import D, TEST, PROD, OVERRIDE
ev = json.load(open("events.json"))
out = []
for e in ev:
    base = D.get(e["code"]) or dict(TEST if e["format"] == "test" else PROD, examples=[])
    base = dict(base); base.update(OVERRIDE.get(e["code"], {}))
    row = {k: e[k] for k in ("code","name","category","format","team","teamSize","division","description","prep")}
    row["detail"] = base
    row.update(json.load(open("pdf_cols.json")).get(e["code"], {}))
    out.append(row)
html = open("template.html").read().replace("/*EVENTS*/", json.dumps(out, ensure_ascii=False))
open("index.html", "w").write(html)
print("built index.html", len(html), "bytes,", len(out), "events")
