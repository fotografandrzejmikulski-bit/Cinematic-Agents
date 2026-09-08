# Agent Contracts

Every agent MUST return a structured artifact with:

```yaml
artifact:
  id: unique-artifact-id
  version: semver-or-sequence
  producer: agent-id
  inputs: []
  assumptions: []
  decisions: []
  constraints: []
  outputs: []
  risks: []
  open_issues: []
  confidence: 0.0
  upstream_refs: []
```

## Conflict protocol

When two specialist outputs disagree:

1. preserve both proposals;
2. identify the exact conflicting variables;
3. score each proposal against narrative intent, continuity, physical plausibility and production feasibility;
4. escalate unresolved trade-offs to Cinematic Commander;
5. record the final decision and rationale in the artifact metadata.

## Revision protocol

A revision order must identify:

- target artifact
- defective field or behavior
- severity
- root-cause hypothesis
- exact change requested
- invariants that must remain untouched
- downstream artifacts requiring revalidation

## Release statuses

- `DRAFT`: incomplete and non-authoritative
- `REVIEW`: specialist work awaiting gate
- `REVISION_REQUIRED`: defects identified
- `APPROVED`: passed local gate
- `RELEASE_BLOCKED`: critical defect
- `MASTER_APPROVED`: final master gate passed

## Severity

- `P0`: release-blocking / catastrophic continuity or visual failure
- `P1`: major perceptual or narrative defect
- `P2`: moderate quality defect
- `P3`: cosmetic/minor defect

No P0 or P1 issue may be silently waived by the generating agent.
