import time

from fastapi import FastAPI, Request, Response
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

from app.main_page.router import router as main_page_router
from app.kyu_4.router import router as kyu_4_router
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
from app.logger import endpoint_logger
from app.config import settings

app = FastAPI(
    title='Мои решения задач на сайте Code Wars',
    description='Здесь приведены решения задач начиная с уровня 4 kyu',
)

# Добавляются в app роутеры с эндпоинтами
app.include_router(router=main_page_router)
app.include_router(router=kyu_4_router)
app.include_router(paintfuck_router)
app.include_router(morse_router)
app.include_router(exp_summ_router)
app.include_router(unknown_digit_router)
app.include_router(hamming_router)
app.include_router(knapsack_router)
app.include_router(matrix_router)
app.include_router(most_user_router)
app.include_router(next_bigger_router)
app.include_router(poker_hand_router)
app.include_router(recover_secret_router)
app.include_router(roman_numerals_router)
app.include_router(string_mix_router)
app.include_router(twice_linear_router)
app.include_router(where_are_you_router)

# Добавляется интсрументатор для сбора метрик
instrumentator = Instrumentator(
    excluded_handlers=['/metrics']
)
instrumentator.instrument(app).expose(app)


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    """
    Middleware функция, добавляющая в headers запроса время выполнения и возвращающая его.

    :param request: Запрос;
    :param call_next: То, что нужно исполнить в ответ на запрос;
    :return: Ответ выполняемого действия
    """
    start_time = time.perf_counter()
    response: Response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers['X-Process-Time'] = str(process_time)

    if request.url != 'http://solutions_app:8000/metrics' and settings.MODE != 'TEST':
        endpoint_logger.info(
            f'Request time: {request.url} | {request.method}',
            extra={
                'process_time': round(process_time, 4),
                'status_code': response.status_code,
                'url': request.url,
                'method': request.method
            })
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
