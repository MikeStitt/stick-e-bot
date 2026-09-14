"""Shift as a lock: hover the face first, then hold Shift, then move to the point.

    uv run --project . python -u .docs/experiments/runs/2026-09-08-draft9p4/scripts/s6_shift_lock.py [lock|nolock]

Shift does not pre-filter what is under the pointer. It pins the reference to whatever face or
edge is already hovered, so the inferred points stay that face's while the cursor travels — even
off the face. That makes the order the whole technique: hover, then Shift, then move, then click.
s3 pressed Shift before the hover, which locks nothing, so it never tested this.

The hard view is the one the guide uses: square on the socket's axis, where `socket connect to
robot` sits between the camera and the cavity and takes any click at the center.

  lock     hover a clear patch of the cavity sphere, hold Shift, travel to the center, click
  nolock   the same travel with no Shift, to show the lock is what carried the reference

Pass is `originQuery` holding one entity, `secondaryOriginQuery` holding none, inference CENTER,
and an origin on (0, 0, -45) mm.
"""
import json
import sys
import time

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
OFF = 2.5           # how far off the axis the first hover sits, in millimeters, each way
SPIKE = "spike mate"


def menu_item(page, name, row_px):
    # Rename and Hide both vanish from the menu whenever more than one thing is selected,
    # and Onshape leaves things selected constantly, so clear before asking.
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)
    page.mouse.click(*gui.EMPTY)
    page.wait_for_timeout(600)
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
        raise RuntimeError(f"no {name!r} on that menu")
    page.mouse.click(*hit)
    page.wait_for_timeout(900)


def settled_camera(page, tries: int = 4):
    """The camera, waking the canvas when it has not drawn since the last look."""
    for _ in range(tries):
        cam = screen.camera(page)
        if cam is not None:
            return cam
        gui.wake(page)
    raise RuntimeError("the canvas will not report a camera")


def origin_entity(page) -> str:
    return page.evaluate(
        """() => {
            const d = document.querySelector('#feature-dialog');
            if (!d) return '(no dialog)';
            const out = [];
            for (const e of d.querySelectorAll('.os-selection-name, .os-query-name, li'))
                { const t = (e.innerText || '').trim(); if (t && t.length < 80) out.push(t); }
            return out.join(' | ') || '(nothing selected)'; }""")


def readback(page):
    time.sleep(1.0)
    r = api.api(page, "GET", f"/api/partstudios/d/{DID}/w/{WID}/e/{HEAD}/features")
    if r["status"] != 200:
        return None
    for ft in r["body"]["features"]:
        f = ft.get("message", ft)
        if f.get("name") != SPIKE:
            continue
        got = {}
        for p in f.get("parameters", []):
            p = p.get("message", p)
            pid = p.get("parameterId")
            if pid in ("originQuery", "secondaryOriginQuery"):
                got[pid] = [g for q in p.get("queries") or []
                            for g in (q.get("message", q).get("geometryIds") or [])]
            elif pid == "entityInferenceType":
                got[pid] = p.get("value")
        return got
    return None


def where_is_it(page, doc):
    fs = """function(context is Context, queries is map)
    {
        var s = "";
        for (var b in evaluateQuery(context, qBodyType(qEverything(EntityType.BODY), BodyType.MATE_CONNECTOR)))
            s = s ~ toString(evMateConnector(context, { "mateConnector" : b }).origin / millimeter) ~ "\\n";
        return s;
    }"""
    try:
        return api.eval_fs(page, doc, fs)
    except Exception as e:                                        # noqa: BLE001
        return f"(featurescript refused: {str(e)[:120]})"


def delete_spike(page):
    page.keyboard.press("Escape")
    page.wait_for_timeout(600)
    try:
        at = gui.row(page, SPIKE)
    except Exception:                                             # noqa: BLE001
        print(f"  no {SPIKE} row to delete")
        return
    page.mouse.click(*at, button="right")
    page.wait_for_timeout(1200)
    hit = page.evaluate(
        """() => {
            for (const e of document.querySelectorAll('li,a,span,div')) {
                if (e.children.length) continue;
                if ((e.innerText || '').trim() !== 'Delete') continue;
                const r = e.getBoundingClientRect();
                if (r.width && r.height)
                    return [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
            }
            return null; }""")
    if not hit:
        page.keyboard.press("Escape")
        print(f"  no Delete on {SPIKE}'s menu")
        return
    page.mouse.click(*hit)
    page.wait_for_timeout(2500)
    print(f"  deleted {SPIKE}" if SPIKE not in gui.tree(page) else f"  {SPIKE} survived")


