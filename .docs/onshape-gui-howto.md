# Driving Onshape's GUI

Read this before driving the browser. It covers connecting and identifying your page, reading an
error, creating a document, selecting, tools and dialogs, sketching, measuring, rendering, and
read-only REST.

**Section 2 comes before the building sections on purpose.** Run 5 posted eleven broken mates
before finding out where Onshape keeps the message that said why, so how to read a failure is
here ahead of how to make one.

Assembled 2026-08-11 from run 1's reports in [`runs/2026-08-11-run1/`](runs/2026-08-11-run1/),
extended after run 2 from the three `build-notes.md` files under
[`build-log/`](build-log/), and after run 5 from
[`experiments/runs/2026-08-13-run5/`](experiments/runs/2026-08-13-run5/). Where something was seen
once rather than established, it says so.

**Where run 1 and run 2 disagree, both are recorded.** Onshape's dialog defaults are not stable
between sessions, and treating one run's observation as a rule is itself a way to lose an hour.

## The hard rules, before anything else

- **Port 9223 only. Never 9222** — that is the user's own browser.
- **Never close a page you did not create.** Never `bring_to_front()`. Never close the context
  or the browser — closing the context destroys the shared login for everyone.
- **Every Bash call under 90 s**, with an explicit timeout. Every Python script must terminate;
  wrap Playwright in `with sync_playwright() as p:` so it does.
- **GUI only for geometry. REST is read-only**, for verification.

## 0. Onshape is Z-up, and this changes every sketch

- **Top** = XY, normal **Z** · **Front** = XZ, normal **Y** · **Right** = YZ, normal **X**.
- "Vertical" is **Z**. "Fore-and-aft" — and so a hinge axis, and the direction of a Mirror about
  Front — is **Y**.

Getting this wrong puts every sketch on the wrong plane, and the model still builds.

## 1. Connect, and know which page is yours

**Run every script with `.venv/bin/python` from the repository root.** Plain `python` and
`python3` do not have Playwright. The environment is `uv`-managed, so `uv run python` works too;
`guide/.venv/bin/python` appears in older notes and no longer exists.

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    ctx = b.contexts[0]
    page = ctx.new_page()          # this one is yours
```

**`onshape_session.CDP_URL` is 9223, the agent's browser, and 9222 is reached by naming it.**
9222 is the browser a person signed in to and is sitting in front of. Until draft9p1p6 the default
was 9222 and only `onshape_gui.connect()` moved it, so a script that imported `onshape_gui` landed
in the agent's browser and a script that imported only `onshape_session` did not; draft9p1p6 ran
its whole Phase C and Phase D through the person's browser before a capture of a sign-in screen
gave it away. **A default that reaches somebody else's session is the failure**, because nothing
in the answer says which browser served it.

**Identifying your page later is the trap.** There are six or more near-identical Onshape tabs
open. Matching on title or URL *will* find someone else's document — in run 1 this happened
twice, once to an agent and once to the session driving it, and both nearly typed into another
document's rename box.

The reliable pattern: **stamp your own page, once, immediately after creating it**, then find it
by that stamp and nothing else.

**A stamp is a convention, not a guarantee, so look before you stamp and fail on any count that
is not one.** In run 3 an agent found its assigned stamp already sitting on another agent's page;
a lookup returning the first match would have driven the whole build into someone else's
document. Copy a prompt, hard-code a default, or leave a page from an earlier run carrying the old
name, and the collision comes back with nothing to detect it. The assertion is what turns an
undetectable wrong-document write into a crash on line one — and **zero matches is a failure
too**, not a reason to fall back to the first page.

```python
MARK = 'MY_MARK_' + secrets.token_hex(3)   # your own suffix, reported in your notes

def marks(ctx):                            # read-only census; run it BEFORE you stamp
    out = []
    for pg in ctx.pages:
        try:
            out.append((pg, pg.evaluate("window.name")))
        except Exception:
            pass
    return out

assert not [p for p, n in marks(ctx) if n == MARK], "somebody already has my mark"
page.evaluate(f"window.name = {MARK!r}")
...
def mypage(ctx):
    hits = [p for p, n in marks(ctx) if n == MARK]
    if len(hits) != 1:
        raise SystemExit(f"expected exactly one page marked {MARK}, found {len(hits)}")
    return hits[0]
```

`window.name` survives a `page.reload()` only if you set it again afterwards — reloading clears
it. Set it again right after any reload.

**Telling a signed-out browser from every other fault.** `GET /api/users/sessioninfo` returning
**200 with a body carrying `roles`** is signed in; **204 with an empty body** is signed out, and
no agent can fix that. Anything else is a *different* fault and must not be reported as a
sign-out: **429** is rate limiting, back off; **5xx** is Onshape down, wait; a thrown error is the
CDP connection. Run 3 observed the 204 five times in one outage and the flip to 200 when a human
signed in — that is one day's observation, not a documented contract, so log the status you
actually got.

## 2. Finding out why something failed

Read this before you build anything. Onshape's failures are quiet by design: a feature that could
not be made sits in the tree in `ERROR` and the rest of the model regenerates around it.

**The message lives in a tooltip and nowhere else.** A failed feature's row carries
`ns-list-item-error` and a red icon. Hover the icon — at the row's left edge, x ≈ 54, not at the
name — and the text appears. Two wordings have been seen: `<name> has error: <message>`
(*"Mate cannot resolve mate connectors."*) and `<name> did not regenerate properly: <message>`
(*"Could not create all instances as entered."*). **A scrape that matches on
`error|fail|cannot|could not|unable` finds neither reliably; match on `regenerat|error` too.**
`GET .../features` gives you `featureStates`, which is a status and no message at all, so **a
failing feature cannot be diagnosed from REST**. Get the status from the API, then go to the
browser for the reason.

```python
pg.evaluate("""() => Array.from(document.querySelectorAll('.os-list-item'))
  .filter(e => e.className.includes('ns-list-item-error'))
  .map(e => e.innerText.trim())""")
