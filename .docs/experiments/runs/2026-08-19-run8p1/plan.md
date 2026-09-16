# Run 8p1 — variables back, and the pattern's centre pinned down

Run 8 built the joint from typed numbers and cut its slits with a sketch circular pattern whose
seed was pinned to the origin. Three things change, and the tool does not:

1. **The variables come back**, and with them the expressions in the dimension boxes.
2. **The slot is dimensioned clear of the centre**, the way run 6 did it.
3. **The pattern's centre gets constrained to the origin**, which is the thing run 8 never tried
   and the reason its sketch could not be fully defined.

The stud, the collar and the hollow keep their shapes. Every measurement is the same measurement;
what changes is how the model records why.

## Why the variables come back

Run 8's plan removed them because
[`../../../robot-build-plan.md`](../../../robot-build-plan.md) had been cut to four driving variables,
none of them the joint's, and nothing was asking for the other eight. That reasoning was about
**scaling** — and it is still right about scaling. A ball twice as big still needs the same 0.2 mm
gap, because that number comes from how the plastic bends.

The reason to bring them back is different: **the model should carry its own design intent.**
`#collar - #wall` says *the whole collar except one wall thickness*. `4.0` says nothing, and the
next person to change the wall has to find every number that moved with it. Run 8 wrote that cost
down and accepted it:

> The model stops surviving a change to the ball's diameter: anyone resizing the joint later
> re-types every number that came from it, and nothing in the tree says which those are.

This run stops accepting it. The eight variables are labels that make the arithmetic checkable,
not knobs for scaling the robot, and the page says so where it introduces them.

**This plan argues for eight rows; it does not create them.**
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) is explicit: a number is a variable
when it has a row in the build plan's Variables table and is not one otherwise, and a run plan MAY
argue for a row but does not create it. So
[`../../../robot-build-plan.md`](../../../robot-build-plan.md) needs eight rows added before the build
starts, marked **not scaled**, alongside the four driving ones. Its *Proportions* section already
anticipates this — *"a later run can promote one without re-deriving it"* — but it also says the
not-scaled numbers *"would not belong in the variables table"*. **That sentence and this run
disagree, and the disagreement has to be settled in the build plan, not here.**

## The eight, as run 8 removed them

| Variable | mm | What it means |
| --- | --- | --- |
| `#ball` | 6 | the ball's diameter |
| `#stalk` | 3 | the stalk's diameter |
| `#fit` | 0.2 | the gap between the ball and the hollow it turns in |
| `#wall` | 1.5 | how much collar there is outside the hollow |
| `#collar` | 5.5 | the collar's height |
| `#grip` | 1.35 | how far the collar reaches up past the ball's centre |
| `#slit` | 0.8 | how wide each relief slit is |
| `#stud_len` | 5 | how far the stud's top face stands above the ball's centre |

And the expressions that go back into the dimension boxes:

| Where | Expression | mm |
| --- | --- | --- |
| stud arc radius | `#ball/2` | 3 |
| stud top line | `#stalk/2` | 1.5 |
| origin to stud top | `#stud_len` | 5 |
| collar circle | `#ball + 2 * #fit + 2 * #wall` | 9.4 |
| collar extrude, up | `#grip` | 1.35 |
| collar extrude, down | `#collar - #grip` | 4.15 |
| boolean offset | `#fit` | 0.2 |
| slit width | `#slit` | 0.8 |
| slit cut depth | `#collar - #wall` | 4.0 |

## What run 6 did with the seed

From a photograph of `run6-ball-and-socket` (`d421233fbff9374b85bb6cc9`) with `slit profile` open
for editing, 2026-08-19: the sketch is on the **Top plane** with **Disable imprinting** ticked,
and the slot carries **four dimensions measured from the axes** — inner end **2.5** from the y
axis, outer end **6**, each long side **0.4** from the x axis. A **`4x`** tag and a pattern glyph
sit among the constraints, and the tree has **no pattern feature row**: the pattern is inside the
sketch, the same tool run 8 used.

