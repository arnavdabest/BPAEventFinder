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

# Security headers. The CSP only allows the exact inline script above (by hash), so injected scripts can't run.
import base64, hashlib, re
scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
hashes = " ".join("'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode()).digest()).decode() for s in scripts)
csp = "; ".join([
    "default-src 'self'",
    f"script-src 'self' {hashes}",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src https://fonts.gstatic.com",
    "img-src 'self' data:",
    "connect-src 'self'",
    "frame-ancestors 'none'",
    "base-uri 'none'",
    "form-action 'none'",
    "object-src 'none'",
    "upgrade-insecure-requests",
])
vercel = {
    "cleanUrls": True,
    "crons": [{"path": "/api/keepalive", "schedule": "0 12 * * *"}],
    "headers": [
        {"source": "/(.*)", "headers": [
            {"key": "Content-Security-Policy", "value": csp},
            {"key": "X-Frame-Options", "value": "DENY"},
            {"key": "X-Content-Type-Options", "value": "nosniff"},
            {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
            {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()"},
            {"key": "Cross-Origin-Opener-Policy", "value": "same-origin"},
            {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload"},
        ]},
        {"source": "/api/(.*)", "headers": [{"key": "Cache-Control", "value": "no-store"}]},
    ],
}
open("vercel.json", "w").write(json.dumps(vercel, indent=2) + "\n")
print("wrote vercel.json with", len(scripts), "script hash(es)")
