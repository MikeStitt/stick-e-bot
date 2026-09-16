"""Open robot sizes and report where each row sits on screen, so c2_drive can click one."""
import sys, base64
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

DID = "4b2e0d48efd37d3327a90afb"
WID = "a1af16872d25103815f1c32a"
VS = "f30d47abeacf3059ec4a3342"
OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/frames/")

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    page.goto(f"https://cad.onshape.com/documents/{DID}/w/{WID}/e/{VS}",
              wait_until="domcontentloaded")
    page.wait_for_timeout(15000)
    boxes = page.evaluate("""() => [...document.querySelectorAll('input')]
        .map(e => { const r = e.getBoundingClientRect();
            return [Math.round(r.left + r.width / 2), Math.round(r.top + r.height / 2),
                    Math.round(r.width), e.value]; })
        .filter(b => b[2] > 30)""")
    for x, y, w, v in boxes:
        print(f"  x {x:5d}  y {y:5d}  w {w:4d}  {v!r}")
    cdp = ctx.new_cdp_session(page)
    d = cdp.send("Page.captureScreenshot", {"format": "png"})
    open(OUT + "c2-table-before.png", "wb").write(base64.b64decode(d["data"]))
    print("shot c2-table-before")
