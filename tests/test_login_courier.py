import requests
import pytest
import allure
from urls import MAIN_URL, LOGIN_COURIER_URL
from data import CourierMessages

# класс, содержащий тесты для логина курьера
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера (валидные данные)")
    @allure.description("Проверяет успешную авторизацию курьера с корректными логином и паролем и получение id.")
    def test_login_courier(self, create_and_delete_courier): # авторизация курьера с валидными данными
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"]
        }

        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
        assert response.status_code == 200, "Статус код ответа не 200"
        assert "id" in response.json(), "В ответе отсутствует id курьера"

    @allure.title("Авторизация с неверным логином")
    @allure.description("Проверяет, что система возвращает ошибку, если указан неверный логин.")
    def test_login_courier_with_invalid_login(self, create_and_delete_courier): # авторизация с неверным логином
        payload = {
            "login": create_and_delete_courier["password"],
            "password": create_and_delete_courier["password"]
        }

        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
        assert response.status_code == 404, "Статус код ответа не 404"
        assert response.json()["message"] == CourierMessages.ACCOUNT_NOT_FOUND, "Неверное сообщение об ошибке"


    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверяет, что система возвращает ошибку, если указан неверный пароль.")
    def test_login_courier_with_invalid_password(self, create_and_delete_courier): # авторизация с неверным паролем
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["login"]
        }

        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
        assert response.status_code == 404, "Статус код ответа не 404"
        assert response.json()["message"] == CourierMessages.ACCOUNT_NOT_FOUND, "Неверное сообщение об ошибке"


    @allure.title("Авторизация без логина")
    @allure.description("Проверяет, что система возвращает ошибку, если не указан логин.")
    def test_login_courier_without_login(self, create_and_delete_courier): # авторизация без логина
        payload = {
            "login": "",
            "password": create_and_delete_courier["password"]
        }

        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
        assert response.status_code == 400, "Статус код ответа не 400"
        assert response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA_FOR_LOGIN, "Неверное сообщение об ошибке"


    @allure.title("Авторизация без пароля")
    @allure.description("Проверяет, что система возвращает ошибку, если не указан пароль.")
    def test_login_courier_without_password(self, create_and_delete_courier): # авторизация без пароля
        payload = {
            "login": create_and_delete_courier["login"],
            "password": ""
        }

        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
        assert response.status_code == 400, "Статус код ответа не 400"
        assert response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA_FOR_LOGIN, "Неверное сообщение об ошибке"
