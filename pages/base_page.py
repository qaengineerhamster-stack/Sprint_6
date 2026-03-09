import allure
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self._driver = driver
        self._wait = WebDriverWait(driver, timeout)

    @property
    def driver(self):
        return self._driver

    def open(self, url: str):
        self._driver.get(url)

    def find(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator) -> bool:
        self.find_visible(locator)
        return True

    def scroll_into_view(self, locator):
        el = self.find(locator)
        self._driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        return el

    @allure.step("Безопасный клик: {locator}")
    def click_safe(self, locator):
        el = self.scroll_into_view(locator)
        try:
            self._wait.until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            self._driver.execute_script("arguments[0].click();", el)

    @allure.step("Ввести текст '{value}' в поле: {locator}")
    def type(self, locator, value: str):
        el = self.find_visible(locator)
        el.clear()
        el.send_keys(value)

    def send_keys(self, locator, keys):
        el = self.find(locator)
        el.send_keys(keys)

    def js_click_body(self):
        self._driver.execute_script("document.body.click();")

    def current_url(self) -> str:
        return self._driver.current_url

    def wait_until_url_changes_from(self, url: str, timeout: int = 10):
        WebDriverWait(self._driver, timeout).until(lambda d: d.current_url != url)

    def switch_to_new_window(self):
        self._wait.until(lambda d: len(d.window_handles) > 1)
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def try_click_if_present(self, locator, timeout: int = 2) -> bool:
        try:
            WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable(locator)).click()
            return True
        except TimeoutException:
            return False

    def wait_until(self, condition, timeout: int = 10):
        return WebDriverWait(self._driver, timeout).until(condition)