# Run 5 — build notes

Run 5 is a repair run, not a build run: it takes run 4's six parts, fixes what the audit found,
re-assembles the robot from named versions, and evaluates it. The plan it followed is
[`../../design-into-cad.md`](../../design-into-cad.md).

This file is the front door. The measurements are in [`evaluation.md`](evaluation.md), the repairs
and what each one exposed are in [`repairs.md`](repairs.md), and what is still open is in
[`register.md`](register.md). Nothing is repeated here.

## Where the work is

Nine documents, all copies made for this run, listed with their element ids in
[`run5-documents.json`](run5-documents.json). The seven that matter:

| Document | Document id | Part Studio | Version | Version id |
| -------- | ----------- | ----------- | ------- | ---------- |
| `torso-run5` | `206f64ca84078adfa732cafa` | `e60771705729bcb7e1f5a72f` | `run 5` | `cdb81ee18dd39a39459084eb` |
| `head-run5` | `92cbe5356b68e79b1fa2de82` | `374227cc36f4d555dbc4cfca` | `run 5` | `0f8c98cf8711856e8920395d` |
| `hand-run5` | `e0ad3f5011419cdd89355a83` | `6e1dd11ab78aaf20a7b04a25` | `run 5` | `cb6595886adb02dbf13d0b1d` |
| `foot-run5` | `f1e10c9011cc7e097e626b0e` | `13f9b306ab6bc18ccc9b2c5d` | `run 5.1` | `2eb1c5a2408e27fca4436e24` |
| `limb-socket-clevis-run5` | `ea99eeb6f9aa9e24a0139ddb` | `d2f73f3c4c16fabaf01927bb` | `run 5` | `940001b89dceed0f4c8fb73a` |
| `limb-blade-ball-run5` | `a430364619418afe61e7ff6f` | `3b0afd71762a41aba6fcc8ec` | `run 5` | `17256fe4d71d13c0d2d1bce7` |
| `lesson-run5` | `a999c3039f292ccb278ac94a` | Assembly `f09a5c881ece9a882e0f6b39` | `run 5 assembled` | `8ccbeb5e531a4633db7a4588` |

The foot has two versions. `run 5` was cut after S4 and is the foot pointing the wrong way;
`run 5.1` is the one the assembly uses. The other five parts have one each.

The assembled robot, live workspace: `https://cad.onshape.com/documents/a999c3039f292ccb278ac94a/w/1110d41029a137a8e1b6cb79/e/f09a5c881ece9a882e0f6b39`

The same assembly at its named version: `https://cad.onshape.com/documents/a999c3039f292ccb278ac94a/v/8ccbeb5e531a4633db7a4588/e/f09a5c881ece9a882e0f6b39`

**The workspace link was opened, repeatedly — that is where all the GUI work happened. The version
link was assembled from ids and never opened.** The version id came back in the `POST
.../versions` response, not from clicking anything.

## The click path that worked

Run 5 started against the API and switched to the GUI partway through, when
`GET/POST .../partstudios/.../features` and `POST .../featurescript` all began returning 429. The
part-studio edits from S4b on, and both of the assembly's shoulder connectors, were done by
driving the browser on port 9223.

### Getting a coordinate out of the GUI

Selecting a mate connector in the assembly tree puts its origin in the status bar at the bottom
right as `Point: X … Y … Z …`. That is how the torso's `Shoulder R` was measured at (23, 0, 24)
and shown to be nowhere near the ball. There is no dialog for it; the readout is the only place
the number appears.

### Reading a feature's error

The tree marks a failed feature with a red icon and `ns-list-item-error` on the row. **The message
is only in the tooltip** — hover the icon and the text appears as `<name> has error: <message>`.
The API's `featureStates` gives the status and no message at all, so a failing assembly feature
cannot be diagnosed from the API alone.

### Placing a mate connector on a ball

1. Right-click the instance in the tree that is in the way → **Hide**. The shoulder balls sit
   inside the arms' sockets and cannot be picked otherwise.
2. Toolbar → the mate connector button, which is `#svg-icon-mate-connector-button`. Every mate
   type has its own button; `Ball` is `#svg-icon-ball`.
3. Click the spherical face. The dialog's `Origin entity` fills with `Face of Torso <1>` and the
   connector lands on the sphere's centre, not on the face.
4. Green check to accept.
5. Right-click the hidden instance → **Show**.

### Picking mate connectors for a mate

Start the mate, then click the connectors **in the tree**, not in the viewport — expand the
instance and its mate connectors are listed by name under it. The dialog shows them as
`Socket of Upper arm / thigh <3>` and `Mate connector 1 of Torso <1>`, which is unambiguous in a
way a viewport click is not.

### What the GUI cost

Two mis-clicks did real damage and both were recoverable:

- A click meant for a context menu landed on the **Part Studio 1** tab and switched documents
  mid-mate, leaving a half-built `Ball 2` in `ERROR`. Deleted and rebuilt.
