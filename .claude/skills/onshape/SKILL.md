---
name: onshape
description:
  "The contract for writing or revising Onshape modeling steps and for driving Onshape: modeling
  standards, the UI vocabulary a step uses, what a written step contains, how the agent browser
  and the session are reached, and the rate limits. Read before the first modeling step of any
  task that touches CAD or the steps that teach it."
---

# Constitution — Onshape part

Read this when writing or revising modeling steps, or when building a reference model. Read with the
[constitution](../../rules/constitution.md) and [`lesson-design`](../lesson-design/SKILL.md).

## Modeling standards

These apply to every reference model, because students copy what they see.

**Build the model the way a careful human would build it**: fully defined sketches anchored to
geometry that already exists, starting at the origin and working outward, every length driven by a
named variable, symmetry expressed as a mirror and repetition as a pattern, each part made once and
derived where it is reused, so that changing any driving dimension rebuilds the whole thing
correctly. That holds whatever the route. The REST feature API authors constraints, mate connectors,
mirrors, patterns and derived features as readily as the GUI does; it costs more calls per feature,
and a script that skips them for that reason has emitted geometry rather than built a model.
`stickbot-draft9p1p2` is what that looks like: four tabs of typed coordinates, no constraint
anywhere, the fork and the socket each built twice, and no way to change a driving length except to
re-run the script that wrote it. [`modeling-practice`](../modeling-practice/SKILL.md) says what each
clause of that sentence means feature by feature.

- **Pick one unit system and never mix.** State it in the step file's first line. A model that mixes
  inches and millimeters teaches a bug.
- **Fully define every sketch before extruding it**, and teach that from session 1. An
  under-defined sketch that drifts three sessions later is unfixable in a classroom.
- **Rename features.** `Extrude 3` tells a student nothing; `Body block` does. The feature tree is
  the vocabulary students read back to you. The name box opens from a small pencil that appears to
  the right of the dialog's title on hover, not from a click on the title itself.
