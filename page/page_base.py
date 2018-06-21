import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

TIME_OUT = 20


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator):
        try:
            return WebDriverWait(self.driver, TIME_OUT).until(expected_conditions.presence_of_element_located(locator))
        except selenium.common.exceptions.TimeoutException:
            raise Exception("Element not found")
