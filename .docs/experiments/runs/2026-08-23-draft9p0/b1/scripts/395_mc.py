import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
name, x, y, tag = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.search_tool(page, "Mate connector")
    page.wait_for_timeout(1500)
    page.mouse.move(x, y); page.wait_for_timeout(600)
    page.mouse.click(x, y); page.wait_for_timeout(600)
    page.mouse.click(x, y); page.wait_for_timeout(1800)
    rows = gui.labels(page)
    for r in rows:
        print(r)
    if not any(r[0].startswith("Face of") for r in rows):
        raise SystemExit("no face picked")
    if any(r[0] == "Select owner entity" for r in rows):
        page.mouse.click(256, 258)
        page.wait_for_timeout(1200)
    page.screenshot(path=D+tag+".png")
    from PIL import Image
    Image.open(D+tag+".png").crop((x-75, y-75, x+75, y+75)).resize((600,600)).save(D+"frames/"+name.replace(" ","_")+".closeup.png")
    gui.tick(page)
    page.wait_for_timeout(3000)
    gui.rename_row(page, "Mate connector 1", name)
    page.wait_for_timeout(2000)
    print("done", name)
