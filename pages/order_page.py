import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_customer_form(self, data: dict):
        self.type(OrderPageLocators.NAME, data["name"])
        self.type(OrderPageLocators.SURNAME, data["surname"])
        self.type(OrderPageLocators.ADDRESS, data["address"])

        self.click_safe(OrderPageLocators.METRO)
        self.type(OrderPageLocators.METRO, data["metro"])
        self.click_safe(OrderPageLocators.METRO_OPTION)

        self.type(OrderPageLocators.PHONE, data["phone"])

    def click_next(self):
        self.click_safe(OrderPageLocators.NEXT)

    def click_samokat_logo(self):
        self.click_safe(OrderPageLocators.LOGO_SAMOKAT)

    def click_yandex_logo(self):
        self.click_safe(OrderPageLocators.LOGO_YANDEX)

    def is_opened(self) -> bool:
        return self.is_visible(OrderPageLocators.NAME)