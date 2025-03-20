import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
router = APIRouter()


@router.get("/")
async def root():
    index_path = os.path.join("app", "static", "index.html")
    print("index_path", index_path)
    return FileResponse(index_path)


@router.get("/health")
async def health():
    return {"message": "OK"}
