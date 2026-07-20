# Magnetic Matter Movers Phase 0 — Execution Checklist & Gate Criteria
### Buy → Build → Measure → Prove → Unlock Phase 1
*Companion to Build Sheets 001 (Inductrack) and 002 (Droplet Thruster). Print this; fill it in ink. The filled document + photos/video is your gate evidence — bring it back and we review it together, line by line.*

---

## 0. How the Gate Works

Phase 0 closes when **both** builds pass their gates below. "Pass" means: the actual-vs-predicted tables are filled, deviations are explained (not ignored), and the evidence artifacts exist. Deviating from prediction does **not** fail the gate — *unexplained* deviation does. A 2× miss with a good story is data; a perfect match with no photos is nothing.

**Gate evidence package (what you bring back):**
☐ Filled tables from §3 and §5 (photo of this document is fine)
☐ Video: 001 hovering ≥60 s · 002 displacement + snap-back
☐ Photos: Halbach jig mid-assembly · enclosure interior with beam dump · goggles on head
☐ Anomaly notes: one paragraph per deviation >50% from prediction

---

## 1. Purchase Checklist (order everything at once — one shipping wait, not four)

**Build 001 — Inductrack (~$80–120)**
☐ 10× ½" N42 cube magnets (8 + 2 spares)
☐ Alloy-rim bike wheel w/ axle (Variant A) — used is fine, must be aluminum rim (magnet test: doesn't stick)
☐ 775-class motor or brushless + ESC, ≥50 W, with speed control
☐ O-ring/belt for friction drive · epoxy (JB Weld) · 2× guide rods + PTFE tape
☐ Print queue: magnet jig, cart body (STL/design per Sheet 001 §5)

**Build 002 — Droplet (~$150)**
☐ TinyLev kit or parts (72× 40 kHz transducers, Arduino Nano, L298N, frame print)
☐ ≤5 mW red laser (starter) — this is the ONLY laser you need to pass Gate 002
☐ 100–500 mW 450 nm module + **OD4+ goggles rated 445–455 nm** (may defer both to post-gate)
☐ 1 mL syringe + blunt 25 ga needle · india ink · foamcore/felt for enclosure + beam dump
☐ Optional: photodiode + resistor ($2) · laser power meter ($25)

**Instruments (shared)**
☐ Feeler gauges · phone tripod · mm-grid card (print one) · multimeter with current mode (or clamp meter)
☐ Phone apps: tachometer (acoustic or strobe), slow-mo camera

---

## 2. Build 001 Sequence (checkbox version of Sheet 001 §5–6)

☐ Jig printed; ONE magnet test-fitted dry
☐ All 10 magnets polarity-marked (red dot = N face) BEFORE any assembly
☐ Array assembled in jig, one cube at a time, pusher block not fingers, clamped through full epoxy cure
☐ **Strong-side check: washer snaps hard to one face, barely holds on the other — strong face marked**
☐ Wheel mounted, spins smoothly to 1,500 RPM, plywood guard over lower half
☐ Guide rails mounted: cart free vertically ~25 mm, constrained laterally
☐ Array epoxied strong-face-down into cart; ballast to ~250 g total (record actual: ______ g)

## 3. Build 001 — Actual vs. Predicted

**Table A — Levitation onset & gap** (Variant A predictions; B in parentheses)

| Measurement | Predicted | Actual | Dev. |
|---|---|---|---|
| First cart motion (RPM) | ~40–60 (40) | ______ | ___ |
| Clean liftoff (RPM) | ~60 (54) | ______ | ___ |
| Gap @ 500 RPM (mm) | 1–3 (3–6) | ______ | ___ |
| Gap @ 1,000 RPM (mm) | 2–6 (6–12) | ______ | ___ |
| Gap @ 1,500 RPM (mm) | 3–8 (8–15) | ______ | ___ |

**Table B — The flat-drag signature** (motor input watts = V × A, minus no-cart baseline at same RPM)

| RPM | Baseline W (no cart) | W with cart | Drag W (diff) |
|---|---|---|---|
| 500 | ______ | ______ | ______ |
| 1,000 | ______ | ______ | ______ |
| 1,500 | ______ | ______ | ______ |

Predicted: drag column ≈ flat, 30–60 W (A) / ~28 W (B). **The plateau in Table A and the flat line in Table B are the physics deliverables.**

**Troubleshooting triage (if outside 2× of prediction):**
- No lift ever → strong-side check failed or array glued weak-side-down → rebuild with spares
- Liftoff RPM ≫ predicted → rim wall thinner than assumed (steel-belted or thin rim) or gap-robbing cart tilt → verify rim is aluminum, check rail squareness
- Gap far below prediction → cart overweight (weigh it) or rim conductivity low → reduce ballast, log both
- Drag not flat → you're reading total motor W not the difference → redo baseline column

**GATE 001 — pass conditions:**
☐ Stable hover ≥60 s at ≤1,500 RPM (video)
☐ Table A filled, gap plateaus with RPM
☐ Table B filled, drag flat within ±30% over a 2–3× speed range
☐ Any >50% deviation has an anomaly paragraph

## 4. Build 002 Sequence (checkbox version of Sheet 002 §5–6)

☐ TinyLev assembled; **foam bead traps rock-solid** (do not proceed to liquid until true)
☐ Enclosure built: grid card behind trap, camera port, horizontal beam path into felt dump
☐ ≤5 mW red laser rigidly mounted, aligned through node using trapped bead, locked down
☐ Dyed water mixed (~1 drop ink/mL); droplet loading practiced until 3 consecutive stable loads
☐ IF proceeding to 3B later: enclosure interlock, goggles for everyone present, key control — photo evidence required before any high-power run

## 5. Build 002 — Actual vs. Predicted (all at ≤5 mW; camera-tracked)

**Table C — Trap stiffness calibration (tilt method, Sheet 002 §7.2)**

| Tilt angle | Force mg·sinθ (μN) | Displacement (mm) | k (μN/mm) |
|---|---|---|---|
| 2° | 1.4 | ______ | ______ |
| 4° | 2.9 | ______ | ______ |
| 6° | 4.3 | ______ | ______ |

Predicted k: 1–10 μN/mm. Three rows should agree within ~30% (that's your instrument error bar).

**Table D — Thrust runs** (displacement × k = thrust; laser incident 5 mW, absorbed unknown → that's what you're measuring)

| Run | Displacement (mm) | Thrust (μN) | Direction horizontal? | Snap-back on off? |
|---|---|---|---|---|
| 1 | ______ | ______ | Y / N | Y / N |
| 2 | ______ | ______ | Y / N | Y / N |
| 3 | ______ | ______ | Y / N | Y / N |

Predicted thrust at 5 mW incident: 0.15–0.4 μN (absorption 30–80%). Implied absorption fraction = measured thrust ÷ 0.5 μN: ______

**Troubleshooting triage:**
- No displacement → underdyed (add ink), beam missing droplet (re-align on bead), or displacement below camera resolution (zoom, track centroid frame-by-frame)
- Vertical displacement → convection or beam above/below node → re-align; beam must pass through node center
- Droplet dies instantly → too big or trap overdriven → smaller droplet, lower amplitude
- k values disagree wildly → trap drifting with temperature → let it warm up 5 min, recalibrate

**GATE 002 — pass conditions:**
☐ Table C filled, k self-consistent within ~30%
☐ Table D: 3 runs, horizontal direction confirmed, snap-back confirmed (video of one run)
☐ Implied absorption fraction between 0.1 and 1.0 (sanity bound)
☐ Any >50% deviation has an anomaly paragraph
☐ *Stretch (not required):* offset map (Sheet 002 §7.6) — 5 offsets, force-vs-offset sketch

---

## 6. What Passing Unlocks — Phase 1

Bring the evidence package back to this chat. We review deviations together (that conversation IS the troubleshooting session), then Phase 1 opens with, in order:

1. **Lab Note 001** — we co-write it from your filled tables: the thrust-vs-power result, the flat-drag result, methods, photos. First publishable Magnetic Matter Movers artifact.
2. **High-power droplet campaign** — 3B laser unlocked (safety photo evidence first): full thrust-vs-power curve at 4 power levels, limit-cycle hunt, offset map if not done.
3. **Wave-optics propagation sim** — the winter project; the go/no-go computation on beam delivery. Built together, here.
4. **Build Sheet 003 scoping** — torsion-pendulum thrust stand, the bridge toward the combined setup.

*Rule of the ladder: no step skips. The gate exists because Phase 1's credibility rests on Phase 0's error bars.*
