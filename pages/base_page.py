from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def wait_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait_clickable(locator).click()

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_windows_count(self, count, timeout=5):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) == count)

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def wait_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: text in d.current_url)
