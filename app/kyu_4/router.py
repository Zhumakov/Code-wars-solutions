"""Этот модуль создаёт роутер для задач уровня 4kyu."""
from fastapi import APIRouter


router = APIRouter(prefix='/kyu_4', tags=['4 kyu kata'])
