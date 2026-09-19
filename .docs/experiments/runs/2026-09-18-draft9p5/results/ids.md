# The ids of stickbot-draft9p5

Written by Phase A0 on 2026-09-18. The machine-readable copy, as Onshape returned it, is
[`elements.json`](elements.json).

## The document

| Field | Value |
| ----- | ----- |
| name | `stickbot-draft9p5` |
| document id | `2f08b54d795df0ee6b72e321` |
| workspace | `Main`, `1d8e4c837228c90bab9ff062` |
| live workspace | <https://cad.onshape.com/documents/2f08b54d795df0ee6b72e321/w/1d8e4c837228c90bab9ff062> |
| workspace length unit | millimeter, display decimals `0.12345` |
| published version | none yet |

## The ten tabs, in Phase B's build order

| Order | Tab | Type | Element id |
| ----: | --- | ---- | ---------- |
| 1 | `robot sizes` | Variable Studio | `3d67f51a630c05c2b5d0b9ea` |
| 2 | `ball and socket` | Part Studio | `1a8322899842a1934e85851d` |
| 3 | `hinge` | Part Studio | `db0ef2ae9777492e7b242acf` |
| 4 | `body` | Part Studio | `5441067befc71f1e3b91482e` |
| 5 | `head` | Part Studio | `303898bd4ba38fc3957b0a21` |
| 6 | `foot` | Part Studio | `229aa0900e5a7e7aa4768c6f` |
| 7 | `u limb` | Part Studio | `fc89b8128993be73a0c9f092` |
| 8 | `l limb` | Part Studio | `be3bd8b485e32946c24ed799` |
| 9 | `gripper` | Part Studio | `a3a4fac68ffb7372a7803003` |
| 10 | `stickbot` | Assembly | `c81b630354bd0739d788a42d` |

The Assembly brings a Bill of Materials element with it, `cc25ef6cbcdced6c0877d72b`, which is not
one of the ten tabs and is left alone.

**The Assembly's element id changed on 2026-09-18, and so did the Bill of Materials' with it.**
The first assembly, `599b6d255571795de9383404`, would not delete its mates reliably by id and
ended up holding twenty-six mates made from thirteen; it was deleted and rebuilt, which is a new
element and a new id. The ids above are the live ones, read back from
`/api/documents/d/{did}/w/{wid}/elements` on 2026-09-19. The old id answers `Element not found.`
and [`../register.md`](../register.md) says how the duplicate mates arose.

## A second document of the same name, trashed

`9b398e076ce2ea8a25710938` was created by the same script minutes later and is in the trash, with
`trash: true` and `trashedAt` `2026-09-18T20:06:43Z` read back from Onshape. Nothing was built in
it. [`../register.md`](../register.md) says how it came to exist.
