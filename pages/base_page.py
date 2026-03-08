from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_logo_scooter(self):
        self.click_element(BasePageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_element(BasePageLocators.LOGO_YANDEX)

    def close_cookie_banner(self):
               
        try:
            banner = self.driver.find_element(*BasePageLocators.COOKIE_BANNER)
            if banner.is_displayed():
                try:
                    accept_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable(BasePageLocators.COOKIE_ACCEPT_BUTTON)
                    )
                    accept_button.click()
                except:
                    self.driver.execute_script("arguments[0].remove();", banner)
        except:
            pass  

    def wait_for_new_window(self, original_window, timeout=5):
        
        def condition(driver):
            return len(driver.window_handles) > 1
        WebDriverWait(self.driver, timeout).until(condition)
        for window in self.driver.window_handles:
            if window != original_window:
                return window
        raise Exception("Новое окно не найдено")

    def switch_to_window(self, window_handle):        
        self.driver.switch_to.window(window_handle)

    def wait_for_url_not_blank(self, timeout=10):        
        def condition(driver):
            url = driver.current_url
            return url not in ["about:blank", ""]
        WebDriverWait(self.driver, timeout).until(condition)

    def get_current_url(self):        
        return self.driver.current_url