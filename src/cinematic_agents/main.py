from __future__ import annotations

import json
import uuid
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException

from .config import settings
from .models import OrchestrationRun, ProjectBrief, SceneRequest

app = FastAPI(title=settings.app_name, version="0.1.0")
ROOT = Path(__file__).resolve().parents[2]


def _auth(x_cinematic_api_key: str | None) -> None:
    if settings.require_api_key:
        if not settings.runtime_api_key or x_cinematic_api_key != settings.runtime_api_key:
            raise HTTPException(status_code=401, detail="Invalid Cinematic Agents API key")


def _load_manifest() -> dict:
    path = ROOT / "agents" / "agents.yaml"
    # Keep dependency footprint small: expose the raw manifest text instead of
    # making YAML parsing a hard runtime requirement.
    return {"path": str(path.relative_to(ROOT)), "exists": path.exists()}


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": "0.1.0",
        "scene_duration_seconds": settings.max_scene_seconds,
    }


@app.get("/agents")
def agents(x_cinematic_api_key: str | None = Header(default=None)) -> dict:
    _auth(x_cinematic_api_key)
    return {"agents_manifest": _load_manifest()}


@app.post("/v1/projects")
def create_project(
    brief: ProjectBrief,
    x_cinematic_api_key: str | None = Header(default=None),
) -> dict:
    _auth(x_cinematic_api_key)
    project_id = str(uuid.uuid4())
    return {
        "project_id": project_id,
        "status": "accepted",
        "brief": brief.model_dump(mode="json"),
        "orchestration": "Cinematic Agent Swarm Ω∞",
    }


@app.post("/v1/scenes", response_model=OrchestrationRun)
def create_scene_run(
    request: SceneRequest,
    x_cinematic_api_key: str | None = Header(default=None),
) -> OrchestrationRun:
    _auth(x_cinematic_api_key)
    run_id = str(uuid.uuid4())
    return OrchestrationRun(
        run_id=run_id,
        project_id=request.project_id,
        status="queued",
        blocking_issues=[
            "Agent runtime execution is intentionally separated from the HTTP contract; connect the Brainbase/OpenAI worker to /v1/scenes."
        ],
    )


@app.get("/v1/openai/manifest")
def openai_manifest() -> dict:
    """Machine-readable contract for an OpenAI/ChatGPT integration layer."""
    return {
        "name": "cinematic-agents",
        "description": "18-agent cinematic production orchestration with 8-second scene atomicity.",
        "authentication": "x-cinematic-api-key",
        "base_path": "/v1",
        "operations": [
            {"method": "GET", "path": "/health"},
            {"method": "GET", "path": "/agents"},
            {"method": "POST", "path": "/projects"},
            {"method": "POST", "path": "/scenes"},
        ],
    }
