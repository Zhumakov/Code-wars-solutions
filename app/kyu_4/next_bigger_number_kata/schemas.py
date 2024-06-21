"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field, field_validator


class ShRequestData(BaseModel):
    number: int = Field(
        2017,
        description='Положительное целое число **длинной до 20** цифр'
    )

    @field_validator('number')
    def validate_number(cls, value):
        if len(str(value)) >= 20:
            raise ValueError('Длинна числа должна быть не более 20 цифр')

        return value


class ShResponseData(BaseModel):
    result: int = Field(..., description='Результат выполнения, целое число')
