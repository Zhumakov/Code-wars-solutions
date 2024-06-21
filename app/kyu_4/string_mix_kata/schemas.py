"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    s1: str = Field(
        'my&friend&Paul has heavy hats! &',
        max_length=3000,
        description='Текст'
    )
    s2: str = Field(
        'my friend John has many many friends &',
        max_length=3000,
        description='Текст'
    )


class ShResponseData(BaseModel):
    result: str = Field(..., description='Результат выполнения, строка')
