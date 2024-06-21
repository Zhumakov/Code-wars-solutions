"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from typing import Literal

from pydantic import BaseModel, Field


class ShRequestData(BaseModel):
    player_hand: str = Field(
        '2H 3H 4H 5H 6H',
        pattern='^([0-9TJQKA][SHDC] ?){5}$',
        description='Строка, представляющая собой руку игрока, например: `2H 3H 4H 5H 6H`'
    )
    opponent_hand: str = Field(
        'KS AS TS QS JS',
        pattern='^([0-9TJQKA][SHDC] ?){5}$',
        description='Строка, представляющая собой руку оппонента, например: `KS AS TS QS JS`'
    )


class ShResponseData(BaseModel):
    result: Literal['Loss', 'Tie', 'Win'] = Field(..., description='Результат выполнения, строка')
