
from selenium.webdriver.common.by import By


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