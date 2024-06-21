"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    number: str = Field(
        'MDCLXVI',
        description='При действии **to roman**, необходимо передать строку,'
                    'представляющую число в диапазоне **от 1 до 5000**. '
                    'При действии **from roman**, необходимо передать строку '
                    'представляющую римское число, длинна строки **от 1 до 30 символов**.'
    )
