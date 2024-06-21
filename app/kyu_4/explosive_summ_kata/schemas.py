"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    number: int = Field(
        20,
        ge=1,
        le=200,
        description='Целое число **от 1 до 200**'
    )


class ShResponseData(BaseModel):
    result: int = Field(..., description='Результат выполнения, число')
