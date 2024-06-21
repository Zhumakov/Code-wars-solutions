"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.where_are_you_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import where_are_you_kata


@router.post(
    '/where_are_you',
    summary='where_are_you',
    description='Ссылка на задачу https://www.codewars.com/kata/5a0573c446d8435b8e00009f'
)
async def where_are_you(request: ShRequestData) -> ShResponseData:
    try:
        explorer = where_are_you_kata.Explorer()
        solution_res = explorer.i_am_here(request.path)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'path': request.path
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

