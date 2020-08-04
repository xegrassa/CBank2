from configparser import ConfigParser
import os.path
import os


def before_scenario(context, scenario):
    config = ConfigParser()
    config.read('behave.ini')
    context.headless = config.getboolean('behave', 'headless')
    context.path_db = os.path.join(os.getcwd(), 'stocks')
    path_chromedriver = os.path.join(os.getcwd(), 'browser_webdriver', 'chromedriver.exe')
    path_geckodriver = os.path.join(os.getcwd(), 'browser_webdriver', 'geckodriver.exe')
    path_firefox_binary = config.get('behave', 'path_firefox_binary')
    context.driver_paths = {'chrome': path_chromedriver,
                            'firefox': path_geckodriver,
                            'path_firefox_binary': path_firefox_binary}


def after_scenario(context, scenario):
    context.driver.quit()
