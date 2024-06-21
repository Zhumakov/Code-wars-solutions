"""Этот модуль создаёт Pydantic схемы для входных и выходных данных."""
from pydantic import BaseModel, Field, field_validator


class ShRequestData(BaseModel):
    matrix: list[list[int]] = Field(
        [[2, 4, 2],
         [3, 1, 1],
         [1, 2, 0]],
        description='Матрица `NxN`, состоящая из целых чисел, максимальная размерность - `8x8`'
    )

    @field_validator('matrix')
    def validate_matrix(cls, matrix):
        num_rows = len(matrix)

        for row in matrix:
            if len(row) != num_rows:
                raise ValueError('Все строки и столбцы должны быть одинаковой длины')

        if len(matrix) > 8 or len(matrix[0]) > 8:
            raise ValueError('Максимальная размерность - 8x8')

        return matrix


class ShResponseData(BaseModel):
    result: int = Field(..., description='Результат выполнения, число')
