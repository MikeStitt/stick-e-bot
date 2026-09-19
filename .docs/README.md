# .docs — working notes

Notes from building the course material and the reference model. These are **working notes, not the
contract** — the contract is [`.claude/rules/constitution.md`](../.claude/rules/constitution.md). If
a note here ever conflicts with the Constitution, the Constitution wins and the note is stale.

Each file marks what was **verified** (performed and observed) versus **unverified** (believed but
not checked), because the difference is the whole point of the Quality Gates.

**This page is not the task list.** [`open-work.md`](open-work.md) is, and the Constitution's
Working Rule *Name a unit of work; do not number it* says so. What is left here is notes: what was
found, what was decided, and what is not worth re-litigating. Not every file in this folder is
named here — the ones below are the ones the current work points at.

## What needs doing, and what needs improving

State of play for the robot, at the end of run 2 (2026-08-11): Session 1 is
`instructions/robot-guide/source/index.rst`, a Sphinx page covering the body and the face. Part
one has been built twice, Part two once, and each was corrected after the run that tested it —
so **no part has been rebuilt from the text as it now stands**, and a run 3 would be its first
test. The run 2 model measures right — eyes r5, mouth 20.000 overall, neck Ø12 — at version
`run2-session1-complete`; the ball-and-socket and hinge joints are built at named versions too,
with ids in [run 2's folder](experiments/runs/2026-08-11-run2/README.md).

**Run 3 was launched, mis-briefed and thrown out** (2026-08-12). Its three agents read a brief
README claiming an open conflict over limb sections that did not exist; `#limbD` had been
settled at 12 the previous day. They were stopped, and the documents `ball-socket-run3` and
`lesson-run3` are deleted. The briefs have since been rewritten —
[`experiments/build-briefs/limbs.md`](experiments/build-briefs/limbs.md) replaces the four
invented limb briefs, and every numbers table carries a Source column. What the launcher does
before the next attempt is [`2026-08-12-launch-gate.md`](2026-08-12-launch-gate.md);
[`experiments/run3-launch.md`](experiments/run3-launch.md) holds the old prompts and is stale
against both.

## Measure `#collar` from the ball's center, so `#grip` stops moving parts

**Done on 2026-08-27 as
[draft9p1p1's A2](experiments/runs/2026-08-26-draft9p1p1/plan.md), in the design source.**
Recorded here because [A2](experiments/runs/2026-08-25-draft9p1/a2-fit.md) got half of what it was
after and the other half was still available. `#collar` is now `#ball / 2 + #wall` = **9.0**, which
is the collar's own radius: the socket goes as deep below the ball's center as it is wide from the
axis. The model still has to be edited — that is Phase B. What follows is why.

`collar blank` extrudes `#grip` one way and `#collar - #grip` the other, so the socket is `#collar`
tall from a mouth at `#grip` down to a root at `#grip - #collar`. **A2 asks that a printing
clearance not ripple into any other robot dimension, and both of those ends move when `#grip`
moves.** [C2](experiments/runs/2026-08-25-draft9p1/c/c2-driving.md) drove `#fit` from 0.08 to 1 and
measured it: the socket stayed 11.000 tall at every value, and the tops of `Foot`, `Gripper` and
`u limb` each rose 2.0312 with `#grip`.

**So `#collar` is now the distance from the ball's center to the bottom of the socket**, and it
goes in `collar blank`'s second position on its own rather than as `#collar - #grip`. The root is
fixed, only the mouth moves, and the parts the socket is added to keep their dimensions when the
fit changes.

What it follows through to:

- The socket's overall height becomes `#collar + #grip` = 10.9465 rather than a constant, so the
  trade is named rather than hidden: before, the tabs kept a constant free length and the parts
  moved; now the parts keep their dimensions and the tabs' free length varies with the fit.
- `#collar - #grip` appears three times in the model and always means *the ball's center to the
  root*, so all three become plain `#collar`: `collar blank`'s second direction, the foot's
  `#collar_down`, and — inside a longer expression — `u limb`'s rod, which is
  `#limbCenter - #collar + #grip - #limbD / 2` and loses its `#grip` term.
- **No consumer sketches on a socket face**, checked over the API on 2026-08-27: `head`, `foot`,
  `u limb` and `gripper` each take the socket by `importDerived` and place it with a mate connector
  or a transform. So re-basing moves expressions and nothing else, and there is no rebuild order to
  get right.
- The slit floor does **not** follow from this on its own, and an earlier version of this section
  said it did. A2 fixes the root; the floor hung off the mouth at `#grip` and would have kept
  moving. It took [A1](experiments/runs/2026-08-26-draft9p1p1/plan.md) dimensioning the floor at
  `#ball / 4` below the ball's center to fix it, and that also
  [made the cut a slot for its whole depth](experiments/build-briefs/ball-and-socket.md).

**The test it has to pass is the robot's height**: `#fit` and `#grip` change no dimension of the
robot once the socket's root stops moving. In the design source it now passes — the figure comes
out 317.000 rather than 317.0535, and it stays there at any fit. Phase C measures the same thing at
the model.

## Carry the useful half of the old Session 1 into the new one

`experiments/session-1-layout-and-torso/` (**A**) was superseded on 2026-08-10 by the commit
that wrote `instructions/robot-guide/source/index.rst` (**B**) — *"Rewrite session 1 to start
from a design plan, and build it as a Sphinx page"*. B has had two test runs since; A has not
been touched since it was written. Before A is retired, four things in it have no counterpart in B.

**Its whole teaching half.** B has no `lesson-design.md` at all — no clock, floor, ceiling or
rubric. Worth carrying across specifically:

- **"Draw it badly on purpose."** The instructor draws visibly crooked, then the room watches
  geometry move as constraints land. B has no instructor guidance of any kind, and this transfers
  straight to B's torso rectangle.
- **The three across-the-room assessment questions**, especially the third — *can the student say
  what would happen if one driving line moved?* B's "Change one number" section already performs
  that demonstration with no assessment framing around it.
- **The ceiling items** — Equal instead of separate dimensions, deliberate over-constraint to find
  the redundant one, driving dimensions from a variable.

**Construction geometry, which B assumes and never teaches.** A teaches it — `q` to toggle, `v`
Vertical, `h` Horizontal. B uses none of them, but `index.rst:309` says *"this is the argument for
the rule about construction geometry: do not draw a construction line where a real edge already
is."* Either teach the rule in B or drop the sentence that depends on it.

**Two warnings B lacks.** `shift+s` is **Point**, not Sketch — A warns, B just says to use the
toolbar. And "the block only grew one way — Symmetric was not ticked", which is in A's failure
table and missing from B's fourteen-entry one.

**The drag test as a habit.** A makes it a ritual: every sketch, every time. B drags a corner at
Step 2 and mentions blue endpoints, but never establishes it.

**Do not carry A's "Tab, not Enter" note.** B's second test run found dimensions need **Enter** —
Escape silently discards the typed value, which produced a 34.8 mm torso instead of 48. Tab applies
only inside feature dialogs. A's version is wrong.

## Coverage and correctness

- **Steps 3 onwards are photographed by opening features for editing**, not by creating them. Same
  dialog, same real values, but never a half-finished selection. This is the main thing to revisit
  if the middle sessions feel thin. Steps 1 and 2 are driven click by click.
- **[`tasks.md`](tasks.md) is the dictionary for the numbers, not a task list.** They were coined
  in a Claude Code task store keyed by session id, which is not in git and does not survive the
  session that made it; the repository cites them 107 times across 42 files, so the definitions
  live in that file. It was closed at #217 on 2026-09-16, reopened on 2026-09-18 for #218 through
  #226, and closed again on 2026-09-19 when the Constitution gained a home for work no plan is
  doing. The four of those still open moved to [`open-work.md`](open-work.md) under the names they
  carried. The 2026-09-16 close and the reasoning behind it are in
  [`2026-09-16-tasks-into-the-repo.md`](2026-09-16-tasks-into-the-repo.md); the 2026-09-19
  amendment is `8.1.0` in the `constitution-maintenance` changelog.
- **Session 1's two documents are reconciled.** `instructions/robot-guide/` supersedes
  `experiments/session-1-layout-and-torso/` — what to salvage from the older one is above, under
  *Carry the useful half of the old Session 1 into the new one*.

## Pipeline improvements worth making

- **Onshape rate-limits hard.** A burst of feature writes earns a 429 on that endpoint family that
  took over an hour to clear on one occasion, blocking all capture work. Writes are paced now, but
  do not plan a working session around many rebuilds.
- **Handling a 429 is written, and the history says why it took eight tries.** Done on 2026-08-28.
  The rule is [`onshape`](../.claude/skills/onshape/SKILL.md) § *Read what a refusal says before
  waiting on it*; the mechanism is `api()` in
  [`../src/stickbot/onshape_session.py`](../src/stickbot/onshape_session.py), which now keeps the
  response headers, honors a short `retry-after`, and raises at once rather than spending a ladder
  to discover the answer is hours away.

  **Verified against a live 429 on 2026-08-28.** `features` answered `retry-after: 522` with
  `x-rate-limit-remaining: 0`, and `api()` raised in 0.10 s naming both, where the old ladder
  would have spent 110 s and five requests to reach a message that was wrong on two counts. In
  the same pass `bodydetails`, `parts` and `assemblies` answered 200 with 486, 500 and 1000 calls
  left, which is the per-family limit measured from the healthy side. The sweep of what came
  before:

  - **08-10, `5263ee7`, the client's `api()`.** Assumed one kind of 429, minutes long, and
    laddered 5 s to 480 s, 955 s in all. It was the first handling of any kind: before it a 429
    read as a `DELETE` that quietly did nothing and a feature list with no `features` key.
  - **08-10, `b5d2aec`, the same function.** Cut the ladder to 5, 15, 30, 60 because *"an
    unbounded backoff turns a rate limit into something indistinguishable from a freeze"*. The
    reasoning holds. The message did not: it hard-coded *"account-wide on the feature endpoints
    and clears in minutes"*, and that sentence is what every later reader believed.
  - **08-10, `be1b460`, `wait_and_capture.py`.** Polled every 60 s and gave up after an hour. A
    runner that waits, for a limit whose answer is a different route.
  - **08-10, `08a50d2`, the same runner.** Polled every 300 s and gave up after six hours, on the
    theory that the polling itself was holding the block open. Six hours does not outlast
    eighteen. Retired on 08-12 with the pipeline that used it.
  - **08-13, `60377ea`, `design-into-cad.md`.** Right, and complete: a daily quota, `retry-after`
    in the tens of thousands of seconds, counting down with the clock, one endpoint throttled
    while the rest answer, so move to the GUI. Prose only. It landed in `.docs/experiments/`,
    which the Constitution files as archive, and no code and no part changed.
  - **08-14, `013b57f`, `onshape-gui-howto.md`.** Took 83 s from the one end-to-end pair in run
    3's torso log and made it the recovery time. One measurement of the short mode, generalized.
  - **08-14, `905fff0`, the same file, hours later.** Corrected itself: two kinds, waiting inside
    a session worked neither time, plan a route that avoids `/features`. Still prose only.
  - **08-24, `15441c6`, tutorial 11's build log.** Backed off every time and it did not clear, so
    `featureStatus` was never read; the acceptance check fell back to looking for error badges in
    the tree frame.
  - **08-27, draft9p1p1 Phase C.** Measured all of it from scratch again, and re-planned a phase
    around never touching `features`.

  **The cause is not that nobody knew.** It was right in the tree on 08-13, fourteen days before it
  was measured again, and re-derived on 08-14. What failed each time is that the finding landed in a
  working note while the client went on asserting the opposite in the message it raised, and the
  client is what the next person read. A finding about a tool has to reach the tool.

## Future work — print orientation, and the edge treatments that depend on it

**Not adopted. Recorded because it blocked a decision we tried to take on 2026-08-11.**

We went looking for a standard fillet size for a 0.4 mm nozzle and found the question is not
answerable on its own. Every useful source qualifies its advice by which way the feature faces
on the plate:

- **Vertical corners are already filleted at about 0.2 mm** — half the nozzle diameter — whether
  drawn or not. Protolabs Network: *"Because FDM printing nozzles are circular, corners and
  edges have a radius equal to the nozzle size."* So nothing below ~0.4 mm is worth drawing.
- **Downward-facing fillets print badly** and want to be chamfers instead. Hydra Research: *"do
  not use downward facing fillets… they may come out with poor aesthetic/surface quality."*
- **Edges on the build plate want a 45° chamfer**, sized 0.3–1.0 mm depending on layer height.

Candidate numbers, if we ever adopt them: **0.5 mm × 45° for a cosmetic edge break, R1.0 as the
minimum drawn fillet, and nothing under 0.4 mm drawn at all.**

**Why it is not adopted:** "upward" and "downward" are properties of the print, not of the
model. Until each part carries a **declared print orientation**, an edge rule cannot be applied
— the same fillet is fine on one face and ugly on the opposite one.

**The bigger instance of the same problem is structural, not cosmetic.** A snap-fit tab flexed
about an axis parallel to the layer lines peels them apart and fails well below the calculated
strain; flexed within a layer it does not. That applies directly to the ball socket's four tabs
and to the hinge's sprung ears, and neither brief says which way up the part is printed. The
hinge report's 2.2 % ear strain and the socket's tab calculations both quietly assume the
favorable orientation.

**What adopting it would take:** a declared orientation per part, shown on the parts drawing;
edge treatments chosen per edge against that orientation; and the tab-bearing parts oriented so
their tabs flex in-layer.

Sources: [Protolabs Network](https://www.hubs.com/knowledge-base/how-design-parts-fdm-3d-printing/),
[Hydra Research](https://www.hydraresearch3d.com/design-rules),
[NExT Lab](https://ms-kb.msd.unimelb.edu.au/next-lab/3d-printing/design-guidelines),
[3DVerkstan](https://support.3dverkstan.se/article/38-designing-for-3d-printing).

## Decisions taken, worth not re-litigating

- **Highlights come from the DOM.** No pixel coordinates anywhere. This is what keeps the
  annotations correct across window sizes and Onshape's redesigns, and it was the single most
  useful decision in the project.
- **Every shot verifies itself.** A click that should select something is checked against Onshape's
  own measurement readout; a highlight target that is not on screen raises rather than quietly
  vanishing.
- **The builder only ever goes forwards.** Rebuilding the figure per step would be ~500 feature
  writes and a guaranteed rate limit; building forwards is 22.
- **Screenshots notice, measurements conclude.** See
  [`verification-lessons.md`](verification-lessons.md) — three wrong diagnoses in one session came
  from treating a surprising picture as evidence of its own cause.
