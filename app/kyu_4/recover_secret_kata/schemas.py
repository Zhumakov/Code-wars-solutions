"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    triplets: list[list[str]] = Field(
        default=[
            ['t', 'u', 'p'],
            ['w', 'h', 'i'],
            ['t', 's', 'u'],
            ['a', 't', 's'],
            ['h', 'a', 'p'],
            ['t', 'i', 's'],
            ['w', 'h', 's']
        ],
        min_length=1,
        max_length=500,
        description='Тройки символов, из которых можно составить строку, '
                    'в примере получается строка whatisup'
    )


class ShResponseData(BaseModel):
    result: str = Field(..., description='Результат выполнения, строка')
