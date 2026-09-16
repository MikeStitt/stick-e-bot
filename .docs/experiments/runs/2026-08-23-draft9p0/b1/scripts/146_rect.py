import sys, numpy as np
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    img = gui.probe(page)[:, :, :3].astype(int)
    # look right of the socket disc only, where the background is white
    sub = img[500:545, 1032:1075]
    dark = sub.sum(axis=2) < 450
    print("cols", [1032 + i for i, c in enumerate(dark.sum(axis=0)) if c >= 20])
    print("rows", [500 + i for i, r in enumerate(dark.sum(axis=1)) if r >= 20])
    for spot, what in [((1050, 514), "top edge"), ((1050, 531), "bottom edge"),
                       ((1063, 518), "right edge"), ((982, 518), "left edge")]:
        gui.clear(page)
        try:
            gui.pick(page, spot, what)
        except RuntimeError as e:
            print("  MISS", what, e)
