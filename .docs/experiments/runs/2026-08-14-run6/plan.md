# Run 6 — re-CAD the robot as a student would, and write the guide from it

Run 5 audited and repaired CAD that already existed. Run 6 builds the whole robot again from
empty documents, through the GUI, one click at a time, recording what a student sees at every
step — and the recording is the deliverable, not a by-product.

The design decisions this run carries out are in [`design-note.md`](design-note.md). This file is
how the run is executed.

## What is different from run 5

- **Every part is rebuilt, not repaired.** Run 5's models are the thing being validated against,
  not the thing being edited.
- **The GUI is the only route.** Steps a student cannot perform are not steps. The API is for
  measuring and for nothing else.
- **Screenshots are taken as the step happens**, not reconstructed afterward. A step with no shot
  is a step that was not recorded.
- **The joints are built once and reused**, per [`design-note.md`](design-note.md). Phase 4 did
  not do this. Phases 7a–7c below are the repair, and the reason they exist is stated there.
- **The torso is built from the front.** See below.

## The torso changes how it is built

Today the torso starts from a sketch named `Torso footprint` — a plan view on the Top plane,
extruded upward. Every overview sheet the student has just looked at is a **front** elevation, so
the first thing they do in Onshape faces a different way than the drawing they are working from.

**Run 6 draws the torso's front face on the Front plane and extrudes it in Y.** A center point
rectangle on the origin, torso width by torso height, extruded symmetric through the torso's
depth. Symmetric keeps the origin at the center of the torso, which is what the layout sketch and
the assembly both rely on.

This must change no geometry at all. The rebuilt torso has to measure the same box as run 5's.
That is a validation check in phase 5, not an assumption.

## The joints are reused, not rebuilt — run 6p2

Phase 4 built every part's joints from native sketches, revolves and Booleans. Nothing in phase 4
references the joint documents phase 3 published. Read the `| Tree row |` tables in
[`build-notes.md`](build-notes.md) side by side and it is plain: the socket appears in the head,
the hand, the foot and the socket-clevis limb, seven or eight features each, and **the four are
not built the same way** — the head and the clevis limb revolve the cavity away, the hand and the
foot revolve a whole ball as a separate part and Boolean-subtract it with an offset. The ball stud
is revolved seven times over. Only the hinge is built once per half, and only because one part
carries each half.

**The geometry is not the problem.** Phase 5 measured every part against `target.json` and phase 7
measured the assembled robot; both pass. The four sockets' cavity areas agree to the fourth
decimal, which [`evaluation.md`](evaluation.md) reads as evidence the brief is followable — and
that reading stands. It is evidence about the brief. It is not reuse, and four independent builds
agreeing is exactly what reuse would have made unnecessary.

**Three things make it worth redoing.** The guide is a teaching document and
`robot-guide2/source/index.rst` already promises the student models each joint once and uses it
everywhere; written from the phase 4 record, five part pages would teach the socket five times,
two different ways. The session has 90 minutes of hands-on and rebuilding a socket per part does
not fit in it. And a part that derives its socket picks up a corrected socket for free, where four
hand-built ones have to be found and fixed one at a time.

### The rule

For each part that carries a joint:

1. **Copy** its run 6 document to a new document named `<part>-run6p2`. Copy
   `ball-socket-run61` and `hinge-run61` across as well, unchanged — the joints themselves are
   fine and are not redesigned.
2. Walk the feature list for **the block of features that re-creates a joint** — a joint's
   features are contiguous. On the gripper that is `Collar circle` to the end; on the foot it is
   `Collar circle` through `Four slits`, with the sole groove and its ribs sitting below it. The
   socket is the collar, its cavity and its slits, so the block starts at the collar, not at the
   cavity.
3. **Delete that block, and the part's phase-6 mate connector on the joint with it** — the
   connector is placed on the joint's own geometry and cannot survive the cut. What is left above
   and below the cut keeps its notes and its shots — but **read the tree back afterwards**,
   because Onshape may take a feature below the cut with it. Why only the block, and what it cost
   to find out, is in [`replan-notes.md`](replan-notes.md) under *Cut the joint's features, not
   everything after them*; what the head lost is under *The head*.