```

**A 200 from the API means "accepted", not "worked".** Run 5 posted eleven mates that all returned
200 and all landed in `ERROR`, because Onshape rewrote a query type it did not like rather than
refusing it. What catches this is a volume or a bounding box, never a status.

**`featureStatus: OK` and a green tree are not evidence either.** A slit that cut half its length
into empty air, and an assembly translated 37 mm off the origin, both left every feature `OK`.
Measure the geometry.

### Failure modes, with the symptom you will actually see

| Symptom on screen | Cause | Fix |
| ----------------- | ----- | --- |
| Click does nothing at all | a tool is still armed, usually Dimension | Escape once, then click |
| Typed dimension ignored, sketch still black | you pressed Escape instead of Enter | retype, commit with Enter |
| Region field empties when you pick the axis | focus never left the region field | click into the axis field first |
| *"Could not create all instances as entered"*, feature red, and every dimension still measures right | Mirror or Pattern transformed result faces instead of replaying the feature; only the original instance was cut | tick **Reapply features**; catch it with **volume**, since N instances of a cut must remove N × the single cut |
| *"Select a mirror plane"* after picking one | the tree scrolled; you hit the panel header | use the feature-tree filter box |
| *"Select Extrude direction."* on a feature you only meant to flip | the `Direction` checkbox is a custom-direction reference field, not a flip | untick it, use the arrow beside `Blind` |
| Two parts become one, or most of a body vanishes | merge scope left on *Merge with all* | set the scope by hand |
| A rod runs straight through another part, preview looks right | starting offset has **its own flip control**, separate from the main direction | check the bounding box |
| A cut is half as deep as asked, and every measurement still passes | Remove extrude arrived with `oppositeDirection` set, so one half of a two-sided depth went into empty air | measure the **z-extent of the cut face**, not the result of the cut |
| Whole sketch turns red, *"could not be solved"* | Coincident added over an existing implicit constraint | undo; redraw the line instead |
| Rename produces `Ball studPart 1` | Ctrl+A does not clear the rename box | End, then Backspace |
| Blank screen, no error | Hide applied to a multi-part selection | undo, deselect, hide one thing |
| Sketch region cannot be picked inside a solid | the dialog picks the solid instead | hide the parts, show the sketch |
| A click on the canvas selects nothing at all | picking follows the hover target | `mouse.move`, wait 400 ms, then click |
| A dimension does nothing — no box, no error | label placed too near the canvas bottom edge | move the label click inward |
| A circle comes out enormous (Ø226) | `Control+A` did not clear the numeric field | use `locator.fill()`, read it back |
| Extrude flip does not take | direction set before the entities were picked | set the flip last, verify by volume |
| Circle drawn in a new sketch is an ellipse | a new sketch does not auto-orient | press `n` after creating it, check the cube |
| Mate returns 200 and sits in `ERROR`, dialog named both connectors | wrong query `btType`; Onshape rewrote it on the way in | hover the row for the message, then repost with the type a GUI-built mate reads back as |
| The whole assembly moves and every mate stays green | a drag landed on empty space, and nothing is fixed by default | `Meta+Z`, then right-click the base part → **Fix** |

## 3. Create a document and set units

1. `page.goto("https://cad.onshape.com/documents")`, wait ~4.5 s.
2. **`button:has-text('Create')` matches a hidden "Create account" button first.** Use
   `button:has-text('Create'):visible`.
3. The **Create menu items are not in the DOM** in any form the ordinary selectors find — not
   `[role=menuitem]`, not `li`, not `a`. Click **Document…** by coordinate: take the Create
   button's `bounding_box()` and click at `(x + 30, y + height + 18)`.
4. In the **New document** dialog, scope everything to the dialog or you will hit the page's own
   Create button behind the modal:
   `page.locator("div[role='dialog']:visible").first` then
   `dlg.get_by_role("button", name="Create", exact=True)`.
5. Units: **☰** (left of the document name) → **Workspace units…** → *Length default unit* =
   **Millimeter**. Set **Display decimals** to **0.12345** — at the default `0.123` you cannot
   tell 4.996 from 4.9961, and several run 1 checks needed five places. Green ✓.

**The red ✗ discards the change silently and leaves you in inches.**

**Workspace units is the one dialog built from real `<select>` elements**, so `select_option(label=
"Millimeter")` works there and coordinate-clicking the list does not — the `<option>` never becomes
visible to Playwright. Feature dialogs are the opposite; theirs are custom widgets that only answer
to clicks. Read the value back (`4: millimeter`, `5: 5`) rather than trusting the click.

**The New document dialog remembers the folder you last created in**, so its location list opens
inside that folder and the folder's own row is not there to click. Look for the row before clicking
it, and treat its absence as *already there* rather than as a miss.

## 3b. Variable Studios — one set of variables for the whole document

**Onshape variables are scoped to a Part Studio.** Ten `Variable` features at the top of the ball
and socket's tree are invisible to every other tab. A **Variable Studio** is the document-level
element that fixes that, and it is on the same **+** menu as *Create Part Studio* and
*Create Assembly*, as **Create Variable Studio**.

**The + that opens that menu is not at a fixed place.** It sits at the left end of the tab
bar, and the tab bar begins where the open left panel ends. With *Versions and history*
open the + moves from x = 57 to x = 600, and a click at the remembered spot lands on bare
tab bar and opens nothing. Ask the page for the box of `.btn-add-element` rather than
remembering where it was, and shut the panel before framing the tab strip, because the
panel pushes the newest tab off the right of the usual clip.

The tab is a table with **Name**, **Variable type**, **Value** and **Description**, a
**Variable Studio name** box above it, an **Insert Variable Studio** button, and along the bottom
edge a control reading **Insert into all Part Studios and Assemblies**.

**All of the following was measured on 2026-08-20 in a scratch document, not read off the help.**

- **`#name` works exactly as it does for a local variable.** In a Part Studio that can see the
  studio, `#torsoH * 2` is accepted; a name that resolves nowhere — `#nosuchvar * 2` — is refused
  by the server outright, so an unresolvable name fails loudly rather than evaluating to zero.
- **A tab created *after* the box is ticked inherits the variables.** This is the one that decides
  where a Variable Studio goes in a build order: it can be made once, first, and every Part Studio
  made later can use it without doing anything.
- **A tab that existed *before* the studio did inherits them too.** Measured 2026-08-20 while
  building the robot's tutorial 1: the Part Studio a new document arrives with resolved `#torsoW`
  in a dimension field, and the Variable Studio was created after it. So the order is a
  convenience, not a requirement, and a student who starts sketching before making the studio is
  not stuck.
- **`Insert into all Part Studios and Assemblies` is a checkbox, not a one-shot action.** Its
  markup is `button.insert-into-all-button`, and it is on when the button holds an `svg.checked`;
  there is no `input[type=checkbox]` to read, so a script that looks for one always sees "off".
- **The first Variable Studio in a document arrives with the box on; a second arrives off.**
  Measured by deleting every Variable Studio in the document and making one from clean: it held an
  `svg.checked` before anything was clicked. Making a second one in the same document gave an
  unchecked button. Read the state rather than ticking it blind — a tick on an already-ticked box
  turns it off, and which state you find depends on what is already there.
- **A Value cell takes two double clicks from cold.** The cell is a `div.os-td` that sits over the
  input and intercepts the pointer. The first double click focuses the div; the second opens the
  `INPUT`. Loop until `document.activeElement.tagName` reads `INPUT` — three tries is enough — and
  only then type. A single double click leaves focus on the div and everything typed afterwards
  goes somewhere else: four values entered that way read back as `0 mm` with the last one landing
  in the next row's Name cell.
- **An empty placeholder Name cell is the exception: it takes a single click.** The row does not
  exist yet, so there is no cell over an input to fight.
- **Tab commits the row but does not reach the Value cell.** The name is accepted, the value
  defaults to `0 mm`, and a fresh empty row appears below. Click the Value cell yourself.
- **Right-click a variable row → Delete** removes it.
- **Inserting a Variable Studio adds no feature to the feature list**, and
  `GET /api/variables/d/{did}/w/{wid}/e/{eid}/variables` reports only *local* variable tables, so
  it comes back empty for a tab that can nonetheless resolve the names. Neither is evidence that
  the insert failed. **To test whether a name resolves, post a feature that uses it** and see
  whether the server accepts it.
- **A new document is in inches.** Typing `48 mm` into a Value cell is accepted and stored, and
  the cell then reads `1.89 in`. Set the workspace units first — see §3 — or every value in the
  table is displayed in the wrong unit while being right underneath.

- **`POST /api/variables/d/{did}/w/{wid}/e/{eid}/variables` takes the array, not the table.**
  The GET returns `[{variableStudioReference, variables}]`; posting that object back is a 400
  (`Cannot deserialize ... ArrayList<BTVariableParams> from Object value`). Post the inner
  `variables` list. The failure is loud, but a script that ignores the status reads the variables
  back unchanged and looks like a model that does not follow its dimensions.

Onshape's own guidance is to leave the box **off** and insert the studio by hand where it is
wanted, because a variable change otherwise regenerates every tab in the document and makes a
merge hard to read. That advice is written for large documents; this robot has ten tabs.

## 4. Selecting things

**Onshape's DOM defeats ordinary selectors.** Assume you will be clicking coordinates, and build
the habit of finding them from something measurable rather than guessing.

- `page.locator("input:visible")` and `bounding_box()` are reliable and are usually the anchor
  you want — find a known input, then offset from it.
- `page.locator("text=Some Label")` works for feature-tree entries and part names, but it is a
  **substring** match and takes the first node. A studio named the way this project names things
  — `Stub circle` sitting directly above `Stub` — hands you the sketch when you asked for the
  extrude. Use `text="Stub"` for an exact match.
- **The feature tree scrolls, and a row outside the panel is unclickable** — silently, with no
  error. Rows can end up above the filter bar or below the panel once the tree gets long. Scroll
  the tree, then assert the row's y is inside the panel before clicking.
- Toolbar buttons, menu items, and most dialog controls do **not** resolve. Screenshot, read the
  position off the image, click with `page.mouse.click(x, y)`.
- **A bare `mouse.click` on the canvas selects nothing.** Onshape's picking follows the *hover*
  target, so you must `mouse.move(x, y)`, wait ~400 ms, then click. This cost run 2's hinge agent
  its first hour.
- **Take a screenshot after every coordinate click** and confirm the state changed. A coordinate
  click that misses does nothing and reports nothing.
- **Everything a part puts on its own axis lines up when the camera is on that axis, and the
  nearest one takes the pick.** The head's socket is the case: on the bottom view the pick pixel
  meets the cavity sphere at (0, 0, -51.08) mm, 0.00 mm from all four traces of the cross slit and
  directly behind a mate connector that came in with the derived socket. Eleven rebuilds across
  nine pixels and three zoom levels could not get off it. Turn the camera off the axis first —
  `shift+7`, then arrow keys 15° at a time — and the same pick lands 2.76 mm clear of the nearest
  edge, on the face and nothing else. Check the angle rather than trusting it: project the point
  you want, read where the ray meets the shape, and refuse the pick when it comes out too close to
  something else.
- **Shift locks the reference to the face already hovered, so the order is the technique.** Hover
  the face until its inferred points come up, *then* press and hold Shift, then travel to the
  point you want, then click. Onshape keeps that face's points alive the whole way, even once the
  cursor has left the face. Pressing Shift first locks nothing: a spike did that four times and
  concluded Shift was inert, which was wrong. The frames say it plainly — without Shift every
  inference square is gone by the time the cursor reaches the target, and with it they are all
  still drawn. Reach for it whenever the reference jumps between a cylindrical face and the
  circular edge across it, which is most of the awkward mate connectors.
- **A lock on a face still cannot win a pixel another body owns.** A mate connector already on the
  model is a body, and a click on its marker selects the marker whatever is locked. If the point
  you want is drawn at the same pixel as somebody else's marker, move the camera; no modifier
  will separate them.
