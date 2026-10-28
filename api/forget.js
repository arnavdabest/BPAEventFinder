// "Delete my data" from the privacy page: removes every row tied to this browser's anonymous ID.
// The ID is a random UUID only that browser knows, so nobody can delete someone else's data by guessing.
const { guard, parseBody, supabase, UUID } = require("./_guard");

module.exports = async (req, res) => {
  if (!guard(req, res, 5)) return;
  const body = parseBody(req);
  if (!body || !UUID.test(body.vid)) return res.status(400).end();
  try {
    await supabase("rpc/forget_visitor", { p_vid: body.vid });
    res.status(204).end();
  } catch (err) {
    console.error(err.message);
    res.status(500).end();
  }
};
