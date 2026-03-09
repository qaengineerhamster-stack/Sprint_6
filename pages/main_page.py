import allure
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Принять cookies, если баннер показан")
    def accept_cookies_if_present(self):
        try:
            self.find(MainPageLocators.COOKIE_BANNER)
            self.click_safe(MainPageLocators.COOKIE_ACCEPT)
        except TimeoutException:
            pass

    def click_order_top(self):
        self.click_safe(MainPageLocators.ORDER_TOP)

    def click_order_bottom(self):
        self.click_safe(MainPageLocators.ORDER_BOTTOM)

    def open_faq_answer(self, i: int):
        self.click_safe(MainPageLocators.FAQ_QUESTION(i))

    def get_faq_answer_text(self, i: int) -> str:
        return self.find_visible(MainPageLocators.FAQ_ANSWER(i)).text