"""The spike: reach the cavity sphere's own center with a turned view and a Shift hover.

    uv run --project . python -u .docs/experiments/runs/2026-09-08-draft9p4/scripts/s3_spike_pick.py [variant]

Variants, all of them one throwaway connector built, read back and deleted:

  shift-hover   Shift held across the hover and released before the click
  shift-click   Shift held across the hover and the click too
  plain         no Shift at all, on the same turned view, to separate the two techniques

Pass is `originQuery` holding one entity, `secondaryOriginQuery` holding none, and an origin
on the sphere's center at (0, 0, -45) mm. The view is left turned, and the throwaway is
deleted whether it passed or not.
"""
import json
import sys
import time


from playwright.sync_api import sync_playwright

from stickbot import repo_root
from stickbot import onshape_gui as gui
from stickbot import onshape_screen as screen
from stickbot import onshape_session as api

DID = "fe052e606c96bb7cc5aaf59f"
WID = "0ff70e8921be572d630dd9cc"
HEAD = "95fe567f38e1c8c891bc94a3"
CAP = str(repo_root()) + "/.docs/experiments/runs/2026-09-08-draft9p4/capture/mate-center"

BALL = (0.0, 0.0, -45.0)          # the cavity sphere's center, in millimeters
R = 6.08                          # its radius
SLIT = 0.8                        # the cross slit's half width; its four traces sit here
SPIKE = "spike mate"


def near_point(cam):
    """Where on the sphere the camera is looking straight at, in millimeters.

    The ray through the sphere's projected center meets the surface at the point
    closest to the camera, and that is the point a click on that pixel lands on. Its
    x and y say whether it is out in a quadrant of the shell or down in the 1.6 mm
    square the four slit traces box in.
    """
    mv = cam["mv"]
    d = (mv[2], mv[6], mv[10])                       # toward the camera, in model space
    n = sum(c * c for c in d) ** 0.5
    return tuple(BALL[i] + R * d[i] / n for i in range(3))


def origin_entity(page) -> str:
    """What the dialog says is in Origin entity, as the reader sees it."""
    return page.evaluate(
        """() => {
            const d = document.querySelector('#feature-dialog');
            if (!d) return '(no dialog)';
            const out = [];
            for (const e of d.querySelectorAll('.os-selection-name, .os-query-name, li'))
                { const t = (e.innerText || '').trim(); if (t && t.length < 80) out.push(t); }
            return out.join(' | ') || '(nothing selected)'; }""")


def readback(page, doc):
    """The committed connector, from /features and from the model."""
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
            if pid in ("originQuery", "secondaryOriginQuery", "originAdditionalQuery"):
                got[pid] = [g for q in p.get("queries") or []
                            for g in (q.get("message", q).get("geometryIds") or [])]
            elif pid == "entityInferenceType":
                got[pid] = p.get("value")
        return got
    return None


def where_is_it(page, doc):
    """The spike connector's origin, in millimeters, off the model itself."""
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
    except Exception as e:                                        # noqa: BLE001
        print(f"  no {SPIKE} row to delete: {str(e)[:100]}")
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
        print(f"  no Delete on {SPIKE}'s menu; it is still in the tree")
        return
    page.mouse.click(*hit)
    page.wait_for_timeout(2500)
    print(f"  deleted {SPIKE}" if SPIKE not in gui.tree(page) else f"  {SPIKE} survived the delete")


def main():
    variant = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else "shift-hover"
    if variant not in ("shift-hover", "shift-click", "plain"):
        raise SystemExit(f"unknown variant {variant!r}")

    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        doc = api.Doc(DID, WID, HEAD)
        gui.open_doc(page, doc)
        screen.hook(page)
        print(f"variant: {variant}")

        if SPIKE in gui.tree(page):
            print(f"  a {SPIKE} is already in the tree; clearing it first")
            delete_spike(page)

        cam = screen.camera(page)
        if cam is None:
            gui.wake(page)
            cam = screen.camera(page)
        if cam is None:
            raise SystemExit("no camera; run s2_turn_view.py first to turn the view")
        at = screen.project(cam, *[v / 1000 for v in BALL])
        at = (round(at[0]), round(at[1]))
        p = near_point(cam)
        print(f"  scale {screen.scale(cam):.2f} px/mm, ball center draws at {at}")
        print(f"  the click lands on the shell at "
              f"({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f}) mm")
        clear = min(abs(p[0]), abs(p[1]))
        print(f"  nearest slit trace is {clear:.2f} mm away "
              f"(it has to beat {SLIT} mm to be clear of the cross)")
        if clear <= SLIT and "--anyway" not in sys.argv:
            print("  REFUSED: that pixel is inside the square the four slit traces box in. "
                  "Turn the view further, or pass --anyway to pick there on purpose.")
            return

        gui.search_tool(page, "Mate connector", settle=3000)
        if not page.locator("#feature-dialog").count():
            raise SystemExit("Mate connector never opened")
        gui.name_feature(page, SPIKE)
        tag = variant + ("-square" if clear <= SLIT else "")
        gui.frame(page, f"{CAP}/{tag}-01-armed.png", park=True)

        # The technique: Shift is held across the hover, not just around the click.
        if variant in ("shift-hover", "shift-click"):
            page.keyboard.down("Shift")
        page.mouse.move(*at)
        page.wait_for_timeout(900)
        gui.frame(page, f"{CAP}/{tag}-02-hover.png")
        if variant == "shift-hover":
            page.keyboard.up("Shift")
            page.wait_for_timeout(300)
        page.mouse.click(*at)
        if variant == "shift-click":
            page.keyboard.up("Shift")
        page.wait_for_timeout(1500)

        print("  Origin entity reads:", origin_entity(page))
        gui.frame(page, f"{CAP}/{tag}-03-picked.png", park=True)
        gui.tick(page)
        page.wait_for_timeout(2000)

        got = readback(page, doc)
        print("  committed:", json.dumps(got))
        print("  it sits at:\n" + (where_is_it(page, doc) or "").rstrip())
        ok = (got and len(got.get("originQuery", [])) == 1
              and not got.get("secondaryOriginQuery")
              and got.get("entityInferenceType") == "CENTER")
        print("  PASS" if ok else "  FAIL")
        gui.frame(page, f"{CAP}/{tag}-04-committed.png", park=True)
        delete_spike(page)


if __name__ == "__main__":
    main()
