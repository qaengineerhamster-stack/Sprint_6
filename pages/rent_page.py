import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import RentPageLocators


class RentPage(BasePage):
    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rent_form(self, data: dict):
        # дата: вводим и подтверждаем Enter, чтобы календарь точно принял значение
        self.type(RentPageLocators.DATE, data["date"])
        try:
            self.driver.find_element(*RentPageLocators.DATE).send_keys(Keys.ENTER)
        except Exception:
            pass

        # закрываем календарь (datepicker), чтобы он не перекрывал dropdown
        try:
            self.click_safe(RentPageLocators.PAGE_TITLE)
        except Exception:
            self.driver.execute_script("document.body.click();")

        self.click_safe(RentPageLocators.PERIOD_DROPDOWN)
        self.click_safe(RentPageLocators.PERIOD_OPTION(data["period"]))

        if data.get("color") == "black":
            self.click_safe(RentPageLocators.COLOR_BLACK)
        elif data.get("color") == "grey":
            self.click_safe(RentPageLocators.COLOR_GREY)

        self.type(RentPageLocators.COMMENT, data.get("comment", ""))

    @allure.step("Оформить заказ и подтвердить (если нужно)")
    def submit_order_and_confirm(self):
        # 1) жёсткий клик по "Заказать"
        btn = self.scroll_into_view(RentPageLocators.ORDER)
        try:
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)

        # 2) ждём: либо появится кнопка "Да" (подтверждение), либо сразу "Заказ оформлен"
        wait = WebDriverWait(self.driver, 15)

        def either_confirm_or_success(d):
            yes = d.find_elements(*RentPageLocators.YES_BUTTON_ANYWHERE)
            ok = d.find_elements(*RentPageLocators.SUCCESS_TEXT)
            return (yes[0] if yes else None) or (ok[0] if ok else None)

        el = wait.until(either_confirm_or_success)

        # 3) если это "Да" — подтверждаем
        try:
            if el.tag_name.lower() == "button" and el.text.strip() == "Да":
                try:
                    el.click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", el)
        except Exception:
            pass

    @allure.step("Проверить, что заказ оформлен успешно")
    def assert_success(self):
        assert self.is_visible(RentPageLocators.SUCCESS_TEXT)