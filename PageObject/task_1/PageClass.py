import time
from BaseClass import MethodsForApp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Locators:
    Search_box = (By.ID, "text")
    Suggests = (By.CLASS_NAME, "mini-suggest_open")
    Enter = (By.ID, "text")


class YaSearch(MethodsForApp):
    def searching_box(self, word):
        try:
            searchbox = self.find_search_box(Locators.Search_box)
            searchbox.send_keys(word)
            print("Поискавая строка найдена")
            time.sleep(3)
        except:
            print("Поисковая строка не найдена")

    def checking_suggests(self):
        try:
            suggests = self.check_suggests(Locators.Suggests)
            print("Подсказки найдены")
            time.sleep(3)
        except:
            print("Подсказки не найдены")

    def clicking_enter(self):
        try:
            click = self.find_search_box(Locators.Enter)
            click.send_keys(Keys.ENTER)
            print("Клавиша ENTER нажата")
            time.sleep(3)
        except:
            print("Нет реакции на клавишу ENTER")

