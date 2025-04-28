import pytest
from locators.locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "vlad.slasnyy20qa@ya.ru"
PASSWORD = "12345678"


@pytest.mark.usefixtures("driver")
class TestLogout:

    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Явное ожидание для кнопки входа
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()

        driver.find_element(*EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LOGOUT_BUTTON).click()

        assert driver.find_element(*LOGIN_ACCOUNT_BUTTON).is_displayed()
