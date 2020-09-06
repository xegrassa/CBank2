import os

from behave import *

from investing_parse import REPORT_DIR_PATH
from investing_parse.core.help_function import get_data_json
from investing_parse.core.parse_company_dividend import parse_dividends


@given('Список компаний')
def step_impl(context):
    path_to_report_json = os.path.join(REPORT_DIR_PATH, 'report.json')
    context.companies = get_data_json(path_to_report_json).keys()


@when('Парсинг дивидендов компаний')
def step_impl(context):
    context.web_storage = parse_dividends(context.companies, context.browser_creator)
