Мои решения различных задач с **Code Wars**

Чтобы использовать API, необходимо отправлять запросы **POST** на соответствующий URL-адрес.
Пример обращения к API с помощью библиотеки **request**:
```python
import request

url = "http://127.0.0.1:8000/kyu_4/poker_hand"
data = {
    'player_hand': '2H 3H 4H 5H 6H',
    'opponent_hand': 'KS AS TS QS JS'
}

response = request.post(url, json=data)
print(response.json())

>>>Lose
```

В [документации](http://localhost/docs) **Swagger UI** описаны все эндпоинты и принимаемые значения,
также описана валидация входных значений, например для примера выше описана валидация входных значений
на основе регулярного выражения.

Не все решения из папки *solutions* имеют соответсвующий эндпоинт.