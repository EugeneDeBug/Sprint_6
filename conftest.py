import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from constants import BASE_URL

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
    
