from fastapi import APIRouter, Query, HTTPException, status

from solutions.kyu_4 import (
    binary_with_unknown_bits, custom_paintfuck_interpreter
)

router = APIRouter(prefix='/kyu_4', tags=['4 kyu kata'])


@router.post('/binary_unknown_bits',
             summary='Binary with unknown bits',
             description='Ссылка на задачу https://www.codewars.com/kata/64348795d4d3ea00196f5e76'
             )
async def binary_with_unknown_bits(
        n: int = Query(None, description='Целое положительное число')
) -> list:
    if not n:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Необходимо передать аргумент n')
    elif n < 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Число должно быть положительным')

    solution_res = binary_with_unknown_bits.average_to_binary(n)
    return solution_res


@router.post('/paintfuck_interpreter',
             summary='custom paintfuck',
             description='Ссылка на задачу https://www.codewars.com/kata/5868a68ba44cfc763e00008d')
async def custom_paintfuck_interpreter(
    code: str = Query(None,
                      description='Код Paintfuck, который необходимо выполнить'),
    iterations: int = Query(None,
                            description='Количество итераций, которое необходимо выполнить,'
                                        'целое неотрицательное число'),
    width: int = Query(None,
                       description='Ширина сетки данных, целое положительное число'),
    height: int = Query(None,
                        description='Высота сетки данных, целое положительное число')
) -> str:
    if iterations < 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Количество итераций должно быть неотрицательным числом')
    elif width < 1 or height < 1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Ширина и высота должны быть положительными числами')

    solution_res = custom_paintfuck_interpreter.interpreter(code=code,
                                                            iterations=iterations,
                                                            width=width,
                                                            height=height)
    return solution_res
