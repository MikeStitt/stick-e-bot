# Phase A — the first geometry feature that reads each variable

Written by [`../scripts/a_variable_readers.py`](../scripts/a_variable_readers.py) on
2026-09-18, from the parents' records. **Goes above** is where the variable is typed in
draft9p5's tree: immediately before that feature. A variable with no reader is one
nothing in the tab uses.

## `robot sizes`

23 features, 23 of them variables. Read from `.docs/experiments/runs/2026-09-08-draft9p4/reference/robot-sizes.features.json`.

**A Variable Studio holds no geometry**, so no row here has a first reader in
its own tab. Every reader is in another tab, and the order of the rows is the
order the studio lists them in. draft9p4 walked these rows once; this table is
the declaration order, and which tab reads each row is that walk's answer.

| Variable | Declared at | First geometry reader | Goes above |
| -------- | ----------: | --------------------- | ---------- |
| `#torsoH` | 0 | nothing reads it | — |
| `#torsoW` | 1 | nothing reads it | — |
| `#torsoD` | 2 | nothing reads it | — |
| `#limbCenter` | 3 | nothing reads it | — |
| `#wall` | 4 | nothing reads it | — |
| `#ball` | 5 | nothing reads it | — |
| `#stand` | 6 | nothing reads it | — |
| `#collar` | 7 | nothing reads it | — |
| `#fit` | 8 | nothing reads it | — |
| `#ballLoss` | 9 | nothing reads it | — |
| `#t_print` | 10 | nothing reads it | — |
| `#grip` | 11 | nothing reads it | — |
| `#limbD` | 12 | nothing reads it | — |
| `#blade` | 13 | nothing reads it | — |
| `#wedge_h` | 14 | nothing reads it | — |
| `#wedge_c` | 15 | nothing reads it | — |
| `#gap` | 16 | nothing reads it | — |
| `#seat` | 17 | nothing reads it | — |
| `#blade_out` | 18 | nothing reads it | — |
| `#slot_deep` | 19 | nothing reads it | — |
| `#tab_free` | 20 | nothing reads it | — |
| `#ear_free` | 21 | nothing reads it | — |
| `#flat` | 22 | nothing reads it | — |

**Read by nothing in this tab:** `#ball`, `#ballLoss`, `#blade`, `#blade_out`, `#collar`, `#ear_free`, `#fit`, `#flat`, `#gap`, `#grip`, `#limbCenter`, `#limbD`, `#seat`, `#slot_deep`, `#stand`, `#t_print`, `#tab_free`, `#torsoD`, `#torsoH`, `#torsoW`, `#wall`, `#wedge_c`, `#wedge_h`.

## `ball and socket`

14 features, 5 of them variables. Read from `.docs/experiments/runs/2026-09-08-draft9p4/reference/ball-and-socket.features.json`.

| Variable | Declared at | First geometry reader | Goes above |
| -------- | ----------: | --------------------- | ---------- |
| `#stalk` | 0 | 5 `stud profile` | `stud profile` |
| `#slit` | 1 | 10 `slit profile` | `slit profile` |
| `#slit_in` | 2 | 10 `slit profile` | `slit profile` |
| `#slit_d` | 3 | 11 `relief slits` | `relief slits` |
| `#slit_out` | 4 | 10 `slit profile` | `slit profile` |

## `hinge`

46 features, 18 of them variables. Read from `.docs/experiments/runs/2026-09-08-draft9p4/reference/hinge.features.json`.

| Variable | Declared at | First geometry reader | Goes above |
| -------- | ----------: | --------------------- | ---------- |
| `#nose` | 0 | 18 `blade profile` | `blade profile` |
| `#ear` | 1 | nothing reads it | — |
| `#stub` | 2 | 20 `stub axle outline` | `stub axle outline` |
| `#stub_proud` | 3 | 21 `stub axle` | `stub axle` |
| `#bore_d` | 4 | 35 `pocket axle sketch` | `pocket axle sketch` |
| `#leaf_root` | 5 | 29 `relief slit outline` | `relief slit outline` |
| `#leaf_tip` | 6 | 29 `relief slit outline` | `relief slit outline` |
| `#slit_h` | 7 | 29 `relief slit outline` | `relief slit outline` |
| `#rod_blade` | 8 | 28 `blade arm` | `blade arm` |
| `#rod_fork` | 9 | 42 `fork arm` | `fork arm` |
| `#wedges` | 10 | 22 `blade wedge outline` | `blade wedge outline` |
| `#ring_in` | 11 | 22 `blade wedge outline` | `blade wedge outline` |
| `#ring_out` | 12 | 22 `blade wedge outline` | `blade wedge outline` |
| `#wedge_bind` | 13 | 22 `blade wedge outline` | `blade wedge outline` |
| `#wedge_inset` | 14 | 22 `blade wedge outline` | `blade wedge outline` |
| `#wedge_eps` | 15 | 22 `blade wedge outline` | `blade wedge outline` |
| `#wedge_w` | 16 | 22 `blade wedge outline` | `blade wedge outline` |
| `#backlash` | 17 | nothing reads it | — |

