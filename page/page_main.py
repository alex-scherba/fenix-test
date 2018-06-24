from entity.record_stats import RecordStats
from helpers.locators import MainPageLocators
from page.page_base import BasePage


class MainPage(BasePage):

    def click_button_usd(self):
        self._find_element(MainPageLocators.USD_BUTTON).click()

    def click_button_eur(self):
        self._find_element(MainPageLocators.EUR_BUTTON).click()

    def get_record_from_stats_table_by_symbol_name(self, symbol_name):
        tab_data = self.driver.find_element(*MainPageLocators.STATS_TABLE)
        list_rows = [[cell.text for cell in row.find_elements(*MainPageLocators.TD_TAG)]
                     for row in tab_data.find_elements(*MainPageLocators.TR_TAG)]
        return RecordStats(symbol_name, list_rows)
