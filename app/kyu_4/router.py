import re
from typing import Literal

from fastapi import APIRouter, HTTPException, Query, status

from solutions.kyu_4 import (
    custom_paintfuck_interpreter_kata,
    decode_the_morse_code_kata,
    explosive_summ_kata,
    find_the_unknown_digit_kata,
    hamming_numbers_kata,
    knapsack_problem_kata,
    matrix_determinant_kata,
    most_frequently_used_kata,
    next_bigger_number_kata,
    poker_hand_kata,
    recover_a_secret_string_from_random_triplets_kata,
    roman_numerals_kata,
    strings_mix_kata,
    twice_linear_kata,
    where_are_you_kata
)

router = APIRouter(prefix='/kyu_4', tags=['4 kyu kata'])


@router.post(
    '/paintfuck_interpreter',
    summary='custom paintfuck',
    description='Ссылка на задачу https://www.codewars.com/kata/5868a68ba44cfc763e00008d'
)
async def custom_paintfuck_interpreter(
    code: str = Query(
        ...,
        min_length=1,
        max_length=2000,
        description='Код Paintfuck, который необходимо выполнить'
    ),
    iterations: int = Query(
        ...,
        ge=0,
        description='Количество итераций, которое необходимо выполнить'
    ),
    width: int = Query(
        ...,
        ge=1,
        description='Ширина сетки данных'
    ),
    height: int = Query(
        ...,
        ge=1,
        description='Высота сетки данных'
    )
) -> str:
    solution_res = custom_paintfuck_interpreter_kata.interpreter(code=code,
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
        ...,
        max_length=10000,
        regex='^[01]*$',
        description='Строка из 0 и 1 обозначающих код Морзе, длиной менее 10000'
    )
) -> str:
    solution_res = decode_the_morse_code_kata.decode_morse(bits)
    return solution_res


@router.post('/exp_summ',
             summary='explosive sum',
             description='Ссылка на задачу https://www.codewars.com/kata/52ec24228a515e620b0005ef')
async def exp_summ(
        n: int = Query(
            ...,
            ge=1,
            le=200,
            description='Целое число от 1 до 200'
        )
) -> int:
    solution_res = explosive_summ_kata.exp_sum(n)
    return solution_res


