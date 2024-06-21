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
        json={'bits': bits}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'number,status_code',
    [
        (10, 200),
        (100, 200),
        (199, 200),
        (0, 422),
        (201, 422)
    ]
)
async def test_exp_summ(number, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/exp_summ',
        json={'number': number}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'runes,status_code',
    [
        ('123*45?=5?088', 200),
        ('??*??=302?', 200),
        ('19--45=5?', 200),
        ('123*45?0000=5?088', 422),
        ('123x*45?x=5?088', 422),
    ]
)
async def test_solve_runes(runes, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/solve_runes',
        json={'runes': runes}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'number,status_code',
    [
        (20, 200),
        (1000, 200),
        (4000, 200),
        (-1, 422),
        (5000, 422),
        (6000, 422),
    ]
)
async def test_hamming(number, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/hamming',
        json={'number': number}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'items,w_limit,status_code',
    [
        ([[2, 3], [6, 5], [8, 2], [4, 5], [2, 8], [5, 5], [2, 2]], 7, 200),
        ([[20, 55], [29, 94], [29, 49], [8, 40], [17, 18], [29, 10]], 6, 200),
        ([[2, 3], [6, 5], [8, 2], [4, 5], [2, 8], [5, 5], [2, 2]]*30, 7, 422),
        ([], 7, 422),
        ([[2, 3], [6, 5], [8, 2], [4, 5], [2, 8], [5, 5], [2, 2]], 100, 422),
        ([[2, 3], [6, 5], [8, 2], [4, 5], [2, 8], [5, 5], [2, 2]], -5, 422),
    ]
)
async def test_knapsack(items, w_limit, status_code, async_client: AsyncClient):
    data = {
        'items': items,
        'w_limit': w_limit
    }
    response = await async_client.post(
        '/kyu_4/knapsack',
        json=data
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'matrix,status_code',
    [
        ([[4, 6],
          [3, 8]],
         200),
        ([[2, 4, 2],
          [3, 1, 1],
          [1, 2, 0]],
         200),
        ([[2, 4, 2],
          [3, 1, 1],
          [1, 2, 0, 4]],
         422),
        ([[2, 4, 2],
          [3, 1, 1],
          [1, 2, 0],
          [1, 2, 0]],
         422),
        ([[2, 4, 2, 5, 1, -5, 6, 1, 7],
          [3, 1, 1, 5, 1, -5, 6, 1, 7],
          [1, 2, 0, 5, 1, -5, 6, 1, 7],
          [3, 1, 1, 5, 1, -5, 6, 1, 7],
          [3, 1, 1, 5, 1, -5, 6, 1, 7],
          [3, 1, 1, 5, 1, -5, 6, 1, 7],
          [3, 1, 1, 5, 1, -5, 6, 1, 7],
          [3, 1, 1, 5, 1, -5, 6, 1, 7],
          [3, 1, 1, 5, 1, -5, 6, 1, 7]],
         422),
    ]
)
async def test_determinant(matrix, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/determinant',
        json={'matrix': matrix}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'text,status_code',
    [
        ('e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e', 200),
        ("  //wont won't won't ", 200),
        ("  //wont won't won't "*100, 422)
    ]
)
async def test_top_3_words(text, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/top_3_words',
        json={'text': text}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'number,status_code',
    [
        (2017, 200),
        (59884848459853, 200),
        (7_094_853_987_630_485_309_485, 422)
    ]
)
async def test_next_bigger(number, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/next_bigger',
        json={'number': number}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'player_hand,opponent_hand,status_code',
    [
        ('2H 3H 4H 5H 6H', 'KS AS TS QS JS', 200),
        ('2H 3H 4H 5H 6H', 'AS AD AC AH JD', 200),
        ('2H 3H 4H 5H 6H 7H', 'AS AD AC AH JD 8H', 422),
        ('2H 3H 4H 5H -2H', 'AS AD AC AH JD', 422),
        ('2H 3H 4H 5H 6H', 'AS DD AC AH JD', 422)
    ]
)
async def test_poker_hand(player_hand, opponent_hand, status_code, async_client: AsyncClient):
    data = {
        'player_hand': player_hand,
        'opponent_hand': opponent_hand
    }
    response = await async_client.post(
        '/kyu_4/poker_hand',
        json=data
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'triplets,status_code',
    [
        ([['t', 'u', 'p'],
          ['w', 'h', 'i'],
          ['t', 's', 'u'],
          ['a', 't', 's'],
          ['h', 'a', 'p'],
          ['t', 'i', 's'],
          ['w', 'h', 's']],
         200),
        ([['t', 'u', 'h'],
          ['w', 'h', 'i'],
          ['t', 's', 'u'],
          ['a', 't', 's'],
          ['w', 'a', 'p'],
          ['t', 'i', 's'],
          ['w', 'h', 's']],
         422),
        ([['t', 'u', 'p'],
          ['w', 'h', 'i'],
          ['t', 's', 'u'],
          ['a', 't', 's'],
          ['h', 'a', 'p'],
          ['t', 'i', 's'],
          ['w', 'h', 's']]*100,
         422),
    ]
)
async def test_recover_secret(triplets, status_code, async_client: AsyncClient):
    response = await async_client.post(
        '/kyu_4/recover_secret',
        json={'triplets': triplets}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'action,number,status_code',
    [
        ('to_roman', '200', 200),
        ('to_roman', '6000', 422),
        ('to_roman', '-20', 422),
        ('to_romans', '500', 422),
        ('to_roman', '500.2', 422),
        ('to_roman', '1x', 422),
        ('from_roman', 'CC', 200),
        ('from_roman', 'MM', 200),
        ('from_roman', 'AM', 422),
        ('froms_roman', 'CC', 422),
        ('from_roman', 'MI'*20, 422)
    ]
)
async def test_roman_numerals(action, number, status_code, async_client: AsyncClient):
    response = await async_client.post(
        f'/kyu_4/roman_numerals/{action}',
        json={'number': number}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    's1,s2,status_code',
    [
        ('Are they here', 'yes, they are here', 200),
        ('Sadus:cpms>orqn3zecwGvnznSgacs', 'MynwdKizfd$lvse+gnbaGydxyXzayp', 200),
        ('Are they here'*300, 'yes, they are here', 422),
        ('Are they here', 'yes, they are here'*300, 422)
    ]
)
async def test_string_mix(s1, s2, status_code, async_client: AsyncClient):
    data = {
        's1': s1,
        's2': s2
    }
    response = await async_client.post(
        f'/kyu_4/string_mix',
        json=data
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'number,status_code',
    [
        (300, 200),
        (19789, 200),
        (21000, 422),
        (-3090, 422)
    ]
)
async def test_twice_linear(number, status_code, async_client: AsyncClient):
    response = await async_client.post(
        f'/kyu_4/twice_linear',
        json={'number': number}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'path,status_code',
    [
        ('r5L2l4', 200),
        ('r41Rr100lR23R9lR92R75', 200),
        ('r5L2l4AB', 422),
        ('r-5L2l4', 422)
    ]
)
async def test_where_are_you(path, status_code, async_client: AsyncClient):
    response = await async_client.post(
        f'/kyu_4/where_are_you',
        json={'path': path}
    )
    assert response.status_code == status_code
