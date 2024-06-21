"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    path: str = Field(
        'r5L2l4',
        pattern='^[0-9lrLR]*$',
        max_length=100,
        description='Строка, обозначающие команды для исследователя, не более 100 **символов**'
    )


class ShResponseData(BaseModel):
    result: list[int] = Field(..., description='Результат выполнения, список чисел, '
                                               'представляющих собой координаты')
