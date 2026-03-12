import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from data_generators import generate_order_data

@allure.feature('Заказ самоката')
class TestOrder:
    def test_order_from_header(self, driver):
        order_data = generate_order_data()[0]
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        order_page = OrderPage(driver)

        with allure.step('Нажать кнопку «Заказать» в шапке'):
            main_page.click_order_button_header()

        with allure.step('Заполнить первую часть формы заказа'):
            order_page.fill_order_form_personal(
                order_data['name'],
                order_data['surname'],
                order_data['address'],
                order_data['metro'],
                order_data['phone']
            )

        with allure.step('Заполнить вторую часть формы заказа (чёрный самокат)'):
            order_page.fill_order_form_rent(
                order_data['date'],
                'сутки',
                OrderPageLocators.COLOR_BLACK,
                order_data['comment']
            )

        with allure.step('Подтвердить заказ'):
            order_page.confirm_order()

        with allure.step('Проверить появление сообщения с номером заказа'):
            assert order_page.is_order_success_message_displayed(), "Сообщение о создании заказа не появилось"

    def test_order_from_middle(self, driver):
        order_data = generate_order_data()[1]
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        order_page = OrderPage(driver)

        with allure.step('Нажать нижнюю кнопку «Заказать»'):
            main_page.click_order_button_middle()

        with allure.step('Заполнить первую часть формы заказа'):
            order_page.fill_order_form_personal(
                order_data['name'],
                order_data['surname'],
                order_data['address'],
                order_data['metro'],
                order_data['phone']
            )

        with allure.step('Заполнить вторую часть формы заказа (серый самокат)'):
            order_page.fill_order_form_rent(
                order_data['date'],
                'сутки',
                OrderPageLocators.COLOR_GREY,
                order_data['comment']
            )

        with allure.step('Подтвердить заказ'):
            order_page.confirm_order()

        with allure.step('Проверить появление сообщения с номером заказа'):
            assert order_page.is_order_success_message_displayed(), "Сообщение о создании заказа не появилось"
            