from selenium import webdriver
import json


def get_browser(browser_name, headless, path_chromedriver):
    if headless and browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return webdriver.Chrome(path_chromedriver, chrome_options=options)
    if browser_name == 'chrome':
        return webdriver.Chrome(path_chromedriver)


def convert_str_to_float(string: str) -> float:
    return float(string.replace('.', '').replace(',', '.'))


def get_data_json(path: str):
    with open(path) as f:
        data = json.load(f)
    return data