- **Clicking something already selected deselects it**, and a selection survives zooming and
  reframing. So a click that lands perfectly can leave the screen with nothing highlighted, which
  is exactly what a miss looks like. Click empty space to clear before any click you intend to
  check.
- **A click on empty canvas does not clear a selection made in the feature tree.** The rule above
  holds for geometry; a plane picked by its row stays picked through a canvas click, so a helper
  that cleared and then clicked the row turned the row off on every pass and reported that nothing
  was selected. Read the selection first and click the row only while it is not the one thing
  selected:

  ```python
  SELECTED = """() => Array.from(document.querySelectorAll('.os-list-item-name'))
      .filter(e => e.closest('.os-list-item').className.includes('selected'))
      .map(e => (e.innerText || '').trim())"""
  ```

- **Dragging an instance in an assembly needs a slow pointer and a clear place to start.** A
  mouse down, one move and a mouse up left the head exactly where it was, twice. It moved when
  the drag started on plain surface off to one side of the face, away from the origin marker, and
  walked up the screen in four moves with half a second on each. Read the result back:
  `GET /api/assemblies/d/…/w/…/e/…` returns `rootAssembly.occurrences`, and each occurrence's
  transform is a 16-number matrix whose 4th, 8th and 12th entries are where that instance sits, in
  meters.
- **Mirror copies; Symmetric constrains.** Two entities held either side of a line come from the
  *Symmetric* constraint, which is what a feature's constraint list calls `MIRROR`. The tool named
  *Mirror* draws a second copy of everything it is given, so handing it a shape's two sides leaves
  six entities where the reference has four. Armed, Mirror says *Select a mirror line* and takes
  the first click as that line; Symmetric reads a plain selection of the two entities and the line,
  and a shift click holds a sketch entity and one of the origin's axes together.
- **A circle's center loses the pick to the circle when the two are close in pixels.** Dimension
  handed a small circle measures to its near edge, which is a radius short, and says nothing. The
  center wins once the rim is a few tens of pixels away, so draw a circle several times the size it
  ends up, dimension from its center, and set the size last. The status strip at the bottom right
  of the window reads `Point: X … Y … Z …` when a point is what got picked.
- **A dimension's own leader is pickable too, and it runs through the geometry it measures.** A
  distance from an axis to a circle's center draws a line from that center straight out to its
  label, so a pick aimed at the circle's edge along that direction takes the dimension and
  Dimension then opens nothing. Aim at a diagonal instead.
- **A pick on the origin's axis has three answers once geometry is held there.** A circle's center
  constrained above the origin sits on the vertical axis, and a click there can take the center
  point, the circle, or the axis. Dimension took the axis and refused with *A dimension cannot be
  created between these items*, because two axes at right angles have no distance between them. Set
  a distance while the geometry is still off to one side, and constrain it onto the axis after.
- **A dimension moves whatever is still free.** Setting the size of a circle that is held only
  sideways slides it along the direction it is free in, so a pick worked out from where it was
  drawn lands on nothing. Place a thing before sizing it, and the pick after is at a place that can
  be worked out.
- **A constraint's own marker is pickable, and it sits next to the thing it marks.** The origin's
  vertical axis was aimed at a few millimeters below the tail of a shape, and the click took the
  tail, whose horizontal marker is drawn just below it. Mirror accepted the tail as its line
  without complaint. Aim at a stretch of the axis with nothing else near it, and confirm the shape
  came out where it should rather than that a pick selected something.
- **`n` gives the far side of the plane first.** Normal to has two answers and Onshape picks the
  one nearer the camera it already had, so the same key from two different views faces two
  different ways. Everything still picks, because the projection knows where the camera is, but
  the part is a mirror of itself on screen and the sketch's name in the corner reads backwards.
  Press `n` again to turn round, and decide which way you are facing by projecting 1 mm and -1 mm
  along the plane's own x: if the first lands left of the second you are behind the plane.
- **The bottom of the window is not canvas.** The status strip is at y = 966 and the tab strip at
  y = 983, so a pixel worked out from the camera can land on another tab and take the page with
  it. Check a computed pixel is inside the graphics area before clicking it.
- **The middle of a face is where the origin is drawn.** A click on the projected origin, meaning
  to take the head's bottom face, took the origin point instead. Chamfer accepted the point and
  changed nothing: twelve faces before, twelve after, no error anywhere and a feature in the tree.
  Pick a face off to one side, on plain surface, and read back what the dialog is holding. The
  field says `Face of head body` when the pick landed and stays empty when it did not.

**Read the camera; do not calibrate against it.** Onshape draws the Part Studio with WebGL on the
page's main thread, so a wrapper around `drawElements` and `drawArrays` on
`WebGLRenderingContext.prototype` can read the current program's `uMVMatrix` and `uPMatrix`
uniforms and hand you the camera itself, in meters. Enumerate `ACTIVE_UNIFORMS`, keep the
`FLOAT_MAT4` ones, and read their values with `gl.getUniform(program, loc)` — a map keyed on
`getUniformLocation` identity does not match what `uniformMatrix4fv` is called with.

- **Every frame draws several cameras.** Record `gl.getParameter(gl.VIEWPORT)` alongside each pair
  of matrices and keep the full-viewport draws: the view cube renders into 11×11. Screen-space
  overlays are full-viewport too, at about 0.001 px per mm, so take the survivor with the largest
  `uPMatrix[0]`.
- **The scale is one multiplication.** `px_per_meter = uPMatrix[0] * viewport_w / 2`, and
  `uPMatrix[5] * viewport_h / 2` agrees with it.
- **A model point becomes a pixel** through `uPMatrix * uMVMatrix`, column-major and orthographic:
  eye, then clip, then divide, then map NDC into the viewport and add the canvas origin with y
  flipped. A sketch (x, y) on the Front plane is the world point (x, 0, y).
- **Zoom to fit centers what is drawn, not the origin.** A shape running from -20 mm to 12 mm
  leaves the origin 4 mm above the middle of the window, and the same offset in millimeters lands
  on a different pixel every time the drawing grows. Work a pick out from where a known piece of
  the shape actually landed rather than from a distance that was clear on the last pass.
- **Matrices only refresh while the page draws.** Nudge the mouse a few pixels and wait before
  reading, or you get the frame before the one you are looking at.

**Assert the projection landed on ink** the first time you use it in a session: screenshot, and
check that the pixel you computed for a known point is inside a run of sketch blue on that row.
At zoom to fit on a Ø20 circle the origin projected to (923.0, 523.0) at 42.5714 px per mm, and
clicking the projected top of the circle selected that circle. Without the hook, the fallback is
to draw a circle roughly and dimension it: the value Onshape pre-fills into the dimension box is
an exact mm-per-pixel reading, and the circle's center gives you the origin's screen position.
The hook, the projection and the two camera laws in section 9 were measured in
[`experiments/runs/2026-08-18-spike-camera/findings.md`](experiments/runs/2026-08-18-spike-camera/findings.md).

## 5. Reaching a named tool

The toolbar's last slot is a **most-recently-used** button, so its meaning changes under you.
Two reliable routes:

- **Search tools** box at the top right (`alt/⌥ c`). Click it, type the tool name, and press
  **Enter** to take the first hit. Clicking the highlighted row in the flyout that appears
  beside it is *not* the same thing and in one run it closed the panel without opening the tool.
- The feature-tree **filter box** (`Filter by name or type`, top left) is the reliable way to
  reach a named plane or feature when the tree has scrolled. Type `Front`, click it, clear the
  filter afterwards.
- **Hover a button and read its tooltip; do not trust a remembered x.** Every toolbar coordinate
  written down in this file is a measurement of one window in one panel state, and the two ways it
  goes wrong both look like the tool is missing. Some of the numbers are left edges rather than
  centers: draft9p2 hovered *Fillet* at the recorded 396 and got no tooltip, because the button's
  box is 395 to 427 and its center is 411, and the recorded *Chamfer* 452 and *Mirror* 724 were
  likewise 11 and 17 px off their centers of 463 and 741. The other way is the panel: at 1600 px
  wide with nothing open down the side the Part Studio toolbar shows 29 buttons flat, and opening
  the versions panel both pushes them right and narrows the strip until it folds them into 16
  dropdown groups, so the tool you want is no longer a button at all. Dump
  `.tool.is-activatable` boxes with `y < 90`, hover each center, and take whichever one answers to
  the tooltip you asked for. It costs one pass over the toolbar and cannot go stale.

**Direction and axis fields take different things, and the two pattern kinds differ.**

- **Linear pattern's `Direction` accepts a plane, a face or an edge.** Its `directionOne` filter
  takes `LINE`, `CIRCLE`, `ARC`, `CYLINDER`, `CONE`, `REVOLVED` and `PLANE`. A default plane
  contributes its normal, a cylindrical face its axis, a straight edge its own direction. **Read
  the field back after clicking**: it names what it took — `Right plane`, `Face of Top edge
  fillet`, `Edge of Top edge fillet`. If it stays empty, the click missed the field, not the
  geometry. Run 3's foot put all three in, in turn, and read the field back each time.
