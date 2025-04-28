import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Константы
EMAIL = "your_email@example.com"
PASSWORD = "your_password"

# Локаторы
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
LOGIN_LINK_FROM_REGISTER = (By.LINK_TEXT, "Войти")
FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
LOGIN_LINK_FROM_FORGOT = (By.LINK_TEXT, "Войти")
ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

@pytest.mark.usefixtures("driver")
class TestLogin:

    def login(self, driver):
        """ Вспомогательный метод логина """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    def test_login_from_main_page(self, driver):
        """ Тест: логин через главную страницу через кнопку 'Личный кабинет' """
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        self.login(driver)
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

    def test_login_from_register_form(self, driver):
        """ Тест: логин через форму регистрации (через ссылку Войти) """
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_LINK_FROM_REGISTER)).click()
        self.login(driver)
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

    def test_login_from_forgot_password_form(self, driver):
        """ Тест: логин через форму восстановления пароля (через ссылку Войти) """
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_LINK_FROM_FORGOT)).click()
        self.login(driver)
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