4. **Put the joint back by deriving it**, on the `Derived → Transform → Boolean Union` route
   phase 0 settled — [`spike-boolean-mate.md`](spike-boolean-mate.md) — from the 6p2 joint
   document's named version. Where the part needs something new to meet the standard joint, it
   is built here: the foot's pedestal is the case, and the head's socket is the one that needs
   the Transform.
5. **Put the part's mate connectors back**, from the table of all twelve in
   [`build-notes.md`](build-notes.md). Neither joint document carries one, so a derive brings
   none — [`replan-notes.md`](replan-notes.md), *The joint documents carry no mate connectors*.
6. **New notes, new shots, new scripts, starting at the cut.** What survives is already recorded
   to the capture standard, so it is not re-performed and not re-shot.
7. **Publish a named version and measure it against the part's run 6 version.** The from-scratch
   part is the thing the derived one has to match. A delta is classified the way phase 5
   classifies one, not waved through.

**Copying a document was forbidden in phase 1 and is allowed here**, and the difference is worth
being clear about. Phase 1's rule exists because a copied run 5 document arrives with a tree
nobody watched being built, so every step after it is an edit of somebody else's CAD. A 6p2 copy
arrives with a tree **this run built through the GUI with a shot per click**, already on disk in
`shots/`. The record is complete for the prefix; that is what makes it safe to keep rather than
re-perform.

### What is not decided yet

- ~~**The foot's collar stands 7.35 proud against the standard 5.5.**~~ Settled by building it:
  the standard socket does not drop into the foot unchanged — it hangs 1.85 clear of the plate,
  and the foot gets a pedestal of its own to stand it on. 7.35 is 5.5 of standard socket on 1.85
  of foot. [`replan-notes.md`](replan-notes.md), *The foot needs a pedestal, and that settles the
  7.35 collar*; the disagreement [`audit.md`](audit.md) carries between `foot.md` and
  `design-note.md` was two right answers about different things.
- ~~**The head's socket is upside down**, so its derive needs the Transform step.~~ It does, and
  it takes two: a Rotate of 180° about the head's own dome and a Translate of z −22.15.
  [`replan-notes.md`](replan-notes.md), *The head*.
- ~~**Whether the hinge halves reuse as cleanly as the ball and socket.**~~ The clevis half does:
  not one of the fork's forty-eight detent teeth shows in the difference against run 6. It brings
  a length of limb with it, though, and the part's own stock shortens to suit —
  [`replan-notes.md`](replan-notes.md), *The socket-clevis limb*. So does the blade half, and it
  brings a length of limb too: the blade-ball limb's own stock is the 4 between them —
  [`replan-notes.md`](replan-notes.md), *The blade-ball limb*.

## Outputs

Everything run 5 produced, for run 6, in `runs/2026-08-14-run6/`:

`target.json`, `audit.md`, `measured.json`, `build-notes.md`, `deconflict.md`, `repairs.md`,
`evaluation.md`, `register.md`, `run6-documents.json`, `run61-documents.json`, `shots/`

Plus the replan's, described under **run 6p2** below:

`run6p2-documents.json`, `replan-notes.md`, `replan-measured.json`

Plus the one that is new:

**`instructions/robot-guide2/`** — a Sphinx page in the shape of
[`../../../../instructions/robot-guide/`](../../../../instructions/robot-guide/): a `Makefile`, a
`README.md` saying what has been proved and what has not, and `source/` with `conf.py`,
`index.rst`, `_static/` and `images/`. Written from the recorded steps and the shots taken while
performing them.

## The phases

Mark each phase **Done.** as it completes.

0. **Spike — the Boolean and the mate connector.** Two blocks, a mate connector owned by each,
   union in both selection orders. Record which connectors survive and who owns them. This gates
   how every joint is added, so nothing else starts until it is answered. Write it to
   `spike-boolean-mate.md`. **Done.** — [`spike-boolean-mate.md`](spike-boolean-mate.md).
