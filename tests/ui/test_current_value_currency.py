import unittest
from hamcrest import *
from selenium import webdriver
from page.page_main import MainPage
from utils.api_client import ApiClient

SYMBOL = 'BTCUSD'
SITE_URL = 'https://www.bitfinex.com/?locale=ru'
IMPLICITLY_WAIT_PERIOD = 10


class CurrentValueCurrency(unittest.TestCase):

    def setUp(self):
        self.api_client = ApiClient()
        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(IMPLICITLY_WAIT_PERIOD)
        self.driver.maximize_window()
        self.driver.get(SITE_URL)

    def test_last_price(self):
        main_page = MainPage(self.driver)
        main_page.click_button_usd()
        row = main_page.get_record_from_stats_table_by_symbol_name(SYMBOL)
        assert_that(row.last_price, equal_to(self.api_client.get_last_price(SYMBOL)))

    def test_day_high(self):
        main_page = MainPage(self.driver)
        main_page.click_button_usd()
        row = main_page.get_record_from_stats_table_by_symbol_name(SYMBOL)
        assert_that(row.high_day, equal_to(self.api_client.get_high(SYMBOL)))

    def test_day_low(self):
        main_page = MainPage(self.driver)
        main_page.click_button_usd()
        row = main_page.get_record_from_stats_table_by_symbol_name(SYMBOL)
        assert_that(row.low_day, equal_to(self.api_client.get_low(SYMBOL)))

    @unittest.skip("clarifying the working principle for this field")
    def test_day_volume(self):
        main_page = MainPage(self.driver)
        main_page.click_button_usd()
        row = main_page.get_record_from_stats_table_by_symbol_name(SYMBOL)
        assert_that(row.volume_day, equal_to(self.api_client.get_volume(SYMBOL)))

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