- **A Variable feature is the exception, because Onshape gives it no name box.** Its title is the
  computed string `#name = value`, so its row already reads what a name would have said and more.
  The dialog's pencil stays hidden however it is hovered, the row's menu offers no *Rename*, and
  `F2` does nothing. A page MUST NOT tell a reader to name a variable. Driven in
  `stickbot-draft9p3-check` on 2026-09-09. What each frame showed is written out in
  [draft9p4's plan](../../../.docs/experiments/runs/2026-09-08-draft9p4/plan.md), § *The variable
  naming rule*; the frames themselves stayed in the `sponge` repository with the rest of the
  capture.
- **A measurement becomes a variable only when the build plan asks for it.** The Variables table
  in [`.docs/robot-build-plan.md`](../../../.docs/robot-build-plan.md) is the whole ask: a number is
  a variable when it has a row there, and is not one otherwise. A session plan, a build brief or a
  run plan MAY argue for a row — it does not create one. Every other measurement is typed, and a
  constraint or a reference carries the intent.
- **The table names them; the steps use those names verbatim** (`#pore_dia`, not `#d1`). Changing
  one number and watching the model update is the moment CAD clicks for most students, so a session
  that wants that moment needs the rows that produce it to exist before it is written.
- **Not every variable is a scaling knob.** A joint's dimensions come from how the plastic bends,
  not from how big the robot is: a ball twice the size still needs the same clearance and the same
  slit width. The table gives those numbers rows of their own and marks them **not scaled**, so the
  model records why they are what they are and they stay clear of whatever drives the robot's size.
- **Do not redeclare a Variable Studio name inside a Part Studio.** The local shadows the studio's
  row: the tab goes on using its own value, the row moves without it, and nothing turns red.
  draft9p1 found five such locals in `ball and socket` and four in `foot`, each holding a number
  the Variable Studio no longer carried. A local computed from studio rows is a different thing and
  is fine; `foot`'s `#collar_down` is one.
- **Keep the feature tree shallow and forgiving.** Students mis-click. A tree where feature 20
  depends on a face selected in feature 4 will break for someone, and debugging it costs the room's
  time, not one student's.
- **Anchor each sketch to the geometry that gives it meaning.** A plane when the shape is placed
  from the origin; the face or edge of a part when it is placed from that part. Picking a plane
  because it happens to be the one an earlier feature used does not remove the dependency — it
  removes the record of it, and the next person to move that feature gets a model that regenerates
  clean and is wrong. Never type a number to place or size something a reference would have given
  you.
- **Place a mate connector on the origin or on a feature that means something.** A connector picked
  off whatever face was under the cursor carries that face's position into the assembly. draft9p1's
  foot took its ankle connector from a wall of the socket's relief slit at x 0.8, so both feet
  landed 0.8 mm off their legs and the pair read as handed.
- **Insert from the workspace, and keep every reference inside one document.** The robot is one
  document: an assembly instances the Part Studios in its own workspace, and a part derives from
  that same workspace. Nothing in this class references another document, and nothing references a
  version. A workspace reference names an element and nothing else, so it follows the edit just
  made and a document copy re-points it. A version reference names a document and a version, and a
  copy has no version of its own for that reference to become, so it goes on naming the original
  after the copy — which is how a draft inherits an assembly that shows the previous draft's parts.
  _Discipline_'s **Cite named versions, never live workspaces** governs material that cites a
  reference document; this governs references inside a model, and the two do not meet.

## Choosing what to teach

Working Rule 6 applied to CAD: the simplest feature that produces the shape wins.

- **A step, or a set of steps, MUST earn its place against doing it the plain way.**
  Extrude, Revolve, Fillet, Shell, Mirror, and Pattern carry almost the whole model. Reach for Loft
  or Sweep only when nothing simpler makes the shape, and only after the basics are solid. A
  step might earn its place by teaching a method or tool that is in the agreed learning objectives.
- Extrude, Revolve, Fillet, Shell, Mirror, and Pattern carry almost the whole model.
- **Configurations, in-context design, and custom features are instructor-side.** If FeatureScript
  removes work for students, students _consume_ the custom feature; they do not write it. Authoring
  FeatureScript is not a beginner exercise and does not belong in these eight hours.

## Writing steps

- **One action per numbered step.** If a step contains "and", it is probably two steps.
- **UI labels verbatim, in bold** — **Extrude**, **New sketch**, **Fully defined**. If the label in
  the file and the label on the screen differ by a word, students stop.
- **Name the mouse action, and put the keystroke after it in parentheses** — **Extrude**
  (or press **shift+e**), **Revolve** (or press **shift+w**), the **Dimension** tool (**d**). A
  student who does not yet know where a tool lives can follow the click; the key is there to be
  picked up by repetition. Say **or press** the first couple of times on a page, then drop to the
  bare key — **Extrude** (**shift+e**) — once the reader has seen the pattern.
- **The key is bold, and there is no space inside the parentheses.** (**shift+e**), not
  ( *shift+e* ). A keystroke is a thing on a keycap, and it is set the way every other thing the
  reader has to find on the screen is set.
- **Write the key the way the keyboard is pressed, in lower case** — (**shift+f**), never **F**. A
  capital letter in a step reads as a different key from the one on the keycap.
- **When the key press *is* the action, write it as one.** A tool the reader clicks gets its name
  and the key in parentheses. A view change has nothing to click, so the sentence has to say what
  to press: *Press **n** to look **n**ormal — square on — at the plane*, not *View normal to
  (**n**) looks square at the plane*. The second one reads as a fact about Onshape, and a reader
  who takes it as a fact never presses the key and never gets the picture in the figure. **Bold
  the key's letter inside the word it comes from** where there is one — **n**ormal, zoom to
  **f**it — because that is what makes the key stick.
- **Take the keys from Onshape's own list, not from memory.** **shift+/** opens it, and it is per
  tab — Part Studio, 3D view and Sketch each have their own. A tool with no row there has no
  shortcut, and inventing one costs class time (see _Discipline_ below).
- **State the expected result after each block**, in terms a student can check without you: what the
  shape looks like, what color the sketch went, what the feature list now says.
- **Name the starting document and the ending version.** Every step file opens with what to open and
  closes with what to publish.
- **List the likely failure and its fix** for each block. Under-defined sketch, extruded the wrong
  direction, lost the view orientation — you know which ones will happen; write the recovery down so
  the mentor is not improvising it thirty times.

## Every build or test report opens with where the work is

The first section of every build or test report is **Where the work is**, and it carries:

- the **document name**, exactly as it appears in Onshape, and the owning account;
- the **document id**, and the **element id** of the Part Studio or Assembly;
- a **published, named version** — id and name both — and a link to it;
- the live workspace link, labeled as live, for anyone who needs to edit rather than read.

**Publish a named version before writing the report** (Working Rule 13, and the _Links resolve_
gate). If none was published, say so in that section rather than leaving it out.

**Say whether you opened the links.** Ids read from a tab and assembled into a URL are not a
followed link, and claiming otherwise is a Working Rule 8 violation.

**Every report carries a render, and whoever reads it looks at it.** The views are the set the
_Model inspected_ gate asks for. Use
`GET /api/partstudios/d/{d}/w/{w}/e/{e}/shadedviews?viewMatrix=isometric&…`, or
`.../parts/…/partid/{pid}/shadedviews` for a single part.

**Before building a second version of something that already exists, look at the first one.**

## Get the session back with the repo's own scripts

A missing session does not announce itself as one. It surfaces as `NotSignedIn` out of
[`tools/onshape_session.py`](../../../tools/onshape_session.py), or as a 401 from a script driving
the agent browser. Answer it with [`tools/browser.py`](../../../tools/browser.py) rather than a
script written for the occasion.

- **Ask before guessing.** `uv run python tools/browser.py --status` names the signed-in user or
  says there is none. A 401 against the agent browser usually means its borrowed cookies went stale
  rather than that anyone is signed out, and
  [`tools/agent_browser.py`](../../../tools/agent_browser.py) says why.
- **`--signin` gets the session back without a person.** It types the account email — from
  `git config user.email`, or from `--email` — into Onshape's first sign-in page, and Chrome's
  saved credential fills the second. If Chrome has nothing saved it says so, and then someone signs
  in by hand once so Chrome can offer to save it.
- **No password is read, typed, printed or stored.** A script MAY look at a password field's length.
  It MUST NOT look at that field's value, and MUST NOT open the browser profile's credential store.
  Chrome does the filling, which is how the tooling signs in and still handles no password.
- **Port 9222 is driven for this and for nothing else.** Scripts drive the agent browser on 9223,
  and restarting it is what carries a new session across.

## Read what a refusal says before waiting on it

Onshape's **429** has two modes and they take different answers. A burst of feature writes earns a
block that clears in minutes. A spent daily quota does not clear that day at all. The response says
which: on 2026-08-27 `partstudios/.../features` answered `retry-after: 67201`, which is 18 hours
40 minutes counting down against the clock, alongside `x-rate-limit-remaining: 0`.

- **Keep the response headers.** A client that returns status and body and drops the headers cannot
  tell the two modes apart, and a retry ladder that cannot read `retry-after` turns a day-long quota
  into something indistinguishable from a hang. `api()` in
  [`tools/onshape_session.py`](../../../tools/onshape_session.py) reads them and decides on them;
  anything else talking to Onshape does the same or uses it. Eight earlier attempts assumed the
  short block, and [`.docs/README.md`](../../../.docs/README.md) § *Pipeline improvements worth
  making* has the sweep and why each one missed.
- **Back off for the burst, and stop.** Waits that reach into the minutes outlast a burst. Nothing
  outlasts a quota, so when `retry-after` reads in the hours, change the plan rather than waiting.
- **The limit is per endpoint family.** With `features` at zero, `bodydetails`, `parts`,
  `boundingboxes`, `assemblies`, `variables` and `sketches?includeGeometry=true` each had hundreds
  to thousands of calls left. A read-back written against the geometry endpoints survives a block
  that stops the feature endpoint.
- **The GUI is not rate limited.** draft9p1p1 read every expression it needed out of the feature
  tree and the dialogs, and deleted three features by right-click, while `features` was refusing.
- **Pace the writes so it never arrives.** A few hundred milliseconds between feature writes costs
  less than one block.

[`.docs/onshape-api.md`](../../../.docs/onshape-api.md) § *Rate limits* carries what an unhandled
429 does to the calling code, which is nothing that looks like rate limiting.

## Wait on the process, not on its name

A browser-driving script runs longer than a foreground shell allows, so it goes to the background
and something waits for it. What that waiter tests decides whether it ever stops.

- **`pgrep -f <script>` matches the waiter itself.** `-f` searches whole command lines, and the
  waiting shell's command line contains the script's name because it is written there in the
  pattern. So `until ! pgrep -f probe.py; do sleep 4; done` waits for itself to exit and never
  returns. On 2026-09-09 twenty-four shells were killed that had been holding that loop for six to
  thirteen days, against scripts that finished the day they were started.
- **Wait on the PID.** Keep what the background launch returns and test `kill -0 $pid`, or wait on
  a sentinel the script writes as its last line and test for that line. Both name one thing rather
  than a pattern that can match the asker.
- **Give every wait a ceiling.** A bounded loop that gives up and says so is a result. An unbounded
  one is a hang wearing a progress message.
- **Check what a wait left behind.** `ps -eo pid,ppid,etime,command` filtered on the session's
  parent shows shells that outlived their work. A finished run leaves none.
- **Sleep between checks.** A loop that reads without sleeping spins a core for as long as it
  waits. `sleep` a few seconds between tests; nothing here answers faster than that.

## Discipline

- **Don't fabricate a mechanism.** If a tool's behavior or a menu's location is uncertain, open
  Onshape and look. Onshape's UI changes between releases, so recalled menu paths are a frequent
  source of confidently wrong steps — and here a wrong step costs class time, not a re-read
  (Working Rule 8).
- **Build it before you write it** (Constitution, _Verification is evidence_). Model the thing, then
  write down what you actually did.
- **Reproduce from empty.** Following your own steps from a blank document is the gate that catches
  the knowledge you did not know you were assuming.
- **Cite named versions, never live workspaces.** A workspace moves under the class.
- **Read a driven change off the part, not off the dialog it was typed into.** A green
  regeneration says the model rebuilt; it does not say the change reached the geometry. draft9p1
  deleted a variable, watched the feature that read it get 1.65 mm shorter, and measured the same
  volume as before, because a union had already welded that material into a derived body and no
  feature went red.
- **Drive a number to a second value before believing a symmetry.** In draft9p1p1 the gripper's
  slab was held on the left by a dimension reading `#clipR` and on the right by a tangent to a
  circle of radius `#clipR`. The sketch was fully defined and the part was symmetric, and one
  number drove half of it: retyping the dimension moved the left edge and left the right at 5. Two
  meanings that move together hide the same way, which is why driving `#torsoH` never showed that
  it was placing both the torso's height and its hips.
- **A comparison finds disagreements, not shared mistakes.** draft9p1 measured the model against
  the design source and matched on all three shapes draft9p1p1 then had to repair, because both
  documents described all three the same wrong way. Reading the source and turning the model is
  what found them, which is the _Model inspected_ gate doing the work measurement cannot.

## See also

- [`.claude/rules/constitution.md`](../../rules/constitution.md) — Working Rules + Quality Gates.
- [`lesson-design`](../lesson-design/SKILL.md) — pacing, floor/ceiling, checkpoints, rubrics.