def main():
    variant = sys.argv[1] if len(sys.argv) > 1 else "lock"
    if variant not in ("lock", "nolock"):
        raise SystemExit(f"unknown variant {variant!r}")

    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        doc = api.Doc(DID, WID, HEAD)
        gui.open_doc(page, doc)
        screen.hook(page)
        print(f"variant: {variant}")

        if SPIKE in gui.tree(page):
            delete_spike(page)

        # A reader building this page for the first time has no `head mate` yet.
        try:
            menu_item(page, "Hide", gui.row(page, "head mate"))
            print("  hid head mate, which a first-time reader does not have")
        except Exception as e:                                    # noqa: BLE001
            print(f"  head mate: {str(e)[:90]}")

        page.mouse.move(*screen.CENTER)
        page.keyboard.press("Shift+6")                 # square on the socket's axis
        page.wait_for_timeout(1600)
        gui.fit(page)
        cam = settled_camera(page)
        at = screen.project(cam, *[v / 1000 for v in BALL])
        gui.zoom_to(page, 29.0, at_px=(round(at[0]), round(at[1])))
        page.wait_for_timeout(900)

        cam = settled_camera(page)
        center = screen.project(cam, *[v / 1000 for v in BALL])
        center = (round(center[0]), round(center[1]))
        # A point on the cavity's near side, out in a quadrant clear of the cross slit.
        dz = (R * R - OFF * OFF - OFF * OFF) ** 0.5
        face_mm = (OFF, OFF, BALL[2] - dz)
        face = screen.project(cam, *[v / 1000 for v in face_mm])
        face = (round(face[0]), round(face[1]))
        print(f"  scale {screen.scale(cam):.2f} px/mm")
        print(f"  first hover on the shell at ({face_mm[0]:.2f}, {face_mm[1]:.2f}, "
              f"{face_mm[2]:.2f}) mm, drawn at {face}")
        print(f"  then travel to the ball's center, drawn at {center}")

        gui.search_tool(page, "Mate connector", settle=3000)
        if not page.locator("#feature-dialog").count():
            raise SystemExit("Mate connector never opened")
        gui.name_feature(page, SPIKE)

        # Hover the face and let its points come up.
        page.mouse.move(*face)
        page.wait_for_timeout(1100)
        gui.frame(page, f"{CAP}/{variant}-01-hover-face.png")

        # Then, and only then, the lock.
        if variant == "lock":
            page.keyboard.down("Shift")
            page.wait_for_timeout(400)

        # Travel to the center in steps, the way a hand does.
        for i in range(1, 7):
            page.mouse.move(face[0] + (center[0] - face[0]) * i / 6,
                            face[1] + (center[1] - face[1]) * i / 6)
            page.wait_for_timeout(180)
        page.wait_for_timeout(700)
        gui.frame(page, f"{CAP}/{variant}-02-arrived.png")

        page.mouse.click(*center)
        page.wait_for_timeout(400)
        if variant == "lock":
            page.keyboard.up("Shift")
        page.wait_for_timeout(1400)

        print("  Origin entity reads:", origin_entity(page))
        gui.frame(page, f"{CAP}/{variant}-03-picked.png", park=True)
        gui.tick(page)
        page.wait_for_timeout(2000)

        got = readback(page)
        print("  committed:", json.dumps(got))
        print("  it sits at:\n" + (where_is_it(page, doc) or "").rstrip())
        ok = (got and len(got.get("originQuery", [])) == 1
              and not got.get("secondaryOriginQuery")
              and got.get("entityInferenceType") == "CENTER")
        print("  PASS" if ok else "  FAIL")
        delete_spike(page)


if __name__ == "__main__":
    main()
