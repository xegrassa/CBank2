from selenium.webdriver.common.by import By


class MainPageLocators:
    MARKETS_MENU = (By.XPATH, ".//a[@class='nav' and text() = 'Котировки']")
    STOCKS_SUBMENU = (By.XPATH, ".//a[@href='/equities/' and text() = 'Акции']")
    RUSSIAN_SUBMENU = (By.XPATH, ".//a[@href='/equities/russia' and text() = 'Россия']")


class RussianStocksPageLocators:
    RUSSIAN_STOCKS_PAGE = (
        By.XPATH, ".//h1[@class = 'float_lang_base_1 shortH1 relativeAttr' and text() = 'Россия - акции	']")
    STOCKS_TABLE = (By.CSS_SELECTOR, "#cross_rate_markets_stocks_1 > tbody tr")

    def get_company_locator(name: str):
        return (By.XPATH, f".//a[text() = '{name}']")


class RussianCompanyPageLocators:
    DIVIDENDI = (By.XPATH, ".//div[@class = 'clear overviewDataTable overviewDataTableWithTooltip']/div[9]/span[2]")


class StockLocator:
    NAME = (By.CSS_SELECTOR, '.bold.left.noWrap.elp.plusIconTd a')
    LAST_PRICE = (By.CSS_SELECTOR, 'td[class$="-last"]')
