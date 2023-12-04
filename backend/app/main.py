from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.middleware.cors import CORSMiddleware
from redis import asyncio as aioredis

from app.core.config import settings
from app.apis.base import api_router

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = start_application()

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(settings.REDIS)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")