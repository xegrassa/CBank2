from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from core.locators import MainPageLocators, RussianStocksPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://ru.investing.com/'

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

    def _move_on_markets(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.LOCATOR_MARKETS_MENU))
        action.perform()

    def _move_on_stocks(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.LOCATOR_STOCKS_SUBMENU))
        action.perform()

    def _move_on_russian(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(MainPageLocators.LOCATOR_RUSSIAN_SUBMENU))
        action.perform()

    def _click(self):
        action = ActionChains(self.driver)
        action.click()
        action.perform()

    # def on_page_russian_stocks(self):
    #     try:
    #         self.find_element(RussianStocksPageLocators.LOCATOR_PAGE_RUSSIAN_STOCKS)
    #     except:
    #         return False
    #     return True

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

    # def get_russian_stocks_table(self):
    #     stocks = self.find_element(RussianStocksPageLocators.LOCATOR_RUSSIAN_STOCKS_TABLE)
    #     return stocks


class RussianStocksPage(BasePage):
    def on_russian_stocks_page(self):
        try:
            self.find_element(RussianStocksPageLocators.LOCATOR_PAGE_RUSSIAN_STOCKS)
        except:
            return False
        return True

    def get_russian_stocks_table(self):
        stocks = self.find_element(RussianStocksPageLocators.LOCATOR_RUSSIAN_STOCKS_TABLE)
        return stocks


class CompanyPage(BasePage):
    pass
