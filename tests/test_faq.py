import pytest
import allure
from pages.main_page import MainPage
from data import FaqData

@allure.title('FAQ')
@allure.description('Проверка текста ответов на вопросы')
class TestFAQ:
    @pytest.mark.parametrize('index, expected_answer',
                             [(i, answer) for i, answer in enumerate(FaqData.answers)], ids=str)
    
    def test_faq_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()  
        with allure.step(f'Клик по вопросу {index + 1}'):
            main_page.click_faq_question(index)
        with allure.step('Проверка текста ответа'):
            actual_answer = main_page.get_faq_answer_text(index)
            assert actual_answer == expected_answer, f"Ожидалось: {expected_answer}, получено: {actual_answer}"