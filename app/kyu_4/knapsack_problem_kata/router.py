"""Этот модуль создаёт эндпоинт для задачи."""
from fastapi import status, HTTPException

from app.kyu_4.router import router
from app.kyu_4.knapsack_problem_kata.schemas import ShRequestData, ShResponseData
from app.logger import error_logger
from solutions.kyu_4 import knapsack_problem_kata


@router.post(
    '/knapsack',
    summary='knapsack problem',
    description='Ссылка на задачу https://www.codewars.com/kata/5c2256acb26767ff56000047'
)
async def knapsack(request: ShRequestData) -> ShResponseData:
    try:
        solution_res = knapsack_problem_kata.knapsack(request.items, request.w_limit)
        return ShResponseData(result=solution_res)

    except Exception:
        error_logger.error(
            msg='Unknown Exception',
            extra={
                'items': request.items,
                'w_limit': request.w_limit
            },
            exc_info=True
        )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
