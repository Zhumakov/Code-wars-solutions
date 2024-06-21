import time

from fastapi import FastAPI, Request, Response
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

from app.main_page.router import router as main_page_router
from app.kyu_4.router import router as kyu_4_router
from app.logger import endpoint_logger
from app.config import settings

app = FastAPI(
    title='Мои решения задач на сайте Code Wars',
    description='Здесь приведены решения задач начиная с уровня 4 kyu',
)

# Добавляются в app роутеры с эндпоинтами
app.include_router(router=main_page_router)
app.include_router(router=kyu_4_router)


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
