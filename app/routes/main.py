
from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Welcome to Hugo"}


@router.get("/health")
async def health():
    return {"message": "OK"}
