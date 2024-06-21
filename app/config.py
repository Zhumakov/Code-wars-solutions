"""Этот модуль создаёт объект с настройками окружения."""

from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    MODE: Literal["DEV", "TEST", "PROD"]

    class Config:
        env_file = '.env'


settings = Settings()
