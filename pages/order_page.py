from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы для первой страницы заказа
        self.name_input = (By.XPATH, "//input[@placeholder='* Имя']")
        self.surname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
        self.address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        self.metro_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
        self.phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        self.next_button = (By.XPATH, "//button[text()='Далее']")

        # Локаторы для второй страницы заказа
        self.date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
        self.rental_period_dropdown = (By.XPATH, "//div[text()='* Срок аренды']")
        self.rental_period_option = (By.XPATH, "//div[@class='Dropdown-option']")
        self.color_checkbox = (By.XPATH, "//input[@type='checkbox']")
        self.comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
        self.order_button = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
        self.confirm_order_button = (By.XPATH, "//button[text()='Да']")
        self.order_success_modal = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    def fill_first_page(self, name, surname, address, metro_station, phone):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.surname_input).send_keys(surname)
        self.driver.find_element(*self.address_input).send_keys(address)
        self.driver.find_element(*self.metro_input).send_keys(metro_station)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.next_button).click()

    def fill_second_page(self, date, rental_period, color, comment):
        self.wait.until(EC.visibility_of_element_located(self.date_input))

        self.driver.find_element(*self.date_input).send_keys(date)
        self.driver.find_element(*self.rental_period_dropdown).click()

        options = self.driver.find_elements(*self.rental_period_option)
        for option in options:
            if option.text == rental_period:
                option.click()
                break

        checkboxes = self.driver.find_elements(*self.color_checkbox)
        for checkbox in checkboxes:
            if color in checkbox.get_attribute("id"):
                checkbox.click()
                break

        self.driver.find_element(*self.comment_input).send_keys(comment)
        self.driver.find_element(*self.order_button).click()

    def confirm_order(self):
        self.wait.until(EC.visibility_of_element_located(self.confirm_order_button))
        self.driver.find_element(*self.confirm_order_button).click()

    def is_order_success_modal_displayed(self):
        return self.driver.find_element(*self.order_success_modal).is_displayed()