- **Circular pattern's axis refuses a default plane, and refuses it silently** — the field stays
  empty, no error, no message, no color. Give it a **cylindrical face** or a **circular edge**;
  the edge is the way in when the face you wanted belongs to a part you have had to hide. Also
  switch the type from **Part pattern** to **Feature pattern** first.

**A feature pattern of a Remove or Add across a curved or filleted boundary needs `Reapply
features`.** Without it Onshape transforms the *result faces* of the original feature; where the
host surface differs at each station the transformed faces have nothing valid to land on, and the
feature errors with *"Could not create all instances as entered. Try selecting 'Reapply features'
option."* Ticking it replays the feature instead, which works. Run 3 hit this on the foot's sole
ribs and the hand's relief slits.

**`Equal spacing` is on by default, so a circular pattern's `angle` is the total sweep, not the
step between instances.** Run 3 entered 24 instances at 15° meaning 15° apart and got 24
instances crammed into 15°. It regenerated cleanly and looked plausible in the tree; only a
volume delta exposed it.

**The pattern split-button's `command-id` changes under you.** It is `linearPattern` until you
use a circular pattern, after which the same button is `circularPattern`. A script that hard-codes
either one breaks on the second use.

**Boolean → Subtract** also carries a **Reapply fillet** checkbox that the help page does not
mention.

**Flyouts close between script invocations.** Open the flyout and click the item inside the same
Playwright call, or it will not be there.

**The toolbar reflows when you leave sketch mode**, so x-coordinates probed inside a sketch open a
different tool outside one. Clicking where Extrude had been opened Sketch twice in a row, each
time leaving a stray `Sketch 1` to cancel. Use `gui.search_tool` rather than a remembered
coordinate whenever the mode has changed.

**`gui.search_tool` clears whatever was selected on the canvas.** Typing into the search box takes
focus away from the graphics area and the pre-selection goes with it, so a feature opened that way
arrives with an empty field and the tree shows an error. **Open the feature first, then pick** —
the reverse of the habit that works from the toolbar.

**The rectangle split-button's `command-id` changes under you**, exactly like the pattern
split-button above. It is `RECTANGLE_TWO_CORNERS` until you use the center point variant, after
which the same button is `RECTANGLE_CENTER` and a locator naming either one hangs for its full
timeout. Match any `command-id` containing `RECTANGLE`.

## 6. Dialogs

- **Name the feature before you fill the dialog in.** The dialog's title is editable — click it
  and type — for every feature type. It is the function-name discipline: naming it first forces the
  decision about what the feature is for, and a feature you cannot name yet is one you have not
  thought through. It also settles the frames. The tree row and the dialog header both sit inside a
  screenshot, so a name typed after the green ✓ is wrong in every picture of that step, and no
  reshoot can reach it. Renaming from the tree afterwards is the fallback, and it carries the
  `End`-then-`Backspace` trap in § *Failure modes*.
- **Fields do not hand focus on.** After picking into one list, clicking the next thing adds it
  to the *same* list. **Click into the next field first**, every time. This bit run 1 on Revolve
  (axis), Boolean (Targets) and Circular pattern (axis). In a **feature** pattern or mirror the
  list takes *the feature that made the geometry you clicked*: run 6 clicked a pocket's rim edge
  to fill the axis and got `Extrude 7` in `Features to pattern`, with the axis still empty.
- **A required field that is empty shows outlined red.** That is your check that a pick landed.
- **Not every refusal turns anything red.** A field can decline a pick by doing nothing at all —
  no error, no message, no color — and circular pattern's axis is the case that bit runs 2 and 3.
  **Check the field's contents, not the dialog's appearance.**
- **Checkboxes are not `input[type=checkbox]`**, so no `is_checked()` will tell you the truth —
  crop a screenshot of the row and look at it. Worse, **clicking to the left of the label focuses
  the control without ticking it**, and a focused checkbox looks enough like a ticked one to fool
  a screenshot taken from too far away. Click the label itself.
- **The green ✓ often needs two clicks** after typing in a numeric field: the first commits the
  field, the second accepts the feature.
- **Inside a dialog, Enter accepts the whole feature.** Use Tab between fields.
- **Do not trust any remembered default.** Run 1 saw Extrude open on **Add** with merge scope
  pre-filled; run 2 saw the same dialog open on **New** with *Merge with all* **unchecked** and the
  scope empty and red. Both happened with a solid already in the studio. **Look at which of New /
  Add / Remove / Intersect is underlined, every time**, and set the merge scope by hand every time.
  The failure mode differs — a silent weld, or a blocked feature — the discipline does not.
- **An empty merge scope is accepted, and does nothing at all.** Not a weld, not an error: the
  feature builds, the preview looks right, and the volume is unchanged. Run 3 lost an Intersect
  and a Remove that way in one build. Assert the field's text contains the part name before
  accepting.
- **Onshape will accept a feature with a required selection field left empty and park it in
  ERROR**, rather than blocking OK. Check `featureStates` through `GET .../features` after
  anything that took an unusual number of clicks.
- **Wheel-scrolling the feature tree drops focus from the dialog's open selection field.** The
  field stays outlined red, the tree row you then click merely highlights, and nothing lands.
  Run 6 committed a Mirror with no mirror plane this way; the model was unchanged and the red
  feature name was the only sign. Scroll first, then click into the field, then pick.
- **"…did not regenerate properly: Overlapping fillets." on a small boss means you picked the
  side wall, not the crown.** A Ø0.8 boss 0.6 tall takes a degenerate r0.4 crown fillet without
  complaint, but its barrel's two rims are 0.6 apart and any radius over 0.3 overruns them. The
  giveaway is that a *smaller* radius fails too. At 46 px/mm the crown ellipse and the barrel are
  one blob; zoom to about 110 px/mm before picking.
- **Set an extrude's direction flip LAST.** Setting `oppositeDirection` on an empty dialog and then
  filling in the entities loses the flip, silently. And prove it afterwards with a volume: a cut
  that removes nothing and a boss that merges into solid both look entirely normal in preview.
- **The extrude dialog carries the flip over from the previous extrude**, so it is not reliably
  off when the dialog opens and "click it once" is not a rule you can apply blind. Reading the
  feature's stored `oppositeDirection` back through `GET .../features` is the only way found so
  far to tell *the button did nothing* from *the direction was already right*.
- **The extrude's `Direction` checkbox is not the flip.** It opens an empty custom-direction
  reference field, and ticking it with nothing selected fails the feature with *Select Extrude
  direction.* The flip is the small arrow to the right of the `Blind` dropdown, tooltip *Opposite
  direction*. Hover a control before believing its label.
- **A starting offset has its own flip arrow, on its own row.** It is on the Depth row, not the
  Blind row, and flipping the extrude does not flip it. Run 3 found this building a stub whose top
  face had to land at z = −4.15.
- **Both arrows are `use` elements of `#svg-icon-flip-direction-opposite`.** Neither carries an
  aria-label, so a search by label finds nothing, and the `button.parameter-state-toggle` that sits
  on the depth row is not a flip at all: it is the precision toggle, and clicking it changes how
  the number is rounded. Ask the dialog for its `use` elements and keep the ones whose `href` holds
  `flip-direction`; sorted down the dialog, the first is the extrude's and the second is the
  starting offset's.
- **The starting offset does not follow the extrude's flip, and the two answer different
  questions.** The offset's arrow says which side of the sketch plane the cut *starts* on and the
  extrude's says which way it then *runs*. Building draft9p2's mouth all four ways on a head
  60 mm deep, with a 30 mm offset and a 3 mm depth, gave: neither lit, starts at −30 and runs to
  −33, outside; offset lit, starts at +30 and runs to +27, a groove in the back; extrude lit,
  starts at −30 and runs to −27, the groove in the face; both lit, starts at +30 and runs to +33,
  outside. **Onshape accepted the two that removed nothing** with no banner and no warning, so a
  Remove extrude proves nothing by being accepted.
- **Find out which arrows are lit by building one and reading it back, not by looking.** The
  arrows carry no state in the DOM and their drawn pixels change on hover, so a screen comparison
  says a click landed when it did not. Six openings of the same dialog in draft9p2 all started at
  *extrude flipped, offset not flipped* — every one of the four builds above lands exactly where
  that starting point plus the clicks made predicts — but that is one document and one session,
  and the way to know is to accept a throwaway with no clicks at all and read its parameters.
- **On a two-sided extrude the flip turns both ends the same way**, which is never what you want.
  *Second end position* draws opposite the first, so the two arrows oppose; clicking *Opposite
  direction* points them both the same way and the feature fails with *Failed to extrude
  selections, check input.* **To move an asymmetric two-sided cut, swap the two depths** and leave
  the flip alone. Run 6 cut a 5.5 mm slit 1.35 down and 4.15 up when it needed 4.15 down and 1.35
  up, and the flip made it worse before the swap fixed it.
