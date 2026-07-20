# Matter Stack — Execution Checklist & Gate Criteria
### Buy → Build → Measure → Prove → Unlock the next stage
*Companion to the Matter Stack Compendium (Parts I–VII). Same rules as the Magnetic Matter Movers Phase 0 checklist: print it, fill it in ink, photograph the filled pages + videos as your gate evidence. Unexplained deviation fails a gate; explained deviation is data.*

**Shared-hardware note:** the Stage 1 acoustic layer IS the TinyLev from Magnetic Matter Movers Build Sheet 002 — one levitator serves both projects. Buy once; the polarity-test discipline here is the same skill as Halbach polarity marking in Build Sheet 001. These projects train each other.

---

## Stage 1 — The 4×4 Base Build (~$332, 3–5 weekends)

### 1.1 Purchase
☐ Makerfabs Acoustic Levitator kit ($70) — or scratch parts per Compendium §6.1
☐ 16× 12 V electromagnets 25 mm ($64) · 16× IRLZ44N MOSFET modules ($18) · 1N5819 diodes 100-pk ($7)
☐ Arduino Mega clone ($18) · 12 V 10 A PSU ($16)
☐ Ferrotec EFH-1 50 ml ($30) · glass cell + lid ($10) · distilled water + salt
☐ Polystyrene beads 1–3 mm · teabag paper/mesh scoop · perfboard/terminals/18 AWG ($14)
☐ Gloves + plastic sheeting ($8) · mini projector ($60) · gantry print
☐ Verify owned: soldering iron, multimeter (mandatory), phone tripod

### 1.2 Build A — Acoustic (order matters: acoustic first)
☐ Frame printed, sockets filed to snug press-fit
☐ **Polarity test EVERY transducer** (A0 + Serial Plotter); + leg paint-marked BEFORE soldering
   → Record: transducers tested ______ / inverted-marking count ______ (builders report this is common — your number is real data)
☐ Arrays populated, epoxied (not hot glue), bussed; continuity: every +→+ bus, −→− bus, no bus-to-bus short
☐ Nano flashed, L298N wired; Nano powered from USB **or** L298N 5 V — never both
☐ Optional scope check: both arrays in phase

### 1.3 Build B — Magnetic
☐ Saturated saline mixed & settled; cell filled ⅔ saline + 10–20 ml ferrofluid injected below surface; **lid sealed**
☐ Hand-magnet test through glass (spiking observed — calibrates intuition) — done gloved, over sheeting
☐ 4×4 grid mounted at ~30 mm pitch, coils labeled 1–16, leads to terminal strip
☐ **Flyback diode across every coil, stripe to + lead — count them: ______ /16 before first power-up**
☐ One MOSFET per coil; coil rail separate from Arduino rail, grounds tied at one point; rail fused
☐ Firmware duty cap set at ______ % (spec: 60–70%)

### 1.4 Stage 1 — Actual vs. Predicted

| Measurement | Predicted / spec | Actual | Dev./notes |
|---|---|---|---|
| Bead levitation duration | ≥ 5 min stable | ______ | ___ |
| Bead vertical move via phase shift | smooth, no drop | ______ | ___ |
| Levitation supply voltage | works at 6–9 V | ______ V | ___ |
| Single coil 50% duty | one smooth bump | ______ | ___ |
| Traveling bump (cross-fade demo) | full orbit, no tearing | ______ | ___ |
| **Tear-speed** (max bump travel speed) | *characterize — YOUR number becomes the spec* | ______ mm/s | — |
| Coil current, one coil full duty | 0.3–0.5 A | ______ A | ___ |
| Coil temp after 10 min @ 50% | warm, touchable | ______ | ___ |
| Two-layer milestone | bead above + bump tracking below, one host | ______ | ___ |
| Full-stack milestone | 3 layers synced from one script | ______ | ___ |

**Triage:** no levitation → re-verify polarity of suspect transducers, try smaller/irregular bead, drop voltage slightly · bead ejects → voltage down · no bump → coil polarity/wiring, cell standoff >8 mm · bump jumps instead of glides → PWM cross-fade logic, not hardware · anything dies at MOSFET switch-off → a missing flyback diode, stop and audit all 16.

**GATE S1 — pass:** ☐ 5-min levitation video ☐ traveling-bump orbit video ☐ full-stack sync video ☐ table filled, tear-speed recorded ☐ diode count photo ☐ anomaly paragraph per >50% deviation. **Unlocks Stage 2 purchasing.**

---

## Stage 2 — 8×8 Upgrade (~$392 delta, +mic & cooling)

### 2.1 Purchase
☐ 64× electromagnets ($200 — or reuse 16, save ~$46) · 64× MOSFET modules ($60) · 4× PCA9685 ($20) · extra diodes ($7)
☐ 12 V 30 A PSU ($32) + fuse · heatsinks + fans ($28) · USB mic ($25) · 16 AWG distribution ($20)

