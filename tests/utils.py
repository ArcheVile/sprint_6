import random
import string

def generate_email():
    name = ''.join(random.choices(string.ascii_lowercase, k=6))
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{name}_student_005_{digits}@ya.ru"

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))