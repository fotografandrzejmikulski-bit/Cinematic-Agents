from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException

from .config import settings
from .models import OrchestrationRun, ProjectBrief, SceneRequest
from .orchestrator import build_run

app = FastAPI(title=settings.app_name, version="0.1.0")
ROOT = Path(__file__).resolve().parents[2]


def _auth(x_cinematic_api_key: str | None) -> None:
    if settings.require_api_key:
        if not settings.runtime_api_key or x_cinematic_api_key != settings.runtime_api_key:
            raise HTTPException(status_code=401, detail="Invalid Cinematic Agents API key")


def _manifest_paths() -> dict:
    return {
        "agents": "agents/agents.yaml",
        "orchestration": "orchestration/cinematic-swarm.yaml",
        "scene_schema": "schemas/scene-spec.schema.json",
        "qc_schema": "schemas/qc-report.schema.json",
    }


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": "0.1.0",
        "scene_duration_seconds": settings.max_scene_seconds,
        "manifests": _manifest_paths(),
    }


@app.get("/agents")
def agents(x_cinematic_api_key: str | None = Header(default=None)) -> dict:
    _auth(x_cinematic_api_key)
    return {"manifests": _manifest_paths()}


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
        "next": "POST /v1/scenes with this project_id to create an atomic scene run",
    }


@app.post("/v1/scenes", response_model=OrchestrationRun)
def create_scene_run(
    request: SceneRequest,
    x_cinematic_api_key: str | None = Header(default=None),
) -> OrchestrationRun:
    _auth(x_cinematic_api_key)
    run_id = str(uuid.uuid4())
    run = build_run(
        request.project_id,
        {
            "scene_id": request.scene_id,
            "brief": request.brief,
            "prior_scene_ids": request.prior_scene_ids,
            "references": [str(x) for x in request.references],
        },
    )
    return OrchestrationRun(
        run_id=run_id,
        project_id=request.project_id,
        status="queued",
        artifacts=[
            {
                "agent": "Cinematic Commander",
                "artifact_type": "production_plan",
                "content": {
                    "scene_id": request.scene_id,
                    "scene_duration_seconds": run.state["scene_duration_seconds"],
                    "pipeline": [step.agent for step in run.steps],
                },
            }
        ],
    )


@app.get("/v1/openai/manifest")
def openai_manifest() -> dict:
    return {
        "name": "cinematic-agents",
        "description": "18-agent cinematic production orchestration with 8-second atomic scenes.",
        "authentication": "x-cinematic-api-key",
        "server": {"protocol": "HTTPS", "style": "JSON HTTP tool contract"},
        "operations": [
            {"method": "GET", "path": "/health", "summary": "Runtime health"},
            {"method": "GET", "path": "/agents", "summary": "Agent manifest locations"},
            {"method": "POST", "path": "/projects", "summary": "Create a film project"},
            {"method": "POST", "path": "/scenes", "summary": "Create an 8-second scene orchestration run"},
        ],
    }
