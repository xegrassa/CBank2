from behave import *
from core.pages import InvestingMainPage, RussianStocksPage
from selenium.webdriver.common.by import By
from core.help_function import convert_str_to_float
from core.storage import Storage, WebStorage, Stock
import os.path
from core.help_function import get_browser


@given('"{browser_name}" browser')
def step_impl(context, browser_name):
    context.driver = get_browser(browser_name=browser_name,
                                 headless=context.headless,
                                 driver_paths=context.driver_paths)
    context.investing_main_page = InvestingMainPage(context.driver)


@when('Открыть страницу Investing')
def step_impl(context):
    context.investing_main_page.go_to_main_page()
    context.investing_main_page.screenshot('screenshots/go_to_ru_investing.png')


@then('Открылась станица ru.investing')
def step_impl(context):
    assert context.investing_main_page.on_investing_main_page() is True


@when('Переходим на страницу русских акций')
def step_impl(context):
    context.russian_stocks_page = context.investing_main_page.go_to_russian_stocks_page()


@then('Открылась страница русских акций')
def step_impl(context):
    assert context.russian_stocks_page.on_russian_stocks_page() is True


@when('Собрать информацию о российских акциях, цена которых изменилась на "{percent}"%')
def step_impl(context, percent):
    context.percent = int(percent)
    storage = Storage(context.path_db)
    context.web_storage = WebStorage()
    context.russian_stocks_page.get_russian_stocks_table()
    stocks = context.russian_stocks_page.stocks
    # stocks = list(map(Stock, table.find_elements(By.TAG_NAME, 'tr')))


    for company in stocks:
        print(company)
        # web_name, web_price = company.get_name(), convert_str_to_float(company.get_last_price())
        # db_price = convert_str_to_float(storage.get_data(web_name))
        # company_percent_change = ((web_price - db_price) / db_price) * 100
        # if company_percent_change >= context.percent:
        #     context.web_storage.set_data(web_name, web_price)


@when('Создать отчет "{json_name}"')
def step_impl(context, json_name):
    context.json_name = json_name
    context.web_storage.create_report_json(f'report/{json_name}')


@then('"{report_file}" отчет создан')
def step_impl(context, report_file):
    assert os.path.exists(f'report/{report_file}')
