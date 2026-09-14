# Launch gate — 2026-08-12

What the launcher performs, and records, before any agent starts.

Dated because it will age out. Every item here exists because of a specific failure in run 1, 2
or 3. An item whose failure can no longer happen should be deleted, not carried.

[`experiments/build-briefs/README.md`](experiments/build-briefs/README.md) is the agent's
contract. This is the launcher's.

## Every brief

**Every number carries a Source.** `plan`, `built` or `proposed` — the convention is in the
brief README. A number with no source cannot be checked by the agent who builds to it.

**Re-trace every `plan` number to `robot-build-plan.md` as it stands today.** Not from memory,
and not from the last time the brief was read. Six of run 2's nine errors were numbers left
behind when the variable that drove them changed.

**Trace every `built` number to the run that measured it, and name that run.** A number nobody
can attribute is a proposal wearing a measurement's clothes.

**Check every open question against the session logs and the memories before it goes out as
open.** On 2026-08-12 three agents were launched against a conflict over limb sections that did
not exist. `#limbD` had been settled at 12 the previous day, in conversation, recorded in no
single file. Absent from the files you read is not the same as undecided.

**Open every link the brief makes** — files, Onshape documents, named versions.

## Every launch prompt

**Open every file in the reading list and check its description against its contents.** The
description is what an agent uses to decide how carefully to read. Run 3's Explore agent was
told book-em-danno was "the big one, 60 files"; true by volume, wrong by relevance, and it had
to disregard the hint to do the job.

**Name the predecessor's build-notes for the same part.** Each run has otherwise re-learned what
the last one found. The how-to carries the general lessons; the part-specific ones stay in the
run's notes.

**Say which numbers are proposals, and that they are not to be tuned.** A proposal is there to
be built to and reported on, not adjusted until it looks right.

## The run's plumbing

**Freeze the text before launching.** An agent reads the shared contract once, at the start. A
correction made afterwards does not reach it — run 3's three agents all read a withdrawn section
before it was withdrawn, and only one of them was told.

**Write deliverables straight into the run's archive directory**,
`experiments/runs/<date>-run<N>/<part>/`. A live directory that has to be moved afterwards is a
step that gets skipped.

**Set the watchdog's grace longer than the reading load.** A six-minute grace raised a false
alarm on a live agent on 2026-08-12, which was still working through `CLAUDE.md`,
`constitution.md`, the how-to, the brief README, its own brief and `.parts/onshape.md`.

**Record every agent's id in the run directory.** `SendMessage` to the id resumes a finished
agent from its transcript, so it can still be interviewed after it reports — `ListAgents` stops
listing it, which is what made this look impossible. The id is the only handle and it does not
outlive the launching session.

## After the report

**Open the model and turn it before reviewing anything the agent wrote.** Each part alone, at
its published version — isometric, the working face, a section — until you know what the shape
is. The Constitution's *Model inspected* gate is the launcher's to perform as much as the
builder's: the brief already asks the agent to render every part, and accepting those renders as
your inspection means looking only at the views it chose to take. A hinge fork was invisible in
all four standard whole-model views because the parts overlapped along the camera axis, and
nobody noticed the joint had never been looked at.

**Re-measure what the report claims, yourself.** Every headline number, and the extents and wall
thicknesses the brief asks for. A relief slit came out 2.7 mm deep against 5.5 specified and
every acceptance check still passed. `shadedviews` renders a view in one request, and REST is
read-only, which is all a review needs.

**Read the report, then interview — a retrospective, not a cross-examination.** You are after
two things: what the agent knows that its report did not carry, and its advice on what to change
so the next run goes better. Ask for that advice directly; the agent is the only witness to
where the brief failed.

**Where your measurement disagrees with the report's, say so and ask what happened.** Telling
the agent you think a number is wrong is how you get at what to do differently — it is not a
charge to be proved. Establishing that an agent was wrong buys nothing. An agent that has to
defend itself stops telling you things, and the things it stops telling you are the ones worth
having.

**Ask what it nearly got wrong.** The written retrospective is what makes an interview possible
when an agent cannot be reached; it is not a substitute for one, because a report records what
happened and the near-miss is what almost happened. Asked "name something you nearly reported
without verifying", run 3's Explore agent gave up a search that would have silently dropped an
entire directory from its answer. It appeared nowhere in what it wrote, and where a careful
agent nearly went wrong is where a student will go wrong.

## Recording

Write which items were performed, and what each turned up, to the run's own directory before the
first agent starts. A gate nobody can show they ran is an assertion.
