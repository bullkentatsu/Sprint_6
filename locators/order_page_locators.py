from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = (By.XPATH, "//*[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//*[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//*[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Далее']")

    DATE = (By.XPATH, "//*[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CSS_SELECTOR, "span.Dropdown-arrow")
    RENT_PERIOD_FIRST_OPTION = (By.XPATH, "//div[contains(@class,'Dropdown-option')][1]")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT = (By.XPATH, "//*[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[normalize-space(text())='Заказать'])[last()]")
    YES_BUTTON = (By.XPATH, "//button[normalize-space(text())='Да']")
    SUCCESS_TEXT = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")
