from behave import *
from core.pages import MainPageInvesting, Stock
from selenium.webdriver.common.by import By
from core.help_function import convert_str_to_float, get_data_json
from core.storage import Storage, Web_storage
from core.parse_company_dividend import parse_divident
import multiprocessing.dummy as multiprocessing
import os.path
from core.help_function import get_browser


@given('"{browser_name}" browser')
def step_impl(context, browser_name):
    context.driver = get_browser(browser_name=browser_name,
                                 headless=context.headless,
                                 driver_paths=context.driver_paths)
    context.app = MainPageInvesting(context.driver)


@given('"{path_to_report_json}"')
def step_impl(context, path_to_report_json):
    context.json_data = get_data_json(path_to_report_json)


@when('run 4 parallel parse company dividend')
def step_impl(context):
    p = multiprocessing.Pool(processes=4)
    results = p.map(parse_divident, context.json_data)
    p.close()
    p.join()
    web_storage = Web_storage()
    for name, divident in results:
        web_storage.set_data(name, divident)
    web_storage.create_report_json(path_report='report/dividend.json')


@when('go to "{url}"')
def step_impl(context, url):
    context.app.go_to_site(url)
    context.app.screenshot('screenshots/go_to_ru_investing.png')


@then('opened page ru.investing')
def step_impl(context):
    assert context.app.on_site_investing() is True


@when('go to menu markets')
def step_impl(context):
    context.app.move_on_markets()
    context.app.screenshot('screenshots/main_page_menu_markets.png')


@when('go to menu stocks')
def step_impl(context):
    context.app.move_on_stocks()
    context.app.screenshot('screenshots/main_page_menu_markets_stocks.png')


@when('go to menu russian')
def step_impl(context):
    context.app.move_on_russian()
    context.app.screenshot('screenshots/main_page_menu_markets_stocks_russian.png')


@when('click')
def step_impl(context):
    context.app.click()


@then('opened page russian stocks')
def step_impl(context):
    assert context.app.on_page_russian_stocks() is True


@when('from stocks table, get stock whose price changed on "{percent}" percent')
def step_impl(context, percent):
    context.percent = int(percent)
    storage = Storage(context.path_db)
    context.web_storage = Web_storage()
    table = context.app.get_russian_stocks_table()
    stocks = list(map(Stock, table.find_elements(By.TAG_NAME, 'tr')))
    for company in stocks:
        web_name, web_price = company.get_name(), convert_str_to_float(company.get_last_price())
        db_price = convert_str_to_float(storage.get_data(web_name))
        company_percent_change = ((web_price - db_price) / db_price) * 100
        if company_percent_change >= context.percent:
            context.web_storage.set_data(web_name, web_price)


@when('create "{json_name}"')
def step_impl(context, json_name):
    context.json_name = json_name
    context.web_storage.create_report_json(f'report/{json_name}')


@then('"{report_file}" file created')
def step_impl(context, report_file):
    assert os.path.exists(f'report/{report_file}')
