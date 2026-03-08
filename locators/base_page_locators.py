from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR' and @href='/']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru']")
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_')]")
    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")