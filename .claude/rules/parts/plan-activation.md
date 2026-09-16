# Plan activation

How a plan becomes the active one and how it stops being active. Nothing here is about the
constitution: the contract binds the work whether or not a plan is active.

## Point `active-plan.md` at the plan before doing any of its work

[`../active-plan.md`](../active-plan.md) holds one `@` import naming the plan, and nothing else.
Writing that import is the first step of executing a plan, ahead of any reading, building or
capture.

A rules file is injected from disk on every request, so the plan it imports arrives with every
request and survives compaction. A file merely re-read comes back as a bare path once it passes
roughly 5,000 tokens, and a run plan is larger than that.

## Exactly one plan is active

Pointing at a new plan replaces the import. It MUST NOT add a second one.

## Confirm the import resolved

A broken `@` import is silent: the line arrives unexpanded, with no error and no placeholder. After
pointing the file at a plan, read the plan's own text back out of the injected instructions rather
than assuming it arrived.

## A plan stops being active only when Mike and Claude agree it has

Finishing the last step is not deactivation; saying so is. Until then the plan is still active and
the work is still governed by it.

## Empty `active-plan.md` on deactivation

An emptied pointer is the record that nothing is active. A stale pointer puts finished work back
into every request after every compaction, and nothing in the injected text marks it as finished.
