"""Put the two head connectors back on screen, then turn the view again.

    uv run --project . python -u .docs/experiments/runs/2026-09-08-draft9p4/scripts/s5_unhide_and_turn.py

The turned view has been proved with `socket mount point` and `head mate` hidden. The page
would rather not ask the reader to hide anything, so this restores them and leaves the camera
where s3 expects it, to find out whether turning the view is enough on its own.
"""
import sys

sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge/tools")
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")

from playwright.sync_api import sync_playwright

import onshape_gui as gui
import onshape_screen as screen
import onshape_session as api

DID = "fe052e606c96bb7cc5aaf59f"
WID = "0ff70e8921be572d630dd9cc"
HEAD = "95fe567f38e1c8c891bc94a3"
CAP = "/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/2026-09-08-draft9p4/capture/mate-center"

BALL = (0.0, 0.0, -45.0)


def menu_item(page, name: str, row_px):
    page.mouse.click(*row_px, button="right")
    page.wait_for_timeout(1200)
    hit = page.evaluate(
        """(want) => {
            for (const e of document.querySelectorAll('li,a,span,div')) {
                if (e.children.length) continue;
                if ((e.innerText || '').trim() !== want) continue;
                const r = e.getBoundingClientRect();
                if (r.width && r.height)
                    return [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
            }
            return null; }""", name)
    if not hit:
        page.keyboard.press("Escape")
        raise RuntimeError(f"no {name!r} on that row's menu")
    page.mouse.click(*hit)
    page.wait_for_timeout(900)


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        gui.open_doc(page, api.Doc(DID, WID, HEAD))
        screen.hook(page)

        # `head mate` is the one row a first-time reader does not have yet, so a run that
        # wants to stand in for that reader hides it and shows the rest.
        hide = set(sys.argv[1:])
        for name in ("socket mount point", "head mate"):
            want = "Hide" if name in hide else "Show"
            try:
                menu_item(page, want, gui.row(page, name))
                print(f"  {want.lower()}: {name}")
            except Exception as e:                                # noqa: BLE001
                print(f"  {name}: already {want.lower()}n, or {str(e)[:90]}")

        gui.fit(page)
        page.mouse.move(*screen.CENTER)
        page.keyboard.press("Shift+7")
        page.wait_for_timeout(1500)
        for _ in range(8):
            page.keyboard.press("ArrowUp")
            page.wait_for_timeout(250)
        for _ in range(3):
            page.keyboard.press("ArrowLeft")
            page.wait_for_timeout(250)
        page.wait_for_timeout(1200)

        cam = screen.camera(page)
        at = screen.project(cam, *[v / 1000 for v in BALL])
        gui.zoom_to(page, 29.0, at_px=(round(at[0]), round(at[1])))
        page.wait_for_timeout(900)
        gui.frame(page, f"{CAP}/turn-04-nothing-hidden.png", park=True)
        cam = screen.camera(page)
        at = screen.project(cam, *[v / 1000 for v in BALL])
        print(f"  scale {screen.scale(cam):.2f} px/mm, ball center draws at "
              f"({at[0]:.0f}, {at[1]:.0f})")


if __name__ == "__main__":
    main()
