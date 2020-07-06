from core.storage import Web_storage, Storage
from core.investing_page import SearchHelper, Stock
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

PATH_TO_DB = '../stocks'
PATH_CHROME_DRIVER = '../browser_webdrver/chromedriver.exe'
PERCENTAGE_CHANGE = 5
driver = webdriver.Chrome(PATH_CHROME_DRIVER)


def convert_str_to_float(string: str) -> float:
    return float(string.replace('.', '').replace(',', '.'))


def main():
    app = SearchHelper(driver)
    try:
        app.go_to_site()
    except TimeoutException:
        print('Таймаут соединения, попытка рефреша')
        app.refresh()
    app.move_on_page_russian_stocks()
    table_stocks = app.get_russian_stocks()
    stocks = list(map(Stock, table_stocks))
    storage = Storage(PATH_TO_DB)
    web_storage = Web_storage()
    for stock in stocks:
        web_name, web_price = stock.get_name(), convert_str_to_float(stock.get_last_price())
        db_price = convert_str_to_float(storage.get_data(web_name))
        percent_change = ((web_price - db_price) / db_price) * 100
        if percent_change >= PERCENTAGE_CHANGE:
            web_storage.set_data(web_name, web_price)
    web_storage.create_report_json('report.json')
    app.driver.quit()


if __name__ == '__main__':
    main()
