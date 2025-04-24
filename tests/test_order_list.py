import requests
import allure
import pytest
from urls import MAIN_URL, GET_ORDER_LIST_URL

# класс, содержащий тесты для проверки получения списка заказов
class TestOrderList:

    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    @allure.description("Проверяет, что API возвращает список заказов в теле ответа при успешном запросе")
    def test_get_order_list(self): # проверяет возможность получения списка заказов через API
        payload = {'nearestStation': '["1", "2"]'}
        response = requests.get(f'{MAIN_URL}{GET_ORDER_LIST_URL}', params=payload)
        assert response.status_code == 200
        response_body = response.json()['orders']
        assert isinstance(response_body, list)
