import allure
import pytest

from pages.main_page import MainPage
from data.urls import BASE_URL
from data.faq_expected import FAQ_EXPECTED


@allure.feature("FAQ")
@pytest.mark.parametrize("question_id", list(FAQ_EXPECTED.keys()))
def test_faq_answer_opens_correct_text(driver, question_id):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.accept_cookies_if_present()

    page.open_faq_answer(question_id)
    text = page.get_faq_answer_text(question_id)

    assert FAQ_EXPECTED[question_id] in text