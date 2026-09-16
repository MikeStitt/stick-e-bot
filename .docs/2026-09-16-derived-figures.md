# Figures that cannot go stale, and figures that are not supposed to

A drawing that explains why a dimension is right has two ways to rot: the picture stops matching
the design, or the picture is redrawn and the sentence above it goes on claiming something the new
picture disproves. The second is worse, because a correct drawing under a false heading looks
checked. This note says which drawings should be generated, which should be frozen, and what makes
the difference cheap rather than a standing maintenance cost.

## Both patterns already exist here

**Derived figures**, driven by the design source: `make_plans.py` emits the two plan sheets and
`make_brief_sheets.py` the three brief sheets, every number of them coming from `make_plans`. A
robot dimension changes in one place and both sets of drawings follow.

**A decision record done right**: [`reviews/hinge/`](reviews/hinge/). Its numbers are typed, in the
frozen `J` in `make_figures.py`, because the joint it reviews was replaced — and it says so at the
top of the page and twice in the generator. What it still does is generate: `make_figures.py` emits
seven SVG figures and all five `.rst` tables from that one frozen set, so the page's prose, its
tables and its pictures cannot disagree with each other. It reads `make_plans` for the drawing
primitives and the stylesheet, not for a dimension, and it solves its spring answers through
`hinge_spring` rather than typing them. The remaining four SVGs come from `seat_figures.py` and
`wedge_figures.py`, each frozen at its own snapshot.

**Decision records that do not say they are**: the three studies in
[`experiments/sketches/`](experiments/sketches/). `hip-clearance.py`, `socket-wrap.py` and
`slit-reach.py` import nothing but `math` and `pathlib` and type their inputs at the top, which is
right for a record — but until 2026-09-16 none of them said which version it belonged to. That is
the whole difference between them and the hinge review, and it is a label, not a mechanism.

## Three layers, three different costs

- **The picture.** Regenerating is one command. This is not the expensive part, and it is the part
  people worry about.
- **The prose beside it.** Typed numbers rot; generated tables do not. The hinge review settled this
  by emitting its `.rst` rather than writing it.
- **The claim in the heading.** Generation does not touch this, and it is the real hazard.
  `hip-clearance.html` is titled *The hip reaches its full travel without touching the torso.*
  Change `#stand` and a redraw will faithfully show the collision, under a heading still saying
  there is none.

## What makes the third layer cheap: the drawing asserts

Two of the three studies already compute their verdict. `socket-wrap` prints *✓ holds the ball —
retention +0.197 mm*; `slit-reach` prints *✓ four separate tabs*. **Make the verdict the exit
code.** Then a design change that breaks the claim fails a check rather than quietly rendering a
picture that disagrees with its title, and the drawing stops being documentation somebody has to
watch. It is the same move as every gate in `ninja check`: a rule that runs beats a rule written
down.

## Two kinds of drawing, and the current three are confused between them

**A derived figure** is regenerated from the design source, carries a verdict, and lives beside the
document it illustrates. It cannot go stale, because going stale is a build failure.

**A decision record** is a frozen picture of an argument made on a date. `socket-wrap` showing
`Ø5.803` beside `Ø11.520` is not a drawing of the robot; it is the case for doubling it. It should
never be regenerated. It should carry its date and the sizing it shows, and be left alone — which
is what `experiments/` is for.

Two of the studies caption a sizing *as built in `stickbot-for-bot-review`*, and this file used to
say that document appears in no run record. It does.
[`2026-08-20-stickbot-audit.md`](2026-08-20-stickbot-audit.md) audits it by id,
`did=111f975041ddb104a6028d45` and `wid=38e73619152eec8be2c51f8b`, at version **V1**; draft9p0's
plan lists it read-only with what to take from it and what to ignore; and a REST read on 2026-09-16
returned it by name with versions Start, V1 and V2. It is a second attempt at the whole robot,
built to the same specification with a different modeling practice: a joint's future mate point
goes at the origin and the part grows outward from it.

What the caption calls that sizing is *Current CAD*, and it has not been current since the robot
was doubled. Inside a `superseded` file that is not a defect — a decision record says what was
thought on a date, and the label at the top of the file now says which date. Left alone.

## What `make_plans` should and should not own

It should own the numbers and the drawing primitives — `circle`, `mm`, `rect`, `text` — and each
figure module should own its own picture and import them. That is how `make_figures.py` is built.

It should not grow a rendering function per study. It is already 1,383 lines and 140 definitions,
and folding every drawing into it produces exactly the god script the Constitution's *keep units
small, bounded, and side-effect-free* rule is about. The one way this becomes a genuine nightmare
is concentrating it.

## Why this matters more once the analysis is taught

An engineering course that shows the analysis behind the specs makes these figures the course
content rather than working notes. A course cannot be allowed to teach a number the design does not
have, so every figure in it has to be derived and every claim it makes has to be checked. Doing it
now, for three studies, is cheaper than doing it later for a syllabus.

## What this would take

- **Done 2026-09-16.** All three studies turned out to argue for a past decision and none to
  describe the design now, so none of them imports `make_plans`: they are labeled `superseded`
  with the version they belong to, per
  [`deciding-is-never-done`](../memory/deciding-is-never-done.md).
  `socket-wrap` and `slit-reach` are the case for doubling the robot, made before it was doubled;
  `hip-clearance` is the socket before draft9p1p4 settled `#wall` and `#collar`.
- **The verdict as an exit code is still owed**, and it belongs to the next figure that describes
  the design now rather than to these three. A decision record's verdict was true on its date and
  is not a check.
- **Done 2026-09-16.** `stickbot-for-bot-review` was already identified, by id and version, in the
  audit and in draft9p0's plan; this file was wrong to say otherwise, and the sketches' *Current
  CAD* caption stands as the record it is.
