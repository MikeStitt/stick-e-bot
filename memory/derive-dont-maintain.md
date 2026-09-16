---
name: derive-dont-maintain
description:
  "Never write down a count, list or summary that a grep or a few lines of Python can produce —
  storing it creates permanent maintenance for no information."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-13T02:29:10.664Z
---

**If grep, `git ls-files`, or a few lines of Python can produce it, do not write it down.** A
stored count or list is a second copy of a fact, and every change to the real thing now has to
be mirrored into it by hand or it goes stale and lies.

The user (Mike) framed it: *"don't make work by counting and listing things that can be found with
simple grep, python techniques, because we're making work by always maintaining the count — it's
part of the stay DRY."*

**Sizes are the worst case, because they read as helpful.** "a 287-line how-to", "roughly 1,200
lines of reading", "the contract, 101 lines", "a 619-line Sphinx page". Every one of these is
`wc -l` frozen into prose, wrong the next time the file is edited, and useless to the reader
while it is right — nobody decides anything differently because a document is 287 lines. Written
2026-08-12, immediately after writing this memory: I cited a how-to as 283 lines, discovered it
was 287, and *corrected the number* instead of deleting it.

**A document must not tally its own contents.** "Eight findings, all fixed", "Drawing them found
four things", "Findings 7 and 8 above", "How findings 1 to 4 were fixed", "the three `study-`
renders", "Run 2's two renders" — every one of these has to be edited the moment the document grows,
and editing it is not progress. The user (Mike), 2026-08-12, after watching it happen through three
successive commits: *"You keep on counting things, that don't need to be counted, and then editing
the counts. I need you to stop doing that!"*

The replacements are always available and always shorter: *"Every finding below is fixed"*,
*"the findings above say which ones came this way"*, *"the `study-` renders"*. Numbered headings
already carry the count for anyone who wants it.

This is the general rule behind the specific ones already recorded: no counts on drawings
(see [[drawing-conventions]]), and never restate a fact another file enforces
(see [[one-fact-one-home]]).

**How to apply:**

- Prefer a pointer and the command over the answer: say where the parts are and how to count
  them, not "eight parts, fourteen instances".
- Enumerations of structure go stale fastest — a list of a file's sections needs editing every
  time the structure changes.
- This governs replies to the user too. Producing an inventory nobody asked for is the same
  work-making, and it costs context on both sides.
- It does not forbid a measured number that came from an actual measurement and is cited as
  evidence. A cavity volume of 109.48 mm³ is a finding. "Six unique parts" is a count.
