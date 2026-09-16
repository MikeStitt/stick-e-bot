# Test report — session 1, first draft

An agent was given [`onshape-steps.md`](onshape-steps.md) and told to follow it exactly, in the
Onshape GUI, in an empty document, with the REST API allowed only for verification. This is
what it found. The lesson was the thing under test.

**Verdict: it finished, but only by deviating from the written steps in four places.** A student
following the text literally is stopped dead at Step 1.4 and builds the wrong centerline at 1.2.

**Time: 52 minutes hands-on.** Step 1.3 alone took 21 of them.

## What was verified as correct

- The torso measures **−18…18 × −12…12 × −24…24 mm** — 36 wide, 24 deep, 48 tall, centered on
  the origin. Exactly as designed.
- Both stated area checks pass verbatim: top face **864.0 mm²**, front face **1728.0 mm²**.
- One part, named as instructed.
- Every UI name quoted in the lesson is correct, and **every keyboard shortcut in the shortcut
  note is right**, including that `shift+s` really is Point rather than Sketch.

## Fatal

**The layout sketch is not fully defined, and the lesson says it will be.** Nothing constrains
the station lines' lengths or their horizontal positions. In edit mode the line *bodies* are
black but the *endpoints* are blue, and they drag freely. The lesson's remedy — "that is the
constraint you have not added yet" — never says which, and no tool taught so far makes it
obvious. Thirty students hit this at once with no way forward.

**Step 1.2.6 builds the wrong centerline.** Making the line's lower *endpoint* coincident with
the origin pulls that endpoint onto the origin, so the centerline runs only upward. Everything
below the origin — hips, knees, ankles, ground — never crosses it. The intended constraint is
point-on-line between the origin and the *line*, not its endpoint.

**"Draw five roughly horizontal lines" produces one zig-zag.** The Line tool chains, and the
lesson only says to press Escape after all five.

**Pressing `d` before each dimension turns the tool off again.** Dimension stays armed after
each use; a second press toggles it off, and the following clicks then silently select things.
No dimension, no error, no feedback. It has to read *press `d` once — it stays on*.

**The given pick order produces diameter dimensions.** Clicking the origin first and the line
second yields Ø48 and Ø138.2. Clicking the **line first, origin second** gives a clean linear
distance every time.

## Serious

- **`ctrl-click` does not work on a Mac** — it opens the OS context menu. `shift-click` is the
  multi-select. The lesson says ctrl-click twice.
- **"Close the dialog" is ambiguous and the wrong choice silently discards the units.** The red
  ✗ reverts to Inch. It must say *click the green ✓*. This guards the one step the lesson
  itself calls fatal.
- **Step 0's check cannot be performed.** On an empty document there is no measurement readout
  at all; it only appears once geometry exists.
- **The final measurement check is impossible from where the lesson leaves you.** The top face
  is edge-on in a normal-to view, and the lesson never teaches rotating the view.
- **`n` in Step 2.1 flips the camera to the Back**, because it is a toggle and you are already
  normal-to. Harmless for a symmetric block, not harmless later.

## Smaller, but real

- Canceling a dimension with the red ✗ **keeps** it at its measured value, which then
  over-constrains the next one.
- "A clear spot" must also mean clear of dimensions already placed — two label placements were
  swallowed silently by an earlier extension line.
- A **useless coincident** can be created between a line and its own endpoint, glyph and all,
  holding nothing. The drag check then fails with no explanation available.
- Undo inside a sketch jumps further back than expected and can remove a constraint silently.
- A red "Syntax error in expression" appears while typing in a dimension box and clears on Tab.
- The dialog field is **"Length default unit"**, not "Length"; precision is **"Display
  decimals"**, and it does not affect the dimension edit box, which shows five decimals.
- Renaming the extrude to `Torso` leaves the part called `Part 1`.

## Assumed knowledge the lesson never states

1. Shortcuts need the pointer in the graphics area.
2. **One Escape drops the tool; two throw the whole sketch away** — and the lesson asks for
   five Escapes.
3. How to deselect, and that empty space is treacherous because of the plane lines.
4. That the Dimension tool stays armed between dimensions.
5. How to rotate the view at all.
6. That the origin, both plane edge-on lines and your own construction line compete for the
   same click.
7. What construction geometry looks like — dash-dot, and it changes color with state.
8. **That blue endpoints on a black line still mean under-defined.**

## What this changes

Every fatal finding is in **Step 1**, which also ate 21 of the 52 minutes.

It would be easy to read that as "construction geometry is too hard for beginners". It is not
what the evidence says. Look at what actually cost the time: the origin, the two default planes
seen edge-on, and the student's own construction line all sitting in the same place and
competing for the same click. The problem is **coincident geometry**, not construction geometry.

The rule that follows is narrower and more useful than "use fewer construction lines":

> **Do not draw a construction line where a real edge already is.** Do draw one where nothing
> else provides what you need — and a revolve axis is usually exactly that case.

The redesign already agreed — a layout sketch holding the *real boxes*, with features selecting
regions out of it — removes the duplicated lines, not the tool.

The findings that survive any redesign, and must be fixed regardless: the dimension tool
staying armed, line-before-point pick order, `shift-click` on a Mac, the green ✓ on the units
dialog, Step 0's unperformable check, view rotation being needed and never taught, `n` as a
toggle, two Escapes destroying a sketch, and blue endpoints meaning under-defined.
