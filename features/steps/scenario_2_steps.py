from behave import *
from core.help_function import get_data_json
from core.parse_company_dividend import parse_divident
import os


@given('Список компаний')
def step_impl(context):
    path_to_report_json = os.path.join(os.getcwd(), 'report', 'report.json')
    context.companies = get_data_json(path_to_report_json).keys()


@when('Парсинг дивидендов компаний')
def step_impl(context):
    context.web_storage = parse_divident(context.companies, context.browser)
