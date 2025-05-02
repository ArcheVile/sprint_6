# test_logout.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from data import EMAIL, PASSWORD, BASE_URL  # Импортируем данные из data.py

@pytest.mark.usefixtures("driver")
class TestLogout:

    def test_logout(self, driver):
        driver.get(BASE_URL)

        # Ожидание кнопки входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()

        # Ввод данных для входа
        driver.find_element(*EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        # Ожидание загрузки страницы и переход в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)
        ).click()

        # Выход из аккаунта
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGOUT_BUTTON)
        ).click()

        # Проверка, что кнопка входа снова доступна
        login_button_after_logout = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        assert login_button_after_logout.is_displayed(), "Login button is not displayed after logout"
