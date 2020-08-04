from core.pages import InvestingMainPage
import threading
from queue import Queue
from core.help_function import get_data_json
from core.help_function import get_browser
from core.storage import WebStorage
import os.path


class ParseDividentThread(threading.Thread):
    def __init__(self, queue, browser_option, storage):
        threading.Thread.__init__(self)
        self.browser_option = browser_option
        self.queue = queue
        self.driver = None
        self.storage = storage

    def run(self):
        while True:
            company_name = self.queue.get()
            self.parse_divident(company_name)
            self.queue.task_done()

    def parse_divident(self, company_name):
        self.driver = get_browser(*self.browser_option)

        while True:
            investing_main_page = InvestingMainPage(self.driver)
            try:
                investing_main_page.go_to_main_page()
                russian_stock_page = investing_main_page.go_to_russian_stocks_page()
                company_page = russian_stock_page.go_to_company(company_name)
                divident = company_page.get_divident()
            except:
                print(company_name, ' не вышло спарсить')
                continue
            else:
                self.storage.set_data(company_name, divident)
                company_page.close()
                break


def parse_divident(browser_params):
    web_storage = WebStorage()
    queue = Queue()
    for _ in range(4):
        t = ParseDividentThread(queue, browser_params, web_storage)
        t.setDaemon(True)
        t.start()

    companies = get_data_json(r'C:\Users\Admin\PycharmProjects\BANK_zadanie_2\report\report.json')
    for company_name in companies.keys():
        queue.put(company_name)
    queue.join()
    web_storage.create_report_json(r'C:\Users\Admin\PycharmProjects\BANK_zadanie_2\report\dividend.json')


if __name__ == '__main__':
    PATH_CHROME_DRIVER = r'C:\Users\Admin\PycharmProjects\BANK_zadanie_2\browser_webdrver\chromedriver.exe'
    args = ('chrome', {'chrome': PATH_CHROME_DRIVER})
    parse_divident(args)
