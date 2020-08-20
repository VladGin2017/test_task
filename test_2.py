import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://yandex.ru/')


def search_image_button():
    try:
        search = driver.find_element_by_link_text('Картинки')
        print(search.text)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.CONTROL + Keys.TAB)

    except:
        print("Кнопка не найдена")


def check_link():
    driver.switch_to.window(driver.window_handles[1])
    if driver.current_url == 'https://yandex.ru/images/':
        print(driver.current_url)
        print("Ссылки совпадают")
    else:
        print("Ссылки неодинаковы")


def open_pic():
    try:
        open = driver.find_element_by_class_name('cl-teaser__link')
        open.click()
        print("Картинка открыта")

    except:
        print("Картинка не была открыта")


def move():
    try:
        move_right = driver.find_element_by_class_name('cl-viewer-navigate__item_right')
        check_image_1 = driver.current_url
        move_right.click()
        time.sleep(3)
        move_left = driver.find_element_by_class_name('cl-viewer-navigate__item_left')
        move_left.click()
        check_image_2 = driver.current_url
        if check_image_1 == check_image_2:
            print("Картинки совпадают")
        else:
            print("Картинки несовпадают")

    except:
        print("Ошибка")


search_image_button()
time.sleep(1)
check_link()
time.sleep(1)
open_pic()
time.sleep(1)
move()