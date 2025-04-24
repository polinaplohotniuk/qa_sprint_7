import requests
import string
import random
from urls import MAIN_URL, CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL

# регистрирует нового курьера и возвращает данные курьера
def register_new_courier_and_return_courier_data(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)
    courier_data = response.json()

    if response.status_code == 201:
        courier_data["login"] = login
        courier_data["password"] = password
        courier_data["firstName"] = first_name

    return courier_data

# генерирует случайную строку заданной длины
def generate_random_string(length):
    letters = string.ascii_lowercase  # Строчные латинские буквы
    random_string = "".join(random.choice(letters) for i in range(length))  # Генерируем случайную строку
    return random_string

# генерирует случайные данные для курьера
def generate_courier_data():
    courier_data = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data["login"] = login
    courier_data["password"] = password
    courier_data["firstName"] = first_name

    return courier_data

# выполняет логин курьера
def courier_login(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload) # Отправляем POST-запрос, используя json=payload
    return response

# удаляет курьера по ID
def delete_courier(id):
    requests.delete(f"{MAIN_URL}{DELETE_COURIER_URL}{id}")
