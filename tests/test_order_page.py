from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import ORDER_DATA_TOP, ORDER_DATA_BOTTOM


class TestOrderPage:
    def test_order_positive_flow_from_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_order_top()

        order_page = OrderPage(driver)
        order_page.fill_step_one(
            ORDER_DATA_TOP["name"],
            ORDER_DATA_TOP["surname"],
            ORDER_DATA_TOP["address"],
            ORDER_DATA_TOP["metro"],
            ORDER_DATA_TOP["phone"],
        )
        order_page.fill_step_two(
            ORDER_DATA_TOP["date"],
            ORDER_DATA_TOP["color_locator"],
            ORDER_DATA_TOP["comment"],
        )
        order_page.submit_order()
        order_page.confirm_yes()

        assert order_page.is_success_modal_displayed()

    def test_order_positive_flow_from_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_order_bottom()

        order_page = OrderPage(driver)
        order_page.fill_step_one(
            ORDER_DATA_BOTTOM["name"],
            ORDER_DATA_BOTTOM["surname"],
            ORDER_DATA_BOTTOM["address"],
            ORDER_DATA_BOTTOM["metro"],
            ORDER_DATA_BOTTOM["phone"],
        )
        order_page.fill_step_two(
            ORDER_DATA_BOTTOM["date"],
            ORDER_DATA_BOTTOM["color_locator"],
            ORDER_DATA_BOTTOM["comment"],
        )
        order_page.submit_order()
        order_page.confirm_yes()

        assert order_page.is_success_modal_displayed()
