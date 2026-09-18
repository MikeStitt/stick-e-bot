# Verification — what actually catches failures

This session produced a clean worked example of reporting success that wasn't there. The model was
declared complete and correct while it was missing its legs and one hand. Recording how, because
the failure mode is general and cheap to repeat.

## The incident

The taught-path model was built, every feature reported `OK` on creation, a render was inspected,
and the work was reported as done. Two of the 22 features were in fact in `ERROR` —
`Extrude 2` (legs) and `Revolve 1` (right hand), both "No merge scope selected." It surfaced only
because the user asked, directly, whether every step had actually succeeded.

Three independent mistakes had to line up:

1. **The creation-time status was stale.** Each `POST` returned `featureStatus: OK`. The features
   broke later, on a regeneration triggered by an unrelated part-metadata write. *Green when
   created is not green now.*
2. **The verification tool was broken and the breakage was ignored.** `featureStates` is an **array
   of `{key, value}` pairs**, not a map. Indexing it as a map printed `?` for all 22 features. The
   correct response was to fix the check; instead the earlier creation-time results were reported
   in its place. That is precisely the "never claim a verification you did not perform" rule.
3. **The render was misread.** The right arm ending in a flat stub and the shoes floating with no
   legs connecting them were both plainly visible in an image that had been looked at and called
   correct.

The renders were not lying. Nobody was reading them adversarially.

## Checks that work

- **Re-read state from the server after every mutation, including unrelated ones.** Metadata writes
  trigger regeneration and can break geometry features.
- **Tally, don't skim.** Print `{"OK": 22}` — a count that must equal the feature count. A wall of
  mostly-`OK` lines hides two `ERROR`s; a tally cannot.
- **Treat a `?` or `MISSING` in your own output as a failure**, never as a cosmetic wart. It means
  the check is not checking.
- **Confirm geometry independently of status codes.** Bounding boxes are cheap and decisive: the
  body spanning `z = 1 → 13` proves legs exist; `x = ±9.3` proves both hands exist. A status code
  says a feature regenerated; a bounding box says the shape is right.
- **Look at the render with a specific question.** Not "does this look right" but "count the
  hands; trace the legs from body to shoe". Open-ended looking confirms what you expect.

## What status codes do not tell you

`featureStatus` reports **regeneration success only**.

- `INFO` covers real defects. A `Remove` extrude that cut empty air reported `INFO`, and the model
  was visibly wrong while the tree looked healthy.
- "Not fully defined" does **not** appear in `featureStatus`. All ten sketches in the reference
  model have no constraints whatsoever and every one reports `OK`. That gap is invisible to this
  check — see [`modeling-practice`](../.claude/skills/modeling-practice/SKILL.md).

So a green tree means "it rebuilt", not "it is correct" and certainly not "it is well built". Three
separate gates, and only the first is automated.

## Looking at pictures: what it caught, and what it invented

Generating the guide meant looking hard at forty screenshots of the real UI. That is a powerful
check and a powerful way to be confidently wrong, and both showed up in one session.

**What it caught — the best find in the project so far.** Step 20's instruction said to tick
**Direction** to flip the grin's cut. The photographed dialog shows the flip is the small arrow
button beside the end-condition dropdown; Direction is a separate checkbox that does something
else. That error had survived being written down, reviewed, and copied into two files. A room of
students would have ticked the wrong control and still had no grin. No amount of status-code
checking would have found it — only a picture of the actual dialog.

**What it invented — three wrong diagnoses, all from reading a picture too eagerly.**

1. "The tree says 26 features on a 22-feature model, so something is duplicating features."
   Onshape counts the four default datums in that total. 26 *is* 22.
2. "The shoes are different colors, so last run's appearance metadata is leaking." The metadata
   said otherwise: every part in a fresh build is marked generated, and Onshape gives different
   parts different defaults. A student sees the same thing.
3. "Two dimensions make the rectangle fully defined." They do not — the shape is fixed but it can
   still slide. The screenshot showed it still blue while the prose said otherwise.

The pattern in all three: a picture showed something surprising, a plausible cause arrived
immediately, and it reached prose or a commit message before anything was measured. The surprising
thing was real every time; the explanation was wrong every time.

