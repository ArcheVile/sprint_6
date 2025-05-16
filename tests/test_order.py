import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

ORDER_DATA = [
    {
        "entry_point": "upper",
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
    {
        "entry_point": "lower",
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
]


@pytest.mark.parametrize("order_data", ORDER_DATA)
def test_order_scooter(browser, order_data):
    main_page = MainPage(browser)
    main_page.wait_for_load()

    # Выбор точки входа
    if order_data["entry_point"] == "upper":
        main_page.click_upper_order_button()
    else:
        main_page.click_lower_order_button()

    order_page = OrderPage(browser)

    # Заполнение первой страницы
    order_page.fill_first_page(
        order_data["name"],
        order_data["surname"],
        order_data["address"],
        order_data["metro"],
        order_data["phone"]
    )

    # Заполнение второй страницы
    order_page.fill_second_page(
        order_data["date"],
        order_data["rental_period"],
        order_data["color"],
        order_data["comment"]
    )

    # Подтверждение заказа
    order_page.confirm_order()

    # Проверка успешного создания заказа
    assert order_page.is_order_success_modal_displayed()