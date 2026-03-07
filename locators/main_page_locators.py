from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_TOP = (By.XPATH, "(//button[contains(@class,'Button_Button') and normalize-space()='Заказать'])[1]")
    ORDER_BOTTOM = (By.XPATH, "(//button[contains(@class,'Button_Button') and normalize-space()='Заказать'])[2]")

    FAQ_QUESTION = lambda i: (By.ID, f"accordion__heading-{i}")
    FAQ_ANSWER = lambda i: (By.ID, f"accordion__panel-{i}")

    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_ACCEPT = (By.XPATH, "//button[contains(@class,'App_CookieButton') and normalize-space()='да все привыкли']")