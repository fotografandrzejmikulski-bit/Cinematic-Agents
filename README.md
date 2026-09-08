# Cinematic Agents Ω∞

Production-grade multi-agent cinematic intelligence system for end-to-end film and generative-video production.

## Mission

Cinematic Agents decomposes filmmaking into specialized autonomous roles coordinated by a chief cinematic orchestrator. The system is designed around deterministic handoffs, continuity control, shot-level specifications, generator abstraction, independent visual QC, and final master auditing.

## Architecture

**Core flow**

`Intent → Story → Script → Characters → Visual World → Cinematography → Optics → Lighting → Performance → Physics → Sound → Music → Edit → VFX → Generation → Continuity → Visual QC → Final Master Audit`

### Agent roster

| # | Agent | Primary responsibility |
|---|---|---|
| 01 | Cinematic Commander | Showrunner, orchestration, trade-off resolution, final authority |
| 02 | Story Architect | Premise, themes, dramaturgy, narrative architecture |
| 03 | Screenwriter | Script, dialogue, beats, scene intent |
| 04 | Character Architect | Character identity, psychology, objectives, continuity |
| 05 | Director of Photography | Framing, camera grammar, exposure, visual strategy |
| 06 | Lens & Optics Specialist | Lens behavior, focal length, DOF, distortion, optical signatures |
| 07 | Lighting Director | Key/fill/rim, practicals, exposure logic, lighting continuity |
| 08 | Production Designer | Sets, props, materials, spatial world-building |
| 09 | Performance Director | Blocking, gaze, gesture, facial and bodily performance |
| 10 | Physics & Motion Supervisor | Natural motion, gravity, cloth, particles, collision, temporal coherence |
| 11 | Sound Director | Production sound, ambience, Foley, SFX, perspective |
| 12 | Music Director | Score strategy, motifs, instrumentation, dynamics, sync |
| 13 | Editor | Rhythm, coverage, transitions, continuity, causal assembly |
| 14 | VFX Supervisor | Compositing, simulation, cleanup, invisible/visible VFX strategy |
| 15 | Generative Video Architect | Model selection, prompt compilation, generation strategy, failure recovery |
| 16 | Continuity Intelligence | State ledger, identity lock, spatial/temporal consistency |
| 17 | Visual QC Auditor | Independent shot/scene visual inspection and defect reporting |
| 18 | Final Master Auditor | End-to-end quality gate and release readiness |

## 8-second atomic scene model

The canonical unit of generation is an 8-second scene/shotspec containing:

- narrative purpose and causal context
- start state and end state
- subject identity lock
- environment and prop state
- spatial geometry and screen direction
- blocking and performance beats
- camera position, movement vector and motivation
- lens, focal length, focus path and depth of field
- exposure and optical characteristics
- lighting topology and continuity constraints
- materials, atmosphere and environmental effects
- motion/physics constraints
- production sound and music intent
- edit in/out behavior
- generator/model parameters
- negative constraints and failure risks
- continuity references
- QC acceptance criteria

## Repository layout

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── agents/
│   └── agents.yaml
├── orchestration/
│   └── cinematic-swarm.yaml
├── schemas/
│   ├── scene-spec.schema.json
│   ├── shot-state.schema.json
│   └── qc-report.schema.json
├── docs/
│   ├── architecture.md
│   ├── agent-contracts.md
│   ├── generation-pipeline.md
│   └── quality-gates.md
└── examples/
    └── scene-001.json
```

## Design principles

1. **Specialization over monolithic prompting.** Each agent owns a bounded domain.
2. **Explicit state over implicit memory.** Critical continuity lives in machine-readable state.
3. **Independent verification.** QC agents do not self-certify the work they generated.
4. **Generator abstraction.** Creative intent is separated from provider-specific syntax.
5. **Regeneration is controlled.** Defects produce targeted revision instructions rather than blind retries.
6. **Cinematic causality is mandatory.** Camera, performance, sound, light and edit choices must support story intent.
7. **No continuity drift.** Identity, geography, props, lighting and temporal states are versioned.

## Runtime

The canonical production graph is defined in `orchestration/cinematic-swarm.yaml`. The agent definitions are in `agents/agents.yaml`.

This repository is the source-of-truth specification for the Cinematic Agents team. Runtime deployment can be mapped to Brainbase, an MCP-based orchestration layer, or another compatible agent runtime without changing the cinematic contracts.

## Quality gates

A scene is not considered production-ready until:

- narrative intent is satisfied
- character identity is stable
- geography is coherent
- optical/camera behavior is plausible
- lighting continuity is preserved
- motion is physically credible
- sound perspective matches image
- edit is causally valid
- generator constraints are satisfied
- visual QC reports no release-blocking defects
- final master audit approves the complete sequence

## Status

**Architecture:** production-ready specification

**Agent count:** 18

**Canonical orchestration:** Cinematic Agent Swarm Ω∞
