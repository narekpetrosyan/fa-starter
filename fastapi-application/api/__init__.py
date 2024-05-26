from fastapi import APIRouter
from .api_v1 import router as v1_router

api_router = APIRouter()
api_router.include_router(v1_router)
