import pytest
import allure
from pages.main_page import MainPage
from urls import Urls


@allure.feature("Тесты редиректов по логотипам")
class TestLogoRedirects:
    @allure.title("Проверка редиректа на главную через логотип Самоката")
    def test_scooter_logo_redirect(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.wait_for_load()

        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить URL после редиректа"):
            assert main_page.current_url == Urls.MAIN_PAGE, \
                f"Ожидался URL {Urls.MAIN_PAGE}, получен {main_page.current_url}"

    @allure.title("Проверка редиректа на Дзен через логотип Яндекса")
    def test_yandex_logo_redirect(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.wait_for_load()

        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Переключиться на новую вкладку"):
            main_page.switch_to_tab(1)

        with allure.step("Дождаться редиректа на Дзен"):
            main_page.wait_for_url_contains("dzen.ru")

        with allure.step("Проверить URL Дзена"):
            assert "dzen.ru" in main_page.current_url, \
                f"URL {main_page.current_url} не содержит 'dzen.ru'"