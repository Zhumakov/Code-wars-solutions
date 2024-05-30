import re

from fastapi import APIRouter, HTTPException, Query, status

from solutions.kyu_4 import (
    binary_with_unknown_bits,
    custom_paintfuck_interpreter,
    decode_the_morse_code,
    explosive_summ,
    find_the_unknown_digit,
    hamming_numbers,
    knapsack_problem,
    matrix_determinant,
    most_frequently_used,
)

router = APIRouter(prefix='/kyu_4', tags=['4 kyu kata'])


@router.post(
    '/binary_unknown_bits',
    summary='Binary with unknown bits',
    description='Ссылка на задачу https://www.codewars.com/kata/64348795d4d3ea00196f5e76'
)
async def binary_with_unknown_bits(
        n: int = Query(
            None, description='Целое положительное число'
        )
) -> list:
    if not n:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Необходимо передать аргумент n')
    elif n < 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Число должно быть положительным')

    solution_res = binary_with_unknown_bits.average_to_binary(n)
    return solution_res


@router.post(
    '/paintfuck_interpreter',
    summary='custom paintfuck',
    description='Ссылка на задачу https://www.codewars.com/kata/5868a68ba44cfc763e00008d'
)
async def custom_paintfuck_interpreter(
    code: str = Query(
        None,
        description='Код Paintfuck, который необходимо выполнить'
    ),
    iterations: int = Query(
        None,
        description='Количество итераций, которое необходимо выполнить,целое неотрицательное число'
    ),
    width: int = Query(
        None,
        description='Ширина сетки данных, целое положительное число'
    ),
    height: int = Query(
        None,
        description='Высота сетки данных, целое положительное число'
    )
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


@router.post(
    '/decode_morse',
    summary='decode the morse code',
    description='Ссылка на задачу https://www.codewars.com/kata/54b72c16cd7f5154e9000457'
)
async def decode_morse(
    bits: str = Query(
        None,
        description='Строка из 0 и 1 обозначающих код Морзе, длиной менее 10000'
    )
) -> str:
    if len(bits) >= 10000:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Входная строка должна иметь длинну менее 10000')

    non_bits = re.findall('[^01]', bits)
    if non_bits:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Во входной строке должны быть только 0 и 1')

    solution_res = decode_the_morse_code.decode_morse(bits)
    return solution_res


@router.post('/exp_summ',
             summary='explosive sum',
             description='Ссылка на задачу https://www.codewars.com/kata/52ec24228a515e620b0005ef')
async def exp_summ(
        n: int = Query(
            None,
            description='Целое число от 1 до 200'
        )
) -> int:
    if not (1 <= n <= 200):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Входное число должно быть в диапазоне от 1 до 200')

    solution_res = explosive_summ.exp_sum(n)
    return solution_res


@router.post(
    '/solve_runes',
    summary='find the unknown digit',
    description='Ссылка на задачу https://www.codewars.com/kata/546d15cebed2e10334000ed9'
)
async def solve_runes(
        runes: str = Query(
            '123*45?=5?088',
            description='Строка вида [number][op][number]=[number]'
        )
) -> int:
    invalid_chr = re.findall('[^0-9*+=?-]', runes)
    if invalid_chr:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Некорректное выражение')

    numbers = re.findall('[0-9?]*', runes)
    if not all(map(lambda x: len(x) < 7, numbers)):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Числа в выражении должны быть меньше 1_000_000')

    solution_res = find_the_unknown_digit.solve_runes(runes)
    return solution_res


@router.post(
    '/hamming',
    summary='humming numbers',
    description='Ссылка на задачу https://www.codewars.com/kata/526d84b98f428f14a60008da'
)
async def hamming(
        n: int = Query(
            None,
            description='Целое число в диапазоне от 1 до 5000'
        )
) -> int:
    if not (0 < n < 5000):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Число должно быть в диапазоне от 1 до 5000')

    solution_res = hamming_numbers.hamming(n)
    return solution_res


@router.post(
    '/knapsack',
    summary='knapsack problem',
    description='Ссылка на задачу https://www.codewars.com/kata/5c2256acb26767ff56000047'
)
async def knapsack(
        items: list[list[int]] = Query(
            None,
            description='Список предметов, представленный в формате [вес, стоимость],'
                        'количество предметов должно быть в диапазоне от 1 до 200'
        ),
        w_limit: int = Query(
            None,
            description='Число, представляющее максимальную вместимость рюкзака,'
                        'должно быть в диапазоне от 1 до 80'
        )
) -> list[int, list[list[int]]]:
    if not (0 < len(items) < 200):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Количество предметов должно быть в диапазоне от 1 до 200')
    if not (0 < w_limit < 80):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Максимальный вес рюкзака должен быть в диапазоне от 1 до 80')

    solution_res = knapsack_problem.knapsack(items, w_limit)
    return solution_res


@router.post(
    '/determinant',
    summary='matrix determinant',
    description='Ссылка на задачу https://www.codewars.com/kata/52a382ee44408cea2500074c'
)
async def determinant(
    matrix: list[list[int]] = Query(
        None,
        description='Матрица NxN, состоящая из целых чисел, максимальная размерность - 8x8'
    )
) -> int:
    num_rows = len(matrix)

    for row in matrix:
        if len(row) != num_rows:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail='Все строки и столбцы должны быть одинаковой длины')

    if len(matrix) > 8 or len(matrix[0]) > 8:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Максимальная размерность - 8x8')

    solution_res = matrix_determinant.determinant(matrix)
    return solution_res


@router.post(
    '/top_3_words',
    summary='most frequently used',
    description='Ссылка на задачу https://www.codewars.com/kata/51e056fe544cf36c410000fb'
)
async def top_3_words(
        text: str = Query(
            None,
            description='Текст, ограничение: 1000 символов'
        )
) -> list[str]:
    if len(text) >= 1000:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Текст должен иметь длину менее 1000 символов')

    solution_res = most_frequently_used.top_3_words(text)
    return solution_res
