import pytest
from selenium import webdriver
from PageClass import YaSearch


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def testing(browser):
    test_ = YaSearch(browser)
    test_.to_site()
    test_.entering("Тензор")
    test_.checking_suggests()
    test_.clicking_enter()

