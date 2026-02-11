import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestMakeOrderWithNewCredentialsTopButton:
    @allure.title("Тест успешного оформления заказа (верхняя кнопка)")
    @allure.description("Проверка оформления заказа с новыми данными через верхнюю кнопку")

    def test_successful_order(self, driver, test_first_data_sets):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Переход к оформлению заказа через верхнюю кнопку"):
            main_page.click_top_order_button()

        with allure.step("Заполнение данных заказчика"):
            order_page.fill_customer_info(test_first_data_sets)

        with allure.step("Переход к выбору параметров аренды"):
            order_page.click_next_button()

        with allure.step("Выбор даты доставки"):
            order_page.select_delivery_date(test_first_data_sets["date"])

        with allure.step("Выбор срока аренды"):
            order_page.select_rent_period(test_first_data_sets["period"])

        with allure.step("Выбор цвета самоката"):
            order_page.select_black_perl_color()

        with allure.step("Ввод комментария к заказу"):
            order_page.enter_comment(test_first_data_sets["comment"])

        with allure.step("Подтверждение заказа"):
            order_page.click_order_button()
            order_page.confirm_order()

        with allure.step("Переход к деталям заказа"):
            order_page.click_order_info_button()

        with allure.step("Проверка данных в деталях заказа"):
            order_page.verify_order_details(test_first_data_sets)



class TestMakeOrderWithNewCredentialsBottomButton:
    @allure.title("Тест успешного оформления заказа (нижняя кнопка)")
    @allure.description("Проверка оформления заказа с новыми данными через нижнюю кнопку")

    def test_successful_order(self, driver, test_second_data_sets):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Скролл до нижней кнопки заказа и клик"):
            main_page.scroll_to_and_click_bottom_order_button()

        with allure.step("Заполнение данных заказчика"):
            order_page.fill_customer_info(test_second_data_sets)

        with allure.step("Переход к выбору параметров аренды"):
            order_page.click_next_button()

        with allure.step("Выбор даты доставки"):
            order_page.select_delivery_date(test_second_data_sets["date"])

        with allure.step("Выбор срока аренды"):
            order_page.select_rent_period(test_second_data_sets["period"])

        with allure.step("Выбор цвета самоката"):
            order_page.select_grey_hopelessness_color()

        with allure.step("Ввод комментария к заказу"):
            order_page.enter_comment(test_second_data_sets["comment"])

        with allure.step("Подтверждение заказа"):
            order_page.click_order_button()
            order_page.confirm_order()

        with allure.step("Переход к деталям заказа"):
            order_page.click_order_info_button()
        
        with allure.step("Проверка данных в деталях заказа"):
            order_page.verify_order_details(test_second_data_sets)
