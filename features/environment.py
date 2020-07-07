from configparser import ConfigParser
from core.help_function import get_browser


def before_scenario(context, scenario):
    config = ConfigParser()
    config.read('behave.ini')
    # browser = config.get('behave', 'browser')
    context.headless = config.getboolean('behave', 'headless')
    context.path_db = config.get('behave', 'stocks_db')
    path_chromedriver = config.get('behave', 'path_chromedriver')
    path_geckodriver = config.get('behave', 'path_geckodriver')
    path_firefox_binary = config.get('behave', 'path_firefox_binary')
    context.driver_paths = {'chrome': path_chromedriver,
                            'firefox': path_geckodriver,
                            'path_firefox_binary': path_firefox_binary}
    # driver = get_browser(browser, headless, context.path_chromedriver)
    # context.driver = driver


def after_scenario(context, scenario):
    context.driver.quit()
