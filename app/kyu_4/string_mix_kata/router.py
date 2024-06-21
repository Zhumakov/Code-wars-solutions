"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException, APIRouter

from app.kyu_4.string_mix_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import strings_mix_kata


router = APIRouter(prefix='')


@router.post(
    '/string_mix',
    summary='string mix',
    description='Ссылка на задачу https://www.codewars.com/kata/5629db57620258aa9d000014'
)
async def string_mix(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = strings_mix_kata.mix(request.s1, request.s2)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                's1': request.s1,
                's2': request.s2
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
