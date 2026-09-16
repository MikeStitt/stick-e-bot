"""B3, second pass — drive #torsoW. argv: value, row y."""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
s = common.load(); did, wid, vs = s["did"], s["wid"], s["vs_eid"]
VAL, Y = sys.argv[1], int(sys.argv[2])
JS = """() => [...document.querySelectorAll('input')].map(e => {
  const r = e.getBoundingClientRect(); return [Math.round(r.y), e.value]; })
  .filter(a => a[1])"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.set_default_navigation_timeout(180000)
    if "/e/" + vs not in page.url:
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{vs}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(12000)
    page.mouse.click(890, Y)
    page.wait_for_timeout(800)
    page.keyboard.press("Meta+A")
    page.keyboard.type(VAL)
    page.wait_for_timeout(400)
    page.keyboard.press("Enter")
    page.wait_for_timeout(8000)
    print(page.evaluate(JS))
