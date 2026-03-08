from selenium.webdriver.common.by import By

class MainPageLocators:
    FAQ_QUESTION = (By.XPATH, "//div[@data-accordion-component='AccordionItem']//div[@role='button']")
    FAQ_ANSWER = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']//p")