# Design sketches

Two kinds of drawing live here. **Explanatory diagrams** — the HTML behind each page published to
claude.ai, where the file is what changes when a number moves, because a published page can be read
but not edited. And **frozen revisions of the initial sketch**, so the plan can be shown changing
under what building it taught.

## A sketch is dated, not current

Each one records the geometry as it stood the day it was drawn, including the reasoning that was
wrong at the time and the correction that followed. The numbers a part is built to live in
[`../build-briefs/`](../build-briefs/). Where a sketch and a brief disagree, the brief is right.

Four carry numbers the design has left behind. Each says so on its own page now, because a
published sketch can be opened by its link without ever passing this table:

- `figure-design-sketch.html` — the concept the project started from: a 150 mm target height, a
  Ø8 limb rod, a Ø6 ball and a 5.0 mouth. The limb is Ø24 and the ball Ø12.
- `socket-study.html` — a Ø16 thigh and `#grip` 1.5, rendered from a model that no longer exists.
- `collar-step-back.html` — the stalk binding "at about 40°". Derived, the limit is 41.76°.
- `hinge-stackup.html` — the fork inside a Ø12 limb, sized before ear and tab were matched on
  section modulus over free length.

## What each one settled

| File | Drawn | What it settled | Published |
| ---- | ----- | --------------- | --------- |
| `figure-design-sketch.html` | 2026-08-10 | Every proportion as a fraction of `#torsoH` 48, and the hand sized to a Ø3.2 LEGO bar | [link](https://claude.ai/code/artifact/45d32957-479f-4ea3-ae5b-5e92fc673ed8) |
| `collar-step-back.html` | 2026-08-11 | That collar height buys swing while limb diameter costs it — why the limb stayed Ø12 | [link](https://claude.ai/code/artifact/6c57b0b2-ce16-45e4-a818-6eb46402c921) |
| `socket-study.html` | 2026-08-11 | Four renders marked up: the sharp mouth rim, the slit root, and a wrong claim that the head's face would block the swing | [link](https://claude.ai/code/artifact/4ca4551b-9045-4679-b0e6-74b1a506c886) |
| `hinge-stackup.html` | 2026-08-11 | The fork drawn as slices of the limb, so no corner stands proud of Ø12 | [link](https://claude.ai/code/artifact/ea2c9509-829d-4466-8b08-a7d4737e7be2) |
| `shoulder-step.html` | 2026-08-11 | The rod-to-blade step narrowing to zero at four points, and the chamfer that gives it a minimum width | [link](https://claude.ai/code/artifact/1c3ec4fb-dd01-4fea-a6a1-d10eea868dca) |
| `hip-clearance.html` | 2026-08-25 | The hip reaching its full ±41.76° with nothing outside the socket in the way, and the collar's rim still 2.554 clear of the torso at that limit | [link](https://claude.ai/code/artifact/5d6520b6-637d-463b-9126-51ba493ae7fa) |
| `socket-wrap.html` | 2026-08-25 | That wrap does not retain the ball — a pure 2× encloses the same 72.5% and still drops it — and that holding the mouth at 96% of the ball retains it while wrapping less, 108.9° against 116.7° | [link](https://claude.ai/code/artifact/6c53133a-de9d-45ca-8dd4-577a54b5e09a) |
| `slit-reach.html` | 2026-08-25 | That the doubled `#slit_in` 5.0 still breaks 0.760 into the mouth, and that the ceiling on `#grip` is 3.459 against the settled 1.9465 | [link](https://claude.ai/code/artifact/20c8d685-0c04-4862-95b9-b7011516d66a) |

**The tab icon each page is published with**, so that republishing one does not turn it into a
different page in a gallery of them: 🦵 `hip-clearance`, 🔵 `socket-wrap`, ✂️ `slit-reach`,
📐 `collar-step-back`, 🔍 `socket-study`, 🔗 `hinge-stackup`. `figure-design-sketch` and
`shoulder-step` have not been republished since theirs were set, so theirs are not recorded here.

## The initial sketch, revision by revision

`src/stickbot/make_plans.py` draws the two plan sheets and writes them over the
previous ones. It draws the current design and only the current design: a generator that can also
draw three superseded revisions is three code paths that have to keep working.

**So freeze the sheets before running it.** Copy both SVGs here under the next revision number,
then regenerate. Miss that and the earlier plan survives only as a diff in the git log, which is
not something a student can be shown beside the new one.

| Revision | Sheets | Generated at | What it depicts |
| -------- | ------ | ------------ | --------------- |
| r1 | `plan-r1-assembly.svg`, `plan-r1-parts.svg` | `624712f` | Height set as a target and the stations fitted to it; arms hanging straight down in both elevations, no shoulder angle in the model at all |
| r2 | `plan-r2-assembly.svg`, `plan-r2-parts.svg` | `3104534` | The shoulder angled and posed, the hinge resized, the height stacked rather than aimed at — 152.65 to the top of the head. Described below |
| r3 | `plan-r3-assembly.svg`, `plan-r3-parts.svg` | `fc8c340` | The head on the standard 5.5 collar, which moved it up: top of head 69.15 and the figure 158.15 |
| r4 | `plan-r4-assembly.svg`, `plan-r4-parts.svg` | `efb314f` | The design at twice the size and the joint left alone, so the figure is 315.4 rather than a doubled 316.3 |
| r5 | `plan-r5-assembly.svg`, `plan-r5-parts.svg` | `6a81d3f` | The blade slit out of the hinge, settled by printing. The blade is solid in both hinge views and the ears carry the whole press fit |
| r6 | `plan-r6-assembly.svg`, `plan-r6-parts.svg` | `0a8a34e` | draft9p1's phase A. The joint dimensioned from the mouth at `#fit` 0.08, so the ball swings ±41.76° and the figure stands 317.05; the eye an ellipse with no pupil; every hinge protrusion on the blade and every recess in the fork; the foot's tread phased off zero and solid at both ends; the head drawn as the arch it is, as wide as the body |
| r7 | `plan-r7-assembly.svg`, `plan-r7-parts.svg` | `edcf145` | draft9p1p1's phase A. The socket measured from the ball's center, so a printing clearance no longer reaches the robot's height and the figure stands 317.00; the relief slit stopped 3.0 below the ball's center so it is a slot for its whole depth rather than a pocket for a third of it; the gripper's clip topped with a flat 18 × 18 platform and necked by a 45° chamfer; the feet centered on their own legs, meeting at x 0 |

Revisions before r1 were overwritten in place and exist only in the history of
`instructions/robot-guide/source/images/`.

r2 is drawn. It carries what run 3 and the geometry audit established: the shoulder stud 53° down
and 30° forward, the hip as a plain stalk after a recess was considered and dropped, and the
joint's own limit on how far it swings. The arms are posed rather than hanging — in one plane
parallel to the front, so the front elevation reads true length with the elbows bent, and the
gripper's bore stays square to that view.

Drawing it moved the shoulder twice. A boss that fat, leaving a vertical face at that angle, traces
an ellipse taller than the room above it — so the first attempt dropped the boss for a plain stalk,
and the second put the boss back and cut it off flush at the torso's top face. Cutting it costs
nothing, and it means the boss can be as fat as it needs to be without the shoulder growing a horn.

The boss is coaxial with the stalk, and that is the part worth remembering. A boss square to the
side face hangs below the ball, so the arm hits it on the way in — worse than no boss at all.
Everything a coaxial boss occupies sits behind the ball, and the socket only ever reaches forward
of it.

The stud also got longer, because the arm is a rod and not a line. With the ball standing the usual
5 mm clear, the Ø12 upper arm fouled the torso through the first 12° of its travel; the sheet said
the joint swings ±37° and the robot could not do it. The stud now runs 13 mm from the side face,
the whole arc is free, and the sheet says what the socket allows rather than what the joint has
left after the body takes its share.

The hinge changed too, and by the same kind of argument. The fork's ears were thin walls that did
not fill the limb; widening them to 4.2 filled it and made them 27 times stiffer, which turned out
to be the wrong 27 times. Ear and blade are springs in series: they carry the same force and split
the movement in inverse proportion to stiffness, so a stiff ear against a thin blade does not share
the work — it takes 0.01 mm of the 0.5 and lets the blade yield alone.

What matters is not thickness but section modulus over free length, because that is what decides
which one yields first. Equal thickness is not equal strength here: the ear is a segment tapering
to nothing at its edges while the tab is a full-width slab. Matched properly, the limb divides four
ways — ear 3.2, tab 2.1, tab 2.1, ear 3.2 — and the movement splits 0.2 and 0.3 at equal stress.

The blade is slit like the socket collar, which is the same trick a second time, and the load path
is what the sizing follows: a joint is only as strong as where the load crosses it, and that is the
tab, not the ear feeding it.

The figure is around 150 mm tall. Height is a consequence of the stations, the stand-off at each
ball and the angle each limb leaves at, so the exact number is whatever `make_plans.py` adds up.
It moved once already, when the hip stalk changed.

## Redrawing one

`hip-clearance.py` writes `hip-clearance.html` into the working directory from the joint's own
numbers. `socket-wrap.py` and `slit-reach.py` each write their page beside themselves from the
inputs of each sizing — ball, stalk, `#fit`, `#grip`, and for the slits a width and two radii —
with every other number and every path point derived. The rest were written by hand.

Republishing an edited file needs that sketch's own URL. Without it the page lands as a second
artifact beside the first, and the table above goes on pointing at the old drawing.
