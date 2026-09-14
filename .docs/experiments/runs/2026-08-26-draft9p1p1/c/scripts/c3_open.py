"""Open the assembly, fit it, and photograph it once so the view cube can be located."""
import sys, base64
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

DID = "4b2e0d48efd37d3327a90afb"; WID = "a1af16872d25103815f1c32a"
ASM = "cd2278317279029435f010de"
OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/frames/")

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    page.goto(f"https://cad.onshape.com/documents/{DID}/w/{WID}/e/{ASM}",
              wait_until="domcontentloaded")
    page.wait_for_timeout(20000)
    page.mouse.move(760, 500)
    page.keyboard.press("f")
    page.wait_for_timeout(4000)
    cdp = ctx.new_cdp_session(page)
    d = cdp.send("Page.captureScreenshot", {"format": "png"})
    open(OUT + "c3-01-iso.png", "wb").write(base64.b64decode(d["data"]))
    print("viewport", page.viewport_size)
    print("shot c3-01-iso")
