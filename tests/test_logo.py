import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@allure.feature("Logo")
def test_click_samokat_logo_returns_to_main(driver):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()
    main.click_order_top()

    order = OrderPage(driver)
    order.click_samokat_logo()

    assert "qa-scooter" in driver.current_url


@allure.feature("Logo")
def test_click_yandex_logo_opens_dzen_in_new_window(driver):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()
    main.click_order_top()

    order = OrderPage(driver)
    order.click_yandex_logo()

    order.switch_to_new_window()

    # ждём, пока уйдём с about:blank (в Firefox часто сначала так)
    order.wait.until(lambda d: d.current_url != "about:blank")

    url = driver.current_url.lower()
    assert ("dzen" in url) or ("zen" in url) or ("yandex" in url)