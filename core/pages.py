from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.locators import Main_Page_Locators
from selenium.webdriver import ActionChains
from core.locators import Main_Page_Locators, Russian_Stocks_Page_Locators

INVESTING_URL = 'https://ru.investing.com/'


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = INVESTING_URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        self.driver.get(self.base_url)

    def refresh(self):
        self.driver.refresh()

    def on_site_investing(self):
        element = self.driver.title
        if element == 'Investing.com - котировки и финансовые новости':
            return True
        return False

    def close(self):
        self.driver.quit()


class Stock:
    def __init__(self, stock):
        self.stock = stock.text
        self.price_last = self.stock.split()[-7]
        self.name = ' '.join(self.stock.split()[:-7])

    def get_name(self):
        return self.name

    def get_last_price(self):
        return self.price_last


class SearchHelper(BasePage):

    def move_on_page_russian_stocks(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(Main_Page_Locators.LOCATOR_MARKETS_MENU))
        action.move_to_element(self.find_element(Main_Page_Locators.LOCATOR_STOCKS_SUBMENU))
        action.move_to_element(self.find_element(Main_Page_Locators.LOCATOR_RUSSIAN_SUBMENU))
        action.click()
        action.perform()

    def on_page_russian_stocks(self):
        try:
            self.find_element(Russian_Stocks_Page_Locators.LOCATOR_PAGE_RUSSIAN_STOCKS)
        except:
            return False
        return True

    def get_russian_stocks_table(self):
        stocks = self.find_element(Russian_Stocks_Page_Locators.LOCATOR_RUSSIAN_STOCKS_TABLE)
        return stocks
