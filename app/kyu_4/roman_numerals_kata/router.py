"""Этот модуль создаёт эндпоинт для задачи."""
import re
from typing import Literal

from fastapi import status, HTTPException, APIRouter

from app.kyu_4.roman_numerals_kata.schemas import ShRequestData
from app.logger import error_logger
from solutions.kyu_4 import roman_numerals_kata


router = APIRouter(prefix='')


@router.post(
    '/roman_numerals/{action}',
    summary='roman numerals helper',
    description='Ссылка на задачу https://www.codewars.com/kata/51b66044bce5799a7f000003'
)
async def roman_numerals(
        action: Literal['to_roman', 'from_roman'],
        request: ShRequestData
):
    helper = roman_numerals_kata.RomanNumerals
    match action:
        case 'to_roman':
            try:
                number = int(request.number)
            except ValueError:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail='Передаваемой строкой должно быть целое число')

            if not (1 <= number <= 5000):
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail='Число должно быть в диапазоне от 1 до 5000')
            try:
                solution_res = helper.to_roman(number)
                return solution_res

            except Exception:
                error_logger.error(
                    msg='Unknown Exception',
                    extra={
                        'action': action,
                        'number': request.number
                    },
                    exc_info=True
                )
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        case 'from_roman':
            if re.findall('[^MCDXLIV]', request.number):
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail='Строка содержит недопустимые символы')
            if not 1 <= len(request.number) <= 30:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail='Длина строки должна быть от 1 до 30 символов')

            try:
                solution_res = helper.from_roman(request.number)
                return solution_res

            except Exception:
                error_logger.error(
                    msg='Unknown Exception',
                    extra={
                        'action': action,
                        'number': request.number
                    },
                    exc_info=True
                )
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
