import pytest
from selenium import webdriver
from PageClass import YaSearch


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test(browser):
    test_ = YaSearch(browser)
    test_.to_site()
    test_.search_image_button()
    test_.check_url()
    test_.click_to_picture()
    test_.move()

