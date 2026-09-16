"""Driving Onshape's GUI for a capture, with the guards that stop a bad frame shipping.

Every guard here is a run's finding turned into code. They are not defensive
programming: each one is a specific thing that went out in a published figure, or a
number that read back wrong, and none of them showed on the screen at the time.

    from playwright.sync_api import sync_playwright
    import onshape_gui as gui

    with sync_playwright() as p:
        browser, ctx, page = gui.connect(p)
        gui.open_doc(page, doc)
        gui.frame(page, images / "stud.revolve-01.png")

What each tool is called and where it lives is `.docs/onshape-gui-howto.md`. How a
capture is conducted is `.docs/build/takes.md`.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

from stickbot import onshape_screen as screen
from stickbot import onshape_session as api

AGENT_PORT = 9223
ONSHAPE = "https://cad.onshape.com"

GREEN_TICK = (423, 93)          # the tick at the top of an open feature dialog
RED_X = (451, 93)               # the cross beside it

# Somewhere on the canvas with nothing on it, for clearing a selection.
EMPTY = (300, 900)


def connect(playwright, port: int = AGENT_PORT):
    """Attach to the agent's browser, on a CAD tab.

    9223 is the agent's browser; 9222 is the user's own signed-in window and is never
    driven. Passing 9222 is refused rather than honored, because every other guard in
    this file is worthless if the clicks land in somebody else's session.
    """
    if port != AGENT_PORT:
        raise ValueError(f"port {port} is not the agent's browser; 9223 only")
    api.CDP_URL = f"http://127.0.0.1:{port}"
    browser = playwright.chromium.connect_over_cdp(api.CDP_URL)
    ctx = browser.contexts[0]
    for page in ctx.pages:
        if page.url.startswith(ONSHAPE):
            return browser, ctx, page
    page = ctx.new_page()
    page.goto(f"{ONSHAPE}/documents", wait_until="domcontentloaded")
    page.wait_for_timeout(4500)
    return browser, ctx, page


def open_doc(page, doc: api.Doc, settle: int = 11000):
    """Put the page on this document, if it is not already there.

    Named lookup lags document creation by minutes, so a capture carries the ids it
    was given rather than searching for the name on every call.
    """
    if not page.url.startswith(doc.url):
        page.goto(doc.url, wait_until="domcontentloaded")
        page.wait_for_timeout(settle)
    return doc


# --- the guards ---------------------------------------------------------------


def viewport(page):
    """Refuse a window that is not the size the pixel masks were measured against."""
    got = page.evaluate("() => [window.innerWidth, window.innerHeight]")
    if tuple(got) != screen.WINDOW:
        raise RuntimeError(
            f"the window is {got[0]}x{got[1]}, not {screen.WINDOW[0]}x{screen.WINDOW[1]}; "
            "every mask in onshape_screen is measured against that size")


BANNER_BAND = (86, 116, 480)     # top, bottom, left edge of the notification strip


def no_banner(page, tries: int = 14, gap: int = 2500):
    """Dismiss Onshape's notification strip rather than photographing it.

    Nine of run 8's figures went out with one in them — a rendering-performance
    notice, and a leftover *Sketch 1 has been canceled* from the script before.

    **A banner is text, not a control.** A Variable Studio puts its own
    *Insert Variable Studio* button in the same band, and reading that as a banner
    refuses every frame in the tab — there is no × to dismiss, so it never clears.
    Anything inside a button or a link is chrome and is skipped.

    **A feature's prompt is not a banner either.** *Select a sketch plane* sits in the
    same band in a `.speech-bubble`, and it is the thing the frame is meant to show:
    it tells the reader what the tool is waiting for. It has no ×, so reading it as a
    banner refuses every frame taken while a feature is waiting for a pick.

    **A panel header is not a banner either.** *Features (6)* sits at y=114 in a
    `.left-panel-header`, which is inside the band. It stays left of the band's left
    edge until a panel to its left is widened, and then it is read as a banner that
    has no × and never clears — so widening the versions panel silently refused every
    frame after it.

    **A feature list row is not a banner either.** A Part Studio that declares its own
    variables lists them above its features, so the top of the head tab's list reads
    `#headW = 72 mm`. Those rows sit left of the band until the versions panel is opened
    and pushes the list right, and then they are read as a notice with no × that never
    clears. They cannot be scrolled out of the way, because the list keeps them pinned
    under its header, so the rows themselves are skipped: a banner is never a tree row.

    **A keyboard-shortcut badge is not a banner either.** The constraint flyout hangs
    below the sketch toolbar, and its first row — *Coincident* — puts the letter `i`
    in a `.shortcut-key` at y=94. A one-letter badge with no × refused every frame of
    the flyout being opened, which is the frame the page is there to take.

    **A dimension's box is not a banner either.** It is dragged by a handle of three
    small squares, and the box follows the label, so a dimension placed near the top of
    the canvas puts that handle at y=115. It is the thing the frame is there to show and
    it has no ×, so it refused every `field` frame of a dimension placed high.

    **A picker's own tabs are not a banner either.** The Select Part Studio panel that
    Derived opens puts *Current document* and *Other documents* at y=124, inside the band
    and inside no dialog this function knew about. They have no ×, so every frame taken
    while the panel was open was refused — and the panel is what those frames are for.
    Anything inside `.select-item-wrapper` is that panel.

    **A tool's own prompt has been renamed and is not a banner either.** *Select an
    additional point, plane, or axis to specify where the angle is measured from* is
    what Plane says while it waits for its second entity, and it arrives in a
    `.osx-message-bubble.alert-info` rather than the `.speech-bubble` this function was
    taught. It has no ×, so it refused every frame of a plane being built, for as long
    as the script was willing to wait. A message bubble is skipped only while a feature
    dialog is open, because *Sketch 1 has been canceled* comes in the same bubble and
    that one arrives with no dialog on screen.

    **A modal dialog is not a banner either.** *Workspace units* puts its *Length* label at
    y=118, and it is the thing the frame is there to show. It has a × of its own that discards
    the change silently, so clicking it would be worse than refusing the frame. Anything inside
    a `[role=dialog]` is skipped, the same way anything inside the feature dialog already is.

    **A banner with no × is waited out, not clicked away.** *Sketch 1 has been
    canceled* carries no close control and fades on its own after something like half
    a minute, so the patience here is set to outlast it. It costs nothing when there
    is no banner, because the first look returns.
    """
    top, bottom, left = BANNER_BAND
    for _ in range(tries):
        band = page.evaluate(
            """([top, bottom, left]) => {
                const out = [];
                const inTool = !!document.querySelector('#feature-dialog');
                for (const e of document.querySelectorAll('*')) {
                    if (e.children.length) continue;
                    const t = (e.innerText || '').trim();
                    if (!t) continue;
                    const r = e.getBoundingClientRect();
                    if (r.y < top || r.y > bottom || r.x < left || !r.width) continue;
                    if (e.closest('#feature-dialog')) continue;
                    if (e.closest('[role=dialog]')) continue;
                    if (e.closest('button, a, [role=button]')) continue;
                    if (e.closest('.speech-bubble, .os-bubble-message')) continue;
                    if (inTool && e.closest('.osx-message-bubble')) continue;
                    if (e.closest('.left-panel-header')) continue;
                    if (e.closest('.os-list-item')) continue;
                    if (e.closest('.shortcut-key')) continue;
                    if (e.closest('.dimension-dialog')) continue;
                    if (e.closest('.select-item-wrapper')) continue;
                    out.push(t.slice(0, 60));
                }
                return out; }""", [top, bottom, left])
        if not band:
            return
        print(f"  a banner is in the way: {band}")
        closed = page.evaluate(
            """([top, bottom]) => {
                for (const e of document.querySelectorAll('*')) {
                    const r = e.getBoundingClientRect();
                    if (r.y < top - 1 || r.y > bottom + 2 || r.x < 1000) continue;
                    if (r.width > 40 || !r.width) continue;
                    const t = (e.innerText || '').trim();
                    if (t === '×' || t === 'x' || t === '') {
                        if (typeof e.click === 'function') e.click();
                        else e.dispatchEvent(new MouseEvent('click', {bubbles: true}));
                        return [Math.round(r.x), Math.round(r.y)];
                    }
                }
                return null; }""", [top, bottom])
        print("  dismissed at", closed)
        page.wait_for_timeout(gap)
    raise RuntimeError("a notification banner will not go away; do not shoot through it")


def still(page, tries: int = 12, gap: int = 1400, quiet: int = 300):
    """Wait until nothing on the canvas is moving.

    A spinner and a *Poor connection...* toast were in the frame of run 8p1's `bs-34`
    before this existed: the midpoint constraint had not reached the server, so the
    figure showed the slot still sitting where it was drawn.

    `quiet` is in changed pixels. A blinking caret in a name box is a couple of
    hundred; a spinner is thousands and it never stops.
    """
    a = None
    for _ in range(tries):
        toast = page.get_by_text("Poor connection", exact=False).locator("visible=true").count()
        b = screen.shot(page)
        if a is not None and not toast and screen.changed(a, b) < quiet:
            return
        a = b
        page.wait_for_timeout(gap)
    raise RuntimeError("the screen will not settle; do not shoot a moving frame")


# --- frames -------------------------------------------------------------------


def frame(page, path, clip=None, park=False) -> Path:
    """A frame a page will publish: guarded, and written where the page names it.

    `clip` is an optional {x, y, width, height} for a frame that is about one
    control rather than the whole window. The published tree shot is 210x640, so a
    crop is part of the convention, not an exception to it — but the guards run
    either way, because a banner outside the crop still means the page is unsettled.

    `park` moves the pointer to `EMPTY` first. Onshape draws a small badge beside
    the pointer over a variable table and a highlight under it in the graphics
    area, and either lands in the published picture on top of whatever it happens
    to cover. A frame that is not about where the pointer is should not carry it.
    """
    if park:
        page.mouse.move(*EMPTY)
        page.wait_for_timeout(400)
    viewport(page)
    no_banner(page)
    still(page)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(path), clip=clip) if clip else page.screenshot(path=str(path))
    print(f"  frame {path.parent.name}/{path.name}")
    return path


def probe(page):
    """A frame nobody publishes, for measuring. No guards, no file."""
    return screen.shot(page)


def ring(page, path, at, radius: int = 30, clip=None) -> Path:
    """A frame with a ring drawn on the pixel the click is about to land on.

    The close-up of a pick answers *which one*, and at medium range a vertex, the
    sketch point under it and the edge through it are one blob. The ring is drawn
    from the same pixel the click uses, so the ring and the click cannot disagree —
    which is the failure a frame ringed by hand invites, and it is invisible in the
    finished picture.

    Shoot the medium view, zoom, ring the close-up, then click from the close-up's
    camera: a zoom moves the pixel the ring was measured in.
    """
    path = frame(page, path, clip=clip)
    im = Image.open(path).convert("RGB")
    # The screenshot is in device pixels and `at` is in CSS pixels, so the ring has to be
    # scaled by however many device pixels the picture spans — the clip's width when there
    # is a clip, the window's when there is not. Dividing by the window either way put
    # every ring on a cropped frame a fixed fraction of the way in from its left edge:
    # draft9p2 ringed the Insert panel's `body` row and got the ring up in the corner on
    # `Current document`, in a picture that otherwise looked right.
    span = clip["width"] if clip else page.evaluate("() => window.innerWidth")
    scale = im.width / span
    x = (at[0] - (clip["x"] if clip else 0)) * scale
    y = (at[1] - (clip["y"] if clip else 0)) * scale
    r = radius * scale
    # A ring drawn outside the picture is a ring nobody can see, on a frame whose words
    # say a thing is circled. The upper limb's connector sat at y=1298 in a window 1000
    # tall, because the close-up zoomed about the canvas center and the far end of the rod
    # went off the bottom. Zoom about the point itself, or reframe, and shoot again.
    if not (0 <= x < im.width and 0 <= y < im.height):
        path.unlink()
        raise RuntimeError(
            f"{path.stem}: the ring is at ({int(x)}, {int(y)}) in a picture "
            f"{im.width} by {im.height}, so it falls outside the frame")
    draw = ImageDraw.Draw(im)
    draw.ellipse([x - r, y - r, x + r, y + r], outline=(214, 40, 40), width=max(2, round(3 * scale)))
    im.save(path)
    print(f"  ring at {int(at[0])},{int(at[1])}")
    return path


# --- picking ------------------------------------------------------------------


def pick(page, xy, what: str, add: bool = False, expect: bool = True) -> int:
    """A canvas pick, checked: after it, more of the model is selected than before.

    Run 8's pattern spike lost one of four sides silently and patterned three. The
    frame looked right, the count was right, and the shape was wrong.
    """
    before = screen.selected(probe(page))
    page.mouse.move(*xy)
    page.wait_for_timeout(400)
    if add:
        page.keyboard.down("Shift")
    page.mouse.click(*xy)
    if add:
        page.keyboard.up("Shift")
    page.wait_for_timeout(800)
    after = screen.selected(probe(page))
    print(f"  pick {what:34s} at {int(xy[0]):5d},{int(xy[1]):4d}   selected {before} -> {after}")
    if expect and after <= before:
        raise RuntimeError(f"pick {what!r} did not select anything ({before} -> {after})")
    return after


def clear(page, xy=EMPTY):
    """Nothing selected, so the next pick's count means what it says."""
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)
    page.mouse.click(*xy)
    page.wait_for_timeout(600)


