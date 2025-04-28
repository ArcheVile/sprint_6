import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

# Локаторы
REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Проверка, что после регистрации попали на форму входа
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")

def generate_random_email():
    """ Генерирует случайный email для регистрации """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8)) + "@example.com"

@pytest.mark.usefixtures("driver")
class TestRegistration:

    def register(self, driver, name, email, password):
        """ Вспомогательный метод для регистрации """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NAME_INPUT)).send_keys(name)
        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    def test_successful_registration(self, driver):
        """ Тест: успешная регистрация с валидными данными """
        driver.get("https://stellarburgers.nomoreparties.site/register")
        random_email = generate_random_email()
        self.register(driver, name="Тест", email=random_email, password="Valid123")
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_HEADER))

    def test_registration_with_invalid_password(self, driver):
        """ Тест: ошибка при регистрации с некорректным паролем (меньше 6 символов) """
        driver.get("https://stellarburgers.nomoreparties.site/register")
        random_email = generate_random_email()
        self.register(driver, name="Тест", email=random_email, password="12345")  # Пароль слишком короткий
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PASSWORD_ERROR_MESSAGE))
