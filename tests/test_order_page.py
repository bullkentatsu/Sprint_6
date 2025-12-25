import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


BASE_URL = "https://qa-scooter.praktikum-services.ru/"


class TestOrderPage:
    @pytest.mark.parametrize(
        "entry_point, name, surname, address, metro, phone, date, rent_period, color, comment",
        [
            ("top", "Егор", "Робкий", "Москва, Москворечье 8", "Кантемировская", "+79774442211", "10.10.2025", "first", "black", "Привезите к подъезду"),
            ("bottom", "Ульяна", "Серьезная", "Москва, Москворечье 8", "Каширская", "+79653339010", "11.10.2025", "first", "grey", "Позвоните за час"),
        ],
    )
    def test_order_positive_flow(self, driver, entry_point, name, surname, address, metro, phone, date, rent_period, color, comment):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        if entry_point == "top":
            main_page.click_order_top()
        else:
            main_page.click_order_bottom()

        order_page = OrderPage(driver)
        order_page.fill_step_one(name, surname, address, metro, phone)
        order_page.fill_step_two(date, rent_period, color, comment)

        order_page.submit_order()
        order_page.confirm_yes()

        assert "Заказ оформлен" in order_page.get_success_text()