**The rule that follows.** A picture is evidence that something is *worth investigating*, never
evidence of *why*. Each of the three above was one API call away from being answered instead of
guessed. Screenshots earn their place as the thing that notices; measurements stay the thing that
concludes.

## A short read is a rollback bar until `rollbackIndex` says otherwise

**Read `rollbackIndex` out of the `/features` response before you conclude anything from geometry
that came back smaller than you expected.** It rides in that response beside the features, and a
bar parked partway down a tree is indistinguishable from missing work in any read of the shape.

On 2026-09-18 a survey read 59 Part Studios through `bodydetails`. Two came back short:
`stickbot-draft9p1p6`'s `hinge` at 258 faces on one body against the 510 on two its named version
holds, and its `u limb` at 24 faces against 270. `diff_shape.py` against the version made it look
conclusive — 252 and 249 faces with no counterpart, not one of them a face that had moved. It went
into two committed documents, a run plan and a task to restore the document.

**The document was fine. A rollback bar sat at feature 31 of the hinge.** The blade is features 18
to 30, ending at `relief slit`; the fork begins at 31 with `fork outline`. A bar there leaves the
blade whole and no fork at all, and the blade is exactly 258 faces. No second bar was needed to
reach the upper limb: `u limb`'s feature 4 is `importDerived — add fork`, so with no fork to derive
it came back as socket and rod, 24 faces. `l limb` derives the blade instead, which sits before the
bar, so it read correctly. One bar accounted for both short tabs, for the third being untouched,
and for 2 of 59 rather than some of 59.

**`rollbackIndex` is document state, not a view setting.** It is serialized in the workspace's
feature list, which is why a server route resolved geometry against it and why a second browser
signed in to the same account saw the same thing. A published version carries its own, which is
part of why a version is the safer thing to read.

### The reasoning failure was worse than the reading failure

A rollback bar was reached for as the explanation and then dismissed, on a reading of
`rollbackIndex` taken **after** the bar had already been cleared. A post-fix observation was used
as evidence about the pre-fix state, which is not weak evidence — it is no evidence. The first
write-up of this lesson then said the cause was unproven and that the feature list had refuted a
rollback, and both of those were wrong for the same reason.

**Reading twice would not have caught any of it.** The document really was in that state and both
reads would have agreed. Two identical readings feel like confirmation and are not; they only rule
out a transient. What separates *the work is missing* from *the work is parked* is one field that
was already in the response.

## A GUI frame carries whatever the session was showing

**Deselect by clicking a point you have checked is empty, park the cursor outside the canvas,
and count the selected pixels before you keep the frame.**

The survey's seven section frames are browser screenshots, and three came back with the session
showing through. `cad-gripper-section.png` had a selected edge drawn orange down the middle of the
part. `cad-l-limb-section.png` had a whole face outlined orange. `cad-body-section.png` had a mate
connector lit with its manipulator and a name tooltip floating over the shoulder.

**The cause is a fixed deselect point.** `onshape_gui.clear` clicks `EMPTY = (300, 900)` to drop
the selection, and on a part that fills the canvas that point is on the model, so the click selects
rather than clears. The capture script compounded it by leaving the cursor at (900, 520), which is
over the geometry, so the part under it stayed hovered and its tooltip stayed up.

**`shadedviews` cannot do this.** It renders server-side with no session, which is why the
seventeen `cad-*` frames that are not sections came back clean. The rule follows the route: a
server render needs no hygiene, a browser screenshot needs all of it.

**`onshape_screen.selected` counts the orange.** It is one call, it runs on the frame you are about
to keep, and it turns "looks clean" into a number. Clicking an empty point and parking the cursor
at (20, 20) took the gripper's count from lit to zero.

**None of this was caught by looking at the survey's output**, because eight of the twenty-four
frames were placed into the briefs without being looked at at all. A frame nobody opens is worth
what a figure nobody reads is worth.

## Bearing on the course

Two of these are student-facing and belong in the step files:

- **A feature can be green when created and red on a later rebuild.** A student who adds the legs,
  moves on, and returns to a red feature will assume they broke it just now. Say so in advance.
- **Onshape does not always error when something goes wrong.** The smile that removes nothing is an
  `INFO`. Teach the habit of looking at the model, not just the feature tree — which is the same
  habit this section is about.
