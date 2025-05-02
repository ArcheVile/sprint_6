# test_profile_navigation.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import EMAIL, PASSWORD, BASE_URL


class TestProfileNavigation:
    def test_navigation_to_profile(self, driver):
        driver.get(BASE_URL)

        # Вход в систему
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()

        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Переход в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))
        ).click()

        # Проверка, что мы на странице профиля
        assert driver.current_url == f"{BASE_URL}/profile"

    def test_navigation_back_to_home(self, driver):
        driver.get(f"{BASE_URL}/profile")

        # Переход назад на главную страницу
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Главная']"))
        ).click()

        # Проверка, что мы на главной странице
        assert driver.current_url == BASE_URL
