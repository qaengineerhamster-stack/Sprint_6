import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.rent_page_locators import RentPageLocators


class RentPage(BasePage):
    def _color_locator(self, color: str):
        mapping = {
            "black": RentPageLocators.COLOR_BLACK,
            "grey": RentPageLocators.COLOR_GREY,
        }
        return mapping[color]  # если пришло не то — упадёт честно

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rent_form(self, data: dict):
        self.type(RentPageLocators.DATE, data["date"])
        self.send_keys(RentPageLocators.DATE, Keys.ENTER)

        # закрываем datepicker
        if not self.try_click_if_present(RentPageLocators.PAGE_TITLE, timeout=1):
            self.js_click_body()

        self.click_safe(RentPageLocators.PERIOD_DROPDOWN)
        self.click_safe(RentPageLocators.PERIOD_OPTION(data["period"]))

        self.click_safe(self._color_locator(data["color"]))
        self.type(RentPageLocators.COMMENT, data.get("comment", ""))

    @allure.step("Оформить заказ и подтвердить (если нужно)")
    def submit_order_and_confirm(self):
        self.click_safe(RentPageLocators.ORDER)

        wait = WebDriverWait(self.driver, 15)

        def either_confirm_or_success(d):
            yes = d.find_elements(*RentPageLocators.YES_BUTTON_ANYWHERE)
            ok = d.find_elements(*RentPageLocators.SUCCESS_TEXT)
            return (yes[0] if yes else None) or (ok[0] if ok else None)

        el = wait.until(either_confirm_or_success)
        if el.tag_name.lower() == "button" and el.text.strip() == "Да":
            # кликаем через BasePage safe (по локатору)
            self.click_safe(RentPageLocators.YES_BUTTON_ANYWHERE)

    def assert_success(self):
        assert self.is_visible(RentPageLocators.SUCCESS_TEXT)