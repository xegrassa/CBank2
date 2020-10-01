import os
import threading
from queue import Queue, Empty

from behave import *
from selenium.common.exceptions import WebDriverException

from investing_parse import SCREENSHOT_DIR_PATH, REPORT_DIR_PATH
from investing_parse.core.help_function import BrowserCreator, \
    convert_str_to_float, get_data_json
from investing_parse.core.pages import InvestingMainPage
from investing_parse.core.storage import Storage


@given('Браузер')
def step_impl(context):
    context.browser_creator = BrowserCreator(browser_name=context.browser_name,
                                             headless=context.headless,
                                             firefox_binary_path=context.firefox_binary_path)


@when('Открыть страницу Investing')
def step_impl(context):
    browser = context.browser_creator.get_browser()
    context.investing_main_page = InvestingMainPage(browser)
    context.investing_main_page.go_to_main_page()

    screenshot_path = os.path.join(SCREENSHOT_DIR_PATH, context.feature_name, f'{context.scenario.name}.png')
    context.investing_main_page.screenshot(screenshot_path)


@then('Открылась станица ru.investing')
def step_impl(context):
    assert context.investing_main_page.on_investing_main_page() is True


@given('Браузер открытый на странице Investing')
def step_impl(context):
    context.execute_steps('''
            given Браузер
            when Открыть страницу Investing
            then Открылась станица ru.investing
        ''')


@when('Переходим на страницу русских акций')
def step_impl(context):
    context.russian_stocks_page = context.investing_main_page.go_to_russian_stocks_page()


@then('Открылась страница русских акций')
def step_impl(context):
    assert context.russian_stocks_page.on_russian_stocks_page() is True


@when('Собрать информацию о российских акциях, цена которых изменилась на "{percent}"%')
def step_impl(context, percent):
    screenshot_path = os.path.join(SCREENSHOT_DIR_PATH, context.feature_name, f'{context.scenario.name}.png')
    context.russian_stocks_page.screenshot(screenshot_path)
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


@given('Список компаний цена которых изменилась на определенный процент')
def step_impl(context):
    path_to_report_json = os.path.join(REPORT_DIR_PATH, 'report.json')
    context.companies = get_data_json(path_to_report_json).keys()


@when('Парсинг дивидендов компаний в 4 потока')
def step_impl(context):
    max_thread = 4
    context.web_storage = Storage()
    company_queue = Queue()
    for company_name in context.companies:
        company_queue.put(company_name)
    while True:
        if threading.active_count() - 1 < max_thread:
            try:
                company = company_queue.get(timeout=5)
                print('Взяли из очереди ', company)
                print('Кол-во потоков', threading.active_count() - 1)
                p = threading.Thread(target=context.execute_steps,
                                     daemon=True,
                                     args=(f'when Получить дивиденды у компании "{company}"',)
                                     )
                p.start()
            except Empty:
                break
    for thread in threading.enumerate():
        if thread is not threading.main_thread():
            thread.join()


@when('Получить дивиденды у компании "{company_name}"')
def step_impl(context, company_name):
    browser = context.browser_creator.get_browser()
    investing_main_page = InvestingMainPage(browser)
    max_fails, fails = 4, 0
    while True:
        if fails > max_fails:
            print(f'Кол-во ошибок превышено. Компания {company_name} не будет спарсена')
            context.web_storage.set_data(company_name, None)
            break
        try:
            investing_main_page.go_to_main_page()
            russian_stock_page = investing_main_page.go_to_russian_stocks_page()
            company_page = russian_stock_page.go_to_company(company_name)
            dividend = company_page.get_dividend()
            context.web_storage.set_data(company_name, dividend)
            break
        except WebDriverException as e:
            print('WebDriverException у {}. {}/{} ошибка'.format(company_name, fails, max_fails))
            fails += 1
            continue
    company_page.close()
