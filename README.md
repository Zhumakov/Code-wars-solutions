Мои решения различных задач с **Code Wars**

Чтобы использовать API, необходимо отправлять запросы **POST** на соответствующий URL-адрес.
Пример обращения к API с помощью библиотеки **request**:
```angular2html
import requests


url = "http://127.0.0.1:8000/kyu_4/exp_summ"

response = requests.post(url, json=20)
print(response.json())

>>>627
```
В случае когда необходимо передать несколько аргументов,
вам нужно использовать словарь и передать его в json:
```angular2html
import requests

url = "http://127.0.0.1:8000/kyu_4/poker_hand"
data = {
    'player_hand': '2H 3H 4H 5H 6H',
    'opponent_hand': 'KS AS TS QS JS'
}

response = requests.post(url, json=data)
print(response.json())

>>>Lose
```

В [документации](http://localhost/docs) **Swagger UI** описаны все эндпоинты и принимаемые значения,
также описана валидация входных значений, например для первого примера диапазон принимаемых значений - 
от 1 до 200 включительно