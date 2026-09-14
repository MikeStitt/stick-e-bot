"""Turn the robot with the view cube and photograph each face it comes to rest on."""
import sys
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S
OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-25-draft9p1/c/frames/")
CUBE_FRONT = (1174, 180)
ARROW_RIGHT = (1258, 167)
CUBE_TOP = (1190, 140)
STEPS = [("c-02-front", CUBE_FRONT), ("c-03-right", ARROW_RIGHT),
         ("c-04-back", ARROW_RIGHT), ("c-05-left", ARROW_RIGHT),
         ("c-06-top", CUBE_TOP)]
with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    for name, at in STEPS:
        page.mouse.click(*at)
        page.wait_for_timeout(3500)
        page.mouse.move(760, 400)
        page.keyboard.press("f")
        page.wait_for_timeout(3500)
        page.mouse.move(1150, 640)
        page.wait_for_timeout(1200)
        page.screenshot(path=OUT + name + ".png", timeout=300000,
                        animations="disabled", caret="initial", scale="css")
        print("shot", name)
