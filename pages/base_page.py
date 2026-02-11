import allure
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.driver.current_url

    @allure.step("Подождать появления номера заказа (track)")
    def wait_for_order_number(self, locator):
        wait = WebDriverWait(self.driver, 30, poll_frequency=1)  # Увеличили время до 30 сек

        try:
            # 1. Ждём видимости элемента с текстом «Номер заказа»
            order_element = wait.until(
                EC.visibility_of_element_located(locator)
            )

            # 2. Ждём, пока в тексте появятся цифры
            wait.until(
                lambda driver: re.search(r'\d+', order_element.text.strip())
            )

            full_text = order_element.text.strip()
            allure.attach(full_text, "Полный текст элемента", allure.attachment_type.TEXT)

            # 3. Извлекаем номер заказа
            match = re.search(r'Номер заказа:\s*(\d+)', full_text)
            if not match:
                match = re.search(r'(\d{4,})', full_text)  # Ищем 4+ цифр (защита от ложных срабатываний)

            if not match:
                raise ValueError(f"Не найден номер заказа в тексте: {full_text}")


            order_number = match.group(1)
            allure.attach(order_number, "Извлечённый номер", allure.attachment_type.TEXT)
            return order_number

        except TimeoutException:
            allure.attach(
                self.driver.page_source,
                "HTML страницы при ошибке",
                allure.attachment_type.HTML
            )
            raise TimeoutException(
                f"Элемент не найден за 30 сек. Локатор: {locator}. Проверьте видимость и текст."
            )
        except Exception as e:
            allure.attach(str(e), "Ошибка при поиске номера", allure.attachment_type.TEXT)
            raise

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        if isinstance(locator, str):
            locator = (By.XPATH, locator)
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Элемент отсутствует на странице")
    def is_element_not_present(self, locator, timeout=TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return False
        except:
            return True

    @allure.step("Подождать изменения количества окон")
    def wait_for_windows_count(self, count, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(count))

    @allure.step("Переключиться на окно по индексу")
    def switch_to_window(self, index):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[index])

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Сделать скриншот")
    def take_screenshot(self):
        return self.driver.get_screenshot_as_png()

    @allure.step("Получить HTML страницы")
    def get_page_source(self):
        return self.driver.page_source

    @allure.step("Проверить, что URL содержит подстроку")
    def assert_url_contains(self, expected_substring):
        current_url = self.get_current_url()
        assert expected_substring in current_url, (
            f"Ожидалось, что URL содержит '{expected_substring}', но URL: '{current_url}'"
        )

    @allure.step("Дождаться новой вкладки и переключиться на неё")
    def wait_for_new_window_and_switch(self, expected_windows=2, timeout=TIMEOUT):
        """
        Ждёт, пока не появится указанное количество окон, затем переключается на последнее (новое).
        """
        self.wait_for_windows_count(expected_windows, timeout)
        self.switch_to_window(-1)

    @allure.step("Дождаться, пока URL содержит подстроку, и проверить")
    def assert_url_contains_with_wait(self, expected_substring, timeout=TIMEOUT):
        """
        Ждёт (с таймаутом), пока текущий URL не будет содержать expected_substring,
        затем проверяет и фиксирует URL в Allure.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: expected_substring in d.current_url
            )
            current_url = self.get_current_url()
            allure.attach(
                current_url,
                name="Текущий URL",
                attachment_type=allure.attachment_type.TEXT
            )
            self.assert_url_contains(expected_substring)
        except TimeoutException:
            allure.attach(
                self.take_screenshot(),
                name="Скриншот при ошибке ожидания URL",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                self.get_page_source(),
                name="HTML страницы при ошибке",
                attachment_type=allure.attachment_type.HTML
            )
            raise AssertionError(
                f"Не удалось дождаться, чтобы URL содержал '{expected_substring}'"
            )

    @allure.step("Подождать, пока элемент станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout=TIMEOUT):
        if isinstance(locator, str):
            locator = (By.XPATH, locator)
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Подождать видимости элемента по CSS-селектору")
    def wait_for_css_selector(self, css_selector, timeout=TIMEOUT):
        locator = (By.CSS_SELECTOR, css_selector)
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
