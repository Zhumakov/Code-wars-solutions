"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException, APIRouter

from app.kyu_4.next_bigger_number_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import next_bigger_number_kata


router = APIRouter(prefix='')


@router.post(
    '/next_bigger',
    summary='next bigger number',
    description='Ссылка на задачу https://www.codewars.com/kata/55983863da40caa2c900004e'
)
async def next_bigger(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = next_bigger_number_kata.next_bigger(request.number)
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
