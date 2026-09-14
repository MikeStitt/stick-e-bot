# Session 1 — lesson design

The instructor's half of the session. Paired with
[`source/index.rst`](source/index.rst), which is what the students follow.

Read with the [`lesson-design`](../../.claude/skills/lesson-design/SKILL.md) skill.

## What this session is for

One idea, taught three times: **geometry gets its position from constraints, not from careful
clicking.** The torso rectangle says it, the neck and head say it again out of the same sketch,
and *Change one number* proves it — the 48 moves and everything above it follows.

The second idea is nearly as big: **a sketch is a pool of shapes, not one part's outline.**
Three features come out of Sketch 1 and nothing is drawn twice.

Everything else — units, the rename, the measuring — is scaffolding for those two.

## The clock, and why it does not fit yet

**The *Fits the clock* gate is unmet. Do not schedule this session as written.**

What has been measured is one agent walking the whole page in a headless browser:

| Block | Elapsed, agent pace |
| ----- | ------------------- |
| Setup, units, and all of Part one to the three area checks | 33 min |
| *Change one number* | 2 min |
| **Part two** | **57 min** |
| — eyes and pupils | 15 min |
| — the mouth | 13 min |
| — chest panel, hole, and pattern | 18 min |
| — lettering | 10 min |
| **Total wall clock** | **92 min** |

Logged action by action in
[`.docs/experiments/build-log/lesson-test/steps.log`](../../.docs/experiments/build-log/lesson-test/steps.log),
and reported in
[test report 2](../../.docs/experiments/reports/robot-guide-test-report-2.md).

**That is not student pace and must not be read as one.** An agent types instantly and never
hesitates, and it also spends a screenshot finding every toolbar button. The two errors do not
cancel out in any known ratio. **Nobody has walked this at student pace, so no timetable here
is a measurement**, and the Constitution's 90-minute rule cannot be certified until someone
clocks it.

What the numbers do say reliably is where the cost sits: **Part two took nearly twice Part
one**, and inside Part two the time went where the text was incomplete rather than where the
modeling was hard. The eye section is the most constraint-heavy thing on the page and was the
fastest, because it was written accurately. Seven of the panel's eighteen minutes were the
Linear pattern alone.

**So the cut line runs after the eyes.** Part one plus eyes and pupils is the floor; mouth,
chest panel and lettering are the ceiling. If the room is ahead, they come back on.

## Floor and ceiling

**Floor** — every student leaves with one solid part called **Robot**: torso 36 × 48 × 24
centered on the origin, a Ø12 neck, a 36 × 36 × 30 head, and two eyes with proud pupils. Every
sketch black, endpoints included. A published, named version at that state is the recovery
point Session 2 starts from.

**Ceiling** — in this order, because each is self-contained:

1. The slot mouth.
2. The chest panel, its hole, and the linear pattern.
3. The lettering.
4. Make the two eye circles **Equal** rather than dimensioning each, then change one and watch
   both move.
5. Deliberately over-constrain a rectangle — width, height *and* diagonal — and find the
   redundant one by clicking the constraint symbols.

**Session 2 must be written to start from the floor**, which means from a body with eyes and
nothing else on the face. Ceiling work is never a prerequisite (Working Rule 12). That is a
constraint on Session 2, not a fact about it — Session 2 does not exist yet.

## The two demonstrations that matter

**Draw it badly on purpose.** When you demo the torso rectangle, place it visibly off the
origin and visibly crooked. Then watch it jump when the origin catches the center point, and
jump again as each dimension is typed. A room that has seen geometry *move* when a constraint
lands does not go on to believe constraints are labels.

**Drag it before accepting.** Every sketch, every time. It costs a second when the sketch is
finished and saves ten minutes when it is not. It is also the only honest test: Onshape reports
"fully defined" by turning the sketch black and nowhere else, and a line can be black while its
endpoints are still blue and still sliding.

## What will go wrong

The student page already carries the failures and their fixes, under *If something else
happened*, plus *What will bite you* up front. Those are the ones to point at.
These three are instructor-side and are not on that page:

| Symptom | Cause | What to say |
| ------- | ----- | ----------- |
| The block only grew one way | **Symmetric** not ticked on the extrude | Double-click the feature and tick it |
| A dimension went back to its old value | The typed value was closed with Escape, which discards it | Type, then **Enter**. Escape means cancel |
| The room is at a different zoom to you | Onshape zooms toward the pointer | Say what should be *big on screen*, not how far to scroll |

The dimension one is the expensive failure: in the second test run it silently produced a
34.8 mm torso instead of 48, and nothing on screen said so until the area check.

## Assessment

Not a mark out of ten. Three yes-or-no questions a mentor can check from across the room:

1. Is there **one** part, and is it the right size? Click the torso's side face with nothing
   else selected — the area readout should say **1152.0 mm²**.
2. Is every sketch black, endpoints included?
3. Can the student say what would happen to the head if the **48** changed?

The third is the one that matters. *Change one number* performs that demonstration; this asks
whether the student can predict it before it runs. A student who can has understood the
session. One who cannot has drawn some rectangles.

## Known gaps in this plan

- **Nobody has taught it.** Every number above is either an agent-pace measurement, labeled as
  one, or absent. There is no student-pace timing in this file and there must not be one until
  someone clocks it.
- **No part has been rebuilt from the text as it now stands.** Part one has been built twice
  and Part two once, each corrected after the run that tested it, so a third run would be the
  first test of the current wording.
- **Construction geometry is never taught, and the page refers to a rule about it.** Line 309
  of `source/index.rst` says *"this is the argument for the rule about construction geometry"*.
  Either teach the rule or drop the sentence that leans on it.
- **The variable ceiling is not offered here on purpose.** Onshape's variable feature has not
  been located in this course's GUI walkthrough, and the Constitution forbids promising a menu
  path nobody has opened.
