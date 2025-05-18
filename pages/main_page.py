from selenium.webdriver.common.by import By
from .base_page import BasePage
from urls import Urls
import allure


class MainPage(BasePage):
    # Локаторы
    UPPER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]")
    LOWER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@id, 'accordion__heading')]")
    FAQ_ANSWERS = (By.XPATH, "//div[contains(@class, 'accordion__panel')]")

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_upper_order_button(self):
        self.click(self.UPPER_ORDER_BUTTON)
        return self  # Для поддержки fluent-интерфейса

    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_lower_order_button(self):
        self.click(self.LOWER_ORDER_BUTTON)
        return self  # Для поддержки fluent-интерфейса

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)
        self.wait_for_url(Urls.MAIN_PAGE)
        return self

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
        return self

    @allure.step("Кликнуть на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        questions = self.find_elements(self.FAQ_QUESTIONS)
        questions[index].click()
        return self

    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_faq_answer_text(self, index):
        answers = self.find_elements(self.FAQ_ANSWERS)
        return answers[index].text

    @allure.step("Проверить видимость ответа FAQ с индексом {index}")
    def is_faq_answer_visible(self, index):
        answers = self.find_elements(self.FAQ_ANSWERS)
        return answers[index].is_displayed()

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_load(self):
        self.find_element(self.UPPER_ORDER_BUTTON)
        return self

    @property
    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url