- **Escape while a feature dialog is open discards the feature.** Not the selection, not the field
  — the whole feature, gone from the tree with no prompt. Run 6 sent one Escape believing an
  extrude had already committed and the Features count went 8 to 7. **Prove the dialog closed
  before you touch the keyboard**: check that a label unique to it, such as *Second end position*,
  is no longer on the page.
- **The right-click menu is cut short while a feature dialog is open** — a part offers only *Hide
  other parts* and *Zoom to selection*, with no Rename. Commit first, then rename.
- **`Control+A` does not clear a numeric field.** Typing `2` into a box reading `226.50977 mm` gave
  a Ø226.5 circle that merged a 226 mm disc into the part. Use Playwright's `locator.fill()`, and
  **read the value back before pressing Enter**.
- **`End` + Backspace is not reliable in the rename box either** — send Deletes as well.
- **Rename vanishes from the context menu whenever more than one thing is selected**, and Onshape
  leaves things selected constantly.
- **Double-clicking a feature row does not open its name for editing — it opens the feature.** The
  keystrokes that follow go to the graphics area as shortcuts. Run 6's spike typed a new name at a
  `Mate connector` row and got hidden planes, a zoom-window prompt, and *"Mate connector 1 did not
  regenerate properly: Cannot resolve entities."* on a connector that had committed clean a moment
  before. One **Undo** put it back. Before typing anywhere, read `document.activeElement` back and
  confirm it is the field you meant.

- **The dialog's name box is opened by a pencil, not by the title.** Clicking or double-clicking
  the title text gives a tooltip and nothing else. Hover the title, and a
  `div.os-dialog-button-edit-name` appears to its right; clicking that summons
  `input.os-dialog-header-rename-textbox`. `gui.name_feature` does exactly this.
- **The name box keeps the keyboard until Enter is pressed.** Typing the name is not the end of
  naming. A `n` pressed next to look normal to the sketch plane made a sketch called
  `pedestal outlinen`, and an `Alt+c` to reach Search tools was swallowed so that `Circle` went
  into the name and no tool ever armed. Enter commits the name and hands the keyboard back to the
  body; the input itself stays in the page afterwards, so `document.activeElement` is what says
  whether the box has let go, and counting the input always answers yes. `gui.name_feature` now
  presses Enter and reads the focus back, and `gui.search_tool` refuses to type while the name box
  holds the keyboard.
- **What a REST route reads is the last accepted state, not the dialog's preview.**
  `boundingboxes` gave the same box with an extrude previewed one way, the same box with it
  previewed the other, and the true box only after the tick. The dialog does write to the model as
  it is filled in, so the screen changes; a script that wants to know which way an extrude is
  running has to accept it and read afterwards.
- **A starting offset is measured to the far end of the cut.** A Remove of depth `#face`, 3 mm,
  with the starting offset set to 27, took the plastic between 24 and 27 mm from the sketch
  plane, not between 27 and 30. The head was left with a sealed cavity behind an unbroken face
  and one plane more than the part is supposed to have. Set the offset to where the cut is to
  come out, 30 here, and count the faces afterwards.
- **An extrude off the Front plane runs toward the front.** Measured on the head's eye: an Add
  extrude of a region on the Front plane, depth `#headD / 2 + #face`, with no direction click, put
  the new material between y = -33 and y = -30, which is the face a Front view looks at. The arrow
  beside `Blind` is what turns it around.
- **A dialog's mode can be a dropdown wearing the current mode's name.** Mirror opens reading
  `Part mirror`, and `Feature mirror` is not a button beside it. Clicking the words `Part mirror`
  opens the menu the other two modes are on.
- **The name box keeps the keyboard until Enter is pressed**, and everything typed after it lands
  in the title. Naming a sketch first and then pressing **n** for a normal view produced a sketch
  called `torso outlinen` on a view that never turned, and the tool name typed into Search tools
  went the same way, leaving `torso outlinenCenter point rectangle` and no rectangle. Press Enter
  and read the title back before touching anything else. A dialog whose fields are filled by
  clicking never showed this, because the click moves the focus.
- **Mirror opens on *Part mirror*, which mirrors the whole solid.** The type dropdown sits at the
  top of the dialog and holds *Part mirror*, *Feature mirror*, *Face mirror* in that order.
  Feature mirror is the one that copies a feature to the other side of a plane, and it wants the
  feature picked in the tree.
- **Where the Extrude dialog's flip arrows sit depends on which operation is chosen.** The arrows
  carry no state a script can read, so which of them is already lit has to be read by building a
  throwaway and looking at where the material went. Build that throwaway on the same operation the
  real feature uses. A `New` throwaway was read, and its two arrow positions were then clicked in a
  `Remove` dialog, where one of them is not an arrow: the slot came out 2 mm above the sole it was
  meant to cut into, and the pattern repeated that eight times.
- **Extrude arrives on `Add` once the studio holds a solid,** not on `New`. Read the row of words
  along the top before you accept: `New`, `Add`, `Remove`, `Intersect`. The frames of `Add` being
  hovered and `Add` being active look nearly identical — the active one is underlined.
- **A feature pattern and a feature mirror each carry a *Reapply features* tick, and it starts
  off.** It is the last checkbox but one, under *Second direction* and above *Skip instances*, and
  it is what the feature record calls `fullFeaturePattern`. Ticked, the copy is made by running the
  feature again at the new place; unticked, the faces the feature left are copied instead. The two
  put the same shape on the screen, so nothing but the feature's own record says which was used:
  the head's `second eye` came out unticked against a reference that is ticked, and every eye was
  still exactly where it belonged.
- **The default planes stay pickable in the tree after they are hidden,** which is how a hidden
  Right plane gets chosen as a mirror plane. Selecting one tints the whole graphics background
  orange; that is the selection, not an error, and it clears when the feature commits.

## 7. Sketching

- Select the plane in the Features list, then click **Sketch**. **A new sketch does not
  auto-orient** — `browser-access.md` says it does; it does not. Sketch 1 opened isometric and a
  circle drawn in it came out an ellipse. Press **n** after *creating* a sketch, not only after
  reopening one.
- **Escape does not close a sketch dialog, and it does not throw the sketch away.** A take that
  died between opening a sketch and drawing in it pressed Escape on its way out and left `Sketch 1`
  in the feature list. Clicking that row re-opens the same dialog instead of offering a context
  menu, so neither Rename nor Delete is reachable from it, and the toolbar Undo does not remove it.
  The dialog's red **×** is what discards it: on an empty sketch it takes the row with it. Any
  script that opens a sketch closes it with `gui.RED_X`, not with Escape.
- **`n` is not deterministic.** On the same Front plane in one session it gave a true Front view
  twice and the **Back** view once, with no rotation in between — and once it did not move the
  camera at all. **Check the view cube after every `n`.** A mirrored pass is harmless on symmetric
  geometry and silently wrong on anything else.
- **Pressing `n` again turns the view through the plane**, which is the way back from the mirrored
  side. The cheap test is arithmetic rather than the view cube: project the origin and a point ten
  millimeters along the model's own x, and read the sign. On the front of the Front plane the
  second point draws to the right of the first and level with it; from behind it draws to the
  left.
- **`n` moves the origin on screen.** Orienting normal to a plane re-frames the camera, so pixel
  coordinates worked out before the keystroke point at the wrong place after it. Run 6 drew a
  collar circle 85 px below the origin that way. Re-find the origin after every `n`.
- **`shift+s` means two different things depending on where you are.** Outside a sketch it opens
  one; inside a sketch it is the **Point** tool. Do not use it to open a sketch from within a
  sketch you have just closed by hand, because the mode may not have changed yet.
- **The sketch shortcuts worth knowing**: **g** corner rectangle, **r** center point rectangle,
  **shift+e** extrude, **n** view normal to, **shift+7** isometric, **f** zoom to fit.
- **A sketch pattern's instance count needs a double-click** to open its inline box; a single
  click only selects the manipulator. **Click somewhere empty in the graphics area to settle the
  pattern** — it has no green ✓ of its own. **Escape discards it**, and nothing says so: the sketch
  still closes clean and still reads fully defined. The tell is the next extrude previewing one
  instance where you asked for four.
- **Keyboard shortcuts go to whatever you last clicked.** After clicking a checkbox in the sketch
  dialog, pressing `g` did nothing at all — focus was still on the checkbox. When a dialog control
  was the last thing you touched, use the toolbar button, not the shortcut.
- Useful keys, all verified: `l` line, `g` corner rectangle, `r` center point rectangle,
  `c` circle, `d` dimension, `q` construction toggle, `i` coincident, `e` equal,
  `shift+q` symmetric, `shift+o` concentric, `shift+e` extrude, `shift+w` revolve.
