from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']")
    DZEN_BUTTON = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru']")
    SCOOTER_BUTTON = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR' and @href='/']")    
