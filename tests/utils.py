import random
import string

def generate_email() -> str:
    """Генерация случайного email"""
    name = ''.join(random.choices(string.ascii_lowercase, k=6))
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{name}_student_005_{digits}@ya.ru"

def generate_password(length: int = 8) -> str:
    """Генерация случайного пароля заданной длины (по умолчанию 8 символов)"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
ices(string.ascii_letters + string.digits, k=8))