import time
from BaseClass import MethodsForApp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Locators:
    Search_button = (By.LINK_TEXT, "Картинки")
    Picture_element = (By.CLASS_NAME, "cl-teaser__link")
    Enter = (By.ID, "text")
    Move_right = (By.CLASS_NAME, "cl-viewer-navigate__item_right")
    Move_left = (By.CLASS_NAME, "cl-viewer-navigate__item_left")


class YaSearch(MethodsForApp):
    def search_image_button(self):
        try:
            search = self.find_image_button(Locators.Search_button)
            search.send_keys(Keys.ENTER)
            # time.sleep(5)
        except:
            print("Не удалось найти кнопку")

    def check_url(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            # time.sleep(10)
            if self.driver.current_url == "https://yandex.ru/images/?utm_source=main_stripe_big":
                print("Ссылки совпадают")
            else:
                print("Ссылки неодинаковы")
        except:
            print("Не удалось сравнить ссылки")

    def click_to_picture(self):
        try:
            click = self.picture(Locators.Picture_element)
            click.click()
            time.sleep(2)
        except:
            print("Картинка не найдена")

    def move(self):
        try:
            move_right = self.move_r(Locators.Move_right)
            check_image_1 = self.driver.current_url
            move_right.click()
            time.sleep(3)
            move_left = self.move_l(Locators.Move_left)
            move_left.click()
            time.sleep(3)
            check_image_2 = self.driver.current_url
            if check_image_1 == check_image_2:
                print("Картинки совпадают")
            else:
                print("Картинки несовпадают")
        except:
            print("Ошибка")
