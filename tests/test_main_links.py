import allure

from pages.main_page import MainPage

class TestMainPageLinkButtons:
    @allure.title("Проверка работы кнопок главной страницы")
    @allure.description("Проверка работы кнопок Яндекс и Самокат")

    def test_push_yandex_button(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажать кнопку Яндекс"):
            main_page.click_yandex_button()

        with allure.step("Дождаться открытия новой вкладки и проверить URL"):
            main_page.wait_for_new_tab_and_check_url("dzen.ru")

        with allure.step("Закрыть новую вкладку и вернуться на главную"):
            main_page.close_new_tab_and_return_to_main()

    def test_push_scooter_button(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажать кнопку Самокат"):
            main_page.click_scooter_button()

        with allure.step("Проверить, что открыта главная страница Самоката"):
            main_page.check_current_url_contains("qa-scooter.praktikum-services.ru")
