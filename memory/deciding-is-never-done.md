---
name: deciding-is-never-done
description:
  "A drawing or generator is controlling, illustrative or superseded relative to the current
  version — say which at the top of the file, because no artifact is simply 'right'."
metadata:
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-09-16T00:00:00.000Z
---

**Label every drawing and generator `controlling`, `illustrative` or `superseded`, and name the
version or the date it belongs to.**

- **controlling** — it specifies the current approach. Change the design here and nowhere else.
- **illustrative** — no decision lives in it. Either it derives from whatever controls the
  design, or it is an analysis tool that answers about whatever geometry it is handed. Name which
  kind it is beside the status.
- **superseded** — an older approach we are not doing any more. Kept as the record of what was
  decided and why it changed; not maintained against the design source.

**Why:** the user (Mike) put it as *"in engineering, deciding is never done."* There is no final
answer, only what we decided in order to make a version. A new version may re-open any decision,
and the fact that the version is different is itself the evidence that some decision changed. So an
artifact is never simply right or wrong — it is only ever specific to a range of versions, or what
we thought on a date. Asking "is this file correct?" has no answer; asking "is this file
controlling, illustrative or superseded, and for which versions?" always does.

**How to apply:** put the status in the file's own opening, above everything else. The version goes
beside it **only when the file lives in a tree named for that version.** Evergreen code is reused by
the next version, so a docstring naming the joint or the draft it was written against reads as scope
and goes false the first time it is reused; there, say what decides the inputs instead, and let the
version arrive in the data. That half is a rule, not a preference, and it is in the
[constitution](../.claude/rules/constitution.md). A frozen artifact is not a defect and MUST NOT be
"fixed" by repointing it at the current design source — that destroys the record and leaves prose
and figures contradicting each other. Three questions settle the status: does anything read this to
build the robot (controlling); does it derive from something that does, or compute about geometry
handed to it (illustrative); or does it describe geometry the robot no longer has (superseded)? An
analysis tool is illustrative however current its method, because the version it speaks about
arrives in its inputs rather than living in the file.

The trap this exists to stop: judging a file by whether its numbers match `make_plans.py`. See
[[test-the-technique-not-a-guess]] and [[no-invented-gates]]; related are
[[derive-dont-maintain]] and [[design-intent-is-not-sacred]].
