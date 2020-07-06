from selenium.webdriver.common.by import By


class Main_Page_Locators:
    LOCATOR_MARKETS_MENU = (By.XPATH, ".//a[@class='nav' and text() = 'Котировки']")
    LOCATOR_STOCKS_SUBMENU = (By.XPATH, ".//a[@href='/equities/' and text() = 'Акции']")
    LOCATOR_RUSSIAN_SUBMENU = (By.XPATH, ".//a[@href='/equities/russia' and text() = 'Россия']")
    LOCATOR_TITLE = (By.TAG_NAME, "title")


class Russian_Stocks_Page_Locators:
    LOCATOR_PAGE_RUSSIAN_STOCKS = (
        By.XPATH, ".//h1[@class = 'float_lang_base_1 shortH1 relativeAttr' and text() = 'Россия - акции	']")
    LOCATOR_RUSSIAN_STOCKS_TABLE = (By.XPATH, ".//table[@id='cross_rate_markets_stocks_1']/tbody")
    LOCATOR_COMPANY = (By.XPATH, ".//a[text() = 'Яндекс']")
    LOCATOR_COMPANY_DATA = By.TAG_NAME, "tr"


class Russian_Company_Page_Locators:
    LOCATOR_DIVIDENDI = (
        By.XPATH, ".//div[@class = 'clear overviewDataTable overviewDataTableWithTooltip']/div[9]/span[2]")
