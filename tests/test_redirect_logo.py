import allure
from pages.main_page import MainPage
from constants import BASE_URL, DZEN_DOMAIN

@allure.feature('Логотипы')
class TestLogoRedirect:
    @allure.title('Клик по логотипу Самоката возвращает на главную')
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.click_order_button_header()
        main_page.click_logo_scooter()
        assert main_page.get_current_url() == BASE_URL

    @allure.title('Клик по логотипу Яндекса открывает Дзен')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        original_window = main_page.get_current_window_handle()
        main_page.click_logo_yandex()

        new_window = main_page.wait_for_new_window(original_window)
        main_page.switch_to_window(new_window)
        main_page.wait_for_url_not_blank()

        current_url = main_page.get_current_url()
        assert DZEN_DOMAIN in current_url, f"Ожидался Дзен, получен {current_url}"
    