from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_TOP = (By.XPATH, "(//button[contains(@class,'Button_Button') and normalize-space()='Заказать'])[1]")
    ORDER_BOTTOM = (By.XPATH, "(//button[contains(@class,'Button_Button') and normalize-space()='Заказать'])[2]")

    FAQ_QUESTION = lambda i: (By.ID, f"accordion__heading-{i}")
    FAQ_ANSWER = lambda i: (By.ID, f"accordion__panel-{i}")

    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_ACCEPT = (By.XPATH, "//button[contains(@class,'App_CookieButton') and normalize-space()='да все привыкли']")


class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[contains(@class,'select-search__select')]//button")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT = (By.XPATH, "//button[normalize-space()='Далее']")

    LOGO_SAMOKAT = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")


class RentPageLocators:
    PAGE_TITLE = (By.XPATH, "//div[contains(@class,'Order_Header') and contains(text(),'Про аренду')]")

    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    PERIOD_OPTION = lambda text: (By.XPATH, f"//div[contains(@class,'Dropdown-option') and normalize-space()='{text}']")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space()='Заказать']")

    YES_BUTTON_ANYWHERE = (By.XPATH, "//button[normalize-space()='Да']")
    SUCCESS_TEXT = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")