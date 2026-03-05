import allure
from pages.base_page import BasePage
from pages.locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_customer_form(self, data: dict):
        self.type(OrderPageLocators.NAME, data["name"])
        self.type(OrderPageLocators.SURNAME, data["surname"])
        self.type(OrderPageLocators.ADDRESS, data["address"])

        self.click(OrderPageLocators.METRO)
        self.type(OrderPageLocators.METRO, data["metro"])
        self.click(OrderPageLocators.METRO_OPTION)

        self.type(OrderPageLocators.PHONE, data["phone"])

    @allure.step("Нажать Далее")
    def click_next(self):
        self.click(OrderPageLocators.NEXT)

    @allure.step("Нажать логотип Самоката")
    def click_samokat_logo(self):
        self.click(OrderPageLocators.LOGO_SAMOKAT)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click(OrderPageLocators.LOGO_YANDEX)