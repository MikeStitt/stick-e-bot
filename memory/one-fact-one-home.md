---
name: one-fact-one-home
description:
  "Never restate in one file a fact another file already enforces; state it where it is enforced
  and link."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-12T17:08:56.896Z
---

Do not write a fact into a document when another document already establishes and enforces it.
`constitution.md` line 11 said "This file is the **always-read core**: the Working Rules below plus
the Quality Gates, the Branch Policy and Governance" — but `CLAUDE.md` is what actually enforces the
always-read ritual. The Constitution was restating someone else's rule.

**Why:** the duplicate costs three ways. Tokens, because it is re-read every session. People's time,
because they read the same thing twice. Maintenance, because a restatement that enumerates goes
stale — that sentence had to be edited when the Governance section was added, and the enumeration
was already missing two of the file's seven sections.

**How to apply:** before adding a sentence, ask which file *enforces* the thing. Put it there, once,
and link to it from anywhere else that needs it. This applies to the same fact appearing in two
documents, not to a pointer — `CLAUDE.md` pointing at `constitution.md` is the correct shape. Prefer
a contrast or a link over an enumeration of sections, since enumerations need editing whenever the
structure changes. See [[instructions-state-facts-not-importance]] for the related rule about text
that adds no fact at all.
