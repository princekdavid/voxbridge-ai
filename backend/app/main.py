from fastapi import FastAPI
from app.api.routes import router
from app.config import settings

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(router, prefix="/api/v1")


@app.get("/", tags=["system"])
def root() -> dict[str, str]:
    return {"name": settings.app_name, "status": "foundation"}
