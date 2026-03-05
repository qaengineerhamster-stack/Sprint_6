import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from pages.locators import OrderPageLocators

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

ORDER_DATA = [
    {
        "name": "Павел",
        "surname": "Соколов",
        "address": "Москва, ул. Тестовая 1",
        "metro": "Арбатская",
        "phone": "+79990000001",
        "date": "10.03.2026",
        "period": "двое суток",
        "color": "black",
        "comment": "Позвонить за 10 минут",
    },
    {
        "name": "Анна",
        "surname": "Иванова",
        "address": "Москва, ул. Пример 2",
        "metro": "Сокольники",
        "phone": "+79990000002",
        "date": "15.03.2026",
        "period": "трое суток",
        "color": "grey",
        "comment": "Оставить у двери",
    },
]

@allure.feature("Order")
@pytest.mark.parametrize("data", ORDER_DATA)
def test_order_positive_flow_with_two_datasets(driver, data):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()

    # полный флоу только через одну точку входа (верхняя кнопка)
    main.click_order_top()

    order = OrderPage(driver)
    order.fill_customer_form(data)
    order.click_next()

    rent = RentPage(driver)
    rent.fill_rent_form(data)
    rent.submit_order_and_confirm()
    rent.assert_success()


@allure.feature("Order")
@pytest.mark.parametrize("entry", ["top", "bottom"])
def test_order_entry_points_open_order_page(driver, entry):
    main = MainPage(driver)
    main.open(BASE_URL)
    main.accept_cookies_if_present()

    if entry == "top":
        main.click_order_top()
    else:
        main.click_order_bottom()

    order = OrderPage(driver)
    assert order.is_visible(OrderPageLocators.NAME)