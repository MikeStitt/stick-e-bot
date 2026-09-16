# Figures that cannot go stale, and figures that are not supposed to

A drawing that explains why a dimension is right has two ways to rot: the picture stops matching
the design, or the picture is redrawn and the sentence above it goes on claiming something the new
picture disproves. The second is worse, because a correct drawing under a false heading looks
checked. This note says which drawings should be generated, which should be frozen, and what makes
the difference cheap rather than a standing maintenance cost.

## The pattern already exists, for one subsystem

[`reviews/hinge/`](reviews/hinge/) is the thing. `make_figures.py` imports `make_plans` and
`hinge_spring` and emits **eleven SVG figures and five `.rst` tables** — `axle`, `doubling`,
`rooted`, `settled`, `slit` — straight into the Sphinx source, and `ninja hinge-figures`
regenerates the lot. Not one number in that document is typed.

The three studies in [`experiments/sketches/`](experiments/sketches/) are the same kind of drawing
built the other way: `hip-clearance.py`, `socket-wrap.py` and `slit-reach.py` import nothing but
`math` and `pathlib`, and type their inputs at the top. So the repository already holds both
answers to the same question, and the hinge's is the one that works.

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

All three studies currently caption themselves *as built in `stickbot-for-bot-review`*, a document
that appears in no run record, and mix sizings. That is the symptom of never having drawn this
line.

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

- The three studies import `make_plans` instead of typing their inputs. This waits on
  [the packaging plan](2026-09-16-python-packaging.md), which makes `make_plans` importable.
- Each one returns non-zero when its own verdict fails, and joins `ninja check`.
- The ones that argue for a past decision are separated from the ones that describe the design
  now, dated, and frozen.
- `stickbot-for-bot-review` is identified, or the caption goes.
