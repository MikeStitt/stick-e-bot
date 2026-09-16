# How Onshape access actually works here

There is **no API key**, and one would not carry this work — see *Limits*. Everything runs on a
logged-in browser session. This works well and has real limits; both are worth knowing before
relying on it.

## The setup

1. Playwright, from the repo's own environment: `uv sync`. **That does not install the
   browser** — `uv sync` gets you a working import and a failing launch, which looks like a
   login problem and is not. `uv run playwright install chromium` is a separate, explicit
   step. The browser binary caches in `~/Library/Caches/ms-playwright`.
2. A **headed** Chromium on `--remote-debugging-port=9222`, launched with
   `launch_persistent_context` against a durable profile —
   [`../src/stickbot/browser.py`](../src/stickbot/browser.py). It stays running as a daemon, and it
   is where the user signs in.
3. A **headless** Chromium on `--remote-debugging-port=9223` with its own profile —
   [`../src/stickbot/agent_browser.py`](../src/stickbot/agent_browser.py) — which borrows the
   signed-in browser's Onshape cookies over CDP at launch. It has no window, so it cannot take focus
   or receive the user's keystrokes, and that is why it and not 9222 is what scripts drive.
4. Short-lived action scripts attach to **9223**, do one job, and detach. Closing that CDP
   connection does not close the browser. `onshape_gui.connect()` sets the port and refuses any
   other; `onshape_session.CDP_URL` still defaults to 9222, so anything importing it directly has
   to set it.
5. API calls are made with `page.evaluate(...)` running `fetch` **inside** the logged-in page, so
   they are same-origin against `cad.onshape.com` and carry the session cookies — exactly how
   Onshape's own web client talks to `/api`.

The **first** sign-in is by hand in the visible window, so Chrome is offered the credential and can
save it. After that `browser.py --signin` re-establishes the session on its own: it types the
account email and clicks through, and Chrome's password manager fills the password field. No
password is handled by the tooling either way — see [`onshape`](../.claude/skills/onshape/SKILL.md)
§ *Get the session back with the repo's own scripts*.

## Things that will surprise you

- **The automation browser shares nothing with Safari or Firefox.** Signing in to Onshape in a
  normal browser does not carry over. It is a separate profile with separate cookies.
- **Cookie auth alone is read-only.** Writes need the `X-XSRF-TOKEN` header — see
  [`onshape-api.md`](onshape-api.md).
- **A page navigating mid-script looks like a bug.** "Element was detached from the DOM" during
  sign-in just means the user completed the login while a locator was waiting.
- **There is no sign-out route to hit.** `/signout` redirects to the documents list with the
  session intact, and the app renders no sign-out anchor in the DOM. Deleting the `on` and
  `on-session-id` cookies over CDP is what ends a session, and it is how `browser.py --signin`
  gets tested from a signed-out start.
- **A hard kill costs a fresh borrow, and so does a clean one.** Playwright's SIGTERM handlers
  close the browser cleanly, which flushes *persistent* cookies to the profile. Onshape's session
  cookie is not one of them — see *Limits* — so no shutdown preserves the login either way.
- **Onshape is a heavy SPA.** Allow ~14 seconds after `goto` before the feature tree is reliably
  interactive. Screenshots taken too early show a login page or an empty viewport, and are easy to
  misread as a failure.

## Reading errors out of the UI

Feature error text is *not* in the API response — `GET .../features` gives you a status and nothing
else. The message lives in the UI tooltip:

```js
await page.getByText('Extrude 2', { exact: true }).first().hover();
// then read .tooltip / [role="tooltip"] / .tooltip-inner
```

That is how "No merge scope selected." and "Select a sketch plane." were found. Budget for this —
it is the only route to a readable diagnostic.

Toolbar buttons carry **no `title` attribute**; they are `div.tool.is-activatable.is-button` and
only reveal their names on hover. Hovering each one in turn is how the verified tool names and
keyboard shortcuts in [`taught-path.md`](experiments/taught-path.md) were collected.

## Driving the GUI from a script

