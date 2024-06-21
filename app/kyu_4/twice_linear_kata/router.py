"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException, APIRouter

from app.kyu_4.twice_linear_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import twice_linear_kata


router = APIRouter(prefix='')


@router.post(
    '/twice_linear',
    summary='twice linear',
    description='Ссылка на задачу https://www.codewars.com/kata/5672682212c8ecf83e000050'
)
async def twice_linear(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = twice_linear_kata.dbl_linear(request.number)
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