# The graphics area, cropped clear of the toolbars, for before-and-after comparison.
MODEL_CROP = (slice(76, 970), slice(246, 1600))


def model_pixels(page):
    return probe(page)[MODEL_CROP]


def moved(page, before, what: str, least: int = 300) -> int:
    """A drag is only proof of a degree of freedom if the geometry moved.

    A drag that misses its target leaves the screen exactly as it found it, which
    looks the same as a sketch with nothing left to move.
    """
    n = screen.changed(before, model_pixels(page))
    print(f"  {what}: {n} pixels changed")
    if n < least:
        raise RuntimeError(f"{what} moved nothing ({n} pixels); the drag missed")
    return n


def cursor(page) -> str:
    """`confirm` while a pattern is waiting to be accepted; `default` once it is."""
    c = page.evaluate("() => getComputedStyle(document.querySelector('canvas')).cursor")
    return "confirm" if "Confirmation_Cursor" in c else c


# --- numbers into fields ------------------------------------------------------


def number_fields(page):
    """Visible number inputs in the open dialog, top to bottom."""
    h = page.evaluate_handle(
        """() => Array.from(document.querySelectorAll('input.os-param-number'))
            .filter(e => e.getBoundingClientRect().width)
            .sort((a, b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y)""")
    return [h.get_property(str(i)).as_element()
            for i in range(int(h.get_property("length").json_value()))]


