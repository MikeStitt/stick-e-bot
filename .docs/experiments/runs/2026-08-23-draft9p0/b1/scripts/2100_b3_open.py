"""B3 — open `robot sizes` and read the table as it stands."""
import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid, vs = s["did"], s["wid"], s["vs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    print("url:", page.url[:120])
    r = osx.api(page, "GET", f"/api/documents/d/{did}/w/{wid}/elements")
    for e in r["body"]:
        print(" ", e["elementType"], e["id"], e["name"])
    page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{vs}")
    page.wait_for_timeout(9000)
    page.screenshot(path=D + "b3_before.png")
    cells = page.query_selector_all("div.os-td")
    print("os-td:", len(cells))
    for i, c in enumerate(cells[:60]):
        t = (c.inner_text() or "").strip()
        if t:
            b = c.bounding_box()
            print(i, repr(t[:28]), None if not b else (round(b["x"]), round(b["y"])))
