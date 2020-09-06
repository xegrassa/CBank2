from selenium.webdriver.common.by import By


class MainPageLocators:
    MARKETS_MENU = (By.XPATH, ".//a[@class='nav' and text() = 'Котировки']")
    STOCKS_SUBMENU = (By.XPATH, ".//a[@href='/equities/' and text() = 'Акции']")
    RUSSIAN_SUBMENU = (By.XPATH, ".//a[@href='/equities/russia' and text() = 'Россия']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login.bold")


class LoginFormLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#signup")

    LOGIN_INPUT = (By.CSS_SELECTOR, "#loginFormUser_email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#loginForm_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#signup .newButton.orange")

    EMAIL_ERROR = (By.CSS_SELECTOR, "#emailSigningNotify.error")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "#passwordSigningNotify.error")
    AUTHORIZATION_ERROR = (By.CSS_SELECTOR, "#serverErrors")


class RussianStocksPageLocators:
    RUSSIAN_STOCKS_PAGE = (
        By.XPATH, ".//h1[@class = 'float_lang_base_1 shortH1 relativeAttr' and text() = 'Россия - акции	']")
    STOCKS_TABLE = (By.CSS_SELECTOR, "#cross_rate_markets_stocks_1 > tbody tr")

    def get_company_locator(name: str):
        return (By.XPATH, f".//a[text() = '{name}']")


class RussianCompanyPageLocators:
    DIVIDENDI = (By.CSS_SELECTOR, ".clear.overviewDataTable.overviewDataTableWithTooltip :nth-child(9) .float_lang_base_2")


class StockLocator:
    NAME = (By.CSS_SELECTOR, '.bold.left.noWrap.elp.plusIconTd a')
    LAST_PRICE = (By.CSS_SELECTOR, 'td[class*="-last"]')
