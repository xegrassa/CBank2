from selenium import webdriver
import json
import os

CHROME = 'chrome'
FIREFOX = 'firefox'


class BrowserCreator:
    def __init__(self, *args, **kwargs):
        self.browser_name = kwargs['browser_name']
        self.headless = kwargs['headless']
        self.firefox_binary_path = kwargs['firefox_binary_path']
        self.chromedriver_path = os.path.join(os.getcwd(), 'browser_webdriver', 'chromedriver.exe')
        self.geckodriver_path = os.path.join(os.getcwd(), 'browser_webdriver', 'geckodriver.exe')
        self.options = None

    def _set_options(self):
        if not self.headless:
            return None
        if self.browser_name == CHROME:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('headless')
        if self.browser_name == FIREFOX:
            self.options = webdriver.FirefoxOptions
            self.options.add_argument('headless')

    def get_browser(self):
        self._set_options()
        if self.browser_name == CHROME:
            return webdriver.Chrome(executable_path=self.chromedriver_path, chrome_options=self.options)
        if self.browser_name == FIREFOX:
            return webdriver.Firefox(executable_path=self.geckodriver_path, firefox_options=self.options,
                                     firefox_binary=self.firefox_binary_path)


def convert_str_to_float(string: str) -> float:
    return float(string.replace('.', '').replace(',', '.'))


def get_data_json(path: str):
    with open(path) as f:
        data = json.load(f)
    return data
