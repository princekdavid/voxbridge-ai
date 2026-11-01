from fastapi import APIRouter
from app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="voxbridge-api")


@router.get("/capabilities", tags=["system"])
def capabilities() -> dict:
    return {
        "input_media": ["mp3", "wav", "mp4", "mov"],
        "source_language_initial": "en",
        "target_language_initial": "hi",
        "pipeline_implemented": False,
        "note": "Foundation only; media ingest and AI stages are planned.",
    }
