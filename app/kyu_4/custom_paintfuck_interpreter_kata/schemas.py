"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    code: str = Field(
        default='*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*',
        min_length=1,
        max_length=2000,
        description='Код Paintfuck, который необходимо выполнить'
    )
    iterations: int = Field(
        default=42,
        ge=0,
        le=1000,
        description='Количество итераций, которое необходимо выполнить'
    )
    width: int = Field(
        default=6,
        ge=1,
        le=100,
        description='Ширина сетки данных'
    )
    height: int = Field(
        default=9,
        ge=1,
        le=100,
        description='Высота сетки данных'
    )


class ShResponseData(BaseModel):
    result: str = Field(..., description='Результат выполнения, строка, представляющая собой матрицу из `0` и `1`')
