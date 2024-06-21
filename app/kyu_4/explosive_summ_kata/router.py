"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException, APIRouter

from app.kyu_4.explosive_summ_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import explosive_summ_kata


router = APIRouter(prefix='')


@router.post('/exp_summ',
             summary='explosive sum',
             description='Ссылка на задачу https://www.codewars.com/kata/52ec24228a515e620b0005ef')
async def exp_summ(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = explosive_summ_kata.exp_sum(request.number)
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
