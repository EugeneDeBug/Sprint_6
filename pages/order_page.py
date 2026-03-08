import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    @allure.step('Выбор станции метро: {subway_name}')
    def choose_subway(self, subway_name: str):        
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.send_keys(OrderPageLocators.METRO_INPUT, subway_name)
        option_locator = OrderPageLocators.subway_option_locator(subway_name)
        self.click_element(option_locator)

    def fill_order_form_personal(self, name, surname, address, metro, phone):       
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.choose_subway(metro)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбор срока аренды: {period}')
    def choose_rental_period(self, period: str):        
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)        
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.DROPDOWN_MENU)
        )
        option_locator = OrderPageLocators.rental_option_locator(period)
        self.click_element(option_locator)

    def fill_order_form_rent(self, date, rental_period, color, comment):        
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.send_keys(OrderPageLocators.DATE_INPUT, Keys.ENTER)  
        self.choose_rental_period(rental_period)
        if color == 'black':
            self.click_element(OrderPageLocators.COLOR_BLACK)
        else:
            self.click_element(OrderPageLocators.COLOR_GREY)
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)

    def confirm_order(self):        
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    def is_order_success_message_displayed(self):        
        return self.wait_for_element_visible(OrderPageLocators.ORDER_SUCCESS_MESSAGE).is_displayed()
    