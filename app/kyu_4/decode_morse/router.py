"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.decode_morse.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import decode_the_morse_code_kata


@router.post(
    '/decode_morse',
    summary='decode the morse code',
    description='Ссылка на задачу https://www.codewars.com/kata/54b72c16cd7f5154e9000457'
)
async def decode_morse(request_data: ShRequestData) -> ShResponseData:
    try:
        morse = decode_the_morse_code_kata.decode_bits(request_data.bits)
        solution_res = decode_the_morse_code_kata.decode_morse(morse)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'bits': request_data.bits
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