def set_field(page, el, expression: str):
    """Type an expression into a specific input. Never leaves focus in it."""
    el.click()
    page.wait_for_timeout(300)
    el.fill(expression)
    page.wait_for_timeout(400)
    el.press("Enter")
    page.wait_for_timeout(1800)


def set_focused_number(page, expression: str):
    """Type into whatever has focus, having checked that it is a field.

    A bare keystroke with the graphics area focused runs as a shortcut: run 7's
    depth read back as `f` because the `f` meant to zoom went into the box.
    """
    if page.evaluate("() => document.activeElement.tagName") != "INPUT":
        raise RuntimeError(f"no field has focus; {expression!r} would go to the canvas")
    el = page.evaluate_handle("() => document.activeElement").as_element()
    el.fill(expression)
    page.wait_for_timeout(400)
    el.press("Enter")
    page.wait_for_timeout(2000)


def fill_box(page, box, text: str) -> str:
    """Fill a DOM input and read it back.

    `Control+A` is line-start on macOS, so selecting and typing appended instead of
    replacing: a pattern count of 4 went in after an existing 3 and made 43.
    """
    box.fill(text)
    page.wait_for_timeout(400)
    got = box.input_value()
    if got != text:
        raise RuntimeError(f"the box holds {got!r}, not {text!r}")
    return got


