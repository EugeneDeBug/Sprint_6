from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators

class MainPage(BasePage):
    def click_order_button_header(self):
        self.click_element(BasePageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_middle(self):
        self.scroll_to_element(BasePageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element(BasePageLocators.ORDER_BUTTON_MIDDLE)

    def click_faq_question(self, index):
        questions = self.find_elements(MainPageLocators.FAQ_QUESTION)
        questions[index].click()

    def get_faq_answer_text(self, index):
        answers = self.find_elements(MainPageLocators.FAQ_ANSWER)
        return answers[index].text
    