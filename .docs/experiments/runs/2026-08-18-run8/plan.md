# Run 8 — the ball and socket, with the slits patterned

Run 7 built the joint and wrote
[`instructions/robot-guide3/source/ball-and-socket.rst`](../../../../instructions/robot-guide3/source/ball-and-socket.rst).
Run 7p1 shot its figures. Since then three things moved, and the page no longer matches any of
them. This run takes the eight variables out of the joint, changes the slits from two drawn bars
to one slot and a **sketch circular pattern**, shoots the figures again, and carries the brief and
the page with it.

## What moved

**The joint's eight variables are being removed.** On 2026-08-17 the rule became: the major shapes
scale, the joints do not — *"we'll adjust the rules so that the joint details are not scaled with
the major robot scaling"*. Constitution 5.0.0 then cut
[`../../../robot-build-plan.md`](../../../robot-build-plan.md) to four driving variables, none of them
the joint's, and recorded that the page's eight are no longer asked for by anything. On 2026-08-18
the decision followed: they go. The joint is built from numbers typed where they are used.

**The pattern came back.** Guide2 cut the slits with a circular pattern. Guide3 replaced it with
two crossed bars and [nobody wrote down why](../2026-08-17-run7p1/decisions-waiting.md). The
reason we can reconstruct — the step was unphotographable and unverifiable — is now answered:
[`../2026-08-18-spike-pattern/findings.md`](../2026-08-18-spike-pattern/findings.md) drives it,
photographs it, and reads the result back out of the document.

**`S11` stops being an orphan.** It is a finding about a step the page will have again, and it is
the source for the section this run writes.

## Settle before the build

**S-1 — the seed and the count.** The brief says *"a slot drawn straight through the axis is
already two slits, so the pattern is 2 instances over 90°, not 4 over 360"*. That was written for
the **feature** circular pattern, which takes an axis and an angle in a dialog. The sketch
circular pattern has no dialog: it arrives as a full circle, and the only control the reader meets
without extra work is the instance count. Two instances over a full circle put the second bar on
top of the first.

So the seed changes shape: **one slot running outward from the origin**, patterned **4 over 360°**.
Its inner end sits on the origin, which is inside the mouth radius by a wide margin — the brief's
*"the slit's inner end must sit inside the mouth radius, or the mouth never opens"* is satisfied
by construction rather than by a number. Fully defined wants one constraint and two dimensions:
the inner edge's **midpoint on the origin**, then the slot's **length** and `#slit` across it.

The four seeds overlap in a small square at the origin, and the union should be the same plus
shape the two bars cut today. **Expected, not verified** — the build tests it by comparing the cut
against run 7p1's, and if regions come out awkward the fallback is an inner end dimensioned clear
of the mouth at a third dimension's cost.

**S-2 — the outer end against the rim.** The seed's outer end meets the collar's round rim, which
is the question [`decisions-waiting.md`](../2026-08-17-run7p1/decisions-waiting.md) left open: a
length equal to the collar's radius touches the rim at one point and leaves 0.017 mm of overhang
across the slot's width, and a length snapped to the circle leaves a sliver of the same size
uncut. This run has to pick one, because the seed is drawn once and copied. Neither number is
worth a student's argument; the plan's recommendation is a named overhang so the cut is
obviously complete, and the name and reason are decided when the section is written, not here.

**S-3 — the brief and the page disagree about the depth.** The brief's acceptance check says *"the
slits are 5.5 mm deep, not 2.7 — it must run the collar's whole length, −4.150 to +1.350"*. The
page cuts `#collar - #wall` and keeps a floor, and says the floor *"is the thing that pulls them
closed again once the ball is in"*. Both cannot be right. The check was written against run 1's
failure, where a two-sided depth sent half the cut into the air; the floor is run 7's design.
Settle which the model is, then fix whichever document is wrong — and give the old check a new
tell, because the failure it was written to catch is real.

**S-4 — what replaces the variables.** Decided: no `Variable` features, and no `#name` in any
dimension box. Every expression the page currently types is one grep away, and each becomes a
number:

```sh
grep -oE '``[^`]*#[a-z_]+[^`]*``' instructions/robot-guide3/source/ball-and-socket.rst | sort -u
```

Four of them are arithmetic rather than a value the reader was given, so the page has to say where
each comes from at the moment it is typed: the collar's **9.4** is the ball plus two gaps and two
walls, the hollow's **3.2** is half the ball plus the gap, the cut's **4.0** is the collar less one
wall, and the slot's length is the collar's radius, **4.7**, plus whatever S-2 settles.

**The cost, stated once.** The model stops surviving a change to the ball's diameter: anyone
resizing the joint later re-types every number that came from it, and nothing in the tree says
which those are. The joint is a fixed-size snap fit, and this is the price of not teaching
variables on the first page a student ever builds.

## Where the work is

A new document, `run8-ball-and-socket`, on port **9223**. `run7p1-ball-and-socket` is left exactly
as it is: it is what the current page cites, and it stays the recovery point until run 8's page
lands.

**Removing the variables costs the whole frame pool.** The feature tree is open on the left of
every figure, and it currently reads `Features (18)` with eight `{x} #ball = 6 mm` rows under
*Default geometry*. A page that never makes them cannot show them in forty-five pictures. So the
economy of editing the run 7p1 document is gone, and the build is the whole joint again.