# --- dialogs ------------------------------------------------------------------


def labels(page):
    """Every leaf label in the open feature dialog, with where it sits."""
    return page.evaluate(
        """() => Array.from(document.querySelectorAll('#feature-dialog *'))
            .filter(e => !e.children.length && (e.innerText || '').trim())
            .map(e => { const r = e.getBoundingClientRect();
                return r.width ? [(e.innerText || '').trim().slice(0, 34),
                                  Math.round(r.x + r.width / 2),
                                  Math.round(r.y + r.height / 2)] : null; })
            .filter(Boolean)""")


def at(page, label: str) -> tuple[int, int]:
    """Where a labeled control in the open dialog is."""
    for text, x, y in labels(page):
        if text == label:
            return (x, y)
    raise RuntimeError(f"{label!r} is not in the dialog: {labels(page)}")


def tick(page, tries: int = 3):
    """Accept the open feature dialog, and be sure it actually closed.

    A run shot its next figure over a dialog that was still open: the click landed,
    the dialog did not go. One tick per feature is not a safe assumption.
    """
    for _ in range(tries):
        if not page.locator("#feature-dialog").count():
            return
        page.mouse.click(*GREEN_TICK)
        page.wait_for_timeout(2500)
    if page.locator("#feature-dialog").count():
        raise RuntimeError("the dialog would not accept")


