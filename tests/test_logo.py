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

    assert "qa-scooter" in order.current_url()


@allure.feature("Logo")
def test_click_yandex_logo_opens_new_tab(driver):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()
    main.click_order_top()

    order = OrderPage(driver)
    order.click_yandex_logo()
    order.switch_to_new_window()
    order.wait_url_not("about:blank", timeout=10)

    url = order.current_url().lower()
    assert ("dzen" in url) or ("zen" in url) or ("yandex" in url)