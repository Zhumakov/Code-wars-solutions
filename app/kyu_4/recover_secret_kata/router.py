"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.recover_secret_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import recover_a_secret_string_from_random_triplets_kata




@router.post(
    '/recover_secret',
    summary='recover a secret string from random triplets',
    description='Ссылка на задачу https://www.codewars.com/kata/53f40dff5f9d31b813000774'
)
async def recover_secret(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = recover_a_secret_string_from_random_triplets_kata.recover_secret(request.triplets)
        return ShResponseData(result=solution_res)

    except TimeoutError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Данные тройки символов не имеют решения')

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'triplets': request.triplets
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
