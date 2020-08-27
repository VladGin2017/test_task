import pytest
from selenium import webdriver
from PageClass import YaSearch


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_yandex_search(browser):
    yandex_main_page = YaSearch(browser)
    yandex_main_page.to_site()
    yandex_main_page.entering("Тензор")
    yandex_main_page.checking_suggests()
    yandex_main_page.clicking_enter()

