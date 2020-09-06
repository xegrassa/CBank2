import os.path

from behave import *

from investing_parse import REPORT_DIR_PATH, SCREENSHOT_DIR_PATH
from investing_parse.core.help_function import BrowserCreator
from investing_parse.core.help_function import convert_str_to_float
from investing_parse.core.pages import InvestingMainPage
from investing_parse.core.storage import Storage


@given('"{browser_name}" браузер')
def step_impl(context, browser_name):
    context.browser_creator = BrowserCreator(browser_name=browser_name,
                                             headless=context.headless,
                                             firefox_binary_path=context.firefox_binary_path)


@when('Открыть страницу Investing')
def step_impl(context):
    browser = context.browser_creator.get_browser()
    screenshot_path = os.path.join(SCREENSHOT_DIR_PATH,
                                   'go_to_ru_investing.png')
    context.investing_main_page = InvestingMainPage(browser)
    context.investing_main_page.go_to_main_page()
    context.investing_main_page.screenshot(screenshot_path)


@then('Открылась станица ru.investing')
def step_impl(context):
    assert context.investing_main_page.on_investing_main_page() is True


@when('Переходим на страницу русских акций')
def step_impl(context):
    context.russian_stocks_page = context.investing_main_page.go_to_russian_stocks_page()


@then('Открылась страница русских акций')
def step_impl(context):
    assert context.russian_stocks_page.on_russian_stocks_page() is True
    screenshot_path = os.path.join(SCREENSHOT_DIR_PATH, 'investing_russian_stock.png')
    context.russian_stocks_page.screenshot(screenshot_path)


@when('Собрать информацию о российских акциях, цена которых изменилась на "{percent}"%')
def step_impl(context, percent):
    context.percent = int(percent)
    context.web_storage = Storage()

    db_storage = Storage(context.path_db)
    stocks = context.russian_stocks_page.get_russian_stocks()
    for company_stock in stocks:
        company_name, company_price = company_stock.get_name(), company_stock.get_last_price()
        db_company_price = convert_str_to_float(db_storage.get_data(company_name))
        company_percent_change = ((company_price - db_company_price) / db_company_price) * 100
        if company_percent_change >= context.percent:
            context.web_storage.set_data(key=company_name, value=company_price)


@when('Создать отчет "{json_name}"')
def step_impl(context, json_name):
    context.report_path = os.path.join(REPORT_DIR_PATH, json_name)
    context.web_storage.create_report(context.report_path)


@then('Отчет создан')
def step_impl(context):
    assert os.path.exists(context.report_path)
