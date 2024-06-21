"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    number: int = Field(
        20,
        ge=1,
        le=20000,
        description='Число'
    )


class ShResponseData(BaseModel):
    result: int = Field(..., description='Результат выполнения, число')
