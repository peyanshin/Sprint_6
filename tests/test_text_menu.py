import allure

from pages.main_page import MainPage
from locators.main_questions_and_answers_locators import MainQuestionsAndAnswerLocators

from data import *
from helper import *
from curl import *


class TestCorrectOpenTextMenu:
    @allure.title("Проверка правильной информации в пунктах открывающегося меню")
    @allure.description("Сравнение текста в первом меню с ожидаемым значением: «Сутки — 400 рублей. Оплата курьеру — наличными или картой.»")
    def test_correct_open_1_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_0)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_0)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_0)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )

    def test_correct_open_2_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_1)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_1)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_1)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )       

    def test_correct_open_3_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_2)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_2)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_2)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )      

    def test_correct_open_4_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_3)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_3)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_3)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )     

    def test_correct_open_5_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_4)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_4)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_4)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )     

    def test_correct_open_6_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_5)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_5)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_5)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )     

    def test_correct_open_7_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_6)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_6)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_6)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )     
 
    def test_correct_open_8_menu(self, driver):
        # Arrange
        main_page = MainPage(driver)
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

        # Act
        with allure.step("Скролл до пункта меню"):
            main_page.scroll_to_element(MainQuestionsAndAnswerLocators.MAIN_Q_7)

        with allure.step("Нажать на пункт меню"):
            main_page.click_menu_button(MainQuestionsAndAnswerLocators.MAIN_Q_7)

        # Assert
        with allure.step("Проверить, что текст в меню соответствует ожидаемому"):
            actual_text = main_page.get_menu_text(MainQuestionsAndAnswerLocators.MAIN_A_7)
            assert actual_text == expected_text, (
                f"Текст в меню не соответствует ожидаемому.\n"
                f"Ожидаемый: '{expected_text}'\n"
                f"Фактический: '{actual_text}'"
            )     
 