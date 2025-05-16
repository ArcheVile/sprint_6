from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.upper_order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]")
        self.lower_order_button = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")
        self.scooter_logo = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
        self.yandex_logo = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
        self.faq_questions = (By.XPATH, "//div[contains(@id, 'accordion__heading')]")
        self.faq_answers = (By.XPATH, "//div[contains(@class, 'accordion__panel')]")

    def click_upper_order_button(self):
        self.driver.find_element(*self.upper_order_button).click()

    def click_lower_order_button(self):
        self.driver.find_element(*self.lower_order_button).click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def click_faq_question(self, index):
        questions = self.driver.find_elements(*self.faq_questions)
        questions[index].click()

    def get_faq_answer_text(self, index):
        answers = self.driver.find_elements(*self.faq_answers)
        return answers[index].text

    def wait_for_load(self):
        self.wait.until(EC.visibility_of_element_located(self.upper_order_button))