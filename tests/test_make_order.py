import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData

class TestMakeOrder:
    @allure.title("Тест успешного оформления заказа (набор данных №{data_set_num})")
    @allure.description("Проверка оформления заказа с разными данными через верхнюю/нижнюю кнопку")

    @pytest.mark.parametrize(
        "data_set, button_type, color_method",
        [
            (
                OrderData.FIRST_SET,
                "top",
                "select_black_perl_color"
            ),
            (
                OrderData.SECOND_SET,
                "bottom",
                "select_grey_hopelessness_color"
            )
        ],
        ids=[
            "Первый набор данных (верхняя кнопка)",
            "Второй набор данных (нижняя кнопка)"
        ]
    )
    def test_successful_order(self, driver, data_set, button_type, color_method):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step(f"Переход к оформлению заказа через {button_type} кнопку"):
            if button_type == "top":
                main_page.click_top_order_button()
            else:
                main_page.scroll_to_and_click_bottom_order_button()

        with allure.step("Заполнение данных заказчика"):
            order_page.fill_customer_info(data_set)

        with allure.step("Переход к выбору параметров аренды"):
            order_page.click_next_button()

        with allure.step("Выбор даты доставки"):
            order_page.select_delivery_date(data_set["date"])

        with allure.step("Выбор срока аренды"):
            order_page.select_rent_period(data_set["period"])

        with allure.step("Выбор цвета самоката"):
            getattr(order_page, color_method)()

        with allure.step("Ввод комментария к заказу"):
            order_page.enter_comment(data_set["comment"])

        with allure.step("Подтверждение заказа"):
            order_page.click_order_button()
            order_page.confirm_order()

        with allure.step("Переход к деталям заказа"):
            order_page.click_order_info_button()

        with allure.step("Проверка данных в деталях заказа"):
            order_page.verify_order_details(data_set)
