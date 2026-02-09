import allure

from pages.base_page import BasePage
from locators.order_locators import OrderLocators

TIMEOUT = 10

class OrderPage(BasePage):
    @allure.step("Ввести текст в поле Имя")
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Нажать на кнопку Далее")
    def click_next_button(self):
        self.click_on_element(OrderLocators.FOR_WHOM_NEXT_BUTTON)

    @allure.step("Нажать на список Срок аренды")
    def click_rent_period_button(self):
        self.click_on_element(OrderLocators.RENT_PERIOD)

    @allure.step("Нажать на цвет самоката Чёрный жемчуг")
    def click_black_perl_button(self):
        self.click_on_element(OrderLocators.RENT_BLACK_PERL)

    @allure.step("Нажать на цвет самоката Серая безысходность")
    def click_grey_hopelessness_button(self):
        self.click_on_element(OrderLocators.RENT_GREY_HOPELESSNESS)

    @allure.step("Нажать на кнопку Заказать")
    def click_rent_order_button(self):
        self.click_on_element(OrderLocators.RENT_ORDER)

    @allure.step("Подтвердить заказ кнопкой Да")
    def click_confirm_yes_button(self):
        self.click_on_element(OrderLocators.RENT_YES_BUTTON)

    @allure.step("Посмотреть статус заказа")
    def click_order_info_button(self):
        self.click_on_element(OrderLocators.RENT_ORDER_INFO_BUTTON)
