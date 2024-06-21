from fastapi import APIRouter


router = APIRouter(prefix='')


@router.get('/', include_in_schema=False)
async def main_page():
    return {'message': 'Здесь ничего нет'}
