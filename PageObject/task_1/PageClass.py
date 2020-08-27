import time
from BaseClass import MethodsForApp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Locators:
    Search_box = (By.ID, "text")
    Suggests = (By.CLASS_NAME, "mini-suggest_open")
    Enter = (By.ID, "text")


class YaSearch(MethodsForApp):
    def entering(self, word):
        searchbox = self.find_search_box(Locators.Search_box)
        searchbox.send_keys(word)
        return searchbox

    def checking_suggests(self):
        return self.check_suggests(Locators.Suggests)

    def clicking_enter(self):
        click = self.find_search_box(Locators.Enter)
        click.send_keys(Keys.ENTER)
        time.sleep(10)
