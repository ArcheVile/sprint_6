from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from urls import Urls
import allure


class MainPage(BasePage):
    # Локаторы
    UPPER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]")
    LOWER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[id^='accordion__heading-']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[id^='accordion__panel-']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Urls.MAIN_PAGE)
        self.accept_cookies()
        return self

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)
        return self

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_upper_order_button(self):
        self.scroll_to_element(self.UPPER_ORDER_BUTTON)
        self.click(self.UPPER_ORDER_BUTTON)
        return self

    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_lower_order_button(self):
        self.scroll_to_element(self.LOWER_ORDER_BUTTON)
        self.click(self.LOWER_ORDER_BUTTON)
        return self

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)
        self.wait_for_url(Urls.MAIN_PAGE)
        return self

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        original_window = self.driver.current_window_handle
        self.click(self.YANDEX_LOGO)
        self.wait_for_new_window(original_window)
        return self

    @allure.step("Получить список вопросов FAQ")
    def get_faq_questions(self):
        return self.find_elements(self.FAQ_QUESTIONS)

    @allure.step("Получить список ответов FAQ")
    def get_faq_answers(self):
        return self.find_elements(self.FAQ_ANSWERS)

    @allure.step("Кликнуть на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        questions = self.get_faq_questions()
        self.scroll_to_element(questions[index])
        questions[index].click()
        return self

    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_faq_answer_text(self, index):
        answers = self.get_faq_answers()
        self.wait.until(
            EC.visibility_of(answers[index]),
            message=f"Ответ с индексом {index} не отображается"
        )
        return answers[index].text

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_load(self):
        self.wait.until(
            EC.visibility_of_element_located(self.UPPER_ORDER_BUTTON),
            message="Верхняя кнопка заказа не отображается"
        )
        return self

    @property
    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url