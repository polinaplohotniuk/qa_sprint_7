# класс, содержащий сообщения об ошибках, связанные с курьерами
class CourierMessages:
    NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_IN_USE = "Этот логин уже используется. Попробуйте другой."
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    NOT_ENOUGH_DATA_FOR_LOGIN = "Недостаточно данных для входа"
    INVALID_LOGIN_OR_PASSWORD = "Учетная запись не найдена"

# класс, содержащий данные для создания заказов
class OrderData:
    order_data_1 = {  # данные для первого заказа
        'firstName': 'Полина',  # имя
        'lastName': 'Плохотнюк',  # фамилия
        'address': 'Пушкина 56',  # адрес доставки
        'metroStation': 1,  # ID станции метро
        'phone': '+37377777777',  # номер телефона
        'rentTime': 2,  # время аренды в днях
        'deliveryDate': '2025-04-30',  # дата доставки
        'comment': 'Люблю кататься с семьёй!',  # комментарий к заказу
        'color': ['GREY']  # цвет самоката
    }
    order_data_2 = {  # данные для второго заказа
        'firstName': 'Сергей',
        'lastName': 'Соколов',
        'address': 'Чапаева 2',
        'metroStation': 2,
        'phone': '+37388888888',
        'rentTime': 3,
        'deliveryDate': '2025-04-29',
        'comment': 'Хочу чёрный',
        'color': ['BLACK']
    }
    order_data_3 = {  # данные для третьего заказа
        'firstName': 'Андрей',
        'lastName': 'Васильев',
        'address': 'проспект Мира',
        'metroStation': 3,
        'phone': '+37388888889',
        'rentTime': 4,
        'deliveryDate': '2025-04-28',
        'comment': 'Да мне любой подойдёт',
        'color': ['BLACK', 'GRAY']
    }
    order_data_4 = {  # данные для четвертого заказа
        'firstName': 'Сабина',
        'lastName': 'Петрова',
        'address': 'Маяковского 34',
        'metroStation': 4,
        'phone': '+37399999999',
        'rentTime': 5,
        'deliveryDate': '2025-04-27',
        'comment': 'Можно и без цвета',
        'color': []  # цвет самоката (пустой список)
    }
