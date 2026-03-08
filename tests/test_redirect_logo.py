import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage

@allure.feature('Логотипы')
class TestLogoRedirect:
    @allure.title('Клик по логотипу Самоката возвращает на главную')
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.click_order_button_header()  
        main_page.click_logo_scooter()
        assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Клик по логотипу Яндекса открывает Дзен')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        original_window = driver.current_window_handle
        main_page.click_logo_yandex()

        new_window = main_page.wait_for_new_window(original_window)
        main_page.switch_to_window(new_window)
        main_page.wait_for_url_not_blank()

        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"Ожидался Дзен или Яндекс, получен {current_url}"

        driver.close()
        main_page.switch_to_window(original_window)
