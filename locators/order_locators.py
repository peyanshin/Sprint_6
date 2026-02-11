from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")

    FOR_WHOM_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    FOR_WHOM_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    FOR_WHOM_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    FOR_WHOM_METRO = (By.XPATH, "//div[@class='select-search']//input[@placeholder='* Станция метро']")  # Выбор станции метро
    METRO_OPTION_TEMPLATE = ".//*[contains(@class, 'select-search__options')]//div[normalize-space()='{}']"
    FOR_WHOM_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    FOR_WHOM_NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")

    RENT_DATE = (By.XPATH, "//input[@type='text' and @placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control') or contains(@class, 'Dropdown-menu')]")

    RENT_BLACK_PERL = (By.XPATH, "//label[@for='black' and text()='чёрный жемчуг']")
    RENT_GREY_HOPELESSNESS = (By.XPATH, "//label[@for='grey' and text()='серая безысходность']")
    RENT_COMMENT = (By.XPATH, "//input[@type='text' and @placeholder='Комментарий для курьера']")
    RENT_BACK_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Назад']")
    RENT_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    RENT_NO_BUTTON = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Нет']")
    RENT_YES_BUTTON = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Да']")
    RENT_ORDER_NUMBER = (By.XPATH, "//div[@class='Order_Text__2broi']")
    RENT_ORDER_INFO_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']//button[text()='Посмотреть статус']")

    CHECK_NAME = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Имя']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_LAST_NAME = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Фамилия']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_ADDRESS = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Адрес']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_METRO = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Станция метро']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_PHONE = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Телефон']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_DATE = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Дата доставки']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_PERIOD = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Срок аренды']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_COLOR = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Цвет']]//div[contains(@class, 'Track_Value__15eEX')]")
    CHECK_COMMENT = (By.XPATH, "//div[contains(@class, 'Track_Row__1sN1F')][.//div[contains(@class, 'Track_Title__1XfhB') and text()='Комментарий']]//div[contains(@class, 'Track_Value__15eEX')]")

    @staticmethod
    def get_metro_option_locator(station_name):
        return (By.XPATH, f"//div[text()='{station_name}']")

    @staticmethod
    def get_period_option_locator(period):
        return (By.XPATH, f".//div[contains(@class, 'Dropdown-option') or contains(@class, 'option')][normalize-space()='{period}']")

    @staticmethod
    def get_calendar_day_locator(day_number):
        return (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day_number}']")

    @staticmethod
    def get_datepicker_locator():
        return (By.CLASS_NAME, "react-datepicker")
