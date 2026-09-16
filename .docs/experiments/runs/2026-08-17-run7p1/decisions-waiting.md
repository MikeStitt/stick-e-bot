# Run 7p1 — what is waiting for a decision

## The slits stopped being a circular pattern and nobody wrote down why

Guide2 cuts the relief slits by drawing one slot and copying it with a sketch **Circular pattern**,
instance count 4. Guide3 draws two **Center point rectangle** bars crossing on the origin, four
dimensions in all, and no pattern.

The change landed in `9099207`, *Rebuild the ball and socket, and start guide3 from it*. The run 7
plan carries the new method as `S10`, sourced `build`, and says nothing about what it replaced. The
commit message does not mention it either. **There is no recorded reason.**

### What the record does hold

`S11` in [`../2026-08-16-run7/plan.md`](../2026-08-16-run7/plan.md), from the human run's
[`retro.md`](../2026-08-16-human-run1/retro.md), about the tool that was dropped:

- A circular pattern **inside a sketch** is a canvas manipulator, not a feature dialog.
- The instance count is a small gray `3x` tag on a leader line. A single click on it does nothing
  visible; a double-click opens it.
- There is no green tick. The pattern is committed by moving to white space and clicking.
- **Escape** discards it silently, and the sketch still closes clean and fully defined.
- The whole operation produced no frames, because the recorder writes on dialog events and no
  dialog opened.

That is a step that is hard to read back, hard to photograph, and hard to tell apart from a step
that did not happen. Whether it is why the switch was made is not written anywhere.

### What the two-bar route cost in this run

- Two bars give four slits only because the middle of the cross sits over the mouth of the hollow.
  The page spends a sentence saying so.
- The first bar collapsed twice when its length was dimensioned: its short ends sat within about
  9 px of the collar's rim, so the pick took the rim instead. Drawing the bar well inside the rim
  and letting the dimension carry it out fixed it. This is `H7`, and it applies to a mouse as well
  as to the harness.
- Everything else is a dimension typed into a box, which is what the rest of the page already
  teaches.

### A straight bar end against a round collar is a discussion point

**Mike's concern.** If the rectangle's corners are made coincident with the collar circle, the
bar's short end is a **chord**, and the circular segment between that chord and the arc is left
uncut. Even if Onshape cuts it anyway, students will find it and argue that the method is not
fool-proof, and the lesson slows down while they do.

**What the model holds.** Read back off `run7p1-ball-and-socket`: `collar profile` carries a
diameter of `#ball + 2 * #fit + 2 * #wall`, and `slit profile` carries the same expression as the
bar's **length**, plus `#slit` as its width. No constraint ties a corner to the circle.

So the sign is the other way round from the concern as described. With half-length equal to the
collar's radius and half-width `#slit / 2`, the corner sits at `hypot(4.7, 0.4)` = 4.716991, which
is **0.016991 mm outside** the rim. The bar's end line touches the rim at exactly one point, on the
axis, and lies outside it across the rest of the slit's width. Nothing is left uncut.

Snapping the corners to the circle instead would put the chord at 4.682948 and leave a segment
**0.017052 mm** thick and `#slit` wide, running the full depth of the cut. That is under a 0.4 mm
nozzle, so it would never print, but in the model it is a web joining each finger to its neighbor
down the whole slit — the fingers stop being able to spring, and at any normal zoom it is invisible.

Neither number is stable across a driving change, and both shrink as the joint grows:

| `#ball` | collar radius | overhang, as built | sliver, if snapped |
| --- | --- | --- | --- |
| 6 | 4.700 | 0.016991 | 0.017052 |
| 9 | 6.200 | 0.012890 | 0.012917 |
| 15 | 9.200 | 0.008692 | 0.008700 |

**The concern survives the correction.** A single-point tangency is still a single point, and it is
still what a student who zooms in will find and argue about. What is at stake is only which
argument the lesson has to answer: *"you cut exactly to the edge and touched at one point"* rather
than *"you left material behind"*.

**The fix that ends the argument** is to make the bar overhang — a length beyond the collar's
diameter rather than equal to it, so the end lies clear of the rim everywhere and the cut is
obviously complete. The cost is a number that is not derived from the joint, which is the thing the
rest of the page refuses to do. If it is taken, it wants a name and a reason, not a bare `+ 1`.
Not decided here.

### Left alone until you decide

- `S11` is still in the run 7 plan as a live finding about a step guide3 no longer has.
- The reason for the switch, whatever it is, has no home yet.
- Whether the slit bars overhang the collar, and what sets the overhang if they do.
