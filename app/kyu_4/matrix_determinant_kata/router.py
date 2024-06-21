"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.matrix_determinant_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import matrix_determinant_kata


@router.post(
    '/determinant',
    summary='matrix determinant',
    description='Ссылка на задачу https://www.codewars.com/kata/52a382ee44408cea2500074c'
)
async def determinant(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = matrix_determinant_kata.determinant(request.matrix)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'items': request.matrix
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
