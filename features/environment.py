from configparser import ConfigParser
import os.path
import os


def before_scenario(context, scenario):
    config = ConfigParser()
    config.read('behave.ini')
    context.firefox_binary_path = config.get('behave', 'firefox_binary_path')
    context.headless = config.getboolean('behave', 'headless')
    context.path_db = os.path.join(os.getcwd(), 'stocks')
    context.driver = None


def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()
