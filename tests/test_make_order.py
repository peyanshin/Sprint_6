import allure
import time
import re

from datetime import datetime
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from helper import *
from curl import *

class TestMakeOrderWithNewCredentialsTopButton:

    @allure.title("Тест успешного оформления заказа")
    @allure.description("Проверка оформления заказа с новыми данными")

    def test_successful_order(self, driver, test_first_data_sets):

        # Arrange
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        wait = WebDriverWait(driver, 10)
        station_name = test_first_data_sets["metro"]
        period = test_first_data_sets["period"]
        date_input = test_first_data_sets["date"]

        # Act
        with allure.step("Оформить заказ"):
            main_page.click_top_order_button()

        with allure.step(f"Ввести имя: {test_first_data_sets['name']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_NAME, test_first_data_sets["name"])

        with allure.step(f"Ввести фамилию: {test_first_data_sets['lastname']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_LAST_NAME, test_first_data_sets["lastname"])       

        with allure.step(f"Ввести адрес: {test_first_data_sets['address']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_ADDRESS, test_first_data_sets["address"])  

        with allure.step(f"Открыть поле ввода станции метро и ввести {station_name}"):
            metro_input = wait.until(EC.element_to_be_clickable(OrderLocators.FOR_WHOM_METRO))
            metro_input.click()
            metro_input.clear()
            metro_input.send_keys(station_name)

            metro_option_locator = OrderLocators.get_metro_option_locator(station_name)
            metro_option = wait.until(EC.element_to_be_clickable(metro_option_locator))
            metro_option.click()

            allure.attach(f"Выбрана станция метро: {station_name}",name="Выбор станции метро",attachment_type=allure.attachment_type.TEXT)

        with allure.step("Проверить, что выбранная станция отображается в поле"):
            actual_value = metro_input.get_attribute("value")
            assert station_name in actual_value, (f"Ожидалось, что в поле будет «{station_name}», "f"но получено: «{actual_value}»")    

        with allure.step(f"Ввести телефон: {test_first_data_sets['phone']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_PHONE, test_first_data_sets["phone"])
            time.sleep(2)   

        with allure.step("Нажать кнопку далее"):
            order_page.click_next_button()

        with allure.step(f"Выбрать дату: {test_first_data_sets['date']}"):
            date_input = wait.until(EC.element_to_be_clickable(OrderLocators.RENT_DATE))
            date_input.click()

            target_date = datetime.strptime(test_first_data_sets["date"], "%Y-%m-%d")
            day_number = target_date.day

            calendar_day_locator = (By.XPATH,f"//div[contains(@class, 'react-datepicker__day') and text()='{day_number}']")
            calendar_day = wait.until(EC.element_to_be_clickable(calendar_day_locator))
            calendar_day.click()

        with allure.step("Закрыть календарь, если открыт"):
            body = driver.find_element(By.TAG_NAME, "body")
            body.click()

        with allure.step(f"Выбрать срок аренды: {period}"):
            dropdown = wait.until(EC.element_to_be_clickable(OrderLocators.RENT_PERIOD))
            dropdown.click()

            period_locator = OrderLocators.get_period_option_locator(period)
            period = wait.until(EC.element_to_be_clickable(period_locator))
            period.click()

        with allure.step("Выбрать цвет самоката Чёрная жемчужина"):
            order_page.click_black_perl_button()

        with allure.step(f"Ввести комментарий: {test_first_data_sets['comment']}"):
            order_page.send_keys_to_input(OrderLocators.RENT_COMMENT, test_first_data_sets["comment"])  
            time.sleep(2)

        with allure.step("Нажать на кнопку Заказать"):
            order_page.click_rent_order_button()

        with allure.step("Подтвердить заказ нажатием кнопки Да"):
            order_page.click_confirm_yes_button()   
            time.sleep(2)

        with allure.step("Найти номер заказа на странице"):
            wait = WebDriverWait(driver, 10)
            order_number_element = wait.until(EC.visibility_of_element_located(OrderLocators.RENT_ORDER_NUMBER))
            full_text = order_number_element.text.strip()

            match = re.search(r'\d+', full_text)
            if not match:
                raise AssertionError(f"Не удалось извлечь номер заказа из текста: {full_text}")
            
            order_number = match.group()
            allure.attach(order_number, name="Извлечённый номер заказа", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Нажать кнопку 'Посмотреть заказ'"):
            order_page.click_order_info_button()
            time.sleep(2)

        with allure.step("Дождаться загрузки страницы отслеживания и проверить URL"):
            wait.until(lambda driver: "track?t=" in driver.current_url)

            current_url = driver.current_url
            allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

        # Assert
            # 0. Проверка URL
            assert order_number in current_url, (f"Номер заказа {order_number} не найден в URL отслеживания. "f"Текущий URL: {current_url}")

            # 1. Проверка имени
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_NAME))
            assert element.text == test_first_data_sets["name"], f"Имя не совпадает: ожидалось '{test_first_data_sets['name']}', найдено '{element.text}'"

            # 2. Проверка фамилии
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_LAST_NAME))
            assert element.text == test_first_data_sets["lastname"], f"Фамилия не совпадает: ожидалось '{test_first_data_sets['lastname']}', найдено '{element.text}'"

            # 3. Проверка адреса
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_ADDRESS))
            assert element.text == test_first_data_sets["address"], f"Адрес не совпадает: ожидалось '{test_first_data_sets['address']}', найдено '{element.text}'"

            # 4. Проверка станции метро
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_METRO))
            assert element.text == test_first_data_sets["metro"], f"Станция метро не совпадает: ожидалось '{test_first_data_sets['metro']}', найдено '{element.text}'"

            # 5. Проверка телефона
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_PHONE))
            assert element.text == test_first_data_sets["phone"], f"Телефон не совпадает: ожидалось '{test_first_data_sets['phone']}', найдено '{element.text}'"

            # 6. Проверка даты доставки
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_DATE))
            assert element.text == test_first_data_sets["date"], f"Дата доставки не совпадает: ожидалось '{test_first_data_sets['date']}', найдено '{element.text}'"

            # 7. Проверка срока аренды
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_PERIOD))
            assert element.text == test_first_data_sets["period"], f"Срок аренды не совпадает: ожидалось '{test_first_data_sets['period']}', найдено '{element.text}'"

            # 8. Проверка цвета (если нужно, хотя в фикстуре его нет)
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_COLOR))
            assert element.text == test_first_data_sets["чёрный жемчуг"], f"Цвет не совпадает: ожидалось ['чёрный жемчуг'], найдено '{element.text}'"

            # 9. Проверка комментария
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_COMMENT))
            assert element.text == test_first_data_sets["comment"], f"Комментарий не совпадает: ожидалось '{test_first_data_sets['comment']}', найдено '{element.text}'"            

