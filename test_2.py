import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://yandex.ru/')


def search_image_button():  # поиск кнопки "Картинки"
    try:
        search = driver.find_element_by_link_text('Картинки')
        search.send_keys(Keys.ENTER)

    except NoSuchElementException:
        print("Кнопка не найдена")


def check_link():  # проверка перехода по правильному URL
    driver.switch_to.window(driver.window_handles[1])
    if driver.current_url == 'https://yandex.ru/images/':
        print("Ссылки совпадают")
    else:
        print("Ссылки неодинаковы")


def open_pic():  # открытие картинки
    try:
        open = driver.find_element_by_class_name('cl-teaser__link')
        open.click()
        print("Картинка открыта")

    except NoSuchElementException:
        print("Картинка не была открыта")


def move():  # перемещение по карусели картинок и проверка на совпадение картинки
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

    except NoSuchElementException:
        print("Ошибка")


search_image_button()
time.sleep(1)
check_link()
time.sleep(1)
open_pic()
time.sleep(1)
move()
driver.quit()