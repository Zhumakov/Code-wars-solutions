from fastapi import FastAPI

from app.kyu_4.router import router as kyu_4_router

app = FastAPI(
    title='Мои решения задач на сайте Code Wars',
    description='Здесь приведены решения задач начиная с уровня 4 kyu',
)
app.include_router(kyu_4_router)
