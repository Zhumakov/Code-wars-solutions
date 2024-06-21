"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    number: int = Field(
        ...,
        gt=0,
        lt=5000,
        description='Целое число в диапазоне **от 1 до 5000**'
    )


class ShResponseData(BaseModel):
    result: int = Field(..., description='Результат выполнения, число')
