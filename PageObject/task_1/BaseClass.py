from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MethodsForApp:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://yandex.ru/"

    def to_site(self):
        return self.driver.get(self.url)

    def find_search_box(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def check_suggests(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def click_enter(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