- A drag meant to pose an arm landed on empty space and **translated the whole assembly** 37.292
  in x and 12.012 in z, with every mate still green. `Meta+Z` put it back and `Fix` on the torso
  stops it recurring.

Both came from computing a screen position from an earlier screenshot. The tree reflows whenever
anything is expanded, hidden or added, so **every click position has to be re-read from the DOM in
the same script that uses it.**

## Every acceptance measurement

In [`evaluation.md`](evaluation.md), per part, against each brief's own *Acceptance checks*
section. The short version: every station matches `make_plans.py` to the thousandth, and the
checks that were not performed are named in [`register.md`](register.md) under **Never attempted**
rather than left out.

## What did not work

The per-step failures are in [`repairs.md`](repairs.md), each next to the measurement that caught
it. Three are worth naming here because they are about the process rather than a part:

- **The API's 200 means "accepted", not "worked".** Eleven mates and one extrude all returned 200
  and all were wrong. In every case the thing that caught it was a volume or a bounding box, not a
  status.
- **`featureStatus: OK` and a green tree are not evidence either.** A slit that cut half its
  length into empty air, and an assembly translated 37 mm off the origin, both left every feature
  `OK`.
- **The rate limit arrived mid-run and changed the method.** `featurescript` was the plan's
  measuring instrument through S3 and was gone by S4. `bodydetails` replaced it and is better for
  most of what the briefs ask, which nobody knew before it had to be found under pressure.

## What the brief never said

- **Which sign of Y is forward.** Three briefs each decided it independently and one disagreed.
  Now stated in [`../../build-briefs/README.md`](../../build-briefs/README.md).
- **Which document owns the stations.** The briefs' README carried its own table and it was five
  millimetres out from the hip down. It now points at `make_plans.py`.
- **What to do when a socket cannot take relief slits.** `ball-and-socket.md` requires them;
  `head.md` says this socket has no free tab length to slit. Neither says which wins.
- **Whether the figure has a pose.** Every joint but the knees and elbows is a ball, so the
  assembled robot has no defined arm position and no arm span to check.

## Screenshots

Renders of the six parts before repair are `shots/r5-<part>-<view>.png`, from the phase 3 audit.
Renders after repair are `shots/s8-<part>-<view>.png`, and the assembly is
`shots/s7-assembly-front.png` and `shots/s7-assembly-right.png`.

**There is no step-by-step screenshot series and no `steps.log` for this run.** The GUI work was
screenshotted heavily, but into a scratch directory, one frame overwriting the next, and only the
frames that ended up as evidence were kept. That is a departure from what
[`../../build-briefs/README.md`](../../build-briefs/README.md) asks for and it is a real loss: the
click paths above were reconstructed from the working scripts, not from a record made at the time.

## Retrospective

**What went well.** Measuring the thing rather than the feature that made it caught every defect
in this run, without exception, and often caught it in a number nobody would have thought to look
at — 3.457 mm³ against an expected 11.512 is what found a slit extruding into empty air, and
24.322 against 24.000 is what found two sketch lines that were never tangent. The plan's rule that
a finding never ends a step was worth having; four of the run's best findings came out of failures
in the middle of steps that then finished anyway. And losing `featurescript` turned out to be the
most productive thing that happened, because `bodydetails` answers more of the briefs' questions
and does it on solved geometry.

**What went poorly.** I trusted colour, status and dialogs far too long. A blue sketch line that
resisted a drag got written down as "blue but rigid", which is not a thing; a mate dialog that
named both connectors got read as a working reference while the mate sat in `ERROR`. Both cost a
step. I also lost the screenshot record, which is the deliverable the briefs are most explicit
about, and I did not notice until writing this. And I spent a long stretch computing click
positions from stale screenshots — the two worst mis-clicks of the run both came from that, and
the fix was obvious in hindsight.

**What I would change.** Three things, in order of how much they would have saved:

1. **Put the "how do I read an error" step in the how-to before the "how do I build" step.**
   Hovering a tree icon for a tooltip is the only way to see why an assembly feature failed, and I
   found it after posting eleven broken mates rather than after posting one.
2. **Make the briefs' README the only place a shared convention lives, and say so.** Two of this
   run's orientation faults were the same fault: a convention that no single brief owned, decided
   independently by each brief, invisible until the parts met. The sign of Y and the station table
   were both this.
3. **Put every click through one wrapper, and let the wrapper keep the record.** The briefs
   already ask for a `steps.log` — a line before each action and a line after — and run 5 wrote
   none, because writing it was something I had to remember between one problem and the next.
   A single `click(pg, x, y, what)` that logs before, clicks, screenshots and logs after would
   have kept it whether or not anyone remembered. **The screenshot has to be numbered, not
   named**: `gui.py`'s `shot(pg, name)` writes `gui-<name>.png`, I reused names, and each frame
   overwrote the last — that, and not forgetfulness, is why there is no series left to show.
   This is not a two-line change: run 5's clicks were bare `pg.mouse.click(x, y)` calls inline in
   throwaway scripts, so there was no choke point to add logging to. Building the wrapper is the
   change; the logging is free once it exists.
