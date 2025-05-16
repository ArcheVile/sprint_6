import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()