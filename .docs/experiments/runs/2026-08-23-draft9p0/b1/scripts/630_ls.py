import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    fs = common.features(page, api, s["did"], s["wid"], s["hinge_eid"])
    print(len(fs))
    for n, fid, st in fs[-4:]:
        print(repr(n), st)
    print(common.bbox(page, api, s["did"], s["wid"], s["hinge_eid"]))
