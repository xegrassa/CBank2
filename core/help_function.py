from selenium import webdriver
import json


def get_browser(browser_name: str, driver_paths: dict, headless: bool = False):
    if headless is True and browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return webdriver.Chrome(driver_paths[browser_name], chrome_options=options)
    if browser_name == 'chrome':
        return webdriver.Chrome(driver_paths[browser_name])
    if headless is True and browser_name == 'firefox':
        options = webdriver.FirefoxOptions
        options.add_argument('headless')
        return webdriver.Firefox(executable_path=driver_paths[browser_name],
                                 firefox_options=options,
                                 firefox_binary=driver_paths['path_firefox_binary'])
    if browser_name == 'firefox':
        return webdriver.Firefox(executable_path=driver_paths[browser_name],
                                 firefox_binary=driver_paths['path_firefox_binary'])


def convert_str_to_float(string: str) -> float:
    return float(string.replace('.', '').replace(',', '.'))


def get_data_json(path: str):
    with open(path) as f:
        data = json.load(f)
    return data