class TestMakeOrderWithNewCredentialsBottomButton:

    @allure.title("Тест успешного оформления заказа")
    @allure.description("Проверка оформления заказа с новыми данными")

    def test_successful_order(self, driver, test_second_data_sets):

        # Arrange
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        wait = WebDriverWait(driver, 10)
        station_name = test_second_data_sets["metro"]
        period = test_second_data_sets["period"]
        date_input = test_second_data_sets["date"]

        # Act
        with allure.step("Скрол до кнопки Заказать внизу экрана"):
            main_page.scroll_to_element(MainPageLocators.ORDER_BOTTOM_BUTTON)

        with allure.step("Оформить заказ"):
            main_page.click_bottom_order_button()

        with allure.step(f"Ввести имя: {test_second_data_sets['name']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_NAME, test_second_data_sets["name"])

        with allure.step(f"Ввести фамилию: {test_second_data_sets['lastname']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_LAST_NAME, test_second_data_sets["lastname"])       

        with allure.step(f"Ввести адрес: {test_second_data_sets['address']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_ADDRESS, test_second_data_sets["address"])  

        with allure.step(f"Открыть поле ввода станции метро и ввести {station_name}"):
            metro_input = wait.until(EC.element_to_be_clickable(OrderLocators.FOR_WHOM_METRO))
            metro_input.click()
            metro_input.clear()
            metro_input.send_keys(station_name)

            metro_option_locator = OrderLocators.get_metro_option_locator(station_name)
            metro_option = wait.until(EC.element_to_be_clickable(metro_option_locator))
            metro_option.click()

            allure.attach(f"Выбрана станция метро: {station_name}",name="Выбор станции метро",attachment_type=allure.attachment_type.TEXT)

        with allure.step("Проверить, что выбранная станция отображается в поле"):
            actual_value = metro_input.get_attribute("value")
            assert station_name in actual_value, (f"Ожидалось, что в поле будет «{station_name}», "f"но получено: «{actual_value}»")    

        with allure.step(f"Ввести телефон: {test_second_data_sets['phone']}"):
            order_page.send_keys_to_input(OrderLocators.FOR_WHOM_PHONE, test_second_data_sets["phone"])                

        with allure.step("Нажать кнопку далее"):
            order_page.click_next_button()

        with allure.step(f"Выбрать дату: {test_second_data_sets['date']}"):
            date_input = wait.until(EC.element_to_be_clickable(OrderLocators.RENT_DATE))
            date_input.click()

            target_date = datetime.strptime(test_second_data_sets["date"], "%Y-%m-%d")
            day_number = target_date.day

            calendar_day_locator = (By.XPATH,f"//div[contains(@class, 'react-datepicker__day') and text()='{day_number}']")
            calendar_day = wait.until(EC.element_to_be_clickable(calendar_day_locator))
            calendar_day.click()

        with allure.step("Закрыть календарь, если открыт"):
            body = driver.find_element(By.TAG_NAME, "body")
            body.click()

        with allure.step(f"Выбрать срок аренды: {period}"):
            dropdown = wait.until(EC.element_to_be_clickable(OrderLocators.RENT_PERIOD))
            dropdown.click()

            period_locator = OrderLocators.get_period_option_locator(period)
            period = wait.until(EC.element_to_be_clickable(period_locator))
            period.click()

        with allure.step("Выбрать цвет самоката Серая безысходность"):
            order_page.click_grey_hopelessness_button()

        with allure.step(f"Ввести комментарий: {test_second_data_sets['comment']}"):
            order_page.send_keys_to_input(OrderLocators.RENT_COMMENT, test_second_data_sets["comment"])  
            time.sleep(2)

        with allure.step("Нажать на кнопку Заказать"):
            order_page.click_rent_order_button()

        with allure.step("Подтвердить заказ нажатием кнопки Да"):
            order_page.click_confirm_yes_button()   
            time.sleep(2)

        with allure.step("Найти номер заказа на странице"):
            wait = WebDriverWait(driver, 10)
            order_number_element = wait.until(EC.visibility_of_element_located(OrderLocators.RENT_ORDER_NUMBER))
            full_text = order_number_element.text.strip()

            match = re.search(r'\d+', full_text)
            if not match:
                raise AssertionError(f"Не удалось извлечь номер заказа из текста: {full_text}")
            
            order_number = match.group()
            allure.attach(order_number, name="Извлечённый номер заказа", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Нажать кнопку 'Посмотреть заказ'"):
            order_page.click_order_info_button()
            time.sleep(2)

        with allure.step("Дождаться загрузки страницы отслеживания и проверить URL"):
            wait.until(lambda driver: "track?t=" in driver.current_url)

            current_url = driver.current_url
            allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

        # Assert
            # 0. Проверка URL
            assert order_number in current_url, (f"Номер заказа {order_number} не найден в URL отслеживания. "f"Текущий URL: {current_url}")

            # 1. Проверка имени
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_NAME))
            assert element.text == test_second_data_sets["name"], f"Имя не совпадает: ожидалось '{test_second_data_sets['name']}', найдено '{element.text}'"

            # 2. Проверка фамилии
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_LAST_NAME))
            assert element.text == test_second_data_sets["lastname"], f"Фамилия не совпадает: ожидалось '{test_second_data_sets['lastname']}', найдено '{element.text}'"

            # 3. Проверка адреса
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_ADDRESS))
            assert element.text == test_second_data_sets["address"], f"Адрес не совпадает: ожидалось '{test_second_data_sets['address']}', найдено '{element.text}'"

            # 4. Проверка станции метро
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_METRO))
            assert element.text == test_second_data_sets["metro"], f"Станция метро не совпадает: ожидалось '{test_second_data_sets['metro']}', найдено '{element.text}'"

            # 5. Проверка телефона
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_PHONE))
            assert element.text == test_second_data_sets["phone"], f"Телефон не совпадает: ожидалось '{test_second_data_sets['phone']}', найдено '{element.text}'"

            # 6. Проверка даты доставки
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_DATE))
            assert element.text == test_second_data_sets["date"], f"Дата доставки не совпадает: ожидалось '{test_second_data_sets['date']}', найдено '{element.text}'"

            # 7. Проверка срока аренды
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_PERIOD))
            assert element.text == test_second_data_sets["period"], f"Срок аренды не совпадает: ожидалось '{test_second_data_sets['period']}', найдено '{element.text}'"

            # 8. Проверка цвета
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_COLOR))
            assert element.text == test_second_data_sets["серая безысходность"], f"Цвет не совпадает: ожидалось ['серая безысходность'], найдено '{element.text}'"

            # 9. Проверка комментария
            element = wait.until(EC.visibility_of_element_located(OrderLocators.CHECK_COMMENT))
            assert element.text == test_second_data_sets["comment"], f"Комментарий не совпадает: ожидалось '{test_second_data_sets['comment']}', найдено '{element.text}'" 
