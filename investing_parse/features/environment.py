import os.path
from configparser import ConfigParser

from investing_parse.core.help_function import get_feature_name


def before_scenario(context, scenario):
    config = ConfigParser()
    config.read(os.path.join('investing_parse', 'behave.ini'))
    context.firefox_binary_path = config.get('behave', 'firefox_binary_path')
    context.headless = config.getboolean('behave', 'headless')
    context.path_db = os.path.join(os.getcwd(), 'investing_parse', 'stocks')
    print(scenario.name)


def before_feature(context, scenario):
    context.feature_name = get_feature_name(context)
