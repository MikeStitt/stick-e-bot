# Session 1 — the skeleton and the body

Build the robot's layout sketch and its torso. By the end there is one solid block, and a
skeleton of construction lines that every later part will hang off.

Units are **millimeters** throughout. Where a step says a number, type that number.

---

## Step 0 — Set the document to millimeters

A new Onshape document is in **inches**. The robot is in millimeters, so this comes first —
everything after it is wrong otherwise.

1. Click the **☰ menu** to the left of the document name, at the top of the window.
2. Choose **Workspace units…**
3. Set **Length** to **Millimeter**.
4. Set the precision next to it to **0.1** — one decimal place is plenty in millimeters.
5. Close the dialog.

**Check:** click anywhere in the graphics area and look at the bottom-right corner. Any
measurement it shows should end in `mm`, not `in`.

---

## Step 1 — The layout sketch

This sketch contains no shape at all. It is a skeleton: a set of lines marking where each
joint lives. Every part built later is measured from it, so it is the only place a height is
written down.

### 1.1 Start the sketch

1. In the Features list on the left, click **Front** to select the Front plane.
2. Click **Sketch** on the toolbar (or press **shift + s**… see the note below).
3. Press **n** to look straight at the sketch plane.

> **Shortcut note.** In Onshape, `shift+s` is the **Point** tool, not Sketch. Use the toolbar
> button for Sketch. The shortcuts that do work here are `l` line, `g` corner rectangle,
> `r` center point rectangle, `c` circle, `d` dimension, `q` construction toggle.

### 1.2 Draw the centerline

1. Press **l** for **Line**.
2. Draw one roughly vertical line, from below the origin to above it, passing near the origin.
3. Press **Escape** to put the Line tool down.
4. Click the line to select it, then press **q**. It turns into a dashed **construction** line.
5. With it still selected, press **v** for **Vertical**. It snaps upright.
6. Click the line's lower endpoint, then ctrl-click the **origin** point, then press **i** for
   **Coincident**. The line now passes through the origin.

**Check:** drag the line sideways. It should not move. If it does, the coincident constraint
did not take.

### 1.3 Draw the station lines

Five horizontal construction lines, each marking a height. Draw them all roughly first, then
constrain and dimension them — **do not try to click accurately**. Getting the position from a
dimension rather than from a careful click is the whole point.

1. Press **l** and draw five roughly horizontal lines crossing the centerline, spread out
   above and below the origin.
2. Press **Escape**.
3. Select all five (click the first, ctrl-click the rest) and press **q** to make them
   construction.
4. With all five still selected, press **h** for **Horizontal**. They straighten.

Now give them their heights. For each, press **d** for **Dimension**, click the **origin**,
click the **line**, click a clear spot to drop the label, then type the number and press
Enter.

| Line | Distance from origin | What it is |
| ---- | -------------------- | ---------- |
| 1st above | **24** | shoulders — also the top of the torso |
| 1st below | **24** | hips — also the bottom of the torso |
| 2nd below | **48** | knees |
| 3rd below | **72** | ankles |
| 4th below | **84** | the ground |

> **Where to drop the dimension label.** The two faint lines crossing at the origin are the
> other default planes seen edge-on, and they are clickable. Drop a label on one and you get
> an angle to a plane instead of a distance. Land it in clear space.

### 1.4 Make it fully defined

1. Click the green **✓** to accept the sketch.

**Check — the drag test.** Reopen the sketch (right-click it in the Features list → **Edit**)
and try to drag each line. Nothing should move, and every line should be **black** rather than
blue. Black means fully defined: there is no freedom left in it.

If something moves, that is the constraint you have not added yet. Add it and try again.

---

## Step 2 — The torso

### 2.1 The rectangle

1. Select the **Front** plane again and start a new **Sketch**. Press **n**.
2. Press **r** for **Center point rectangle**.
3. Click **on the origin** for the first click — Onshape will snap to it and show a marker.
4. Click again out to one corner. Size does not matter yet.
5. Press **Escape**.

A center point rectangle placed on the origin is already held there. That is why this course
never uses the **Fix** constraint: Fix pins something in place without saying why, and a
rectangle centered on the origin says exactly why.

### 2.2 Two dimensions

1. Press **d**, click the **bottom edge**, drop the label below it, type **36**, press Enter.
2. Press **d**, click the **left edge**, drop the label to the left, type **48**, press Enter.

**Check:** the rectangle should now be black. Drag a corner — nothing moves.

### 2.3 Make it solid

1. Accept the sketch with the green **✓**.
2. Click once inside the rectangle, on the fill rather than a line. The whole region goes
   orange, and the bottom-right corner reads **1728 mm²** — because 36 × 48 = 1728.
3. Press **shift + e** for **Extrude**.
4. In **Depth**, type **24**.
5. Tick **Symmetric**.
6. Click the green **✓**.

> **Tab, not Enter.** Inside a feature dialog, Enter means *accept the whole feature*, not
> *finished typing this number*. Press it early and the block gets built before Symmetric is
> ticked.

### 2.4 Name it

Right-click **Extrude 1** in the Features list, choose **Rename**, and call it **Torso**.

---

## What you should have

- **Parts (1)** — one solid block.
- A torso **36 wide, 48 tall, 24 deep**, centered on the origin in all three directions.
- A layout sketch that is entirely black.

**The measurement check.** Click the top face of the torso. The readout should say
**864 mm²**, because 36 × 24 = 864. Click the front face and it should say **1728 mm²**.
Two faces, and between them they prove all three dimensions.

---

## If something else happened

**The dimension came out as an angle**
: The label landed on one of the faint plane lines through the origin. Undo, and drop it in
  clear space.

**A line will not go horizontal**
: Something else is already holding it. Click the line to see the constraints attached to it,
  or click a constraint icon to see what it holds. Delete whichever one is fighting you.

**Onshape refuses a constraint**
: The sketch already says that. Same move: click the entity, read its constraints, remove the
  one that duplicates what you are adding.

**The extrude went one way instead of both**
: Symmetric was not ticked. Double-click the feature and tick it — nothing is ever stuck.

**Everything is in inches**
: Step 0 was skipped. Set the units, then double-click each dimension and retype it.
