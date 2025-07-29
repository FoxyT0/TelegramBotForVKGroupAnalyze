from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from dotenv import load_dotenv

import os 

load_dotenv()

class Settings(BaseSettings):
    app_name: str
    tg_bot_token: SecretStr

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()
