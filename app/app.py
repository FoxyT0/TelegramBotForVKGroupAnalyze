from fastapi import FastAPI

from config.config_reader import config


app = FastAPI()


@app.get("/")
async def info():
    print(config.tg_bot_token)
    return {
        "app_name": config.app_name,
        "bot_token": config.tg_bot_token
    }
