# Magnetic Matter Movers Build Sheet 002 — The Smallest Beamed-Thermal Rocket
### A water droplet, levitated on sound, propelled by light
*Phase 0 of the launch-architecture ladder. Same physics as the flight vehicle with zero substitutions: dumb mass + energy at the point of use + steam thrust. Also the strangest catalog piece.*

---

## 1. What This Is

A ~2 mm dyed-water droplet floats in an acoustic levitation trap (TinyLev, the open-source cousin of Bristol's MATD). A laser fired **horizontally** at the droplet evaporates its lit side; the departing vapor's momentum recoils the droplet **away from the beam** — vapor-recoil propulsion, the identical mechanism as the launch vehicle's heat-exchanger stage. The trap doubles as the instrument: it's a spring, so the droplet's displacement from the trap node is a direct thrust readout. A microthrust balance on a desk.

**Two facts that make it more than a toy:**
- At 500 mW absorbed, thrust exceeds droplet weight (**T/W = 1.2**) — the droplet could hover on its own steam
- Demo flux is 30–160 kW/m² vs. the flight panel's 48 MW/m² — same mechanism, 1,000× below flight conditions

## 2. Predicted Performance (validate against these)

2 mm droplet: 4.2 mg, weight 41 μN. Table is **absorbed** power; india-ink-dyed water absorbs ~50–80% of incident, so incident laser power runs ~1.5–2× these values.

| Absorbed | Flux on droplet | Evap rate | Droplet life | Thrust | T/W | Trap displacement* |
|---|---|---|---|---|---|---|
| 5 mW | 1.6 kW/m² | 2.2 μg/s | ~30 min | 0.5 μN | 0.01 | 0.05–0.5 mm (camera only) |
| 50 mW | 16 kW/m² | 22 μg/s | ~3 min | 5.0 μN | 0.12 | 0.5–5 mm |
| 100 mW | 32 kW/m² | 44 μg/s | ~95 s | 10 μN | 0.24 | 1–10 mm (naked eye) |
| 500 mW | 159 kW/m² | 0.22 mg/s | ~19 s | 50 μN | 1.21 | ejection likely |

*TinyLev-class trap stiffness ≈ 1–10 μN/mm; calibrate yours in §7 step 2.

**Predicted dynamics to look for:** (a) steady offset along the beam axis at low power; (b) at higher power, a **limit-cycle flicker** — pushed off-beam → thrust dies → spring pulls it back into the beam → pushed again (beam-riding oscillation, a real flight-control phenomenon); (c) the endgame — as the droplet evaporates, T/W rises and it gets livelier before vanishing.

## 3. Bill of Materials (~$150)

| Item | Spec | Est. |
|---|---|---|
| TinyLev acoustic levitator | open-source design: 72× 16 mm 40 kHz transducers, Arduino Nano, L298N driver, 3D-printed frame — kit or self-build | $70 |
| Laser module — starter | ≤5 mW, 650 nm red, Class 3R, dot focusable | $10 |
| Laser module — main | 100–500 mW, 445–450 nm, adjustable focus, TTL/PWM power control | $30 |
| **Safety goggles** | **OD 4+ at 445–455 nm, CE/ANSI rated — for every person in the room** | $30 |
| Enclosure | cardboard/foamcore box, matte-black interior; black felt beam dump | $10 |
| Droplet handling | 1 mL syringe + blunt 25 ga needle | $5 |
| Dye | india ink (best) or black food coloring | $3 |
| Camera | phone with macro/slow-mo on a small tripod, mm-grid card behind trap | on hand |
| Power meter (optional) | cheap laser power meter for absorbed-power calibration | $25 |
| Photodiode (optional) | any photodiode + resistor into a multimeter/scope, aimed at the droplet from the side — backscatter is a second data channel (evaporation events show as scatter flickers) | $2 |

## 4. Safety — read before powering anything

**Laser (the real hazard):**
- 100+ mW at 450 nm is **Class 3B: a stray reflection causes permanent eye damage faster than you can blink.** The droplet is a spherical mirror that sprays specular reflections in ALL directions.
- Non-negotiables: rated goggles on before power on; beam path fully inside the enclosure; beam terminates in the dump; remove watches/rings; beam horizontal at desk height never at face height; key/switch control so it can't power on by accident.
- **Graduation rule: run the entire §7 protocol at ≤5 mW red first.** Camera-tracked displacement at 0.5 μN is a complete, publishable measurement. Move to Class 3B only after the low-power protocol is routine.

**Ultrasound:** TinyLev runs high-intensity 40 kHz — inaudible to you, unpleasant for pets (cats hear well past 40 kHz). Keep animals out of the room; keep fingers out of the trap while loading (tingling is normal, prolonged exposure isn't).

## 5. Build Sequence

1. Assemble TinyLev per the open-source guide; verify all transducers phase-matched (the guide's oscilloscope or buzz test). Confirm it traps a 1–2 mm foam bead rock-solid before ever trying liquid.
2. Mount trap inside the enclosure, mm-grid card behind the trap axis, camera port on one side, laser port on the adjacent side so the beam runs **horizontal**, through a trap node, into the felt dump.
3. Rigidly mount the starter (red, ≤5 mW) laser; align to the node using a trapped foam bead as the target. Lock it down.
4. Mix dye: ~1 drop india ink per mL water. Darker = more absorption = more thrust per incident mW.

## 6. Droplet Loading (the finicky part)

1. Trap a foam bead first to confirm the trap is live; remove it.
2. Draw dyed water; touch a small hanging drop from the needle tip *slowly* into a pressure node — the trap will pluck it off. Start small (~1 mm); oversized droplets flatten, wobble, and atomize.
3. If droplets keep bursting: smaller droplet, or reduce drive amplitude slightly. Stable droplets sit still, slightly oblate.

## 7. Measurement Protocol

1. **Baseline:** trapped droplet, laser off. Record 30 s. Note rest position on the grid.
2. **Calibrate trap stiffness:** tilt the whole enclosure by a measured small angle θ; the droplet's weight component mg·sinθ is a known force; its displacement gives k (μN/mm). Two or three angles → a line.
3. **Thrust runs:** laser on at fixed power, record until steady offset (or oscillation), laser off, watch it snap back. Repeat at 3–5 power levels. Slow-mo the higher-power runs.
4. **Reduce:** displacement × k = thrust. Plot thrust vs. incident power — prediction is a straight line whose slope gives your absorbed fraction. Photograph the droplet diameter each run (shrinkage → evaporation rate → cross-check via the table).
5. **The money shots:** (a) horizontal displacement with beam horizontal — proof it's recoil, not convection (convection pushes up, recoil pushes along the beam); (b) the snap-back on laser-off; (c) the limit-cycle flicker if you find its power threshold.
6. **Beam-riding offset map (imported from the 28 GHz gyrotron program's misalignment studies):** at fixed power, park the beam deliberately off the droplet's rest position in ~0.5 mm steps (laser on a micrometer stage or shim the mount). Record steady-state displacement at each offset → force-vs-offset curve. This is the bench-scale version of published beam-riding stability data: it tells you whether an off-axis vehicle gets pushed back toward the beam (self-centering) or shoved further out (divergent) — the core control question for any beamed-flight system. If the photodiode is fitted, log its channel too; scatter amplitude vs. offset is your transmitter-as-sensor demonstration.

## 8. Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| Nothing happens | Undyed/underdyed water — beam passes through | More ink |
| Droplet atomizes on laser-on | Boiling onset / trap drive too hot | Lower power; smaller droplet; reduce drive |
| Droplet drifts without laser | Room air currents | Enclosure sealed; let it settle 60 s |
| Displacement vertical not horizontal | You're seeing convection or beam misaligned above/below node | Re-align beam through node center |
| Droplet ejects at high power | T/W approaching 1 — working as designed | Celebrate, then lower power for data runs |

## 9. Where This Goes

- **Lab note 001:** thrust-vs-power curve + the horizontal-displacement proof = the first Magnetic Matter Movers publication, and the cheapest credible evidence of the architecture's core mechanism
- **v2:** swap dyed water for a black-anodized aluminum micro-panel with a wet face — a heat-exchanger *shape* instead of a bare droplet; measure thrust vs. panel angle
- **Catalog piece:** enclosure with a window, one-button run, the two curves printed on the base — *"the smallest beamed-thermal rocket in existence"*

*Companion documents: Build Sheet 001 (Inductrack, Phase 0); Space Transportation Architecture (§Demonstration Ladder, §Technology Risk Register — heat exchanger).*
