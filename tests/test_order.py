import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Тесты заказа самоката")
class TestOrderScooter:
    ORDER_DATA = [
        pytest.param(
            {
                "name": "Иван",
                "surname": "Иванов",
                "address": "Москва, ул. Ленина, 1",
                "metro": "Чистые пруды",
                "phone": "+79998887766",
                "date": "01.01.2023",
                "rental_period": "сутки",
                "color": "black",
                "comment": "Тестовый заказ"
            },
            0,  # индекс верхней кнопки
            id="upper_button_order"
        ),
        pytest.param(
            {
                "name": "Петр",
                "surname": "Петров",
                "address": "Санкт-Петербург, Невский пр., 10",
                "metro": "Адмиралтейская",
                "phone": "+79997776655",
                "date": "02.02.2023",
                "rental_period": "двое суток",
                "color": "grey",
                "comment": "Еще один тестовый заказ"
            },
            1,  # индекс нижней кнопки
            id="lower_button_order"
        )
    ]

    @pytest.fixture
    def setup_order(self, browser, request):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.open()
            main_page.accept_cookies()

        button_index = request.param[1]
        with allure.step(f"Нажать кнопку заказа (индекс {button_index})"):
            main_page.click_order_button(button_index)

        return order_page, request.param[0]

    @pytest.mark.parametrize("setup_order", ORDER_DATA, indirect=True)
    @allure.title("Заказ самоката через разные кнопки")
    def test_order_scooter(self, setup_order):
        order_page, order_data = setup_order

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