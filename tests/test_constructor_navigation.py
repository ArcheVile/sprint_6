# test_constructor_navigation.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from data import BASE_URL, EMAIL, PASSWORD


@pytest.mark.usefixtures("driver")
class TestConstructorNavigation:

    def login(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_ACCOUNT_BUTTON)).click()
        driver.find_element(*EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    def test_go_to_constructor_button(self, driver):
        # Выполняем логин
        self.login(driver)

        # Ожидаем, пока кнопка личного кабинета не станет кликабельной и нажимаем ее
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()

        # Ожидаем, пока кнопка конструктора не станет кликабельной и нажимаем ее
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)).click()

        # Проверяем, что мы на правильной странице
        expected_url = BASE_URL.rstrip('/') + "/constructor"  # Убираем лишний слэш, если он есть в BASE_URL
        assert driver.current_url == expected_url, f"Expected URL: {expected_url}, but got {driver.current_url}"
