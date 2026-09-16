import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    for pg, n in common.marks(ctx):
        print("page", repr(n), pg.url[:80])
    page = common.mypage(ctx)
    for n, fid, st in common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-3:]:
        print(repr(n), st)
    page.screenshot(path=D+"tl26.png")
