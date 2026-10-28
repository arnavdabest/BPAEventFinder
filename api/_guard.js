// Shared checks for the public API endpoints. Files starting with "_" are not routes on Vercel.

const ALLOWED_ORIGINS = new Set(["https://bpaeventfinder.vercel.app", "http://localhost:4110"]);
const WINDOW_MS = 60_000;
const hits = new Map(); // ip -> [count, windowStart]. Memory only, never stored.

function clientIp(req) {
  return String(req.headers["x-forwarded-for"] || req.socket?.remoteAddress || "").split(",")[0].trim();
}

// Best-effort per-IP rate limit (per warm function instance).
function rateLimited(req, max) {
  const ip = clientIp(req), now = Date.now();
  const h = hits.get(ip);
  if (!h || now - h[1] > WINDOW_MS) { hits.set(ip, [1, now]); }
  else if (++h[0] > max) return true;
  if (hits.size > 5000) for (const [k, v] of hits) if (now - v[1] > WINDOW_MS) hits.delete(k);
  return false;
}

// Rejects requests coming from other websites. (A script can still fake these headers,
// which is why the database also enforces its own limits.)
function badOrigin(req) {
  const origin = req.headers.origin;
  if (origin && !ALLOWED_ORIGINS.has(origin)) return true;
  const site = req.headers["sec-fetch-site"];
  return !!site && site !== "same-origin";
}

function guard(req, res, maxPerMinute) {
  res.setHeader("Cache-Control", "no-store");
  if (req.method !== "POST") { res.setHeader("Allow", "POST"); res.status(405).end(); return false; }
  if (badOrigin(req)) { res.status(403).end(); return false; }
  if (rateLimited(req, maxPerMinute)) { res.setHeader("Retry-After", "60"); res.status(429).end(); return false; }
  if (!process.env.SUPABASE_URL || !process.env.SUPABASE_KEY) { res.status(503).end(); return false; }
  return true;
}

function parseBody(req) {
  let b = req.body;
  if (typeof b === "string") { if (b.length > 64000) return null; try { b = JSON.parse(b); } catch { return null; } }
  return b && typeof b === "object" && !Array.isArray(b) ? b : null;
}

async function supabase(path, body, prefer = "return=minimal") {
  const key = process.env.SUPABASE_KEY;
  const headers = { apikey: key, "Content-Type": "application/json", Prefer: prefer };
  if (!key.startsWith("sb_")) headers.Authorization = `Bearer ${key}`;
  const r = await fetch(`${process.env.SUPABASE_URL}/rest/v1/${path}`, { method: "POST", headers, body: JSON.stringify(body) });
  if (!r.ok) throw new Error(`${path}: ${r.status} ${await r.text()}`);
  return r;
}

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

module.exports = { guard, parseBody, supabase, UUID };
