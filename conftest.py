import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("-headless")  # если нужно

    # geckodriver должен быть в PATH (brew install geckodriver)
    service = Service()

    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1280, 900)

    yield driver
    driver.quit()