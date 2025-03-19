from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Welcome to the sdx-fastapi-boilerplate"}


@router.get("/health")
async def health():
    return {"message": "OK"}