**Read by nothing in this tab:** `#backlash`, `#ear`.

## `body`

33 features, 8 of them variables. Read from `.docs/experiments/runs/2026-08-29-draft9p3/reference/body.features.json`.

| Variable | Declared at | First geometry reader | Goes above |
| -------- | ----------: | --------------------- | ---------- |
| `#hip_half` | 2 | 18 `hip connector location` | `hip connector location` |
| `#shoulder_half` | 3 | 10 `pivot lines` | `pivot lines` |
| `#shoulder_drop` | 4 | 10 `pivot lines` | `pivot lines` |
| `#shoulder_len` | 5 | 12 `torso shoulder profile` | `torso shoulder profile` |
| `#boss_len` | 6 | 12 `torso shoulder profile` | `torso shoulder profile` |
| `#boss_d` | 7 | 12 `torso shoulder profile` | `torso shoulder profile` |
| `#tilt` | 8 | 12 `torso shoulder profile` | `torso shoulder profile` |
| `#yaw` | 9 | 11 `plane for shoulder` | `plane for shoulder` |

## `head`

26 features, 12 of them variables. Read from `.docs/experiments/runs/2026-08-29-draft9p3/reference/head.features.json`.

| Variable | Declared at | First geometry reader | Goes above |
| -------- | ----------: | --------------------- | ---------- |
| `#headW` | 0 | 12 `head profile` | `head profile` |
| `#headD` | 1 | 13 `head body` | `head body` |
| `#eyeX` | 2 | 16 `eye profile` | `eye profile` |
| `#eyeUp` | 3 | 16 `eye profile` | `eye profile` |
| `#eyeRx` | 4 | 16 `eye profile` | `eye profile` |
| `#eyeRy` | 5 | 16 `eye profile` | `eye profile` |
| `#face` | 6 | 17 `eye` | `eye` |
| `#mouthW` | 7 | 19 `mouth profile` | `mouth profile` |
| `#mouthH` | 8 | 19 `mouth profile` | `mouth profile` |
| `#mouthDn` | 9 | 19 `mouth profile` | `mouth profile` |
| `#chamfer` | 10 | 15 `lower head chamfer` | `lower head chamfer` |
| `#round` | 11 | 14 `upper rounds` | `upper rounds` |

## `foot`

24 features, 13 of them variables. Read from `.docs/experiments/runs/2026-08-29-draft9p3/reference/foot.features.json`.

| Variable | Declared at | First geometry reader | Goes above |
| -------- | ----------: | --------------------- | ---------- |
| `#foot_l` | 0 | 15 `foot outline` | `foot outline` |
| `#foot_w` | 1 | 15 `foot outline` | `foot outline` |
| `#ankle_h` | 2 | 16 `foot` | `foot` |
| `#plate` | 3 | 11 `foot pedestal` | `foot pedestal` |
| `#top_round` | 4 | 17 `top round` | `top round` |
| `#collar_r` | 5 | 10 `pedestal outline` | `pedestal outline` |
| `#collar_down` | 6 | 11 `foot pedestal` | `foot pedestal` |
| `#pedestal` | 7 | 11 `foot pedestal` | `foot pedestal` |
| `#rib_w` | 8 | 18 `groove profile` | `groove profile` |
| `#rib_d` | 9 | 19 `sole groove` | `sole groove` |
| `#heel_r` | 12 | 15 `foot outline` | `foot outline` |
| `#toe_r` | 13 | 15 `foot outline` | `foot outline` |
| `#heel_y` | 14 | 15 `foot outline` | `foot outline` |

## `u limb`

9 features, 0 of them variables. Read from `.docs/experiments/runs/2026-09-08-draft9p4/reference/u-limb.features.json`.

No variables are declared in this tab.

## `l limb`

9 features, 0 of them variables. Read from `.docs/experiments/runs/2026-09-08-draft9p4/reference/l-limb.features.json`.

No variables are declared in this tab.

## `gripper`

15 features, 8 of them variables. Read from `.docs/experiments/runs/2026-08-29-draft9p3/reference/gripper.features.json`.

| Variable | Declared at | First geometry reader | Goes above |
| -------- | ----------: | --------------------- | ---------- |
| `#gripperL` | 0 | 9 `clip profile` | `clip profile` |
| `#clipR` | 1 | 9 `clip profile` | `clip profile` |
| `#barD` | 2 | 9 `clip profile` | `clip profile` |
| `#bore` | 3 | 9 `clip profile` | `clip profile` |
| `#mouth` | 4 | 9 `clip profile` | `clip profile` |
| `#ball` | 5 | 9 `clip profile` | `clip profile` |
| `#wall` | 6 | 9 `clip profile` | `clip profile` |
| `#collarR` | 7 | 9 `clip profile` | `clip profile` |

