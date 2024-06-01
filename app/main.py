from fastapi import FastAPI
import uvicorn

from app.kyu_4.router import router as kyu_4_router

app = FastAPI(
    title='Мои решения задач на сайте Code Wars',
    description='Здесь приведены решения задач начиная с уровня 4 kyu',
)
app.include_router(router=kyu_4_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
