"""#58 — heroes for the two of the first five pages that need no rollback.

`ball and socket` has not been touched since tutorial 4, and `head` has not been
touched since tutorial 5, so what is in each tab today is exactly what its page
ends on. The other three pages need a state the model has moved past.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
OUT = "/Users/mikestitt/projects/first/2027/sponge/instructions/stickbot-draft9p0/source/images/"
s = common.load(); did, wid = s["did"], s["wid"]
JOBS = [("ball and socket", s["bs_eid"], "ball-and-socket"),
        ("head", s["head_eid"], "head-socket")]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.set_default_navigation_timeout(180000)
    page.set_default_timeout(120000)
    for name, eid, folder in JOBS:
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(15000)
        gui.viewport(page)
        page.mouse.move(900, 500)
        page.keyboard.press("Shift+7")
        page.wait_for_timeout(2000)
        gui.fit(page)
        page.wait_for_timeout(2500)
        gui.clear(page)          # a hovered face pre-highlights and lands in the frame
        page.mouse.move(*gui.EMPTY)
        page.wait_for_timeout(1500)
        gui.frame(page, OUT + folder + "/hero.png")
        print(f"  {name}: {gui.tree(page)[-4:]}")
