// Called once a day by Vercel Cron (see vercel.json). Keeps the free Supabase project from
// pausing and deletes data older than 2 years (the retention period in the privacy policy).
// Vercel sends "Authorization: Bearer $CRON_SECRET", so nobody else can trigger it.
module.exports = async (req, res) => {
  if (!process.env.CRON_SECRET || req.headers.authorization !== `Bearer ${process.env.CRON_SECRET}`) return res.status(401).end();
  const key = process.env.SUPABASE_KEY;
  const headers = { apikey: key, "Content-Type": "application/json" };
  if (!key.startsWith("sb_")) headers.Authorization = `Bearer ${key}`;
  const r = await fetch(`${process.env.SUPABASE_URL}/rest/v1/rpc/keepalive`, { method: "POST", headers, body: "{}" });
  res.status(r.ok ? 200 : 502).json({ ok: r.ok });
};
