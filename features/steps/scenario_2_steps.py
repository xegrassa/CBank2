from behave import *
from core.help_function import get_data_json
from core.storage import WebStorage
from core.parse_company_dividend import parse_divident
import multiprocessing.dummy as multiprocessing


@when('run 4 parallel parse company dividend')
def step_impl(context):
    p = multiprocessing.Pool(processes=4)
    results = p.map(parse_divident, context.json_data)
    p.close()
    p.join()
    web_storage = WebStorage()
    for name, divident in results:
        web_storage.set_data(name, divident)
    web_storage.create_report_json(path_report='report/dividend.json')


@given('"{path_to_report_json}"')
def step_impl(context, path_to_report_json):
    context.json_data = get_data_json(path_to_report_json)
