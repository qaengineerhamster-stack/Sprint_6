import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Принять cookies, если баннер показан")
    def accept_cookies_if_present(self):
        # если баннер не показывается — просто ничего не делаем
        try:
            self.wait.until(lambda d: d.find_element(*MainPageLocators.COOKIE_BANNER))
            self.click_safe(MainPageLocators.COOKIE_ACCEPT)
        except Exception:
            pass

    @allure.step("Нажать кнопку Заказать (вверху)")
    def click_order_top(self):
        self.click_safe(MainPageLocators.ORDER_TOP)

    @allure.step("Нажать кнопку Заказать (внизу)")
    def click_order_bottom(self):
        self.click_safe(MainPageLocators.ORDER_BOTTOM)

    @allure.step("Открыть FAQ вопрос #{i}")
    def open_faq_answer(self, i: int):
        self.click_safe(MainPageLocators.FAQ_QUESTION(i))

    @allure.step("Получить текст ответа FAQ #{i}")
    def get_faq_answer_text(self, i: int) -> str:
        return self.get_text(MainPageLocators.FAQ_ANSWER(i))