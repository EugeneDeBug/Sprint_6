import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_phone():
    return f"+7{random.randint(9000000000, 9999999999)}"

def generate_order_data():
    data_sets = [
        {
            "name": "Иван",
            "surname": "Иванов",
            "address": "ул. Ленина, д. 1",
            "metro": "Сокольники",
            "phone": generate_phone(),
            "date": "01.01.2026",
            "comment": "Позвонить за час"
        },
        {
            "name": "Петр",
            "surname": "Петров",
            "address": "пр. Мира, д. 5",
            "metro": "Чистые пруды",
            "phone": generate_phone(),
            "date": "02.02.2026",
            "comment": "Оставить у двери"
        }
    ]
    return data_sets
