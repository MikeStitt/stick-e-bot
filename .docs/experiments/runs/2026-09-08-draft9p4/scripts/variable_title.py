"""What a Variable feature's title holds, and whether anything in the GUI can change it.

    uv run --project . python -u .docs/experiments/runs/2026-09-08-draft9p4/scripts/variable_title.py

draft9p4's variable naming rule says a Variable feature keeps Onshape's title,
`###name = #value`, so its tree row reads its own name and its value. That rule was read
off stored titles in draft9p1p6, and nobody had driven the box. This adds one variable to
`stickbot-draft9p3-check`, frames the title as it arrives and as it fills, looks for every
route a feature is renamed by, and deletes the variable again. It touches no reference
model.

Two controls run beside it, so that a missing rename is read as the Variable feature and
not as a click that did not land: `Extrude`'s dialog is opened and cancelled, and
`torso block`'s row menu is opened and dismissed. Both are renamed the ordinary way.
"""
import sys


from pathlib import Path
from playwright.sync_api import sync_playwright

from stickbot import repo_root
from stickbot import onshape_gui as gui
from stickbot import onshape_session as api

CHECK = api.Doc("555033d6ce000bb44430dd6e",
                "7786456e4391bf899e70d825",
                "74433d23ba8c3b718fe83b85")
HINGE = api.Doc("500752af84dc92deea53f9e4",       # stickbot-draft9p1p6, read only here
                "f30bf96cfeece59f61e0e7b2",
                "62fca6aa5a67b51adcb2318c")
OUT = Path(str(repo_root()) + "/.docs/experiments/runs/"
           "2026-09-08-draft9p4/capture/variable-title")
RED_X = (452, 93)

# every leaf in the menu column, which is where a context menu opens
MENU = """() => Array.from(document.querySelectorAll('li,a,span,div'))
   .filter(e => !e.children.length && (e.innerText||'').trim() && e.getBoundingClientRect().width)
   .map(e => [(e.innerText||'').trim().slice(0,30), Math.round(e.getBoundingClientRect().x)])
   .filter(r => r[1] > 150 && r[1] < 400).map(r => r[0])"""


def say(*a):
    print(*a, flush=True)


def title(page):
    t = page.locator("#feature-dialog .ns-dialog-title").first
    return t.inner_text().strip() if t.count() else None


def pencil(page):
    """The edit-name pencil's box after hovering the title and its hover area."""
    t = page.locator("#feature-dialog .ns-dialog-title").first.bounding_box()
    page.mouse.move(t["x"] + t["width"] / 2, t["y"] + t["height"] / 2)
    page.wait_for_timeout(1000)
    got = page.locator("#feature-dialog .os-dialog-button-edit-name").first.bounding_box()
    if got:
        return got
    area = page.locator("#feature-dialog .ns-dialog-edit-hover-area").first
    if area.count():
        h = area.bounding_box()
        page.mouse.move(h["x"] + h["width"] / 2, h["y"] + h["height"] / 2)
        page.wait_for_timeout(1000)
        got = page.locator("#feature-dialog .os-dialog-button-edit-name").first.bounding_box()
    return got


def shut(page):
    page.keyboard.press("Escape")
    page.wait_for_timeout(1000)
    if page.locator("#feature-dialog").count():
        page.mouse.click(*RED_X)
        page.wait_for_timeout(1200)
    if page.locator("#feature-dialog").count():
        raise RuntimeError("a dialog is still open")


def open_menu(page, name: str):
    page.keyboard.press("Escape")
    page.wait_for_timeout(500)
    page.get_by_text(name, exact=True).locator("visible=true").first.click(button="right")
    page.wait_for_timeout(1500)
    return page.evaluate(MENU)


def click_item(page, word: str):
    hit = page.evaluate(
        """(w) => {
            for (const e of document.querySelectorAll('li,a,span,div')) {
                if (e.children.length) continue;
                if ((e.innerText || '').trim() !== w) continue;
                const r = e.getBoundingClientRect();
                if (r.width && r.height)
                    return [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
            }
            return null; }""", word)
    if not hit:
        raise RuntimeError(f"no {word!r} in the open menu")
    page.mouse.click(*hit)
    page.wait_for_timeout(2500)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser, ctx, page = gui.connect(p)
        gui.open_doc(page, CHECK)
        gui.no_banner(page)
        if page.locator("#feature-dialog").count():
            shut(page)
        start = gui.tree(page)
        say("tree before:", start)

        # --- control: another dialog does offer the pencil -------------------
        gui.search_tool(page, "Extrude", settle=3000)
        say("Extrude dialog title:", repr(title(page)), "pencil:", pencil(page))
        shut(page)

        # --- the Variable dialog as it arrives and as it fills ---------------
        gui.search_tool(page, "Variable", settle=3000)
        say("Variable dialog title on arrival:", repr(title(page)))
        gui.frame(page, OUT / "01-arrives.png")
        say("Variable dialog pencil, nothing filled:", pencil(page))

        nx, ny = gui.at(page, "Name")
        page.mouse.click(nx + 90, ny)
        page.wait_for_timeout(400)
        page.keyboard.type("probe", delay=50)
        page.wait_for_timeout(900)
        say("title after the name alone:", repr(title(page)))
        vx, vy = gui.at(page, "Value")
        page.mouse.click(vx + 90, vy)
        page.wait_for_timeout(400)
        page.keyboard.press("ControlOrMeta+a")
        page.keyboard.type("7 mm", delay=50)
        page.keyboard.press("Tab")
        page.wait_for_timeout(1200)
        say("title after the value:", repr(title(page)))
        gui.frame(page, OUT / "02-filled.png")
        say("Variable dialog pencil, filled:", pencil(page))
        gui.tick(page)

        made = [r for r in gui.tree(page) if r not in start]
        say("tree row as built:", made)
        gui.frame(page, OUT / "03-row.png")

        # --- every route a feature is renamed by -----------------------------
        say("control, torso block's menu:", open_menu(page, "torso block"))
        gui.frame(page, OUT / "04-menu-extrude.png")
        page.keyboard.press("Escape")
        page.wait_for_timeout(700)

        say("the variable's menu:", open_menu(page, made[0]))
        gui.frame(page, OUT / "05-menu-variable.png")
        page.keyboard.press("Escape")
        page.wait_for_timeout(700)

        x, y = gui.row(page, made[0])
        page.mouse.click(x, y)
        page.wait_for_timeout(700)
        page.keyboard.press("F2")
        page.wait_for_timeout(1000)
        say("what F2 focuses:", page.evaluate(
            "() => [document.activeElement.tagName,"
            " String(document.activeElement.className).slice(0, 40)]"))
        page.keyboard.press("Escape")
        page.wait_for_timeout(700)

        # --- leave the check document as it was found ------------------------
        open_menu(page, made[0])
        click_item(page, "Delete")
        say("tree after:", gui.tree(page))
        if gui.tree(page) != start:
            raise RuntimeError("the check document did not come back to where it started")

        # --- the reference, read only ----------------------------------------
        gui.open_doc(page, HINGE)
        gui.no_banner(page)
        say("hinge rows:", gui.tree(page)[:23])
        gui.frame(page, OUT / "06-hinge-tree.png")
        say("a renamed variable's menu in the reference:", open_menu(page, "nose"))
        page.keyboard.press("Escape")
        page.wait_for_timeout(700)


if __name__ == "__main__":
    main()
