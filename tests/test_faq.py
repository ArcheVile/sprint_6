import pytest
from pages.main_page import MainPage

FAQ_DATA = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    # Добавить остальные вопросы и ответы
]

@pytest.mark.parametrize("question_index,expected_answer", FAQ_DATA)
def test_faq_questions(browser, question_index, expected_answer):
    main_page = MainPage(browser)
    main_page.wait_for_load()
    main_page.click_faq_question(question_index)
    assert main_page.get_faq_answer_text(question_index) == expected_answer