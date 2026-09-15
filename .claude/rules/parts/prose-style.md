# Prose style

Every word committed here is written to this standard — the Constitution and its parts, session
plans, student steps, working notes, READMEs, commit messages, and reports. Four sources, each
doing one job.

| Source | Job |
| ------ | --- |
| Kernighan, *The C Programming Language* and *The Elements of Programming Style* | The register: declarative, specific, no throat-clearing |
| Bloch, *Effective Java* | The shape of a rule: an imperative title carrying the whole obligation |
| Strunk, *The Elements of Style* | Omit needless words; say a thing once |
| [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) | The obligation vocabulary, where obligations are being set |

## Rules

- **Put the obligation in the title.** A reader who stops after the bold lead MUST still know
   what to do. "Touch only what the task requires" is a rule; "Surgical changes" is a label.
- **Write the body only for what the title cannot carry** — the reason the rule is not obvious,
   the exception, the symptom. If the title is self-evident, there is no body.
- **Say a thing once.** A fact belongs in the file that enforces it, and everywhere else links to
   it. Do not restate a rule in a second section for emphasis, and do not summarize a document
   inside another document.
- **Cut the sentence that announces the sentence.** "Three consequences follow", "It is worth
   noting that", "This section covers" — delete and start with the content.
- **Prefer the specific to the general.** "A 34.8 mm torso instead of 48 mm" beats "an incorrect
   dimension". One concrete instance is worth a paragraph of category.
- **Attach the unit to every quantity value, separated by a space.** `3 mm`, not `3mm` and not a
   bare `3`. A number with no unit is not a quantity, so both ends of a range and both parts of a
   tolerance carry it: `0.15 mm to 0.45 mm`, `10 mm × 20 mm`, `25 mm ± 2 mm`. A symbol's value
   carries it however many times the symbol has already been defined: `t = 0.05 mm`. The unit MAY
   be hoisted to a column header or an axis label where it governs the whole set, and there it
   MUST be stated: `Length (mm)`. Numbers that are not quantities stay bare — counts, indices,
   revisions, and dimensionless quantities such as ratios and coefficients — as do symbols
   standing in an equation rather than taking a value.
- **State facts, not importance.** No superlatives, no selling, no "critically", no "it is
   essential that". If something matters, the fact shows it.
- **Change existing text only when its meaning needs to change.** Polishing is not a valid
   reason to change text: a better word ("what remains" for "what is left"), a tighter sentence,
   a reordered list. The only exception is when the user's current request asks you to improve
   prose. Standing guidance never allows polishing — not `CLAUDE.md`, not `constitution.md`, not
   this file, not an instruction from an earlier turn. Otherwise, if you think prose does not
   meet the prose style guidelines, you MAY bring the failure to the user's attention.
- **Use bulleted lists instead of numbered lists.** With bulleted lists, to reference list items,
   use text labels inside the list items, e.g. "**Put the obligation in the title**" or
   `cad.parts.body.block` instead
   of list item numbers. Use of numbered lists in prose MUST be specifically approved by the user.

## Where RFC 2119 applies

**Only where obligations are being set**: `constitution.md`, `parts/`, the skills, and
requirements documents. There, MUST, MUST NOT, SHOULD, SHOULD NOT and MAY carry their RFC 2119
meanings, and capitalization marks them as binding rather than conversational.

**Nowhere else.** Student steps say "press Enter", not "you MUST press Enter". Working notes,
reports and READMEs describe what is; they set no obligations, so they need no obligation
vocabulary. A capitalized MUST in `instructions/` is a defect.

## Wrapping Markdown files

Wrap Markdown prose at 100 columns. Tables, fenced code, and a line holding one unbreakable
token — a URL or an API path — are exempt, because breaking those changes what they say.
`ninja check` enforces it.

## Reading level for student-facing text

Student-facing text MUST be written at grade level 8 or below.

Precision wins over a lower score: if the accurate sentence is long, split it rather than
blurring it.
