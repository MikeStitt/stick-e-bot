# Test report — session 1, Sphinx draft

An agent followed `source/index.rst` exactly, in the Onshape GUI, in an empty document, on
the private headless browser. The REST API was allowed for verification only.

**Result: completed, and every dimension is exactly right.** But one step cannot be
performed as written, one instruction describes something that does not work at all, and
three more are missing an action you cannot proceed without.

## Verified correct

| Part | Measured | Expected |
| ---- | -------- | -------- |
| Torso | 36 × 24 × 48, centered on the origin | ✅ exact |
| Head | 36 × 30 × 36 above it | ✅ exact |
| Neck | 12 across, 6 tall | ✅ exact |

The neck's volume measured **678.584 mm³**, and π·6²·6 = 678.584 — it is a true cylinder,
not a many-sided prism. Both face-area checks read exactly as the lesson says: 864.0 and
1728.0 mm².

**The sketch is genuinely fully defined**, established two independent ways: every endpoint
sampled per-pixel came back grayscale with zero saturated blue anywhere in the sketch, and
three dragged corners moved the geometry not one pixel.

## The blocker — Step 6

**Accepting the torso extrude auto-hides Sketch 1.** The head and neck rectangles vanish.
Clicking where the head was selects the Front plane instead, and the status bar shows no
area at all. Steps 6 and 7 are both unreachable.

The fix is right-click **Sketch 1** → **Show**, which the lesson never mentions. This lands
at the exact moment the lesson is making its central point — *two features out of one
sketch* — and a room of thirty hits it simultaneously.

There is a sting in the tail: with the sketch shown again, its lines sit on top of the
solid and steal clicks meant for faces.

## The impossible instruction — Step 7.3

> "For **Revolve axis**, click the **vertical line through the origin**."

That line is the **Right plane seen edge-on**. In the Revolve dialog it does not highlight
and does not select — tried at three heights with the axis field focused, and the field
stayed empty and red every time.

What works is clicking the **neck's own left edge**, which reads `Edge of Sketch 1` and is
geometrically the same line.

**And the lesson contradicts itself.** Its own admonition says *"do not draw a construction
line where a real edge already is — two things in the same place are impossible to click
apart."* Step 3.2 then instructs the student to put the neck's left edge exactly on top of
the origin's vertical line, and Step 7.3 asks them to click the two apart.

## Missing actions

**The Dimension tool is still armed when you are told to select.** Steps 3.5, 4.3 and 4.4
all begin with an ordinary selection while Dimension is still on — as the lesson itself
said it would be, two steps earlier. Both picks get eaten, `i` silently arms Coincident
instead of applying it, and nothing errors. **Escape once first**, and the lesson never
says so.

**Zoom is never mentioned.** At the zoom you land on, the 6 mm neck is about 40 px across
and buried under constraint glyphs roughly 20 px each. Dimensioning it needed about
thirteen scroll notches in, and the head needed five back out.

**Constraint glyphs are clickable and occlude the geometry underneath.** The first neck
rectangle drew *nothing*: a parallel-constraint glyph floats directly above the torso's top
edge, centered on the centerline — precisely where the lesson says to start — and swallowed
the click. The existing warning about plane lines does not cover this.

**Nothing says how to clear a selection.** Escape is unreliable; clicking empty space
works. A stale selection turned one measurement into `Perp line and plane angle: 90.000`.

## The self-check does not work

The head is **30 deep** and the torso **24**, so the head's footprint fully contains the
torso's top face. From the isometric view the lesson sends you to, the visible sliver is
about **5 px**. Three clicks at it returned edge lengths and a stale angle before zooming
six notches in made it selectable.

That is the lesson's own verification step, and as written it produces a room full of
students reading numbers that are not 864.

## Smaller

- The units dialog has **twelve** "Display decimals" dropdowns; the step does not say which.
- `Front` is nested under a **Default geometry** folder, not loose in the Features list.
- The area readout is `Area: 1728.0 mm²` — the lesson omits the label and the `.0`.
- The Depth field already contains `25 mm`; the step does not say to clear it. *Untested —
  the agent select-all'd before typing.*
- The **Tab, not Enter** advice lives only in a sidebar; the numbered steps never say Tab.
- The checkbox is `Full revolve`, not "full revolution", and is already ticked.
- Selecting the "vertical line through the origin" highlights the **Right** row in the
  feature tree — you are constraining a sketch line to a *plane*. It works; the mental
  model the sentence gives is wrong.
- From isometric, the head's overhang completely hides the neck — the student cannot see
  the thing Step 7 just made. It is visible from the front.
- Step 8 renames features; the parts stay `Part 1/2/3` while the summary leads with
  "Parts (3)".

## Did the design plan drawing help?

**Yes** — referred back to three times: to confirm the 6 was the neck's height not its
width, that the head is 30 deep not 36, and that the head sits *on* the neck rather than
overlapping. The single most useful thing on it is the callout **"origin — center of the
torso"**, because that is the idea the whole sketch hangs on and the steps never say it.

Five things to fix in the drawing:

1. **The neck's 12 mm is drawn but never dimensioned** — and 12 is the punchline of Step 7.
2. **The `6` has no dimension line or arrowheads**, unlike every other dimension on the
   sheet, and the lesson uses 6 for both the neck's height *and* its width. Guessing wrong
   is silently survivable.
3. **The solid parts are drawn with rounded corners**; the lesson builds sharp boxes.
4. **The eyes are drawn in the solid style**, contradicting the caption's own key — a
   student will go looking for the eyes step.
5. **`24 deep` sits close enough to the pale leg** to read as the leg's dimension.

Nothing in the plan was numerically wrong.

## Timing

About **31 minutes** total — but this is an agent driving a headless browser with
screenshot analysis between clicks, and must not be read as student pace. What it says
reliably is the *shape* of the cost: **the neck took as long as every other step combined**,
and the three stages that overran are exactly the three where the text was incomplete.
