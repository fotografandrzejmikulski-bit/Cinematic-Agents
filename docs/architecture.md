# Architecture

## System boundary

Cinematic Agents is a control-plane architecture for AI-assisted filmmaking. The repository defines domain agents, artifact contracts, dependency topology, state management, and quality gates. Provider-specific execution belongs behind the generation/runtime adapter boundary.

## Control plane

The **Cinematic Commander** owns project-level intent, resolves conflicts between specialist outputs, and authorizes stage transitions. It does not replace specialist work; it adjudicates it.

## Artifact plane

Every handoff is a versioned artifact. Critical artifacts include:

- story bible
- screenplay and scene beats
- character identity lock
- set/prop bible
- camera plan
- lens/optics plan
- lighting plan
- performance/blocking plan
- physics constraints
- sound and music plans
- edit plan
- VFX plan
- generator specification
- scene state / continuity ledger
- QC report
- final master audit

## State model

The atomic unit is an 8-second scene specification. Scene state must encode at minimum:

1. narrative state
2. subject identity state
3. spatial state
4. temporal state
5. camera state
6. optical state
7. lighting state
8. performance state
9. physical state
10. audio state
11. editorial state
12. generation state
13. QC state

State changes are explicit and attributable to an upstream artifact or approved revision.

## Failure containment

A defect should travel backward only to the smallest responsible abstraction. Examples:

- identity drift → Character Architect / Continuity Intelligence
- impossible lens behavior → Lens & Optics Specialist
- inconsistent illumination → Lighting Director
- unnatural movement → Physics & Motion Supervisor
- generation syntax failure → Generative Video Architect
- editorial contradiction → Editor / Cinematic Commander

Blind whole-scene regeneration is prohibited when a localized repair is possible.

## Independence rule

The agent that produces an artifact cannot be the sole authority that approves the same artifact for release. Visual QC and Final Master Auditor therefore remain independent quality gates.

## Provider abstraction

The Generative Video Architect converts the neutral scene specification into provider-specific execution packages. The neutral specification remains the canonical creative source of truth and must not become coupled to a single generator vendor.
