# Item 23 — Tube Exit Aperture: Concept Selection (v0)
### Magnetic Matter Movers · July 21, 2026 · closes ledger item 23 at concept level
*Epistemic tags per the study convention: [E] established · [I] inference · [S] speculation. Detail engineering lands in Phase 2 track design; cycle-life verification rides the item-20 cadence rig.*

---

## 1. Problem

The coilgun tube is evacuated; the muzzle must be open at slug arrival but cannot stand open (the tube refills). Candidates listed at item creation: fast shutter, plasma window, per-shot membrane — plus km-scale thermal expansion, handled in §5.

## 2. Governing timing physics

- Slug covers the final 500 m of track in **~51 ms** at 9.8 km/s muzzle velocity [E].
- Air entering an opened vacuum aperture: the rarefaction leading edge advances at up to 2c₀/(γ−1) ≈ **1.7 km/s** but at vanishing density; the mass-significant fill front moves at roughly sonic speed, **~340 m/s** [E]. A door fully open 50 ms early therefore admits meaningful air only ~15–20 m into the tube — which the slug crosses in ~2 ms en route to crossing the entire atmosphere.
- **Consequence: muzzle vacuum purity is not the requirement.** The binding requirements are mechanical: aperture-class opening in tens of ms, 20+ cycles/day, reseal quality for pump-down, and cycle life at the cadence doctrine's 5,000-cycle standard.
- The slug drives a precursor shock through residual tube gas that arrives at the aperture **before the slug**; door-timing specs are written against shock arrival, not slug arrival [I]. At mtorr tube pressure the shock's mass loading is negligible; the point is timing discipline, not loads.

## 3. Selected concept: two-stage muzzle vestibule — slow outer door + per-shot burst membrane

A short vestibule chamber at the muzzle, bounded by two elements in series:

- **Outer door (slow, robust):** ordinary vacuum gate valve class hardware. Opens well before the shot; its only job is vacuum maintenance between shots. No fast actuation, no fatigue-critical motion.
- **Inner element (per-shot burst membrane):** a thin sacrificial film across the bore that the slug bursts through. Zero moving parts at shot time, zero timing risk; the vestibule's air load is bounded by geometry, not by actuation precision.

**Bounding numbers [E-arithmetic on stated geometry]:** a 1 m bore × 10 m vestibule at full atmosphere holds ~9.4 kg of air; on its own roughing pump it holds a fraction of that. Membrane consumption at full cadence (20 shots/day) ≈ 7,300/yr — a trivial consumable. Film mass is grams against a nose ablation budget of ~1 kg/shot [I]; debris is ingested by the same ablative surface built for the atmosphere.

**Shot cycle:** outer door open → (tube already at operating vacuum; membrane holding vestibule/tube boundary) → fire; slug bursts membrane → close outer door → vent/pump vestibule (~8 m³, not 4.9 km of tube) → replace membrane via magazine/cassette → re-establish vestibule vacuum → ready. Membrane replacement automation is Phase 2 detail engineering.

**Selection rationale:** among the candidates, this is the one with no fast-moving parts, no plasma physics, and no timing race — the failure modes are a torn film (abort, no damage) and a stuck gate valve (commodity hardware). At 5,000-cycle economics, boring is the specification.

## 4. Documented alternate: phase-locked rotary shutter

A continuously spinning disk with a bore aperture, phase-locked to the coil sequencer (which already owns microsecond timing), never accelerates from rest; at ~3,000 RPM the open window is a few ms. Retained as the alternate if membrane logistics disappoint at cadence — it trades a consumable for a precision rotating machine at the muzzle. Not selected for baseline on complexity grounds.

## 5. Thermal expansion (the item's second clause)

Km-scale evacuated tube expansion is standard vacuum-pipeline engineering: bellows expansion joints at intervals, anchored/guided supports — no new physics and no program-specific risk [I]. Existence proof at adjacent scale: the LIGO beam tubes (4 km arms, ~1.2 m diameter, vacuum orders of magnitude harder than this tube's mtorr requirement) [I — cite LIGO tube engineering references in the item-22 pass before this line appears in the study body]. Disposed at concept level; joint pitch and support design land in Phase 2 track engineering.

## 6. Verification path

1. Vestibule fill/venting gas-dynamics calc (desk, hours) — bounds door-timing margins formally.
2. Membrane burst behavior + debris characterization — benchtop, subscale bore (fits the existing Phase 0–2 rig family).
3. Door/valve and membrane-cassette cycle life — item-20 cadence rig scope.

## 7. Ledger disposition

Item 23 **CLOSED** at concept level: baseline selected (two-stage vestibule, slow gate + burst membrane), alternate documented (rotary), expansion clause disposed to standard practice with Phase 2 detail. Successor work: verification steps above fold into items 20 (cycle life) and 16/Phase-2 track design (joints, cassette automation); no new ledger number required.
