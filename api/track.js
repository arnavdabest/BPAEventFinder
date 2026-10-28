// Receives batched analytics events from the site and writes them to Supabase.
// Env vars: SUPABASE_URL, SUPABASE_KEY (the publishable key; database rules only allow inserts, never reads).
const { guard, parseBody, supabase, UUID } = require("./_guard");

const TYPES = new Set([
  "session_start", "landing_view", "quiz_start", "question_view", "option_toggle", "answer", "back",
  "quiz_complete", "results_view", "browse_all", "detail_open", "detail_close", "link_click",
  "start_over", "home_click", "page_hidden",
]);
const MAX_EVENT_BYTES = 6000;
const str = (v, n = 200) => (v == null ? null : String(v).slice(0, n));
const int = v => (Number.isFinite(+v) && Math.abs(+v) < 1e6 ? Math.round(+v) : null);

function parseUA(ua = "") {
  const os = /iPhone|iPad|iPod/.test(ua) ? "iOS" : /Android/.test(ua) ? "Android" : /CrOS/.test(ua) ? "ChromeOS"
    : /Windows/.test(ua) ? "Windows" : /Mac OS X/.test(ua) ? "macOS" : /Linux/.test(ua) ? "Linux" : "Other";
  const browser = /Edg\//.test(ua) ? "Edge" : /OPR\//.test(ua) ? "Opera" : /SamsungBrowser/.test(ua) ? "Samsung"
    : /CriOS|Chrome\//.test(ua) ? "Chrome" : /FxiOS|Firefox\//.test(ua) ? "Firefox" : /Safari\//.test(ua) ? "Safari" : "Other";
  return { os, browser };
}

module.exports = async (req, res) => {
  if (!guard(req, res, 40)) return;
  const body = parseBody(req);
  if (!body || !UUID.test(body.sid) || !UUID.test(body.vid) || !Array.isArray(body.events)) return res.status(400).end();

  const { sid, vid } = body;
  const h = req.headers;
  const decode = v => { try { return v ? decodeURIComponent(v) : null; } catch { return null; } };
  const now = Date.now();

  const events = body.events.slice(0, 60)
    .filter(e => e && TYPES.has(e.type) && (e.d == null || (typeof e.d === "object" && !Array.isArray(e.d))))
    .map(e => ({
      session_id: sid, visitor_id: vid, type: e.type,
      question_id: typeof e.q === "string" && /^[a-z]{1,20}$/.test(e.q) ? e.q : null,
      // ignore client clocks that are wildly off
      client_ts: Number.isFinite(e.t) && Math.abs(e.t - now) < 864e5 ? new Date(e.t).toISOString() : null,
      data: e.d || {},
    }))
    .filter(e => JSON.stringify(e.data).length <= MAX_EVENT_BYTES);

  try {
    const start = body.events.find(e => e && e.type === "session_start");
    if (start) {
      const c = start.d && typeof start.d === "object" ? start.d : {};
      const { os, browser } = parseUA(h["user-agent"]);
      await supabase("sessions", [{
        session_id: sid, visitor_id: vid,
        visit_number: int(c.visit), referrer: str(c.referrer, 500),
        utm_source: str(c.utm_source, 100), utm_medium: str(c.utm_medium, 100), utm_campaign: str(c.utm_campaign, 100),
        landing_path: str(c.path, 300),
        country: str(h["x-vercel-ip-country"], 5), region: str(decode(h["x-vercel-ip-country-region"]), 20),
        timezone: str(c.tz, 60), language: str(c.lang, 20),
        device: ["phone", "tablet", "desktop"].includes(c.device) ? c.device : null, os, browser,
        screen_w: int(c.sw), screen_h: int(c.sh), viewport_w: int(c.vw), viewport_h: int(c.vh),
        dark_mode: !!c.dark, touch: !!c.touch,
      }]).catch(err => { if (!/ 409 /.test(err.message)) console.error(err.message); }); // 409 = retried batch, row already saved
    }
    if (events.length) await supabase("events", events);
    res.status(204).end();
  } catch (err) {
    console.error(err.message);
    res.status(500).end();
  }
};
