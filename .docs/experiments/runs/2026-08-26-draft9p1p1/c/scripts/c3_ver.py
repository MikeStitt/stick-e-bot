"""Open Create version… and report the dialog's fields at this window size."""
import sys, base64
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/frames/")

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    page.keyboard.press("Escape")
    page.wait_for_timeout(600)
    page.mouse.click(20, 92)
    page.wait_for_timeout(4000)
    rows = page.evaluate("""() => {
        const out = [];
        for (const el of document.querySelectorAll('input,textarea,button,label,h1,h2,h3')) {
            const r = el.getBoundingClientRect();
            if (r.width < 4 || r.height < 4) continue;
            const t = (el.value || el.getAttribute('placeholder') ||
                       el.textContent || '').trim();
            out.push([el.tagName, t.slice(0, 40), Math.round(r.x + r.width / 2),
                      Math.round(r.y + r.height / 2)]);
        }
        return out;
    }""")
    for tag, t, x, y in rows:
        print(f"  {tag:9s} {x:5d} {y:5d}  {t!r}")
    cdp = ctx.new_cdp_session(page)
    d = cdp.send("Page.captureScreenshot", {"format": "png"})
    open(OUT + "c3-version-dialog.png", "wb").write(base64.b64decode(d["data"]))
