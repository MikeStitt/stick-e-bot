"""Shared bits for the draft9p0 build. Probe-script rules apply: this lives in the
session scratchpad and is not held to the repo's gates."""
import json, os, sys, secrets
from pathlib import Path

REPO = Path("/Users/mikestitt/projects/first/2027/sponge")
sys.path.insert(0, str(REPO / "tools"))
HERE = Path(__file__).parent
STATE = HERE / "state.json"
MARK = "DRAFT9P0_BUILD"


def load():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save(**kw):
    s = load(); s.update(kw); STATE.write_text(json.dumps(s, indent=2)); return s


def marks(ctx):
    out = []
    for pg in ctx.pages:
        try:
            out.append((pg, pg.evaluate("window.name")))
        except Exception:
            pass
    return out


def mypage(ctx):
    hits = [p for p, n in marks(ctx) if n == MARK]
    if len(hits) != 1:
        raise SystemExit(f"expected exactly one page marked {MARK}, found {len(hits)}")
    return hits[0]


def menu_item(page, text):
    return page.evaluate(
        """(t) => { for (const e of document.querySelectorAll('li,a,span,div')) {
             if (e.children.length) continue;
             if ((e.innerText || '').trim() !== t) continue;
             const r = e.getBoundingClientRect();
             if (r.width && r.height) return [Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)];
           } return null; }""", text)


def delete_row(page, gui, name):
    x, y = gui.row(page, name)
    page.mouse.click(x, y, button="right")
    page.wait_for_timeout(1200)
    hit = menu_item(page, "Delete")
    if not hit:
        raise SystemExit(f"no Delete in the menu for {name!r}")
    page.mouse.click(*hit)
    page.wait_for_timeout(2500)


def _one(node):
    """bodydetails returns a list, massproperties a dict — take the single body either way."""
    return node[0] if isinstance(node, list) else list(node.values())[0]


def faces(page, api, did, wid, eid, pid):
    r = api.api(page, "GET",
                f"/api/parts/d/{did}/w/{wid}/e/{eid}/partid/{pid}/bodydetails")
    return _one(r["body"]["bodies"])["faces"]


def volume(page, api, did, wid, eid, pid):
    r = api.api(page, "GET",
                f"/api/parts/d/{did}/w/{wid}/e/{eid}/partid/{pid}/massproperties")
    return round(_one(r["body"]["bodies"])["volume"][0] * 1e9, 3)


def bbox(page, api, did, wid, eid):
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/boundingboxes")
    return {k: round(v * 1000, 3) for k, v in r["body"].items() if k[0] in "lh"}


def add_var(page, gui, name, value, kind="Length", settle=1500):
    """One Variable feature. kind is Length or Angle; value is an expression."""
    gui.search_tool(page, "Variable")
    page.wait_for_timeout(1000)
    if kind == "Angle":
        page.mouse.click(332, 149)
        page.wait_for_timeout(600)
    els = page.query_selector_all("#feature-dialog input")
    els[1].click()
    page.keyboard.press("Meta+A")
    page.keyboard.type(name.lstrip("#"))
    page.wait_for_timeout(300)
    els[2].fill(value)
    page.wait_for_timeout(300)
    page.keyboard.press("Tab")
    page.wait_for_timeout(600)
    gui.tick(page)
    page.wait_for_timeout(settle)


def features(page, api, did, wid, eid):
    """[(name, featureId, status)] in tree order. Both payloads are BTM-wrapped."""
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
    st = {row["key"]: row["value"]["message"]["featureStatus"]
          for row in r["body"]["featureStates"]}
    out = []
    for f in r["body"]["features"]:
        m = f["message"]
        out.append((m["name"], m["featureId"], st.get(m["featureId"], "?")))
    return out


JROW = """(t) => { const out=[];
  for (const e of document.querySelectorAll('span,div,a')) {
    if (e.children.length) continue;
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.x < 250) out.push([Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
  } return out; }"""


def jrow(page, text):
    """The one tree row with this exact label, by DOM. gui.row matches the toolbar too."""
    hits = page.evaluate(JROW, text)
    if len(hits) != 1:
        raise SystemExit(f"{len(hits)} rows named {text!r}: {hits}")
    return tuple(hits[0])


def scroll_tree(page, n):
    page.mouse.move(150, 400)
    for _ in range(abs(n)):
        page.mouse.wheel(0, -120 if n > 0 else 120)
        page.wait_for_timeout(40)
    page.wait_for_timeout(800)


def edit_row(page, gui, name, settle=3500):
    """Right-click a feature row and take Edit; dblclick is unreliable low in the tree."""
    x, y = jrow(page, name)
    page.mouse.click(x, y, button="right")
    page.wait_for_timeout(1500)
    hit = menu_item(page, "Edit feature") or menu_item(page, "Edit")
    if not hit:
        raise SystemExit(f"no Edit in the menu for {name!r}")
    page.mouse.click(*hit)
    page.wait_for_timeout(settle)
