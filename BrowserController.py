from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep


class BrowserController:
    def __init__(self, browser=None):
        self.init_chrome()
        self.init_whats()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def init_chrome(self):
        self.driver = Chrome()

    def init_whats(self):
        try:
            self.driver.get("https://web.whatsapp.com/")
        except (InvalidSessionIdException, AttributeError):
            print("Navegador não iniciado")

    def close(self):
        try:
            self.driver.close()
        except (InvalidSessionIdException, AttributeError):
            print("Navegador não iniciado")

    def test_chrome(self):
        driver = Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.close()

    def send_message(self, num=5584998184097, msg='ola123'):
        self.driver.get('https://api.whatsapp.com/send?phone={}&text={}'.format(num, msg))
        self.driver.find_element_by_id('action-button').click()
        delay = 10  # seconds
        try:
            WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, '_35EW6')))
            print("Page is ready!")
            sleep(1)
            self.driver.find_element_by_class_name('_35EW6').click()
        except TimeoutException:
            print("Loading took too much time!")
