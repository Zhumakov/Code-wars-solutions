"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
import re

from pydantic import BaseModel, Field, field_validator


class ShRequestData(BaseModel):
    runes: str = Field(
        '123*45?=5?088',
        description='Строка вида `[number][op][number]=[number]`, '
                    'например: `123*45?=5?088`'
    )

    @field_validator('runes')
    def validate(cls, value):
        invalid_chr = re.findall('[^0-9*+=?-]', value)
        if invalid_chr:
            raise ValueError('Некорректное выражение')

        numbers = re.findall('[0-9?]+', value)
        if not all(len(num) < 7 for num in numbers):
            raise ValueError('Числа в выражении должны быть меньше **1_000_000***')
        return value


class ShResponseData(BaseModel):
    result: int = Field(..., description='Результат выполнения, число')
