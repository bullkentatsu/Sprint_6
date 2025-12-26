from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_step_one(self, name, surname, address, metro, phone):
        self.wait_visible(OrderPageLocators.NAME).send_keys(name)
        self.wait_visible(OrderPageLocators.SURNAME).send_keys(surname)
        self.wait_visible(OrderPageLocators.ADDRESS).send_keys(address)

        metro_input = self.wait_visible(OrderPageLocators.METRO)
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

        self.wait_visible(OrderPageLocators.PHONE).send_keys(phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_step_two(self, date, color_locator, comment):
        date_input = self.wait_visible(OrderPageLocators.DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENT_PERIOD_FIRST_OPTION)

        self.click(color_locator)
        self.wait_visible(OrderPageLocators.COMMENT).send_keys(comment)

    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_yes(self):
        self.click(OrderPageLocators.YES_BUTTON)

    def is_success_modal_displayed(self):
        self.wait_visible(OrderPageLocators.SUCCESS_MODAL_HEADER)
        return True
