import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    drv = webdriver.Firefox(options=options)
    drv.set_window_size(1280, 900)
    yield drv
    drv.quit()
