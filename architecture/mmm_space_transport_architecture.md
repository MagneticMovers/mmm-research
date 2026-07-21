# A Minimum-Chemical Space Transportation Architecture: Coilgun Freight, Laser-Thermal Launch, and a Water-Based Orbital Logistics Network

**Christopher Brotherton**
*Magnetic Matter Movers — independent research program · magneticmattermovers.com*
*Internal program designation: MTS — Magnetic Transportation Systems*
*Original compilation July 15, 2026; extensions through July 20, 2026; restructured for submission July 21, 2026. The public repository's commit history is the authoritative revision record.*

---

## Abstract

We present a concept-stage architecture study of a launch portfolio that eliminates chemical propulsion except as a crew abort motor: (A) a coilgun freight line (4.9 km track, 1,000 g) delivering bulk mass to LEO at ~$150/kg; (B) a maglev + laser-thermal cargo system (6.8 km track at 30 g, 475 MW beam, Isp 900 hydrogen heat exchanger) delivering delicate cargo at $323–3,800/kg depending on flight rate; (C) a crewed variant (38 km track at 3 g, 3.8 GW beam) at $0.6–2.4M/seat at maturity; and (D) a LEO water depot with beamed-steam tugs extending the network to escape, the Moon, and Mars. First-cut split-step wave-optics simulation shows the vertical-beam-plus-relay-mirror geometry delivers 0.75 ± 0.02 of beam power through the full atmospheric degradation budget, while adaptive optics is shown to be structurally ineffective on slant paths — consistent with published moving-target power-beaming data. All cost figures are stated as bands under an explicit calibration doctrine (×2–3 first-of-a-kind bands; a 3× survivability test on every headline claim); the architecture retains its advantage over chemical incumbents at 3× cost growth everywhere the program bets, with the sole failing claim (crew capex) pre-declared and carrying its own kill criterion. A demonstration ladder from sub-$1k benchtop builds to the full system, a technology risk register with retirement costs, and a free published slug interface standard for demand generation complete the program design.

