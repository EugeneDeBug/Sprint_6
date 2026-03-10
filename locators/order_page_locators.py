from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Форма "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    DROPDOWN_MENU = (By.XPATH, "//div[@class='Dropdown-menu']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FINAL = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    # Всплывающее окно подтверждения
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, ".//div[contains(text(),'Номер заказа')]")

    @staticmethod
    def subway_option_locator(station_name: str):
        """Локатор для кнопки станции метро."""
        return (By.XPATH, f"//button[contains(., '{station_name}')]")

    @staticmethod
    def rental_option_locator(period: str):
        """Локатор для опции срока аренды."""
        return (By.XPATH, f"//div[@class='Dropdown-option' and contains(text(), '{period}')]")
    