- **`d` toggles the Dimension tool, and the tool survives between actions.** Pressing it when the
  tool is already lit puts it down, and the next pick then reports *"A dimension cannot be created
  between these items."* or opens no box at all. Ask before pressing: read the toolbar button's
  grandparent `div` and test its class for `is-active`.
- **The solver relocates an under-defined entity the moment you dimension it.** A circle drawn
  265 px above the origin jumped to 548 px when its diameter went in, and the follow-up click on
  its center hit empty canvas. Re-shoot and re-find the entity after every dimension.
- **Typing a value while drawing does nothing.** The live readout looks editable; it is not.
  Digits are discarded and Enter commits whatever the cursor was at. Double-clicking that
  readout makes it worse — one run got a `Ø0` label with no clean way back and restarted the
  sketch.
- **Dimension, then press Enter.** Pressing Escape to put the tool down *discards the number you
  just typed* and keeps the dragged size. The sketch still goes black. This produced a 34.8 mm
  torso where 48 was asked for.
- **Enter is not a guarantee either.** Run 2 saw a typed value silently discarded **twice in
  eleven** dimensions — edit box focused, value confirmed present by reading `input_value()` back,
  Enter pressed — and the dimension committed at the *dragged* size. **Read the label back off a
  screenshot after every dimension.** Double-click and retype fixes it every time.
- **A sketch has no axes to pick.** A symmetric relation wants a line and two things of the same
  type, and the sketch's vertical is not drawn anywhere, so there is nothing to take. A click
  where it would be lands on the solid behind the sketch and takes a point on one of its edges;
  Onshape then says *A symmetry constraint requires a line and two other geometries of the same
  type* and adds nothing. Hold a shape in the middle with a dimension from the origin, or draw a
  construction line and be symmetric about that.
- **A complaint about a relation arrives as a yellow bar, not as a feature error.**
  `gui_steps.errors` reads the feature list, finds nothing wrong and returns an empty set while
  the bar sits across the top of the window saying what was refused. The bar's words are plain
  text in the page, so read them back after asking for a relation.
- **A line drawn by clicking is vertical only if the pointer was inside the inference.** The
  head's profile came out with its left side leaning by a quarter of a millimeter, off a click a
  pixel wide of true, and nothing on screen said so. Ask for the relation rather than hoping for
  it, and read the closed sketch's geometry back before believing it.
- **Which dimension an ellipse gives you is decided by where the label is dropped.** Pick the
  ellipse and drop the label above it for the long way across; pick it again and drop the label
  out to the side for the short way up. Both are diameters, so a variable holding a radius is
  doubled in the box.
- **There is no readable `Under defined` anywhere in the page.** A scan of every childless `div`
  and `span` for the word came back empty while a sketch was plainly under-defined, so a script
  cannot ask the page whether a sketch is solved. Read the geometry back through
  `sketches?includeGeometry=true` once the sketch is closed. **A read taken while the sketch is
  still open answers with the last committed geometry**, so it cannot tell a constraint that took
  from one that did not, and it reads as failure either way. Four repairs to `ear wedge outline`
  were applied, checked against that read, and thrown away by the dialog's red **×** before the
  gate was moved to the screen.
- **A blue-pixel test for an under-defined entity starts right of the feature panel.** Onshape
  draws such an entity in a saturated blue, near RGB (65, 66, 254), and a scan for it is the only
  way to read a sketch's state while its editor is open. The sketch dialog's own checkboxes are
  that same blue, so a scan that begins at the window's left edge finds three of them in every
  frame and calls a solved sketch unsolved.
- **The label click has to clear the sketch axes, not only the model.** A width label placed
  straight above the rectangle landed on the vertical axis, which joined that line to the
  dimension: the readout became a 270° angle between the top edge and the axis, and no edit box
  opened. Nothing on screen says the pick went wrong except the angle itself. Offset the label
  sideways as well as away.
- **The label-placement click has a dead zone near the bottom of the canvas.** A label placed at
  y = 955 of a 1000 px window aborted the whole dimension — no box, no error, tool disarmed. The
  same dimension worked with the label at y = 790. If a dimension "does nothing", move the label
  click inward before suspecting the entity pick.
- **Draw arcs before the lines that meet them.** Dropping an arc onto a line's free endpoint
  constrains the arc to the *line*, not to the point, leaving the endpoint free to slide. The
  region still shades and every line goes black; a single blue dot is the only tell. Repairing
  it by adding Coincident over-constrains the sketch instead.
- **Black lines can still have blue endpoints.** Look at the dots, and drag anything blue.
- **A center point rectangle's corner click snaps to the sketch axis** if it lands within about
  10 px of one, and the rectangle comes out zero-width. Put the corner well clear and dimension it
  down afterwards.
- **Two parallel-line picks do not always give you the distance between them.** The Dimension tool
  sometimes reads the pair as one line and offers its *length*. It pre-filled 12 mm for a gap of
  4.4; typing 0.8 over that drove the wrong entity and the sketch went red. **Read the pre-filled
  value and check its magnitude before typing.** A single-edge length dimension is the
  unambiguous pick where the geometry allows it.
- **Escape clears a selection; clicking empty canvas does not.** A click meant for empty space
  lands on the part face behind it, and the status bar quietly starts reporting that face.

- **The Slot tool does not draw a slot.** Its tooltip reads *create a slot around continuous
  sketch entities*: it wraps something already drawn. Draw a **line**, arm Slot, click the line,
  move the mouse to set the width, and click. Clicking it on bare face does nothing at all, which
  reads exactly like a broken tool.
- **Arm the tool first, then pick the curve.** Arming Slot from the offset button's dropdown clears
  whatever was selected, so a line picked beforehand is not the line the tool gets, and the run ends
  with the line still there and no slot. Picking the line and then arming from the *tool search*
  does keep the selection, which is why the two orders read as one working and one broken.
- **The width click leaves a preview, and Enter is what keeps it.** Escape at that point takes the
  slot away and leaves the line and its dimensions, so the screen looks exactly as it did before the
  tool was armed. Committing with Enter came back Ø20 from a click 5 mm off the line, so the width
  the preview showed is not the width that lands: measure the slot, then edit its own diameter.
- **A tool in progress does not survive a script boundary.** Arm, pick, move and commit have to
  run inside one Playwright invocation; a second invocation that only sends the commit click does
  nothing. A *placed* dimension's edit box does survive, so reading and filling it in the next
  script is fine.
- **The Slot preview is far bigger than a tight crop.** A stadium spanning most of the model looks
  like nothing happened if the screenshot is clipped to where the slot was meant to be. Read the
  full frame before deciding an attempt failed.
- **Slot brings its own `DIAMETER` constraint** on `endCap`, with `labelRatio` 4 — the label sits
  four radii from the cap center, which is off-screen at any working zoom. Adding a second width
  or radius dimension over-constrains and gives *"Sketch could not be solved."* Zoom out, find the
  `Ø` label, and edit that one.
- **A failed dimension attempt leaves a driven `RADIUS` reference dimension behind.** Undo restores
  the previous *value* and leaves the dimension in place. Click the label once to select it and
  press Delete, then read the constraint list back over REST to prove it is gone.
- **Double-clicking a dimension label opens its edit box.** Verified on a `Ø20` label at
  (1020, 97). It does not work everywhere — one attempt at (1240, 616) highlighted the label tan
  and opened nothing — so read `document.activeElement.tagName` before typing.
- **The toolbar Undo button is at (57, 58) and works when `Ctrl+Z` does not.** `Ctrl+Z` sent to the
  graphics area did not undo a slot.
- **Constrain an ellipse Horizontal before dimensioning it.** It has a major axis, a minor axis and
  an angle; pinning the angle first makes the two diameter dimensions land where you expect.
- **A slot's center line does not split its region.** One Extrude click takes the whole stadium.
- **Sketch toolbar x-positions, y = 58**: line 193, rectangle 245, ellipse 297, arc 349,
  polygon 401, spline 453, point 511, text 538, use 574, construction 626, fillet 664, trim 717,
  slot 767 (its flyout caret 796, holding one item *Slot* at (761, 129)), mirror 819,
  linear pattern 854, dxf 906, dimension 962, constraint 1000 (caret 1028).
- **Constraint flyout geometry**: caret (1033, 58); items at x = 1009 — coincident 94,
  concentric 130, parallel 166, tangent 200, horizontal 236, vertical 272, perpendicular 307,
  equal 343, midpoint 379, normal 414, pierce 449, symmetric 485, fix 521, equal-curvature 556.

## 8. Measuring

The techniques below that work off a face dump are modules in `stickbot`, each taking
the JSON and printing its answer: `measure_walls.py` for concentric walls, `measure_planes.py` for
flat ones, `measure_gaps.py` for the closest approach between any two faces, `measure_solid.py` to
say which of those are plastic, `measure_line.py` to march a line through the part, and
`measure_tangency.py` for the crease angle at every edge. Read the docstring at the top of each for
what it can and cannot see.

