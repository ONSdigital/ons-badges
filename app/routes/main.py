import os

from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
router = APIRouter()


# Serve frontends static files
router.mount("/static", StaticFiles(directory="app/static"), name="static")


@router.get("/")
async def root():
    index_path = os.path.join("app", "static", "index.html")
    return FileResponse(index_path)


@router.get("/health")
async def health():
    return {"message": "OK"}
