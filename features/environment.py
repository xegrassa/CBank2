from configparser import ConfigParser
from core.help_function import get_browser


def before_scenario(context, scenario):
    config = ConfigParser()
    config.read('behave.ini')
    browser = config.get('behave', 'browser')
    headless = config.getboolean('behave', 'headless')
    context.path_chromedriver = config.get('behave', 'path_chromedriver')
    path_db = config.get('behave', 'stocks_db')
    driver = get_browser(browser, headless, context.path_chromedriver)
    context.driver = driver
    context.path_db = path_db


def after_scenario(context, scenario):
    context.driver.quit()
