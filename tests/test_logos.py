import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_scooter_logo_redirect(browser):
    main_page = MainPage(browser)
    main_page.wait_for_load()
    main_page.click_scooter_logo()
    assert browser.current_url == "https://qa-scooter.praktikum-services.ru/"


def test_yandex_logo_redirect(browser):
    main_page = MainPage(browser)
    main_page.wait_for_load()
    main_page.click_yandex_logo()

    # Переключение на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # Ожидание редиректа на Дзен
    WebDriverWait(browser, 10).until(
        lambda d: "dzen.ru" in d.current_url
    )

    assert "dzen.ru" in browser.current_url