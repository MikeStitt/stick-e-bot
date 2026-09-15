---
name: read-think-plan-do
description:
  "The working cycle the user (Mike) expects by default — Read, Think, Plan, Do, then check it
  worked. Run it without being asked."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-12T22:52:04.763Z
---

**Read → Think → Plan → Do → Did it work?** Run this automatically. In autonomous mode it is
the default shape of work, not a thing to propose or ask permission for.

**Read** is four things, and it is the step that gets skipped:

1. **Read** the files the task names.
2. **Investigate** — look at the thing itself, not only what is written about it.
3. **Research our requirements and specs.** The settled specification is an input to the work,
   not a thing to check afterwards.
4. **What happened last time.** Previous runs, previous sessions, the conversation log. A
   decision can be settled and live in no single file.

**Did it work?** closes the loop. Building the thing is not the same as checking it, and a
check you did not perform is not a check.

**Why:** the failure this came out of, 2026-08-12 — three agents were launched against briefs
written without reading the settled spec, and the briefs invented numbers that contradicted a
decision made the previous day in conversation. Every one of the four Read sub-steps would have
caught it on its own.

**How to apply:** the same cycle governs directing a subagent as governs doing the work by
hand. Writing a brief or a launch prompt is Do; it needs its own Read and Think first, and its
own "did it work" after. See [[limbs-are-twelve-mm-cylinders]] for the specific decision that
was missed, and [[derive-dont-maintain]] for what not to produce along the way.
