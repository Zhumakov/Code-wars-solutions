import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    'code,iterations,width,height,status_code',
    [
        ('*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*', 0, 6, 9, 200),
        ('*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*', 42, 6, 9, 200),
        ('*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*', 100, 6, 9, 200),
        ('', 100, 6, 9, 422),
        ('*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*', 100, -6, 9, 422),
        ('*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*', 100, 6, 0, 422),
    ]
)
async def test_custom_paintfuck_interpreter(
        code, iterations, width, height, status_code, async_client: AsyncClient
):
    data = {
        'code': code,
        'iterations': iterations,
        'width': width,
        'height': height
    }
    response = await async_client.post(
        '/kyu_4/paintfuck_interpreter',
        json=data
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'bits,status_code',
    [
        ('11001100110011000000110000001111110011001111110011111100000000000000'
         '11001111110011111100111111000000110011001111110000001111110011001100000011', 200),
        ('000000011100000', 200),
        ('0000000111000002', 422),
        ('00000001f1100000', 422),
        ('000000011100000'*700, 422)
    ]
)
async def test_decode_morse(bits, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/decode_morse',
        json=bits
    )
    assert response.status_code == status_code