def name_feature(page, new: str):
    """Name the open feature in its dialog header, the way the page tells the reader to.

    The name box is not summoned by clicking the title — it is summoned by the small
    pencil to the title's right.
    """
    title = page.locator("#feature-dialog .ns-dialog-title").first
    t = title.bounding_box()
    if not t:
        raise RuntimeError("no dialog title; is a feature dialog open?")
    page.mouse.move(t["x"] + t["width"] / 2, t["y"] + t["height"] / 2)   # the pencil
    page.wait_for_timeout(700)                                          # appears on hover
    b = page.locator("div.os-dialog-button-edit-name").first.bounding_box()
    if not b:
        raise RuntimeError("the edit-name pencil did not appear on hover")
    page.mouse.click(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2)
    page.wait_for_timeout(900)
    box = page.locator("input.os-dialog-header-rename-textbox")
    if not box.count():
        raise RuntimeError("the pencil did not summon the name box")
    page.keyboard.press("ControlOrMeta+a")
    page.keyboard.type(new, delay=45)
    page.wait_for_timeout(500)
    got = box.first.input_value()
    if got != new:
        raise RuntimeError(f"name box holds {got!r}, not {new!r}")
    page.keyboard.press("Enter")                                        # commit and let go
    page.wait_for_timeout(700)
    # The box stays in the page after Enter; what changes is where the keyboard is. Asking whether
    # the input still exists always answers yes and proves nothing.
    held = page.evaluate("() => (document.activeElement || {}).className || ''")
    if "rename-textbox" in held:
        raise RuntimeError("the name box still holds the keyboard after Enter")
    if not page.locator("#feature-dialog").count():
        raise RuntimeError("naming the feature closed its dialog")


# --- the tree and the parts list ----------------------------------------------


def tree(page) -> list[str]:
    """Every row of the feature tree, in order."""
    return page.evaluate(
        """() => Array.from(document.querySelectorAll('.os-list-item'))
            .map(e => e.innerText.trim().split('\\n')[0]).filter(Boolean)""")


