from selenium.webdriver.common.by import By


class BasePageLocators:

    TR_TAG = (By.TAG_NAME, 'tr')
    TD_TAG = (By.TAG_NAME, 'td')


class MainPageLocators(BasePageLocators):

    USD_BUTTON = (By.XPATH, '//*[@id="tickers-landing-container"]/div/div/div[1]/div[2]')
    EUR_BUTTON = (By.XPATH, '//*[@id="tickers-landing-container"]/div/div/div[1]/div[3]')
    STATS_TABLE = (By.ID, 'fav-ticker-list-table')
