"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.find_the_unknown_digit_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import find_the_unknown_digit_kata


@router.post(
    '/solve_runes',
    summary='find the unknown digit',
    description='Ссылка на задачу https://www.codewars.com/kata/546d15cebed2e10334000ed9'
)
async def solve_runes(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = find_the_unknown_digit_kata.solve_runes(request.runes)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'runes': request.runes
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