def _split_parts(rows: list[str]) -> tuple[list[str], list[str]]:
    """The feature rows, and the parts pane under them."""
    for i, r in enumerate(rows):
        if r.startswith("Parts ("):
            return rows[:i], rows[i:]
    return rows, []


def tree_all(page) -> list[str]:
    """Every row of the feature list, read at both ends and stitched together.

    Onshape keeps only about thirty rows in the page at a time, so a list longer than that
    is read short at whichever end is furthest from the scroll, and a row that is not drawn
    reads exactly like a row that is not there. Tutorial 6's third connector was recorded as
    creating nothing for that reason, and two steps before it were recorded as deleting
    `Default geometry`.

    The list is read at the top and again at the bottom, and the second reading contributes
    only the feature rows the first did not have. Feature names are unique inside a Part
    Studio, so the join is exact.

    The parts pane is pinned to the foot of the panel and is drawn whatever the scroll, so it
    is taken off both readings before they are joined and put back afterwards. Left in, it
    lands in the middle of the stitched list and everything after it reads as parts — which
    is how the first version of this function lost the very rows it was written to find. Its
    rows are not unique, so anything counting parts uses `tree` and scrolls to them itself.
    """
    page.mouse.move(140, 400)
    page.mouse.wheel(0, -4000)
    page.wait_for_timeout(700)
    out, parts = _split_parts(tree(page))
    page.mouse.wheel(0, 4000)
    page.wait_for_timeout(700)
    tail, more = _split_parts(tree(page))
    out.extend(r for r in tail if r not in out)
    return out + (parts if len(parts) >= len(more) else more)


# The feature list starts here. Above it are the filter box and the row of icons whose
# leftmost, at (155, 130), is `New folder`.
LIST_TOP = 145
LIST_POINT = (140, 420)


def list_scroll_to(page, name: str, tries: int = 16):
    """Wheel the feature list until the row called `name` is in it.

    The list holds only the rows it is showing. A row that has scrolled off the panel
    is not in the page at all, so `get_by_text` finds nothing and a wait for it times
    out rather than saying what is wrong.
    """
    here = page.get_by_text(name, exact=True).locator("visible=true")
    if here.count():
        return True
    page.mouse.move(*LIST_POINT)
    page.mouse.wheel(0, -6000)
    page.wait_for_timeout(600)
    for _ in range(tries):
        if page.get_by_text(name, exact=True).locator("visible=true").count():
            return True
        page.mouse.wheel(0, 300)
        page.wait_for_timeout(350)
    return False


def row(page, name: str) -> tuple[int, int]:
    """Where a named row sits, in the tree or the parts list.

    Scrolled into view first, and refused if it is still above the list. `bounding_box`
    answers for a row that has scrolled out of the panel as readily as for one on
    screen, and the answer is a point somewhere over the panel's own header. In
    `stickbot-draft9p2`'s head, where twelve variables sit in front of the geometry, it
    put `Front` at y=122 — eight pixels off the `New folder` button. Three runs clicked
    there, made a folder, and left the sketch toolbar grayed out behind its rename box.
    """
    if not list_scroll_to(page, name):
        raise RuntimeError(f"no row called {name!r} is in the feature list")
    el = page.get_by_text(name, exact=True).locator("visible=true").first
    el.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    b = el.bounding_box()
    y = round(b["y"] + b["height"] / 2)
    if y < LIST_TOP:
        raise RuntimeError(
            f"the row for {name!r} reads y={y}, above the feature list at y={LIST_TOP}: "
            f"it is scrolled out of the panel and a click there would land on its header")
    return (round(b["x"] + b["width"] / 2), y)


