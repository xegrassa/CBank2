import json
import os

from selenium import webdriver

from investing_parse import CHROMEDRIVER_PATH, GECKODRIVER_PATH, CHROME, \
    FIREFOX


class BrowserCreator:
    def __init__(self, **kwargs):
        self.browser_name = kwargs['browser_name']
        self.headless = kwargs['headless']
        self.firefox_binary_path = kwargs['firefox_binary_path']
        self.chromedriver_path = CHROMEDRIVER_PATH
        self.geckodriver_path = GECKODRIVER_PATH
        self.options = None

    def _set_options(self):
        """Set Browser Options"""
        if not self.headless:
            return None
        if self.browser_name == CHROME:
            self.options = webdriver.ChromeOptions()
        if self.browser_name == FIREFOX:
            self.options = webdriver.FirefoxOptions
        self.options.headless = True

    def get_browser(self):
        """Return a new instance driver (Chrome or FireFox) with settings"""
        self._set_options()
        if self.browser_name == CHROME:
            return webdriver.Chrome(executable_path=self.chromedriver_path,
                                    chrome_options=self.options)
        if self.browser_name == FIREFOX:
            if os.name == 'nt':
                return webdriver.Firefox(executable_path=self.geckodriver_path,
                                         firefox_options=self.options,
                                         firefox_binary=self.firefox_binary_path)
            else:
                return webdriver.Firefox(executable_path=self.geckodriver_path,
                                         firefox_options=self.options)


def convert_str_to_float(string: str) -> float:
    """Convert string number example: 1.234,5 -> 1234.5"""
    return float(string.replace('.', '').replace(',', '.'))


def get_data_json(path: str):
    """Read data from json"""
    with open(path) as f:
        data = json.load(f)
    return data
