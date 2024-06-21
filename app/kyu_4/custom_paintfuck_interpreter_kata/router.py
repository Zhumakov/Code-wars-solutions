"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.custom_paintfuck_interpreter_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import custom_paintfuck_interpreter_kata


@router.post(
    '/paintfuck_interpreter',
    summary='custom paintfuck',
    description='Ссылка на задачу https://www.codewars.com/kata/5868a68ba44cfc763e00008d'
)
async def custom_paintfuck_interpreter(request_data: ShRequestData) -> ShResponseData:
    try:
        solution_res = custom_paintfuck_interpreter_kata.interpreter(
            code=request_data.code,
            iterations=request_data.iterations,
            width=request_data.width,
            height=request_data.height
        )
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'code': request_data.code,
                'iterations': request_data.iterations,
                'width': request_data.width,
                'height': request_data.height
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
