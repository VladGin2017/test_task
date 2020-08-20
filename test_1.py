import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://yandex.ru/')


def search_box():
    try:
        searching_box = driver.find_element_by_id('text')
        searching_box.send_keys('Тензор')
        print("Поле ввода найдено")

    except:
        print("Поле ввода не найдено")


def check_suggests():
    try:
        checking_suggests = driver.find_element_by_class_name('mini-suggest_open')
        print("Подсказки найдены")

    except:
        print("Подсказки не найдены")


def enter():
    try:
        entering = driver.find_element_by_id('text')
        entering.send_keys(Keys.ENTER)
        print("Ввод клавишей Enter")

    except:
        print("Ввод клавишей Enter недествует")


search_box()
time.sleep(1)
check_suggests()
time.sleep(1)
enter()
time.sleep(10)
driver.quit()