def rename_row(page, old: str, new: str):
    """Rename through the row's context menu, never the dialog header.

    A name typed with the graphics area focused runs as shortcuts: `stud profile`
    toggled the planes and armed an equal constraint.
    """
    page.keyboard.press("Escape")
    page.wait_for_timeout(500)
    page.get_by_text(old, exact=True).locator("visible=true").first.click(button="right")
    page.wait_for_timeout(1200)
    hit = page.evaluate(
        """() => {
            for (const e of document.querySelectorAll('li,a,span,div')) {
                if (e.children.length) continue;
                if ((e.innerText || '').trim() !== 'Rename') continue;
                const r = e.getBoundingClientRect();
                if (r.width && r.height)
                    return [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
            }
            return null; }""")
    if not hit:
        raise RuntimeError(f"no Rename in the menu for {old!r}")
    page.mouse.click(*hit)
    page.wait_for_timeout(1000)
    if page.evaluate("() => document.activeElement.tagName") != "INPUT":
        raise RuntimeError(f"rename field never took focus for {old!r}")
    page.keyboard.press("ControlOrMeta+a")
    page.keyboard.type(new, delay=70)
    page.keyboard.press("Enter")
    page.wait_for_timeout(1500)


# --- reaching a tool ----------------------------------------------------------


def search_tool(page, name: str, settle: int = 2500):
    """Arm a tool through Search tools rather than its letter.

    A sketch tool's letter is a toggle, so it turns the tool off as often as on and
    the picks that follow land as plain selection clicks.
    """
    page.keyboard.press("Alt+c")
    page.wait_for_timeout(700)
    held = page.evaluate("() => (document.activeElement || {}).className || ''")
    if "rename-textbox" in held:
        raise RuntimeError(
            "Search tools did not take the keyboard; the feature's name box still has it, "
            "so the tool's name would be typed into the name"
        )
    page.keyboard.type(name, delay=60)
    page.wait_for_timeout(1500)
    page.keyboard.press("Enter")
    page.wait_for_timeout(settle)


def dimension(page, picks, label_px, expression: str, settle: int = 1500):
    """Arm Dimension, pick, place the label clear of the model, set the expression.

    The label goes clear of the model because a label click that lands on an edge
    makes a two-entity dimension instead of opening the field.
    """
    page.keyboard.press("Escape")
    page.wait_for_timeout(700)
    search_tool(page, "Dimension", settle=2000)
    for spot in picks:
        page.mouse.move(*spot)
        page.wait_for_timeout(400)
        page.mouse.click(*spot)
        page.wait_for_timeout(800)
    page.mouse.click(*label_px)
    page.wait_for_timeout(settle)
    set_focused_number(page, expression)
    page.keyboard.press("Escape")
    page.wait_for_timeout(700)


# --- the view -----------------------------------------------------------------


def wake(page, at_px=None):
    """Make the canvas draw. A mouse move over empty space does not.

    A wheel in and a wheel straight back out is the smallest thing that does, and it
    leaves the scale where it found it: one event multiplies by 2**(1/12), the other
    divides by it.
    """
    at_px = at_px or screen.CENTER
    page.mouse.move(*at_px)
    page.wait_for_timeout(150)
    page.mouse.wheel(0, -120)
    page.wait_for_timeout(250)
    page.mouse.wheel(0, 120)
    page.wait_for_timeout(600)


def fit(page):
    """Zoom to fit, with the pointer on the canvas so the key reaches the view."""
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("f")
    page.wait_for_timeout(1500)


def planes_hidden(page) -> bool:
    """Are Top, Front and Right hidden? Their tree rows carry the answer.

    Refused when the three rows are not all in the list. A closed `Default geometry` has no
    plane rows at all, and Onshape draws only the rows near the scroll position, so a row
    that cannot be read looks exactly like a plane that is not hidden. Answering `False`
    there told `planes(shown=False)` there was nothing to press: `body`'s Boolean frame came
    out with two planes across it and the part fitted to them rather than to itself.
    """
    rows = page.evaluate(
        """() => { const want = ['Top', 'Front', 'Right'];
            return Array.from(document.querySelectorAll('.os-list-item-name'))
                .filter(e => want.includes((e.innerText || '').trim()))
                .map(e => e.closest('.os-list-item').className) }""")
    if len(rows) != 3:
        raise RuntimeError(
            f"Top, Front and Right are not all in the feature list ({len(rows)} of 3 found): "
            f"open Default geometry and scroll it into view before asking about the planes")
    return all("ns-list-item-hidden" in c for c in rows)


