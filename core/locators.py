from selenium.webdriver.common.by import By


class MainPageLocators:
    MARKETS_MENU = (By.XPATH, ".//a[@class='nav' and text() = 'Котировки']")
    STOCKS_SUBMENU = (By.XPATH, ".//a[@href='/equities/' and text() = 'Акции']")
    RUSSIAN_SUBMENU = (By.XPATH, ".//a[@href='/equities/russia' and text() = 'Россия']")
    # TITLE = (By.TAG_NAME, "title")


class RussianStocksPageLocators:
    RUSSIAN_STOCKS_PAGE = (
        By.XPATH, ".//h1[@class = 'float_lang_base_1 shortH1 relativeAttr' and text() = 'Россия - акции	']")
    RUSSIAN_STOCKS_TABLE = (By.CSS_SELECTOR, "#cross_rate_markets_stocks_1 > tbody tr")
    # COMPANY = (By.XPATH, ".//a[text() = 'Яндекс']")
    # COMPANY_DATA = By.TAG_NAME, "tr"


class RussianCompanyPageLocators:
    LOCATOR_DIVIDENDI = (
        By.XPATH, ".//div[@class = 'clear overviewDataTable overviewDataTableWithTooltip']/div[9]/span[2]")
