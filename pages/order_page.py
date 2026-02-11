import allure

from datetime import datetime

from pages.base_page import BasePage

from locators.order_locators import OrderLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 3000

class OrderPage(BasePage):
    @allure.step("Заполнение данных заказчика")
    def fill_customer_info(self, data):
        self.enter_name(data["name"])
        self.enter_lastname(data["lastname"])
        self.enter_address(data["address"])
        self.select_metro(data["metro"])
        self.enter_phone(data["phone"])
    
    @allure.step("Ввести имя")
    def enter_name(self, name):
        self.send_keys_to_input(OrderLocators.FOR_WHOM_NAME, name)

    @allure.step("Ввести фамилию")
    def enter_lastname(self, lastname):
        self.send_keys_to_input(OrderLocators.FOR_WHOM_LAST_NAME, lastname)

    @allure.step("Ввести адрес")
    def enter_address(self, address):
        self.send_keys_to_input(OrderLocators.FOR_WHOM_ADDRESS, address)

    @allure.step("Ввести номер телефона")
    def enter_phone(self, phone):
        self.send_keys_to_input(OrderLocators.FOR_WHOM_PHONE, phone)

    @allure.step("Выбрать станцию метро")
    def select_metro(self, station_name):
        metro_input = self.wait_for_element(OrderLocators.FOR_WHOM_METRO)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(station_name)

        metro_option = self.wait_for_element(OrderLocators.get_metro_option_locator(station_name))
        metro_option.click()

    @allure.step("Нажать кнопку «Далее»")
    def click_next_button(self):
        self.click_on_element(OrderLocators.FOR_WHOM_NEXT_BUTTON)

    @allure.step("Выбрать дату доставки")
    def select_delivery_date(self, date_str):
        date_input = self.wait_for_element(OrderLocators.RENT_DATE)
        date_input.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderLocators.get_datepicker_locator()))

        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        day_number = target_date.day

        calendar_day_locator = OrderLocators.get_calendar_day_locator(day_number)
        calendar_day = self.wait_for_element(calendar_day_locator)
        calendar_day.click()

    @allure.step("Закрыть календарь, если открыт")
    def close_calendar(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.click()

    @allure.step("Выбрать срок аренды")
    def select_rent_period(self, period):
        dropdown = self.wait_for_element(OrderLocators.RENT_PERIOD_DROPDOWN)
        dropdown.click()    
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.get_period_option_locator(period)))
        period_element = self.wait_for_element(OrderLocators.get_period_option_locator(period))
        period_element.click()

    @allure.step("Выбрать цвет самоката «Чёрная жемчужина»")
    def select_black_perl_color(self):
        self.click_on_element(OrderLocators.RENT_BLACK_PERL)

    @allure.step("Выбрать цвет самоката «Серая безысходность»")
    def select_grey_hopelessness_color(self):
        self.click_on_element(OrderLocators.RENT_GREY_HOPELESSNESS)

    @allure.step("Ввести комментарий к заказу")
    def enter_comment(self, comment):
        self.send_keys_to_input(OrderLocators.RENT_COMMENT, comment)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order_button(self):
        self.click_on_element(OrderLocators.RENT_ORDER)

    @allure.step("Подтвердить заказ нажатием кнопки «Да»")
    def confirm_order(self):
        self.click_on_element(OrderLocators.RENT_YES_BUTTON)
        WebDriverWait(self.driver, timeout=2).until(EC.element_to_be_clickable(OrderLocators.RENT_ORDER_INFO_BUTTON))
        
    @allure.step("Нажать кнопку «Посмотреть заказ»")
    def click_order_info_button(self):
        self.click_on_element(OrderLocators.RENT_ORDER_INFO_BUTTON)

    @allure.step("Проверка данных в деталях заказа")
    def verify_order_details(self, data: dict):
        # 1. Проверка имени
        element = self.wait_for_element(OrderLocators.CHECK_NAME)
        assert element.text == data["name"], (
            f"Имя не совпадает: ожидалось '{data['name']}', найдено '{element.text}'"
        )

        # 2. Проверка фамилии
        element = self.wait_for_element(OrderLocators.CHECK_LAST_NAME)
        assert element.text == data["lastname"], (
            f"Фамилия не совпадает: ожидалось '{data['lastname']}', найдено '{element.text}'"
        )

        # 3. Проверка адреса
        element = self.wait_for_element(OrderLocators.CHECK_ADDRESS)
        assert element.text == data["address"], (
            f"Адрес не совпадает: ожидалось '{data['address']}', найдено '{element.text}'"
        )

        # 4. Проверка станции метро
        element = self.wait_for_element(OrderLocators.CHECK_METRO)
        assert element.text == data["metro"], (
            f"Станция метро не совпадает: ожидалось '{data['metro']}', найдено '{element.text}'"
        )

        # 5. Проверка телефона
        element = self.wait_for_element(OrderLocators.CHECK_PHONE)
        assert element.text == data["phone"], (
            f"Телефон не совпадает: ожидалось '{data['phone']}', найдено '{element.text}'"
        )

        # 6. Проверка даты доставки
        element = self.wait_for_element(OrderLocators.CHECK_DATE)
        # Преобразуем дату в нужный формат (предполагаем, что в интерфейсе дата отображается как DD.MM.YYYY)
        expected_date = datetime.strptime(data["date"], "%Y-%m-%d").strftime("%d.%m.%Y")
        assert element.text == expected_date, (
            f"Дата доставки не совпадает: ожидалось '{expected_date}', найдено '{element.text}'"
        )

        # 7. Проверка срока аренды
        element = self.wait_for_element(OrderLocators.CHECK_PERIOD)
        # Формируем ожидаемое значение с корректным склонением
        period = int(data["period"])
        if period == 1:
            expected_period = f"{period} день"
        elif 2 <= period <= 4:
            expected_period = f"{period} дня"
        else:
            expected_period = f"{period} дней"
        assert element.text == expected_period, (
            f"Срок аренды не совпадает: ожидалось '{expected_period}', найдено '{element.text}'"
        )

        # 8. Проверка цвета
        element = self.wait_for_element(OrderLocators.CHECK_COLOR)
        color_map = {
            "black": "Чёрная жемчужина",
            "grey": "Серая безысходность"
        }
        expected_color = color_map.get(data.get("color", ""), "Не указан")
        assert element.text == expected_color, (
            f"Цвет не совпадает: ожидалось '{expected_color}', найдено '{element.text}'"
        )

        # 9. Проверка комментария
        element = self.wait_for_element(OrderLocators.CHECK_COMMENT)
        expected_comment = data.get("comment", "")
        assert element.text == expected_comment, (
            f"Комментарий не совпадает: ожидалось '{expected_comment}', найдено '{element.text}'"
        )
