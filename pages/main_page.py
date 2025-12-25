from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def open_answer(self, question_locator):
        self.scroll_to(question_locator)
        self.click(question_locator)

    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    def click_order_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
