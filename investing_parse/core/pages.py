from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from investing_parse.core.locators import MainPageLocators, RussianStocksPageLocators, RussianCompanyPageLocators
from investing_parse.core.storage import Stock


class BasePage:

    def __init__(self, driver):
        """Constructor, takes a WebDriver instance"""
        self.driver = driver

    def find_element(self, locator, time=10):
        """Find an element given a By strategy and locator. Waiting added"""
        print(locator[0], locator[1])
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """Find an elements given a By strategy and locator. Waiting added"""
        print(locator[0], locator[1])
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url):
        """Loads a web page in the current browser session"""
        self.driver.get(url)

    def refresh(self):
        """Refreshes the current page"""
        self.driver.refresh()

    def close(self):
        """Closes the browser"""
        self.driver.quit()

    def screenshot(self, path):
        """Saves a screenshot of the current window to a PNG image file"""
        self.driver.get_screenshot_as_file(path)


class InvestingMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://ru.investing.com/'

    def _move_on_markets(self):
        """Open sub-menu markets"""
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.MARKETS_MENU))
        action.perform()

    def _move_on_stocks(self):
        """Open sub-menu stocks with opened markets"""
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.STOCKS_SUBMENU))
        action.perform()

    def _move_on_russian(self):
        """Move mouse target to Russia with opened sub-menu markets -> stocks"""
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.RUSSIAN_SUBMENU))
        action.perform()

    def _click(self):
        """Clicks on current mouse position"""
        action = ActionChains(self.driver)
        action.click()
        action.perform()

    def go_to_main_page(self):
        """Open Main Page Investing"""
        self.go_to_site(self.base_url)

    def go_to_russian_stocks_page(self):
        """Open Russian Stocks Page"""
        self._move_on_markets()
        self._move_on_stocks()
        self._move_on_russian()
        self._click()
        return RussianStocksPage(self.driver)

    def on_investing_main_page(self):
        """Check that the page is open"""
        element = self.driver.title
        if element == 'Investing.com - котировки и финансовые новости':
            return True
        return False


class RussianStocksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.stocks = None

    def on_russian_stocks_page(self):
        """Check that the page is open"""
        try:
            self.find_element(RussianStocksPageLocators.RUSSIAN_STOCKS_PAGE)
        except:
            return False
        return True

    def get_russian_stocks(self):
        """Find stocks and return list of Stock"""
        if self.stocks is None:
            html_stocks = self.find_elements(RussianStocksPageLocators.STOCKS_TABLE)
            self.stocks = list(map(Stock, html_stocks))
        return self.stocks

    def go_to_company(self, company_name):
        """Open Company Page"""
        company_locator = RussianStocksPageLocators.get_company_locator(company_name)
        self.find_element(company_locator).click()
        return CompanyPage(self.driver)


class CompanyPage(BasePage):
    def get_divident(self):
        """Return company dividend"""
        return self.find_element(RussianCompanyPageLocators.DIVIDENDI).text.split()[1]
