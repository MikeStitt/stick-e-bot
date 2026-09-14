# Session 1 — lesson design

Paired with [`onshape-steps.md`](onshape-steps.md), which is the student-facing script.

## What this session is for

One idea, taught three times: **geometry gets its position from constraints, not from careful
clicking.** The layout sketch says it, the torso says it again, and the drag test proves it.

Everything else in the session — units, the extrude, the rename — is scaffolding for that.

## The clock

| Block | Minutes | What happens |
| ----- | ------- | ------------ |
| Settle | 10 | Signed in, document made, units set to millimeters |
| Demo: the layout sketch | 15 | Instructor draws it badly on purpose, then constrains it |
| Do: the layout sketch | 25 | Students build theirs; drag test before accepting |
| Demo: the torso | 10 | Center point rectangle on the origin, two dimensions |
| Do: the torso and extrude | 20 | Students build and measure it |
| Wrap | 10 | Version published, look at each other's work |

That is 90 minutes of hands-on inside a 120-minute session, with the rest lost to arriving,
signing in and packing up. If the session is running long, the layout sketch's lower stations
(knee, ankle, ground) can be cut to next time — the torso only needs shoulder and hip.

## Floor and ceiling

**Floor** — every student leaves with a solid torso, 36 × 48 × 24, centered on the origin.
Nothing in Session 2 depends on the layout sketch being complete, only on it existing.

**Ceiling** — for anyone who finishes early:

- Add the remaining stations and make the two leg segments **Equal** instead of dimensioning
  the knee and ankle separately. Then change one number and watch both move.
- Deliberately over-constrain a rectangle — dimension its width, its height *and* its diagonal
  — and find the redundant one by clicking constraints.
- Create a variable for the torso height and drive the dimensions from it.

## The two demonstrations that matter

**Draw it badly on purpose.** When the instructor draws the station lines, they should be
visibly crooked and unevenly spaced. Then watch them snap straight as `h` lands on them, and
jump to position as each dimension is typed. A room that has seen geometry *move* when a
constraint is applied does not go on to believe constraints are labels.

**Drag it before accepting.** Every sketch, every time. It costs a second when the sketch is
finished and saves ten minutes when it is not. It is also the only way to tell — Onshape says
"fully defined" by turning the sketch black and nowhere else.

## What will go wrong

| Symptom | Cause | What to say |
| ------- | ----- | ----------- |
| Everything is in inches | Step 0 skipped | Set units, then double-click each dimension and retype |
| A dimension came out as an angle | The label landed on a default plane's edge-on line | Undo, drop it in clear space |
| "Onshape won't let me add this constraint" | It already says that | Click the entity, read its constraints, delete the duplicate |
| The whole sketch vanished | Escape pressed twice | Undo. One Escape puts the tool down; the green tick accepts |
| The block only grew one way | Symmetric not ticked | Double-click the feature and tick it |

## Assessment

Not a mark out of ten. Three yes-or-no questions a mentor can check from across the room:

1. Is there one part, and is it the right size? (Click a face; the area readout is the answer.)
2. Is the layout sketch black?
3. Can the student say what would happen to the torso if the shoulder line moved?

The third is the one that matters. A student who can answer it has understood the session;
one who cannot has drawn a rectangle.

## Known gaps in this plan

- **Nobody has taught it.** The timings above are estimates, not measurements.
- **The variables ceiling is unverified.** Onshape's variable feature has not been located in
  the GUI for this course yet; do not promise it until it has been.
- `shift+s` is **Point**, not Sketch. The steps say so, but it is the kind of thing that
  catches an instructor out live.
