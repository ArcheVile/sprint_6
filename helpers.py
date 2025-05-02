import random
import string

def generate_random_email():
    """Генерирует случайный адрес электронной почты для регистрации"""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(8))
    return f"{random_string}@example.com"
