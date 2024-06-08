"""Этот модуль создаёт объект с настройками окружения."""

from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: Literal['INFO', 'WARNING', 'ERROR']

    class Config:
        env_file = '.env'


settings = Settings()
