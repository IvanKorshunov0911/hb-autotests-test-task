import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--gui', action='store', default="n",
                     help="n - for headless browser, y - for gui show")


@pytest.fixture(scope="function")
def browser(request):
    gui = request.config.getoption("gui")
    browser = None
    options = Options()
    if gui == "n":
        options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    logging.info("Quit browser")
    browser.quit()