- **There is no measure dialog.** Select one entity and read the **bottom-right of the graphics
  area**: an edge gives `Diameter`, a spherical face `Radius`, a planar face `Area`.
- **Verify what is in the selection list before trusting a number.** A "click empty space to
  clear" that lands on geometry leaves the panel summing two faces, and the result looks
  plausible. Run 1 lost ~15 minutes to a face area that was real arithmetic on the wrong set.
- Volume and mass properties: the **Display mass and section properties** icon, bottom right,
  then *Parts to measure*.
- **`POST .../featurescript` is the measuring tool this project kept missing.** `evDistance`
  between two bodies gives minimum clearance directly — that is how run 2 proved its two parts do
  not touch. A loop over `evPlane` for faces whose normal lies on an axis prints a whole stackup
  as a list of numbers. `evCurveDefinition` on every edge gives you every radius in the model in
  one call. Cookie auth plus the `X-XSRF-TOKEN` header is enough.
- **Measure the thinnest wall anywhere**, not the one you were thinking about. Run 2's hinge had a
  0.26 mm rim nobody had considered while everyone watched a 1.0 mm web that was fine.
- **Count the planes to tell an open pocket from a sealed void.** A blind cut that opens on a face
  contributes one plane, its floor; the same cut buried inside the solid contributes two, floor
  and roof, and removes exactly the same volume. Run 6's valley cut ran inward instead of outward
  and the 20-vs-19 plane count is what showed it, before any picture did.
- **When `featurescript` is 429, `bodydetails` still measures every shelled wall exactly.** Shell
  offsets each face inward, so a shelled surface and its offset **share an origin and an axis and
  differ only in radius** — and that radius gap *is* the wall. Group the dump's faces by
  `(origin, axis)`, take `abs(r1 - r2)` within each group, and you have every shell wall in the
  part with no estimation anywhere. It is exhaustive over concentric pairs and **blind to
  everything else** — a flat cut face approaching a curved one is exactly what it cannot see — so
  say which of the two you measured. `evDistance` is still the tool for the rest.
- **Flat walls need the material side, not just the spacing.** Two parallel planes 0.3 apart are a
  wall if plastic is between them and a gap if it is not, and the distance cannot tell you which.
  The dump can: each face carries `orientation` and its surface carries `isOrientedWithFace`, and
  the product of the two turned into the surface normal is the face's **outward** normal, which
  points away from material. So a pair is a wall only when the two outward normals oppose *and*
  point out of the space between them; every other close pair is a void. Skip this test and a
  shelled part reports thin walls it does not have — a boss standing 1.5 proud of a 1.2 shell
  leaves a 0.3 air gap at every one of them.
- **A throttled `featurescript` does not stop you measuring: `GET .../tessellatedfaces` answers
  200.** It returns triangles for **every** face, including the ones `bodydetails` gives up on and
  types `OTHER` with no geometry at all, so it reaches the cases the two searches above cannot —
  flat against curved, swept faces, fillets. Ask for a chord tolerance (`chordTolerance=0.0002`,
  `angleTolerance=0.02`) and expect a large answer: a 36 mm part came back as 185,582 facets and
  101 MB, so write it to a file rather than holding it, and do not commit it.
- **Do not pull a tessellation through `page.evaluate`.** It has to serialize the whole response
  across CDP, and past about 100 MB the tab dies — `TargetClosedError: Target page, context or
  browser has been closed`, with the browser itself still fine, so it reads like a dropped session
  when it is not. Use the browser context's own request object instead: `ctx.request.get(url,
  headers={'X-XSRF-TOKEN': …})` shares the signed-in cookie jar and streams straight to a file.
  `bodydetails` is small enough either way.
- **Size the tolerance to the part, or the request never finishes.** The same
  `chordTolerance=0.0002` that took 101 MB on the head did not return for the torso inside ten
  minutes; at `chordTolerance=0.001, angleTolerance=0.1` the torso came back in under four, at
  15.9 MB. Coarser costs accuracy — facet normals then lag the true surface by up to the angle
  tolerance, about 5.7° at 0.1 rad — so choose it against the smallest thing you mean to measure,
  not by what downloads fastest.
- **With the triangles you have the closed boundary, and that is enough for two things a kernel
  would normally do.** Closest approach between two faces: put every vertex in a spatial grid and
  compare only across cells, skipping pairs that share an `edgeId` because adjacent faces meet and
  the zero means nothing. Inside or outside: fire a ray and count crossings, odd is inside. Together
  they answer *thinnest wall anywhere* — the grid finds the close pairs, and the ray test says which
  are plastic and which are a slit.
- **Tangency is measurable, and looking at a render is not measuring it.** A render only shows that
  no crease is *visible*. Two faces meeting tangentially share a normal along their common edge, so
  take every pair that shares an `edgeId`, find the vertices they have in common in the
  tessellation, and compare the facet normals across them: zero degrees is tangent, anything else is
  a crease of that many degrees. Allow the angle tolerance you asked the tessellation for — at 0.02
  rad a true tangency reads as about half a degree, not zero. Then check the answer against
  `bodydetails`, where tangency is exact and always the same relation: the distance from an arc's
  axis to the line it meets equals the arc's radius.
- **Two faces can also come close by both running out at the same edge**, and then the midpoint sits
  exactly on the surface and the ray test is a coin toss. That number is the width of the land left
  between them, not a thickness. March a line inward instead and read the solid run: 1.2 of material
  behind a 0.4 gap means a narrow strip of face, not a thin wall.
- To measure into a cavity you must hide the part in front **and** right-click any plane →
  **Hide all planes**, or a plane sits between camera and target and swallows every click.
- **Hide applies to the whole current selection.** Hiding one part while another is still
  selected hides both, with no error and a blank screen.

## 9. Rendering the model, and looking at it

```
GET /api/partstudios/d/{d}/w/{w}/e/{e}/shadedviews?viewMatrix=isometric&outputHeight=900&outputWidth=900&pixelSize=0&edges=show&useAntiAliasing=true
```

returns `{images: [<base64 png>]}`, rendered server-side. Per part:
`/api/parts/d/{d}/w/{w}/e/{e}/partid/{pid}/shadedviews`, which frames that part alone.

`viewMatrix` takes `isometric`, `front`, `top`, `right`, `back`, `bottom`, `left`.

**Render every part on its own, from at least three angles, and look at the images.** A
whole-model isometric hides everything interesting: in run 1 a joint's entire fork was invisible
in all four standard views because the parts overlapped along the camera axis.

The view menu has *Isometric / Dimetric / Trimetric*, *Zoom to fit* and *Section view…* — but
**no Top/Bottom/Front entries**. Right-drag rotates, middle-drag pans, `n` is View normal to.

**Zoom to fit frames the default planes, not the part.** The planes are far larger than anything
this robot is made of, so `f` on a Ø9.4 collar leaves it a smudge in the middle of the window.
Hide Top, Front and Right first and `f` then frames the part.

**Sketches stay shown after you close them**, and `f` frames their union. A Ø20 circle came back
at 12.9 px per mm instead of 42.6 because a 100 mm rectangle two sketches earlier was still on
screen.

**Zoom to fit is exact arithmetic.** For a canvas W×H it sets
`scale = min(W / (1.05 * bbox_w), H / (1.05 * bbox_h))` and puts the bounding box's center on the
canvas center — a 5 % margin on whichever axis binds, not a fixed one in pixels. It is a home you
can return to: `f` gave 42.5714 px per mm at (923.0, 523.0) before and after an arbitrary scroll,
to the digit, and the same computed pixel selected the same circle both times.

**One wheel event multiplies the scale by 2^(1/12)**, 1.059463 — a semitone, twelve notches to a
doubling — whatever `deltaY` magnitude you send. So `round(12 * log2(target / current))` events
put you on a scale you choose. **Negative `deltaY` zooms in**, positive zooms out.

**`gui.zoom_to`'s target is pixels per millimeter, not millimeters across the canvas.** They run
opposite ways, so a number chosen as *how much of the model I want to see* zooms in when it should
zoom out. A 96 mm foot on a 1350 px canvas wants about 9; a 45 mm fork end wants about 13. Passing
140 puts you inside the part.

**Zooming keeps the point under the pointer still, which leaves it wherever it already was.** A
connector two thirds of the way down the canvas is still two thirds of the way down after the
zoom, and at a close scale that puts it off the edge. Pan it to the canvas center *first* — middle
drag from its projected pixel to `screen.CENTER` — then zoom about it, then pan again, because the
zoom moves it back. Re-project after every one of those, since each changes the camera.

**The view cube's arrow triangles turn 15° per click, not 90°.** Two clicks look like nothing
happened. Front to Left is six of them, and a seventh is what run 6 needed to see one ear's
domes past the other ear.

**To get a true orthographic view on screen, click a *face* of the view cube.** The cube's face
snaps the camera square and its label then names the view you are in, which is the confirmation
`n` never gives you. The cube's arrow triangles and its roll arcs produce partial rotations that
are hard to predict, and *View normal to* on the Front plane has come back 180° rolled. The view
menu's items are not `li` elements — scrape everything to the right of the canvas edge instead.

## 10. Read-only REST, for verification only

Same-origin `fetch` from inside the Onshape page. Cookie auth alone gives **401 on writes**; echo
the `XSRF-TOKEN` cookie back as an `X-XSRF-TOKEN` header. Full details and the encodings are in
[`onshape-api.md`](onshape-api.md).

Most useful for checking your own work:

- `GET .../features` — read `featureStates`; it is an **array of {key, value} pairs**, not a map.
- `GET .../parts/.../boundingboxes` — **the only thing that caught a rod extruded the wrong way**
  in run 1. Preview and isometric both looked fine. **Check a bounding box after any extrude that
  uses a starting offset.**
- `POST .../featurescript` — evaluate arbitrary FeatureScript against the model. Returns
  `{result, notices}`, and the notices carry real error text with line numbers.

**`massproperties` can hand back a center of mass of zero.** The head read
`centroid [0, 0, 0, -1e-06, -1e-06, -1e-06, 1e-06, 1e-06, 1e-06]` while sitting plainly off
center, so the middle of a part is not a number to test against. `bodydetails` gives each face's
`origin` in millimeters and answers the same questions properly: which way a cut ran, how deep it
went, and how many faces of each kind the part has.

**Read `expression`, not `value`.** `GET .../features` returns each quantity as
`expression: "1.35 mm"` with `value: 0` beside it. Reading `expression` is how run 2 pinned a
direction bug: the depths were right and `oppositeDirection: true` was the culprit.

**A Variable feature stores one expression per variable type, and only the typed one drives the
model.** `assignVariable` carries a `variableType` enum and the parameters `lengthValue`,
`angleValue`, `numberValue` and `anyValue`, with a generic `value` beside them that nothing
evaluates. Writing `value` alone is accepted, `GET .../features` reads the new expression back,
every feature status stays `OK`, and the geometry does not move. Write the parameter the type
names, and write `value` with it so the two cannot disagree.

**Read a change off the model, not off the feature you wrote it into.** `getVariable` in a
`POST .../featurescript` at the end of the tree, or a face census off `bodydetails`, tells a change
that reached the geometry from one that did not. In draft9p1p6 the feature said `#wedges = 24`, the
model said 12, and `#ring_out` answered `#flat - 0.4 mm` evaluated against the *new* `#flat`, so
even the stale value tracked its inputs and looked alive.

