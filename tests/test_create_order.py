import json
import pytest
import requests
import allure
from urls import MAIN_URL, CREATE_ORDER_URL
from data import OrderData

# класс, содержащий тесты для создания заказов
class TestCreateOrder:

    @allure.title('Создание заказа с различными вариантами цветов')
    @allure.description('Проверяет успешное создание заказа с указанием одного цвета (BLACK/GREY), обоих цветов и без указания цвета. Тело ответа содержит track.')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_1,  # чёрный
        OrderData.order_data_2,  # серый
        OrderData.order_data_3,  # чёрный и серый
        OrderData.order_data_4   # без цвета
    ], ids=["BLACK", "GREY", "BLACK_GREY", "NO_COLOR"])
    def test_create_order(self, order_data): # проверяет успешное создание заказа с различными данными
        order_data_json = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', data=order_data_json, headers=headers)

        assert response.status_code == 201, f"Ожидался статус код 201, получен {response.status_code}. Ответ: {response.text}"
        assert 'track' in response.text, f"В ответе отсутствует 'track'. Ответ: {response.text}"