## The frames

The page names every image it wants, so the shot list is still the page:

```sh
grep -oE 'images/[a-z0-9-]+\.png' instructions/robot-guide3/source/ball-and-socket.rst
```

**Every frame is shot again**, because the tree in every one of them names variables the page no
longer makes. Two slugs retire rather than move: `bs-02-the-variable-dialog-with-ball-and-6` and
`bs-03-eight-variables-at-the-top-of-the-tree`. The rest keep the numbers they have, gaps and all
— a slug is a name, and renumbering forty-five files to close two gaps is churn the page would
have to be edited for twice.

| Frames | What they become |
| --- | --- |
| `bs-01` | unchanged in content: workspace units, still the first thing done |
| `bs-02`, `bs-03` | retired with the variables |
| `bs-04` … `bs-30` | the same steps, with numbers in the dimension boxes instead of `#names` |
| `bs-31` … `bs-37` | the new section: one slot, its two dimensions, and the pattern |
| `bs-38` … `bs-43` | the same extrude, on a sketch that now has patterned regions |
| `bs-44`, `bs-45` | the tree — ten rows shorter — and the new version |
| `bs-00-*` | both overviews, from the new document |

New frames the section needs, and none of them exists in any pool:

- the four sides picked, before the tool — the pick that decides what gets copied;
- the pattern as it arrives, three instances and the `3x` tag, at a zoom where the tag is legible;
- the count box open with `4` in it;
- the accepted pattern, four slots, `4x`.

The tag is about 19 x 12 px at working zoom, so the tag frames are shot zoomed in and the wide
frame is a separate figure. `f` is exactly computable now, so both are deterministic —
[`../2026-08-18-spike-camera/findings.md`](../2026-08-18-spike-camera/findings.md).

## Harness rules

Run 7's H4 to H8 carry forward unchanged. The spike adds four:

| | Rule |
| --- | --- |
| H9 | After every canvas pick, the orange must increase. Run 8's spike lost one of four sides silently and patterned three |
| H10 | Read `getComputedStyle(canvas).cursor`. `Confirmation_Cursor` means a pattern is pending; `default` everywhere means it was accepted |
| H11 | The count box is a DOM input. `fill()` and read back — `Control+A` is line-start on macOS, and typing after it made 43 instances |
| H12 | Reach an existing pattern with **Show constraints off**: hover any instance, one new mark appears in the frame, walk to it, right-click, **Edit pattern** |

The screencast (`rec.py` in the spike's scratchpad) runs for the whole build. It is the only
record of a step that raises no dialog event, and it is what the human recorder could not see.

## What the page becomes

- **The numbers, once, at the top** loses its subject. What survives is the units step and the
  reason the joint's numbers are what they are — a ball twice as big still needs the same 0.2 mm
  gap, because that comes from how the plastic bends. What goes is the eight-row table, the
  Variable tool, and the promise that the tree will tell you why a number is what it is. Each
  number is now introduced where it is typed.
- **Two bars, four slits** → **one slot, patterned four ways**. New steps: draw the slot, put its
  inner edge's midpoint on the origin, dimension its length and its **0.8** width, select its four
  sides, pick **Circular pattern**, double-click the `3x`, type `4`, then move to white space and
  click the cursor with the green button. It has no green tick of its own.
- **An advice callout for getting back in**, which is H12 written for a reader: turn **Show
  constraints** off, hover a slot, and right-click the little pattern icon that appears.
- **How you know it worked**, in the reader's terms: four slots, and the extrude previews four
  cuts. Escape discards the pattern silently and the sketch still closes clean and fully defined.
- **Cut the slits** keeps its steps. `#collar - #wall` becomes **4.0**, with the sentence that
  says where 4.0 came from, and the frames are shot against the new sketch.

## What the brief becomes

- Step 6's *"2 instances over 90°"* gets the sketch-pattern case beside it — see S-1.
- **The numbers table is now the only place the joint's numbers are named.** The page cites values
  as it types them and no longer holds a table of its own, so a change to the fit or the slit width
  starts here and reaches the page as prose edits, not as a variable's value.
- The depth check is resolved either way S-3 goes, with a tell that catches the failure it was
  written for.
- The stretch section stops calling the circular pattern optional; it is the method now.
- The feature circular pattern's axis rules stay where they are. They are a different tool and
  this run does not touch it.

## Floor and ceiling

**Floor.** The joint rebuilds with the pattern, every acceptance check in the brief is measured
rather than inferred, every image the page names exists, and Sphinx builds with no missing-image
warning.

**Ceiling.** The instruction above each new frame is checked against the frame — run 7's F3, and
the audit task #26 asks for — and the page's pattern section is walked from an empty document by
someone who did not build it.

**Recovery point.** A published, named version of `run7p1-ball-and-socket` with the patterned
slits, cited by the page in place of the version it cites now.

## What this run does not do

It does not touch `robot-guide2`, it does not change the stud, the collar or the hollow, it does
not amend the Constitution or its parts, and it does not go near the feature-level circular
pattern. If a step cannot be shot as the page describes it, the page changes and the change is
reported — not the caption.
