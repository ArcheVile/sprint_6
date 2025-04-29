import pytest
from locators.locators import *

EMAIL = "vlad.slasnyy20qa@ya.ru"
PASSWORD = "12345678"

@pytest.mark.usefixtures("driver")
class TestConstructorNavigation:

    def test_go_to_constructor_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*CONSTRUCTOR_BUTTON).click()

        assert driver.find_element(*BUN_SECTION).is_displayed()

    def test_go_to_constructor_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*STELLAR_LOGO).click()

        assert driver.find_element(*BUN_SECTION).is_displayed()
