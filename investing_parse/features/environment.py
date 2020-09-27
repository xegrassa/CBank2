import os.path
from configparser import ConfigParser

from investing_parse import SCREENSHOT_DIR_PATH
from investing_parse.core.help_function import get_feature_name


def before_scenario(context, scenario):
    print(scenario.name)


def before_feature(context, scenario):
    context.feature_name = get_feature_name(context)
    try:
        os.mkdir(os.path.join(SCREENSHOT_DIR_PATH, context.feature_name))
    except FileExistsError:
        pass

    config = ConfigParser()
    config.read(os.path.join('investing_parse', 'behave.ini'))
    context.browser_name = config.get('behave', 'browser')
    context.headless = config.getboolean('behave', 'headless')
    context.firefox_binary_path = config.get('behave', 'firefox_binary_path')

    context.path_db = os.path.join(os.getcwd(), 'investing_parse', 'stocks')
