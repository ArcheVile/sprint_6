# test_login.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import EMAIL, PASSWORD, BASE_URL


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)

        # Ожидание кнопки входа
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()

        # Ввод данных для входа
        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))
        )
        assert driver.current_url == f"{BASE_URL}/profile"

    def test_login_from_register_form(self, driver):
        driver.get(f"{BASE_URL}/register")

        # Логин через форму регистрации
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        ).click()

        # Ввод данных для входа
        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))
        )
        assert driver.current_url == f"{BASE_URL}/profile"

    def test_login_from_forgot_password_form(self, driver):
        driver.get(f"{BASE_URL}/forgot-password")

        # Логин через форму восстановления пароля
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        ).click()

        # Ввод данных для входа
        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))
        )
        assert driver.current_url == f"{BASE_URL}/profile"
