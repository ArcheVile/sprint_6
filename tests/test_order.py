import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Тесты заказа самоката")
class TestOrderScooter:
    UPPER_ORDER_DATA = {
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, ул. Ленина, 1",
        "metro": "Чистые пруды",
        "phone": "+79998887766",
        "date": "01.01.2023",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Тестовый заказ"
    }

    LOWER_ORDER_DATA = {
        "name": "Петр",
        "surname": "Петров",
        "address": "Санкт-Петербург, Невский пр., 10",
        "metro": "Адмиралтейская",
        "phone": "+79997776655",
        "date": "02.02.2023",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "Еще один тестовый заказ"
    }

    @allure.title("Заказ самоката через верхнюю кнопку")
    def test_order_via_upper_button(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.wait_for_load()

        with allure.step("Нажать верхнюю кнопку заказа"):
            main_page.click_upper_order_button()

        self._complete_order_flow(order_page, self.UPPER_ORDER_DATA)

    @allure.title("Заказ самоката через нижнюю кнопку")
    def test_order_via_lower_button(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.wait_for_load()

        with allure.step("Нажать нижнюю кнопку заказа"):
            main_page.click_lower_order_button()

        self._complete_order_flow(order_page, self.LOWER_ORDER_DATA)

    def _complete_order_flow(self, order_page, order_data):
        with allure.step("Заполнить первую страницу заказа"):
            order_page.fill_first_page(
                order_data["name"],
                order_data["surname"],
                order_data["address"],
                order_data["metro"],
                order_data["phone"]
            )

        with allure.step("Заполнить вторую страницу заказа"):
            order_page.fill_second_page(
                order_data["date"],
                order_data["rental_period"],
                order_data["color"],
                order_data["comment"]
            )

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление"):
            assert order_page.is_order_success_modal_displayed()