import pytest

from constants import BASE_URL, DZEN_DOMAIN_PART
from pages.main_page import MainPage
from test_data import FAQ_DATA


class TestMainPageFAQ:
    @pytest.mark.parametrize("question, answer, expected_text", FAQ_DATA)
    def test_faq_opens_correct_answer_text(self, driver, question, answer, expected_text):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.open_answer(question)

        assert expected_text in main_page.get_answer_text(answer)


class TestMainPageNavigation:
    def test_scooter_logo_goes_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_order_top()
        main_page.click_scooter_logo()

        assert main_page.current_url().startswith(BASE_URL)

    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()

        dzen_url = main_page.open_dzen_from_yandex_logo()
        assert DZEN_DOMAIN_PART in dzen_url
