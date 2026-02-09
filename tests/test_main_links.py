import allure

from curl import *

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestMainPageLinkButtons:

    @allure.title("Проверка работы кнопок главной страницы")
    @allure.description("Проверка работы кнопок Яндекс и Самокат")

    def test_push_yandex_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        dzen_page = dzen_site

        # Act & Assert
        with allure.step("Нажать кнопку Яндекс"):
            main_page.click_yandex_button(MainPageLocators.DZEN_BUTTON)
        with allure.step("Проверить URL"):
            main_page.wait_for_new_tab_and_check_url(dzen_page)
        with allure.step("Закруть новую вкладку"):
            main_page.close_new_tab_and_return_to_main()

    def test_push_scooter_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        scooter_page = main_site

        # Act
        main_page.click_yandex_button(MainPageLocators.SCOOTER_BUTTON)

        # Assert
        with allure.step("Оформить заказ"):
            main_page.click_top_order_button()

        with allure.step("Нажать кнопку Самокат"):
           main_page.test_push_scooter_button(scooter_page)
