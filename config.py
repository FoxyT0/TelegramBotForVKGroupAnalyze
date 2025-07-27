from pydantic_settings import BaseSettings
from typing import Optional

from dotenv import load_dotenv

import os 

load_dotenv()

class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME", "default_app_name")
    tg_bot_token: str = os.getenv("TG_BOT_TOKEN", "default_tg_bot_token")


settings = Settings()