### 2.2 Build
☐ 64 coils at ~15 mm pitch; cell standoff 3–8 mm; PCA9685 addresses 0x40–0x43 jumpered, I²C chained
☐ Per-coil MOSFET + flyback retained — **diode count: ______ /64**
☐ Bus bars 16 AWG+, rail fused; fans wired to run whenever coils energized
☐ Firmware: duty cap, simultaneity cap ("max hot coils": ______), per-coil dwell limit set

### 2.3 Stage 2 — Actual vs. Predicted

| Measurement | Predicted | Actual | Dev./notes |
|---|---|---|---|
| **Separable terrain features** | 8–12 (fluid physics, not coil count, sets ceiling) | ______ | ___ |
| Re-measured tear-speed (finer grid) | differs from Stage 1 value | ______ mm/s | ___ |
| Total current, typical scene | well under 30 A fused | ______ A | ___ |
| Coil-bank temp, 30-min run w/ fans | stable, not climbing | ______ | ___ |
| Sound-reactive demo | bass→center swell, onset→bead dart | ______ | ___ |
| Existing scenes on denser grid | run unchanged (normalized coords) | ______ | ___ |

**GATE S2 — pass:** ☐ feature-count photo with count annotated ☐ 30-min thermal log ☐ sound-reactive video ☐ table filled. **Unlocks Stage 3 or the art-piece fork (a gallery-ready machine legitimately stops here at ~$724).**

---

## Stage 3 — MATD Phased Array (~$425 delta)

*Compendium warning stands: attempting this first is the most common project-killer. Entry condition: Gate S2 passed.*

☐ Flat array 64–256 transducers (Ultraino/OpenMPD route); **every transducer polarity-tested** — same discipline, larger scale
☐ Phase controller (FPGA/MCU + driver boards) brought up
☐ **Static trap first** — reproduce a stationary hover before any steering
☐ Then slow commanded moves → then fast trajectories → RGB LED sync

| Measurement | Predicted | Actual |
|---|---|---|
| Static trap with flat array | stable hover | ______ |
| Slow 3-D steering | smooth, no drops | ______ |
| Max reliable bead speed | ≤ 8.75 m/s (literature ceiling) | ______ m/s |
| POV shape (circle/line) | visible figure | ______ |
| Mid-air haptic point | felt on palm | ______ |
| Audible sound from array | recognizable tone | ______ |

**GATE S3 — pass:** ☐ static-trap video ☐ POV-figure photo (long exposure) ☐ measured max speed ☐ bead-loss/re-trap behavior noted.

---

## Stage 4 — V3 Museum Hardening (~$144 delta)

*Safety stage, not polish. Until complete, machine runs attended only.*

☐ Enclosure + security fasteners · levitator guard cage · warning signage (magnet/ultrasound)
☐ Access-panel interlock cuts coil power + levitator · hardware thermal cutoff independent of firmware
☐ E-STOP latching, one action kills coils + levitator · fused/switched IEC inlet, earth bonding, strain relief
☐ Software: attract/idle loop · bead-loss graceful recovery · 150 ms link watchdogs · daily restart

**GATE S4 — the sign-off tests (each verified to reach safe state, each its own checkbox):**
☐ Open access panel mid-show → safe state
☐ Trip thermal cutoff → safe state
☐ Hit E-STOP → safe state, latches until reset
☐ Pull Mega USB → coils drop ≤150 ms · ☐ Pull Nano USB → levitator idles
☐ Unattended soak test: ______ hours (spec: several minimum), zero interventions
**Evidence:** video of each safe-state test + soak log. **Unlocks public deployment and Stage 5.**

---

## Stage 5 — V4 Collaborative Exhibit (~$70 delta)

☐ One station wired (knob/slider→ADS1115, button debounced) → values streaming to host
☐ Calibration table per pot (min ______ / max ______ / dead-zone applied)
☐ One station → one feature confirmed (knob=height, slider=x, button=lock/reset)
☐ Stations duplicated: ______ total, each own feature + projected hue
☐ Collision handling behavior chosen (merge / repulsion) and demonstrated
☐ Fair-idle drift + no-visitors generative idle confirmed
☐ **Ensemble rehearsal: 2–3 people, tuned for responsiveness vs. calm** (the actual product test)

**GATE S5 — pass:** ☐ multi-person play video ☐ calibration table ☐ collision + idle demos. **The roadmap's destination: exhibit live.**

---

## Standing Rules (shared with the Magnetic Matter Movers ladder)
1. No stage skips — each stage's reliability is the next one's foundation.
2. Deviation with a story is data; deviation ignored fails the gate.
3. Characterized values (tear-speed, feature count) become YOUR machine's spec sheet — record them like they matter, because every scene you author obeys them.
4. Bring each gate's evidence package back for review — that conversation is the troubleshooting session.
5. The three recurring hazards never expire: flyback diodes on every coil, ferrofluid stays sealed, ears away from 40 kHz.
