"""Этот модуль создаёт роутер для задач уровня 4kyu."""
from fastapi import APIRouter

from app.kyu_4.custom_paintfuck_interpreter_kata.router import router as paintfuck_router
from app.kyu_4.decode_morse.router import router as morse_router
from app.kyu_4.explosive_summ_kata.router import router as exp_summ_router
from app.kyu_4.find_the_unknown_digit_kata.router import router as unknown_digit_router
from app.kyu_4.hamming_number_kata.router import router as hamming_router
from app.kyu_4.knapsack_problem_kata.router import router as knapsack_router
from app.kyu_4.matrix_determinant_kata.router import router as matrix_router
from app.kyu_4.most_frequently_user_kata.router import router as most_user_router
from app.kyu_4.next_bigger_number_kata.router import router as next_bigger_router
from app.kyu_4.poker_hand_kata.router import router as poker_hand_router
from app.kyu_4.recover_secret_kata.router import router as recover_secret_router
from app.kyu_4.roman_numerals_kata.router import router as roman_numerals_router
from app.kyu_4.string_mix_kata.router import router as string_mix_router
from app.kyu_4.twice_linear_kata.router import router as twice_linear_router
from app.kyu_4.where_are_you_kata.router import router as where_are_you_router


router = APIRouter(prefix='/kyu_4', tags=['4 kyu kata'])

router.include_router(paintfuck_router)
router.include_router(morse_router)
router.include_router(exp_summ_router)
router.include_router(unknown_digit_router)
router.include_router(hamming_router)
router.include_router(knapsack_router)
router.include_router(matrix_router)
router.include_router(most_user_router)
router.include_router(next_bigger_router)
router.include_router(poker_hand_router)
router.include_router(recover_secret_router)
router.include_router(roman_numerals_router)
router.include_router(string_mix_router)
router.include_router(twice_linear_router)
router.include_router(where_are_you_router)
