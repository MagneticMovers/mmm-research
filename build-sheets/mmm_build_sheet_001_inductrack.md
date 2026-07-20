# Magnetic Matter Movers Build Sheet 001 — Inductrack Levitation Demo
### Halbach cart over a spinning aluminum track
*Phase 0 of the launch-architecture ladder: a working scale model of System B's maglev-track levitation physics. Also a catalog piece.*

---

## 1. What This Is

A passive magnetic levitation demo: a small cart carrying a Halbach array of permanent magnets floats above a spinning aluminum surface with **no power to the cart, no control system, no superconductors**. Motion induces eddy currents in the aluminum; the currents repel the array. This is Post's Inductrack — the levitation layer of the maglev launch sled — at desk scale.

**Two build variants:**
- **Variant A — Bike wheel (recommended first build):** vertical aluminum-rim bicycle wheel, cart hovers at the apex. Cheapest, fastest, classic.
- **Variant B — Machined drum:** 30 cm aluminum drum, ≥3 mm wall, horizontal axis. More lift, better product photography, more machining.

## 2. Expected Performance (set your instruments to these)

| Parameter | Variant A (rim ~1.5 mm eff.) | Variant B (drum 4 mm) |
|---|---|---|
| Characteristic speed w | ~30 m/s | ~11 m/s |
| Levitation onset | ~60 RPM (700c wheel) | ~54 RPM |
| Visible hover gap @ 1,000–1,500 RPM | 3–8 mm | 8–15 mm |
| Drag power (constant with speed!) | ~30–60 W | ~28 W |
| Cart mass budget | ≤250 g | ≤250 g |

The flat drag-power curve is the launch-relevant physics: magnetic drag *force* falls as speed rises (L/D ≈ v/w). Measure it — it's the demo's party trick and the sales copy.

## 3. Bill of Materials (~$80–120)

| Item | Spec | Source | Est. |
|---|---|---|---|
| Magnets ×10 (8 + 2 spares) | ½" N42 cubes (e.g. K&J B888) | K&J Magnetics / Applied Magnets | $35 |
| Track | Alloy-rim 700c bike wheel w/ axle **(A)** or 12" OD 6061 tube, 4 mm wall **(B)** | used bike shop / metal supplier | $15–60 |
| Motor + speed control | 775-class DC or brushless + ESC, ≥50 W, PWM throttle | hobby | $25 |
| Drive | O-ring / belt friction drive to tire or drum edge | hardware | $5 |
| Cart body + magnet jig | PLA, ~100 g | 3D print | $3 |
| Epoxy | JB Weld or Loctite E-120HP | hardware | $6 |
| Guide rails | 2× smooth rod or aluminum angle + PTFE tape | hardware | $8 |
| Frame | 2×4 lumber or 2020 extrusion, bearing blocks | on hand | — |
| Instruments | feeler gauges (gap), phone tachometer app (RPM), clamp meter (motor W) | — | — |

## 4. Halbach Layout — THE CRITICAL DIAGRAM

Eight cubes, magnetization rotating **90° per cube**, two full wavelengths (λ = 50.8 mm). Arrows show the direction each cube's **north pole points**. TRACK SIDE IS DOWN.

```
 cube #:    1     2     3     4     5     6     7     8
 N points:  ↓     →     ↑     ←     ↓     →     ↑     ←
            (↓ = toward track, → = direction of track surface motion)

 STRONG side (field concentrated):  BOTTOM (track side)
 WEAK side (field canceled):        TOP (cart side)
```

**Verify before gluing:** hold the assembled clamped array over a steel washer — the strong face snaps it hard, the weak face barely holds it. If it's backwards, your cart will do nothing. Mark cube tops with paint dots (Magnetic Matter Movers pole code: red = N-out face, blue = S-out face) *before* assembly while polarity is easy to test.

## 5. Assembly Jig (print this first)

Halbach neighbors **repel and twist** — cubes want to flip 180°. Never assemble by hand-holding.

- Print an open-top channel: 12.9 mm inner width (½" + 0.2 mm), 110 mm long, 3 mm walls, with an **M4 clamp screw boss at one end** and a sliding pusher block.
- Insert cube 1, orient per diagram, seat against the fixed end.
- Butter the mating face of cube 2 with epoxy, insert with **fingers off — use the pusher block**; it will fight you sideways. Clamp screw snug.
- Repeat through cube 8. Keep the screw loaded until full cure (24 h for JB Weld).
- The cured stick epoxies into the cart body, strong face flush with the cart underside.

**Pinch warning:** two ½" N42 cubes can blood-blister a fingertip and shatter each other on impact. Work over a towel, one cube out of the shipping stack at a time, keep the stack a meter away from the jig.

## 6. Build Sequence

1. Print jig + cart. Test-fit one magnet dry.
2. Polarity-mark all 10 cubes (dot code). Set 2 aside as spares.
3. Assemble array in jig per §4–5. Cure fully.
4. Mount wheel/drum on frame, motor friction-drive on edge. Confirm smooth spin to 1,500 RPM **with a plywood guard covering the lower half**.
5. Mount guide rails so the cart can rise/fall ~25 mm vertically above the apex but not translate sideways. PTFE tape the contact lines.
6. Epoxy array into cart, add ballast tray (target 250 g total — tune later).

## 7. Test Procedure

1. Cart resting on apex (or on 2 mm shims), rails engaged. Guard on.
2. Spin up slowly. Log: RPM at first motion, RPM at clean liftoff, gap (feeler gauges between passes) at 500 / 1,000 / 1,500 RPM, motor watts at each point.
3. Expected signatures: liftoff near table values in §2; gap grows then **plateaus** with RPM; motor power ≈ flat once levitating. Plot gap-vs-RPM and W-vs-RPM — those two curves are the physics content of the catalog page and the first Magnetic Matter Movers lab note.
4. Tune: more ballast → smaller gap; if the cart oscillates vertically, add 20–50 g (raises the magnetic spring's damping ratio via smaller gap).

## 8. Known Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| No lift at any RPM | Array glued weak-side-down | Rebuild (spares exist for a reason) |
| Cart slams sideways | No lateral constraint — Inductrack gives lift+drag only | Rails per §6; or V-groove the drum (Variant B) |
| Cart creeps in spin direction and jams | That's the drag force working | Angle rails 2–3° or add a soft end-stop |
| Violent buzz at high RPM | Rim runout / unbalanced wheel | True the wheel; stay ≤1,500 RPM |
| One magnet pops out of array | Under-epoxied joint fighting torque | Re-glue; clamp harder next time |

**Hard limit: 1,500 RPM.** The demo is fully expressive by 1,200; rim energy above that buys risk, not physics.

## 9. Where This Goes (v2 hooks)

- **Null-flux ladder track:** replace the solid surface with shorted litz-wire loops — higher L/D, the real launch-track topology (open work item for a future sheet)
- **Linear motor propulsion:** drive the cart itself with sequenced coils — the cart's Halbach array is already the rotor of a linear synchronous motor
- **Catalog packaging:** acrylic case, red/blue pole graphics, the two measured curves silk-screened on the base — "a scale model of a launch system, and it proves it every time you spin it"

*Companion document: Magnetic Matter Movers Space Transportation Architecture (System B, §Demonstration Ladder Phase 0).*
