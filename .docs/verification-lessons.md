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
- **Look at the render with a specific question.** Not "does this look like SpongeBob" but "count
  the hands; trace the legs from body to shoe". Open-ended looking confirms what you expect.

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

## Bearing on the course

Two of these are student-facing and belong in the step files:

- **A feature can be green when created and red on a later rebuild.** A student who adds the legs,
  moves on, and returns to a red feature will assume they broke it just now. Say so in advance.
- **Onshape does not always error when something goes wrong.** The smile that removes nothing is an
  `INFO`. Teach the habit of looking at the model, not just the feature tree — which is the same
  habit this section is about.