**Keywords:** beamed-energy propulsion · laser-thermal launch · coilgun · electromagnetic launch · Inductrack · propellant depot · space logistics · adaptive optics · thermal blooming

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Epistemic Framework and Cost Calibration Doctrine](#2-epistemic-framework-and-cost-calibration-doctrine)
3. [Governing Physical Constraints](#3-governing-physical-constraints)
4. [Trade Space: Design Filters and Rejected Architectures](#4-trade-space-design-filters-and-rejected-architectures)
5. [Selected Architecture](#5-selected-architecture)
6. [Beam Delivery: Wave-Optics Analysis](#6-beam-delivery-wave-optics-analysis)
7. [External Validation and Design Imports](#7-external-validation-and-design-imports)
8. [Technology Risk Register and Retirement Path](#8-technology-risk-register-and-retirement-path)
9. [Development Program: Demonstration Ladder, Test Infrastructure, Cadence Doctrine](#9-development-program)
10. [Environmental Assessment](#10-environmental-assessment)
11. [Network Extensions: Mars Pipeline and Destination Ranking](#11-network-extensions-mars-pipeline-and-destination-ranking)
12. [Demand Generation and the Slug Interface Standard](#12-demand-generation-and-the-slug-interface-standard)
13. [Cost Survivability of Headline Claims](#13-cost-survivability-of-headline-claims)
14. [Limitations and Adversarial Review](#14-limitations-and-adversarial-review)
15. [Open Work and Future Directions](#15-open-work-and-future-directions)

Appendix A — [Work Item Status Ledger](#appendix-a--work-item-status-ledger)
Appendix B — [Key Reference Numbers](#appendix-b--key-reference-numbers)
Appendix C — [Benchtop Inductrack Build](#appendix-c--benchtop-inductrack-build)
Appendix D — [Document History](#appendix-d--document-history)

---

## 1. Introduction

This study documents a three-system launch portfolio plus one orbital node, sharing magnetics-and-power DNA, with chemical rockets eliminated except as a crew abort motor:

1. **Coilgun freight line** — 4.9 km track at 1,000 g, bulk mass to LEO at ~$150/kg (direct-to-escape variant: 8.7 km, ~$190/kg)
2. **Maglev + laser-thermal cargo** — 6.8 km track (30 g) + 475 MW beam, delicate cargo to LEO, $323–3,800/kg depending on flight rate
3. **Maglev + laser-thermal crew** — 38 km track (3 g) + 3.8 GW beam, 6-seat vehicles, $0.6–2.4M/seat at maturity
4. **LEO dock + tug fleet** — slugs become ships; tugs add the final 3.2 km/s to escape

The total capital ladder runs $0.1B pilot → $4–12B cargo → $23–84B crew, with every phase generating revenue and de-risking the next. Marginal costs are electricity: $11/kg (beamed) and ~$3.6/kg (gun) in energy alone.

The study is presented as a *concept/architecture paper*: physics checks, subsystem sizing, cost models, and — deliberately foregrounded — the decision trail, including rejected branches, an adversarial self-review, and pre-declared kill criteria. Section 2 states the epistemic rules under which every claim in the document is made.

## 2. Epistemic Framework and Cost Calibration Doctrine

### 2.1 Claim tiers (owner standard, adopted Jul 20, 2026)

Claims in this study carry three tiers: **[E] established** (textbook physics, published data), **[I] inference** (first-cut analysis, scaling laws, our simulations — method-limited), **[S] speculation** (demand models, far-horizon concepts). Blanket assignments unless marked otherwise: Physics constraints (§3) = [E]. Simulation results = [I] (v0/v1 are first-cut: limited Monte Carlo, reduced-order blooming). All dollar figures = [I]-grade approximations from memory-sourced cost curves, not verified quotes — and they sit atop 5+ step inference chains (payload fraction × capex × rate × amortization) where errors compound; every $/kg is ±2× until work item 22 (citation and uncertainty pass, Appendix A) closes it. Demand/market claims = [S].

Governing equations for checkable math: rocket equation Δv = vₑln(m₀/m₁) · jet power P = Tvₑ/2 · magnetic pressure B²/2μ₀ · Inductrack L/D ≈ v/w · Bradley–Herrmann N_D scaling · F = BIL — implementations in `mmm_waveoptics_v0/v1.py` and the program's models.

### 2.2 Cost Calibration Doctrine (adopted Jul 20, 2026)

**Motivation.** The item-22 citation pass showed that memory-sourced cost errors are not uniformly directional and therefore cannot be fixed by a single "% of realism" dial: the chemical-launch comparison was stale in the *unfavorable* direction (published 2026 prices are lower than the strawman), the EM-launcher extrapolation ratio was ~5% high, and the black-carbon figure was fine at midpoint but banded too narrowly. Meanwhile the published record on first-of-a-kind megaprojects (pioneer-plant and aerospace overrun literature) puts early capital estimates at roughly **40–60% of final actuals** — 2–3× growth is the historical norm, not the exception. A program that publishes optimistic points is betting reviewers won't know this; they will.

**The doctrine:**

1. **Physics exact.** No calibration dial ever applies to [E]-tier claims.
2. **Costs are bands, not points.** The stated midpoint is the honest estimate — never a target, never a goal-seeded number. Default band ×2–3 for first-of-a-kind items until item 22 closes that figure with sources; quotes and bids narrow bands, opinions don't.
3. **The 3× survivability test.** Every headline $/kg or capex claim carries the question: *does the architecture keep its advantage over the incumbent at 3× the estimate?* Advantage retained at 3× = the claim is load-bearing; advantage inverted inside the band = the claim is decorative and must not carry an argument.
4. **Kill-criterion restatement.** A cost estimate "fails" when the *advantage inverts inside the band* — not when the midpoint moves. An estimate that doubles while keeping a 10× advantage is a pass and is reported as such.

The doctrine applied to this study's headline claims is presented as results in §13.

## 3. Governing Physical Constraints

**Space is fast, not high.** Three destinations, three price tags: touch 100 km and fall back — 1.4 km/s; stay in LEO — 7.8 km/s; leave Earth (escape) — 11.2 km/s (= √2 × orbital). Altitude to 100 km is 1 MJ/kg; orbital kinetic energy is 30 MJ/kg. Any altitude-first scheme (balloons, towers) attacks 3% of the problem.

**The atmosphere is a 17% tax.** Gravity + drag + steering losses ≈ 1.6 of the 9.4 km/s LEO budget. Worth harvesting (evacuated tube, mountain exit, thrust above the dense air) — never worth building an architecture around.

**The rocket equation lives at the top of the velocity budget.** Shaving the first 2 km/s saves ~8% of propellant; raising exhaust velocity attacks the exponent. Ground-assist helps; changing the engine (Isp 350 → 900) transforms (payload fraction 2% → 21%).

**Every technology is regime-locked.** Electric thrusters, power beaming, and Earth's magnetic field are all useless during ascent and excellent after orbit. Chemical wins ascent by *power density*, not efficiency — the propellant is the power plant. To launch without chemistry, either leave the power plant on the ground (beam) or deliver all velocity on the ground (track/gun).

**G-force sorts the passengers permanently.** Humans (≤3 g) can never take their velocity from the ground: direct-to-escape would need a 2,655 km track. Crew requires sustained thrust over minutes. Hardened cargo at 1,000 g needs 4.9–8.7 km. This is a law, not an engineering gap.

**Ballistic coefficient is destiny in the atmosphere.** A dense, slender 1,000 kg slug from a 4 km exit loses 516 m/s and ~1 kg of ablator crossing the whole atmosphere at 13 km/s. A flat plate (the Pascal-B manhole cover) becomes a reverse meteor.

## 4. Trade Space: Design Filters and Rejected Architectures

### 4.1 Design filters

1. **No step-function infrastructure.** Anything that must be 100% complete before delivering 1% of value will consume the program. Prefer systems that scale continuously and earn on every phase.
2. **Put complexity where the wrenches are.** Vehicle dumb and cheap; intelligence, power, and maintenance on the ground.
3. **Space assets must be thin, passive, and optional.** A dead relay mirror is a degraded day; a cut tether is a dead program.
4. **Non-contact magnetic force wherever surfaces meet at speed.** Inductrack levitation, coilgun (not railgun) launch, magnetic tug docking aids.

### 4.2 Rejected branches (and the numbers that killed them)

| Concept | Fatal number | Verdict |
|---|---|---|
| Momentum-exchange tether | 15–25 t infrastructure per t payload; catch = hypersonic rendezvous, meter tolerance, seconds; single structure in the debris belt | Step-function megastructure; bootstrap paradox |
| Fully electric launch | T/W > 1 needs ~100 MW-class jet power per tonne; power plant 10–500× vehicle mass; scale-invariant | Specific-power wall (~10–100× beyond batteries/reactors) |
| EAD as launch stage | Thrust density 2–20 N/m² → 2,551 m² of electrode for a 1 t vehicle; no air above ~50 km; thrust decays with airspeed | Regime-locked to atmospheric flight (per Gomez Vega framing) |
| Harnessing Earth's magnetic field | 50 μT field = 1 mPa magnetic pressure; dipole levitation of 1 t needs 4×10¹⁴ A·m²; static field carries no energy | Cannot amplify a field you didn't generate; no reaction partner. **Exception:** electrodynamic tethers in orbit (3 N from 10 km/10 A → 1,555 m/s per month, propellant-free) |
| 100 km "zipper tower" | Altitude = 3% of the job; NdFeB self-support height 1.1 km; erection mass 50,000+ t; magnetic joints have no bending stiffness | Compression + mass + hinging. Salvage: the instinct (magnetic structure held by fields) is the launch loop / space fountain family — dynamic support via momentum flux — itself rejected on filter #1 |
| Space-based power generation | 950 MW platform = 3,200 t solar + 2,400 t radiators (waste heat has no pond in space); burst variant still ~1,500 t (ISS = 420 t) | Bootstrap paradox, heavier than the tether |
| Ground-only slant beaming (full burn) | Isoplanatic patch ~16 μrad vs vehicle crossing 8,571 μrad/s; thermal blooming N_D = 270 at end-of-burn slant | Adaptive optics structurally cannot track the target; works only for first ~⅓ of burn |
| Microwave (28 GHz) instead of laser | Published system estimate: ~80 MW beam + 90–175 m antenna for an 8 kg payload ≈ 10,000 MW/t — ~100× our laser figure (95 MW/t) — because 10,000× longer wavelength wrecks diffraction; pulsed air-plasma thrusters also self-shield (residual plasma absorbs the next pulse) | Cheap watts (fusion-industry gyrotrons), impossible optics; CW solid-HX laser avoids plasma timing entirely. Their tracking data imported in §7 |

## 5. Selected Architecture

*Systems are lettered in build order — A is built first, and each system's flight heritage is the entry condition for the next.*

### 5.1 System A — Coilgun Freight (build first, with the pilot)

- **Staged-to-LEO (primary):** 9.8 km/s muzzle, 4.9 km track, 1,000 g, 48 GJ/shot (36 GW pulse). Slug: 180 kg shell + 190 kg circularization kick → **~630 kg to LEO, ~$150/kg**
- **Direct-to-escape (variant):** 13.05 km/s muzzle, 8.7 km track, 85 GJ (64 GW pulse); 670 kg cargo to escape at **$190/kg** (5,000 shots/yr) — vs published chemical pricing: ~$3–7k/kg to LEO (2026 Falcon-class list/rideshare), $5–10k/kg escape-class [sourced, item-22 pass]
- **Atmosphere transit (4 km mountain exit):** 516 m/s toll, peak 109 kW/cm² for <1 s, ~1 kg ablated (carbon-phenolic, 3× margin carried)
- **Gating tech: pulsed power.** 36–64 GW for ~1.3 s = flywheel motor-generator / compensated pulsed-alternator farms (batteries and capacitors both disqualify). ~1,500–2,700× (variant-dependent) the largest EM launcher built (Navy/GA ~33 MJ class) — the biggest extrapolation in the portfolio
- **Coilgun, not railgun:** no contact at 10–13 km/s. 25 MW feed → 20+ shots/day. Cargo: water, cryogens, metals, propellant, artillery-grade electronics (15,000 g proven)

### 5.2 System B — Maglev + Laser-Thermal Cargo (build second)

- **Vehicle:** 5 t gross; maglev exit 2.0 km/s (6.8 km evacuated track, 30 g); laser-thermal stage: 6.8 km/s at Isp 900 on 2,685 kg LH2; **payload 1,065 kg (21% — vs 2% chemical for the same job)**
- **Ground power:** 475 MW beam / 950 MW wall-plug for 462 s. Energy 122 MWh/launch (~$12,200; **$11/kg marginal**). 25 MW grid feed → 5 h recharge. Battery buffer note: 7.8C draw exceeds LFP comfort — oversize to ~500 MWh, use LTO, or hybridize with flywheels
- **Laser array:** ~24,000 × 20 kW fiber modules; $2.4–9.5B at $5–20/W (the dominant capex; riding a falling cost curve)
- **Beam path:** direct slant for early burn only; **relay mirrors are load-bearing** for the back half — 4–8 m passive mirrors, 100–500 kg each, 2–3 for full-burn coverage. Ground beam exits vertically (blooming N_D 83 → 28 with 300 m array footprint; relay drift 83 μrad/s is trackable). Relay constraint: ≥99.99% dielectric coatings (bench-testable). Alternative: 2–3 extra full ground arrays downrange (~1000× more expensive)
- **Capex: $4–12B.** Per-kg: $36,600 @ 10 flights/yr; $3,800 @ 100 (Falcon 9 parity); **$870 @ 500; $323 @ 2,000**

### 5.3 System C — Crewed Variant (build last)

- 6 seats (~1 t/seat), 3 g limit → maglev only 1.5 km/s on a 38 km track; 40 t gross; **3.8 GW beam**
- Crew *status*, not crew count, drives cost (g-limits, human-rating margin, abort). 6-max saves little; larger cabins amortize better
- **Abort:** beam loss = engine loss → independent solid chemical abort motor. Chemical as parachute, not propulsion
- **Capex $23–84B.** Per seat: $45M @ 10 flights/yr (market parity) → $2.4M @ 200 → $0.6M @ 1,000. An airline: ruinous at low utilization, unbeatable at high

### 5.4 Node D — LEO Dock and Tug Fleet

Orbit is **92% of escape energy**; the tug adds only 3.2 km/s. Docking at ~0 m/s relative replaces hypersonic catching; slugs aggregate into assembled ships. Propellant is itself gun-delivered at ~$150/kg — the depot bootstrap.

**Preliminary tug screening** (superseded by the full accounting below; retained as the trade record):

| Tug | Isp | Trip | Propellant kg per cargo kg |
|---|---|---|---|
| Chemical hydrolox | 450 | 3 days | 1.07 |
| Beamed-thermal (perigee kicks from the existing array — Oberth optimal) | 900 | ~1 week | 0.44 |
| Electric Hall (spiral penalty: 7.7 km/s dv, still frugal) | 2,500 | 6–9 mo | 0.37 |

**Full-accounting trade result (Jul 15, 2026 revision — governing):** water at $150/kg LEO, plant amortization, fleet sizing for 2,287 t/yr:

| Tug | Water kg / cargo kg | Fleet needed | $/kg to escape |
|---|---|---|---|
| **Beamed steam (Isp 400, perigee kicks) — SELECTED** | 1.38 | 8 | **$225** |
| Hydrolox chemical (Isp 450) | 1.36 (after 0.78 electrolysis yield) | 4 | $269 |
| Electric water plasma (Isp 800, spiral) | 1.67 | 133 | $560 |

**Key finding:** steam and hydrolox consume essentially identical water per kg of cargo — electrolysis yield cancels the Isp advantage. The 192 t propellant plant (incl. 89 t of cryocoolers, the node's hardest development) buys nothing and is **deleted from baseline**. Node D reduces to: water storage tanks + docking ports + ~8 beamed-steam tugs. Hydrolox remains a fast-lane option (3-day vs 10-day trips) if a time-critical market appears; electric tugs lose on fleet capital (210-day trips), niche only.

**Engineering delta:** steam oxidizes carbon — tug HX uses oxide-coated or Ir-lined refractory instead of the C-C/TaC hydrogen stack. Same coupon test rig; add steam coupons to the campaign.

**Staged vs direct escape:** $216–320/kg staged vs $190 direct — direct gun wins for dumb bulk; staging wins for anything that must arrive as a functioning spacecraft.

**Architecture-wide principle, confirmed at every node:** ship the dumbest possible mass; add energy at the point of use. Gun throws water; beam superheats it; one laser array serves ascent and perigee departure; one HX technology family (two coating systems) powers both.

## 6. Beam Delivery: Wave-Optics Analysis

*Work item 1; first-cut split-step simulation complete Jul 19, 2026 (scripts: `mmm_waveoptics_v0.py`, `mmm_waveoptics_v1.py`, MIT-licensed).*

**Method.** Kolmogorov/von Karman phase screens (structure-function-calibrated) layered per the HV5/7 profile from the 2 km site; AO modeled physically as conjugation of the beacon-path column with 10 cm actuator-pitch fitting cutoff; point-ahead anisoplanatism implemented by laterally shifting each turbulence layer by θ_pa·h for the outgoing beam; vacuum far-field beyond the atmosphere; 8-draw Monte Carlo; metric = power fraction into the 2.5 m HX at range.

### 6.1 v0 results

| Case | Zenith | Range | Point-ahead | AO | Delivered fraction |
|---|---|---|---|---|---|
| **Vertical → relay mirror (baseline)** | 0° | 600 km | 2 μrad | on | **0.83 ± 0.01** |
| Slant mid-burn → vehicle | 55° | 350 km | 20 μrad | on | 0.64 ± 0.05 |
| Vertical, no AO | 0° | 600 km | — | off | 0.46 ± 0.09 |
| Slant, no AO | 55° | 350 km | — | off | 0.56 ± 0.09 |

(Diffraction-limited/no-atmosphere reference ≈ 0.99. Slant bucket angles are geometrically larger at closer range; comparison is against each case's own delivery requirement.)

**Findings.** (1) The **relay-vertical baseline closes**: 83% delivery through the full atmosphere with modest AO, tight variance — before array-scale refinements, which only help. (2) **AO is structurally ineffective on the slant path** (0.56 → 0.64): with the correction measured through air offset from the beam's path by the point-ahead angle, conjugation decorrelates — now confirmed by wave propagation, independently of the earlier isoplanatic-patch scaling argument and the published 60.1%→0.43% moving-target collapse (§7). Shown slant numbers *flatter* reality: end-of-burn (72°, 700 km) is worse on every term and carries blooming N_D = 270 (excluded from this model; vertical N_D = 28 with 300 m footprint).

### 6.2 v1 gauntlet (blooming + AO temporal lag)

Blooming coupled into propagation (similarity-scaled steady-state upwind-integral model, iterated to convergence) plus AO temporal lag (1 ms latency against Bufton frozen-flow winds). Results: **vertical relay baseline 0.75 ± 0.02 with the full degradation budget** (blooming-off reference 0.80); slant progression 0.78 (early, 30°) → 0.22 (mid, 55°) → **0.03 (end-of-burn, 72°, N_D 270)** — quantitatively reproducing the "direct works early, relays carry the back half" design claim from an independent method. Residual caveat on the baseline: phase-compensation instability not modeled (threatens high-N_D slant far more than N_D 28 vertical; explicit check assigned to Phase 1 completion).

### 6.3 Array configuration

**Vertical phased-array configuration confirmed as baseline.** The simulated 1 m director is a single subaperture of the distributed array; array synthesis (many subapertures over a 100–300 m footprint) is deferred to the full Phase 1 sim — with the standing correction that **thermal absorption requires no optical coherence**: incoherent tiled addition suffices, so each subaperture needs only its own AO and pointing, and array-wide phase-locking is deleted from the requirements entirely. Tiling distributes per-aperture flux and *reduces* blooming — the first-cut result is therefore conservative for the baseline and optimistic only for the already-rejected slant case.

**Remaining Phase 1 sim scope (work item 10):** time-dependent thermal blooming coupled into propagation (the one term that could still move the vertical verdict); end-of-burn geometry sweep; Greenwood/temporal AO bandwidth error; distributed-array aperture synthesis; ≥100-draw Monte Carlo; radiometric absorption ledger.

## 7. External Validation and Design Imports

*Source: the Japanese 28 GHz microwave beamed-propulsion program (Shimamura et al. — J. Spacecraft & Rockets drone power-beaming test; Sci. Rep. 2025 tractor-beam and vortex-plate studies; Phys. Plasmas rectenna monitoring). The nearest running hardware program to this architecture's Phase 1; four items adopted (Jul 17, 2026):*

1. **Tracking-collapse validation (risk register: beam combining + propagation).** Their measured end-to-end efficiency fell from 60.1% (fixed receiver) to 0.43% (free-flying drone) — a ~140× collapse purely from target motion. First published hardware confirmation of the tracking argument that makes relay mirrors load-bearing in this architecture. Cite in the propagation white paper.
2. **Beam shaping as thermal-control actuator (risk register: heat exchanger, hot spots).** Their vortex-phase-plate result showed beam *shape* determines where energy deposits and whether force helps or opposes the vehicle. Adopted implication: our phased array actively flattens the flux profile across the HX panel — the hot-spot problem (AO residual 1.5–2× local flux) gains an active mitigation path in addition to passive HX margin. Adds a requirement to Phase 2–3 array control software; adds a flux-profile command interface to the SIS-adjacent vehicle spec.
3. **Transmitter-as-sensor (risk register: HX; Build Sheet 002).** Their rectenna standing-wave monitor watched the plasma front without cameras. Adopted: backscatter monitoring of the HX panel from the ground array (per-subaperture return power = panel health map); at Phase 0, a photodiode watching droplet scatter.
4. **Beam-riding misalignment data (Build Sheet 002 §7).** Their offset-vs-thrust studies are the gyrotron-scale version of the droplet limit-cycle; the deliberate-offset protocol run added to Build Sheet 002 reproduces the measurement at bench scale.

**Their unresolved problem we structurally avoid:** pulsed air-plasma thrusters self-shield (residual plasma absorbs subsequent pulses), forcing front-fed "tractor" geometries. The CW solid-HX vehicle has no plasma and no pulse timing — a design rationale line for the white paper.

## 8. Technology Risk Register and Retirement Path

| Risk | Why it gates | Retirement path | Cost to retire |
|---|---|---|---|
| **Hydrogen heat exchanger** | Wall temp caps gas temp caps Isp caps payload. 48 MW/m² absorbed (3× fusion divertor); 2,900 K hydrogen; walls sub-mm (microchannels mandatory); hot-H2 corrosion (NERVA's killer — fixed with ZrC/NbC; modern stack: TaC/HfC on carbon-carbon, whose 44 MPa thermal stress beats W-Re 16×) | Coupon (10 kW laser, $10k) → tile (100 kW) → panel (1 MW pilot). Flux, not power, is what material sees — bench results transfer to 475 MW. Watch: Ledinegg flow instability (orifice the channels), 300→3,000 K cycle fatigue, hot spots at 1.5–2× design flux from AO residual | $10k–$5M |
| Design margin | Isp 900 sits at the solid-HX ceiling; laser-sustained plasma (gas hotter than walls) offers Isp 1,100–1,400 as block upgrade | De-rate check: Isp 850 → payload 21%→19%. Architecture robust | — |
| **Beam combining + propagation** | 24k fibers into one phased aperture; thermal blooming self-defocus | Split-step wave-optics simulation (§6), then subscale field tests. Relay-vertical geometry buys ~10× margin | ~$0 → $10M |
| Relay mirror coatings | 475 MW × 0.01% absorption = 48 kW radiative-only rejection | ≥99.99% dielectric coating coupons, ground vacuum test | $1–10M |
| **Pulsed power (gun)** | 36–64 GW / 1.3 s; nothing built within 1,000× | Flywheel/pulsed-alternator farm; subscale gun (Navy-railgun-class energies) first | $50–500M |
| Slug terminal ops | Kick stage must survive 1,000 g (guided-artillery heritage); deep-space catch unpriced for direct-escape variant | Staged-to-LEO architecture sidesteps it (tug docks, doesn't catch) | design choice |

## 9. Development Program

### 9.1 Demonstration ladder

| Phase | Beam / hardware | Delivers | Cost | Milestone |
|---|---|---|---|---|
| 0 | Benchtop | — | <$1k | Inductrack drum + Halbach cart (Appendix C); watt-class lightcraft |
| 1 | 10 kW laser | 100 g craft | ~$100k | Lightcraft-class climb (Myrabo flew this in 2000: 50 g to 71 m) |
| 1.5 | 100 kW (owned OR **rented** — industrial fiber / HELSTF beam time via SBIR customer) | 1 kg free-flight hop | $0.5–3M | Suborbital-class demo at SBIR scale; closes the 100 g → 10 kg gap |
| 2 | 1 MW array | 10 kg suborbital | $10–50M | **HX qualification at full flux**; AO field data. Buy the array only when flight cadence justifies capex — beam time rents before it owns |
| 3 | 10 MW array | 22 kg near-orbital | $50–200M | Venture-scale pilot; first revenue (microsats) |
| 4 | 475 MW + 6.8 km track | 1,065 kg LEO | $4–12B | System B operational; coilgun (System A) built in parallel |
| 5 | 3.8 GW + 38 km track | 6 crew | $23–84B | System C, on System B's flight heritage |

### 9.2 Test infrastructure and range plan (Jul 19, 2026)

**Height-ladder finding:** test altitude requirements are bimodal — bench height, then ~30 ft, then open sky. Intermediate tall-ceiling facilities (100–400 ft class) buy nothing: beam-riding control qualifies on **guide-wire tethered hops at 20–30 ft** (Myrabo lightcraft method), and free flight wants kilometers, not rafters. No 400 ft facility exists to rent, and none is needed.

The ladder (all within ~3 h of Rio Rancho — New Mexico is the one state where the full test infrastructure is a day trip):

| Tier | Venue | Phase | What runs there | Access route |
|---|---|---|---|---|
| Bench | Home shop | 0–1 | Builds 001/002, torsion stand, low-power droplet | owned |
| Laser lab | Light-industrial rental, ABQ/Rio Rancho (~1–2k sq ft, 3-phase 240 V, interlocked blackout laser room, ventilation + exterior gas storage for hydrogen coupons; 14 ft ceiling suffices) | 2 | 1–10 kW HX coupon campaign, steam microthruster, coilgun stage bench | ~$1–2k/mo lease at Phase 2 funding |
| Tethered hop | Same lab or 26–32 ft warehouse | 2–3 | Beam-riding control on guide wire | lease |
| Gun range | **EMRTC (NM Tech, Socorro)** | 2–3 | Subscale coilgun projectiles beyond lab backstop | commercial range rental |
| Free flight | **Spaceport America** | 3+ | 10 kg vehicle flights; restricted-airspace umbrella eases outdoor-laser clearance | negotiated campaign contract |
| National labs | **Sandia via NMSBA** | 1+ | Pulsed power, magnetics, HX consultation at no cost to NM small businesses; CRADA path for facilities | apply after LLC formation |
| MW-class laser | White Sands / HELSTF | 3+ | Megawatt beam heritage (lightcraft flew here) | SBIR-customer partnership, not rental |

**Regulatory (file mentally now, act at Phase 2/3):** outdoor beams require FAA coordination (AC 70-1) and DoD **Laser Clearinghouse** deconfliction for sky-directed propagation — the decisive argument for testing under Spaceport America's restricted airspace rather than private land.

### 9.3 Cadence doctrine (gate plan amended Jul 19, 2026)

Economics live at 100+ flights/yr and 1,000–5,000 shots/yr; gates must therefore prove **cycling, not just capability**. Cadence risk is cycle-count-invariant — switch lifetime, coil thermal fatigue, flywheel cycling, HX cycle life all retire at benchtop scale. Adopted: Phase 2 cadence endurance rig (item 20: 5,000 automated subscale cycles, ~$10–30k); HX coupon protocol extended to ≥1,000 cycles; Phase 3 gate adds sustained flights/week; Phase 4 adds dummy-payload cadence campaigns at marginal (energy-only) cost. **Low-demand operating mode is designed, not feared:** 50 bookings + 450 water-slug dummy shots ≈ a 500-shot year for ~$6k of additional electricity — the cycle ledger accumulated on unsold capacity is itself the sales instrument. No chemical system can afford to prove cadence on empty manifests; this one barely notices the cost.

## 10. Environmental Assessment

*Thesis-relevant: constraint as moat (Jul 19, 2026).*

Operational emissions are electricity: 115 MWh/t (beamed) and 21 MWh/t (gun) — near-zero carbon from NM solar; exhaust is steam; no soot, alumina, perchlorates, hypergolics, or deluge contamination anywhere in the stack. Chemical launch, by contrast, carries ~25–30 t CO₂/t payload plus ~0.3–3 t black carbon per launch (engine/cycle-dependent) injected at stratospheric altitude (≈500× surface warming potency — Ryan et al. 2022, sourced) — a compounding regulatory exposure that grows with exactly the industry-wide cadence this program bets on. Tightening launch regulation is a tailwind for this architecture.

**Honest residuals, ranked:** (1) sonic booms — the dominant real externality at 20+ shots/day; priced into WSMR-adjacent siting; (2) ~24 t H₂O per beamed launch partly above the tropopause — monitor-and-report item, owned in the white paper preemptively; (3) ~1 kg ablated carbon per gun shot (≈5 t/yr at full cadence — negligible vs. aviation); (4) beam-path wildlife/aviation safety — radar-triggered beam interrupt, Phase 3 requirement.

## 11. Network Extensions: Mars Pipeline and Destination Ranking

### 11.1 The Mars pipeline (Jul 15, 2026)

**Principle:** interplanetary space cannot hold a track — everything placed there is itself in solar orbit. The road (Kepler coasting) is free; all cost lives at the ramps. Infrastructure therefore replaces per-trip propellant only at the endpoints.

**On-ramp: already built.** The escape gun's 12.53 km/s atmospheric-exit velocity gives v∞ = 5.65 km/s — Mars Hohmann needs only 2.95 (ground requirement 11.57 km/s). Margin buys 4–5 month fast transits and stretches each launch window to ~4–6 months. Departure propellant: zero.

**Coast:** 259 days (Hohmann) / ~130–150 (fast), propellant zero. Windows every 780 days (synodic). At 5,000 shots/yr, one window ships ~1,300 t Marsward; between windows the gun serves LEO/lunar traffic.

**Off-ramp: aerocapture (baseline).** Entry speeds 5.7 km/s (Hohmann) to 7.1 km/s (fast) — below MSL's 5.8 for freight, well below Earth-return capsule heritage (12.5). Slug carries 12–15% ablative heatshield (1,000 g-compatible carbon nose, same family as launch ablator). Aerocapture pass → Mars orbit → 50–100 m/s periapsis-raise (steam puff). Arrival propellant: ~zero. Toll per kg ≈ heatshield mass fraction.

**Mars-orbit port (the ownable asset).** Tug fleet's one-time emplacement job, then Earth tugs retire from the route: station + water stock, nav/comm beacons, small local steam tugs (watered by incoming slugs) for orbit consolidation. Nobody owns the transfer orbit; the port sets the price of mass at Mars.

**Phase-2 upgrade: Phobos momentum bank.** Tether/rotating catcher anchored to Phobos (1.07×10¹⁶ kg): inbound freight deposits momentum into Phobos's orbit; outbound Earthward cargo withdraws it — inbound traffic funds outbound flings. 2,000 t/yr of 3 km/s catches perturbs Phobos by ~micrometers/s per year (planetary flywheel, effectively infinite bank). Passes the step-function filter as an *optional* upgrade: aerocapture runs the route without it. Softer than the Earth tether (no debris belt, lower closing speeds, free anchor mass); still inherits the catch-precision problem — phase it after the route is proven.

**Steady state.** Gun throws water and freight → Kepler carries → Mars atmosphere brakes → port aggregates. Per-trip consumables: one carbon nose and a puff of steam. The tug's role, as specified: build the off-ramp once, then stand down.

### 11.2 Destination ranking (Jul 15, 2026)

**Law:** the gun and the Kepler coast are destination-agnostic; only the off-ramp changes. Destinations rank by their brakes: atmospheres are free off-ramps; airless bodies charge a steam toll — but airless + low-g bodies are where the coilgun re-roots and turns importers into exporters.

| Destination | Ground req (km/s) | Gun margin | Transit | Window | Off-ramp | Toll per kg cargo |
|---|---|---|---|---|---|---|
| **Moon** | 10.95 | huge | 3 d | **daily** | propulsive (steam) | 0.24 kg water (self-paying when cargo is water) |
| Venus | 11.46 | +1.07 | 146 d | 584 d | thick atmo — generous aerocapture corridor (entry 10.7 km/s) | ~0.14 heatshield |
| Mars | 11.57 | +0.96 | 259 d | 780 d | thin atmo — narrow corridor (work item 13) | ~0.13 heatshield |
| Jupiter+ | 14.23 | −1.70 (out of direct reach) | 997 d+ | 399 d | — | via gravity assists or tug Oberth perigee kick |

**Sequence:**

1. **Moon first — the debug destination.** Daily windows delete the gun's idle-capacity problem; 3-day feedback loop iterates operations ~250× faster than Mars; nearest-term freight market. Phase-2: lunar surface coilgun (escape 2.38 km/s → **290 m track at 1,000 g**; vacuum, low-g, no weather = ideal site) plus lunavator drive the off-ramp toll to zero and flip the Moon to exporter (polar water, regolith, metals). Earth launcher tech exports at 1/30 scale.
2. **Mars — the anchor tenant.** Full pipeline per §11.1; Phobos momentum bank as phase-2.
3. **Venus — the switch-yard.** Best transport physics (frequent windows, short transit, forgiving aerocapture), thinnest market (no reachable surface, no moon for momentum banking). Small port justified as gravity-assist junction to Mercury and outer-system routing, not as a terminus.
4. **Beyond the belt:** the gun's direct horizon ends near Jupiter's requirements; outer-system freight stages through tug perigee kicks (Oberth) or planetary assists.

## 12. Demand Generation and the Slug Interface Standard

*Extension of Jul 16, 2026.*

**Premise:** every cost model in this study clears its break-even only at high flight rates; demand is therefore the binding constraint, ahead of any single technology. History shows demand in space has been created by *documents*, not consortia: a free interface standard (CubeSat spec, 1999 → the smallsat industry), a published price (rideshare price sheets → manifested smallsat demand), and an anchor-tenant purchase promise (CLPS → seven lander companies). Coordination through paper scales; coordination through meetings doesn't. The pipeline adopts the same instrument set.

### 12.1 Slug Interface Standard (SIS) — Draft A scope

A free, published specification letting any mission designer, CubeSat program, servicing startup, or depot operator design against the pipeline before it exists:

- **Mass classes & envelopes:** S-630 (baseline LEO slug, 630 kg net), S-670 (direct-escape, 670 kg), sub-classes for rideshare partitions within one slug
- **Environment rating:** 1,000 g axial design / 1,500 g proof; vibration & thermal transit envelopes (launch heat pulse, coast cold-soak)
- **Berthing interface:** standard grapple/berthing feature for tug capture at ~0 m/s relative; alignment, capture-envelope, and load-path definitions
- **Water payload spec:** purity classes (propellant-grade vs. life-support-grade), freeze state, tank venting standard
- **Kick-stage envelope:** volume/mass allocation, minimum reliability floor and disposal requirement (debris control at 1,000+ shots/yr is a licensing precondition)
- **Nav & transponder minimums:** tracking, arrival-corridor trim authority, abort-to-disposal logic
- **Heatshield classes:** L (none — LEO), M (Mars aerocapture, ~13%), V (Venus, ~14%)

### 12.2 Companion instruments

- **Published price sheet:** the $/kg curves from this study, stated as offered service prices at declared flight rates — designers write proposals against numbers, not visions
- **Demand registry:** non-binding letters of intent ("would purchase N kg water at L1/LLO/Mars orbit at $X/kg") — the traction instrument that converts latent demand into evidence for funders
- **Circulation venues:** CONFERS (on-orbit servicing/assembly standards body), SmallSat conference, standards submission once Draft B stabilizes

### 12.3 Phase placement

SIS Draft A is a Phase 1–2 deliverable (cost ≈ $0; authored alongside the wave-optics work). The registry opens with Draft A publication. Draft B incorporates feedback before any Phase 3 hardware commitment, so the 10 MW pilot flies payloads already designed to the standard.

## 13. Cost Survivability of Headline Claims

*The doctrine of §2.2 applied to this study's current headline claims:*

| Claim | Midpoint | At 3× | Advantage at 3×? |
|---|---|---|---|
| Gun freight $/kg to LEO | $150 | $450 | **Yes** — vs $3–7k/kg published chemical; ~10× margin survives |
| Beamed cargo $/kg (500–2,000 flights/yr) | $323–870 | ~$1,000–2,600 | **Yes at rate** — still at/below Falcon parity; but break-even flight rate ≈3× higher → item 9 (demand model) is the binding analysis, not the capex digit |
| Marginal energy cost | $11/kg | $33/kg | **Trivially** — remains noise against any incumbent |
| Phase 0–2 program cost | $270–$500k | scales | Absorbable at self/SBIR funding tiers by design |
| Crew capex (System C) | $23–84B | $69–252B | **No** — not robust at 3×; consistent with the already-accepted end state (gate plan Phase 6 kill: chemical crew taxis remain the permanent answer) |

**Reading:** the architecture survives the realistic number everywhere the program actually bets. The one claim that fails the 3× test (crew) already carries its own kill criterion and an acceptable end state — which is the correct shape for a failing cost claim: pre-declared, gated, and non-load-bearing. This table, maintained as estimates are re-sourced under item 22, is itself the anti-fragility exhibit for reviewers and funders: the program does not need its optimistic numbers to be right.

## 14. Limitations and Adversarial Review

*Red-team register, Jul 19, 2026 — adversarial self-review ahead of any public submission.*

**Hidden advantages banked:** (1) thermal propulsion needs incoherent tiled power, not a phased beam — array-wide coherence deleted from requirements (correction applied, §6.3); (2) unburned slugs are suborbital by default — orbit requires an affirmative kick, so the gun's failure mode is disposal, not debris; (3) the 500 MWh battery farm is a merchant grid-storage asset between launches; (4) gun (all-weather) and beam (clear-sky) hedge each other's availability; (5) engineless vehicles make marginal airframe cost trivial.

**Hidden liabilities opened as work items:** beamed-line weather/clearance availability unquantified (item 21 — first cut now published: ~200 flyable days/yr); tube exit aperture and km-scale expansion unaddressed (23); relay μrad pointing under load likely 2–3× mass growth, and cargo beam-loss impact footprints undrafted (24); dual-use/ITAR posture for a steerable near-GW array to be decided deliberately, before external framing decides it for us.

**Peer-review posture:** the study survives review as a *concept/architecture paper* (Acta Astronautica / JBIS / AIAA class) contingent on item 22 — citations on every cost figure, uncertainty bands on every result, claims scoped to evidence. It is not, and does not claim to be, a validated engineering study; the gate/kill-criteria apparatus is the submission's differentiating strength and is foregrounded accordingly (§2, §13).

## 15. Open Work and Future Directions

The program's open work is maintained as a live status ledger (Appendix A), ordered easiest → hardest across three tiers: desk-and-paper items at the current phase (wave-optics completion, benchtop builds, the SIS and demand instruments, HX coupon specs, the citation and availability passes); engineering analyses for Phases 1–3 (flux-profile control, relay constellation geometry, aerocapture corridors, pulsed-power point design); and far-horizon concept work gated behind earlier data (lunar surface coilgun, Mars port, Phobos catcher). The gate item for the beam-delivery verdict is time-dependent thermal blooming coupled into propagation (item 10); the precondition for journal submission is the full citation and uncertainty pass (item 22).

---

## Appendix A — Work Item Status Ledger

*Maintained live; items close when completed, without prompting. Conventions: the ledger is ordered easiest → hardest, and IDs match that order 1–19. IDs were renumbered once to complexity order by owner decision, Jul 19, 2026, with all cross-references updated in the same edit; they are frozen henceforth. CLOSED items are immutable records. Last updated Jul 20, 2026.*

### Tier 1 — Desk & paper, current phase (0–1): items 1–10, hours to weeks each, ~$0

| # | Item | Status |
|---|---|---|
| 1 | Split-step wave-optics propagation sim | **CLOSED** — v0 + v1 gauntlet complete (0.75 vertical baseline; slant 0.78/0.22/0.03); remainder transferred to 10 |
| 2 | Benchtop builds (Inductrack drum; droplet rig) | OPEN — build sheets released; hardware ordering underway |
| 3 | NMSBA application | OPEN — triggers immediately on LLC formation |
| 4 | Phase 2 laser-lab requirements sheet; Spaceport America first contact at Phase 3 planning | OPEN |
| 5 | SIS Draft A authoring | OPEN — skeleton published; full document is a Phase 1–2 deliverable |
| 6 | Demand registry instrument (LOI template, tiers) | OPEN — pairs with 5 |
| 7 | Standards-body engagement plan (CONFERS, SmallSat) | OPEN — follows 5 |
| 8 | HX coupon test spec (hydrogen + steam coupon sets) | OPEN — Phase 1; gates Phase 2 hardware; spec extended to ≥1,000-cycle automated endurance |
| 9 | Market/utilization model (flight-rate demand curves) | OPEN |
| 10 | Phase 1 sim completion (inherits from item 1): PCI stability check, distributed-array synthesis, ≥100-draw Monte Carlo, radiometric ledger | OPEN — blooming coupling and end-of-burn sweep already delivered by v1; scope reduced |
| 20 | Cadence endurance rig spec: automated subscale coilgun, 5,000-cycle campaign, condition monitoring + cost-per-shot ledger (~$10–30k, Phase 2) | OPEN — new under cadence doctrine |
| 21 | Beamed-line availability analysis: NM cloud/wind statistics × Laser Clearinghouse windows → flyable-days model feeding the cadence economics | OPEN — **first cut v0 published Jul 20** (mmm_item21_flyable_days_v0, this directory): ~200 flyable days/yr (150–250); LCH quantified from published observatory data; availability binds at the 2,000-flights/yr tier; v1 refinement scope listed therein |
| 22 | Citation & uncertainty pass: source every cost figure, band every result, apply [E]/[I]/[S] labels line-by-line per the Epistemic Convention — precondition for journal submission AND now mandated by owner's accuracy standard | OPEN — **kickoff published Jul 20** (mmm_item22_citation_pass_v0, this directory): 11 headline rows sourced; corrections applied to this document in the same commit; full inference-chain pass remains |
| 23 | Tube exit-aperture concept: fast shutter vs. plasma window vs. per-shot membrane; km-scale thermal expansion joints | **CLOSED Jul 21, 2026** — concept selected (mmm_item23_exit_aperture_v0, this directory): two-stage muzzle vestibule — slow outer gate valve + per-shot burst membrane; phase-locked rotary shutter documented as alternate; expansion clause disposed to standard bellows practice (LIGO-class existence proof). Verification folds into item 20 (cycle life) and Phase 2 track design |
| 24 | Beam-loss range-safety footprint analysis + relay pointing-stability budget under thermal load | OPEN — red-team finding; Tier 2 |
| 25 | Trademark application: "Magnetic Matter Movers" word mark via USPTO TEAS — base fee $350/class (+$200/class surcharge if using custom goods/services description instead of the ID Manual); file after LLC formation so the LLC is owner; likely classes: research/publication services + catalog hardware (one class suffices to start). Not deadline-bound: common-law rights accrue from use, and the dated public repo establishes first use | OPEN — new Jul 20, 2026 |

### Tier 2 — Engineering analyses, Phases 1–3: items 11–16, weeks to months each, still simulation/paper

| # | Item | Status |
|---|---|---|
| 11 | Flux-profile control requirement (beam-shape modes + backscatter loop) | OPEN |
| 12 | Relay constellation geometry (orbits, count, 462 s handoff) | OPEN |
| 13 | Aerocapture corridor vs. gun dispersion + kick-stage trim budget | OPEN — first data-free Monte Carlo candidate |
| 14 | Venus corridor memo (quantifies thin/thick gap for 13) | OPEN — pairs with 13 |
| 15 | Lunar off-ramp point design (steam brake vs. semi-hard bulk; polar water bootstrap) | OPEN |
| 16 | Pulsed-power farm point design + subscale demonstrator spec | OPEN — hardest Tier 2 item; feeds System A; now carries 5,000-cycle switch/coil/flywheel life requirement |

### Tier 3 — Far-horizon concept work, Phases 3+: items 17–19, meaningful only after earlier tiers return data

| # | Item | Status |
|---|---|---|
| 17 | Lunar surface coilgun concept (290 m track; catch-mass economy) | OPEN |
| 18 | Mars port point design (station mass, tug count, emplacement manifest) | OPEN |
| 19 | Phobos catcher feasibility memo | OPEN — deliberately last: gated behind a proven Mars route |

## Appendix B — Key Reference Numbers

- Delta-v to LEO: 9.4 km/s (7.8 orbital + ~1.6 losses) · Escape from surface: 11.2 · Escape from LEO: +3.2
- Isp 900 laser-thermal hydrogen: T_gas ≈ 2,900 K; propellant fraction for 6.8 km/s = 54% (vs 86% chemical)
- Beam requirement: ~95 MW per tonne of vehicle gross (T/W 1.5, 50% coupling)
- Halbach near-field: 1 T at 1 cm gap ≈ 30 t/m² lift — 10⁸ × Earth-field pressure
- Inductrack L/D ≈ v/w; drag *power* constant with speed (magnetic lift gets cheaper as you go faster; aero drag grows as v³)
- Earth's field: 1 mPa pressure, 1 mJ/m³ — an orbital reboost resource only (ED tether: 1,555 m/s per month on 5 t)

## Appendix C — Benchtop Inductrack Build

*Magnetic Matter Movers catalog piece / scale model of the launch sled (demonstration ladder Phase 0):*

8× ½" N42 cubes in Halbach (λ = 51 mm, B0 ≈ 0.93 T), 3D-printed carrier (N-red/S-blue pole language), 30 cm aluminum drum ≥3 mm wall, 50 W motor. Lift-off at ~54 RPM; ~1 cm hover gap at 1,000–1,500 RPM; constant ~28 W drag at any speed (the launch-relevant signature). Gotchas: Halbach assembly needs a clamping jig (adjacent magnets fight the pattern); add guide rails or V-groove drum for lateral stability; cap at 1,500 RPM for rim safety. BOM ~$80–120.

## Appendix D — Document History

| Date (2026) | Event |
|---|---|
| Jul 15 | Original compilation: core architecture, physics ground rules, rejected branches, Systems A–C, Node D + water-depot revision, Mars pipeline, destination ranking |
| Jul 16 | Extension: demand generation & Slug Interface Standard |
| Jul 17 | Extension: external validation & design imports (28 GHz program) |
| Jul 19 | Extensions: wave-optics first-cut results (v0 + v1 gauntlet); test infrastructure & range plan; environmental ledger & cadence doctrine; red-team register. Ledger renumbered to complexity order (frozen) |
| Jul 20 | Epistemic Convention adopted; Cost Calibration Doctrine adopted; item-21 and item-22 first cuts published; corrections applied; items 20–25 added. Public repository and site live (prior-art date) |
| Jul 21 | Restructuring for journal layout — content preserved; structure, TOC, and section numbering added. Item 23 closed same date (exit-aperture concept note, this directory); ledger row updated. Changes go forward in dated commits |

---

*Analyses in this repository are published CC BY 4.0; hardware designs CC BY-NC 4.0; code MIT. Technical feedback via the public repository.*
