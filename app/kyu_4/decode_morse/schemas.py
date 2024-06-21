"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    bits: str = Field(
        default='110011001100110000001100000011111100110011111100111111000000000000001100'
                '1111110011111100111111000000110011001111110000001111110011001100000011',
        max_length=10000,
        pattern='^[01]*$',
        description='Строка из `0` и `1` обозначающих код Морзе, длиной менее **10000**'
    )


class ShResponseData(BaseModel):
    result: str = Field(..., description='Результат выполнения, строка')
