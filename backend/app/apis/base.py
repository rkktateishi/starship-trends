from fastapi import APIRouter

from app.apis.routers import starships


api_router = APIRouter()
api_router.include_router(starships.router, prefix="/starships", tags=["starships"])