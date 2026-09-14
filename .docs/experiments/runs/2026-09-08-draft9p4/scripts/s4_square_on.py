"""Put the camera square on the socket's axis, the way the guide tells the reader to.

    uv run --project . python -u .docs/experiments/runs/2026-09-08-draft9p4/scripts/s4_square_on.py

Finds which Shift+number is the bottom view by reading the camera back rather than by
trusting a list, then zooms to the socket and reports how far the pick pixel is from the
cross slit. This is the view draft9p3 worked from, and the one that produced the 0.8 mm.
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
R = 6.08


def toward_camera(cam):
    mv = cam["mv"]
    d = (mv[2], mv[6], mv[10])
    n = sum(c * c for c in d) ** 0.5
    return tuple(c / n for c in d)


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        gui.open_doc(page, api.Doc(DID, WID, HEAD))
        screen.hook(page)

        best = None
        for k in range(1, 8):
            page.mouse.move(*screen.CENTER)
            page.keyboard.press(f"Shift+{k}")
            page.wait_for_timeout(1600)
            cam = screen.camera(page)
            if cam is None:
                print(f"  Shift+{k}: no camera")
                continue
            d = toward_camera(cam)
            print(f"  Shift+{k}: camera lies toward ({d[0]:+.3f}, {d[1]:+.3f}, {d[2]:+.3f})")
            if d[2] < -0.99:                       # under the head, looking up the axis
                best = k
        if best is None:
            raise SystemExit("none of Shift+1..7 looks up the socket's axis")

        print(f"  the bottom view is Shift+{best}")
        page.mouse.move(*screen.CENTER)
        page.keyboard.press(f"Shift+{best}")
        page.wait_for_timeout(1600)
        gui.fit(page)

        cam = screen.camera(page)
        at = screen.project(cam, *[v / 1000 for v in BALL])
        gui.zoom_to(page, 29.0, at_px=(round(at[0]), round(at[1])))
        page.wait_for_timeout(900)

        cam = screen.camera(page)
        at = screen.project(cam, *[v / 1000 for v in BALL])
        d = toward_camera(cam)
        p = [BALL[i] + R * d[i] for i in range(3)]
        print(f"  scale {screen.scale(cam):.2f} px/mm, ball center draws at "
              f"({at[0]:.0f}, {at[1]:.0f})")
        print(f"  a click there lands on the shell at ({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f}) mm; "
              f"the nearest slit trace is {min(abs(p[0]), abs(p[1])):.2f} mm away")
        gui.frame(page, f"{CAP}/square-00-view.png", park=True)


if __name__ == "__main__":
    main()
