import allure

from pages.main_page import MainPage

class TestQuestionsAndAnswers:
    @allure.title("Проверка текста ответа на вопрос №1")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")

    def test_answer_1(self, driver):
        main_page = MainPage(driver)
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

        with allure.step("Скролл до вопроса №1"):
            main_page.scroll_to_question(0)

        with allure.step("Раскрыть ответ на вопрос №1"):
            main_page.click_question(0)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(0, expected_text)

    @allure.title("Проверка текста ответа на вопрос №2")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")
    def test_answer_2(self, driver):
        main_page = MainPage(driver)
        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

        with allure.step("Скролл до вопроса №2"):
            main_page.scroll_to_question(1)

        with allure.step("Раскрыть ответ на вопрос №2"):
            main_page.click_question(1)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(1, expected_text)

    @allure.title("Проверка текста ответа на вопрос №3")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")
    def test_answer_3(self, driver):
        main_page = MainPage(driver)
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

        with allure.step("Скролл до вопроса №3"):
            main_page.scroll_to_question(2)

        with allure.step("Раскрыть ответ на вопрос №3"):
            main_page.click_question(2)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(2, expected_text)

    @allure.title("Проверка текста ответа на вопрос №4")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")
    def test_answer_4(self, driver):
        main_page = MainPage(driver)
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

        with allure.step("Скролл до вопроса №4"):
            main_page.scroll_to_question(3)

        with allure.step("Раскрыть ответ на вопрос №4"):
            main_page.click_question(3)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(3, expected_text)

    @allure.title("Проверка текста ответа на вопрос №5")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")
    def test_answer_5(self, driver):
        main_page = MainPage(driver)
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

        with allure.step("Скролл до вопроса №5"):
            main_page.scroll_to_question(4)

        with allure.step("Раскрыть ответ на вопрос №5"):
            main_page.click_question(4)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(4, expected_text)

    @allure.title("Проверка текста ответа на вопрос №6")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")
    def test_answer_6(self, driver):
        main_page = MainPage(driver)
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

        with allure.step("Скролл до вопроса №6"):
            main_page.scroll_to_question(5)

        with allure.step("Раскрыть ответ на вопрос №6"):
            main_page.click_question(5)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(5, expected_text)

    @allure.title("Проверка текста ответа на вопрос №7")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")
    def test_answer_7(self, driver):
        main_page = MainPage(driver)
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

        with allure.step("Скролл до вопроса №7"):
            main_page.scroll_to_question(6)

        with allure.step("Раскрыть ответ на вопрос №7"):
            main_page.click_question(6)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(6, expected_text)

    @allure.title("Проверка текста ответа на вопрос №8")
    @allure.description("Сравнивается текст ответа с ожидаемым значением")
    def test_answer_8(self, driver):
        main_page = MainPage(driver)
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

        with allure.step("Скролл до вопроса №8"):
            main_page.scroll_to_question(7)

        with allure.step("Раскрыть ответ на вопрос №8"):
            main_page.click_question(7)

        with allure.step("Проверить текст ответа"):
            main_page.should_have_correct_answer(7, expected_text)
