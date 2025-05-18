import pytest
import allure
from pages.main_page import MainPage


@allure.feature("Тесты раздела 'Вопросы о важном'")
class TestFAQ:
    FAQ_DATA = [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
            "можете просто сделать несколько заказов — один за другим."),
        (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
            "Привезём его в интервале, который укажете при заказе."),
        (3, "Только начиная с завтрашнего дня. И да, придётся подождать."),
        (4, "Пока что нет! Но если что-то срочное — можно позвонить в поддержку по телефону 8 800 000-00-00"),
        (5, "Самокат приезжает к вам с полной зарядкой. Честная зарядка хватает на восемь суток — "
            "даже если будете кататься без передышек и во сне."),
        (6, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
        (7, "Да, пока самокат не привезли. А ещё можно отменить заказ до разгрузки."),
    ]

    @allure.story("Проверка соответствия ответов на вопросы")
    @pytest.mark.parametrize("question_index,expected_answer", FAQ_DATA)
    def test_faq_answer_matches_question(self, browser, question_index, expected_answer):
        """
        Проверяет, что текст ответа соответствует ожидаемому для заданного вопроса
        """
        with allure.step("Подготовка: Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.wait_for_load()

        with allure.step(f"Действие: Кликнуть на вопрос №{question_index + 1}"):
            main_page.click_faq_question(question_index)

        with allure.step("Проверка: Сравнить текст ответа с ожидаемым"):
            actual_answer = main_page.get_faq_answer_text(question_index)
            assert actual_answer == expected_answer, \
                (f"Несоответствие текста ответа для вопроса №{question_index + 1}\n"
                 f"Ожидалось: {expected_answer}\n"
                 f"Фактически: {actual_answer}")

    @allure.title("Проверка видимости всех ответов после клика")
    def test_all_answers_visibility(self, browser):
        """
        Проверяет, что все ответы становятся видимыми после клика на вопрос
        """
        with allure.step("Подготовка: Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.wait_for_load()

        for i in range(len(self.FAQ_DATA)):
            with allure.step(f"Проверка видимости ответа для вопроса №{i + 1}"):
                main_page.click_faq_question(i)
                assert main_page.is_answer_visible(i), f"Ответ №{i + 1} не отображается"