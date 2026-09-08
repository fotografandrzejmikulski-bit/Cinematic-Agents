# ChatGPT Integration

Cinematic Agents is designed to be exposed to ChatGPT through a secure HTTPS tool/API layer.

## Required production topology

ChatGPT → secure integration endpoint → Cinematic Agents runtime → Brainbase orchestration → specialist agents → artifacts/QC → integration endpoint → ChatGPT.

The repository includes `/v1/openai/manifest` as the machine-readable contract for an integration adapter. The runtime must be deployed behind HTTPS before connecting it to ChatGPT.

## Security

Never commit API keys, bearer tokens, cookies, private URLs, or provider credentials. Use environment variables or a managed secret store. Keep `CINEMATIC_REQUIRE_API_KEY=true` in production.

## Current Brainbase deployment

- Organization: `Moje Alterego's Team`
- Team: `General`
- Orchestration: `Cinematic Agent Swarm Ω∞`
- Orchestration ID: `b3ae2b36-a562-4edb-8464-f3bccb5b8f21`
- Members: 18 specialist agents

The GitHub repository is the versioned source of truth for agent roles, topology, contracts, schemas, and examples. Brainbase remains the managed agent runtime.
