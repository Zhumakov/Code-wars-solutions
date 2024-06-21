"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.hamming_number_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import hamming_numbers_kata


@router.post(
    '/hamming',
    summary='humming numbers',
    description='Ссылка на задачу https://www.codewars.com/kata/526d84b98f428f14a60008da'
)
async def hamming(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = hamming_numbers_kata.hamming(request.number)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'number': request.number
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
