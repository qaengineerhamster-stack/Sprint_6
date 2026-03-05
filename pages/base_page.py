import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу: {url}")
    def open(self, url: str):
        self.driver.get(url)

    def scroll_into_view(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Безопасный клик (со скроллом) по элементу: {locator}")
    def click_safe(self, locator):
        el = self.scroll_into_view(locator)
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            # запасной вариант — клик через JS
            self.driver.execute_script("arguments[0].click();", el)

    @allure.step("Ввести текст '{value}' в поле: {locator}")
    def type(self, locator, value: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator) -> bool:
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    @allure.step("Дождаться, что URL содержит: {part}")
    def wait_url_contains(self, part: str):
        self.wait.until(EC.url_contains(part))

    @allure.step("Переключиться на новое окно/вкладку")
    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])