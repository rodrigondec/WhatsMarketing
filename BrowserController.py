from selenium.webdriver import Firefox, Chrome
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.common.keys import Keys


class BrowserController:
    def __init__(self, browser=None):
        self.driver = None
        if browser is 'Firefox':
            self.initFirefox()
        elif browser is 'Chrome':
            self.initChrome()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def init_firefox(self):
        self.driver = Firefox()

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

    def test_firefox(self):
        driver = Firefox()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.close()

    def test_chrome(self):
        driver = Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.close()

    def send_message(self, num=5584998184097, msg='ola'):
        self.driver.get('https://api.whatsapp.com/send?phone={}&text={}'.format(num, msg))

