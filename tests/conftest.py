import pytest

from curl import *

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.set_preference("signon.autofillForms", False)
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("signon.generation.enabled", False)
    options.set_preference("security.insecure_field_warning.contextual.enabled", False)
    options.add_argument("--width=2560")
    options.add_argument("--height=1440")

    browser = webdriver.Firefox(options=options)
    browser.get(main_site)

    yield browser
    browser.quit()
