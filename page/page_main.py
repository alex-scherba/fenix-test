from helpers.locators import MainPageLocators
from page.page_base import BasePage

row_name = ['star', 'symbol', 'last_price', 'change_day', 'high_day', 'low_day', 'volume_day']


class MainPage(BasePage):

    @staticmethod
    def _remove_commas_from_value_in_dict(dictionary):
        for key, value in dictionary.items():
            if ',' in value:
                dictionary[key] = value.replace(',', '')
        return dictionary

    def click_button_usd(self):
        self._find_element(MainPageLocators.USD_BUTTON).click()

    def click_button_eur(self):
        self._find_element(MainPageLocators.EUR_BUTTON).click()

    def get_record_from_stats_table_by_symbol_name(self, symbol_name):
        tab_data = self.driver.find_element(*MainPageLocators.STATS_TABLE)
        list_rows = [[cell.text for cell in row.find_elements(*MainPageLocators.TD_TAG)]
                     for row in tab_data.find_elements(*MainPageLocators.TR_TAG)]
        record = [dict(zip(row_name, row)) for row in list_rows if symbol_name in row].pop()
        return self._remove_commas_from_value_in_dict(record)

