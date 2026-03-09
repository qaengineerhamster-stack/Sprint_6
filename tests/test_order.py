import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage

from data.urls import BASE_URL
from data.order_data import ORDER_DATA


@allure.feature("Order")
@pytest.mark.parametrize("data", ORDER_DATA)
def test_order_positive_flow_with_two_datasets(driver, data):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()
    main.click_order_top()

    order = OrderPage(driver)
    order.fill_customer_form(data)
    order.click_next()

    rent = RentPage(driver)
    rent.fill_rent_form(data)
    rent.submit_order_and_confirm()
    rent.assert_success()


@allure.feature("Order")
@pytest.mark.parametrize(
    "entry_click",
    [MainPage.click_order_top, MainPage.click_order_bottom],
    ids=["top", "bottom"],
)
def test_order_entry_points_open_order_page(driver, entry_click):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()

    entry_click(main)

    order = OrderPage(driver)
    assert order.is_opened()