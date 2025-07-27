from functools import lru_cache

from fastapi import FastAPI

from config import settings

app = FastAPI()

@lru_cache
def get_settings():
    pass

@app.get("/")
async def info():
    return {
        "app_name": settings.app_name,
        "bot_token": settings.tg_bot_token
    }