import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.config import SETTINGS

router = APIRouter()


@router.get("/")
async def root():
    if SETTINGS.ui_enabled:
        index_path = os.path.join(SETTINGS.project_root, "app", "static", "index.html")
        return FileResponse(index_path)
    else:
        return {"message": "Welcome to ons-badges"}


@router.get("/health")
async def health():
    return {"message": "OK"}