**All four slots render blue.**

Guide2's collar is Ø9.4, the same as this one, so the numbers are about the same geometry.

Guide2's page gives the reason the slot stops short: *"Each slot stops 2.5 mm short of the center,
so the collar's floor stays in one piece and the four fingers stay joined at the bottom. That is
what lets them spring back."* Run 8's seed starts on the origin, so its four slots meet in a plus
over the mouth. This run goes back to run 6's placement.

## Settle before the build

**S-1 — pin the pattern's centre to the origin, and teach the freedom before you remove it.**
The spike found the pattern arrives with *"a pivot square on the origin"*. Sitting on the origin
is not the same as being held there, and that unconstrained point is the likeliest reason run 8's
copies stayed blue. Run 8 never tried to constrain it.

The step, and it teaches the idea as well as fixing the sketch:

1. **Drag one of the copies.** The whole pattern swings round. That is the degree of freedom, and
   it is the answer to *why is it still blue*.
2. **Undo** ( *ctrl/cmd+z* ). Everything goes back.
3. **Box-select the origin and the pattern's centre point together.** They sit on top of each
   other, so a click and a shift-click cannot separate them — dragging a selection box over both
   is what picks up two coincident points.
4. **Coincident** ( *i* ). The two points are now one.

**Expected, not verified: the sketch goes fully defined and every slot turns black.** The build
tests it. If it does not fully define, the build reports what degree of freedom is left rather
than the page promising a colour that does not arrive — and run 8's S-5 stands after all.

**S-2 — two of the four slit numbers need an expression, and neither is obvious.** `#slit/2`
gives the 0.4 either side, exactly. The other two do not fall out of the eight:

- **The inner end, 2.5.** Its job is to sit inside the mouth, and the mouth's radius is
  `sqrt((#ball/2 + #fit)^2 - #grip^2)` = 2.9013. The honest expression is that minus a margin,
  which is heavy for the first page a student builds. The alternatives are a ninth variable with a
  name that says what it is, or a plain number with the sentence that says why.
- **The outer end, 6.** Its job is to clear the collar's rim, `(#ball + 2*#fit + 2*#wall)/2` =
  4.7. `+ #wall` gives 6.2; `+ #slit` gives 5.5. Neither is 6, and 6 was not derived from anything
  — it was drawn long enough to be obviously long enough.

**Recommendation: two more variables, `#slit_in` = 2.5 and `#slit_out` = 6**, each with a row and
a meaning, so the sketch has no bare numbers in it at all. That makes ten rows, not eight. Decide
before the build, because it changes the first section of the page and two of its figures.

**S-3 — which plane the sketch goes on.** Run 6 used the **Top plane** with **Disable imprinting**
ticked; run 8 used the **collar's top face**.
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) says to anchor a sketch to the geometry
that gives it meaning, and the slits belong to the collar. **Recommendation: keep run 8's collar
top face** and take run 6's dimensions onto it. Both are proven on this geometry, so this is a
teaching choice, not a modeling one.

**S-4 — the socket will not measure what run 8 measured.** Run 8's plus removes material near the
axis that these four slots leave in place, so `Socket body` comes out **larger** than 248.9915 mm³.
The build measures it and the register records it. No acceptance check carries run 8's number
forward unchanged.

**S-5 — the cut keeps run 8's depth.** `#collar - #wall` = 4.0 deep over a `#wall` floor, **Merge
scope** = `Socket body`. Run 8's S-3 settled that against runs 2 and 3's cut-through, and nothing
here reopens it.

## What the page becomes

- **The numbers, once, at the top** gets its subject back: the **Variable** tool, the table of
  eight (or ten — S-2), and the promise that the tree says why each number is what it is. The
  advice callout *These are labels, not a size knob* comes back with it, because the reason for
  the variables is design intent and not scaling.
- **Every dimension box takes an expression again**, with the sentence that says what the
  expression means where it is typed. `#ball + 2 * #fit + 2 * #wall` is *the ball, plus the gap on
  each side, plus the wall on each side*.
