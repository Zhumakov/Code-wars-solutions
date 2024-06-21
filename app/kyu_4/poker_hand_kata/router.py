"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.poker_hand_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import poker_hand_kata


@router.post(
    '/poker_hand',
    summary='ranking poker hands',
    description='Ссылка на задачу https://www.codewars.com/kata/5739174624fc28e188000465'
)
async def poker_hand(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = poker_hand_kata.run_kata(request.player_hand, request.opponent_hand)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'player_hand': request.player_hand,
                'opponent_hand': request.opponent_hand
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