1. **Empty documents, and freeze the sheets.** Create the run 6 documents **empty** and record the
   ids in `run6-documents.json`. **Nothing is copied from run 5.** A copied document arrives with
   the feature tree already built, and every step after it would be an edit of somebody else's CAD
   rather than a step a student performs — which is the whole run. Run 5's documents are opened to
   measure against in phase 5 and are never a starting point. Freeze the current sheets into
   [`../../sketches/`](../../sketches/) under the next revision before anything regenerates them.
   **Done.** Nine empty documents in `Coach Mike Experiments`, each set to millimetres at five
   decimals — [`run6-documents.json`](run6-documents.json). The working sheets were frozen as **r3**,
   which is the head-collar revision that had been sitting unfrozen since `fc8c340`.
2. **State the target.** Re-run `make_target.py` into `target.json`, so the run has one machine-
   written statement of every design constant and brief row. Nothing typed in. **Done.** —
   [`target.json`](target.json). Against run 5's it moves in four places and all four are the head
   collar: `HEAD_RIM` is new at 27.65, `HEAD_B` 27.65 → 33.15, `HEAD_T` 63.65 → 69.15, `HEIGHT`
   152.65 → 158.15. Nothing else in the design changed number.
3. **Build the four halves.** Ball stud, socket collar, clevis fork, detent blade — each modeled
   once, at the origin, and published as a named version. Steps and shots recorded as they are
   performed. **A joint's two halves share one Part Studio**, not one each:
   [`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) makes the
   cavity by subtracting the ball from the socket with an offset, so the two have to be in the same
   studio for the clearance to be one number in one field rather than a second sphere that can
   drift. So two studios, two halves each — which is also how run 5's documents were laid out.
   **The scaffolding does not come along.** The brief stands its test socket on a Ø12 limb stub and
   its test stud on a Ø10 base; both exist to give a study something to hold. A reusable half
   carries only itself, because the socket mounts on a limb, a head, a hand and a foot, and a stub
   would be wrong on three of them.
   Built once in the run 6 documents and measured — versions `ball-socket-run6-2026-08-14`
   (`14ca9e264e8aa2032b6de377`) and `hinge-run6-2026-08-14` (`6fdeee5b50121f8c751c3612`) — and
   those numbers stand. **Then built again**, from empty documents, to the capture and naming
   standard below, because the first pass did not produce a record a beginner can learn Onshape
   from: its shots are of geometry after a step succeeded rather than of the dialog with its
   fields filled, and its tree carries `Sketch 1`, `Extrude 7`, `Mirror 3`. The rebuild's
   documents are named **run 6.1** so they stay separate from the run 6 ones when starting over;
   ids in [`run61-documents.json`](run61-documents.json). Run 5's, run 5.1's and run 6's models
   may be opened to check a number against — be back on the run 6.1 document before performing a
   step.
   **Done.** — [`build-notes.md`](build-notes.md), versions `ball-socket-run61-2026-08-14`
   (`cd146dc9becaaac2dc34c1d7`) and `hinge-run61-2026-08-14` (`2d85fa248db742e137da6e96`).
4. **Build the six parts.** Torso, head, `limb-socket-clevis`, `limb-blade-ball`, hand, foot —
   each from an empty document, through the GUI, reusing the halves from phase 3. The torso
   front-first. Steps and shots recorded as they are performed, to the same capture and naming
   standard. A named version per part.
   Build them the way [`spike-guide2.md`](spike-guide2.md) found they need to be built to be
   writable: **finish one part before starting the next** where the geometry allows it, and note
   the crossings that are forced; **no starting offsets on a Remove** — sketch on the face or use
   **Up to face**, so no step has to say "check it did not go the other way"; **a sketch is
   finished when the next feature can consume it**, not when it looks like the shape.
   **Done.** — [`build-notes.md`](build-notes.md), versions `torso-run6-2026-08-14-2`
   (`a802fa578af50f48eabadb06`), `head-run6-2026-08-14` (`2c594a3ade6bbc9e50bcb377`),
   `limb-socket-clevis-run6-2026-08-15` (`6f362f52291d44e89d84e193`),
   `limb-blade-ball-run6-2026-08-15-2` (`6adf73417e7b344c74c03fed`), `hand-run6-2026-08-15`
   (`6f4f1d9a8c70581028b4d122`) and `foot-run6-2026-08-15-2` (`418e39c06d54804cd87f737a`).
5. **Validate against run 5.** Measure every rebuilt part and compare against run 5's
   `measured.json` and against `target.json`. Classify every delta: a **run 5 defect** the rebuild
   exposed, a **run 6 regression**, or a **deliberate change** from `design-note.md`. Write
   `audit.md`. Nothing is waved through because it is small.
   **Done.** — [`audit.md`](audit.md) and [`measured.json`](measured.json), measured off the six
   named versions. Every part hits its target numbers; no run 6 part carries a mate connector,
   which phase 6 needs.
6. **Assemble.** Every instance from a named version, never a workspace. Publish the assembled
   version.
   **Done.** — [`build-notes.md`](build-notes.md). Twelve mate connectors first, since phase 5
   found the parts had none, then fourteen instances and thirteen mates in `lesson-run6`'s
   Assembly 1, published as `robot-run6-2026-08-15` (`cab79923d9e94d9f908d359f`). The parts were
   re-versioned to carry their connectors — `torso-run6-mates-2026-08-15`
   (`3a882a1ecb98644fa63a6e8e`), `head-run6-mates-2026-08-15` (`b2c9747847cf20e523105b66`),
   `limb-socket-clevis-run6-named-2026-08-15` (`e316910ec9c9dc3dc6f155f2`),
   `limb-blade-ball-run6-named-2026-08-15` (`4e5e510f296c182db74ba8b1`),
   `hand-run6-mates-2026-08-15` (`fe622c2d51542d98056f0550`) and `foot-run6-mates-2026-08-15`
   (`f3a10c6ba450a92a22bf0c4a`).
7. **Evaluate.** The three axes, on the parts and on the robot, into `evaluation.md`.
   **Done.** — [`evaluation.md`](evaluation.md). Every station matches, including the two the head
   collar moved; the arms hang where the solver left them because no ball mate carries a pose. The
   thinnest wall in the parts is the 0.2531 land between detent valleys, which is the one number
   below a nozzle width. Print orientation, joint ranges and the ear spring's margin are not
   answered and go to phase 9 in those words.

   The replan lands here, between 7 and 8, because phase 8 writes from what the parts are and
   these three change it. They keep 7's number so 8 and 9 keep theirs.

   - **7a. Spike the reuse route, on the gripper.** One part, the whole rule above, so the route
     is known before five more parts ride on it. Copy `hand-run6`, `ball-socket-run61` and
     `hinge-run61` to run 6p2 and record the ids in `run6p2-documents.json`. Cut the gripper at
     `Collar circle`, derive `Socket body` from `ball-socket-run6p2`'s named version, place it on
     the clip and union it. Publish, measure against `hand-run6-2026-08-15`
     (`6f4f1d9a8c70581028b4d122`), and write what the route costs and what it takes to
     `replan-notes.md`. The gripper is the spike because it is the shortest part that carries a
     joint — two features of its own, and everything after is socket.
     **Done.** The gripper is four features where it was ten, and
     [`replan-notes.md`](replan-notes.md) carries the route: `Derived` is reached from the
     **Alt+c** tool search and from no toolbar flyout, the union renames the merged part as well
     as keeping the first tool's connectors, and `Base origin` placed the socket with no
     Transform. The measured delta is real and it is classified there — run 6's slits cross the
     axis and the joint's stop short of it, so the derived gripper is 24.1627 mm³ heavier and
     **it is the from-scratch socket that drifted from the joint**, not the derived one.
   - **7b. The rest of the parts that carry a joint.** Head, foot, `limb-socket-clevis`,
     `limb-blade-ball`, torso — the same rule, the same capture and naming standard, each
     measured against its own run 6 version. The torso derives a ball stud three times; the
     socket-clevis limb derives both a socket and a clevis fork and is the one that answers
     whether the hinge reuses as cleanly. Where a part will not take the standard joint
     unchanged, that is a finding for `replan-notes.md` and the run keeps going.
     **Done.** — [`replan-notes.md`](replan-notes.md), *7b*. Versions `head-run6p2-2026-08-15`,
     `foot-run6p2-2026-08-15`, `limb-socket-clevis-run6p2-2026-08-15-2`,
     `limb-blade-ball-run6p2-2026-08-15` and `torso-run6p2-2026-08-15`
     (`9c8d9298e7fc0ef0f005b0c9`), the last of which matches its run 6 part face for face. The
     head, foot and gripper were then given the phase-6 connectors the joint documents do not
     carry, in versions `hand-run6p2-mates-2026-08-15`, `foot-run6p2-mates-2026-08-15` and
     `head-run6p2-mates-2026-08-15` — `replan-notes.md`, *The joint documents carry no mate
     connectors*.
   - **7c. Re-assemble from the 6p2 versions.** The same thirteen mates as phase 6, every
     instance from a 6p2 named version. Publish it, and check it against phase 7's stations. The
     connectors ride in on the derived joint or they are made on the host after the merge, which
     is what phase 0 settled and 7a is the first real use of.
     **Done.** — [`replan-notes.md`](replan-notes.md), *7c*. `robot-run6p2-2026-08-15`
     (`058dd63ee387e60a85040d70`) in `lesson-run6p2`, every instance from a 6p2 named version and
     every one of the fourteen on the same transform as `robot-run6-2026-08-15`.
8. **Write `robot-guide2`.** From the recorded steps and shots. It must pass the Constitution's
   Quality Gates, including the one that matters most here: **rebuild the result from an empty
   document following only the written steps.** Writing steps is not proving them. Start from the
   redrafted spike, not from nothing. Phase 8 adds the six parts and the assembly, folds in
   whatever phases 4–7 change about the joints, and settles the session split — the floor, the
   ceiling and the recovery version. The one experiment it carries forward:
   [`spike-guide2.md`](spike-guide2.md) argues that four of the habits are one habit; try merging
   them and keep the merge only if it stays actionable at the point of use.
   **Each part page is written from two records**: the run 6 and run 6.1 one up to the feature
   where that part switches to 6p2, and the 6p2 one after it. The cut point in the tree is the
   seam in the page as well.
   **Done, with one gate unmet.** `source/` now holds the two joints, the six parts and the
   assembly, plus [`lesson-design.md`](../../../../instructions/robot-guide2/lesson-design.md) for
   the split. The habit merge **held**: *read the dialog back before you tick it* now fires on
   every page, and phase 8 added the read-backs the foot, the torso and the assembly were missing.
   Three pages carried claims the 6p2 route falsified — the gripper and the foot said a derive
   brings the joint's mate connectors with it, and it does not — so each grew a section that makes
   the connector on the host. **The rebuild gate is unmet:** no page has been driven from an empty
   document following only its own written steps, and that is recorded in `lesson-design.md` and
   in the register.
9. **Register.** `register.md` — resolved, not resolved, never attempted, in those words.
   **Done.** — [`register.md`](register.md). Not resolved is headed by the rebuild gate and the
   unclocked session split; never attempted is the list run 5 left, plus printing. Run 5's one open
   item — the torso's two shoulder connectors at the old stations — is closed by the rebuild.

The instruction spike is **redrafted from the rebuilt joints' shots as soon as phase 3 is done**,
and phase 8 starts from that draft. The first spike — [`spike-guide2.md`](spike-guide2.md) — is a
do-over: it was written as a list of things that go wrong rather than as advice to a student who
is going to succeed, and it had no shots of what to click.

## How the guide is written

This is the part the first spike got wrong, so it is stated before the building starts.

- **Advice, not warnings.** Every admonition is `:class: advice`. It says what to do and what you
  will see when it works. The failure does not appear on the page in any form — not as a warning,
  not as "watch out for", not as a clause on the end of a sentence.
- **Light-hearted.** The reader is going to succeed at this. Write like you expect that.
- **The plan comes first**, at the top level: what the whole robot is, and a picture of it built.
  Then, at the start of each part, the detailed view of what that part looks like when it is done.
  The first spike got this second part right and it stays.
- **A picture at every click.** If a step says click something or type something, the page shows
  it.
- **Named headings, no numbers.**

Findings, gotchas, and what went sideways during the build belong in `build-notes.md`. That file's
reader is the next builder. The guide's reader is a student.

## The capture standard

For every feature:

| Frame | When |
| ----- | ---- |
| the tool, about to be picked | before the click that opens it |
| the dialog, empty | as it opens, so the reader sees which fields exist |
| the dialog, filled | every field set, before the green tick |
| the result | after the tick, with the tree row showing its new name |

Sketches get one more: the profile fully defined — black — with its dimensions on screen.

## The naming standard

Rename in the same step that commits the feature, not in a pass at the end. A name says what the
feature is for: `Stud profile`, `Revolve stud`, `Collar blank`, `Cavity from ball`, `Relief slits`.
Parts too: `Ball stud`, `Socket body`, `Clevis fork`, `Detent blade`.

Run the phases in order, in this top-level agent, which does all of the CAD itself. Analysis,
research and evaluation may go to sub-agents; CAD may not.

**A finding never ends a step, a part, or the run.** Record it and keep going. Phases do not end
in a report-and-wait — mark Done, commit, start the next.

## Rules this run works under

These are not new. They are the ones this run will be tempted to break.

- **Port 9223 only.** Port 9222 is the user's own signed-in browser and is never driven.
- **The GUI is the record.** A menu path not opened is not written down. A dimension recalled is
  not measured. This is the Constitution's rule 9 and it is the whole point of the run.
- **Build it before you write it.** The guide is written from what was done, in the order it was
  done, never from what should work.
- **Named versions only** in anything that cites a model.
- **Feature branch, no pushing unless asked.** Commit at every phase boundary and at every part.
- **The clock is a constraint on the guide, not on the run.** The session the guide describes has
  to fit 90 minutes of hands-on in a 2-hour session, and it needs a floor, a ceiling, and a
  published recovery version.

## Screenshots

Shots live in `shots/` as they are taken, named for the phase and step that produced them, and
the ones the guide uses are copied into `robot-guide2/source/images/`. The originals stay, so a
later reader can see the steps that did not make the page.

A shot is taken **before** the click that a student could get wrong, not only after — the dialog
as it appears, with the field that matters visible. A picture of a finished feature does not teach
anyone which button made it.

Take a shot per **habit** as well as per step: the Extrude dialog with the merge scope named, the
underlined New / Add / Remove, a field with its chip in it, the view cube after **n**. The spike
found the guide's habits section carries the warnings that cost run 6 the most time and had no
pictures at all, because shots get taken after a step succeeds rather than before it can go wrong.

## The watchdog

This run uses a watchdog so it continues while unattended. Its job is to restart the run at the
phase in flight, nothing else.

**The watchdog is cancelled when the run reaches phase 9 and the register is written.** It is not
used to find more work, extend the run, or start anything that is not in the phase list above. A
finished run with a live watchdog is a defect.

## Known unknowns at the time of writing

- ~~The Boolean/mate-connector behavior.~~ Answered by phase 0 —
  [`spike-boolean-mate.md`](spike-boolean-mate.md). The union keeps only the first tool's
  connectors, so every joint's connectors are made on the host after the merge.
- Whether the hinge halves reuse as cleanly as the ball and socket. They carry detents and a
  handedness the ball joint does not. Phase 4 answered nothing here because it reused neither;
  7b is where it gets answered, on `limb-socket-clevis`.
- ~~What `Derived` costs per part, in clicks.~~ Twenty-five on the gripper, cut to named union,
  counted off `shots/p7a-gripper.log` in [`replan-notes.md`](replan-notes.md). What it costs a
  student in wall-clock is still open; 7a's own nineteen minutes were mostly spent finding the
  tool, so 7b's five parts are where a per-part number comes from.
- Whether the rebuilt parts match run 5 exactly. Where they do not, run 5 is not automatically
  the correct one — see [`design-intent`](../../build-briefs/README.md) and phase 5's
  classification.
