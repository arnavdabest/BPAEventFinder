// Opt-out and "delete my data" controls on the privacy page.
(() => {
  const ls = (k, v) => { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch { return null; } };
  const $ = id => document.getElementById(id);
  const signal = navigator.globalPrivacyControl || navigator.doNotTrack === "1";

  function render() {
    const off = ls("bpa_optout") === "1";
    $("state").textContent = signal ? "off (your browser's privacy signal)" : off ? "off" : "on";
    $("toggle").textContent = off ? "Turn tracking back on" : "Turn off tracking";
    $("toggle").disabled = signal;
    $("vid").textContent = ls("bpa_vid") || "none";
    $("forget").disabled = !ls("bpa_vid");
  }

  $("toggle").onclick = () => {
    const off = ls("bpa_optout") === "1";
    ls("bpa_optout", off ? null : "1");
    $("status").textContent = off ? "Tracking is back on." : "Tracking is off for this browser.";
    render();
  };

  $("forget").onclick = async () => {
    const vid = ls("bpa_vid");
    if (!vid) return;
    $("forget").disabled = true;
    $("status").textContent = "Deleting…";
    try {
      const r = await fetch("/api/forget", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ vid }) });
      if (!r.ok) throw new Error(r.status);
      ls("bpa_vid", null); ls("bpa_visits", null); ls("bpa_optout", "1");
      $("status").textContent = "Done. Your data is deleted and tracking is now off for this browser.";
    } catch {
      $("status").textContent = "Something went wrong. Try again in a minute, or contact us through the Support page.";
    }
    render();
  };

  render();
})();
