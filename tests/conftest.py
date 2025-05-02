import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """ Фикстура для драйвера Chrome """

    # Опции для запуска браузера
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')  # Установка размера окна
    options.add_argument('--headless')  # Ожидаемый запуск без GUI (можно отключить для отладки)
    options.add_argument('--disable-gpu')  # Отключение GPU (если работает без графики)

    # Инициализация WebDriver с использованием ChromeDriverManager для автоматического управления версией драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Настройка неявного ожидания для загрузки элементов
    driver.implicitly_wait(10)

    yield driver

    # Закрытие браузера после завершения теста
    driver.quit()
