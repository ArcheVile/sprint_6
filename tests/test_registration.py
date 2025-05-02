import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import BASE_URL

# URL регистрации
REGISTER_URL = BASE_URL + "register"

# Локаторы
REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок формы входа
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")


def generate_random_email():
    """Генерация случайного email для тестов"""
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"


@pytest.mark.usefixtures("driver")
class TestRegistration:

    def register(self, driver, name, email, password):
        """Универсальный метод регистрации"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NAME_INPUT)).send_keys(name)
        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    def test_successful_registration(self, driver):
        """Регистрация с валидными данными"""
        driver.get(REGISTER_URL)
        email = generate_random_email()
        self.register(driver, name="Тест", email=email, password="Valid123")

        # Ожидаем появления заголовка страницы входа после успешной регистрации
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_HEADER))

    def test_registration_with_invalid_password(self, driver):
        """Регистрация с паролем менее 6 символов"""
        driver.get(REGISTER_URL)
        email = generate_random_email()
        self.register(driver, name="Тест", email=email, password="12345")

        # Ожидаем появления ошибки о некорректном пароле
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PASSWORD_ERROR_MESSAGE))
