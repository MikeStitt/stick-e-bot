"""Turn the robot with the view cube and photograph each face it comes to rest on.

CDP rather than page.screenshot, which times out on Onshape.
"""
import sys, base64
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/frames/")
CUBE_FRONT = (1174, 180)
ARROW_RIGHT = (1258, 167)
CUBE_TOP = (1190, 140)
STEPS = [("c3-02-front", CUBE_FRONT), ("c3-03-right", ARROW_RIGHT),
         ("c3-04-back", ARROW_RIGHT), ("c3-05-left", ARROW_RIGHT),
         ("c3-06-top", CUBE_TOP)]

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    cdp = ctx.new_cdp_session(page)
    for name, at in STEPS:
        page.mouse.click(*at)
        page.wait_for_timeout(3500)
        page.mouse.move(760, 400)
        page.keyboard.press("f")
        page.wait_for_timeout(3500)
        page.mouse.move(700, 640)
        page.wait_for_timeout(1200)
        d = cdp.send("Page.captureScreenshot", {"format": "png"})
        open(OUT + name + ".png", "wb").write(base64.b64decode(d["data"]))
        print("shot", name, flush=True)
