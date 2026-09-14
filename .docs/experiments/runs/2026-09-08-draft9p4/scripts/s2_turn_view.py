"""Turn the head so the socket's cross slit stops lying on top of its own center.

    uv run --project . python -u .docs/experiments/runs/2026-09-08-draft9p4/scripts/s2_turn_view.py

No CAD. It hides the two connectors, turns the camera, and reports where the sphere's center
and each slit circle's center land in pixels, so the pick can be aimed at a patch of sphere
rather than at a slit edge.
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

# The cavity, read off bodydetails: one sphere, cut by a cross slit 1.6 mm wide.
BALL = (0.0, 0.0, -45.0)
SLITS = {"y-": (0.0, -0.8, -45.0), "y+": (0.0, 0.8, -45.0),
         "x-": (-0.8, 0.0, -45.0), "x+": (0.8, 0.0, -45.0)}


def menu_item(page, name: str, row_px):
    """Right-click a tree row and take the named item off its menu."""
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


def report(page, what):
    cam = screen.camera(page)
    if cam is None:
        print(f"  {what}: no camera yet")
        return None
    print(f"  {what}: {screen.scale(cam):.2f} px/mm")
    px = {}
    for name, p in [("ball center", BALL)] + list(SLITS.items()):
        xy = screen.project(cam, p[0] / 1000, p[1] / 1000, p[2] / 1000)
        px[name] = xy
        print(f"    {name:12s} {p} mm  ->  {xy[0]:7.1f},{xy[1]:7.1f} px")
    b = px["ball center"]
    for name in SLITS:
        d = ((px[name][0] - b[0]) ** 2 + (px[name][1] - b[1]) ** 2) ** 0.5
        print(f"    {name} slit center is {d:5.1f} px from the ball's center")
    return cam


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        doc = api.Doc(DID, WID, HEAD)
        gui.open_doc(page, doc)
        screen.hook(page)
        print("signed in as:", api.require_signed_in(page))

        for name in ("socket mount point", "head mate"):
            try:
                menu_item(page, "Hide", gui.row(page, name))
                print(f"  hid {name}")
            except Exception as e:                                # noqa: BLE001
                print(f"  {name}: {str(e)[:120]}")

        gui.planes(page, shown=False)
        gui.fit(page)

        # shift+7 looks down on the head, and the socket is under it. Four up arrows
        # drop the camera below the horizon; the left arrows then swing the heading so
        # the slit's cross sits diagonally rather than square to the screen.
        page.mouse.move(*screen.CENTER)
        page.keyboard.press("Shift+7")
        page.wait_for_timeout(1500)
        for _ in range(8):                       # 8 x 15 deg = 120 deg, under the head
            page.keyboard.press("ArrowUp")
            page.wait_for_timeout(250)
        page.wait_for_timeout(1200)
        gui.frame(page, f"{CAP}/turn-01-from-below.png", park=True)
        report(page, "from below")

        for _ in range(3):                       # 45 deg of heading
            page.keyboard.press("ArrowLeft")
            page.wait_for_timeout(250)
        page.wait_for_timeout(1200)
        gui.frame(page, f"{CAP}/turn-02-heading-45.png", park=True)
        cam = report(page, "heading turned 45 deg")

        if cam is not None:
            at = screen.project(cam, 0, 0, -45 / 1000)
            gui.zoom_to(page, 30.0, at_px=(round(at[0]), round(at[1])))
            page.wait_for_timeout(900)
            gui.frame(page, f"{CAP}/turn-03-zoomed.png", park=True)
            report(page, "zoomed to 30 px/mm")


if __name__ == "__main__":
    main()
