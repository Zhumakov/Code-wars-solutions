"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from typing import Union

from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    items: list[list[int]] = Field(
        ...,
        min_length=1,
        max_length=200,
        description='Список предметов, представленный в формате `[вес, стоимость]`,'
                    'количество предметов должно быть в диапазоне **от 1 до 200**'
    )
    w_limit: int = Field(
        ...,
        ge=1,
        le=80,
        description='Число, представляющее максимальную вместимость рюкзака'
    )


class ShResponseData(BaseModel):
    result: list[Union[int, list]] = Field(
        ...,
        description='Возвращает список максимальной стоимости с отсортированными '
                    'списками всех списков предметов, которые также отсортированы.'
                    'Т.е. данные представляются в формате:'
                    '`[max_value, sorted_list( sorted_list A ,sorted_list B, ... )]`'
    )