Every toolbar button carries a `command-id`, which makes it directly selectable and its name
readable from `data-bs-original-title`. These were read off the live sketch toolbar:

| `command-id`             | Tool                       | `command-id`          | Tool                  |
| ------------------------ | -------------------------- | --------------------- | --------------------- |
| `LINESEGMENT`            | Line (l)                   | `USE`                 | Use (Project/Convert) (u) |
| `RECTANGLE_TWO_CORNERS`  | Corner rectangle (g)       | `TOGGLE_CONSTRUCTION` | Construction (q)      |
| `CIRCLE_CENTER_RADIUS`   | Center point circle (c)    | `TRIM`                | Trim (m)              |
| `ARC_START_END_RADIUS`   | 3 point arc (a)            | `OFFSET`              | Offset (o)            |
| `POINT`                  | Point (shift+s)            | `SKETCHMIRROR`        | Mirror                |
| `DIMENSION`              | Dimension (d)              | `COINCIDENT`          | Coincident (i)        |

Feature tools are the same idea: `newSketch`, `extrude`, `revolve`, `fillet`, `mirror`,
`booleanBodies`. Feature dialog rows carry `data-parameter-id` matching the REST parameter
names, and the accept and cancel buttons are `[data-automation=ok-button]` and
`[data-automation=cancel-button]`.

### Sketching, specifically

Five things cost an hour between them:

- **The feature toolbar is replaced while a sketch is open.** Waiting for
  `div.tool[command-id=newSketch]` is a reliable test for "no dialog is open".
- **Escape with no active tool discards the whole sketch.** One Escape leaves the drawing tool;
  accepting needs the green tick. A script that ends a sketch with Escape silently produces
  nothing at all.
- **A newly created sketch auto-orients to its plane; a reopened one does not.** Press `n` after
  reopening, or every click lands somewhere in perspective.
- **The other two default planes are drawn as lines through the origin, and they are clickable.**
  A click meant for empty space that lands on one silently adds it to the selection. A dimension
  then comes out as an angle to a plane rather than a length.
- **A dimension is: clear the selection with Escape, pick the tool, click the entity, click clear
  space to place the label, type, Enter.** The placement click has to miss all geometry *and* both
  origin axes, and be inside the canvas — a click a few pixels below the viewport bottom edge
  reads as a second entity pick.

### Five more, found while building the robot

- **Pick the right tab.** REST calls are a `fetch` from inside the page, so they are
  same-origin against *whatever that page is*. Attaching to the last tab means an open
  Learning Center tab silently becomes the API host: calls hang or 404 with nothing pointing
  at the cause. Always attach to a `cad.onshape.com` tab.
- **Opening a sketch zoom-to-fits.** Any screen-to-model mapping measured beforehand describes
  a camera that no longer exists, and everything drawn with it lands at the wrong scale with no
  error. Establish the camera at the same point in the calibration and in the drawing.
- **Measure direction, not just distance.** "Normal to" a plane can leave the camera on either
  side of it, and from behind the x axis runs the other way. A calibration that only measures
  lengths cannot tell, so every left-hand part lands on the right — silently. Calibrate with a
  *line*, whose start point is the first click, and keep the sign.
- **The sketch toolbar collapses into icon groups on a narrower window**, so a button that was
  in the DOM a moment ago may now be inside a dropdown. Pick tools by keyboard shortcut
  instead; the shortcut is always live.
- **Center point rectangle is not on the toolbar; it is in the rectangle group's dropdown.** Only
  `RECTANGLE_TWO_CORNERS` (Corner rectangle, `g`) is visible. The one the modeling standard asks
  for is `RECTANGLE_CENTER`, **Center point rectangle (r)**, read off the live dropdown on
  2026-08-20 — and the shortcut `r` reaches it without opening anything.
- **Draw roughly, then dimension.** A center point rectangle clicked at the origin and any second
  point needs no camera calibration at all, because the two dimensions set the size afterwards.
  That is also what a student does, so the taught path and the scripted one are the same path.
