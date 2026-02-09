import allure
import time
from curl import *

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

TIMEOUT = 5

class MainPage(BasePage):
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Нажать на кнопку Заказать вверху экрана")
    def click_top_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Нажать на кнопку Заказать внизу экрана")
    def click_bottom_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BOTTOM_BUTTON)

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)

    @allure.step("Нажать кнопку «Яндекс» (открывает в новой вкладке)")
    def click_yandex_button(self, locator):
        yandex_button = self.wait.until(EC.element_to_be_clickable(locator))

        href = yandex_button.get_attribute("href")
        target = yandex_button.get_attribute("target")

        allure.attach(f"href: {href}\ntarget: {target}", name="Атрибуты кнопки «Яндекс»", attachment_type=allure.attachment_type.TEXT)

        yandex_button.click()

    @allure.step("Дождаться открытия новой вкладки и проверить URL")
    def wait_for_new_tab_and_check_url(self, expected_domain):
        try:
            self.wait.until(EC.number_of_windows_to_be(2))
            all_windows = self.driver.window_handles
            self.driver.switch_to.window(all_windows[1])
            self.wait.until(lambda d: expected_domain in d.current_url)
            current_url = self.driver.current_url

            allure.attach(current_url, name="Текущий URL новой вкладки", attachment_type=allure.attachment_type.TEXT)
            assert expected_domain in current_url, \
                f"Ожидался домен '{expected_domain}', но URL: '{current_url}'"

        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="Скриншот при ошибке переключения вкладки", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.driver.page_source, name="HTML страницы при ошибке", attachment_type=allure.attachment_type.HTML)
            raise AssertionError(f"Не удалось переключиться на вкладку с доменом '{expected_domain}'")

    @allure.step("Закрыть новую вкладку и вернуться на исходную страницу")
    def close_new_tab_and_return_to_main(self):
        self.driver.close()  # закрываем текущую (новую) вкладку
        self.driver.switch_to.window(self.driver.window_handles[0])  # переключаемся на первую вкладку

    @allure.step("Открыть страницу Самоката")
    def test_push_scooter_button(self, expected_domain):
        self.wait.until(lambda d: expected_domain in d.current_url)
        current_url = self.driver.current_url
        allure.attach(current_url, name="Текущий URL новой вкладки", attachment_type=allure.attachment_type.TEXT)
        assert expected_domain in current_url, \
            f"Ожидался домен '{expected_domain}', но URL: '{current_url}'"      
        
    @allure.step("Нажать на пункт меню списка")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Нажать на пункт меню")
    def click_menu_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def get_menu_text(self, locator) -> str:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def is_menu_text_correct(self, expected_text):
        actual_text = self.get_menu_text()
        return actual_text == expected_text


