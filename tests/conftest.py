import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from curl import *

@pytest.fixture(scope="function") #Фикстура для Mozilla Firefox
def driver():
    options = Options()
    
    #Отключение менеджера паролей Firefox
    options.set_preference("signon.autofillForms", False)
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("signon.generation.enabled", False)
    options.set_preference("security.insecure_field_warning.contextual.enabled", False)
    
    options.add_argument("--width=2200")
    options.add_argument("--height=1100")
     
    browser = webdriver.Firefox(options=options)
    browser.get(main_site) 
    
    yield browser
    browser.quit()

@pytest.fixture(params=[
    {
        "name": "Иван",
        "lastname": "Иванов",
        "address": "Тверская улица, 15",
        "metro": "Тверская",
        "phone": "89251241246",
        "date": "2026-02-12",
        "period":"двое суток",
        "color":"чёрный жемчуг",
        "comment": "Позвонить за 15 минут"
    }
])
def test_first_data_sets(request):
    return request.param

@pytest.fixture(params=[
    {
        "name": "Анна",
        "lastname": "Петрова",
        "address": "Ленинский проспект, 90",
        "metro": "Ленинский проспект",
        "phone": "89164536825",
        "date": "2026-02-15",
        "period":"семеро суток",
        "color":"серая безысходность",
        "comment": "Позвонить за час"
    }
])
def test_second_data_sets(request):
    return request.param