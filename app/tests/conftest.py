import asyncio

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app as fastapi_app


@pytest.fixture(scope='session')
def event_loop_policy(request):
    return asyncio.DefaultEventLoopPolicy()


@pytest.fixture(scope='session')
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url='http://test') as ac:
        yield ac