**Onshape's copy and version routes drop the `d/`.**
`POST /documents/{did}/workspaces/{wid}/copy` and `POST /documents/{did}/versions` answer;
`POST /documents/d/{did}/workspaces/{wid}/copy` and `POST /documents/d/{did}/w/{wid}/versions`
answer 404, which reads as a missing document rather than a missing prefix. A `GET` on the same
shape tells them apart before a write does.

**429 arrives late and is per-endpoint.** One run hit it on every call from the start and had to
take every number off the GUI readout. Another sailed through ~90 calls and then had `/features`
start returning `{"message":"Too many requests."}` while `/parts`, `/massproperties` and
`/featurescript` kept working. **`GET /features` returning `{"features":[]}` with status 200 is
not how it fails — check the status.** Do not build a verification plan that only works if REST
answers.

**429 clears in about a minute and a half of silence, and retrying resets the clock.** The one
place it was clocked end to end is
[`experiments/runs/2026-08-12-run3/torso/steps.log`](experiments/runs/2026-08-12-run3/torso/steps.log):
first 429 at 04:17:31, a 45 s backoff, one more failed attempt, then 200 at 04:18:54 — **83
seconds**. Against that, a retry loop of eight attempts at 20 s apart never recovered at all, and
run 5 recorded `featurescript` as 429 "for the whole second half of the run" while still calling.
Treat it as a bucket that only refills while you are not drawing on it: stop calling entirely,
wait longer than you think, then make **one** request. Polling is what turns a 90-second pause
into an outage that lasts as long as you keep polling.

**But 83 seconds is not the only kind of 429.** On 2026-08-14 `/features` on the torso stayed 429
through more than fifteen minutes of silence, with `/companies` answering 200 the whole time, so
the session was fine and one endpoint was not. Run 5 saw the same endpoint stay 429 for half a
run. **Plan for a route that does not need `/features` at all** — the GUI, or `bodydetails` and
`tessellatedfaces`, which both kept answering here.

**The longer one is a spent quota, and it says so in the headers.** Read on 2026-08-27: `/features`
answered `retry-after: 67201` — 18 hours 40 minutes — beside `x-rate-limit-remaining: 0`, and the
number counted down with the clock rather than resetting when the calls stopped. So the two kinds
are told apart by asking, not by waiting and seeing: a burst block either names a short wait or
names none, and a quota names hours. [`onshape-api.md`](onshape-api.md) § *Rate limits* carries the
endpoints that stayed open, and `api()` in
[`../src/stickbot/onshape_session.py`](../src/stickbot/onshape_session.py) now reads the header and
stops instead of laddering.

## 11. Housekeeping the report depends on

- **Rename features and parts as you go.** `Extrude 4` tells the next reader nothing, and run 1's
  hinge shipped with every feature unnamed.
- **Publish a named version before writing the report** — left rail → **Create version…**, the
  top icon, above Comments. A report citing only a workspace has recorded a moving target. The
  GUI route always works; if `POST .../versions` comes back 401 while `GET` on the same path
  answers 200, suspect a truncated XSRF token before concluding the endpoint is closed — see
  [`onshape-api.md`](onshape-api.md).
- **The left rail's buttons carry no label of any kind.** No `aria-label`, no `title`, no
  `data-automation`; a search for a button whose label says *version* finds nothing. Each one's
  `svg` `<use>` names its sprite instead, and the one to click is
  `#svg-icon-create-version-button`. The rail reads, top to bottom,
  `versions-history-panel`, `create-version-button`, `comments-panel`, `notes-panel`,
  `performance-panel`, `onshape-ai-advisor-button`, `action-items`.
- **The Create-version dialog's confirm button carries no `data-automation`.** It is a plain
  `<button>` whose text is `Create`; `[data-automation=ok-button]` times out. And the dialog is
  the reason to publish through the GUI at all when a page needs a frame of it — REST never shows
  it.
- **A version cannot be renamed from its context menu.** There is no *Rename*; use
  **Properties…** → edit the name → **Save**. Two versions are allowed to hold the same name, and
  nothing warns you, so a second publish under a name already used leaves the citation ambiguous.
- **Clicking a version parks the browser inside it, view-only**, and every frame taken afterwards
  carries a *Versions are view only* banner. **Return to Main** before shooting anything.
- **Deleting the tab you are looking at leaves an undismissable banner** — *Can't open tab. The
  tab does not exist in this document work* — with no ×, so `no_banner` retries and raises.
  `page.goto` the URL of a tab that still exists; the reload clears it.
- **`page.mouse.click` has no `modifiers` keyword.** For a shift-click, bracket the click with
  `page.keyboard.down("Shift")` and `.up("Shift")`.
- **There is no *hide planes* in the view menu.** Select Top, Front and Right in the feature tree
  (shift-click, per the line above), then right-click → **Hide**. A tree row's context menu
  sometimes needs a plain left-click first, and the very first right-click after a fresh CDP
  connect can be swallowed entirely — click again rather than concluding the row is wrong.
- **`featureStates` in the features response is a list of `{key, value}` wrappers**, not a dict.
  `.items()` raises and `s["message"]` raises; read `s["value"]["message"]["featureStatus"]`.
- **A `TargetClosedError` after `gui.tick()` does not mean the action failed.** It has fired with
  the browser alive and the feature committed; check the model before re-running anything.
- **The left-rail icons carry no `title` or `aria-label`.** Hover each and read the tooltip out of
  the DOM; do not count rows to guess which is which, because the rail's contents change with the
  tab you are on.
- **Take every click through [`../src/stickbot/onshape_gui.py`](../src/stickbot/onshape_gui.py).**
  Its guards are what stop a bad frame shipping: it refuses to shoot through a notification banner
  or a moving screen, checks that a canvas pick selected something, and reads every typed number
  back out of its field. [`onshape_screen.py`](../src/stickbot/onshape_screen.py) answers where
  things are — by reading the pixels, and by projecting a model point through the camera it reads
  off the GPU. [`onshape_record.py`](../src/stickbot/onshape_record.py) records a stage as video.
  How a capture is conducted is [`build/takes.md`](build/takes.md).
- **[`../src/stickbot/gui_steps.py`](../src/stickbot/gui_steps.py) is superseded** by those. It was
  the earlier choke point, and its numbered frames and `steps.log` belong to the wave-of-agents
  cycle that `build/takes.md` replaces.