@router.post(
    '/solve_runes',
    summary='find the unknown digit',
    description='Ссылка на задачу https://www.codewars.com/kata/546d15cebed2e10334000ed9'
)
async def solve_runes(
        runes: str = Query(
            ...,
            description='Строка вида [number][op][number]=[number], '
                        'например: 123*45?=5?088'
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

    solution_res = find_the_unknown_digit_kata.solve_runes(runes)
    return solution_res


@router.post(
    '/hamming',
    summary='humming numbers',
    description='Ссылка на задачу https://www.codewars.com/kata/526d84b98f428f14a60008da'
)
async def hamming(
        number: int = Query(
            ...,
            gt=0,
            lt=5000,
            description='Целое число в диапазоне от 1 до 5000'
        )
) -> int:
    solution_res = hamming_numbers_kata.hamming(number)
    return solution_res


@router.post(
    '/knapsack',
    summary='knapsack problem',
    description='Ссылка на задачу https://www.codewars.com/kata/5c2256acb26767ff56000047'
)
async def knapsack(
        items: list[list[int]] = Query(
            ...,
            min_length=1,
            max_length=200,
            description='Список предметов, представленный в формате [вес, стоимость],'
                        'количество предметов должно быть в диапазоне от 1 до 200'
        ),
        w_limit: int = Query(
            ...,
            ge=1,
            le=80,
            description='Число, представляющее максимальную вместимость рюкзака'
        )
) -> list[int, list[list[int]]]:
    solution_res = knapsack_problem_kata.knapsack(items, w_limit)
    return solution_res


@router.post(
    '/determinant',
    summary='matrix determinant',
    description='Ссылка на задачу https://www.codewars.com/kata/52a382ee44408cea2500074c'
)
async def determinant(
    matrix: list[list[int]] = Query(
        ...,
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

    solution_res = matrix_determinant_kata.determinant(matrix)
    return solution_res


@router.post(
    '/top_3_words',
    summary='most frequently used',
    description='Ссылка на задачу https://www.codewars.com/kata/51e056fe544cf36c410000fb'
)
async def top_3_words(
        text: str = Query(
            ...,
            max_length=1000,
            description='Текст'
        )
) -> list[str]:
    solution_res = most_frequently_used_kata.top_3_words(text)
    return solution_res


@router.post(
    '/next_bigger',
    summary='next bigger number',
    description='Ссылка на задачу https://www.codewars.com/kata/55983863da40caa2c900004e'
)
async def next_bigger(
        n: int = Query(
            ...,
            description='Положительное целое число длинной до 20 цифр'
        )
) -> int:
    if len(str(n)) >= 20:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Длинна числа должна быть не более 20 цифр')

    solution_res = next_bigger_number_kata.next_bigger(n)
    return solution_res


@router.post(
    '/poker_hand',
    summary='ranking poker hands',
    description='Ссылка на задачу https://www.codewars.com/kata/5739174624fc28e188000465'
)
async def poker_hand(
        player_hand: str = Query(
            ...,
            regex='^([0-9TJQKA][SHDC] ?){5}$',
            description='Строка, представляющая собой руку игрока, например: 2H 3H 4H 5H 6H'
        ),
        opponent_hand: str = Query(
            ...,
            regex='^([0-9TJQKA][SHDC] ?){5}$',
            description='Строка, представляющая собой руку оппонента, например: KS AS TS QS JS'
        )
) -> Literal['Loss', 'Tie', 'Win']:
    solution_res = poker_hand_kata.run_kata(player_hand, opponent_hand)
    return solution_res


@router.post(
    '/recover_secret',
    summary='recover a secret string from random triplets',
    description='Ссылка на задачу https://www.codewars.com/kata/53f40dff5f9d31b813000774'
)
async def recover_secret(
        triplets: list[list[str]] = Query(
            default=[
                ['t', 'u', 'p'],
                ['w', 'h', 'i'],
                ['t', 's', 'u'],
                ['a', 't', 's'],
                ['h', 'a', 'p'],
                ['t', 'i', 's'],
                ['w', 'h', 's']
            ],
            min_length=1,
            max_length=500,
            description='Тройки символов, из которых можно составить строку, '
                        'в примере получается строка whatisup'
        )
) -> str:
    try:
        solution_res = recover_a_secret_string_from_random_triplets_kata.recover_secret(triplets)
    except TimeoutError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Данные тройки символов не имеют решения')
    return solution_res


@router.post(
    '/to_roman/{action}',
    summary='roman numerals helper',
    description='Ссылка на задачу https://www.codewars.com/kata/51b66044bce5799a7f000003'
)
async def roman_numerals(
        action: Literal['to_roman', 'from_roman'],
        number: str = Query(
            ...,
            description='При действии **to roman**, необходимо передать строку,'
                        'представляющую число в диапазоне от 1 до 5000. '
                        'При действии **from roman**, необходимо передать строку '
                        'представляющую римское число, длинна строки от 1 до 30 символов'
        )
):
    helper = roman_numerals_kata.RomanNumerals
    match action:
        case 'to_roman':
            try:
                number = int(number)
            except ValueError:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail='Передаваемой строкой должно быть целое число')

            if not (1 <= number <= 5000):
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail='Число должно быть в диапазоне от 1 до 5000')
            return helper.to_roman(number)

        case 'from_roman':
            if re.findall('[^MCDXLIV]', number):
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail='Строка содержит недопустимые символы')

            return helper.from_roman(number)


@router.post(
    '/string_mix',
    summary='string mix',
    description='Ссылка на задачу https://www.codewars.com/kata/5629db57620258aa9d000014'
)
async def string_mix(
        s1: str = Query(
            ...,
            max_length=3000,
            description='Текст'
        ),
        s2: str = Query(
            ...,
            max_length=3000,
            description='Текст'
        )
) -> str:
    solution_res = strings_mix_kata.mix(s1, s2)
    return solution_res


@router.post(
    '/twice_linear',
    summary='twice linear',
    description='Ссылка на задачу https://www.codewars.com/kata/5672682212c8ecf83e000050'
)
async def twice_linear(
        number: int = Query(
            ...,
            ge=1,
            le=20000,
            description='Число'
        )
) -> int:
    solution_res = twice_linear_kata.dbl_linear(number)
    return solution_res


@router.post(
    '/where_are_you',
    summary='where_are_you',
    description='Ссылка на задачу https://www.codewars.com/kata/5a0573c446d8435b8e00009f'
)
async def where_are_you(
        path: str = Query(
            ...,
            regex='^[0-9lrLR]*$',
            max_length=100,
            description='Строка, обозначающие команды для исследователя'
        )
) -> list[int]:
    explorer = where_are_you_kata.Explorer()
    solution_res = explorer.i_am_here(path)
    return solution_res
