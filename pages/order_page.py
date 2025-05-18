from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderPage(BasePage):
    # Локаторы для первой страницы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй страницы заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_PERIOD_OPTION_TEMPLATE = "//div[@class='Dropdown-option' and text()='{}']"
    COLOR_CHECKBOX_TEMPLATE = "//input[@id='{}']"
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    def fill_first_page(self, name, surname, address, metro_station, phone):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.SURNAME_INPUT, surname)
        self.input_text(self.ADDRESS_INPUT, address)

        # Для поля метро используем клик и выбор из списка
        self.click(self.METRO_INPUT)
        metro_option = (By.XPATH, f"//div[text()='{metro_station}']")
        self.click(metro_option)

        self.input_text(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    def fill_second_page(self, date, rental_period, color, comment):
        self.wait_for_element_visible(self.DATE_INPUT)
        self.input_text(self.DATE_INPUT, date)

        # Выбор периода аренды
        self.click(self.RENTAL_PERIOD_DROPDOWN)
        period_option = (By.XPATH, self.RENTAL_PERIOD_OPTION_TEMPLATE.format(rental_period))
        self.click(period_option)

        # Выбор цвета
        color_checkbox = (By.XPATH, self.COLOR_CHECKBOX_TEMPLATE.format(color))
        self.click(color_checkbox)

        # Комментарий
        if comment:
            self.input_text(self.COMMENT_INPUT, comment)

        self.click(self.ORDER_BUTTON)

    def confirm_order(self):
        self.wait_for_element_visible(self.CONFIRM_ORDER_BUTTON)
        self.click(self.CONFIRM_ORDER_BUTTON)

    def is_order_success_modal_displayed(self):
        try:
            return self.find_element(self.ORDER_SUCCESS_MODAL).is_displayed()
        except:
            return False