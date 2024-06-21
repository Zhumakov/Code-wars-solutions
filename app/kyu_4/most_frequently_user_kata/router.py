"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.most_frequently_user_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import most_frequently_used_kata


@router.post(
    '/top_3_words',
    summary='most frequently used',
    description='Ссылка на задачу https://www.codewars.com/kata/51e056fe544cf36c410000fb'
)
async def top_3_words(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = most_frequently_used_kata.top_3_words(request.text)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'text': request.text
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