- **The slot is drawn clear of the origin** and dimensioned to the axes. The **midpoint** step
  goes, and with it the shift-click on an edge that is hard to hit.
- **A new step after the pattern**: drag, undo, box-select, **Coincident** ( *i* ) — S-1. It is
  the only place on the page where a reader is asked to break something on purpose, and it earns
  its space by answering the question the blue was already raising.
- **How you know it worked** becomes four slots with a gap in the middle over the mouth, and a
  sketch that closes **fully defined** — if S-1 lands.
- **Getting back to the pattern** stays. It is H12, verified in run 8, still the only way back
  into a sketch pattern.

## What the brief becomes

Yes — the brief changes, and it changes in four places:

- **Step 6's "2 instances over 90°" is settled by the seed.** A slot drawn through the axis is
  already two slits and wants 2 over 90°; a slot drawn to one side wants 4 over 360°, which is
  also the tool's default. Both belong, with the seed as the thing that decides.
- **The mouth-radius rule gets its number back.** *"The slit's inner end must sit inside the mouth
  radius, or the mouth never opens"* was satisfied by construction in run 8, because the slot
  started on the origin. It is now satisfied by a dimension, 2.5 against 2.9013 — which is the
  form the brief asks for.
- **The numbers table stops being the only place the joint's numbers are named.** Run 8 moved that
  sentence in when the variables went; with the variables back, the model names them too, and the
  brief's table is the source the variable values are set from.
- **The `Socket body` volume row is re-measured** — S-4.

## The frames

`bs-02` and `bs-03` **come back from the dead**: the Variable dialog and the variables at the top
of the tree. Their slugs were retired by run 8 and are re-used, because they name exactly what
they showed before.

**Every other frame is re-shot**, because the feature tree is open on the left of all of them and
it now has eight more rows than it did — the same reason run 8 had to re-shoot everything when the
variables went. The dimension boxes also read expressions rather than numbers, so `bs-08`,
`bs-09`, `bs-10`, `bs-19`, `bs-22`, `bs-23`, `bs-29`, `bs-35`, `bs-36` and `bs-41` change content
as well as tree.

New frames the slit section needs: the two extra dimensions on the slot, the drag that shows the
freedom, and the box-select with **Coincident** applied. Letter suffixes continue from `bs-37d`.

## Harness

Run 8's guards carry forward and are why this run is cheaper than run 8 was: `no_banner()` refuses
to shoot through Onshape's notification strip, `still()` refuses to shoot a moving frame, and every
number goes in through a double-click, a `fill` and a read-back.

H9 to H12 stand. One new rule the drag needs:

| | Rule |
| --- | --- |
| H13 | A drag is only proof of a degree of freedom if the geometry moved. Read the slot's pixels before and after, and fail if they are the same — a drag that missed its target looks exactly like a fully defined sketch |

## Floor and ceiling

**Floor.** The joint rebuilds with the variables and the expressions; the slot is dimensioned clear
of the centre; the pattern's centre is constrained and the result — defined or not — is reported
as measured; every acceptance check is measured rather than inferred; every image the page names
exists; Sphinx builds with no missing-image warning.

**Ceiling.** The pattern section is walked from an empty document by someone who did not build it
— run 8's ceiling, still unmet. And the variable lesson's real test: change `#fit` from 0.2 to 0.3
and confirm every dependent dimension moves with it.

**Recovery point.** A published, named version of the run 8p1 document, cited by the page in place
of `run8-ball-and-socket-v3`.

## What this run does not do

It does not touch `robot-guide` or `robot-guide2`, it does not change the shape of the stud, the
collar or the hollow, it does not go near the feature-level circular pattern, and it does not
amend the Constitution or its parts. It does not add rows to
[`../../../robot-build-plan.md`](../../../robot-build-plan.md) — it argues for them. If a step cannot be
shot as the page describes it, the page changes and the change is reported — not the caption.
