import requests
import pytest
import allure
from urls import MAIN_URL, CREATE_COURIER_URL
from helpers import generate_courier_data
from data import CourierMessages

# тесты для проверки создания курьера
class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    @allure.description("Проверяет успешное создание курьера с валидными данными, правильный код ответа и структуру ответа.")
    def test_create_courier_success(self): # курьера можно создать, запрос возвращает правильный код ответа
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}. Ответ: {response.text}"
        assert response.json() == {'ok': True}, f"Ожидался ответ {{'ok': True}}, получен {response.json()}. Ответ: {response.text}"

    @allure.title('Попытка создания курьера с существующим логином')
    @allure.description("Проверяет, что при попытке создать курьера с логином, который уже используется, возвращается ошибка.")
    def test_create_courier_duplicate_login(self): # если создать пользователя с логином, который уже есть, возвращается ошибка
        courier_data_1 = generate_courier_data()
        payload_1 = {
            "login": courier_data_1["login"],
            "password": courier_data_1["password"],
            "firstName": courier_data_1["firstName"]
        }
        response_courier_1 = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload_1)
        assert response_courier_1.status_code == 201, f"Ожидался код 201, получен {response_courier_1.status_code}. Ответ: {response_courier_1.text}"
        assert response_courier_1.json() == {'ok': True}, f"Ожидался ответ {{'ok': True}}, получен {response_courier_1.json()}. Ответ: {response_courier_1.text}"

        courier_data_2 = generate_courier_data()
        payload_2 = {
            "login": courier_data_1["login"],
            "password": courier_data_2["password"],
            "firstName": courier_data_2["firstName"]
        }

        response_courier_2 = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload_2)
        assert response_courier_2.status_code == 409, f"Ожидался код 409, получен {response_courier_2.status_code}. Ответ: {response_courier_2.text}"
        assert response_courier_2.json()["message"] == CourierMessages.LOGIN_ALREADY_IN_USE, f"Ожидалось сообщение '{CourierMessages.LOGIN_ALREADY_IN_USE}', получено {response_courier_2.json().get('message')}. Ответ: {response_courier_2.text}"

    @allure.title('Проверка создания курьера без обязательных полей')
    @allure.description("Проверяет, что при попытке создать курьера без логина или пароля, возвращается ошибка.")
    @pytest.mark.parametrize("missing_field", ["login", "password"], ids=["without_login", "without_password"])
    def test_create_courier_missing_required_field(self, missing_field): # чтобы создать курьера, нужно передать в ручку все обязательные поля. Если одного из полей нет, запрос возвращает ошибку
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        payload.pop(missing_field)

        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA, f"Ожидалось сообщение '{CourierMessages.NOT_ENOUGH_DATA}', получено {response.json().get('message')}. Ответ: {response.text}"

    @allure.title('Попытка создания двух курьеров с одинаковыми данными')
    @allure.description("Проверяет, что нельзя создать двух курьеров с одинаковыми данными.")
    def test_create_courier_cannot_create_two_identical_couriers(self): # нельзя создать двух одинаковых курьеров
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        response1 = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)
        assert response1.status_code == 201, f"Ожидался код 201, получен {response1.status_code}. Ответ: {response1.text}"
        assert response1.json() == {'ok': True}, f"Ожидался ответ {{'ok': True}}, получен {response1.json()}. Ответ: {response1.text}"

        response2 = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        assert response2.status_code == 409, f"Ожидался код 409, получен {response2.status_code}. Ответ: {response2.text}"
        assert response2.json()["message"] == CourierMessages.LOGIN_ALREADY_IN_USE, f"Ожидалось сообщение '{CourierMessages.LOGIN_ALREADY_IN_USE}', получено {response2.json().get('message')}. Ответ: {response2.text}"
