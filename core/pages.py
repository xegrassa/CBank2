from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from core.locators import MainPageLocators, RussianStocksPageLocators, RussianCompanyPageLocators
from core.storage import Stock


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.quit()

    def screenshot(self, path):
        self.driver.get_screenshot_as_file(path)


class InvestingMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://ru.investing.com/'

    def _move_on_markets(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.MARKETS_MENU))
        action.perform()

    def _move_on_stocks(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.STOCKS_SUBMENU))
        action.perform()

    def _move_on_russian(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.RUSSIAN_SUBMENU))
        action.perform()

    def _click(self):
        action = ActionChains(self.driver)
        action.click()
        action.perform()

    def go_to_main_page(self):
        self.go_to_site(self.base_url)

    def go_to_russian_stocks_page(self):
        self._move_on_markets()
        self._move_on_stocks()
        self._move_on_russian()
        self._click()
        return RussianStocksPage(self.driver)

    def on_investing_main_page(self):
        element = self.driver.title
        if element == 'Investing.com - котировки и финансовые новости':
            return True
        return False


class RussianStocksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.stocks = None

    def on_russian_stocks_page(self):
        try:
            self.find_element(RussianStocksPageLocators.RUSSIAN_STOCKS_PAGE)
        except:
            return False
        return True

    def get_russian_stocks(self):
        if self.stocks is None:
            html_stocks = self.find_elements(RussianStocksPageLocators.STOCKS_TABLE)
            self.stocks = map(Stock, html_stocks)
        return self.stocks

    def go_to_company(self, company_name):
        company_locator = RussianStocksPageLocators.get_company_locator(company_name)
        self.find_element(company_locator).click()
        return CompanyPage(self.driver)


class CompanyPage(BasePage):
    def get_divident(self):
        return self.find_element(RussianCompanyPageLocators.DIVIDENDI).text.split()[1]
