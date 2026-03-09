import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import BASE_URL, SAMOKAT_URL_MARKER, DZEN_URL_MARKER


@allure.feature("Logo")
def test_click_samokat_logo_returns_to_main(driver):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()
    main.click_order_top()

    order = OrderPage(driver)
    order.click_samokat_logo()

    assert SAMOKAT_URL_MARKER in order.current_url()


@allure.feature("Logo")
def test_click_yandex_logo_opens_dzen_in_new_window(driver):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()
    main.click_order_top()

    order = OrderPage(driver)
    order.click_yandex_logo()
    order.switch_to_new_window()
    order.wait_until_url_changes_from("about:blank", timeout=10)

    assert DZEN_URL_MARKER in order.current_url().lower()