def planes(page, shown: bool) -> bool:
    """Put the three default planes into a known state. True if `p` had to be pressed.

    `p` is a toggle, and a take that presses it because the page says to press it shows
    the planes as often as it hides them. The revolve's finished-part frame came out
    with all three planes across it and the part fitted to them rather than to itself,
    because the pass before had already hidden them.

    A step that teaches `p` calls this for `shown` first, so the reader's state and the
    take's are the same one; a later step calls it for hidden without recording a key,
    because the reader hid them once and they stayed hidden.
    """
    if planes_hidden(page) is not shown:      # hidden and wanted hidden, or shown and
        return False                          # wanted shown: nothing to press
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("p")
    page.wait_for_timeout(1500)
    return True


def one_camera(page, tries: int = 3):
    """The camera as the canvas last drew it, however the view is moving.

    `screen.camera` clears the record before it waits, so the wake has to happen
    inside that window rather than before it.
    """
    for _ in range(tries):
        cam = screen.camera(page)
        if cam is not None:
            return cam
        page.evaluate("() => window.__cam.seen = []")
        wake(page)
        cam = screen._model_camera(page.evaluate("() => window.__cam.seen"))
        if cam is not None:
            return cam
    raise RuntimeError("no full-viewport camera; is the hook installed?")


def px_per_mm(page, tries: int = 3, still: int = 4):
    """Pixels per millimeter, and the camera it came from, once the view has stopped.

    `f` and the view cube both animate, and a reading taken part way through one
    describes a view that is already gone; every pick computed from it then lands
    somewhere else. Two readings that agree on the scale and on where the origin lands
    are a view that has arrived. A view that will not settle still gets an answer, with
    a line saying so, because a reading of a moving view is what this returned before
    and some of it is right.
    """
    last = None
    for _ in range(still):
        cam = one_camera(page, tries)
        now = (screen.scale(cam), screen.project(cam, 0, 0, 0))
        if last is not None:
            (s0, o0), (s, o) = last, now
            if (abs(s - s0) <= 0.005 * max(s, s0)
                    and abs(o[0] - o0[0]) <= 2 and abs(o[1] - o0[1]) <= 2):
                return s, cam
        last = now
    s, o = last
    print(f"  the view is still moving after {still} readings; taking {s:.2f} px/mm with "
          f"the origin at {o[0]:.0f}, {o[1]:.0f}", flush=True)
    return s, cam


def project(page, x_mm: float, y_mm: float, z_mm: float = 0.0, cam=None):
    """A model point in millimeters to the pixel it is drawn at."""
    cam = cam or screen.camera(page)
    if cam is None:
        raise RuntimeError("no full-viewport camera; nudge the mouse and try again")
    return screen.project(cam, x_mm / 1000, y_mm / 1000, z_mm / 1000)


def zoom_to(page, target: float, at_px=None, tries: int = 4):
    """Wheel until the scale is `target` pixels per millimeter.

    One wheel event multiplies the scale by 2**(1/12). Zooming with the pointer on a
    point keeps that point still, so `at_px` defaults to the canvas center, where a
    freshly opened sketch puts the origin.
    """
    at_px = at_px or screen.CENTER
    for _ in range(tries):
        s, cam = px_per_mm(page)
        if abs(s - target) / target < 0.03:
            return s, cam
        n = round(math.log2(target / s) * 12)
        if n == 0:
            return s, cam
        page.mouse.move(*at_px)
        for _ in range(abs(n)):
            page.mouse.wheel(0, -120 if n > 0 else 120)
            page.wait_for_timeout(30)
        page.wait_for_timeout(900)
    return px_per_mm(page)