- **`shift+s` is Create new sketch in the Part Studio and Point inside a sketch.** Shortcuts are
  per tab. Both tooltips, read off the live toolbars: `Create new sketch (shift+s)` on the feature
  toolbar, `Point (shift+s)` on the sketch toolbar. Worth knowing before writing either into a
  lesson.

### Three more, found the hard way

- **The feature list does not keep every row in the DOM.** Once the figure was finished,
  `Sketch 10` was simply not there to be right-clicked, and scrolling the panel did not bring it
  back. Typing into the list's filter box does, every time. Clear the filter before photographing
  the tree.
- **"Normal to" (`n`) looks at a plane from whichever side the camera is already on.** After a few
  sketch edits, a script asking for the front view gets the *back* of the model and no warning.
  Reopening the document is the only cheap way to get a known camera; it always comes back to the
  same front-ish isometric.
- **Creating a sketch through the GUI is invisible to anything tracking features itself.** A
  script that draws one by hand and then carries on building through the API will stack its own
  `Sketch 1` on top of the hand-drawn one and end up with more features than it thinks.

## Two Onshape pages at once

**One profile holds two live Onshape documents, and the limit is in the attach rather than in the
browser.** Measured on 2026-08-25: two pages in the 9223 context, one on `stickbot-draft9p0` and
one on `stickbot`, both authenticated, both titled and resolved to a tab, sharing Onshape's own
cache worker — the second page was given a bare `/documents/<did>` with no workspace and Onshape
redirected it to a real workspace and element, which it does only for a signed-in session.

- **`connect_over_cdp` attaches to every target in the browser, so its cost follows the page
  count.** Against one open page it returned in **3.2 s**. Against four it did not return inside
  **150 s**, and afterwards the browser would not answer `/json/list` either. Restarting
  `agent_browser.py` cleared it — a wedged endpoint is one of the few reasons to override *leave
  the agent browser running* below.
- **Connect once and keep both page handles.** `onshape_gui.connect()` returns the first Onshape
  page it finds and makes one if there is none, so it cannot hand back two. A two-page script asks
  the context for its own pages and holds them.
- **Close what you opened.** Every page left behind is added to the next script's attach.
- **A second driven browser buys nothing.** It costs a second profile and a second borrowed
  session to do what a second page in the one context already does.
- **Give a probe a short per-call timeout.** An in-page `fetch` inside `page.evaluate` hung during
  this experiment, and with `set_default_timeout(180000)` each hung call cost three minutes. What
  the run needed was to fail in twenty seconds and say so.

## Limits — read before depending on this

- **The session expires**, and it is a copy of somebody else's — see the next bullet. It does run
  **headless**: the agent browser on 9223 has no window, and every capture and every measurement
  goes through it.
- **The agent browser's session dies with its process.** Onshape's `on-session-id` is a session
  cookie — no expiry, memory only, never written to a profile — so a durable profile directory
  does not make the login durable. `agent_browser.py` borrows cookies from the signed-in browser
  at every launch, which works only while that browser is still signed in. Leave the agent browser
  running rather than restarting it.
- **An API key would not carry this work.** Onshape's API-keys page allows this plan 2500 requests a
  year. One part's retake reads the feature list before and after every stage script and measures
  every acceptance check off `bodydetails`, which is hundreds of calls. Onshape's dashboard shows
  zero requests for us because a `fetch` from inside the signed-in page is web-client traffic and is
  not metered against that quota — it is metered as a burst rate instead, which is the `RateLimited`
  path in [`../src/stickbot/onshape_session.py`](../src/stickbot/onshape_session.py) and the
  account-wide 429 that once took over an hour to clear.
- Automating the GUI is slow and brittle compared to the REST API, and the capture pipeline drives
  it anyway, because the frames are what a guide ships. Everything a page does not have to show
  goes through REST.

## Clean up after probing

GUI probes leave artifacts. Opening the sketch dialog to read its field names creates a real
`Sketch N` in the feature tree if it gets accepted, and `Escape` sometimes cancels rather than
accepting. After any UI poking at a reference document, list the features and delete strays before
walking away.
