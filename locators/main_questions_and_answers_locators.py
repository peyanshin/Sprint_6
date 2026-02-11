from selenium.webdriver.common.by import By

class MainQuestionsAndAnswerLocators:
    # Заголовки вопросов (кликабельные)
    MAIN_Q_0 = (By.XPATH, "//div[@id='accordion__heading-0']")
    MAIN_Q_1 = (By.XPATH, "//div[@id='accordion__heading-1']")
    MAIN_Q_2 = (By.XPATH, "//div[@id='accordion__heading-2']")
    MAIN_Q_3 = (By.XPATH, "//div[@id='accordion__heading-3']")
    MAIN_Q_4 = (By.XPATH, "//div[@id='accordion__heading-4']")
    MAIN_Q_5 = (By.XPATH, "//div[@id='accordion__heading-5']")
    MAIN_Q_6 = (By.XPATH, "//div[@id='accordion__heading-6']")
    MAIN_Q_7 = (By.XPATH, "//div[@id='accordion__heading-7']")

    # Текстовые ответы
    MAIN_A_0 = (By.XPATH, "//p[normalize-space()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    MAIN_A_1 = (By.XPATH, "//p[normalize-space()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    MAIN_A_2 = (By.XPATH, "//p[normalize-space()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    MAIN_A_3 = (By.XPATH, "//p[normalize-space()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    MAIN_A_4 = (By.XPATH, "//p[normalize-space()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    MAIN_A_5 = (By.XPATH, "//p[normalize-space()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    MAIN_A_6 = (By.XPATH, "//p[normalize-space()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    MAIN_A_7 = (By.XPATH, "//p[normalize-space()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")
