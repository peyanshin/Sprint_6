import allure

from pages.base_page import BasePage

from locators.main_page_locators import MainPageLocators
from locators.main_questions_and_answers_locators import MainQuestionsAndAnswerLocators

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10

class MainPage(BasePage):

#Кнопки главной страницы
    @allure.step("Нажать на кнопку «Заказать» вверху экрана")
    def click_top_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Скролл до кнопки «Заказать» внизу экрана и клик")
    def scroll_to_and_click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BOTTOM_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_BOTTOM_BUTTON)

    @allure.step("Нажать кнопку «Яндекс» (открывает в новой вкладке)")
    def click_yandex_button(self):
        yandex_button = self.wait_for_element(MainPageLocators.DZEN_BUTTON)
        href = yandex_button.get_attribute("href")
        target = yandex_button.get_attribute("target")

        allure.attach(
            f"href: {href}\ntarget: {target}",
            name="Атрибуты кнопки «Яндекс»",
            attachment_type=allure.attachment_type.TEXT
        )
        yandex_button.click()

    @allure.step("Нажать кнопку «Самокат»")
    def click_scooter_button(self):
        scooter_button = self.wait_for_element(MainPageLocators.SCOOTER_BUTTON)
        scooter_button.click()

    @allure.step("Дождаться открытия новой вкладки и проверить URL")
    def wait_for_new_tab_and_check_url(self, expected_domain):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.number_of_windows_to_be(2))
            all_windows = self.driver.window_handles
            self.driver.switch_to.window(all_windows[1])

            WebDriverWait(self.driver, TIMEOUT).until(
                lambda d: expected_domain in d.current_url
            )
            current_url = self.driver.current_url

            allure.attach(
                current_url,
                name="Текущий URL новой вкладки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert expected_domain in current_url, (
                f"Ожидался домен '{expected_domain}', но URL: '{current_url}'"
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Скриншот при ошибке переключения вкладки",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                self.driver.page_source,
                name="HTML страницы при ошибке",
                attachment_type=allure.attachment_type.HTML
            )
            raise AssertionError(f"Не удалось переключиться на вкладку с доменом '{expected_domain}'")

    @allure.step("Закрыть новую вкладку и вернуться на исходную страницу")
    def close_new_tab_and_return_to_main(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step("Проверить, что текущий URL содержит ожидаемый домен")
    def check_current_url_contains(self, expected_domain):
        current_url = self.driver.current_url
        allure.attach(
            current_url,
            name="Текущий URL",
            attachment_type=allure.attachment_type.TEXT
        )
        assert expected_domain in current_url, (
            f"Ожидался домен '{expected_domain}', но URL: '{current_url}'"
        )

#Кнопки пунктов меню Вопросы о важном
    @allure.step("Скролл до вопроса №{num} в разделе «Вопросы и ответы»")
    def scroll_to_question(self, num: int):
        locator = getattr(MainQuestionsAndAnswerLocators, f"MAIN_Q_{num}")
        self.scroll_to_element(locator)

    @allure.step("Нажать на вопрос №{num} для раскрытия ответа")
    def click_question(self, num: int):
        locator = getattr(MainQuestionsAndAnswerLocators, f"MAIN_Q_{num}")
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Получить текст ответа на вопрос №{num}")
    def get_answer_text(self, num: int) -> str:
        locator = getattr(MainQuestionsAndAnswerLocators, f"MAIN_A_{num}")
        element = self.wait_for_element(locator)
        return element.text.strip()

    @allure.step("Проверить, что ответ на вопрос №{num} соответствует ожидаемому")
    def should_have_correct_answer(self, num: int, expected_text: str):
        actual_text = self.get_answer_text(num)
        assert actual_text == expected_text, (
            f"Текст ответа на вопрос №{num} не соответствует ожидаемому.\n"
            f"Ожидаемый: '{expected_text}'\n"
            f"Фактический: '{actual_text}'"
        )
